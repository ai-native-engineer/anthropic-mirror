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

As you work with Claude in a channel, it learns from your feedback, and most of the time giving feedback is as easy as telling Claude. What you tell Claude goes to one of two places: memory or channel instructions.

|  | Memory | Channel instructions |
| --- | --- | --- |
| **Who writes it** | Claude, on its own or when asked | A person, deliberately |
| **Where it is edited** | By talking to Claude in the channel (Owners can also edit notes in admin settings) | The channel’s settings (Configure, under any reply) |
| **Best for** | Context Claude learns as it goes (preferences, conventions, owners, corrections), and rules you are trying out | Rules that must hold in every thread: purpose, tone, when to reply, never do X, who to escalate to |
| **Precedence** | Advisory; instructions outrank it | Read in every new thread; outranks memory |

*For a deeper dive on what Claude learns, see [what Claude remembers(opens in new tab)](https://claude.com/docs/claude-tag/users/memory).*

### Memory[](#memory)

Claude's memory is a set of notes, called memory notes, that Claude can use in later threads. When Claude learns something that should still apply after the current thread, such as a preference, a convention, who owns what, or a correction, Claude writes a note on its own. Anyone in the channel can also ask Claude to add, correct, or remove a note. There are two kinds of memory notes, channel notes and workspace notes, described below.

* **How to use it:** `@Claude remember for this channel: …` for things that matter, such as corrections, preferences, and the reason behind a decision. Corrections are valuable feedback that helps Claude's work in this channel improve over time.
* **Channel notes:** notes for one channel. Claude uses them in later threads in that channel only. Every public and private channel has its own, and a DM has its own notes for you alone.
* **Workspace notes:** notes for the whole workspace, such as an organization-wide naming rule. Claude is designed to save there only what is useful in every channel and what no channel would mind everyone in the workspace reading. Claude adds them only from public channels and can use them in every channel, private ones included. See [what Claude remembers(opens in new tab)](https://claude.com/docs/claude-tag/users/memory).

### How to keep memory useful over time[](#how-to-keep-memory-useful-over-time)

Claude keeps adding notes as it works, so notes can go out of date as your organization changes. At any time, you can ask Claude to show, correct, or update them:

* To [see what it has picked up(opens in new tab)](https://claude.com/docs/claude-tag/users/memory#check-and-correct-what-claude-tag-remembers): `@Claude what do you remember about this channel?`
* If something is wrong, correct it: `@Claude remember for this channel: [corrected version]`
* If something is stale, prune it: `@Claude that’s outdated, forget the entry about [topic].`

Owners of your Claude organization can also [view, edit, and delete(opens in new tab)](https://claude.com/docs/claude-tag/users/memory#check-and-correct-what-claude-tag-remembers) a channel's notes and the workspace notes in Claude Tag's admin settings on claude.ai.

### Channel instructions[](#channel-instructions)

Channel instructions are the rules a person writes for the channel. Claude reads them in every new thread, and they outrank memory. They are guidance Claude follows closely, not a hard lock: for anything that must never happen, use a setting or an access control rather than a sentence.

* **Good uses:** the channel's purpose; what to pick up without being tagged; tone and length; which sources to answer from; where to file things.
* **How to use them:** select the [Configure link(opens in new tab)](https://claude.com/docs/claude-tag/users/good-habits#configure-claude-for-a-channel) under any Claude reply to open the channel's settings page. By default, anyone in the channel who is a member of your Claude organization can edit the instructions and the [**Respond automatically**(opens in new tab)](https://claude.com/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off) setting on that page. The Respond automatically setting controls whether Claude replies without being tagged. An admin can [make the page read-only for members(opens in new tab)](https://claude.com/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions). Connections are listed on the page too, but only admins and [channel managers(opens in new tab)](https://claude.com/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) can add them. If something you need is locked, ask whoever manages Claude Tag for your channel. Instruction edits apply to new threads, so test in a fresh one.
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
| Replies feel thin or generic | Claude lacks access to the tools your work lives in | Ask whoever manages Claude Tag for the channel to [connect them to this channel(opens in new tab)](https://claude.com/docs/claude-tag/admins/add-connections). Your own connectors can cover your requests, where it’s available to your organization. |
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
