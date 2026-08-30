<!-- source: https://academy.claude.com/courses/claude-code-in-action/permission-modes -->

Lesson 4 of 9 · Claude Code in ActionPermission modes

3. /[Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action)

[Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action)

# Permission modes

Lesson 45 min

Permission modes

Permission modes let you decide once what Claude is allowed to run without
stopping to ask you. Instead of approving every action one prompt at a
time, you pick a mode that matches the job and let Claude work at the level
of trust you're comfortable with.

You've already met a few of these modes. Every time you hit shift-tab, you
cycle through them: manual, accept edits, and plan. Those cover the
everyday, hands-on work. The rest of the modes are where hands-off Claude
Code really lives, and the one to reach for there is auto.

## The six permission modes[](#the-six-permission-modes)

Here's the full set. Each mode draws a different line between what runs freely and what needs your sign-off.

* **Manual** reads only, without prompting. Everything else asks first.
* **Accept edits** runs reads, file edits, and common file system bash commands without asking. This is for iterating on code that you review after the fact.
* **Plan** reads only. It researches and proposes changes without editing anything.
* **Auto** accepts everything, with a separate classifier model reviewing each action before it runs.
* **Don't ask** allows only pre-approved tools. Everything else is auto-denied with no prompt.
* **Bypass permissions** skips all checks. This is the equivalent of the dangerously-skip-permissions flag. Only run it inside an isolated container or virtual machine.

## Cycling with shift-tab[](#cycling-with-shift-tab)

You don't need to memorize a command for each mode. Press shift-tab to cycle through the everyday ones: manual, accept edits, plan, and auto. The status bar at the bottom always shows which mode you're currently in, so you can glance down and know exactly what Claude is allowed to do.

## How auto mode works[](#how-auto-mode-works)

Auto is the hands-off mode. Claude runs on its own, but before each action executes, a separate classifier model reviews it. The classifier guards intent. It's watching for moves that escalate beyond what you actually asked for.

Here's the kind of thing it's designed to block:

* Production deploys and migrations
* Force pushing, or piping downloaded code straight into a shell
* Sending sensitive data to external endpoints
* Destroying files that exist for the session

And it waves through the everyday work: local edits in your project, installing dependencies from your lock file, read-only requests, and pushing to your own branch.

## What the classifier can't do[](#what-the-classifier-cant-do)

The classifier checks intent, not correctness. It won't catch whether the code actually works. So if you ask Claude to refactor authentication and it writes broken authentication, the classifier waves it through, because broken isn't dangerous.

That's why you pair auto mode with a stop hook that runs your tests. The two work together:

* Auto mode watches what Claude is *trying* to do while it runs.
* The stop hook confirms the code actually runs once Claude finishes.

One guards intent before each action, the other guards correctness after. Auto mode's guardrails are still evolving, so check the docs for the current block and allow lists.

## Don't ask, for unattended runs[](#dont-ask-for-unattended-runs)

Don't ask is the right move whenever no human is around to approve prompts: CI pipelines, scheduled jobs, overnight batches. Only pre-approved tools are allowed, and anything off that list gets auto-denied with no prompt. That's the whole point. Your pipeline keeps moving instead of hanging on an approval no one is there to give.

## Match the mode to the job[](#match-the-mode-to-the-job)

There are several permission modes, and you reach the everyday ones by cycling shift-tab. To sum it up:

* **Auto** is the hands-off mode. The classifier checks intent before each action, and a stop hook checks correctness after.
* **Don't ask** covers unattended pipelines where no one is there to approve.
* **Bypass permissions** belongs only inside isolated containers and VMs.

Pick the mode that fits what you're doing, and let Claude run at that level.

[Previous lessonVerification skills](https://academy.claude.com/courses/claude-code-in-action/verification-skills)[Next lessonHooks](https://academy.claude.com/courses/claude-code-in-action/hooks)

Lesson 4 of 9 · Claude Code in ActionPermission modes

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

* [The six permission modes](#the-six-permission-modes)
* [Cycling with shift-tab](#cycling-with-shift-tab)
* [How auto mode works](#how-auto-mode-works)
* [What the classifier can't do](#what-the-classifier-cant-do)
* [Don't ask, for unattended runs](#dont-ask-for-unattended-runs)
* [Match the mode to the job](#match-the-mode-to-the-job)
