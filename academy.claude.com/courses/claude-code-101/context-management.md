<!-- source: https://academy.claude.com/courses/claude-code-101/context-management -->

Lesson 6 of 12 · Claude Code 101Context management

3. /[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

# Context management

Lesson 67 min

Context management

SummaryTranscript

Context is Claude's working memory. Every file it reads, every command it
runs, every message you send — it all takes up space in the context window.

## What is the Context Window?[](#what-is-the-context-window)

Think of the context window as the amount of space Claude can hold in its memory. Whenever you enter a prompt, Claude reads a file, runs a tool call, or receives a tool call result, it's all adding to the context window. Since there's a finite amount of space, it becomes important to optimize how you use it.

![Diagram showing the context window as a grid of tokens — some taken, most available](https://academy.claude.com/assets/media/0b452da83b5903a000236abfd55cc34f13f28dbfeb7e3acc9f6da07cdd78241e.jpg)

## What Happens When Context Fills Up[](#what-happens-when-context-fills-up)

When you approach the limit, the context window is automatically **compacted**. Compaction summarizes important details and removes unnecessary tool call results to free up space. Note that this process can potentially lose details.

![Claude Code showing 'Compacting conversation...' as it summarizes the context](https://academy.claude.com/assets/media/9511065cfe218d3894f551b9096b6eead92b74f5714126e6ccdd26e2d4a5f4a0.jpg)

![Claude Code displaying a compact summary of the previous conversation including key technical concepts and files](https://academy.claude.com/assets/media/a1539801b08e330701dc44e3361a079860d4586b1eff878237dff5ec28f39e64.jpg)

## Commands[](#commands)

You can run compaction manually with the `/compact` command. This compacts everything up to that point. It's handy when you want to free up context space while keeping a memory of what you previously worked on.

![The /compact command in Claude Code's autocomplete menu](https://academy.claude.com/assets/media/d348719608e1d100f9adaca481d43be6759a9d3e896b67de6054e8cf6591dfe5.jpg)

If you want to completely start from scratch with no memory of the previous session, run `/clear`. This removes everything.

![Running /clear in Claude Code to start a fresh session](https://academy.claude.com/assets/media/93098b21ae0152b1fbf763fd9e30ea76e4ada64966526203458bb0a83006851a.jpg)

To check the state of your context, run the `/context` command. You'll get a high-level overview of your context size, the categories taking up the most space, and a visual graphic showing the breakdown.

![Output of the /context command showing context usage breakdown with a visual bar chart](https://academy.claude.com/assets/media/d0b6a1d0ad4a21aa61a48751f2d382a77edc3fde154f8f5aebd2509ebc325420.jpg)

## When to Use Which[](#when-to-use-which)

A general rule of thumb:

* **Use `/compact`** when you're working on a specific feature and running up against the context limit but need to continue. Keeping the context relevant to your current feature is important.
* **Use `/clear`** when you want to start a new feature. You don't want the previous conversation to introduce bias into something new. For things you want Claude to remember across sessions, put them in your CLAUDE.md file so it doesn't have to rediscover things from scratch.

  ![A CLAUDE.md file with commands, important notes, and architecture sections](https://academy.claude.com/assets/media/c31ad4239bea62c006ae5d41ab0c60d0c0d2e89676ddeee440e139e1690c1f67.jpg)

## Tips for Saving Context Space[](#tips-for-saving-context-space)

**Be specific.** A vague prompt might seem smaller, but it actually costs more context in the long run. Without clear instructions, Claude is forced to explore your codebase more and do its own reasoning — which takes up far more context space than a detailed prompt would.

**Manage your MCP servers.** MCP servers load all of their available tools into context by default, even when you're not using them. If you have servers configured for things unrelated to the current project, consider turning them off. You can also try "Skills," which work similarly to MCP servers but don't load everything into context upfront.

**Use subagents.** Subagents run in parallel with your main agent but have a completely separate context window. For tasks where you only need the answer — like "where are the authentication endpoints located?" — a subagent does the work and returns just a summary to your main agent, keeping your primary context clean.

## Recap[](#recap)

Managing context within Claude Code is crucial. Use `/compact` to summarize long sessions and `/clear` to start fresh. To use your context window effectively: be specific with your prompts, check what's consuming your current context, and use subagents to delegate tasks where you only need the result.

[Previous lessonThe explore → plan → code → commit workflow](https://academy.claude.com/courses/claude-code-101/the-explore-plan-code-commit-workflow)[Next lessonCode review](https://academy.claude.com/courses/claude-code-101/code-review)

Lesson 6 of 12 · Claude Code 101Context management

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

* [What is the Context Window?](#what-is-the-context-window)
* [What Happens When Context Fills Up](#what-happens-when-context-fills-up)
* [Commands](#commands)
* [When to Use Which](#when-to-use-which)
* [Tips for Saving Context Space](#tips-for-saving-context-space)
* [Recap](#recap)
