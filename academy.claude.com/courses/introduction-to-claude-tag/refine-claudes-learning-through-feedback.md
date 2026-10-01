<!-- source: https://academy.claude.com/courses/introduction-to-claude-tag/refine-claudes-learning-through-feedback -->

Lesson 6 of 11 · Introduction to Claude TagRefine Claude's work through memory and instructions

3. /[Introduction to Claude Tag](https://academy.claude.com/courses/introduction-to-claude-tag)

[Introduction to Claude Tag](https://academy.claude.com/courses/introduction-to-claude-tag)

# Refine Claude's work through memory and instructions

Lesson 610 min

In this lessonBy the end, you’ll be able to

* Save corrections so Claude learns what matters to your team
* Choose between memory and instructions by how firmly a rule should hold
* Check and correct a channel's notes over time

## How Claude learns, and how to give feedback[](#how-claude-learns-and-how-to-give-feedback)

When you correct Claude or tell it how your team works, you usually want that to apply next time too, not only in the thread you are in. Claude Tag has two places for things that should last:

* **Memory:** notes Claude writes down about the channel and your work. You can also add to them by telling Claude in a message.
* **Channel instructions:** rules a person types into the channel's settings page. Claude follows them in every thread.

|  | Memory | Channel instructions |
| --- | --- | --- |
| **What it is** | Notes Claude keeps about the channel | Rules a person writes for the channel |
| **How you change it** | Tell Claude in a message | Edit the channel’s settings page (Configure, under any Claude reply) |
| **Use it for** | Things Claude picks up as it works: corrections, preferences, who owns what | Rules for every thread: the channel’s purpose, tone, when to reply, what never to do |

If a note and an instruction disagree, Claude follows the instruction.

*For a deeper dive on what Claude learns, see [what Claude remembers(opens in new tab)](https://claude.com/docs/claude-tag/users/memory).*

### Memory[](#memory)

Memory is Claude's notes about your channel. When you tell Claude something that should apply next time too, like a correction, a preference, or who owns what, it saves a note. It also saves notes on its own as it works. In later threads, Claude reads these notes before it answers. Anyone in the channel can ask Claude to add, change, or delete a note. Each note is scoped either to one channel or to the whole workspace:

* **To add a note:** `@Claude remember for this channel: …`
* **Channel notes** apply in that channel only. Claude keeps a separate set of notes for each channel. In your DM, Claude also keeps notes, and those are scoped to you and only you can access them.
* **Workspace notes** apply in every channel. Claude saves one only from a public channel, and only for things everyone should know, like a company-wide naming rule. See [what Claude remembers(opens in new tab)](https://claude.com/docs/claude-tag/users/memory).

### How to keep memory useful over time[](#how-to-keep-memory-useful-over-time)

Claude keeps adding notes as it works, so notes can go out of date as your organization changes. At any time, you can ask Claude to show, correct, or update them:

* To [see what it has picked up(opens in new tab)](https://claude.com/docs/claude-tag/users/memory#check-and-correct-what-claude-tag-remembers): `@Claude what do you remember about this channel?`
* If something is wrong, correct it: `@Claude remember for this channel: [corrected version]`
* If something is stale, remove it: `@Claude that’s outdated, forget the entry about [topic].`

Owners of your Claude organization can also [view, edit, and delete(opens in new tab)](https://claude.com/docs/claude-tag/users/memory#check-and-correct-what-claude-tag-remembers) a channel's notes and the workspace notes in Claude Tag's admin settings on claude.ai.

### Channel instructions[](#channel-instructions)

Channel instructions are rules someone on your team types into the channel's settings page, for example: "This channel handles billing questions. Keep replies short. Never contact customers directly." Claude reads them at the start of every thread. They are guidance Claude follows closely, not a hard lock: for anything that must never happen, use a setting or an access control rather than a sentence.

* **Good uses:** the channel's purpose, what to reply to without being tagged, tone and length, which sources to answer from, where to file things.
* **Where to edit them:** click [Configure(opens in new tab)](https://claude.com/docs/claude-tag/users/good-habits#configure-claude-for-a-channel) under any Claude reply. Usually anyone in the channel with a Claude account at your organization can edit them; an admin can [lock the page(opens in new tab)](https://academy.claude.com/tutorials/claude-tag-admin-guide#configure-page). If it is locked, ask whoever manages Claude Tag for your channel.
* **Also on that page:** the [**Respond automatically**(opens in new tab)](https://claude.com/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off) setting, which controls whether Claude replies without being tagged ([lesson 7(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-tag/proactivity-let-claude-reply-without-being-tagged)), and the list of connected tools, which only admins and [channel managers(opens in new tab)](https://academy.claude.com/tutorials/claude-tag-admin-guide#who-can-do-what) can change.
* Changes apply to new threads, so test in a fresh one.
* **For more:** see [how to set channel instructions(opens in new tab)](https://claude.com/docs/claude-tag/users/good-habits#configure-claude-for-a-channel).

You will see the whole page, with what sits beside the instructions, in [lesson 10(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-tag/expand-what-claude-owns).

Example channel instructions for a bug triaging channel:

```
This channel triages customer bug reports for the billing service.
When a new message contains an error ID, start a thread:
- look the error up in the monitoring tool
- link the dashboard
- propose an owner
Otherwise stay quiet unless tagged.
Keep replies under six lines; link to logs rather than pasting them.
File confirmed bugs in the tracker with the label from-chat.
Investigation is read-only; never touch production.
```

**Memory can hold a rule too; it just [holds it more loosely(opens in new tab)](https://claude.com/docs/claude-tag/users/memory#make-an-instruction-stick) than instructions do.** Some feedback, like formatting and voice rules, can live in either place. To try a rule out quickly, tell Claude "keep replies under six lines" in the channel: it saves it to memory and follows it.

### To recap[](#to-recap)

**Memory** holds what Claude learns as it goes and the rules you are trying out. **Channel instructions** hold the rules that have proven themselves and must apply in every thread. When a rule you tried in memory has settled, move it to the channel's instructions. If you don't have edit access to the instructions, ask whoever manages Claude Tag for the channel to promote it.

Check your own setup

Asking `@Claude what do you remember here?` in the channel shows the memory. Opening the channel's settings shows whether you can edit the instructions.

## Improving Claude's results[](#improving-claudes-results)

Now that you know how memory and instructions work, when Claude's results are not what you expected you can usually spot the cause, and each cause has a fix:

| If you notice | Likely cause | What to do |
| --- | --- | --- |
| Replies feel thin or generic | Claude lacks access to the tools your work lives in | Ask whoever manages Claude Tag for the channel to [connect them to this channel(opens in new tab)](https://academy.claude.com/tutorials/claude-tag-admin-guide#access-editor). Your own connectors can cover your requests, where it’s available to your organization. |
| Claude answers things it should leave alone | Claude lacks clarity on its job or role in this channel | Give Claude a job in [channel instructions(opens in new tab)](https://claude.com/docs/claude-tag/users/good-habits#configure-claude-for-a-channel) |
| The same correction keeps coming up | It was said once in a thread, without saying it was for the channel going forward | Say “[remember for this channel(opens in new tab)](https://claude.com/docs/claude-tag/users/memory)” |
| Claude doesn’t respond in this channel | It is not turned on for this channel | Ask whoever manages Claude Tag to turn it on here ([when Claude responds(opens in new tab)](https://claude.com/docs/claude-tag/users/when-claude-responds)) |

## Practice[](#practice)

## Try it[](#try-it)

### Save a pattern and see how it shapes Claude's work

In your workspace · 5 minutes

1. Ask `@Claude what do you remember about this channel?` to see what it has already learned.
2. Pick one task your team does regularly. Work with Claude on it and notice where its approach doesn't match how your team actually thinks.
3. Name the principle it missed: "We always check what we shipped before recommending something new." "We prioritize by impact to retention, not just effort."
4. Save it to memory: `@Claude remember for this channel: [pattern]`.
5. Give Claude similar work again in a new thread. If the change doesn't land right, update the memory or try a different way of stating it.

**Done when:** you've added something to memory and watched how Claude's next answers shift.

## Before you move on[](#before-you-move-on)

**Key takeaway:** say it in the channel; promote what must hold every time into instructions.

**After practicing:** You will have saved one correction to the channel's notes and seen it show up in Claude's next answer, and you will know whether you can edit this channel's instructions.

[Previous lessonPick the right place for the work](https://academy.claude.com/courses/introduction-to-claude-tag/pick-the-right-place-for-the-work)[Next lessonProactivity: let Claude reply without being tagged](https://academy.claude.com/courses/introduction-to-claude-tag/proactivity-let-claude-reply-without-being-tagged)

Lesson 6 of 11 · Introduction to Claude TagRefine Claude's work through memory and instructions

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

* [How Claude learns, and how to give feedback](#how-claude-learns-and-how-to-give-feedback)
* [Improving Claude's results](#improving-claudes-results)
* [Practice](#practice)
* [Try it](#try-it)
* [Before you move on](#before-you-move-on)
