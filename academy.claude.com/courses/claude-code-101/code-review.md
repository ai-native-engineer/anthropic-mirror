<!-- source: https://academy.claude.com/courses/claude-code-101/code-review -->

Lesson 7 of 12 · Claude Code 101Code review

3. /[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

# Code review

Lesson 73 min

Code review

SummaryTranscript

Claude Code has a few built-in features that make your git workflow faster.
Let's go through them.

## Review with a Subagent

Before you push a PR, ask Claude to use a **subagent** to review your changes. The subagent runs in its own context window with fresh eyes — it doesn't carry the bias of the main agent that just spent the session writing the code.

When creating a code-reviewer subagent, restrict it to read-only tools. A reviewer should flag issues, not edit files. Check the subagent configuration into your repo so your whole team uses the same reviewer.

## The /commit-push-pr Skill

The `/commit-push-pr` skill handles the commit, push, and PR creation all in one step. Instead of doing each manually, just run the skill and Claude takes care of it.

If you have a Slack MCP server configured with channels listed in your CLAUDE.md, it will automatically post the PR link to your team's channel.

## Session Linking with --from-pr

When Claude creates a PR through `gh pr create`, the session gets linked to that PR automatically. If you need to come back to it later — maybe to address review comments or fix a failing build — run:

`claude --from-pr <PR_NUMBER>`

This picks up right where you left off.

## Recap

Use a subagent for an unbiased code review before pushing. Use `/commit-push-pr` to handle the full commit-to-PR flow in one step. And use `--from-pr` to resume work on a PR later. These are small features, but they remove a lot of friction from your daily workflow.

[Previous lessonContext management](https://academy.claude.com/courses/claude-code-101/context-management)[Next lessonThe CLAUDE.md file](https://academy.claude.com/courses/claude-code-101/the-claude-md-file)

Lesson 7 of 12 · Claude Code 101Code review

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

* [Review with a Subagent](#review-with-a-subagent)
* [The /commit-push-pr Skill](#the-commit-push-pr-skill)
* [Session Linking with --from-pr](#session-linking-with---from-pr)
* [Recap](#recap)
