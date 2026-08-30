<!-- source: https://academy.claude.com/courses/claude-code-101/hooks -->

Lesson 12 of 12 · Claude Code 101Hooks

3. /[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

# Hooks

Lesson 126 min

Hooks

SummaryTranscript

Hooks let you run commands at specific points in Claude Code's lifecycle.
The key difference between hooks and everything else covered in this course
is that hooks are **deterministic** — they always run.

## Why Use Hooks[](#why-use-hooks)

You can tell Claude in your CLAUDE.md to run Prettier after every file edit. Most of the time it will. But sometimes it won't. A hook makes it happen every single time, no exceptions.

Common use cases include:

* Auto-formatting after file edits
* Logging all executed commands for compliance
* Blocking dangerous operations like modifying production files
* Sending yourself notifications when Claude finishes a task

## How They Work[](#how-they-work)

Hooks are configured in your `settings.json`. You pick an event, optionally set a matcher for which tools it applies to, and provide a command to run. Some of the most common events are:

* **PreToolUse** — runs before a tool call
* **PostToolUse** — runs after a tool call completes
* **UserPromptSubmit** — runs when you submit a prompt, before Claude processes it
* **Stop** — runs when Claude finishes responding
* **Notification** — runs when Claude sends a notification

These are just a few of the events you can hook into — Claude Code supports many more. See the [hooks reference(opens in new tab)](https://code.claude.com/docs/en/hooks) for the full list.

You configure them through the `/hooks` command inside Claude Code, or by editing `settings.json` directly.

![The settings.json file inside the .claude directory with hooks configuration](https://academy.claude.com/assets/media/de2ac2dab9f24bb445af53ec3f2dbb17f4399fb472247165532f814f350126d5.jpg)

## A Practical Example[](#a-practical-example)

The most common hook: auto-formatting after edits. Set a **PostToolUse** hook with a matcher of `"Edit|MultiEdit|Write"` so it fires whenever Claude modifies a file. The command checks the file extension and runs the appropriate formatter — Prettier for TypeScript, gofmt for Go, whatever your project uses.

## Blocking with PreToolUse[](#blocking-with-pretooluse)

PreToolUse hooks can **block tool calls** before they execute. Your hook receives the tool name and input as JSON on stdin. The exit code determines the behavior:

* **Exit code 0** — proceed normally.
* **Exit code 2** — block the action. The stderr message gets fed back to Claude as feedback so it knows why it was blocked and can adjust.
* **Any other exit code** — a non-blocking error that gets shown to you but doesn't stop anything.

This is how you enforce hard rules. Block writes to a production config directory. Block bash commands that contain `rm -rf`. Block commits to main. Whatever your team needs to be *guaranteed*, not suggested.

![A settings.json file showing PreToolUse and PostToolUse hooks with matchers and commands](https://academy.claude.com/assets/media/6749d1e1eb639dbc9d9532162c45f182aa63b60e4c6fc633e1d32f7780324234.jpg)

## Sharing Hooks with Your Team[](#sharing-hooks-with-your-team)

Hooks configured in `.claude/settings.json` are project-level and can be checked into your repo. This means your entire team gets the same hooks automatically. Use the `CLAUDE_PROJECT_DIR` environment variable in your commands to reference scripts stored in your project, so they work regardless of Claude's current working directory.

## Recap[](#recap)

Hooks give you deterministic control over Claude Code's behavior. Use PostToolUse for auto-formatting and logging. Use PreToolUse to block dangerous operations. Configure them with `/hooks` or in `settings.json`. And check them into your repo so your team gets them too.

If something needs to happen every time without fail, don't put it in a prompt. Put it in a hook.

[Previous lessonMCP](https://academy.claude.com/courses/claude-code-101/mcp)[Next lessonCourse quiz](https://academy.claude.com/courses/claude-code-101/course-quiz)

Lesson 12 of 12 · Claude Code 101Hooks

What is Claude Code?

* [What is Claude Code?](https://academy.claude.com/courses/claude-code-101/what-is-claude-code)
* [How Claude Code works](https://academy.claude.com/courses/claude-code-101/how-claude-code-works)

Your first prompt

* [Installing Claude Code](https://academy.claude.com/courses/claude-code-101/installing-claude-code)
* [Your first prompt](https://academy.claude.com/courses/claude-code-101/your-first-prompt)

Daily workflows

* [The explore → plan → code → commit workflow](https://academy.claude.com/courses/claude-code-101/the-explore-plan-code-commit-workflow)
* [Context management](https://academy.claude.com/courses/claude-code-101/context-management)
* [Code review](https://academy.claude.com/courses/claude-code-101/code-review)

Customizing Claude Code

* [The CLAUDE.md file](https://academy.claude.com/courses/claude-code-101/the-claude-md-file)
* [Subagents](https://academy.claude.com/courses/claude-code-101/subagents)
* [Skills](https://academy.claude.com/courses/claude-code-101/skills)
* [MCP](https://academy.claude.com/courses/claude-code-101/mcp)
* [Hooks](https://academy.claude.com/courses/claude-code-101/hooks)

Quiz

* [Course quizQuiz](https://academy.claude.com/courses/claude-code-101/course-quiz)

* [Completion badge](https://academy.claude.com/courses/claude-code-101/badge)

* [Why Use Hooks](#why-use-hooks)
* [How They Work](#how-they-work)
* [A Practical Example](#a-practical-example)
* [Blocking with PreToolUse](#blocking-with-pretooluse)
* [Sharing Hooks with Your Team](#sharing-hooks-with-your-team)
* [Recap](#recap)
