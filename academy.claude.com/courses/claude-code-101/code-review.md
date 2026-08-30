<!-- source: https://academy.claude.com/courses/claude-code-101/code-review -->

Lesson 7 of 12 · Claude Code 101Code review

3. /[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

[Claude Code 101](https://academy.claude.com/courses/claude-code-101)

# Code review

Lesson 710 min

When you give Claude Code a task to complete in your codebase, Claude will often report back in a succinct way. Underneath the description of what Claude changed, there can be a variety of files that were changed (from small to major changes). Oftentimes, the session that wrote the code changes themselves (and explained them) is not the highest-quality judge of those changes. It's a good practice to give every change a look yourself before you keep it, and then have Claude review it again from a clean context, without this session's history.

## Review the actual changes[](#review-the-actual-changes)

A diff is the before-and-after of a change: the lines removed and the lines added, file by file. The `/diff` command opens an interactive viewer of your uncommitted changes in that form, and it can also show what each of Claude's turns changed. Use the up and down arrows to move between files and `Enter` to open one.

`/diff`

Read moreNothing shows up in /diff?

`/diff` and `/code-review` read git's record of what changed, so your project needs to be in a git repository. Git is the version-control tool most projects already use, and the Commit step in the Explore → Plan → Code → Commit lesson relies on it. This course doesn't teach git itself. If your project isn't in git yet, ask Claude to set it up and make a first commit before your next task. From that point on, every change shows up in both commands. For the change in front of you right now, ask for a review in plain words (below). On a different version control system, `/diff` and `/code-review` won't see your changes, but the rest still applies: read the change in your own tool, ask Claude in plain words to review the files Claude touched, and `/rewind` still works because Claude tracks its own edits.

The most important things that deserve a second look every time are:

* **Changes you didn't ask for.** A config value that was edited while Claude was in the file or a rewritten helper method that you didn't mention.
* **Tests that got weaker.** If the project you're working in contains tests, identify any that were skipped, deleted, or loosened until they passed.
* **New packages and hard-coded values.** A dependency that was added for only one function, a URL or a key written straight into the code.

If the whole change is wrong, run `/rewind` (or press `Esc` twice on an empty prompt), pick the prompt that produced it, and choose **Restore code and conversation**. One limit worth knowing: files changed by shell commands Claude ran, such as a package install, aren't rolled back.

The exercise below uses a small signup-form task: Claude's summary on top, the eight files Claude touched underneath.

## Ask for a second opinion[](#ask-for-a-second-opinion)

The Explore → Plan → Code → Commit lesson said to have a second reviewer on a change before you commit it. A long session carries everything it has read and decided. That's the context you learned to manage in the previous lesson, and it's exactly the history you don't want in a reviewer. `/code-review` is that second reviewer: it reviews the change in a clean context, with none of your session's history, and reports what it finds. It edits nothing unless you ask it to.

`/code-review`

The review runs in the background, anywhere from seconds to a few minutes, and counts against your usage like any other task, so save it for changes that deserve a second look. The findings arrive in your conversation when it finishes. You can also ask in plain words, and Claude can start the same review from the request. If Claude answers inline instead of starting a review, run the command yourself.

Review the changes you just made. Report problems; don't fix anything yet.

Copy prompt

Read moreWant a lighter or a deeper review?

Add an effort level to the command. `/code-review low` reports only the findings it's most confident about, so you see fewer false alarms. `/code-review high` casts a wider net and may include findings it's less sure of. The level you type is remembered for later reviews until you type a different one.

For the signup-form change, the review came back with four findings:

## Decide what to do with each finding[](#decide-what-to-do-with-each-finding)

Sort each finding into one of three piles:

1. **Fix now.** This is a real problem, it matters, and it must be fixed.
2. **Ask why.** This is the pile for findings you can't quite verify or that seem off. It's possible for reviewers that are reading code changes cold to also miss things.
3. **Leave it.** This is a real problem but small or inconsequential. These can often be batched into a group of fixes that you'll cover in one future session.

To ask why, quote the finding back to Claude and ask Claude to check again. For the second finding above, you would type:

You reported that isValidEmail doesn't trim spaces, but line 4 calls trim(). Check again and tell me whether the finding stands.

Copy prompt

Whenever you ask for a fix, it's good to ask for evidence with it:

Fix the first finding: don't skip the empty-email test and restore the original assertion. Then run the tests and show me the output.

Copy prompt

If a fix eventually grows into a large change of its own, run the review again.

## When it pays off to review things more closely[](#when-it-pays-off-to-review-things-more-closely)

A simple, one-line change often needs a quick glance at the diff and nothing else. You should use a human review and a Claude review when a change is bigger than you could hold in your head, when it touches something sensitive or does something destructive, and before you hand the work to a teammate.

Read moreIs this the same as Claude Code Review?

No. [Claude Code Review(opens in new tab)](https://code.claude.com/docs/en/code-review) is a separate product for teams: an admin turns it on for a GitHub repository, and it posts its findings on pull requests. Nothing in this lesson needs it.

## Try it: sort the four findings[](#try-it-sort-the-four-findings)

## Recap[](#recap)

* Read the actual diff of the file changes before you trust the summary alone. Run `/diff` and look for changes you didn't ask for, weaker tests, and new packages or hard-coded values.
* Get a second opinion from a clean context with `/code-review` (or ask in plain words and let Claude start it). The reviewer reports, and Claude doesn't edit unless you ask.
* Treat each finding as fix now, ask why, or leave it, and ask for evidence with every fix.

When the reviewer flags the same issue a few times, it might be a good idea to write a rule for Claude to read at the start of every session. That file is `CLAUDE.md`, and it's next.

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

* [Review the actual changes](#review-the-actual-changes)
* [Ask for a second opinion](#ask-for-a-second-opinion)
* [Decide what to do with each finding](#decide-what-to-do-with-each-finding)
* [When it pays off to review things more closely](#when-it-pays-off-to-review-things-more-closely)
* [Try it: sort the four findings](#try-it-sort-the-four-findings)
* [Recap](#recap)
