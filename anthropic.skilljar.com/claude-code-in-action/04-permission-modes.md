<!-- https://anthropic.skilljar.com/claude-code-in-action/486932 -->

Permission modes let you decide once what Claude is allowed to run without stopping to ask you. Instead of approving every action one prompt at a time, you pick a mode that matches the job and let Claude work at the level of trust you're comfortable with.

You've already met a few of these modes. Every time you hit shift-tab, you cycle through them: manual, accept edits, and plan. Those cover the everyday, hands-on work. The rest of the modes are where hands-off Claude Code really lives, and the one to reach for there is auto.

## The six permission modes

Here's the full set. Each mode draws a different line between what runs freely and what needs your sign-off.

* **Manual** reads only, without prompting. Everything else asks first.
* **Accept edits** runs reads, file edits, and common file system bash commands without asking. This is for iterating on code that you review after the fact.
* **Plan** reads only. It researches and proposes changes without editing anything.
* **Auto** accepts everything, with a separate classifier model reviewing each action before it runs.
* **Don't ask** allows only pre-approved tools. Everything else is auto-denied with no prompt.
* **Bypass permissions** skips all checks. This is the equivalent of the dangerously-skip-permissions flag. Only run it inside an isolated container or virtual machine.

## Cycling with shift-tab

You don't need to memorize a command for each mode. Press shift-tab to cycle through the everyday ones: manual, accept edits, plan, and auto. The status bar at the bottom always shows which mode you're currently in, so you can glance down and know exactly what Claude is allowed to do.

## How auto mode works

Auto is the hands-off mode. Claude runs on its own, but before each action executes, a separate classifier model reviews it. The classifier guards intent. It's watching for moves that escalate beyond what you actually asked for.

Here's the kind of thing it's designed to block:

* Production deploys and migrations
* Force pushing, or piping downloaded code straight into a shell
* Sending sensitive data to external endpoints
* Destroying files that exist for the session

And it waves through the everyday work: local edits in your project, installing dependencies from your lock file, read-only requests, and pushing to your own branch.

## What the classifier can't do

The classifier checks intent, not correctness. It won't catch whether the code actually works. So if you ask Claude to refactor authentication and it writes broken authentication, the classifier waves it through, because broken isn't dangerous.

That's why you pair auto mode with a stop hook that runs your tests. The two work together:

* Auto mode watches what Claude is *trying* to do while it runs.
* The stop hook confirms the code actually runs once Claude finishes.

One guards intent before each action, the other guards correctness after. Auto mode's guardrails are still evolving, so check the docs for the current block and allow lists.

## Don't ask, for unattended runs

Don't ask is the right move whenever no human is around to approve prompts: CI pipelines, scheduled jobs, overnight batches. Only pre-approved tools are allowed, and anything off that list gets auto-denied with no prompt. That's the whole point. Your pipeline keeps moving instead of hanging on an approval no one is there to give.

## Match the mode to the job

There are several permission modes, and you reach the everyday ones by cycling shift-tab. To sum it up:

* **Auto** is the hands-off mode. The classifier checks intent before each action, and a stop hook checks correctness after.
* **Don't ask** covers unattended pipelines where no one is there to approve.
* **Bypass permissions** belongs only inside isolated containers and VMs.

Pick the mode that fits what you're doing, and let Claude run at that level.

<!-- youtube: Fjg4O-ZcRSU -->

[![Permission Modes](https://img.youtube.com/vi/Fjg4O-ZcRSU/hqdefault.jpg)](https://www.youtube.com/watch?v=Fjg4O-ZcRSU)

<details>
<summary>자막: Permission Modes</summary>

Permission mode lets you decide once what's safe to run without you. You already cycle through several of them with shift-tab, manual, accept edits, and plan. The rest are where hands-off Claude code lives and the one to lead with is auto. Claude runs without prompts while a separate classifier reviews each action before it executes, stepping in on ones it identifies as dangerous. So here are the permission modes. First, we have manual, which reads only without prompting. Everything else asks. Accept edits, reads, file edits, and common file system bash commands. This is for iterating on code that you review after the fact. Plan reads only. It researches and proposes without editing. Auto mode accepts everything with a classifier model reviewing each action before it runs. Don't ask. Only pre-approved tools allowed. Everything else auto-denied with no prompt. This is great for your CI pipelines. And then bypass permissions, skips all check. This is equivalent to the dangerously skipped permissions. Only run it inside of an isolated container or virtual machine. Press shift tab to cycle through manual, accept edits, plan, and auto. The status bar shows which one that you're in. Auto mode is where Claude runs, but before each action executes, a separate classifier model reviews it. The classifier guards intent. It blocks the moves that escalate beyond your request, production deploys, and migrations, force pushing or piping download code into a shell, sending sensitive data to external endpoints, and destroying files that exist for the session. It allows the everyday work, local edits in your project, installing dependencies from your log file, read-only requests, and pushing to your own branch. Now, the classifier won't catch whether the code works or not. So if you ask Claude to refactor authentication and it writes broken authentication, the classifier waves it through because broken isn't dangerous. Use auto mode together with a stop hook that runs your tests. Auto mode watches what Claude is trying to do while the hook confirms that the code actually runs. Auto mode guardrails are still evolving, so check the docs for the current block and allow lists. Don't ask is the right move whenever no human is there to approve prompts. CI, scheduled jobs, overnight batches. Anything off that list gets auto-denied. So your pipeline keeps moving instead of hanging on an approval no one will give. There are several permission modes and you can reach the everyday ones by cycling shift tab. Auto is the hands-off default. The classifier checks intent before each action runs and a stop hook checks correctness after. Don't ask covers unattended pipelines and bypass permission belong only inside isolated containers and VMs. Match the mode to the job.

</details>
