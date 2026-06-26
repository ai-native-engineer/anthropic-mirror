<!-- source: https://claude.com/docs/claude-tag/users/when-claude-responds -->

@-mentioning Claude guarantees a response. Claude can also auto-respond. It may reply to a top-level channel message that doesn’t mention it when it judges that an unprompted reply would be useful. Include the mention to guarantee a response. After the first mention in a thread, it follows the rest of that thread and may reply without another mention. Any channel member can quiet Claude further, give it [standing work that posts on a schedule](/docs/claude-tag/users/proactivity), or remove it from the channel.

##  What triggers a response

In channels where the app has been added, an @-mention guarantees a response. A top-level message without a mention may still get an unprompted reply when Claude judges one is warranted, but isn’t guaranteed to. Once a thread is active, Claude follows replies in that thread without another mention; quiet that per thread or per channel with the instructions below.
For work that should happen without anyone typing a message, use a [routine](/docs/claude-tag/users/proactivity): scheduled posts, channel watches, and pull-request subscriptions run on their own trigger and post into the channel.

##  Make a channel quieter

If Claude is replying to messages that weren’t meant for it, turn that down from inside the channel.

###  Quiet one conversation

Tell Claude in the thread to respond only when mentioned.

@Claude only respond when I @-mention you

Claude stops following that thread, and the rest of the channel is unaffected. This is the fix when one busy thread is the noise.

###  Quiet the whole channel

Save a mention-only instruction to channel memory.

@Claude remember for this channel: only respond when someone @-mentions you directly.

Claude confirms what it saved, and the instruction applies to everyone’s threads in the channel, not only yours.
Threads it already joined keep forwarding replies; quiet those individually with the in-thread line above.

###  Remove Claude Tag from the channel

When quieting isn’t enough, end Claude’s presence in the channel.

/remove @Claude

Claude can no longer read or post in that channel. Any member can run this unless your Slack admin restricts the command. Admins have further options, through full removal from the workspace, on [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access).

##  Messages that never get a reply

A few cases produce silence even when the message includes a mention:

* **Editing a message to add the mention.** An edit doesn’t trigger a response. Delete the message and send a new one with `@Claude` included.
* **Channels with guest accounts.** By default, Claude is off in channels that include guests; your admin can turn it on per scope. Ask whoever runs your Claude plan, or send them [the guest access setting](/docs/claude-tag/admins/restrict-access#restrict-guest-channels).
* **Channels shared across workspaces.** Claude won’t reply in a channel that spans more than one workspace in your Enterprise Grid, or that more than one Claude-connected workspace shares. You’ll see a refusal message instead. Use a channel that belongs to one workspace, or send Claude a DM.
* **Slack Connect channels.** Channels shared with another company are always off.

To confirm a quieting instruction saved, ask `@Claude what do you remember about responding in this channel?`; [What Claude Tag remembers](/docs/claude-tag/users/memory) covers where instructions like these are stored and how to change them.

* [Customize Claude Tag](/docs/claude-tag/admins/customize): the settings only an admin can change, if channel memory isn’t enough
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): the admin-side controls, from guest channels to full removal

[Get started](/docs/claude-tag/users/getting-started)[Good habits](/docs/claude-tag/users/good-habits)
