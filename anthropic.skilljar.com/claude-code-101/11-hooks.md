<!-- https://anthropic.skilljar.com/claude-code-101/469798 -->

### Video



### Hooks

Hooks let you run commands at specific points in Claude Code's lifecycle. The key difference between hooks and everything else covered in this course is that hooks are **deterministic** — they always run.

## Why Use Hooks

You can tell Claude in your CLAUDE.md to run Prettier after every file edit. Most of the time it will. But sometimes it won't. A hook makes it happen every single time, no exceptions.

Common use cases include:

* Auto-formatting after file edits
* Logging all executed commands for compliance
* Blocking dangerous operations like modifying production files
* Sending yourself notifications when Claude finishes a task

## How They Work

Hooks are configured in your `settings.json`. You pick an event, optionally set a matcher for which tools it applies to, and provide a command to run. The available events are:

* **PreToolUse** — runs before a tool call
* **PostToolUse** — runs after a tool call completes
* **UserPromptSubmit** — runs when you submit a prompt, before Claude processes it
* **Stop** — runs when Claude finishes responding
* **Notification** — runs when Claude sends a notification

You configure them through the `/hooks` command inside Claude Code, or by editing `settings.json` directly.

![The settings.json file inside the .claude directory with hooks configuration](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686375%2Fvideo11settingsjsonfile.1775686375582.jpg)

## A Practical Example

The most common hook: auto-formatting after edits. Set a **PostToolUse** hook with a matcher of `"Edit|MultiEdit|Write"` so it fires whenever Claude modifies a file. The command checks the file extension and runs the appropriate formatter — Prettier for TypeScript, gofmt for Go, whatever your project uses.

## Blocking with PreToolUse

PreToolUse hooks can **block tool calls** before they execute. Your hook receives the tool name and input as JSON on stdin. The exit code determines the behavior:

* **Exit code 0** — proceed normally.
* **Exit code 2** — block the action. The stderr message gets fed back to Claude as feedback so it knows why it was blocked and can adjust.
* **Any other exit code** — a non-blocking error that gets shown to you but doesn't stop anything.

This is how you enforce hard rules. Block writes to a production config directory. Block bash commands that contain `rm -rf`. Block commits to main. Whatever your team needs to be *guaranteed*, not suggested.

![A settings.json file showing PreToolUse and PostToolUse hooks with matchers and commands](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686375%2Fvideo11hooksblock.1775686375002.jpg)

## Sharing Hooks with Your Team

Hooks configured in `.claude/settings.json` are project-level and can be checked into your repo. This means your entire team gets the same hooks automatically. Use the `CLAUDE_PROJECT_DIR` environment variable in your commands to reference scripts stored in your project, so they work regardless of Claude's current working directory.

## Recap

Hooks give you deterministic control over Claude Code's behavior. Use PostToolUse for auto-formatting and logging. Use PreToolUse to block dangerous operations. Configure them with `/hooks` or in `settings.json`. And check them into your repo so your team gets them too.

If something needs to happen every time without fail, don't put it in a prompt. Put it in a hook.
<!-- youtube: IkaPHiMDazM -->

# Hooks

[![Hooks](https://img.youtube.com/vi/IkaPHiMDazM/hqdefault.jpg)](https://www.youtube.com/watch?v=IkaPHiMDazM)

<details>
<summary>자막: Hooks</summary>

Hooks let you run commands at different points in Claude code's life cycle. The key difference between hooks and everything else we covered is that hooks are deterministic. They always run. So, put it this way. You can tell Claude in your claude.md file to run prettier after every file edit and most of the time it will do that, but sometimes it won't. It's not perfect. But a hook makes it happen every single time with no exceptions. Common use cases could include auto formatting after file edits, logging all executed commands for compliance, blocking dangerous operations like modifying production files, and sending yourself notifications when Claude finishes a task. Hooks are configured in your settings.json file. You pick an event, optionally set a matcher for which tool it applies to, and provide a command to run. User prompt submit runs when you submit a prompt before Claude processes it. Pre-tool use which runs before a tool call. Post-tool use runs after a tool call completes. Notification runs when Claude sends a notification, and stop runs when Claude finishes responding. The most common hook. Auto formatting after edits. You set a post-tool use hook with a matcher of edit or multi-edit, right? So, it fires whenever Claude modifies a file. The command checks the file extension and runs the appropriate formatter. This could be prettier for TypeScript, Go format for Go, Ruff for Python, whatever your project uses. Pre-tool use hooks can block tool calls before they execute. So, your hook receives a tool name and input as JSON on stdin. If it exits with code two, the action is blocked and the stderr message gets fed back to Claude as feedback so Claude knows why it was blocked and can adjust. Exit code zero means proceed. Exit code two means block. This is how you enforce hard rules. Block writes to a production config directory, block bash commands that contain rm -rf, block commits to main, whatever your team needs to be guaranteed, not suggested. Hooks configured in .Claude/settings.json are project level and can be checked into your repo. This means that your entire team gets the same hooks automatically. Use the Claude project dir environment variable in your commands to reference scripts stored in your project so they work regardless of Claude's current working directory.
>> [music]
>> Hooks gives you deterministic control
over Claude code's behavior.
>> [music]
>> Use post-tool-use for auto-formatting
and logging. Use pre-tool-use to block dangerous operations. Configure them in the /hooks or in settings.json
>> [music]
>> and check them into your repository so
your team gets them, too. If something needs to happen every time without fail, don't put it in a prompt. Put it in a hook.
>> [music]

</details>
