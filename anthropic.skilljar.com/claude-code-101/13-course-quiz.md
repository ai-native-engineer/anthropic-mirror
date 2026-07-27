<!-- https://anthropic.skilljar.com/claude-code-101/469849 -->

## About this course

AI coding agents are changing what it means to write software. Tasks that used to take an afternoon — tracing a bug across a large codebase, scaffolding a new service, reviewing a stack of pull requests — can now happen in a single focused session, with an agent that reads your code, runs your commands, and edits files alongside you. But getting real value from an agent requires more than installing it and typing a request. It requires understanding how the agent thinks, what context it has access to, and how to steer it when it heads in the wrong direction.

This course teaches developers how to use [Claude Code](https://claude.com/product/claude-code) effectively, whether you're new to software engineering or an experienced engineer who hasn't yet worked with AI coding agents. We start from first principles — what an agentic loop actually is, how the context window shapes what Claude can see, how tools and permissions determine what it can do — so that the techniques later in the course make sense rather than feeling like a list of tricks to memorize.

You'll learn how to install Claude Code across multiple environments (terminal, VS Code, JetBrains, Claude Desktop, and the web), and how to write prompts that get good results on the first try using approval mode, auto-accept, and Plan Mode. The core of the course is the Explore → Plan → Code → Commit workflow: a repeatable rhythm for breaking down a task, letting Claude propose an approach, reviewing the work as it happens, and landing it cleanly. We also cover code review with Claude Code and the context-management commands (`/compact`, `/clear`, `/context`) that keep long sessions productive.

The final section is about making Claude Code your own. You'll write a `CLAUDE.md` file so Claude remembers your project's conventions across sessions, build custom subagents and skills for tasks you repeat often, connect external systems through MCP servers, and write hooks that add deterministic guardrails around what Claude is allowed to do. By the end, you'll have a setup tailored to how you actually work — not a generic install.

#### Recommended prerequisites

Basic familiarity with a code editor and the command line. You'll also need a Claude account (Pro, Max, or Enterprise) or an API key. No prior experience with AI tools is assumed.

#### Who this is for

New developers entering software engineering who want AI-assisted workflows from the start, and experienced engineers curious about coding agents but who haven't taken the plunge yet. If you've tried a coding assistant before and found the results underwhelming, this course is designed to show you what changes when you work with an agent rather than against it.

## Course sections

### What is Claude Code?

2 lessons

Before you write your first prompt, it helps to know what's actually happening when Claude Code runs. This section explains what separates an AI coding agent from a chat-based assistant, then walks through the agentic loop — gather context, take action, verify results — and the tools and permissions that govern each step. You'll come away with a mental model that makes everything in the rest of the course click.

Course preview images

![What is Claude Code? introduction video](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8vqsu7jt1fsbeepmjgbk7gzfi%2Fpublic%2F1775748058%2F01-01-medium.1775748058806.webp)

![Agentic loop diagram: gather context, take action, verify results](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8vqsu7jt1fsbeepmjgbk7gzfi%2Fpublic%2F1775748059%2F01-02-medium.1775748059276.webp)

### Your first prompt

2 lessons

Get Claude Code running wherever you already work — in the terminal, inside VS Code or JetBrains, in Claude Desktop, or on the web. Then write your first prompt and see how approval mode, auto-accept, and Plan Mode change the way Claude responds, so you can pick the right level of oversight for the task in front of you.

Course preview images

![Installing Claude Code from the terminal](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8vqsu7jt1fsbeepmjgbk7gzfi%2Fpublic%2F1775748060%2F02-01-medium.1775748060012.webp)

![Claude in Chrome browser extension](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8vqsu7jt1fsbeepmjgbk7gzfi%2Fpublic%2F1775748060%2F02-02-medium.1775748060468.webp)

### Daily workflows

3 lessons

This is where Claude Code becomes part of how you ship. Learn the Explore → Plan → Code → Commit rhythm for tackling real tasks, use the context-management commands to keep long sessions fast and focused, and put Claude to work reviewing code — your own and your teammates' — before it lands.

Course preview images

![Spawning a code-reviewer subagent in Claude Code](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8vqsu7jt1fsbeepmjgbk7gzfi%2Fpublic%2F1775748061%2F03-01-medium.1775748060923.webp)

### Customizing Claude Code

5 lessons

Out of the box, Claude Code is general-purpose. This section shows you how to make it yours: write a CLAUDE.md file so it remembers your project's conventions, build subagents and skills for the workflows you repeat, wire in external systems through MCP servers, and add hooks for deterministic guardrails. By the end you'll have a setup tuned to the way your team actually works.

Course preview images

![Editing a CLAUDE.md project memory file in VS Code](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8vqsu7jt1fsbeepmjgbk7gzfi%2Fpublic%2F1775748061%2F04-01-medium.1775748061356.webp)

![Connecting Claude Code to a Linear MCP server](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8vqsu7jt1fsbeepmjgbk7gzfi%2Fpublic%2F1775748061%2F04-02-medium.1775748061832.webp)

![Configuring hooks in .claude/settings.json](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8vqsu7jt1fsbeepmjgbk7gzfi%2Fpublic%2F1775748062%2F04-03-medium.1775748062359.webp)
