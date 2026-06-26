---
title: "Context Management in Claude Code"
channel: claude
url: https://www.youtube.com/watch?v=eW3oTyfeWZ0
youtube_id: eW3oTyfeWZ0
published: 2026-05-18
duration: "3:30"
---

# Context Management in Claude Code

[![Context Management in Claude Code](https://img.youtube.com/vi/eW3oTyfeWZ0/hqdefault.jpg)](https://www.youtube.com/watch?v=eW3oTyfeWZ0)

<details>
<summary>자막: Context Management in Claude Code (3:30)</summary>

[00:00]
Context is Claude's working memory.
Every file it reads, every command it
runs, every message you send, it all
takes up space in the context window.
Think of the context window as the
amount of space that Claude can hold in
its memory.
Whenever you enter a prompt, Claude
reads a file, runs a tool call, gets a
tool call result. This is added onto the
context window. And since there's only a
finite amount you can can put in the
context window, it becomes extremely
important to optimize this as much as
possible.
Now, when you approach this limit, the
context window is automatically
compacted.
Compaction will summarize important
details and remove the unnecessary tool
call results and free up a lot of space
in your context window.
Do note though that this could
potentially lose details in your
previous conversation.
You can run the compaction manually as
well with the {slash} compact command.

[00:01]
This will compact everything that you've
done up to that point, which could be
handy if you want to clear up context
space, but also have a memory of what
you previously worked on.
If you want to completely start from
scratch without memory of what was
previously worked on, you can also run
{slash} clear and that will remove
everything, starting from scratch.
To check the state of your context, run
the {slash} context command. Here,
you'll get a big picture of how large
your context size is, the different
categories that are taking up the most
context, and a graphic showing you all
of this.
A general rule of thumb is when you're
working on a specific feature and are
going over the context window, but need
to continue, then compact.
Keeping the context relevant for this
feature is important when continuing
development.
If you have finished the plan and want
to start on a new feature, then clear.
You don't want the previous conversation
to present bias in anything new that you
want to create. For things that you do
want Claude to remember in other
sessions, put it in the Claude.md file.

[00:02]
That way, it doesn't have to rediscover
things from scratch all over again.
Be specific. The irony behind writing a
smaller prompt is that it in the long
run, it will take up more context.
Without being explicit, Claude is forced
to look around your code base more and
do his own thinking, which takes up a
lot more context window space than if
you were just a little bit more clear
with a sentence or two.
MCP servers load all of the tools
available into context by default. So,
if you have a lot of MCP servers for
things that are unrelated to the
project, it might be worth turning them
off. You can also try out skills, which
works similarly to MCP servers, but
doesn't put the entire thing into
context, saving you space.
Sub agents run in parallel with your
main agent, but has a complete separate
context window. So, for tasks that
require an answer without the journey,
like where is the authentication
endpoints located, you can have the sub
agent do the work and return just a

[00:03]
summary to your main agent.
Managing context within Claude code is
crucial. Use /compact to summarize long
sessions and /clear to start fresh. To
use your context window effectively, be
specific with what you want.
>> [music]
>> Check what's using your current context
window and use sub agents to delegate
tasks you only need the answer for.

</details>
