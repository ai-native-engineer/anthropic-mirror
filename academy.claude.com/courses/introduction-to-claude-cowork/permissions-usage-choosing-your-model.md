<!-- source: https://academy.claude.com/courses/introduction-to-claude-cowork/permissions-usage-choosing-your-model -->

Lesson 11 of 14 · Introduction to Claude CoworkBest practices for working safely

3. /[Introduction to Claude Cowork](https://academy.claude.com/courses/introduction-to-claude-cowork)

[Introduction to Claude Cowork](https://academy.claude.com/courses/introduction-to-claude-cowork)

# Best practices for working safely

Lesson 119 min

In this lessonBy the end, you’ll be able to

* Set up your workspace so the important stuff stays protected
* Write prompts that don't leave room for the wrong action
* Recognize the moments when "stop and think" matters more than speed

## Your part in working safely with Cowork[](#your-part-in-working-safely-with-cowork)

You already know from Lesson 2 that Claude always asks before deleting, and — in the default permission mode — before sending or sharing too. That's the floor. This lesson is what *you* bring on top — the pre-emptive moves that keep an autonomous tool with file, app, and connector access from doing something you didn't intend.

## Set up so mistakes can't reach what matters[](#set-up-so-mistakes-cant-reach-what-matters)

The single highest-leverage move is the folder you point Claude at. It's the boundary for what Claude can read, write, and (with your confirmation) delete.

* **Use a dedicated working folder, not a catch-all.** Pointing Claude at Documents, Downloads, or Desktop is the equivalent of letting a new colleague rummage through every file you have. Make a folder for the work. Move (or copy) in what's needed. Point Claude there.
* **Back up anything irreplaceable before you start.** If a file matters and a fresh copy can't be regenerated — old client deliverables, contracts you can't get re-issued, anything you'd be sorry to lose — make sure a copy lives somewhere Cowork can't reach. Cloud backup, a separate folder, a drive that isn't connected. Claude won't delete without asking, but the cost of clicking through the wrong confirmation is the cost of the file.
* **Test new workflows on copies first.** For example if you're building a scheduled task that'll run every Friday, the first run goes against a copy of the data. Once you've seen it behave, point it at the live folder.

## Write prompts that leave no room for the wrong action[](#write-prompts-that-leave-no-room-for-the-wrong-action)

How you ask matters as much as what folder you point at.

* **Be specific about destructive verbs.** *"Cut the section"* can be read as *"remove from view"* or *"delete from the file."* *"Update the file"* can mean *"rewrite it"* or *"add to it."* If the wrong reading would be irrecoverable, name what you mean: *"Remove the section from the draft, but keep the file."* *"Add a new appendix; don't rewrite the existing sections."*
* **Name the bounds in the prompt.** *"Only the 3 most recently updated files in this folder."* *"Only contracts that closed in Q3."* *"Don't message anyone — draft only."* This narrows what Cowork is doing and gives you a clear line for spotting drift.
* **Use scheduled tasks for drafts initially.** Scheduled tasks run while you're not watching. Until you're confident that the task runs the way you need it to, prompt it to draft for your review rather than send on your behalf.

## In the moment: the three checks that catch the rest[](#in-the-moment-the-three-checks-that-catch-the-rest)

**Read the plan once it has been made.** When Claude starts a task, it lays out what it's going to do in the progress tab. Skim it. Consider: does the plan make sense? are the steps in the right order? is it using the right sources? Redirect as necessary.

**Watch for unexpected patterns.** You don't need to validate every command. But if Claude is touching files or sites you didn't mention, or scope is creeping past what you asked for, stop the task. *"Something feels off"* is a real signal — pay attention to this.

**Approve confirmation prompts deliberately.** Stay in “Ask before acting” for anything that sends, posts, or shares — and when a confirmation prompt does appear, read it. Most mistakes don't happen because the safeguards failed; they happen because someone clicked through a confirmation that wasn't quite the action they intended. The dialog exists because the action matters — treat it that way.

## When Cowork isn't the right tool[](#when-cowork-isnt-the-right-tool)

A short list:

* **Regulated workflows that need an audit trail.** Cowork activity isn't captured in audit logs or data exports; the Compliance API does return Cowork session transcripts, but only for Claude Enterprise organizations and in beta.
* **Anything you wouldn't trust a smart, quick colleague to do unsupervised.** Sending the legal doc to a counterparty, posting the public announcement, pushing a customer-facing change. Claude can prepare; you ship.
* **Highly sensitive personal data** outside the boundary your IT team has explicitly approved.

## Go deeper[](#go-deeper)

[Use Claude Cowork safely(opens in new tab)](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely) is a valuable resource for learning what to do — and not to do — when working with Claude in Cowork. It covers the rest of what warrants more thought so that you understand the built-in guardrails and what you remain responsible for as Claude acts on your behalf.

## Lesson reflection[](#lesson-reflection)

Review the interactive below to get a sense for how to work safely with Cowork.

As you think about the tasks *you're* going to hand to Cowork:

* Which folder would you point Claude at — and is there anything inside it that shouldn't be reachable, or anything irreplaceable that needs to be backed up first?
* Is there a destructive verb in the prompt you'd write that you'd want to be more specific about?

## What’s next[](#whats-next)

In the next lesson, you'll learn how to make sure the skills and plugins you build actually behave — using lightweight evals to check their output before you rely on them or share them with anyone else.

[Previous lessonClaude for Microsoft 365](https://academy.claude.com/courses/introduction-to-claude-cowork/claude-for-microsoft-365)[Next lessonValidating skills for plugins](https://academy.claude.com/courses/introduction-to-claude-cowork/validating-skills-for-plugins)

Lesson 11 of 14 · Introduction to Claude CoworkBest practices for working safely

Meet Claude Cowork

* [What is Claude Cowork](https://academy.claude.com/courses/introduction-to-claude-cowork/what-is-cowork)
* [Setting up Claude Cowork](https://academy.claude.com/courses/introduction-to-claude-cowork/getting-set-up)
* [What Claude Cowork can do for you](https://academy.claude.com/courses/introduction-to-claude-cowork/scheduled-tasks)
* [Hand Claude Cowork your first task](https://academy.claude.com/courses/introduction-to-claude-cowork/the-task-loop)

Make Claude Cowork yours

* [Get better results faster](https://academy.claude.com/courses/introduction-to-claude-cowork/research-analysis-at-scale)
* [Standing context: Global instructions and projects](https://academy.claude.com/courses/introduction-to-claude-cowork/giving-cowork-context)
* [Skills: Teach Claude Cowork your way](https://academy.claude.com/courses/introduction-to-claude-cowork/file-document-tasks)
* [Plugins: Encode your team's expertise](https://academy.claude.com/courses/introduction-to-claude-cowork/plugins-cowork-as-a-specialist)

Use Claude wherever you work

* [Claude in Chrome](https://academy.claude.com/courses/introduction-to-claude-cowork/claude-in-chrome)
* [Claude for Microsoft 365](https://academy.claude.com/courses/introduction-to-claude-cowork/claude-for-microsoft-365)

Sharing and safety in Claude Cowork

* [Best practices for working safely](https://academy.claude.com/courses/introduction-to-claude-cowork/permissions-usage-choosing-your-model)
* [Validating skills for plugins](https://academy.claude.com/courses/introduction-to-claude-cowork/validating-skills-for-plugins)
* [Share what you build with your team](https://academy.claude.com/courses/introduction-to-claude-cowork/share-what-you-build-with-your-team)
* [Wrap up and next steps](https://academy.claude.com/courses/introduction-to-claude-cowork/troubleshooting-next-steps)

Check your understanding

* [Quiz on Claude CoworkQuiz](https://academy.claude.com/courses/introduction-to-claude-cowork/quiz-on-claude-cowork)

* [Completion badge](https://academy.claude.com/courses/introduction-to-claude-cowork/badge)

* [Your part in working safely with Cowork](#your-part-in-working-safely-with-cowork)
* [Set up so mistakes can't reach what matters](#set-up-so-mistakes-cant-reach-what-matters)
* [Write prompts that leave no room for the wrong action](#write-prompts-that-leave-no-room-for-the-wrong-action)
* [In the moment: the three checks that catch the rest](#in-the-moment-the-three-checks-that-catch-the-rest)
* [When Cowork isn't the right tool](#when-cowork-isnt-the-right-tool)
* [Go deeper](#go-deeper)
* [Lesson reflection](#lesson-reflection)
* [What’s next](#whats-next)
