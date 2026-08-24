<!-- source: https://academy.claude.com/courses/claude-code-101/the-claude-md-file -->

Lesson 8 of 12 · Claude Code 101The CLAUDE.md file

3. /[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

# The CLAUDE.md file

Lesson 810 min

The CLAUDE.md file

SummaryTranscript

One of the most useful features in Claude Code is the CLAUDE.md file. It
gives Claude Code persistent memory about your project.

## The Problem It Solves

When you open Claude Code without a CLAUDE.md file, it starts fresh every time. It has to re-explore your codebase, figure out what dependencies are needed, and understand what features are already implemented. Sometimes it makes assumptions, which makes it harder to steer Claude in the right direction.

CLAUDE.md solves this. It's a Markdown file you add to the root of your project, and Claude Code reads it automatically every time you start a session. Think of it as an onboarding script for your codebase. The contents of the CLAUDE.md file are appended to your prompt.

## An Example

Here's what a typical CLAUDE.md file looks like:

markdown

```
# Project

This is a Next.js 15 app using the App Router, Tailwind, and Drizzle ORM.

# Commands
- Dev server: `pnpm dev`
- Run tests: `pnpm test`
- Lint: `pnpm lint`

# Code Style
- Use 2-space indentation
- Prefer named exports
- All API routes go in app/api/
- Use server actions instead of API routes where possible
```

It's straightforward. Now if you ask Claude Code to create a React component, it already knows to use Tailwind for styling and to follow your code conventions.

![A CLAUDE.md file open in VS Code showing project info, commands, and code style rules](https://academy.claude.com/assets/media/3bc0b82a5595e143f7c169346d9cca4e578013befa12eeb71963851299cb097b.jpg)

## CLAUDE.md is for Teams

You can (and should) commit your CLAUDE.md to version control so your team benefits from it. There's actually a hierarchy of memory files depending on who they're for:

* **Project-level CLAUDE.md** lives in the root directory of your project. Shared with the team.
* **User-level CLAUDE.md** lives in your configuration folder. This one is just for you and applies across all your projects. Put your personal preferences here.

## Tips

**Save corrections to memory.** If you find yourself correcting Claude repeatedly — like telling it to always use server actions instead of API routes — explicitly ask Claude to save that rule to memory. Next time you open the project, it'll know.

![Asking Claude to save a rule to the CLAUDE.md file — always use server actions instead of API routes](https://academy.claude.com/assets/media/aa738f148200bde3fe73a9c6457da77f035577f249bc0dc74149c1b91b0328ae.jpg)

**Reference project docs.** If you have documentation in your project that you want Claude to reference, use the `@` symbol with the file path:

markdown

```
## README.md

Please read if you need more info: @README.md
```

**Start without one.** We recommend starting a project without a CLAUDE.md file so you can see where you constantly have to course-correct the model. This keeps your CLAUDE.md compact and focused on only the necessary information. When you're ready, run `/init` to have Claude generate one for you.

## Recap

The difference between a frustrating Claude Code session and a productive one often comes down to context — and the CLAUDE.md file is how you provide that context. Start with your stack, your preferences, and your commands, then build from there as you go.

[Previous lessonCode review](https://academy.claude.com/courses/claude-code-101/code-review)[Next lessonSubagents](https://academy.claude.com/courses/claude-code-101/subagents)

Lesson 8 of 12 · Claude Code 101The CLAUDE.md file

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

* [The Problem It Solves](#the-problem-it-solves)
* [An Example](#an-example)
* [CLAUDE.md is for Teams](#claudemd-is-for-teams)
* [Tips](#tips)
* [Recap](#recap)
