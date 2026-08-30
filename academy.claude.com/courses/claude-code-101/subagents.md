<!-- source: https://academy.claude.com/courses/claude-code-101/subagents -->

Lesson 9 of 12 · Claude Code 101Subagents

3. /[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

# Subagents

Lesson 96 min

Subagents

SummaryTranscript

Claude can delegate tasks to subagents that break them down and run
component tasks in parallel, improving your context management. Each
subagent operates in its own isolated context window.

## How It Works[](#how-it-works)

Managing context in Claude Code is important. A lot of the context window gets consumed by things like tool calls exploring your codebase or running web searches for research. What Claude discovers during that exploration isn't always relevant to the main feature you're developing.

This is where subagents come in. Claude spawns a subagent to handle a task like "explore this codebase for me." The subagent runs in parallel with its own context window, does all the exploration work, and once finished, summarizes its findings and returns that summary back to Claude.

The result: you get the answer you were looking for, without the entire journey it took to get there cluttering your main context.

## Creating Your Own Subagent[](#creating-your-own-subagent)

Subagents are defined in Markdown files with YAML frontmatter. The easiest way to get started is to let Claude generate one for you. Run:

`/agents`

Then select "Create new agent." You'll walk through steps including choosing the scope of the agent, defining its purpose, selecting the tools it has access to, and even picking a color for it.

Claude will generate a name, description, and prompt for the subagent. This also tells Claude when to call the subagent based on the prompts you give it.

## Further Customization[](#further-customization)

Subagents can be customized further. Here are some highlights:

* **Persistent memory** lets your subagent retain memory across conversations. This is great if you're using it consistently on the same projects.
* **Preload skills** into subagents by adding the `skills` key and listing skills by name. Note that unlike skills in your main conversation, the entire skill is loaded into context here.

## Recap[](#recap)

Keeping your context window clean is one of the best ways to stay productive with Claude Code. With subagents, you can run an agent in the background to handle the heavy lifting and return just the answer to your main context window.

**Want to go deeper?** Check out our dedicated course: [Introduction to subagents(opens in new tab)](https://academy.claude.com/courses/introduction-to-subagents)

[Previous lessonThe CLAUDE.md file](https://academy.claude.com/courses/claude-code-101/the-claude-md-file)[Next lessonSkills](https://academy.claude.com/courses/claude-code-101/skills)

Lesson 9 of 12 · Claude Code 101Subagents

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

* [How It Works](#how-it-works)
* [Creating Your Own Subagent](#creating-your-own-subagent)
* [Further Customization](#further-customization)
* [Recap](#recap)
