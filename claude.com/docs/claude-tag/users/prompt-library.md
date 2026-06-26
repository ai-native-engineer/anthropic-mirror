<!-- source: https://claude.com/docs/claude-tag/users/prompt-library -->

These prompts are ready to copy, paste, and adapt: swap in your own channel names, services, and repositories. Each comes with the reason it works, so you can keep the mechanism when you change the words.

##  First messages in a new channel

Ask what Claude can access from this channel:

@Claude what can you access from this channel?

**Why it works**: what Claude can do differs per channel, and without this grounding it may suggest tasks it can’t do here.
Get a personalized starting point:

@Claude learn what you can about my role from this workspace, then tell me three tasks you could take off my plate this week.

**Why it works**: it’s a discovery task with a bounded output. “Three tasks” gives you a list you can judge in ten seconds, and the answer doubles as a menu of next tasks.
Start with a low-stakes task:

@Claude catch me up on this channel since Monday.

**Why it works**: “since Monday” bounds the task, and you can grade the result yourself because you were there.

##  Shape how the channel works

The prompts below set channel-wide behavior that applies to every thread, not just yours.

@Claude remember for this channel: keep replies short, and always include a link to the source.

**Why it works**: “remember for this channel” is the explicit save instruction; preferences mentioned in passing usually aren’t kept.

@Claude stay quiet in this channel unless tagged.

**Why it works**: it’s stated as standing channel behavior, so it persists instead of lasting one conversation.

##  Check and correct memory

@Claude what do you remember about this channel?

**Why it works**: memory is a curated note and Claude decides what’s worth keeping, so checking is the only way to know what stuck.

@Claude that's outdated — forget the entry about the old project name.

**Why it works**: it names the specific entry. “Clean up your memory” makes Claude guess what’s stale; naming the entry doesn’t.

@Claude update your memory for this channel so this doesn't happen again.

**Why it works**: a correction in a thread fixes that thread only. This sentence is what turns it into a standing fix that applies to everyone’s future threads.

##  Manage routines

Create, audit, and stop the scheduled jobs Claude runs in this channel.

@Claude every Friday at 3pm, post a summary of this week's requests: how many, top themes, and anything still unrouted.

**Why it works**: the schedule is specific, and the post’s contents are named, so every rollup has the same shape and is comparable to last week’s. “Anything still unrouted” turns a recap into a sweep: nothing gets dropped silently.

@Claude what routines do you have set up in this channel?

**Why it works**: schedules are channel state, and someone else may have set them up. Auditing first beats creating a duplicate digest.

@Claude disable the daily digest job.

**Why it works**: it names which job. Any channel member can disable a scheduled job; you don’t need to find an admin to stop a noisy routine.

##  Steer work mid-thread

Reply in the same thread; once Claude is working there, you don’t need to @-mention it again.

Status check — what's done and what's left?

**Why it works**: the reply lands in the session that’s running the task, with full context. Asking in a new thread instead queues a second session that knows nothing about the first.

Change of plan: target the staging config instead, and post the diff here before applying anything.

**Why it works**: redirecting in-thread keeps everything the session has already learned. “Post the diff here before applying” adds a checkpoint, so the channel reviews the change before it lands.

Post the draft to the thread, or commit and push what you have, then keep going.

**Why it works**: the thread is durable but [the isolated workspace behind it isn’t](/docs/claude-tag/concepts/how-it-works#what-survives-between-replies). Work posted to the thread or pushed to a branch survives idle recycling; files that exist only in that workspace don’t.

##  Task starters, by shape

Each entry in the use case library gets one starter here; the linked page has the full setup and the reasoning behind its prompts.

| To do this | Paste this |
| [Triage requests](/docs/claude-tag/users/use-cases/triage-requests) | ”remember for this channel: when someone tags you on a request, check whether it duplicates something already reported, answer it directly if the answer exists, and otherwise route it to the right owner with a one-line summary. Track recurring themes.” |
| [Catch up](/docs/claude-tag/users/use-cases/catch-up) | ”what got decided in this thread, and what’s still open?” |
| [Create an artifact](/docs/claude-tag/users/use-cases/create-artifacts) | ”turn this thread into a one-page decision doc” |
| [Track a project](/docs/claude-tag/users/use-cases/track-projects) | ”where are we on the migration? What’s blocked and on whom?” |
| [Answer a data question](/docs/claude-tag/users/use-cases/answer-data-questions) | ”show signup growth by week, and explain the dips discussed above” |
| [Find an answer in the docs](/docs/claude-tag/users/use-cases/find-answers) | ”what’s our policy on data retention, and which doc says so?” |
| [Pull deal state](/docs/claude-tag/users/use-cases/pull-deal-state) | ”what’s the state of the Acme renewal?” |
| [Watch monitors](/docs/claude-tag/users/use-cases/watch-monitors) | ”every morning at 7, check the dashboards and post one line per service” |
| [Fix a bug](/docs/claude-tag/users/use-cases/fix-bugs) | ”in acme/data-pipeline, reproduce the bug in this thread, fix it, and open a draft PR” |

* [Use case library](/docs/claude-tag/users/use-cases): the full setup behind each starter
* [Good habits](/docs/claude-tag/users/good-habits): the habits these prompts are built from
* [Getting started](/docs/claude-tag/users/getting-started): the basics, if you haven’t sent a first message yet

[What Claude Tag remembers](/docs/claude-tag/users/memory)[Browse the library](/docs/claude-tag/users/use-cases)
