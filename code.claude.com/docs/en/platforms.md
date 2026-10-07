<!-- source: https://code.claude.com/docs/en/platforms -->

# Platforms and integrations

> Choose where to run Claude Code and what to connect it to. Compare the CLI, Desktop, VS Code, JetBrains, web, mobile, and integrations like Chrome, Slack, and CI/CD.

Claude Code runs the same underlying engine everywhere, but each surface is tuned for a different way of working. This page helps you pick the right platform for your workflow and connect the tools you already use.

## Where to run Claude Code

Choose a platform based on how you like to work and where your project lives.

| Platform | Best for | What you get |
| :- | :- | :- |
| [CLI](https://code.claude.com/docs/en/quickstart) | Terminal workflows, scripting, remote servers | Full feature set, [Agent SDK](https://code.claude.com/docs/en/headless), [computer use](https://code.claude.com/docs/en/computer-use) on macOS (Pro and Max), third-party providers |
| [Desktop](https://code.claude.com/docs/en/desktop) | Visual review, parallel sessions, managed setup | Diff viewer, app preview, [computer use](https://code.claude.com/docs/en/desktop#let-claude-use-your-computer) and [Dispatch](https://code.claude.com/docs/en/desktop#sessions-from-dispatch) on Pro and Max |
| [VS Code](https://code.claude.com/docs/en/vs-code) | Working inside VS Code without switching to a terminal | Inline diffs, integrated terminal, file context |
| [JetBrains](https://code.claude.com/docs/en/jetbrains) | Working inside IntelliJ, PyCharm, WebStorm, or other JetBrains IDEs | Diff viewer, selection sharing, terminal session |
| [Web](https://code.claude.com/docs/en/claude-code-on-the-web) | Long-running tasks that don't need much steering, or work that should continue when you're offline | Cloud, Anthropic-managed by default; continues after you disconnect |
| [Mobile](https://code.claude.com/docs/en/mobile) | Starting and monitoring tasks while away from your computer | Cloud sessions from the Claude app for iOS and Android, [Remote Control](https://code.claude.com/docs/en/remote-control) for local sessions, [Dispatch](https://code.claude.com/docs/en/desktop#sessions-from-dispatch) to Desktop on Pro and Max |

The CLI is the most complete surface for terminal-native work: scripting and the Agent SDK are CLI-only. Third-party providers also work in [VS Code](https://code.claude.com/docs/en/vs-code#use-third-party-providers) and in [JetBrains](https://code.claude.com/docs/en/feature-availability#features-available-on-every-provider), which runs the CLI in your IDE's terminal. Enterprise [Desktop](https://code.claude.com/docs/en/desktop) deployments support Google Cloud's Agent Platform, and Desktop supports [gateway providers](https://code.claude.com/docs/en/llm-gateway-connect#desktop-app); for Amazon Bedrock or Microsoft Foundry, use the CLI or an IDE extension, or [Claude Desktop on 3P](https://claude.com/docs/third-party/claude-desktop/overview), which runs the Code tab on those providers. Desktop and the IDE extensions trade some CLI-only features for visual review and tighter editor integration. The web runs in the cloud, so tasks keep going after you disconnect. Mobile is a thin client into those same cloud sessions or into a local session via Remote Control, and can send tasks to Desktop with Dispatch.

You can mix surfaces on the same project. Configuration, project memory, and MCP servers are shared across the local surfaces.

## Connect your tools

Integrations let Claude work with services outside your codebase.

| Integration | What it does | Use it for |
| :- | :- | :- |
| [Chrome](https://code.claude.com/docs/en/chrome) | Controls your browser with your logged-in sessions | Testing web apps, filling forms, automating sites without an API |
| [GitHub Actions](https://code.claude.com/docs/en/github-actions) | Runs Claude in your CI pipeline | Automated PR reviews, issue triage, scheduled maintenance |
| [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd) | Same as GitHub Actions for GitLab | CI-driven automation on GitLab |
| [Code Review](https://code.claude.com/docs/en/code-review) | Reviews every PR automatically | Catching bugs before human review |
| [Slack](https://code.claude.com/docs/en/slack) | Responds to `@Claude` mentions in your channels, under your own account | Turning bug reports into pull requests from team chat on Pro and Max plans |
| [Claude Tag](https://claude.com/docs/claude-tag) | Runs `@Claude` as your organization's shared identity with admin-configured access | Shared team access on Team and Enterprise plans, instead of per-user Slack sessions |

For integrations not listed here, [MCP servers](https://code.claude.com/docs/en/mcp) and [connectors](https://code.claude.com/docs/en/desktop#connect-external-tools) let you connect almost anything: Linear, Notion, Google Drive, or your own internal APIs.

## Work when you are away from your terminal

Claude Code offers several ways to work when you're not at your terminal. They differ in what triggers the work, where Claude runs, and how much you need to set up.

| | Trigger | Claude runs on | Setup | Best for |
| :- | :- | :- | :- | :- |
| [Dispatch](https://code.claude.com/docs/en/desktop#sessions-from-dispatch) | Message a task from the Claude mobile app | Your machine (Desktop) | [Pair the mobile app with Desktop](https://support.claude.com/en/articles/13947068) | Delegating work while you're away, minimal setup |
| [Remote Control](https://code.claude.com/docs/en/remote-control) | Drive a running session from [claude.ai/code](https://claude.ai/code) or the Claude mobile app | Your machine (CLI, Desktop, or VS Code) | Run [`claude remote-control` or `/remote-control`](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session) | Steering in-progress work from another device |
| [Channels](https://code.claude.com/docs/en/channels) | Push events from a chat app like Telegram or Discord, or your own server | Your machine (CLI) | [Install a channel plugin](https://code.claude.com/docs/en/channels#quickstart) or [build your own](https://code.claude.com/docs/en/channels-reference) | Reacting to external events like CI failures or chat messages |
| [Slack](https://code.claude.com/docs/en/slack) | Mention `@Claude` in a team channel | Anthropic cloud | [Install the Slack app](https://code.claude.com/docs/en/slack#setting-up-claude-code-in-slack) with [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) enabled, on Pro and Max plans | PRs and reviews from team chat |
| [Self-hosted environments](https://code.claude.com/docs/en/self-hosted-environments) | Start a [cloud session](https://code.claude.com/docs/en/claude-code-on-the-web) and pick your organization's environment | Your organization's infrastructure | [Deploy runners](https://code.claude.com/docs/en/self-hosted-environments-quickstart), on Team and Enterprise plans | Cloud sessions that must run inside your network |
| [Scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks) | Set a schedule | [CLI](https://code.claude.com/docs/en/scheduled-tasks), [Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks), or [cloud](https://code.claude.com/docs/en/routines) | Pick a frequency | Recurring automation like daily reviews |

If you're not sure where to start, [install the CLI](https://code.claude.com/docs/en/quickstart) and run it in a project directory. If you'd rather not use a terminal, [Desktop](https://code.claude.com/docs/en/desktop-quickstart) gives you the same engine with a graphical interface.

## Related resources

### Platforms

* [CLI quickstart](https://code.claude.com/docs/en/quickstart): install and run your first command in the terminal
* [Desktop](https://code.claude.com/docs/en/desktop): visual diff review, parallel sessions, computer use, and Dispatch
* [VS Code](https://code.claude.com/docs/en/vs-code): the Claude Code extension inside your editor
* [JetBrains](https://code.claude.com/docs/en/jetbrains): the extension for IntelliJ, PyCharm, and other JetBrains IDEs
* [Web](https://code.claude.com/docs/en/claude-code-on-the-web): cloud sessions from your browser at claude.ai/code that keep running when you disconnect
* [Projects](https://code.claude.com/docs/en/claude-projects): one conversation where Claude coordinates many cloud sessions for a body of work and reports back
* [Mobile](https://code.claude.com/docs/en/mobile): the Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) for starting and monitoring tasks while away from your computer

### Integrations

* [Chrome](https://code.claude.com/docs/en/chrome): automate browser tasks with your logged-in sessions
* [Computer use](https://code.claude.com/docs/en/computer-use): let Claude open apps and control your screen on macOS
* [GitHub Actions](https://code.claude.com/docs/en/github-actions): run Claude in your CI pipeline
* [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd): the same for GitLab
* [Code Review](https://code.claude.com/docs/en/code-review): automatic review on every pull request
* [Slack](https://code.claude.com/docs/en/slack): send tasks from team chat and get PRs back, on Pro and Max plans
* [Claude Tag](https://claude.com/docs/claude-tag): run `@Claude` as your organization's shared identity on Team and Enterprise plans

### Remote access

* [Dispatch](https://code.claude.com/docs/en/desktop#sessions-from-dispatch): message a task from your phone and it can spawn a Desktop session
* [Remote Control](https://code.claude.com/docs/en/remote-control): drive a running session from your phone or browser
* [Channels](https://code.claude.com/docs/en/channels): push events from chat apps or your own servers into a session
* [Scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks): run prompts on a recurring schedule
