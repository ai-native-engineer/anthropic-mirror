<!-- source: https://claude.com/docs/third-party/claude-desktop/chat -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

The Chat tab in Claude Desktop on third-party (3P) is a conversational surface for quick questions and drafting. Unlike the [Cowork](https://claude.com/docs/cowork/overview) and [Code](https://claude.com/docs/third-party/claude-desktop/code) tabs, which run agentic sessions with access to folders you grant and a code-execution environment, a Chat conversation runs with a deliberately small tool surface: it can search and fetch the web under your admin configuration, read files attached to the conversation, and write files into a scratch space of its own, and nothing else on the machine. The Chat tab is off by default and is enabled with a single configuration key.
Like everything else in 3P mode, Chat conversations run against your configured inference provider, and conversation history lives on the user’s device. See [User identity and local data](https://claude.com/docs/third-party/claude-desktop/data-storage#chat-conversations) for exactly what is written where and what can leave the device.

##  What a Chat conversation can reach

| Capability | Scope |
| --- | --- |
| Web search | Same options and rules as the other tabs; depends on your provider or a configured search server. See [Web search](https://claude.com/docs/third-party/claude-desktop/web-tools#web-search). |
| Web fetch | Runs in the app on the device, never inside a sandbox. Every fetch is checked against `coworkEgressAllowedHosts`; with no allowlist configured, fetch is disabled. See [Web fetch](https://claude.com/docs/third-party/claude-desktop/web-tools#web-fetch). |
| Attached files | Read-only access to files the user attaches to the conversation. Each attachment is copied or hard-linked into the conversation’s local uploads directory; Claude cannot reach anything else on disk. |
| Scratch directory | A per-conversation working directory where Claude can create and edit files (documents, data files, HTML artifacts) and offer them to the user for download or preview. |
| Managed MCP servers | The servers you provision via [`managedMcpServers`](https://claude.com/docs/third-party/claude-desktop/configuration#managedmcpservers) are available in Chat with the same approval model as the other tabs: a tool’s `toolPolicy` of `"allow"` pre-approves it, `"blocked"` blocks it, and `"ask"` requires user approval on every call. A tool with no policy asks the user, who can allow it once or grant standing approval, as in the other tabs. |
| Clarifying questions | Claude can present multiple-choice questions to the user (the `AskUserQuestion` tool). |
| Code execution | Off by default. When you enable [advanced file analysis](#advanced-file-analysis), Claude can additionally run code in an offline local sandbox against attached files. |

`disabledBuiltinTools` and `builtinToolPolicy` apply in Chat the same way they do in the other tabs. For example, adding `"WebFetch"` removes web fetch from Chat conversations too.

##  What a Chat conversation cannot do

In a Chat conversation, Claude cannot:

* **Read or write the filesystem** beyond the conversation’s own uploads and scratch directories. Chat conversations never receive folder access: the tool for requesting folder access is removed, and the app refuses folder grants to a Chat conversation even when requested through internal interfaces.
* **Run code on the host.** There is no shell access. With advanced file analysis off (the default), the sandbox VM is never started for Chat; with it on, code runs only inside the offline sandbox described below, never on the host itself.
* **Act without asking.** Chat conversations always run in the default permission mode. Auto mode and other reduced-supervision modes are rejected for Chat regardless of `autoModeEnabled`.
* **Create or run scheduled tasks**, or list the ones that exist.
* **Escalate into an agentic session.** The tools that launch Code sessions or dispatch background agent tasks are removed. When a request needs capabilities Chat doesn’t have, Claude says so and suggests starting the task in Cowork instead.
* **Read other conversations.** The tools that list sessions or read other sessions’ transcripts are removed, so a Chat conversation cannot search or quote your other chats, Cowork sessions, or Code sessions.
* **Use or write memory.** Chat conversations neither read nor write the local [memory](https://claude.com/docs/third-party/claude-desktop/data-storage#memory) that Cowork sessions maintain.

These restrictions are enforced in the app’s main process, not just hidden in the UI.

##  Advanced file analysis

By default, Chat can read attached files only in the formats Claude understands natively. Setting `chatAdvancedFileAnalysisEnabled` to `true` lets Claude also run code against attachments. This is useful for spreadsheets, PowerPoint files, and other formats that need parsing, and for inline data analysis on attached data.
The execution environment is intentionally narrower than the Cowork sandbox:

* Code runs in the same isolated local VM that Cowork uses. For Chat, the VM starts only when analysis is coming: on the first analysis call, or at the start of a turn with files attached.
* The sandbox has **no network access**. This is unconditional for Chat and independent of `coworkEgressAllowedHosts`: an allowlist that opens egress for Cowork sessions does not open it for Chat analysis.
* The only conversation data the sandbox sees is the conversation’s attached files (read-only) and its scratch directory (writable), plus read-only reference material bundled by the app. No user folders, no memory, no other sessions’ data.
* Each command runs independently; results land in the scratch directory, where Claude can offer them to the user as downloads or artifacts.

The data flow end to end: an attached file is copied into the conversation’s local uploads directory, mounted read-only into the sandbox when analysis runs, and any outputs are written to the conversation’s scratch directory on local disk. File content leaves the device only as conversation context sent to your configured inference provider, in web search queries to your configured search backend, through web fetches your egress allowlist permits, in a connector tool call permitted by your `toolPolicy` configuration and the user’s approvals, or, if you have enabled [content capture](https://claude.com/docs/third-party/claude-desktop/telemetry#content-capture), in telemetry to your own collector.

Advanced file analysis uses the same shell tool as Cowork’s sandbox, so adding `"Bash"` to `disabledBuiltinTools` disables it even when `chatAdvancedFileAnalysisEnabled` is `true`. Running it requires the sandbox VM bundle, which the app downloads from Anthropic unless you deployed the offline installer (see [required egress paths](https://claude.com/docs/third-party/claude-desktop/telemetry#required-egress-paths)).

##  Configuration

| Key | Default | Effect |
| --- | --- | --- |
| [`chatTabEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chattabenabled) | off | Shows the Chat tab. Chat is opt-in: the tab appears only when this key is explicitly `true`. |
| [`chatAdvancedFileAnalysisEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#chatadvancedfileanalysisenabled) | off | Allows code execution on attached files in the offline sandbox, as described above. Has no effect unless the Chat tab is enabled. |

Enforcement of `chatTabEnabled` happens in the app’s main process: when the key is unset or `false`, the tab is hidden, and the app additionally refuses to start or continue a Chat conversation, including conversations created before an admin turned the key off.
The rule that at least one surface must stay enabled counts the Chat tab only when `chatTabEnabled` is explicitly `true`: a configuration that disables the Cowork and Code tabs without enabling Chat re-enables the Cowork tab with a validation warning, rather than leaving users with an empty app. With `chatTabEnabled` set to `true`, a chat-only configuration is valid.

##  Where Chat data lives

Chat conversations are stored on the local device, in the same per-session layout as Cowork sessions: conversation history, attachment copies, scratch outputs, and a tamper-evident audit log, all under the application-data directory. Nothing is synced to a server, and there is no server-side index of past conversations. See [Chat conversations](https://claude.com/docs/third-party/claude-desktop/data-storage#chat-conversations) on the data-storage page for the breakdown.
