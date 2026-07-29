<!-- https://anthropic.skilljar.com/claude-code-in-action/486938 -->

You handed Claude a task and let it run without watching every step. Now it says it's done. Before you ship that work, you need a way to check something you didn't even supervise. That check is what makes hands-off Claude Code safe to rely on.

The idea here is simple: verify in proportion to how much rope you gave the run. If you watched the messages scroll by in a short session, a quick glance is enough. But an unattended run, or a job that fired in continuous integration with nobody in the loop, needs a real check. No one saw what happened, so you have to reconstruct it after the fact.

Here's a way to picture it. The less you watched, the more you verify.

## Keep unattended runs in auto mode

When a run goes unattended at work, keep it in auto mode rather than bypass permissions. In auto mode, the classifier still reviews each action for danger. That's a safety net worth keeping.

But be clear about what that net does and doesn't do. The classifier never judges whether the code is actually correct. It only flags dangerous actions. So your verification bar stays exactly where it was. Set that bar based on how unsupervised the run was.

## Start with the diff, not the summary

Don't start with Claude's summary of what it did. Start with the diff itself.

1. Run `/code-review` to walk the changes and flag issues.
2. Then put your own eyes on `git diff`.

The trap is a tidy summary that reads perfectly fine, while the actual diff touched a file you honestly didn't expect it to touch. The summary won't tell you that. The diff will.

So read what changed. Read the files that were part of the plan first, then look for anything outside it. A clean write-up is not proof of clean code.

## Turn tests into a gate, not a promise

The real gate on an unsupervised run is whether the tests passed, and whether Claude actually ran them or only claimed that it did. Don't leave that to trust. Wire it as a hook so Claude can't skip it.

A couple of hooks do the job:

* A **stop hook** that runs your tests and refuses to end the turn on a failure.
* A **post-tool-use hook** that lints and type checks after every edit.

The key detail is the exit code. A hook that exits with `exit 2` feeds the failure straight back to Claude. Claude reads that failure and fixes it without you asking. Best of all, the check fires on every run, whether or not you remember to ask for it.

## Get a cold second opinion

The sub-agent code review you'd run before a pull request works here too. Point it at an unsupervised run.

Open a fresh session or sub-agent and have it review the changed code with no memory of how the code was built. Because it has no stake in the approach, it catches the things the original run talked itself past. A second reviewer with fresh eyes finds what the author rationalized away.

## Putting it together

Make the check as serious as the run was unsupervised:

* Read the diff yourself.
* Turn the tests into a hook that gates the turn.
* Verify headless runs by their JSON result and exit code.
* Get a cold second opinion on anything that matters.

Do that, and "Claude did it while I wasn't looking" no longer takes faith.

<!-- youtube: lalGZSNhm8E -->

[![Trust IT Verifying Unsupervised Runs](https://img.youtube.com/vi/lalGZSNhm8E/hqdefault.jpg)](https://www.youtube.com/watch?v=lalGZSNhm8E)

<details>
<summary>자막: Trust IT Verifying Unsupervised Runs</summary>

You handed Claude a task and let it run without watching every step. Now it says it's done, but before you ship that, you need a way to check work that you didn't even supervise. Check is what makes hands-off Claude code safe to rely on. Verify in proportion to the road that you gave the run. A short session where you watched the messages scroll by needs a glance. An unattended run or a job that fired in continuous integration with nobody in the loop actually needs a real check because no one saw happen. And when a run does go unattended at work. keep it in auto mode rather than bypass permissions. The classifier still reviews each actions for danger. It never judges whether the code is right though, so the verification bar stays where it was. Set that bar from how unsupervised this run was. So start with the diff itself rather than a cloud summary of it. Run slash code review to walk the changes and flag issues. Then put your eyes on git diff. The trap is a tidy summary that reads fine while the diff touched a file that you honestly didn't even expect it to. Read what changed and read the files that were in the plan first. The real gate on an unsupervised run is whether the test passed and whether Claude ran them or only claimed that it did. Don't leave that to trust. Wire it as a hook so Claude can't skip it. A stop hook that runs your test and refuses to end the turn on a failure, or a post-tool use hook that lints and type checks after every edit. A hook that exists with code 2 feeds the failure straight back to Claude, which reads it and fixes it without you asking. The check fires on every run, whether or not you remember to ask. The sub-agent code review you'd run before a PR works here too. Point it at an unsupervised run. Open a fresh session or sub-agent and have it review the change code with no memory of how the code was built. It has no stake in the approach and catches what the original run talked itself past. Make the check as serious as the run was unsupervised. Read the diff, turn the test into a hook that gates the turn, verify headless runs by their JSON result and exit code, and get a cold second opinion on anything that matters. Do that, and Claude did it while I wasn't looking, no longer takes faith.

</details>
