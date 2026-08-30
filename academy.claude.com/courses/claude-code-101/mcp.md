<!-- source: https://academy.claude.com/courses/claude-code-101/mcp -->

Lesson 11 of 12 · Claude Code 101MCP

3. /[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

# MCP

Lesson 116 min

MCP

SummaryTranscript

Model Context Protocol (MCP) is an open standard that lets Claude Code
connect to external tools and data sources. When you ask a question, Claude
automatically understands when it should use those tools to better handle
your query.

A lot of your context lives outside your codebase — in databases, productivity apps, or public repositories. MCP bridges that gap.

## What Can You Do With It?[](#what-can-you-do-with-it)

First, it's important to understand the concept of "tools" in agentic AI. Tools give agents like Claude Code the ability to perform actions that help them complete tasks more effectively. This is different from typical AI, where you just get a text response back.

For example, if your team uses Linear for project management, you can add a Linear MCP server to bring in the details of your specific issues. If you need up-to-date documentation for a dependency, a docs MCP server like Context7 can provide that to Claude Code.

![Claude Code querying a Linear MCP server to retrieve issue details for ticket MEN-12](https://academy.claude.com/assets/media/8b45d337d7061da8f40d66261dede8996ae317467c47f5224bc14a95d7549f54.jpg)

![Claude Code using the Context7 MCP server to look up the latest shadcn/ui documentation](https://academy.claude.com/assets/media/d6d21d5d4f27b7b129d16d21e8578d2d754778562751293844160576ab26f545.jpg)

## Adding an MCP Server[](#adding-an-mcp-server)

You can add MCP servers with the `claude mcp add` command. There are two main types:

![Running claude mcp add to add an HTTP Linear MCP server from the terminal](https://academy.claude.com/assets/media/2e38357f8b365758bc4d9d96a290c1acd8eafc93f673a38d40738b499bd9453b.jpg)

* **HTTP servers** are for remote services. These are hosted by the service provider and connect over the network.
* **Stdio servers** are for local processes that run on your machine.

![Running claude mcp add to add a local stdio MCP server with a Python script](https://academy.claude.com/assets/media/a19228083bd37109bd90468a8d18342a091bc905273c3b5aa4184804b4b1e68c.jpg)

You can manage your servers with `/mcp` inside a Claude Code session to see what's connected, check status, and disable servers you don't need.

![The /mcp command showing connected MCP servers and their status](https://academy.claude.com/assets/media/ad513f212c47b68feec4010cd6d1c2b348d5a1ed94ea1da993e0454d3bf08159.jpg)

## Scoping Servers[](#scoping-servers)

MCP servers can be scoped in three ways:

1. **Local** — only available in the current project, just for you.
2. **User** — available across all your projects.
3. **Project** — uses a `.mcp.json` file that you check into version control so anyone on the codebase gets the exact same servers automatically.

## Context Costs[](#context-costs)

MCP servers add tool definitions to your context window — even when you're not actively using them. If you have a lot of servers configured, this eats into your available context. Run `/mcp` to see what's connected and disable anything you're not actively using.

![The /mcp server detail view with options to view tools, reconnect, or disable a server](https://academy.claude.com/assets/media/f536fa89801900377bb63a689ae8e23c9b3b57a60c08dd04fef92e3fce3bf756.jpg)

If a tool has a CLI equivalent (like `gh` for GitHub or `aws` for AWS), the CLI is more context-efficient because it doesn't add persistent tool definitions.

You might also benefit from using a **Skill** instead. A Skill has a name and description loaded into context, and Claude only loads the full skill contents when it determines it needs to use it.

If your MCP tools exceed 10% of your context window, Claude Code automatically switches to tool search mode, which discovers the right tools on demand — though this may not work as reliably.

## Recap[](#recap)

MCP connects Claude Code to your external tools and data sources. Add servers with `claude mcp add`. Scope them to your project with `.mcp.json` so your team gets them automatically. And keep an eye on context usage by disabling servers you're not actively using.

[Previous lessonSkills](https://academy.claude.com/courses/claude-code-101/skills)[Next lessonHooks](https://academy.claude.com/courses/claude-code-101/hooks)

Lesson 11 of 12 · Claude Code 101MCP

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

* [What Can You Do With It?](#what-can-you-do-with-it)
* [Adding an MCP Server](#adding-an-mcp-server)
* [Scoping Servers](#scoping-servers)
* [Context Costs](#context-costs)
* [Recap](#recap)
