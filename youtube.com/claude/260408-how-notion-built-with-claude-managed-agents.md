---
title: "How Notion built with Claude Managed Agents"
channel: claude
url: https://www.youtube.com/watch?v=45hPRdfDEsI
youtube_id: 45hPRdfDEsI
published: 2026-04-08
duration: "3:40"
captions: en
---

# How Notion built with Claude Managed Agents

[![How Notion built with Claude Managed Agents](https://img.youtube.com/vi/45hPRdfDEsI/hqdefault.jpg)](https://www.youtube.com/watch?v=45hPRdfDEsI)

<details>
<summary>자막: How Notion built with Claude Managed Agents (3:40)</summary>

[00:00]
Hi, I'm Eric.
I'm a product manager at Notion,
and I work on our agents
and agent orchestration.
I had 30 tasks to make a prototype.
I took all of that
and just drag it to start, and it was
like a Claude running wild.
I was like, oh,
I don't need to watch this.
So I got like a snack.
I came back and like,
all the prototypes were made.
That was sort of the unlock.
We want Notion to be
the agent orchestration platform.
Notion is such a good place
for human and agent collaboration.
You bring the right agent together
for the job, and we help to manage
all of your workflows.
We were really excited about bringing managed agents into Notion,
because Claude is really good at complex,
long running tasks.
If you work to roll it up yourself,
it's like a mega brain engineering effort.
You need like a PhD in all of this
to make it work.
And so the managed agent product was great
because it makes it really plug and play

[00:01]
to bring in Claude.
It runs the sessions in the cloud.
We just pull in the API
and it works for our customers.
What that means is that they can kick off
a ton of jobs in Notion.
I'd love to show a use case of how
we use managed agents
to build agent orchestration in Notion.
So this example is something
that a lot of our non-technical users do,
which is they'll onboard clients.
Let's take a fictitious client
called Harbor and Pine.
They are a lifestyle brand
and now here are all the action items.
We have within Notions a custom agent,
and we've basically
given it all of the client databases
and task boards.
So it has the full context to onboard,
and it helps us in the onboarding
workflows for clients behind the scenes.
This agent has Claude as well.
It is pulling in all the contexts
within notion to go and generate this.
And so what I want to do
is call upon the client onboarding manager
and then take these action items,
turn them into tasks so you can see them.

[00:02]
They're all in this task board.
And this is what I like about it.
Like I can take all of this
and just dump it here.
And you can see on the side
that it kicks off a bunch
of agent threads.
And that all basically
feeds into Claude.
And then Claude will then kick off
a Claude session on that.
And so now you can, talk to that
Claude session within Notion here,
which mirrors the actual session
that was kicked off.
So if we go into the Claude platform
so you can see that this session
is running for Claude manage agents,
it kind of gives you a different view
of what's happening.
And it's useful for us
on the development side.
To go and see like what's happening,
but also actually
to feed all of these traces to go
and improve our agent.
Having a harness that can do
long running tasks is really essential.
You might need to run it for 20 minutes
an hour.
That ability to continue to run it,
to manage memory, to have high quality
outputs over time, is a layer that's

[00:03]
super critical on
top of the model itself.
A lot of the tasks are
completed already.
This is what a example
homepage could look like,
and it is pulling in all the contexts
within Notion to go and generate this
and if we wanted to iterate on that,
we can talk to Claude directly here.
That's how we used
managed agents in Notion
to help ourselves and help our customers.
So the managed
agent product is
like a playground for me.
And I just really cool to be able to
kick off all these jobs
at the same time.
I just love building cool s#!t.

</details>
