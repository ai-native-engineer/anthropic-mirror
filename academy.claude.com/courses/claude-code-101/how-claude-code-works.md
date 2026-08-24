<!-- source: https://academy.claude.com/courses/claude-code-101/how-claude-code-works -->

Lesson 2 of 12 · Claude Code 101How Claude Code works

Loading

How Claude Code works

Claude Code is different from typical chat applications. Understanding how
it works under the hood will help you use it more effectively.

## The Agentic Loop

Claude Code is best explained through the **agentic loop**:

1. You enter a prompt into Claude Code.
2. Claude gathers the context it needs by interacting with the model, which returns text or a tool call that Claude Code can execute.
3. It takes action — for example, editing a file or running a command.
4. It verifies the results and determines whether they achieve what your prompt set out to do.
5. If they do, Claude finishes and waits for the next prompt. If they don't, it loops back and tries again until the results are complete and verifiable.

Throughout this loop, you can add context, interrupt, or steer the model to help guide it toward your goal.

![Diagram of the agentic loop: Your prompt flows into the loop of Gather context, Take action, and Verify results, with the ability to interrupt, steer, or add context at any point](https://academy.claude.com/assets/media/141ad1329bacde1d351f9078f8b1aeafecea0340c110721031060f1b11ec46a1.jpg)

## Context

Claude has a **context window** that determines how much of your conversation, file contents, command outputs, and more it can store and reference. Once you reach that limit, Claude Code compacts your conversation — automatically determining what it can remove or summarize to bring the context window back down to a usable size.

## Tools

Tools are the backbone of how agents work. Most AI assistants simply take text in and return text out. Tools let Claude Code determine *when* to execute code to get closer to completing a task. This could be a file-reading tool, a web search tool, or any number of other capabilities. Claude Code uses semantic understanding to determine when to call a tool and how to use the output.

## Permissions

Claude Code has several permission modes:

* **Manual (the default):** Claude asks for explicit permission before editing a file or running a shell command.
* **Auto-accept:** Files are edited without asking, but commands still require approval.
* **Plan mode:** Uses read-only tools to compile a plan of action before starting any work.

![Claude Code asking for permission before running a bash command](https://academy.claude.com/assets/media/8d2d1170d15c7ba9eed77d9ec83eec23486de420931ab4901a67b771f9cbb4b7.jpg)

All of this can be configured in your settings file. Be cautious when skipping permissions — giving Claude Code free rein to run commands means a mistake could be harder to catch before it happens.

## Recap

Claude Code combines several agentic concepts: an agentic loop, a managed context window, tools, and configurable permissions — all inside your terminal. It can read your codebase, take action, and verify its own work. That's what makes it fundamentally different from a chat window.
