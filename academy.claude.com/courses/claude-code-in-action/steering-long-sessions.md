<!-- source: https://academy.claude.com/courses/claude-code-in-action/steering-long-sessions -->

Lesson 1 of 9 · Claude Code in ActionSteering long sessions

Loading

Steering long sessions

Prompting Claude to knock out a quick task is easy. You ask, it works, you
check the result. But long tasks are a different game. Refactoring across a
dozen files or building out a new feature can take hours. And the more you
have to steer Claude along the way, the longer it drags on.

The good news is that you have a lot of tools to help Claude during these
long sessions. It really comes down to two habits: scope the work before
Claude starts, and steer it while it runs. Let's walk through both.

## Scope the work first with plan mode

Before Claude writes a single line, get it to lay out a plan. In plan mode, Claude does its research in read-only mode. It reads the code, figures out what needs to change, and hands you a plan to review.

When you get that plan, actually read it. Don't skim it. The more thorough the plan, the fewer surprises you'll hit once Claude starts executing. If something's off or missing, just ask Claude to add it where you want. Iterating on a plan is much faster than letting Claude run and hoping for the best, then cleaning up the mess.

## Steer while Claude works

Once Claude is running, you have a few ways to keep it pointed in the right direction. The first is compaction.

### Compact

Compact summarizes your conversation, uses that summary as the new context, and deletes the old messages. This frees up your context window so Claude can keep going. The risk is that something important gets dropped in the summary, and Claude drifts off course.

So don't just run `/compact` on its own. Add instructions after the command to tell Claude how to summarize. For example, if you finished debugging a while back and now you only care about some API changes, say so:

`/compact Focus on the --version flag implementation`

Anything you write after the command shapes what the summary keeps. That's your steering wheel for context.

### Rewind

When Claude heads down the wrong path, you don't have to prompt your way back out. Rewind takes you to your last checkpoint. Every user prompt creates a checkpoint you can revert to. To open the menu, double tap escape on an empty prompt.

From the rewind menu you get a few options:

* **Restore code and conversation** - roll back both together.
* **Restore conversation** - roll back just the chat.
* **Restore code** - roll back just the files.
* **Summarize from here** - summarizes everything after the checkpoint. Great if you had a side conversation and just want to free up some space.
* **Summarize up to here** - summarizes everything before the checkpoint. Great when you had a long setup phase you want to compress, but you want to keep the implementation parts intact.

## Let Claude run more autonomously

Everything so far assumes you're hands-on, watching and correcting. If you want something more autonomous, there's goal and loop.

### Goal

Goal sets a completion condition. You describe what "done" looks like, and Claude keeps working across turns until a fast evaluator confirms those conditions are met. It won't just stop the first time it thinks it's finished.

For example:

`/goal all tests in src/billing pass, and the type checker reports zero errors`

To cancel it, run `/goal clear`. One important constraint: the evaluator only reads the transcript. So your condition has to be checkable from the output Claude actually produces, like the results of a test run.

### Loop

Loop runs a prompt on an interval between turns, either fixed or self-paced. Use it to pull something external, like a CI run or a deploy, and act when the state changes.

To stop a loop, just press escape.

## Run parallel work with worktrees

The steering metaphor so far assumes one steering wheel in one car. But when you're running multiple agents on the same codebase, you don't want two steering wheels in one car. That's unsafe. Two Claude sessions fighting over the same files leads to conflicts.

That's where worktrees come in. Instead of sessions stepping on each other, each one gets its own independent file tree.

Because each agent has its own tree, they can't clobber each other's changes. When a session exits, a clean worktree is automatically removed.

There's one helpful file to know about. A `.worktreeinclude` file at the repo root lists git-ignored files to copy into each worktree. This is useful for things like an environment variable file or a local config that you need in every worktree but don't want to commit to version control.

## Putting it together

Handling long Claude Code sessions comes down to a handful of habits:

1. Scope your work first, then steer.
2. Direct your compaction so the summary keeps what matters.
3. Use the rewind menu to course correct when Claude drifts.
4. Set a goal when you can describe "done" better than you can describe the steps.
5. Run parallel work in worktrees.

Do that, and you can trust a long run without babysitting every step of it.
