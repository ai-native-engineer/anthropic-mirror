---
title: "Memory and dreaming for self learning agents"
channel: claude
url: https://www.youtube.com/watch?v=IGo225tfF2I
youtube_id: IGo225tfF2I
published: 2026-05-21
duration: "21:34"
---

# Memory and dreaming for self learning agents

[![Memory and dreaming for self learning agents](https://img.youtube.com/vi/IGo225tfF2I/hqdefault.jpg)](https://www.youtube.com/watch?v=IGo225tfF2I)

<details>
<summary>자막: Memory and dreaming for self learning agents (21:34)</summary>

[00:00]
[music]
>> Hello. Thank you for joining us today.
I'm excited to
kick things off on the breakout stage.
My name is Ravi and I lead the API
knowledge team within platform at
Anthropic.
And since joining Anthropic last year,
my focus has been creating the building
blocks for agents to interact with many
forms of knowledge, ranging from the
context window itself to skills, files,
and even content on the web.
And we recently released two features
that I'm most excited about.
Memory and dreaming.
We now have the building blocks for
agents to learn over time and improve
from one task to the next.
And I'll talk about why we think memory
is important, how we designed it, and

[00:01]
we'll close out with dreaming, our new
frontier memory feature.
Oop.
There we go.
But first,
a quick timeline of milestones that got
us here.
And the important thing is
models have been improving and agents
are capable of completing tasks that
take many, many hours and are
increasingly complex.
So in 2024,
we released Model Context Protocol, MCP.
And this gave models access to external
tools and data in a principled way.
In 2025, we released Claude Code and the
Agent SDK, which lowered the barrier to
using and building agents.
Which, as an aside, that blows my mind
that that was in 2025. It honestly feels
like a lifetime ago.
Later that year, we launched skills,
which gave model else
>> [clears throat]
>> a models a

[00:02]
generic abstraction for unlocking and
effectively bolting on new capabilities
to complete specific tasks.
Last month, we released Claude managed
agents, a platform for reliably running
agents that takes care of the hard
parts.
Now,
the important through line here is that
agents can do more, and they can operate
over longer and longer time horizons.
So,
in 2025, Meter released a study saying
the length of tasks that agents can
complete is doubling every seven seven
months.
And we're seeing this happen.
But managing context over long horizon
tasks is still a work in progress, and
that's where memory comes in.
Memory lets agents learn.
It lets agents carry forward learnings
from their previous tasks.
And

[00:03]
in the simplest sense,
imagine a set of tasks. Task one, task
two, task three, and so on.
The goal is for performance to improve
from one task to the next.
In the base case, without something like
memory, performance on each task might
be similar.
Because every agent is just starting
from the same slate.
In the optimal case, performance
improves from task one to two, task two
to three, and so on. That's the goal.
Learning from task to task, but also
from environment to environment, and
agent to agent.
So, with memory, agents can learn from
common strategies and previous mistakes.
They can learn from the tools they have
access to, or code bases and files.
And finally, they can transfer these
learnings to and from other agents.
Think swarms of agents contributing to
and maintaining a shared understanding

[00:04]
of the organization they work in.
This is the dream.
So, we recently launched memory for
Claude managed agents.
And this is a major step towards this
vision.
It gives developers a frontier memory
system that is built to maximize
intelligence out of the box, and it
supports multi-agent systems
all with enterprise control and
observability.
And we built memory in partnerships with
several teams that are using managed
agents. And the results speak for
themselves. Rakuten saw a 97% decrease
in first pass errors in agents deployed
in production.
WiseDocs
reduced common issues using
cross-session memory in their document
document verification pipeline. And the
through line here and the common

[00:05]
feedback we get is that our memory
primitive allows teams to focus on
building the product, not the infra.
And all while reaping the benefits of
increased intelligence that comes along
with better memory.
Now,
you might be thinking, is memory really
new?
Rightfully so.
Memory is a concept that's not entirely
new, but our approach for it with agents
has greatly evolved.
And previously,
we built memory
focusing on capabilities in the harness.
So, you might be familiar with Claude.md
for Claude code, or dedicated memory
tools in the SDKs.
But,
one pattern we're seeing is that as
models improve, we really just want to
get out of Claude's way,
similar to what we did with skills.
And skills was a very basic format that

[00:06]
was highly flexible, and it created
endless possibilities, and the model
understood how to operate with it.
And so with memory, we've leaned into
that same direction
with files.
So, let's talk about some of the
capabilities that we designed memory
around.
So, right now, with the current set of
models, we know a few things.
Models and Claude are great at
navigating virtual environments and a
file system.
And Claude is also very capable at using
familiar tools like bash and grep to
read, update, and organize files.
Opus 4.7, our uh that we launched last
month, is a state-of-the-art model at
file system-based memory.
And it's increasingly capable of
discerning which context is most
important to save for its future self,
and how it should be structured, and how
it should be represented.

[00:07]
And so, with memory, we've modeled it as
a file system to Claude.
Again, the key principle is getting out
of Claude's way and letting it use the
capabilities it already has that are
very strong at.
Or as we like to say, let it cook.
This is the dream.
But,
we've talked about Claude's memory
capabilities within the context of a
single agent. But, we want it to work
across multiple agents that are
operating in the same environment at the
same time, or maybe across environments.
And this introduces new requirements.
Like, for example, letting multiple
sessions share the same memory store at
the same time. And maybe they want
different scopes. So, we offer read-only
scopes and read-write scopes. So, for
example,
you could have organization-wide memory
that's read-only and it's updated fairly
infrequently, and it can be accessed by
all agents. And the same set of agents

[00:08]
can have access to
more granular memory stores that they
can read and write freely. And so, this
creates a hierarchy and uh allows the
memory system to really scale.
Now, to combat write conflicts, to make
sure that one agent isn't clubbering
another's rights, we employed a
optimistic concurrency control model to
avoid agents overriding each other's
changes.
And
last but not least,
memory needs to work for real production
agents.
This means enterprise-grade controls.
So,
version control
uh creates an audit trail as agents make
changes. And developers can see how
memory evolves over time. They can even
diff between versions. And there's
attribution to see which agent wrote
which part of the memory.
And
I think one of the most important pieces
is that memory has a standalone API.

[00:09]
It enables developers to manage their
memory from anywhere. And the reality is
teams are building their systems in many
different environments. So, they can use
memory via these APIs, which provide
standard CRUD operations, but also more
enterprise-focused operations like
exports and redactions.
Okay.
So, we've covered three key components
of a memory architecture.
One, we started with the storage layer,
which is how the data is managed itself
and how changes are tracked. Next, the
structure of memory, optimizing it in a
format that allows Claude to get the
most out of it.
And finally,
Claude-driven processing
for updating the memory.
>> [clears throat]
>> Now, let's stop at that processing
point.
Agents writing memory as they work is

[00:10]
very key to the processing layer. Think
of it as taking notes while you're doing
something.
But,
as we scaled up this pattern to more
complex multi-agent works like uh
use cases, [clears throat]
we started seeing some limits
across different sessions. We started
seeing some common patterns. For
example,
agents were prone to making many of the
same mistakes, and they learn from their
mistakes independently. Agents also
displayed some of the same patterns of
inefficiency.
And
the general theme was memory was being
updated in a locally optimal way, but it
wasn't globally optimal. In some cases,
there was duplication or fragmentation.
And so,
we started thinking really deeply about
this problem, and in the last couple of
months, we built a feedback loop in the
processing layer that combated some of
these problems.
Now, I've said it a couple times, but
this time I mean it. This really is the

[00:11]
dream. We call this process dreaming.
And dreaming is available in research
preview right now, and it can be used
with managed agents.
It's a process that looks for patterns
in mistakes across agents and sessions.
And it automatically organizes and
curates their memory.
Customers like
Harvey saw a six-times increase in
completion rates for their legal
benchmark with dreaming. And we're
actively seeing other usage of dreaming
and we're really excited to see how
people are benefiting from it.
A quick overview of how dreaming works.
It is a batch process. It runs out of
band from sessions. It's completely
decoupled.
Think of it like a feedback loop. Agents
write memories and dreaming refines them
and this process repeats.
And dreaming can be kicked off ad hoc,
nightly, hourly, or it can even be

[00:12]
triggered by events like the end of a
session. It's all controlled via API, so
it's very flexible.
Each dreaming run analyzes session
transcripts. It inspects the existing
state of memory and it proposes
optimizations to the memory in scenarios
where sessions were inefficient, made
mistakes, or needed improved guidance.
And the output is a verified, better
organized snapshot of memories that
agents can choose to adopt.
And dreaming truly enables continuous
self-learning. It closes the loop on
memory.
I mentioned out of band.
The out of band component of dreaming is
really, really critical.
Creating a process that's decoupled from
the underlying agent loop has benefits.
For one, this architecture makes it
useful for multi-agent systems.

[00:13]
Looking at cross-session, cross-agent
transcripts discerns patterns that a
single agent in isolation might struggle
to identify.
There's also benefits to having a
dedicated dreaming harness. It allows
for clearer objectives. Since dreaming
is an independent process, there's no
risks of agents needing to trade off
between
improving their memory quality or
actually just completing their task
objective.
It's clean separation.
And lastly, it doesn't add any latency
to the agent. It's completely removed
from the hot path.
So, zooming out,
we now have a robust memory layer that
can be shared across agents and
environments instead of
only within specific tasks or usage.
We also have dreaming,
a process that globally optimizes and
reconciles memory across agents.

[00:14]
And
the result is a capable memory system
for organizational memory that is
capable of scaling up both the size as
well as the quality of memory.
And
the way I think about it is sharing
memory that's constantly improving
across agents raises the floor for every
agent. And dreaming raises it even
further.
And if you really
explode the size of this capability and
you pull it all together, memory
becomes a huge source of knowledge that
Claude can use to understand the
organization and the world that it's
operating in.
One way to think about dreaming is like
thinking models or test time compute
where
letting models spend some tokens to
explore a problem
on average produces better outcomes.

[00:15]
With dreaming,
agents are doing the same thing.
They're spending some work up front to
curate and produce higher quality
memory, and that pays dividends for all
downstream agent performance.
We believe that dreaming and memory form
the basis of a frontier your system.
Memory on the left helps agents learn
and remember from task to task.
And dreaming on the right verifies,
organizes, and enriches the memory.
The way I think about it is
dreaming is the bridge between memory as
we know it today and organization scale
memory and knowledge.
Now,
I'm going to flip over to
a demo.
So,
this uses both dreaming and memory in
practice. It's an agent platform for
SREs.

[00:16]
And everyone loves being on call, right?
So,
here we have a system that looks at
incoming alerts and pages. And for some
of them, it actually uh spins up agents
that decide how to triage and fix the
issues as they come up.
And it has access to a couple of memory
stores. One is a read-only org-wide
knowledge memory store. And so, this
contains things like the SLO policy or
runbooks and on-call mappings.
Information that doesn't change very
often, but is important for every agent.
And it also has access to read-write
memory stores that are
specific to the task at hand.
Now,
we can dig into an interesting example
here
where
an agent investigated
and found the root cause of an alert.
And
it put up a fix, and it noted in memory,
you can see the rights, it noted in

[00:17]
memory that a fix was in flight and it
was incoming.
And then,
the shared memory store can be read by
uh subsequent sessions.
And so, here we can see that when a
similar issue arises,
the downstream session
already knows that a fix is in flight
and it's able to act based on that
information.
And
I really think this is
just such a cool pattern because, you
know, the
I was once an SRE in my career and this
really uh
helps coordinate across all agents.
And it's really cross-session memory at
work.
>> [snorts]
>> Now,
for running in enterprises, uh an
important piece here is audit logs and
history. So, with memory, you can see
the full version history. You can switch
between different versions and you can

[00:18]
also attribute the rights to specific
sessions.
And there's also a precondition here and
that's the optimistic concurrency model
to make sure that
agents aren't clobbering each others'
rights.
Now,
we'll flip over to
the Cloud console.
One moment.
There we go.
So,
here we see the list of underlying
memory stores that we were using in that
application.
And so, we'll go over to our team SRE
memory store and you can see exactly the
underlying files that were populated
there.
And we're going to head over to the
Dreams tab.
And we're going to kick off a dream.
And so, this can also be done via the
API uh but also in the UI.
And we're going to select the team SRE
memory store and we're going to select a
batch of sessions from the last 7 days,
so that's about five.

[00:19]
And we're going to start dreaming.
As it begins, you can see it making
progress.
You can look at the dream and see that
there are five input sessions and then
you'll see there's actually an output
memory store that's being compiled and
you can actually open the dreaming
session. This is an important piece.
Dreaming itself is built on Cloud Manage
agents. So, it's a feature for Cloud
Manage agents built on Cloud Manage
agents itself.
You can see that it spins off a series
of sub-agents to analyze transcripts in
parallel
and it has all the same UX as the rest
of Manage agents.
And we'll fast forward to a completed
dream session
and you can see the diffs on the memory
store updates.
And
in this example here
we see that
across sessions and across agents,
there's a a common pattern of an alert
triggering 60 seconds after a CPU spike.

[00:20]
And this is a recurring pattern.
And so, it starts to discern that there
might be some issue with the retry
behavior.
And so, it makes a note. So, the
dreaming process makes a note and
updates memory so that the next agent
that sees this pattern can actually act
on this information.
And similarly
it updates the triage log in a more
holistic way rather than just being a
wrote log of all the events that
happened.
And that's memory and dreaming at work.
So, we'll flip back over to the slides.
And we'll close out.
So, with that demo we saw how we can
build a a production agent that uses
memory and dreaming
to self-improve the agents.
And
this year I think it's going to be a
really big one. We're going to see
agents run for longer and longer time
scales

[00:21]
days, for example, and continuously
building upon and improving their
understanding and view of the world
around them is very critical to
unlocking that capability.
And I think memory systems are going to
be a big part of what makes this
behavior possible.
So,
give it a try. I'm excited to see what
everyone builds with it. And I'll be
outside if you have more questions.
Thank you.
>> [music]
[music]

</details>
