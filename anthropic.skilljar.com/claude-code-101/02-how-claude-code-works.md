<!-- https://anthropic.skilljar.com/claude-code-101/469789 -->

### Video



### How Claude Code Works

Claude Code is different from typical chat applications. Understanding how it works under the hood will help you use it more effectively.

## The Agentic Loop

Claude Code is best explained through the **agentic loop**:

1. You enter a prompt into Claude Code.
2. Claude gathers the context it needs by interacting with the model, which returns text or a tool call that Claude Code can execute.
3. It takes action — for example, editing a file or running a command.
4. It verifies the results and determines whether they achieve what your prompt set out to do.
5. If they do, Claude finishes and waits for the next prompt. If they don't, it loops back and tries again until the results are complete and verifiable.

Throughout this loop, you can add context, interrupt, or steer the model to help guide it toward your goal.

![Diagram of the agentic loop: Your prompt flows into the loop of Gather context, Take action, and Verify results, with the ability to interrupt, steer, or add context at any point](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686365%2Fagenticloop.1775686365141.jpg)

## Context

Claude has a **context window** that determines how much of your conversation, file contents, command outputs, and more it can store and reference. Once you reach that limit, Claude Code compacts your conversation — automatically determining what it can remove or summarize to bring the context window back down to a usable size.

## Tools

Tools are the backbone of how agents work. Most AI assistants simply take text in and return text out. Tools let Claude Code determine *when* to execute code to get closer to completing a task. This could be a file-reading tool, a web search tool, or any number of other capabilities. Claude Code uses semantic understanding to determine when to call a tool and how to use the output.

## Permissions

Claude Code has several permission modes:

* **Default behavior:** Claude asks for explicit permission before editing a file or running a shell command.
* **Auto-accept:** Files are edited without asking, but commands still require approval.
* **Plan mode:** Uses read-only tools to compile a plan of action before starting any work.

![Claude Code asking for permission before running a bash command](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686376%2Fvideo2ask.1775686376586.jpg)

All of this can be configured in your settings file. Be cautious when skipping permissions — giving Claude Code free rein to run commands means a mistake could be harder to catch before it happens.

## Recap

Claude Code combines several agentic concepts: an agentic loop, a managed context window, tools, and configurable permissions — all inside your terminal. It can read your codebase, take action, and verify its own work. That's what makes it fundamentally different from a chat window.
<!-- youtube: 6bs5b4FltCU -->

# How Claude Code works

[![How Claude Code works](https://img.youtube.com/vi/6bs5b4FltCU/hqdefault.jpg)](https://www.youtube.com/watch?v=6bs5b4FltCU)

<details>
<summary>자막: How Claude Code works</summary>

We know that Claude code is different from usual chat applications, but how does it work? Claude code is best explained through the agentic loop. You enter a prompt into Claude code. Claude code will then gather contacts required to complete your prompt. It does so by interacting with the model which will return text or a tool call that Claude code can execute. Then it takes action. For example, editing a file or running a command. Finally, it verifies those results and determines if they achieve what your prompt set out to do in the first place. If they do, then Claude finishes and waits for the next prompt. And if they don't, Claude goes back and runs the loop again until the results are complete and verifiable. Throughout this loop, you're able to add contacts, interrupt it, or steer the model to help guide it towards your end goal. Claude has a context window, which determines how much of your conversation, file contents, command outputs, and more it can store and look back on. Once you reach that limit, Claude code compacts your conversation, which automatically determines what it can take out of the context window and what it can summarize in order to bring the context window back down. Tools are the backbone of how agents work. Currently, most AI assistants are simply input text and output text. Nothing in between. Tools let Claude code and other agents determine when to execute code to get closer to a task. This could be read file tool or search web tool, for example. Claude code uses semantic searching to determine when to call a tool and get the output of it. Claude code also has permission modes. Default behavior is that it has to ask explicit permission before editing a file or running a shell command. You can use shift and tab to toggle between different modes. Auto accept edits files without asking, but still ask for commands. Plan mode uses read-only tools to help compile a plan of action before starting. It's worth being cautious when skipping permissions. Giving Claude code free reign to run commands means a mistake could be harder to catch before even happens. Claude code works by combining different agentic concepts, an agentic loop, a managed context window, tools, and configurable permissions into your terminal. It can read your code base, take action, and verify its own work, and that makes it fundamentally different from a chat window.

</details>
