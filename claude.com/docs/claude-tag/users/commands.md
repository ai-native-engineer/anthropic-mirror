<!-- source: https://claude.com/docs/claude-tag/users/commands -->

A command is `@Claude` followed immediately by one of a few exact words starting with `!`. Claude matches the message against that word and runs a fixed action instead of starting a normal turn. `!help`, `!restart`, `!mute`, and `!unmute` must stand alone: adding extra words, as in `!restart` with words tacked on, makes the message an ordinary prompt instead. `!feedback` and `!routines` accept text after the command, covered below.

##  See the commands available to you

```
@Claude !help
```

Claude replies with the commands it understands in your workspace. The list can differ by workspace, since a command can be enabled for some workspaces and not others.

##  Restart a stuck or wrong-context session

```
@Claude !restart
```

Use this when a session is stuck, or when it’s carrying context you don’t want the next reply to build on. Claude archives the current session and starts a fresh one in its place.
Every thread Claude takes part in runs a session of its own, holding that one conversation. Some channels have one more session on top of the per-thread ones. That session belongs to the channel itself, and it’s the session Claude works from at the channel’s top level, outside any thread. When Claude [replies to a top-level message no one mentioned it in](/docs/claude-tag/users/when-claude-responds), the channel’s session is the one replying.
Where you run `!restart` picks which session gets replaced:

* **In a thread**, `!restart` replaces that thread’s session. The fresh session rereads the thread, so it keeps what’s in the messages and drops everything else the old one was carrying.
* **At a channel’s top level**, `!restart` replaces the channel’s session. The fresh session picks up from where the old one left off.

Claude confirms once the replacement session is ready. If the restart can’t complete, Claude tells you and you can run `!restart` again.
You need the same access to run `!restart` that you’d need to message the session directly; someone who can only observe a thread can’t restart it.

##  Mute or unmute a thread or channel

```
@Claude !mute
```

Where you run `!mute` sets what goes quiet:

* **To quiet one thread**, run `!mute` in that thread. Claude stops replying there; other threads and the rest of the channel are unaffected.
* **To quiet a whole channel**, run `!mute` at the top level of a channel that has [a session of its own](#restart-a-stuck-or-wrong-context-session), where Claude posts at the top level outside threads. Claude stops posting unprompted there, including [routine](/docs/claude-tag/users/proactivity) posts, but still answers direct mentions.

Unmute the same way:

```
@Claude !unmute
```

* **A muted thread** also unmutes on any direct `@Claude` mention, so you don’t need `!unmute` before asking something new.
* **A muted channel** stays muted through direct mentions; only `!unmute` at the top level turns unprompted replies back on.

You need the same access to mute or unmute that you’d need to message Claude there.

##  Send feedback

```
@Claude !feedback
```

Opens a form in Slack for sending feedback on Claude Tag to the team that builds it, along with a note on what the report includes. Add words after `!feedback` and Claude carries them into the form as a starting draft, which you can still edit before submitting:

```
@Claude !feedback the channel summary skipped the pinned thread
```

##  List the routines in a channel

```
@Claude !routines
```

Claude replies in the thread with the [routines](/docs/claude-tag/users/proactivity) set up in the channel: the scheduled jobs, watched channels, and other standing work it runs there. The list covers only that channel’s routines.

* **For the current channel**, run `!routines` in that channel.
* **For another channel**, add the channel mention or its ID, as in `@Claude !routines #other-channel`. You need to be a member of that channel, and it must belong to your organization. Claude sends the list in a reply only you can see, so that channel’s routines aren’t posted for everyone in the channel where you asked.

If what follows `!routines` isn’t a channel mention or ID, Claude replies with how to use the command instead.

##  Related resources

* [Set up routines](/docs/claude-tag/users/proactivity): the standing work `!routines` lists, and how to create, edit, or disable it
* [Control when Claude Tag responds](/docs/claude-tag/users/when-claude-responds): what makes Claude reply without any command or mention at all
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): the admin controls that decide who can message Claude at all, including its commands

[Get started](/docs/claude-tag/users/getting-started)[Control when Claude Tag responds](/docs/claude-tag/users/when-claude-responds)
