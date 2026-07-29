<!-- source: https://claude.com/docs/claude-tag/users/getting-started -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Claude Tag is Claude working in your Slack workspace. You hand it work by writing a message where Claude is, and Claude carries it out in that thread. An `@Claude` mention guarantees a response in a channel, but it isn’t required everywhere. DMs and threads Claude is already in reach it without one. There’s nothing for you to install or configure; if `@Claude` is in your channel, you can use it (unless your admin has [restricted who can invoke Claude](https://claude.com/docs/claude-tag/admins/restrict-access#members)).

##  When to tag Claude in a channel versus a DM

Where you tag Claude decides whose tools it uses and who sees the result.

* **Channel** for shared team work. The work happens in the open, so anything Claude does in the thread, including its checklist and results, is visible to everyone in the channel, and anyone can reply to steer the work. An admin sets what Claude can reach in each channel, and everyone who asks there gets the same access. By default you don’t need a Claude account to tag Claude in a channel; the work bills to the organization. An admin can [restrict who can invoke Claude](https://claude.com/docs/claude-tag/admins/restrict-access#members).
  + Example: `@Claude where are we on the launch checklist? Pull what's still open from this channel and #design-review.`
* **DM** for personal tasks. A DM runs on your own claude.ai account with [your own connectors](https://claude.com/docs/connectors/overview). Every DM message reaches Claude without an @-mention. DMs are one-to-one only; group DMs aren’t supported.
  + Example: `Pull my afternoon meetings from my calendar and draft a one-line prep note for each.`

See [team channels and personal DMs](https://claude.com/docs/claude-tag/concepts/how-it-works#team-channels-and-personal-dms) for the full comparison.
If your workspace previously used the earlier Claude in Slack app, see [how Claude Tag differs](https://claude.com/docs/claude-tag/admins/migrate-from-earlier) for what has changed.

##  Add Claude to a channel

Claude only works in channels it’s been added to. To add it, anyone in the channel can run:

```
/invite @Claude
```

Run the command in the channel’s message box. Slack rejects `/invite` sent from inside a thread.
Or mention `@Claude` in a message; Slack will prompt you to add it.

##  Check that Claude is working

Mention `@Claude` in any channel where it’s been added. In the Slack message box, send:

```
@Claude what can you access from this channel?
```

A reply means it’s running there, and the answer tells you what it can reach.

###  What you see when Claude first joins a channel

When a person first invites Claude to a channel, it posts a short intro on its own: it reads the channel’s history and suggests a few tasks it could pick up. The intro doesn’t post when a bot adds Claude, in org-shared channels, or in channels that already have memory.
Each reply ends with a footer showing an **Open session in Claude** link (the full record of that task), a **Configure** link (opens a page where you can [tailor how Claude works in this channel](https://claude.com/docs/claude-tag/users/good-habits#configure-claude-for-a-channel)), and which model handled the reply. You can [choose a different model](https://claude.com/docs/claude-tag/users/models) yourself, and admins [set the default model for each channel](https://claude.com/docs/claude-tag/admins/customize#choose-the-model-for-a-scope).

| If you see | It means | Do this |
| --- | --- | --- |
| Typing `@Claude` doesn’t show **Claude** with an **APP** badge in the suggestion list | The Claude app isn’t installed in your workspace | Ask your Slack admin to install the Claude app, and send them [the installation guide](https://claude.com/docs/claude-tag/admins/pair-workspace#install-and-pair) |
| The mention sends but Claude doesn’t reply | Setup isn’t finished for this channel | Ask your Claude organization admin to enable Claude Tag for this channel, and send them [the setup guide](https://claude.com/docs/claude-tag/admins/setup-overview) with the channel name |
| Claude replies “I couldn’t find a Claude Code environment for your account” | Your own claude.ai account has no cloud environment yet; this appears in DMs, which run on your account rather than the organization’s | Sign in at [claude.ai/code](https://claude.ai/code) once, then try again |

##  Hand Claude a task

Every interaction has the same shape. You mention `@Claude` with a task, Claude works on it in the thread, and Claude posts the result there.

```
@Claude learn what you can about my role from this workspace, then tell me three tasks you could take off my plate this week.
```

An “is thinking…” line appears at the bottom of the thread when Claude picks the task up, and it replies with results; a multi-step task also gets a checklist it updates as it works. A quiet thread after the “is thinking…” line means Claude is working, not stuck; long tasks can take a minute or more before the first reply.
Once Claude is in a thread, you don’t need to @-mention it again; it reads every reply in that thread.
Read Claude’s work before you use it, in proportion to what’s at stake. A summary you can skim; something going to a customer or changing a system gets a careful read. If a result needs checking, ask it to show its work in the same thread.
The work runs on Anthropic’s servers, so it continues after you close Slack.
Replies in the thread reach Claude without re-mentioning. If the thread looks idle, Claude is usually still working; see [how to read its progress](https://claude.com/docs/claude-tag/concepts/how-it-works#track-claude%E2%80%99s-progress).

##  What Claude can see

After you’ve handed Claude a task, the first question is what it has to work with. The short version: it reads the thread you tagged it in, it can search your workspace’s public channels, and anything beyond Slack depends on what your admin connected.

| What you give Claude | Can Claude read it? |
| --- | --- |
| Messages in this thread | Yes. Mentioning it mid-thread also gives it the thread’s earlier messages |
| An image or screenshot you attach | Yes |
| Other public channels in your workspace | By searching only, the same way a person searches Slack; Claude can find a message by keyword but can’t read a channel’s full history unless it’s been added there |
| Private channels and DMs | Only from inside them. Adding Claude to a private channel lets it work there, but the channel stays unreadable from any other channel or DM. |
| A link you paste, like a Google Doc or a webpage | Only if your admin allowed that site for this channel. If not, Claude tells you it can’t reach it. For files in your personal Drive or Google account, DM Claude instead; [a DM uses your own connectors](https://claude.com/docs/claude-tag/concepts/agent-identity#direct-message-channels) |
| A Slack canvas | No |
| A message you edited after sending | Yes. Each edit sends Claude a note showing the text before and after the edit. Claude reads the note but doesn’t act on it, so say a correction in a new reply. Deleting a message doesn’t notify Claude |

The fastest way to find out for your channel is to ask: `@Claude can you read the doc I just linked?` gets you a yes or a “that site isn’t allowed here.”

Slack doesn’t expose personal account settings (your sidebar, notification preferences, channel membership, or DMs between you and other people) to apps. If you want help organizing channels, paste or screenshot the list and Claude can propose a scheme you apply yourself.

###  Which messages Claude reads

* An @-mention guarantees a response. Claude may also respond to a message that doesn’t mention it when it judges a reply is warranted; include the mention to guarantee one. It receives the thread’s root message and earlier replies for context when you mention it mid-thread; for details on the window, refer to [what Claude sees when you mention it](https://claude.com/docs/claude-tag/concepts/how-it-works#conversation-context).
* Once mentioned in a thread, Claude follows the rest of that thread and may reply without another mention.
* While working on a task, Claude can search the workspace’s public channels by keyword, the same way a person searches Slack. It can’t read a channel’s full history unless it’s been added there.

To quiet Claude in a thread or remove it from a channel, see [Control when Claude Tag responds](https://claude.com/docs/claude-tag/users/when-claude-responds).

##  Give Claude standing instructions

Set instructions for a channel by telling Claude there, the way you’d ask anyone on the team:

```
@Claude remember for this channel: keep replies short, and always include a link to the source.
```

The instruction saves to channel memory and applies to everyone’s threads. Public-channel memory is also [shared across your workspace](https://claude.com/docs/claude-tag/users/memory). Verify with “what do you remember about this channel?”

##  Related resources

* [Use case library](https://claude.com/docs/claude-tag/users/use-cases): every shape of work, each with the prompts to paste
* [Good habits](https://claude.com/docs/claude-tag/users/good-habits): how to write tasks that finish
* [Set up routines](https://claude.com/docs/claude-tag/users/proactivity): once a task works, have Claude run it on its own schedule
* [Commands](https://claude.com/docs/claude-tag/users/commands): exact words starting with `!` that run a fixed action, like `!restart` for a stuck session
