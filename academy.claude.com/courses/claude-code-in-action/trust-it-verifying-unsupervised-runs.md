<!-- source: https://academy.claude.com/courses/claude-code-in-action/trust-it-verifying-unsupervised-runs -->

Lesson 8 of 9 · Claude Code in ActionTrust it: Verifying unsupervised runs

3. /[Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action)

[Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action)

# Trust it: Verifying unsupervised runs

Lesson 85 min

Trust it: Verifying unsupervised runs

You handed Claude a task and let it run without watching every step. Now it
says it's done. Before you ship that work, you need a way to check
something you didn't even supervise. That check is what makes hands-off
Claude Code safe to rely on.

The idea here is simple: verify in proportion to how much rope you gave the
run. If you watched the messages scroll by in a short session, a quick
glance is enough. But an unattended run, or a job that fired in continuous
integration with nobody in the loop, needs a real check. No one saw what
happened, so you have to reconstruct it after the fact.

Here's a way to picture it. The less you watched, the more you verify.

## Keep unattended runs in auto mode[](#keep-unattended-runs-in-auto-mode)

When a run goes unattended at work, keep it in auto mode rather than bypass permissions. In auto mode, the classifier still reviews each action for danger. That's a safety net worth keeping.

But be clear about what that net does and doesn't do. The classifier never judges whether the code is actually correct. It only flags dangerous actions. So your verification bar stays exactly where it was. Set that bar based on how unsupervised the run was.

## Start with the diff, not the summary[](#start-with-the-diff-not-the-summary)

Don't start with Claude's summary of what it did. Start with the diff itself.

1. Run `/code-review` to walk the changes and flag issues.
2. Then put your own eyes on `git diff`.

The trap is a tidy summary that reads perfectly fine, while the actual diff touched a file you honestly didn't expect it to touch. The summary won't tell you that. The diff will.

So read what changed. Read the files that were part of the plan first, then look for anything outside it. A clean write-up is not proof of clean code.

## Turn tests into a gate, not a promise[](#turn-tests-into-a-gate-not-a-promise)

The real gate on an unsupervised run is whether the tests passed, and whether Claude actually ran them or only claimed that it did. Don't leave that to trust. Wire it as a hook so Claude can't skip it.

A couple of hooks do the job:

* A **stop hook** that runs your tests and refuses to end the turn on a failure.
* A **post-tool-use hook** that lints and type checks after every edit.

The key detail is the exit code. A hook that exits with `exit 2` feeds the failure straight back to Claude. Claude reads that failure and fixes it without you asking. Best of all, the check fires on every run, whether or not you remember to ask for it.

## Get a cold second opinion[](#get-a-cold-second-opinion)

The sub-agent code review you'd run before a pull request works here too. Point it at an unsupervised run.

Open a fresh session or sub-agent and have it review the changed code with no memory of how the code was built. Because it has no stake in the approach, it catches the things the original run talked itself past. A second reviewer with fresh eyes finds what the author rationalized away.

## Putting it together[](#putting-it-together)

Make the check as serious as the run was unsupervised:

* Read the diff yourself.
* Turn the tests into a hook that gates the turn.
* Verify headless runs by their JSON result and exit code.
* Get a cold second opinion on anything that matters.

Do that, and "Claude did it while I wasn't looking" no longer takes faith.

[Previous lessonGitHub Actions and Code Review](https://academy.claude.com/courses/claude-code-in-action/github-actions-and-code-review)[Next lessonPlugins](https://academy.claude.com/courses/claude-code-in-action/plugins)

Lesson 8 of 9 · Claude Code in ActionTrust it: Verifying unsupervised runs

Steer the work

* [Steering long sessions](https://academy.claude.com/courses/claude-code-in-action/steering-long-sessions)

Configure Claude

* [A CLAUDE.md that follows](https://academy.claude.com/courses/claude-code-in-action/a-claude-md-that-follows)
* [Verification skills](https://academy.claude.com/courses/claude-code-in-action/verification-skills)
* [Permission modes](https://academy.claude.com/courses/claude-code-in-action/permission-modes)
* [Hooks](https://academy.claude.com/courses/claude-code-in-action/hooks)

Automate repeat work

* [Routines and headless](https://academy.claude.com/courses/claude-code-in-action/routines-and-headless)
* [GitHub Actions and Code Review](https://academy.claude.com/courses/claude-code-in-action/github-actions-and-code-review)

Verify and share

* [Trust it: Verifying unsupervised runs](https://academy.claude.com/courses/claude-code-in-action/trust-it-verifying-unsupervised-runs)
* [Plugins](https://academy.claude.com/courses/claude-code-in-action/plugins)

Quiz

* [Course quizQuiz](https://academy.claude.com/courses/claude-code-in-action/course-quiz)

* [Completion badge](https://academy.claude.com/courses/claude-code-in-action/badge)

* [Keep unattended runs in auto mode](#keep-unattended-runs-in-auto-mode)
* [Start with the diff, not the summary](#start-with-the-diff-not-the-summary)
* [Turn tests into a gate, not a promise](#turn-tests-into-a-gate-not-a-promise)
* [Get a cold second opinion](#get-a-cold-second-opinion)
* [Putting it together](#putting-it-together)
