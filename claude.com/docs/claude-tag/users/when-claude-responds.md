<!-- source: https://claude.com/docs/claude-tag/users/when-claude-responds -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Claude replies without an @-mention in DMs, in any thread it’s already part of, and to channel messages it judges warrant a reply. It’s an ambient presence in the channel, and the @-mention is how you guarantee a response, not a requirement for one. Claude also [turns unprompted replies off on its own](#when-claude-quiets-itself) in a channel whose messages stop giving it anything to respond to. Any channel member can quiet Claude further, give it [standing work that posts on a schedule](https://claude.com/docs/claude-tag/users/proactivity), or remove it from the channel.

##  What triggers a response

Where you send the message decides whether you need the mention.

| Where you write | Replies without an @-mention? |
| --- | --- |
| A DM with Claude | Always. Every message is addressed to Claude already |
| A thread Claude is already in | Yes, unless you’ve [quieted the thread](#quiet-one-conversation). Once Claude has joined, every reply there reaches it without another mention |
| A channel, top-level | Sometimes, when it can answer a question or pick up a task. Include `@Claude` to guarantee a reply, or [turn unprompted replies off](#quiet-the-whole-channel) |

All of this is adjustable. You can [quiet a single thread](#quiet-one-conversation), [quiet unprompted replies across a channel](#quiet-the-whole-channel), or tell Claude which kinds of messages to respond to.
For work that should happen without anyone typing a message, use a [routine](https://claude.com/docs/claude-tag/users/proactivity): scheduled posts, channel watches, and pull-request subscriptions run on their own trigger and post into the channel.

##  The name on a reply

Claude doesn’t post every reply under the same display name. The name shows which kind of work produced the reply, in two forms:

* **Claude**, the name alone: the reply comes from Claude’s ambient presence in the channel, including unprompted replies
* **Claude** followed by a short description of the task in square brackets: the reply comes from a [working session](https://claude.com/docs/claude-tag/concepts/how-it-works) handling that task in its thread. The description changes with every task, so a channel might show something like `Claude [reviewing the launch checklist]`, `Claude [debugging a failing deploy]`, or `Claude [summarizing customer feedback]`.

##  Make a channel quieter

If Claude is replying to messages that weren’t meant for it, turn that down from inside the channel.

###  Quiet one conversation

Tell Claude in the thread to respond only when mentioned.

```
@Claude only respond when I @-mention you
```

Claude stops following that thread, and the rest of the channel is unaffected. This is the fix when one busy thread is the noise. The [`!mute` command](https://claude.com/docs/claude-tag/users/commands#mute-or-unmute-a-thread-or-channel) goes further and silences the thread entirely; any direct `@Claude` mention turns it back on.

###  Quiet the whole channel

Save a mention-only instruction to channel memory.

```
@Claude remember for this channel: only respond when someone @-mentions you directly.
```

Claude confirms what it saved, and the instruction applies to everyone’s threads in the channel, not only yours.
Threads it already joined keep forwarding replies; quiet those individually with the in-thread line above. In channels where Claude has a session of its own at the top level, [`!mute`](https://claude.com/docs/claude-tag/users/commands#mute-or-unmute-a-thread-or-channel) run there also stops unprompted replies until someone runs `!unmute`.

###  Remove Claude Tag from the channel

When quieting isn’t enough, end Claude’s presence in the channel.

```
/remove @Claude
```

Claude can no longer read or post in that channel. Any member can run this unless your Slack admin restricts the command. Admins have further options, through full removal from the workspace, on [Restrict where Claude Tag operates](https://claude.com/docs/claude-tag/admins/restrict-access).

##  When Claude quiets itself

When a channel’s messages stop giving Claude anything to respond to, with no questions it can answer and no tasks it can pick up, Claude turns unprompted replies off there on its own. Mentioning `@Claude` turns unprompted replies back on.
A [mention-only instruction saved to channel memory](#quiet-the-whole-channel) stays in effect until someone changes it.

##  Messages that never get a reply

A few cases produce silence even when the message includes a mention:

* **Editing a message to add the mention.** An edit doesn’t trigger a response. Delete the message and send a new one with `@Claude` included.
* **Channels with guest accounts.** By default, Claude is off in channels that include guests; your admin can turn it on per scope. Ask whoever runs your Claude plan, or send them [the guest access setting](https://claude.com/docs/claude-tag/admins/restrict-access#restrict-guest-channels).
* **Channels shared across workspaces connected to different Claude organizations.** Every workspace where Claude runs is connected to a Claude organization, the account a company sets up for Claude. When a channel is shared across workspaces connected to different Claude organizations, Claude won’t reply there and posts a refusal message instead. You can’t tell from Slack how a workspace is connected; the refusal message itself is the signal. Use a channel that belongs to one workspace, or send Claude a DM.
* **Slack Connect channels.** Channels shared with another company are always off.

When the workspaces sharing a channel all belong to one Claude organization, Claude replies there, but with only your organization’s default access and settings. The repositories, instructions, and memory set up for that channel or its workspaces don’t apply, and Claude posts a notice in the thread explaining this from time to time. The guest check above still applies first where guest access is restricted.
To confirm a quieting instruction saved, ask `@Claude what do you remember about responding in this channel?`; [What Claude Tag remembers](https://claude.com/docs/claude-tag/users/memory) covers where instructions like these are stored and how to change them.

##  Related resources

* [Customize Claude Tag](https://claude.com/docs/claude-tag/admins/customize): the settings only an admin can change, if channel memory isn’t enough
* [Restrict where Claude Tag operates](https://claude.com/docs/claude-tag/admins/restrict-access): the admin-side controls, from guest channels to full removal
