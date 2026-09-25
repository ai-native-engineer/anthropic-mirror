<!-- source: https://academy.claude.com/courses/introduction-to-claude-tag/claude-in-a-public-channel -->

Lesson 3 of 11 · Introduction to Claude TagClaude in a public channel

3. /[Introduction to Claude Tag](https://academy.claude.com/courses/introduction-to-claude-tag)

[Introduction to Claude Tag](https://academy.claude.com/courses/introduction-to-claude-tag)

# Claude in a public channel

Lesson 315 min

In this lessonBy the end, you’ll be able to

* Describe how colleagues build on work in a public channel
* Explain how what Claude learns in a public channel is shared with everyone in it
* Have Claude use one connected tool and check the result

If you want Claude to use your team's tools, on work others can see, correct, and continue, ask Claude in a public channel. What Claude learns there helps everyone in the channel, so when more than one place would do, choose this one.

## What you can do in a public channel[](#what-you-can-do-in-a-public-channel)

In a public channel, Claude has access to your team's tools and can be shaped by anyone there, through that channel's instructions and corrections.

A few key things change from a DM:

In the illustration below, pick a team to watch one piece of work run in its channel: the request, the tools Claude reaches, the artifacts it posts back, and the team steering it.

## What Claude can use in a public channel[](#what-claude-can-use-in-a-public-channel)

On top of what it can do anywhere ([lesson 1(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-tag/tag-claude-and-see-what-happens)), Claude can see this channel's full history, including messages from before Claude was added, and use any tools connected to this channel. [Whoever sets Claude Tag up(opens in new tab)](https://claude.com/docs/claude-tag/admins/attach-to-scope) decides which tools each channel is connected to, and those tools work the same for everyone who asks there. By default you do not need a Claude account to tag Claude in a channel; the work is covered by the organization.

### What connections add[](#what-connections-add)

A channel can be connected to tools your team already uses, like GitHub, Google Drive, your CRM, or the team calendar; [whoever manages Claude Tag for the channel(opens in new tab)](https://claude.com/docs/claude-tag/admins/add-connections) sets these up. These are called [connections(opens in new tab)](https://claude.com/docs/claude-tag/concepts/glossary#connection). With them, Claude can move straight from the discussion to the work. With the right tools connected in a channel, Claude can:

* **Sales:** pull the account from the CRM before a call
* **Data:** run the warehouse query that answers the question in the thread
* **Support:** draft the reply on a support ticket
* **Engineering:** open the pull request for the fix the team just agreed on

In these tools Claude acts as itself, under its own account, with the access the channel was given. Connections open up a different set of use cases for each channel type and job function; the [use-case library(opens in new tab)](https://claude.com/docs/claude-tag/users/use-cases) has examples for each.

### Your own connectors, for your requests[](#your-own-connectors-for-your-requests)

Claude can also use the [personal connectors(opens in new tab)](https://claude.ai/customize/connectors) you have set up in your own Claude account, like your calendar, inbox, or issue tracker, when a request you make in the channel needs them, where it's available to your organization. Ask `@Claude add Thursday's launch review to my calendar` in the team channel, and it can do that for you.

In those tools Claude works under your name, the same as in a DM. Claude shows you a prompt that only you can see before it uses your personal connectors in a channel:

* **Allow:** Claude posts its responses directly. It first checks each response and holds any that look sensitive for you to review. The check can miss things.
* **Allow with review:** Claude shows you every response to approve before it posts.
* **Don't allow:** Claude does not use your connectors for this request.

On the Enterprise plan, an Owner of your Claude organization can remove one of the two Allow choices. What Claude posts back is visible to everyone in the channel, like any other reply.

## Protecting your privacy and data[](#protecting-your-privacy-and-data)

### Whose access Claude is using[](#whose-access-claude-is-using)

In a channel, Claude works with one of two kinds of access. In the team's connections it has [its own account(opens in new tab)](https://claude.com/docs/claude-tag/concepts/agent-identity) and acts as itself, so the team can see who did what. In your connectors it acts under your name, and only for you.

* **In a team connection, Claude can do only what Claude's own account in that tool allows:** your admin sets up that account, and anything Claude does there appears under Claude's account, not your name.
* **Anyone in the channel can use a team connection with the level of access Claude's account is set to:** for example, if that account can make changes in your issue tracker, anyone here can ask Claude to update a ticket; if it can only read, Claude can look tickets up but not change them. [How channel access works(opens in new tab)](https://claude.com/docs/claude-tag/concepts/agent-identity#agent-access) has more.
* **Your personal connectors serve only your requests:** Claude acts under your name in those tools, including making changes, and no one else in the thread can direct that work.
* **You can stop a task that is using your connectors:** select **Stop** under Claude's message saying it is going to use your connectors.
* **No reach into anyone else's private channels or DMs:** Claude cannot read them from here.

Check your own setup

Ask in the channel: `@Claude what can you access from here?` lists the tools connected to this channel.

Everyone in the channel sees the work, so restricted information belongs in a private channel ([lesson 4(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-tag/claude-in-a-private-channel)) and work only you should see in a DM ([lesson 2(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-tag/claude-in-a-dm)).

## Try it[](#try-it)

### Have Claude fetch one real record

In your workspace, in the channel where your work happens · 10 minutes

1. Ask `@Claude what can you access from this channel?`
2. Pick one tool or data source from its list. If a tool you need is missing, ask whoever manages Claude Tag for the channel to connect it.
3. Have Claude fetch one real item from it. Change the underlined parts to match your channel, then copy it in:

4. Open that item at its source and compare: is Claude's version current, is anything missing that you can see there, and did it say where each figure came from? If something is off, say so in the thread and watch it correct itself.
5. If a colleague is around, you can also ask them to reply in the thread with one correction and watch Claude take it; that is the part a DM cannot do.

**Done when:** you've compared what Claude retrieved against the source, and told it about anything that didn't match.

The **Configure** link under any Claude reply [opens a page that lists this channel's connections(opens in new tab)](https://claude.com/docs/claude-tag/users/good-habits#configure-claude-for-a-channel) too.

## Before you move on[](#before-you-move-on)

**Key takeaway:** in a channel the work is the team's: others steer it, the team's tools are in reach, and what Claude learns helps everyone in the channel.

**After practicing:** You will have had Claude fetch one real record from a connected tool and checked it against the source, and you will know what this channel can access.

[Previous lessonClaude in a DM](https://academy.claude.com/courses/introduction-to-claude-tag/claude-in-a-dm)[Next lessonClaude in a private channel](https://academy.claude.com/courses/introduction-to-claude-tag/claude-in-a-private-channel)

Lesson 3 of 11 · Introduction to Claude TagClaude in a public channel

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

* [What you can do in a public channel](#what-you-can-do-in-a-public-channel)
* [What Claude can use in a public channel](#what-claude-can-use-in-a-public-channel)
* [Protecting your privacy and data](#protecting-your-privacy-and-data)
* [Try it](#try-it)
* [Before you move on](#before-you-move-on)
