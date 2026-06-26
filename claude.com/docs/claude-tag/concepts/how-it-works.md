<!-- source: https://claude.com/docs/claude-tag/concepts/how-it-works -->

Claude Tag is Claude, working inside your team’s Slack channels. An organization Owner gives it its own accounts to the tools your team uses, so it arrives already able to act, and anyone in a channel can tag it into a problem without setting anything up.
When someone tags Claude in with a task, a working session starts for that thread. Claude works through the task and posts the result back into the conversation. It runs in an ephemeral cloud sandbox that Anthropic hosts, not on your local machine or inside your network.
This page covers:

* [Walk through a session](#walk-through-a-claude-tag-session): an annotated example thread showing one task end to end
* [Starting a session](#start-a-session), [tracking progress](#track-claudes-progress), and [steering mid-thread](#reply-in-the-thread-to-steer): what to type, what to watch, and who can redirect
* [Team channels and personal DMs](#team-channels-and-personal-dms): which surface to use, and how access differs between them
* [Key concepts](#key-concepts): agent identity, scheduling, and memory defined
* [Lifecycle of a request](#lifecycle-of-a-request): the five-step loop, [the checklist](#how-the-checklist-updates), [per-channel access](#channel-access), and [scheduled tasks](#one-off-and-scheduled-tasks)
* [Session context and memory](#session-context-and-memory): what Claude reads, what survives idle, and what carries across channels

##  Walk through a Claude Tag session

The thread below is one task end to end in Slack: Jordan tags @Claude into `#launch-week` with a question, a colleague steers mid-thread, and the answer lands in the channel.

# launch-week19 members

J

Jordan9:02 AM

@Claude where are we on launch prep? Pull together what’s still open from this channel.

![](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/logo/clay-spark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=032101c39ca3b1af9f72fc4af8e60d12)

ClaudeAPP9:02 AM

On it. I’ll go through this channel’s open threads and the launch plan.

Done: Read 14 open threadsDone: Cross-checked the launch plan in DriveDone: Listed who each item is waiting onDone: Drafted the status summary

S

Sam9:06 AM

fold in the vendor quotes from last week’s thread too

![](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/logo/clay-spark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=032101c39ca3b1af9f72fc4af8e60d12)

ClaudeAPP9:08 AM

Done. Full status below: eight items closed, three open. The venue contract is the oldest, waiting on legal since the 2nd.

Each of the five moments in that thread shows a piece of how Claude Tag works:

1. **Jordan handed Claude a problem, not a prompt.** Typing `@Claude` in a message that asks for something is what starts a working session.
2. **Claude acknowledged, then went quiet.** The “is thinking…” line and the checklist are the progress surface; the silence between 9:02 and 9:06 was the work happening. [How the checklist updates](#how-the-checklist-updates)
3. **Sam steered Claude without `@`-mentioning it again.** Once a session is active in a thread, it belongs to everyone there. [Reply in the thread to steer](#reply-in-the-thread-to-steer)
4. **The work ran somewhere real, with the channel’s tools.** Reading fourteen threads happened in a sandbox built for this thread, and the launch plan came through this channel’s Drive connection. What a session can reach is set per channel. [Access follows the channel, not the person](#channel-access)
5. **The result is in the thread.** The whole channel can see it, use it, and build on it. [What survives between replies](#what-survives-between-replies)

The rest of this page takes each piece apart.

###  Start a session

To start a session, type `@Claude` in a Slack message and say what you need in that same message (a question to answer, a task to run, a problem to dig into). Jordan’s “`@Claude` where are we on launch prep?” is the whole move. Anyone in the channel can do it.

###  Track Claude’s progress

Once your message sends, an “is thinking…” line at the bottom of the thread means Claude picked it up. What happens next depends on the size of the ask. Questions and one-off requests get a direct reply. A longer task, like Jordan’s, gets a checklist instead. [How the checklist updates](#how-the-checklist-updates) covers how it works and how to read one while it runs.
While a session runs, check in by replying in the same thread. Asking “how’s it going?” in the thread is enough; it reads new replies as it works.
Each delivery ends with an “Open session in Claude” link showing the full record of the work, including every tool call. Anyone in the channel can open the link. The page is read-only; follow-ups go in the Slack thread.

###  Reply in the thread to steer

Anyone in the channel can steer a running session by replying in its thread, not just the person who started it. That is what Sam did in the walkthrough. Without re-mentioning `@Claude` or starting over, he replied in Jordan’s thread, and the session folded his instruction into work already in progress. Add context, redirect the approach, or pick up the result later; a colleague’s thread is yours to continue.
Editing or deleting a message in the thread does not change what Claude has already received. There is no rewind; to back out of something you sent, say so in a new reply, or start a fresh thread for a clean session.

##  Team channels and personal DMs

Where you message Claude determines whose tools and accounts it uses. In a channel, it acts with the connections an organization admin set for that channel, and the work is attributed to its own accounts. In a DM, the same engine runs with your own claude.ai connectors, and the work is attributed to you.

| Working in… | Access | Attribution | Best for |
| --- | --- | --- | --- |
| A channel | The channel’s connections, set by an admin | The agent’s own accounts | Shared work the team should see |
| A DM | Your own claude.ai connectors | You | Personal tasks using your own data |

The Access column is about external systems. A channel session reaches what the channel was granted, and a DM session reaches what your own account is connected to.
Everything below describes channel sessions, where most of the model lives. For the DM side, see [direct message channels](/docs/claude-tag/concepts/agent-identity#direct-message-channels), and for choosing between the two, see [pick the right surface](/docs/claude-tag/users/good-habits#pick-the-right-surface).

##  How Claude Tag differs from Cowork and Claude Code

Anthropic offers several ways to work with Claude on real tasks; they reach the same kinds of systems but through different mechanisms.

|  | Claude Tag | Cowork | Claude Code |
| --- | --- | --- | --- |
| Where | Slack channels | claude.ai chat | Your terminal or IDE |
| Whose access | The team’s: service-account credentials an admin sets per channel | Yours: your personal OAuth connectors | Yours: your local credentials and filesystem |
| Who sees the work | Everyone in the channel | Just you | Just you |
| Best for | Shared work the team should see and steer | Personal research and drafting | Hands-on coding in your own checkout |

The short version: **team work → Claude Tag; personal work → Cowork or Claude Code.** Claude Tag’s connections authenticate the agent itself with service accounts, not any person. Personal connectors apply in a Claude Tag DM, which runs on your own claude.ai account, the same way Cowork does.

##  Key concepts

Three ideas recur across this page and the rest of these docs.

* **Agent identity**: in channels, Claude acts under its own service accounts that an admin provisions, not as the person who asked. What it can reach follows the channel, not the user. See [How agent identity works](/docs/claude-tag/concepts/agent-identity).
* **Scheduling and long-running work**: a task can run on a schedule, trigger on a repository event, or keep going across many turns in one thread. The same channel access applies whether a person or a schedule started it. See [Set up routines](/docs/claude-tag/users/proactivity).
* **Memory**: what Claude learns in public channels is saved as workspace memory that any channel can use; private channels keep their own. See [What Claude remembers](/docs/claude-tag/users/memory).

##  Lifecycle of a request

Every session, in any channel, follows the same five-step loop.

1. **The session starts.** Someone tags `@Claude` with a task, or a [scheduled routine](/docs/claude-tag/users/proactivity) runs.
2. **A sandbox builds.** Anthropic builds an isolated working environment for this thread.
3. **The working loop runs.** Claude works through the task with the channel’s access, editing its checklist in place.
4. **The result lands in the thread.** An answer, a doc, a chart, or a pull request.
5. **A quiet period follows.** The sandbox is released while the thread persists; a new reply rebuilds it and starts the loop again.

![Flow diagram of one session in five numbered steps. Step 1, tag Claude in with an @Claude message carrying a task. Steps 2 and 3 happen inside the sandbox. Step 2, a sandbox builds, one per thread; step 3, the working loop runs through the task's steps using the channel's access. Step 4, Claude posts the result in the thread as an answer, a doc, a chart, or a pull request. Step 5, a dashed quiet period follows, where the sandbox is released while the thread persists. A dashed return arrow from the quiet period back up into the sandbox shows that a new reply rebuilds it and the loop continues.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/session-loop.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=436dd451c4ab3ab0f0b072f85051e844)
![Flow diagram of one session in five numbered steps. Step 1, tag Claude in with an @Claude message carrying a task. Steps 2 and 3 happen inside the sandbox. Step 2, a sandbox builds, one per thread; step 3, the working loop runs through the task's steps using the channel's access. Step 4, Claude posts the result in the thread as an answer, a doc, a chart, or a pull request. Step 5, a dashed quiet period follows, where the sandbox is released while the thread persists. A dashed return arrow from the quiet period back up into the sandbox shows that a new reply rebuilds it and the loop continues.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/session-loop-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=616c51832cbb9bc57fe6da5346c6ac85)
Steps 1 and 2 are [starting a session](#start-a-session): a message tags Claude in, and a sandbox builds for that thread. Step 3, the working loop, is [the checklist](#how-the-checklist-updates) below. Steps 4 and 5, the result and the quiet period that follows, are covered in [What survives between replies](#what-survives-between-replies).
Every session runs in an ephemeral sandbox Anthropic hosts, a real working environment where it can read documents, run code, build charts, and open pull requests. Claude clones your repositories into the sandbox, edits them there, and pushes changes back to your Git host as a branch or pull request. The sandbox runs the same engine that powers Claude Code on the web, Anthropic’s agent for writing and running code, which is why the results are working artifacts rather than chat.
Two threads in the same channel are two separate sessions with separate sandboxes; sessions don’t share state directly.
Even with nothing connected, every session starts from the same baseline.

* It reads its own thread and the channel’s history, including pinned items
* It searches the workspace’s content
* It writes and runs code inside the sandbox, which is how a chart comes out of a posted CSV, or a doc out of a long thread, with nothing wired up

###  What Claude posts back

Claude posts each session’s result in the thread you asked in, choosing the form that fits the work.

| Form | What it is | When you see it |
| --- | --- | --- |
| A reply | An answer, list, or summary as a Slack message | Questions and short results |
| A file or chart | Attached to the thread the way anyone shares a file | Data, images, generated documents |
| A page kept current | Any of the above, edited in place over time | Digests, indexes, standing reports |

For code work, the result is usually a draft pull request opened under the Claude GitHub App, with the link posted in the thread.

###  How the checklist updates

For a longer task, Claude’s first reply is a checklist, a live task list that it edits in place as it goes. Slack does not send notifications when a message is edited, so the thread can look frozen while the list is still moving.
A quiet thread usually means Claude is mid-task, not stuck. Open the thread. Checklist items checked off since you last looked mean the work is moving. In the walkthrough, nothing new arrived in anyone’s notifications between 9:02 and 9:06, while the checklist ticked through fourteen threads of reading. If the work hits a wall, that arrives as a reply, not as silence.

###  Channel access

Connections extend a session’s reach into your own systems. Which ones a session gets follows the channel, not the person asking. An organization admin attaches access to a scope (the organization, a workspace, or a single channel), so the same request can do more in one channel than in another, and everyone in a given channel works with the same capability.

####  How to identify access

Because access is set per channel rather than per person, the way to find out what a session can reach is to ask it, not to guess from your own permissions.

* **Ask what Claude can reach.** In any channel, `@Claude what can you access from this channel?` lists its current reach.
* **If Claude cannot reach something, the channel was not granted access.** Another channel may have the access, and an organization Owner can add it. [How agent identity works](/docs/claude-tag/concepts/agent-identity) covers the model.
* **Personal connectors apply only in DMs.** A connection an admin attaches to a channel is separate from a connector on your personal claude.ai account; anything on your own account works in your DMs, not here.

###  One-off and scheduled tasks

A session starts the same way whether a person triggers it or a schedule does. A mention starts a session for that one task, and the sandbox is released once it finishes. A routine runs the same loop on a schedule, a channel watch, or a repository event, with the channel’s connections, so a recurring digest or watcher gets the same access a typed request would. See [set up routines](/docs/claude-tag/users/proactivity).

##  Session context and memory

Every session runs the same lifecycle; what varies by place and thread is [what it can see](#conversation-context), [what survives idle](#what-survives-between-replies), and [what it remembers](#channel-and-workspace-memory).

###  Conversation context

A session reads its own thread and its channel. Mentioning `@Claude` partway into an existing thread gives it up to 50 messages from the start of the thread (the root plus the oldest replies, with other bots’ replies filtered out). In long threads, the most recent messages before your mention can fall outside that window, so restate anything critical.
Claude works in channels it has been added to, but workspace search can still find messages by keyword from public channels it’s not a member of (the same search any Slack user has). Finding something is broader than being able to act somewhere; to have it participate in a channel directly, invite it with `/invite @Claude`.

###  What survives between replies

The thread is durable; the sandbox is not. When a session is idle, its sandbox is released, and it is rebuilt when the next message arrives.
![Timeline with two lanes. The Slack thread lane is one continuous bar that persists from the moment a task starts. The sandbox lane below it is segmented, built when the task starts, released while the thread goes quiet, and rebuilt fresh when someone replies.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/session-lifecycle.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=9a56231787b03f179e8d552d887778fc)
![Timeline with two lanes. The Slack thread lane is one continuous bar that persists from the moment a task starts. The sandbox lane below it is segmented, built when the task starts, released while the thread goes quiet, and rebuilt fresh when someone replies.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/session-lifecycle-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=0693a90b98baa729dcacfd35261f6494)

|  | Survives idle periods |
| The conversation and its context | Yes |
| Channel memory | Yes |
| Work pushed, posted, or opened as a PR | Yes, in the external system |
| Files that exist only in the sandbox | No. Claude recreates them if asked. |

For long tasks, ask it to push branches and post drafts as it goes, so deliverables are saved somewhere durable while the work is still running. See [Good habits](/docs/claude-tag/users/good-habits#give-every-task-a-definition-of-done).

###  Channel and workspace memory

Memory follows places the same way access does, and it accumulates for the team rather than for any individual.
Memory from public channels is shared across the workspace, so a decision recorded while working in #launch-week is available when someone asks in #gtm-west. When Claude cites something from a channel you have never used it in, it is reading workspace memory, not a record about you.
Private channels read workspace memory while working, and what they save is written to that channel’s own store rather than the workspace store.
To see what it holds, ask `@Claude what do you remember about this channel?`. Anyone in the channel can correct or remove entries. [What Claude Tag remembers](/docs/claude-tag/users/memory) covers reading, correcting, and adding to memory.
The whole model so far fits in one picture, with access set at the scope, memory shared from public channels, work in progress per thread, and DMs outside all of it.
![Diagram showing three nested levels. A scope container holds two channels, #platform-eng and #gtm-west, and each channel holds its own threads, like 'fix checkout latency' or 'pull deal state'. The private channel is marked with a lock. Callouts mark what lives at each level (identity and access at the scope; memory, shared from public channels across the workspace while private channels keep their own; and work in progress at the thread). A DM with Claude sits below, outside every scope, and runs on your own account.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/three-levels.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=511231c5561da4ade26f91cd395488fa)
![Diagram showing three nested levels. A scope container holds two channels, #platform-eng and #gtm-west, and each channel holds its own threads, like 'fix checkout latency' or 'pull deal state'. The private channel is marked with a lock. Callouts mark what lives at each level (identity and access at the scope; memory, shared from public channels across the workspace while private channels keep their own; and work in progress at the thread). A DM with Claude sits below, outside every scope, and runs on your own account.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/three-levels-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=e593920bd85a97c285a56f7b9d3e5019)
DMs are outside this picture; they run on your own account, as covered in [Team channels and personal DMs](#team-channels-and-personal-dms) above. Admins can disable DMs organization-wide; see [Allow or disable direct messages](/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages).

* [Getting started](/docs/claude-tag/users/getting-started): hand Claude your first task
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): why access follows the channel, and how credentials stay out of the sandbox
* [Good habits](/docs/claude-tag/users/good-habits): write tasks that survive the sandbox lifecycle

[Overview](/docs/claude-tag/overview)[How agent identity works](/docs/claude-tag/concepts/agent-identity)
