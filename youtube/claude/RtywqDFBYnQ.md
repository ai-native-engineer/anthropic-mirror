---
title: "Memory and dreaming for self-learning agents"
channel: claude
url: https://www.youtube.com/watch?v=RtywqDFBYnQ
youtube_id: RtywqDFBYnQ
published: 2026-05-08
duration: "24:28"
---

# Memory and dreaming for self-learning agents

[![Memory and dreaming for self-learning agents](https://img.youtube.com/vi/RtywqDFBYnQ/hqdefault.jpg)](https://www.youtube.com/watch?v=RtywqDFBYnQ)

<details>
<summary>자막: Memory and dreaming for self-learning agents (24:28)</summary>

[00:00]
Hello.
Everyone, how's it going?
Thanks for coming.
My name is Mahesh and I'm a product
manager on the platform team here at
Anthropic. Uh over the past year and a
half, I've gotten to work on primitives
like MCP and skills. And today I want to
talk about the primitive that I'm most
excited about next, which is memory.
Um I'll talk about why we think memory
is so important and why we've been
spending so much time on it at
Anthropic, how we think about designing
memory systems that are built for
frontier agents, and I'm excited to also
talk about dreaming, a brand new product
that we're launching today in research
preview in the managed agents API.
Model capabilities have improved really
quickly over the last couple of years.

[00:01]
And agents are capable of tasks that
take many, many hours and can run for
hours or almost days at a time. And as
models and agents have improved, we've
also invested in building higher and
higher-level capabilities and primitives
that kind of get out of those models'
way and give them access to additional
bits of their environment and things
that they can manage and become more
powerful over time.
So, for example, we launched MCP, which
gives agents access to external tools
and data.
We launched harnesses that were really
powerful like Claude Code and the agent
SDK. And in October, we launched skills,
which let agents pick up brand new
capabilities that either other agents
have designed and shared with them or
humans and users that they interact with
designed for them.
Each primitive has let agents do
increasingly powerful things for longer
periods of time, but we still think that
something is still kind of unsolved, and

[00:02]
that's continuous self-learning and
context management over long horizon
tasks.
So, memory is the next primitive. It's
the thing that I think we'll get us to
self-learning agents that evolve and
improve based on the tasks that they're
working on and their own experience.
With memory, agents can learn about the
tasks they work on, things like the
success criteria, common mistakes,
strategies that are or are not working.
They can learn about their environments,
things like the code bases that they
interact with, the files and the assets
that they're constantly keeping up to
date. And they can also learn from other
agents that are in the same environment
as them. They can share learnings, they
can figure out what's going wrong
elsewhere in a system, and incorporate
that into their own memory.
And I think this last point is the one
that I've been most excited about this
year and over the next couple of months.
I think self-managed memory is going to
be super important in these large and
complex multi-agent systems where a

[00:03]
swarm of agents that are working in a
similar environment on discrete tasks
are essentially building up their own
understanding and their own model of the
worlds that they're in over time.
So, to help get to this vision, we just
launched memory in cloud-managed agents
in public beta a couple of weeks ago.
This gives developers a frontier memory
system that works out of the box to
maximize intelligence by default, to
support these systems of many agents
running concurrently in the same
environment, and most importantly, to
give enterprises and developers the
flexibility and control they need to
actually run these in production in an
enterprise setting.
We've already heard from a bunch of
teams building on this to date, um that
all say that this helps them get to
continuous learning and continuous
improving agents a lot faster. Uh,
Rakuten, for example, mentioned that uh,
this helped them drop their first pass

[00:04]
mistakes in their internal uh, knowledge
agents by 90% because agents were able
to catch mistakes and share them with
the next iteration of agents, which also
led to better token efficiency and lower
costs and better latency because they
started deploying memory systems.
So, I want to talk a bit about the
requirements that we kept in mind uh,
that we discovered while talking to
customers and building this.
The first and most important is memory
needs to be built to maximize
intelligence by default.
Agent builders have uh, been designing
memory systems for a while. I mean, we
ourselves launched Claude.md uh,
originally with Claude code, I think uh,
about a year and a half ago. And this
was a pretty constrained early version
of memory where an agent could leave
notes for itself. Sometimes the user
would also leave notes in the same
memory file. And we also launched
something like the memory tool uh,
within our SDKs, which was a pretty
well-specified tool call with specific

[00:05]
parameters and output formats that uh,
API builders could use.
As agents have improved, we've tried to
get more and more out of Claude's way
and delegate more of this
decision-making to Claude without
over-constraining um, the design of
these harnesses.
And as we did with skills, we kind of
came to the conclusion that hey, we know
that agents are able to manage a virtual
environment and manage their own file
system. So, why can't we go the same
direction with memory?
Memory in Claude-managed agents models
memory as a file system to Claude, a
series of files with a specific
hierarchy and format that Claude can
manage and update on its own.
It can use familiar tools like bash and
grep to update this memory to keep it
organized and to constantly change it as
it starts working on a task.
Now this this also tracks with what
we're seeing in the latest models. With
Claude Opus 4.7, which we just launched
last month, we saw that it was state of

[00:06]
the art at file system-based memory.
That means it's a lot better at
discerning what content to put into
memory, what's worth remembering. It's
better at figuring out what's the right
structure for memory, how many files
should I split memory into, how do I
keep it organized inside of a file
system. And ultimately it all does this
with just Bash tools and grep tools that
already make Claude so good at agentic
coding.
The other thing that we had in mind when
designing memory is that it needs to
scale with the multi-agent systems that
we're going to be building over the
coming months.
Multi-multi-parallel agents is something
that we're already kind of starting to
do with Claude Code. There's a lot of
power users that have like 10 or 15
Claude Code sessions running at the same
time, and we're starting to see this in
an enterprise setting as well, where
enterprises, including Anthropic, have
hundreds or sometimes even thousands of
agents running in parallel, interacting
with the same set of shared state and

[00:07]
the same shared memory.
So there's a couple of properties that
come out of this.
One is we want to give agents the
ability to mix and match between the
session and the work that it's doing
and the set of memory stores that it has
access to. So one property of memory and
managed agents is permission scopes. The
ability for one agent to have read-only
access to one memory store, and maybe
that memory store is organization-wide
knowledge, a set of best practices, a
runbook for how to deal with these
common tasks. And then it has read-write
memory for another memory store. So
maybe that's another one where it has
working memory that's a lot more
specific and frequently updated based on
the work it's doing.
The other property that came out of this
was concurrency. If there are hundreds
or thousands of agents interacting at
the same time with the same set memory
state, it needs to be able to know that
it's not going to clobber the memory or
overwrite it as it continues working.
So, we implemented optimistic

[00:08]
concurrency where one agent can
essentially use a content hash to
check if it's going to overwrite another
agent's memory before it actually makes
an update.
From talking to customers, the final and
most important property from all of this
is about developer and enterprise
control for actual production agents. A
couple of things came out of this. The
first and probably most sought-after
property is version history. It's the
ability for the developers building with
managed agents to see an entire audit
log of every time memory was updated and
to actually even give agents access to
the same audit log in the future so they
can keep track of what change was made
and when.
It's also attribution metadata to say
what agent made an update, what time did
it make that update, what session made
that specific change, and to go super
granularly so this is predictable and in
developers control.

[00:09]
The other property that came out of this
was a standalone API. We talked to a lot
of customers that are building bespoke
systems outside of managed agents to
manage and curate their memory and keep
it up to date. We talked to customers
that do PII scanning to make sure that
memory doesn't have sensitive content
that shouldn't be in there. We also
talked to customers that wanted to clean
up memory in their own separate pipeline
or to clone it into external systems.
So, we didn't want to lock them in into
a specific system that was only
available to manage agents. We built
this portable API so they could go and
control these additional things on their
own.
So, taking a step back, we've started to
form this picture of the different
layers that we need to work in as we
build a frontier memory system.
We've talked about the storage layer,
which is where the data is actually
stored, what kind of metadata and
attribution data we're leaving alongside
of it.
We've talked about the structure and the
content layer. This is things like our

[00:10]
decision to model files uh memory as
files in a file system. And earlier um
with skills as a form of procedural
memory that have a pretty lightweight
spec that say, "Hey, here's how you can
actually learn how to do this new
capability and equip yourself with new
knowledge."
And then there's the process layer. This
is things like how often is memory
actually updated, what triggers updates
to that memory, and what sources does it
use to decide what changes to make to
memory and have new things to learn.
And we think that agent memory, the API
that we've been discussing, solves part
of this. Um but as we started to scale
this up into these more complex
multi-agent systems, we also saw a bunch
of limitations. We saw cases where
memory was sessions were kind of missing
learnings that other agents and other
sessions had already kind of figured out
on their own. We saw these common
mistakes and these shared patterns
across multiple agents working in the
same environment.
And we also saw that they weren't super

[00:11]
efficient at keeping up this large-scale
memory store and keeping it up to date
in a holistic and efficient way. They
were kind of siloed into the specific
task that they were working on.
So, for the past couple of months, we've
been experimenting with a couple of
different types of processes to kind of
supplement this with. And we landed on
one. Um we call this process dreaming,
and today we're launching this in
research preview in the managed agents
API.
Dreaming is a process that looks for
patterns and mistakes across your recent
agent sessions and their transcripts and
automatically produces organized and
up-to-date memory content.
We've worked with a few customers in
early testing and for example Harvey
when they deployed dreaming in one of
their legal benchmarks which tests out a
pretty realistic legal scenario, they
saw a six-times increase in the task
completion rate for one of their legal
scenarios. And we're really excited to
see how other customers use this uh when

[00:12]
they start testing out this research
preview.
So, let's talk a bit about why we got
excited about dreaming in the first
place and some of the design and harness
considerations we kept in mind as we
designed it.
So, how does dreaming work? It's a batch
asynchronous process that runs
separately from the work that you're
doing uh within a specific session
that's working on a specific task.
You can kick off dreaming periodically
um using our console or VR or API on
kind of a cron basis or you can plug it
in using our API into an existing
process. For example, some customers
kick off dreaming once their agents have
finished a task and are spinning down
and want to save those learnings to the
memory state.
And dreaming comprehensively looks
through recent transcripts, looks for
common mistakes, things that a bunch of
agents are doing like a failed tool call
or strategies that are working out for
them, and finds opportunities to update
the memory state that will improve it in
the future. And it produces this updated

[00:13]
memory state that you can then apply
immediately to your memory store or
maybe you want to run some checks and do
some manual review um which you can do
via the API.
The ultimate goal of dreaming is
continuous self-learning and
self-improvement where the next day's
agents automatically get better based on
the learnings and the work of the
previous day's experience.
We're excited about dreaming from a
design and research perspective for a
couple of reasons. The first property
is, compared to the memory APIs we've
been talking about previously, dreaming
is out of band. It happens outside the
context of an agent working on a
specific session or a specific task.
And this has a couple of benefits. The
The first that is that it's a really
good fit for multi-agent systems.
When a single agent is reading and
writing memory, it has the perspective
of itself, of its own context, and of
its task. But, dreaming lets us go kind
of a step above that and look at

[00:14]
multiple agents at the same time to find
these shared patterns and learnings that
a single agent might not learn or notice
from its own limited perspective.
From a harness design perspective, we've
also found consistently that it's
important for agents to have really
discrete and clear objectives as they
start working on a task. So, dreaming
really lets us separate out this new
objective of memory quality because we
think over the coming months memory is
going to be increasingly important and
load-bearing to the actual outcomes and
the work that agents are doing.
So, this lets us separate the memory
quality objective from the task
completion and task performance
objective that a lot of agents already
have today.
And again, because dreaming is an
out-of-band process, it's in the
background, it does this without adding
any latency to the hot path of an
agent's existing task.
The other design perspective we had here

[00:15]
and thing that we wanted to enable,
which I'm very excited about, is
large-scale memory systems and how we
can use compute effectively to create
and curate these.
Today, most memory deployments are
pretty localized to a specific user or a
specific task or maybe a small team
that's working together. But, agent
systems are quickly getting to
enterprise scale. And again, within
Anthropic and within other enterprises
that we work with, they already have
hundreds or thousands of agents running
concurrently that share state.
So, this effectively starts to turn into
a really large knowledge base as opposed
to just a simple memory store to to
store working context about a specific
task.
And to support this, we need to find
ways to let Claude scale up memory
systems to be super large while still
being up-to-date and fresh and not too
token intensive.
Dreaming is a process that lets us do
this by essentially following similar
scaling laws of using additional compute
and additional effort to keep these
memory systems organized.

[00:16]
One way to think about this is how we
considered test time compute or thinking
models from a couple of years ago where
giving models the ability to go explore
and try different things and especially
spend more tokens leads to a lot better
final outcomes on the task they're
working on. And dreaming is a similar
thing that lets a dreaming agent spend
more tokens to keep these systems well
organized and up-to-date.
Another perspective we have here is like
a search system where there's this
upfront effort to kind of produce this
high-quality, up-to-date index that then
is then used at retrieval time or search
time to get the latest results super
efficiently and performatively. So, this
is something that dreaming also lets us
do by creating this index upfront and
then curating it so that all the
downstream agents can use it. And
effectively lets us amortize this effort
across all of those agents that are
reading from a memory store.
So, now with memory and dreaming in the

[00:17]
managed agents API, we start to build
this picture of what we think of as a
frontier memory system, at least so far.
Memory on the left side is a primitive
for agents to immediately in real time
read and write things and remember
things as as working on a task.
And dreaming is a comprehensive process
built on top of that to verify the state
of memory,
to organize it, and to enrich and
backfill it with additional information
um that based on the tasks that the
agents are doing during a day.
Dreaming is kind of the bridge between
these more intermediate memory systems
and these larger scale knowledge bases
that again we think are going to be
really prominent over the next few
months.
So, let's walk through a
quick demo.
What we're looking at here is a SRE
agent. Let me make sure this starts.
There you go. That is looking at alerts
that are coming in and it's reacting
based on those alerts, spinning up

[00:18]
specific agents that either do a bunch
of triage work, maybe sometimes it spin
up spins up an agent to go submit PRs.
And each of these agents are equipped
with a couple of memory stores.
We can see that it has an org-wide
knowledge memory store. It has an SRE
and a code base memory store.
And so if we click into the org-wide
knowledge memory store, we can see it's
read-only. It's a set of, let's say,
runbooks and SLO guidelines.
Um it it points the agents to the
specific owners that they might need to
go ping. And it's something that doesn't
get updated very often. We don't want
agents necessarily to be going and
making changes as they work.
Now, there's also the SRE memory store
that's read-write. And of course the SRE
agents are able to constantly make
changes to this as they react and learn
from the environment around them.
So, we see this alert, this P1 that's
coming in from the dispatch service, and
we spin up this SRE agent um that goes
and starts to kick off an investigation.
It goes and investigates the CPU

[00:19]
utilization. Um maybe it goes and checks
out some of the traffic patterns and
queries for some of the recent PRs that
have gotten deployed.
It writes down these learnings um if we
click into the SRE memory store and
notes these in a new diff that gets
updated in that memory store.
Now, a couple minutes later, that same
alert gets paged again, and a different
SRE agent spins up with access to the
same memory store.
The first thing it does is it sees that
note within its memory store that says,
"Hey, we already did this investigation.
Here's what we found. Here's a way you
can short-circuit what you're looking
at." And ultimately, it saves um the a
bunch of time that it would have spent
going and investigating the same thing.
So, we see an immediate token efficiency
gain and an intelligence gain since it
now knows um what else it can go
investigate.
Now, this is great, um but we want to
actually be able to deploy these in an
enterprise and actually have reliability
and see what decision-making led to
certain things um certain outcomes. So,
if we click into the memory store, we
can see it has version history. It says

[00:20]
every single time an update was made to
this, we can actually go back in time
and see what changes were made.
We can also see which agent made that
change. When was it written? And we also
have this little precondition hash,
which is again what lets us do this
optimistic concurrency to say, "Hey, I
made this change. Let's actually verify
it is what it is before I go and
override it."
So, we've been talking about agent
memory, but let's now see how dreaming
can now make this a more holistic and
up-to-date memory system. So, we'll go
and um pivot over to the cloud console,
where it actually reflects the exact
state of what we're looking at in the
API. It's the set of memory stores that
we've created, and we'll click into the
team SRE memory store, which again
reflects the latest state of memory that
we had written.
If we go and navigate to the dreaming
tab, specifically,
we can kick off a dreaming job where we
say, "Hey, I want to go and update and
create this specific memory store,
and I want to look at a bunch of the
sessions um that we've been looking at

[00:21]
for the past 7 days. These are all the
sessions that touched this memory store,
and we We to start a dreaming job to
look over those.
So, I'll click into the dream and we can
see some of the work that it's doing
under the hood. It says, "Hey, here are
some of the input sessions that it's
going to go and spend time looking into,
look through the transcripts." And it
spins up within the cloud console an
actual session where you can go and see
what's happening. It's looking at the
specific transcript entries and it's
going to spin up a bunch of sub agents
that go and look through those
transcripts, try to identify those
learnings, and then produce that updated
memory state.
So, we'll jump ahead a few minutes and
look at the completed dreaming job to
see what the output was.
It produces a diff, which is a set of
updated files that it's going to apply
to this memory store.
The first one is an update to this
dispatch latency note that we were
looking at in the demo earlier.
It said, "Hey, a bunch of these agents
were triggered exactly 60 seconds after
an upstream spike in CPU utilization."

[00:22]
And it kind of figures out based on that
pattern that there might be some retry
logic that's getting triggered that's
really inefficient and leading to a lot
of wasted time when we're actually
triaging this stuff. So, it identifies
that because each of the individual
agents aren't really noticing that
pattern. They don't know that other
agents are also seeing kind of that
60-second pattern every single time and
it leaves a note. And the goal with this
is future agents benefit from this
learning and can go figure this out more
efficiently.
It also does a deduplication and
creation step. It sees that there were
five of the same entries from previous
agents that were working with this
memory store and it consolidates they
consolidates that into a single entry.
It removes a stale entry that's no
longer valid that it saw in the
transcript that is no longer relevant.
And then it adds this verification note.
It says, "At this time, based on this
transcript I just looked at, this memory
is actually accurate. I was able to
verify it based on the work that the
agent was doing and therefore you can
rely on it in the next day when you
start using the same memory store."
So, there's that verification backfill

[00:23]
organization steps that we think memory
and dreaming are really useful for.
Um and so with this demo, what we've
kind of seen is how we can actually
build production agents using the memory
and dreaming APIs in the managed agents
API.
And to close out, I think that over the
next couple of months, we're going to
start seeing agents that run for days or
many, many hours at a time, and I think
that memory is going to be an really
important part of that system and what
makes it ultimately possible.
So, I'm really excited to see what
everyone builds with memory and dreaming
in the Cloud Managed Agents API,
um and you should get started today.
Thank you.

</details>
