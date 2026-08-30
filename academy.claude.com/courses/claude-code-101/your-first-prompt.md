<!-- source: https://academy.claude.com/courses/claude-code-101/your-first-prompt -->

Lesson 4 of 12 · Claude Code 101Your first prompt

3. /[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

# Your first prompt

Lesson 46 min

Your first prompt

SummaryTranscript

You talk to Claude Code like you would any AI assistant. When entering your
prompt, here are some things to consider that can both protect you and make
things easier.

## Choosing a Permission Mode[](#choosing-a-permission-mode)

You can choose how much oversight to keep while Claude works. Press `Shift + Tab` to cycle between modes.

* **Manual mode:** Claude asks permission each time it wants to edit a file or run a command.
* **Auto-accept mode:** File edits are automatically approved, but commands still require your permission.
* **Auto mode:** Claude works without permission prompts while a background safety check screens each action; when something is blocked, Claude usually finds a safer approach or asks you for the go-ahead.

There's no right or wrong answer — it's whatever you're comfortable with.

![Claude Code in auto-accept mode, reading files and working through a task](https://academy.claude.com/assets/media/03c5a203be29e0bc03bd7b3fd14794232c15a9a6e1ecf583dcf6372ead0afab5.jpg)

## Plan Mode[](#plan-mode)

Within the `Shift + Tab` menu is **Plan Mode**. Plan mode takes your prompt and uses read-only tools to analyze your codebase and research your suggested implementation. It will ask clarifying questions along the way, then return a detailed plan it can execute.

Plan mode is great for planning complex changes or doing a safe code review. Many times you'll be asking Claude to handle multi-step implementations toward a feature, and this is exactly where Plan Mode excels.

![Claude Code with plan mode on, showing the status bar indicator](https://academy.claude.com/assets/media/fb00d337c540c5c34581d96aeef29834c7ceb70bed2bec918a77d1043b310899.jpg)

## Example: Add a Dark Mode Toggle[](#example-add-a-dark-mode-toggle)

Let's walk through an example. Say you have an application that needs a dark mode toggle. Open the root directory of your project and run `claude`. Press `Shift + Tab` a couple of times to enter Plan Mode, then write a prompt like:

My app needs a dark mode implemented across the entire app. Can you create a toggle switch on the header that allows a user to toggle between light mode and dark mode? I need you to find a good contrast color that works based on my existing light theme.

Open in Claude Code

![Entering the dark mode prompt in Claude Code with plan mode enabled](https://academy.claude.com/assets/media/39b0125f002f95b0b05695f9426a1596afca1f307fa8458efb2d92e46661dac3.jpg)

Let Claude plan it out. After reviewing the plan, if it looks good, accept it and let Claude work through it — depending on your permission mode, it may check in with you along the way. At the end, you can see exactly what Claude did and how it reached its conclusions.

## Recap[](#recap)

When using Claude Code, try to be as descriptive as possible with your prompt. If you want to stay in the loop at every step, you can. Use Plan Mode to let Claude dig into the details of what you want to achieve before executing on any code.

[Previous lessonInstalling Claude Code](https://academy.claude.com/courses/claude-code-101/installing-claude-code)[Next lessonThe explore → plan → code → commit workflow](https://academy.claude.com/courses/claude-code-101/the-explore-plan-code-commit-workflow)

Lesson 4 of 12 · Claude Code 101Your first prompt

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

* [Choosing a Permission Mode](#choosing-a-permission-mode)
* [Plan Mode](#plan-mode)
* [Example: Add a Dark Mode Toggle](#example-add-a-dark-mode-toggle)
* [Recap](#recap)
