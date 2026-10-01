<!-- source: https://academy.claude.com/courses/introduction-to-claude-tag/write-a-request-claude-can-work-with -->

Lesson 9 of 11 · Introduction to Claude TagWrite a request Claude can work with

3. /[Introduction to Claude Tag](https://academy.claude.com/courses/introduction-to-claude-tag)

[Introduction to Claude Tag](https://academy.claude.com/courses/introduction-to-claude-tag)

# Write a request Claude can work with

Lesson 915 min

In this lessonBy the end, you’ll be able to

* Set Claude up for success before you send a request
* Write a request Claude can succeed with
* Verify Claude's output and give feedback that improves its future work

You have now seen Claude reply on its own, run work on a schedule, and keep going while you are away, which means you can hand it larger jobs than a single question. That kind of work benefits from a different kind of instruction than a one-off ask.

When you hand Claude a task or a responsibility rather than a question, think about what Claude would need to understand the work well enough to know when to step in, when it is done, and how to decide something when you are not around. This lesson walks through choosing the work, writing that request, and what to expect while Claude carries it out.

## Step 1: Pick the work[](#step-1-pick-the-work)

Before you write, think through what you want, what Claude can access, and how you'll know if it worked.

* **Shift from step-by-step thinking to outcome thinking:** Picture delegating to someone who understands your workspace completely. What would you ask them to pull together or figure out?
* **Consider the inputs your task needs and make sure Claude can reach them:** Does it have access to the tools, files, and threads the work depends on? If unsure, ask `@Claude what can you access from this channel?` If Claude doesn't have what it needs, either move the task to a channel that does or ask your admin to connect the tool ([lesson 5(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-tag/pick-the-right-place-for-the-work)).
* **Think about who can see the work:** Check if the channel is appropriate. Sensitive work belongs in a private channel ([lesson 4(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-tag/claude-in-a-private-channel)).

## Step 2: Write the request[](#step-2-write-the-request)

* **State the goal, then the process that matters:** Say what you're trying to accomplish and why, and what a good result looks like and where it will go. Add the steps or constraints you care about; for the rest, knowing the intent lets Claude make good calls on the details you didn't spell out.
* **Point to the inputs you want Claude to use in the task:** It can read the channel, search the workspace, and use that channel's connections or attached files. If you have an example of a good result, link or paste it, or tell Claude where to find it.
* **Build in a way to check Claude's work:** Once you've thought about what success looks like, how will you be able to tell if Claude got it right? Think about ways you can ask Claude to verify the work, like giving it a rubric for what a good result looks like, linking its sources, or separating what it verified from what it inferred.
* **Tell Claude what to prioritize:** State what you care about in a good response. Consider things like the audience, the level of polish, what to avoid, or which decisions to bring back to you. When Claude faces a choice you didn't expect, these help steer its judgment.
* **Say what form the result should take:** A short answer belongs in the thread or channel. If people will open it, revisit it, or pass it on, ask for a page. Claude publishes the dashboard, report, or prototype on claude.ai and posts the link; the whole channel can open it, and later requests in the thread update that same link.

For some tasks, you may want to write the request differently:

* **For big, complex tasks that need planning,** ask Claude to propose an outline of its plan so you can align on an approach before it starts.
* **When the work is exploratory or ambiguous,** say so. Give Claude the question and why it matters, then leave room for it to propose a few directions before deciding how to execute.
* **For proactive or scheduled work,** tell Claude what it owns and where you decide. One way to do this is to [set a north star(opens in new tab)](https://claude.com/blog/building-effective-human-agent-teams): a person posts one ambitious, measurable goal in a channel Claude reads and pins it there. Claude in that channel can then propose work toward the goal on its own.

To learn how to set up and run a human-agent team, see the [Building Effective Human-Agent Teams(opens in new tab)](https://academy.claude.com/courses/building-effective-human-agent-teams) course. For examples, see [use cases of what Claude can do(opens in new tab)](https://claude.com/docs/claude-tag/users/use-cases).

## Step 3: Let Claude work[](#step-3-let-claude-work)

Claude reacts to your message and posts a short note that it's started. It keeps working without you, and if you're working in a channel, anyone in it can jump in to add context or adjust Claude's plan. Everything stays in the thread, so anyone can pick up where you left off.

You'll see:

* **A progress checklist, edited in place:** A longer task gets [one message that Claude updates as it works(opens in new tab)](https://claude.com/docs/claude-tag/concepts/how-it-works#how-the-checklist-updates). Those edits send no notification, so look for items ticked off since you last checked, or say in your request that you want a message at the bigger decision points and Claude will post one in the thread.
* **A new reply when Claude needs you or has a result:** A question, a problem it cannot solve alone, or the finished work. Claude waits for your answer to a question.
* **Quiet usually means working:** If the work gets blocked, Claude usually says so in a reply rather than going silent.

Editing a message you already sent has no effect; send a [new reply instead(opens in new tab)](https://claude.com/docs/claude-tag/concepts/how-it-works#reply-in-the-thread-to-steer). Each top-level message starts a new task for Claude. Keep separate tasks in different threads, but remember that Claude's channel notes apply to every thread in the channel.

## Step 4: Review the result[](#step-4-review-the-result)

Review Claude's work before you use it, and look more closely when more is at stake. A result in a thread arrives without the dashboards or documents you would usually check it against. Because you built verification into the request, you can follow the links, files, or queries it cited to see how it reached its answer.

If a result needs adjusting, see what Claude actually did by reading its checklist. If you spot something that needs fixing:

* If Claude looked in the wrong place or couldn't reach the right one, move the task to a channel with that tool or ask your admin to connect it.
* If Claude's work is incomplete, ask which sources or channels it searched. It may have been blocked from some of the sources you would have wanted it to use, or stopped the task early.
* If your request wasn't clear, reply and rewrite it. Include what you want, the form, what to prioritize, and where to look.
* If Claude missed a pattern your team follows, including how you check work, save it to memory so everyone in the channel benefits going forward ([lesson 6(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-tag/refine-claudes-learning-through-feedback)).

If you run into other errors, visit the [troubleshooting page(opens in new tab)](https://claude.com/docs/claude-tag/users/troubleshooting) or contact your admin. [`@Claude !help`(opens in new tab)](https://claude.com/docs/claude-tag/users/commands#see-the-commands-available-to-you) lists the commands you can send in a thread.

## Try it[](#try-it)

### Run one real task through all four steps

In your workspace · 15 minutes

1. Pick a task and confirm Claude can reach what it needs: `@Claude what can you access from this channel?`
2. Write the request with the goal, where to look, a way to check, and what to prioritize, then send it in the channel where the material is.
3. While it runs, reply in the thread to add one thing.
4. Review the result against its links, then save one correction with `remember for this channel`.

**Done when:** you have checked the result, and the channel's notes hold your correction.

## Before you move on[](#before-you-move-on)

**Key takeaway:** hand over a whole task with a goal, its inputs, and a way to check it; steer in the thread; check the result before you use it.

**After practicing:** You will have run one real task from request to reviewed result, and saved the correction it needed for next time.

[Previous lessonPut recurring work on a schedule](https://academy.claude.com/courses/introduction-to-claude-tag/put-recurring-work-on-a-schedule)[Next lessonExpand what Claude owns](https://academy.claude.com/courses/introduction-to-claude-tag/expand-what-claude-owns)

Lesson 9 of 11 · Introduction to Claude TagWrite a request Claude can work with

Get started with Claude Tag

* [Tag Claude to see what you can do](https://academy.claude.com/courses/introduction-to-claude-tag/tag-claude-and-see-what-happens)
* [Claude in a DM](https://academy.claude.com/courses/introduction-to-claude-tag/claude-in-a-dm)
* [Claude in a public channel](https://academy.claude.com/courses/introduction-to-claude-tag/claude-in-a-public-channel)
* [Claude in a private channel](https://academy.claude.com/courses/introduction-to-claude-tag/claude-in-a-private-channel)
* [Pick the right place for the work](https://academy.claude.com/courses/introduction-to-claude-tag/pick-the-right-place-for-the-work)

Shape how Claude works in your channels

* [Refine Claude's work through memory and instructions](https://academy.claude.com/courses/introduction-to-claude-tag/refine-claudes-learning-through-feedback)
* [Proactivity: let Claude reply without being tagged](https://academy.claude.com/courses/introduction-to-claude-tag/proactivity-let-claude-reply-without-being-tagged)
* [Put recurring work on a schedule](https://academy.claude.com/courses/introduction-to-claude-tag/put-recurring-work-on-a-schedule)

Run one task well

* [Write a request Claude can work with](https://academy.claude.com/courses/introduction-to-claude-tag/write-a-request-claude-can-work-with)

Expand Claude's ownership to larger tasks and ongoing work

* [Expand what Claude owns](https://academy.claude.com/courses/introduction-to-claude-tag/expand-what-claude-owns)
* [Review your team's habits](https://academy.claude.com/courses/introduction-to-claude-tag/review-your-teams-habits)

Check your understanding

* [Course quizQuiz](https://academy.claude.com/courses/introduction-to-claude-tag/course-quiz)

* [Completion badge](https://academy.claude.com/courses/introduction-to-claude-tag/badge)

* [Step 1: Pick the work](#step-1-pick-the-work)
* [Step 2: Write the request](#step-2-write-the-request)
* [Step 3: Let Claude work](#step-3-let-claude-work)
* [Step 4: Review the result](#step-4-review-the-result)
* [Try it](#try-it)
* [Before you move on](#before-you-move-on)
