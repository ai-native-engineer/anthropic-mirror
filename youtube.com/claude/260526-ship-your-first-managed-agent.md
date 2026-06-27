---
title: "Ship your first Managed Agent"
channel: claude
url: https://www.youtube.com/watch?v=19HDQ9HppOA
youtube_id: 19HDQ9HppOA
published: 2026-05-26
duration: "37:09"
captions: en-orig
---

# Ship your first Managed Agent

[![Ship your first Managed Agent](https://img.youtube.com/vi/19HDQ9HppOA/hqdefault.jpg)](https://www.youtube.com/watch?v=19HDQ9HppOA)

<details>
<summary>자막: Ship your first Managed Agent (37:09)</summary>

[00:00]
[music]
>> All right. Hello everyone. It's great to
see you all here today for our session
on shipping your first manage agent.
Let's go ahead and get started. My name
is Isabella He. I'm a member of
technical staff at Anthropic on the
Applied AI team.
The Applied AI team at Anthropic sits at
the intersection of products, research,
and our customers, which means that I
get to contribute internally to products
at Anthropic like Claude code and our
Claude harnesses, as well as work
externally with our customers that are
building on top of Claude and on top of
our harnesses.
So, my goal today is to get you all
hands-on with actually building on top
of manage agents, understanding how the
harness works under the hood, and
getting you ready to actually ship your
first incident response management.

[00:01]
So, the quick overview of today's
agenda. We're going to cover first a
quick refresher of Claude manage agents.
I want to talk you through a little bit
about how this harness works under the
hood and what makes it so special. Our
team put a lot of thought into the
architectural design of Claude manage
agents to make sure that it runs ready
and reliably for production-ready
agents. So, I want to talk you through a
little bit of how that works so that
then when we transition to the second
portion here, which is the hands-on
workshop, you'll actually understand
what each of the primitives you're
building actually mean for your agents
under the hood.
So, for the majority of today's session,
I want you all to actually have your
laptops open, building alongside me,
actually working inside of a repository,
and getting you ready to actually spin
up a working incident response agent.
Lastly, we'll talk a little bit about
beyond the basics. Today's session is
the first session of a couple of other
ones that will build on top of this on
Claude manage agents.
Specifically, right after this one, I
think there's another session on
dreaming, which is one of my favorite
new features with Claude manage agents
for self-improving agents and memory

[00:02]
built into the harness. So, encourage
everyone to dive in a little bit deeper
into what else is in the box after we
set you all up for success today with a
quick introduction.
So, let's first touch a little bit about
how we got here with Claude manage
agents.
When we first released the very first
Claude back in 2023, we released a
messages API alongside access to Claude.
This provided raw model access to all
Claude models. This became the very
first way that people could
programmatically build on top of Claude
and essentially gave a way for people to
access tokens in and tokens out via our
Claude models.
This also meant that for everyone
building on top of Claude models, they
had to implement all the various
primitives themselves. Things like
context management, the actual agent
loop, compaction, etc. All the
primitives that come alongside making
the agent work.
When models were less intelligent back
in the early days of let's say 2023,
some of these primitives were much
simpler because agents could simply do
less. But, as we evolved into now with

[00:03]
higher model intelligence and as agents
are able to take on more complex tasks
and actually take actions within
environments and come to actually do
entire tasks for humans,
the primitives that come alongside
context management and managing an
agent's ability to execute API calls and
tool calls becomes much more complex.
So, that's when we moved to the agent
SDK, which became a harness that allows
you to programmatically call Claude
code, one of our agents at Anthropic.
So, Claude code is something that an
agent has access to a computer and takes
actions within file system. So, the
agent SDK became a way for you to make
Claude much more powerful by leveraging
the power of Claude code within a
harness.
The main thing here though is that with
the agent SDK,
developers still had to manage hosting
and scaling on their own and making sure
that the agent SDK would be safe to run
within their containers.
That's only then evolved into Claude
managed agents, which is the first
harness to be able to handle scaling and
production ready components for you by

[00:04]
Anthropic,
providing things like a purpose-built
harness, sandboxing, observability, tool
runtime, all within a managed
infrastructure system. This means that
developers can focus on task and agent
configuration, custom tool logic, the
things that actually matter for bringing
domain expertise and customizability to
your agents, where you're handing off
the rest of all the primitives and core
compute and primitives of essentially
managing the basics of agent running to
Anthropic.
So, that brings me to managed agents as
the fastest way to build production
ready agents on Claude.
We've seen people build 10 to 15 times
faster to production with Claude managed
agents by leveraging our purpose-built
harness.
Part of the reason why we built Claude
managed agents is because is because
harnesses should evolve alongside your
agents.
For example, back when we were building
ourselves on top of models like Sonnet
4.5, we noticed that Sonnet 4.5 emitted
a particular behavior called context
anxiety. This meant that with Sonnet

[00:05]
4.5, Claude started wrapping up tasks
early even when it still had room to
spare in its context window.
To manage that in our harness, we then
added some mitigations to combat against
this early stopping behavior.
But, when Opus 4.5 then came out, we
actually saw this behavior go away,
making all that work we had done inside
of the harness essentially obsolete
because Claude had evolved beyond that
behavior that we had built into the
harness to manage.
So, the takeaway there is that it's a
lot of work to maintain harnesses and
make sure that they actually evolve
alongside your agents, which is why with
Claude managed agents, we want to make
it really easy for Claude and Anthropic
to handle all the complexities that come
with compaction, caching, things like
context anxiety, all these various
primitives that come with actually
making agent production ready and
getting the most out of Claude. So
again, you can focus on the tasks,
tools, and things that actually matter
for building agents on Claude.
So three primary resources go into
building on Claude managed agents.

[00:06]
First is the agent's endpoint, which is
the persona and capabilities. This is
the core system prompt that powers your
agent. Essentially here, you're defining
the model, the MCP servers, the skills,
the various components that your agent
can actually leverage when it's able to
run in that agent loop.
The next is the environments.
You can think of this as the hands of
the agent, where the previous one is the
brain of the agent where the agent is
thinking through what to execute, and
then it's using an environment to
actually have a space and a container to
actually take action on your behalf.
Sessions are next the way to tie
together agents and environments.
A single session has a spun up on an
agent instance within an environment. So
you can connect the two together and
actually stream events back to your user
and start to take action on behalf of
your humans as part of a Claude powered
agent.
A key thing here, as I alluded to
briefly before, Claude managed agent has
the agent loop run server side.
This means that a lot of the
complexities that come with managing

[00:07]
hosting and scaling are abstracted away.
And when you close your laptop or you
hit hard refresh on your agent that
you're building on Claude managed
agents, everything is maintained and you
don't have to worry about durability,
reliability, all these various aspects
that usually come to bite you when
you're trying to turn your agent from a
prototype into production.
And lastly here, before we dive into the
hands-on portion, is I want to talk you
through a key design decision that went
into Claude managed agents.
Previously, with a lot of agent
harnesses, we saw the agent loop coupled
tightly with tool execution.
This design pattern made sense and still
makes sense for some agents because you
want to give the agent powerful
abilities to actually take action within
the environment. For instance, with
Cloud Code, we want the agent to be able
to access various files on your
computer, take action within a file
system, and therefore it makes sense for
the agent to have access to all those
tools spun up on every container.
But, we also realized there are some
constraints for this, especially with

[00:08]
some agents where you essentially want
to be able to decouple the hands from
the brains of the agents.
For instance,
credentials and uh
credentials and security became a huge
concern.
With the ability to have the agent
access your file system, you can
actually add very distinct sandboxing by
decoupling these two components, where
the agent is no longer able to access
the actual credentials without
encryption by decoupling the hands from
the sandbox of the agent.
The other aspect here is actually you
can see huge benefits by doing these
decoupling on things like time to first
token and latency.
Previously, with the agent loop into
execution in the same box, you had to
spin up containers for every single
session that you're spinning up in the
agent, which contributed to additional
latency from a time to first time to
first token perspective.
But, with this now decoupled, our teams
actually saw reductions in time to first
token along the lines of over 90%
reduction in TTFT for our P95 metrics on

[00:09]
latency.
So, here you can start to see the power
of this design decision coming through
from the perspective of safety,
reliability, latency, and everything
else that you care about when it comes
to building production-ready agents.
All right, so now it's time for the
exciting part of today's session, which
is where I want you all to open up your
laptops and go to this URL here to
actually clone a repository, and let's
start to actually feel the magic of
everything that I just talked through.
So, I'm going to give everyone a second
to just go over to that URL there
and just spin up the repository that we
have ready for you.
All right, so here are some additional
commands that I want you all to run to
make sure this is all set up on your
computers.
So, the first step many of you might
have done already, but just take that
repository, hit the URL, get clone it,
and then I want you to CD into the
specific repository for the session,
which is ship your first manage agent.
And then, if you're on Mac, you'll see
those two commands on the side, the
Python and the source. Um, there's a

[00:10]
command there for Windows as well.
And you'll just do the rest there where
you want to install the requirements,
copy over the environment key into your
.env file. Um, here you'll put in the
Anthropic API key that hopefully all of
you also received from the QR code for
free credits earlier. And lastly, we'll
just run the app.
All right, let's go ahead and dive in,
but as I mentioned before, let me just
show everyone where these instructions
are. If you go into the repository in
the link and then go to ship your first
manage agents, you scroll down on the
read me, you'll see all the setup
instructions here. So, feel free to do
this, um, as we go along or even in your
own time later today and continue
playing around with it, but as I
mentioned before, everything will be
also shown on the screen to follow along
with. So, do not worry if you did not
have time to fully get it set up on your
laptop.
Without further ado, let's go ahead and
dive in. So, once you run streamlit run
app.py, you should be able to see a URL
that looks like this and a page that
looks like this.
What we're doing here is we're going to
be simulating an agent, um, interaction

[00:11]
here where we have an incident that's
going to come up. A lot of you who might
be software engineers in the room will
be intimately familiar with the pain
that comes alongside incident response.
If you are software engineer, you might
be woken up at, let's say, 3:00 a.m. in
the morning, 2:00 a.m. in the morning
when you're out around on on vacation as
you're on call, and this is usually a
very painful portion of a software
engineer's life, uh, because when you're
on call, it means that if a server goes
down or a service goes down, you have to
be immediately the one there to respond
and tackle the incident. Usually for a
human, this means diving into metrics
and logs and deployments. You can
actually investigate what's going on.
And so, what we're going to do is we're
going to now have an agent run on Claude
manage agents to do all this for us. So,
that when we get woken up by 3:00 a.m.,
we can hand it off to an agent, or maybe
we don't even get woken up at all if
Claude is able to do everything for us.
Okay. So, let's now go ahead and dive
into the code here.
What we're going to open up here is we
have the agent.py file on the left and

[00:12]
the agent complete on the right. If you
want to challenge yourself, you can of
course try to implement everything
yourself here or with Claude. Um but,
what we're going to do just for
simplicity's sake is just copy over
various elements from the completed file
onto the incomplete file one by one. So,
you can see how these primitives compose
our agent one piece at a time.
So, let's go ahead and start off with
this very first part, which is the
agent.
We mentioned before that the agent is
the one that defines the persona and the
capabilities of the agent here. So,
that's model, the system prompts, and
the tools in our case for our agent
here.
So, let me go ahead and copy over what
we see there on the screen. And you can
see here that we're defining the SRE
agent. We're going to use Claude Opus
4.7 here. And I've preconfigured a
system prompt and tools for the agent.
We can actually take a quick look into
what that system prompt and tool looks
like here.
For the system prompt, you can see that
it's actually extremely simple for the
agent that we're defining today. You can
of course add more complexity and

[00:13]
constraints here, but we actually see a
very simple prompt working for our agent
that we're building today. We're just
telling it that it's an SRE agent. It's
responsible for coming in and debugging
incidents, and it has access to various
tools like metrics, recent deployments,
get diff. These are tools that you would
want as a developer if you're actually
managing an incident response as well,
like the ability to actually fetch logs
so you can see exactly what's going
wrong.
So, we're going to give those same tools
and the same instructions over to our
agent.
So now that we've configured this on the
screen and feel free for those of you
who are able to spin it up on your own
laptops to just follow along with
exactly what I'm doing, which is copying
over this portion from the right onto
the left here.
And then when we flip back over to the
screen, what we'll see is this wasn't
there until I just added that there, but
we can now actually have a unique
identifier attached to the agent that
we're building.
Okay, so that's step one. Now let's go
ahead and move on to step two,
which is the environment where the agent

[00:14]
is going to actually do work in.
All of you here were very lucky for
those of you who were able to come
yesterday as well to code with Cloud
London. We actually just released
yesterday the ability to bring your own
containers and your own compute to Cloud
Managed Agents, which means that you can
actually execute the agent for the tools
and the actual ability for the agent's
actions to work within your own
infrastructure and not just Entropic's
managed infrastructure. So that's an
exciting update that just came to Code
with Cloud London. Um before today's
purposes, you can actually see if we
copy over this environment configuration
here.
We're defining our SRE agent to work
within the Entropic cloud and here we're
just giving it unrestricted access from
a networking perspective.
We've made Cloud Managed Agents very
composable and very customizable. So
this networking list here is actually an
allowed list. If you want your agent to
only be able to access specific sites
and URLs, you can restrict this down as
much as you would like.
We also released um Cloud MCP tunnels,
which actually also gives you the

[00:15]
ability to run MCP servers within a
private environment instead of on the
public network as well. So again, just
offering various components to help you
make sure that your agents are as
production ready and as secure as
possible.
So now that we've defined this
environment here, let's flip back over
and we just saw that environment piece
come into our agent as well. So here we
have unique identifier for an agent and
an environment.
And that will next help us as we go
along with setting up the rest of our
agents as we start to get into session
definitions here.
The next thing that we have to do is
actually give our agent the ability to
look at logs.
With Cloud Code, that is one of the
first times where we realized the power
of giving the agent access to files and
a file system. Here with Cloud Managed
Agents, we're leveraging essentially the
files API by uploading the metrics and
logs to the agent. So the agent can
start to run code and process through
those files.
So here we've attached the log here as a
file for our agent. So we just also saw

[00:16]
that populate and come through. Again
here, the key takeaway is as much data
as you're able to give the agent um as
possible is what makes it so powerful.
Context engineering is a huge portion
that comes to actually making an agent
powerful. And this is where we see the
developers spending the majority of
their time working on top of primitives
like Cloud Managed Agents is managing
context and managing what types of files
are uploaded, how the agent processes
those files. These are components that
you compose yourself and are very
customizable on top of Cloud Managed
Agents to make it work as far and as
wide as you want it to.
Okay. So now let's go ahead and start to
define the session that we have here.
The session is going to oops, the
session is going to bind the agent and
the environment and also mount the log
here. So you can see we're passing in
the agent ID, the environment ID, and
the resources that we're giving to the
agent.
And this is going to give it the ability
to start to actually act and interact
with me as a user.
Let's go ahead and just complete the

[00:17]
rest of this here so that we can
actually start to run our agent.
What we want to do is now also give the
ability for the agent to come in and
stream responses to me as we go along.
There we go.
Okay, and the key portion here is that
when our Cloud Managed Agents runs
within a single session, instead of
responding in tokens in and tokens out,
it actually works in units of events.
Events here are things like user
messages or agent tool calls, agent
responses, so that every event can be
logged from an observability
perspective, as well as streamed back to
the user for the user to see the agent
responding as it calls tools and as it
starts to populate responses. This is
crucial for both a user experience
perspective, so user starts to see
things as they come through and not just
when Claude finishes an entire task, and
also from an observability perspective,
and Claude Managed Agents actually has a
very neat console built in for looking
at everything the agent is doing, and a

[00:18]
lot of observability features built into
Claude Managed Agents.
Okay, the last step here of just being
able to put our agent together, you can
start to see that our agent is actually
starting to come together. We can start
to create sessions and we can start to
do things. Um, what we're actually going
to see here though is that if I send
something like hi to the agent, it can
respond, um, but it doesn't actually
have the ability to be able to call the
various tools that we want it to yet,
because we haven't connected that
locally to what we want the agent to do
when it calls tools like get metrics.
So, the agent is ready. The agent is
actually defined on the server side
already. The missing piece here is just
to finally give it our local tools
so the agent can start to take action
here on my computer or my
infrastructure.
Okay, so now that we have that copied
over, the agent is going to be able to
start to call get metrics, get recent
deploys, get diffs, so it can truly
start to take action in terms of helping
us debug this incident.

[00:19]
The last thing I'm going to do here is
also just to make sure I give my agent
the ability to delete sessions.
So, that's when I come in, I can start
to hit this delete button and delete
sessions as I compose my agent. And this
is also crucial from a security
perspective. If you want to make sure
that, you know, nothing is being
retained for sessions that you don't
want on the cloud or on your
infrastructure, you can actually just
come in and proactively manage how
sessions are deleted. And once they're
deleted, they will be also removed from
every single log aspect here, so that
you can truly make sure that whatever
data you want managed is managed
actively and proactively via Cloud
Manager agents.
Okay.
So, with that all set up, let's go ahead
and give our agent a test run here.
I'm going to click the new session here,
and I'm going to just go ahead and ask
the agent to debug my incident for me.

[00:20]
You can see here that because we gave
the agent access to tools like
sandboxing and bash, and get recent
deploys,
the agent is starting to really take
powerful actions on my behalf here. It's
come in, it's run the sandbox command.
We can open this up and see what this
looks like.
Um we can see that it's actually coming
in and looking at what the logs were
added to.
It's then come in and called this tool
called get recent deploys,
which is coming in and returning results
like what the recent deployments look
like, the metrics. We can see this from
a user perspective if you click on the
tabs here, but this is essentially the
data that's actually being passed into
the agent via these local tools that we
define.
And again, we can start to see the magic
of that streaming that we implemented
come through as well, because we saw
these tools come in as they were being
called from the agent. We saw the user
prompt come in as soon as I prompted it
to the agent, and the agent is actually
streaming responses to me as it comes

[00:21]
through with more token response and
outputs, as well as as it calls more
tool as it goes along as well.
Okay, so what we're going to start to
see is the agent being able to help us
actually debug what's going on here,
which we can see here that the incident
is that there's something going wrong
with our P99 latency that seems to be 10
times above the baseline.
The agent is coming in and debugging
everything for us. Looks like it's
taking another second there.
So some of the major design decisions
that come in here when you're designing
a real site reliability site incident
response agent for your systems is to
think deeply about the various
components that go in and the various
MCP servers and skills that you want to
give your agent. Here we've defined, of
course, a very, very simple agent, but
for lots of the SRE agents that we
build, we actually also think about
things like how can we give the agent a
skill to actually execute and run
runbooks.
Runbooks are things where as teams debug
incidents, they note down and document

[00:22]
how they debug that incident so that
they can do it again for a future
session or future incident. You want to
give the agent the same access to the
materials that you would have as a human
developer. So something like a runbook
skill where the agent is actually able
to look at example runbooks or fetch
other postmortems from other incident
responses. That is something that is
very powerful for the agent to be able
to understand how to work within your
systems and debug incidents
successfully.
Okay, let's go ahead and take a look at
the agent here.
Let's see.
I'm going to go ahead and just start a
new session here to make sure everything
is working well.
All right, let's say debug
my incident for me.
Okay, hopefully this one works.
Is anyone able to get it working on
their laptops better than I have on the
screen? Okay, we got some success in the
room, so hopefully this will work as it
goes along.

[00:23]
>> Okay, looks like we are streaming. We're
getting everything in.
Let the agent go.
Okay, agent is checking logs, debugging
everything.
So, if we just also look through some of
the data here as the agent is working,
the data that's actually being passed in
for our agent here is all local just for
our sake of our purposes for our demo
now workshop that we're running today.
But, with the ability for you to run
your agents within a container and
infrastructure, you can start to see how
things like your get metrics tool that
are currently pulling from JSON can be
easily moved to something like DataDog
or other production systems for your
infrastructure from that perspective.
So, everything that you see here that is
currently local can be something that's
easily movable into infrastructure as
well via Cloud Manager agents.

[00:24]
Okay. Let's all cross our fingers and
see if this one works.
Oh, there we go. Success.
Okay, so the agent has come in. You can
see here that if we scroll through all
the tool calls, everything is persisted
in the cloud from a logs perspective.
All of this will also be logged in the
observability console.
And then the agent has come back to us
with the incident response here. It says
that this seems to be caused by a
database pool exhaustion. Seems like a
commit that someone added here from
Alice to refactor the order summary
builder introduced a query that then
caused the pool resources to be
exhausted. So, it's looking at and
giving us the exact everything that went
wrong from all the metrics they were
able to call. It ruled out various other
causes, and then it's also giving us
recommended actions to take.

[00:25]
Another key component here in a lot of
other incident response management
agents that we built is actually giving
the agent to actually go ahead and fix
everything that it's been able to find.
By giving the agent then access to
something like Cloud Code for instance,
you can actually imagine this agent can
then go into your code base, suggest
fixes, put up a PR, and essentially do
everything that it needs to do to help
you go from initial incident all the way
to fixing the root cause. So again here
for demo purposes, we're stopping at
just the agent giving us the recommended
actions, but I want you all to imagine
the possibilities of where this can go
if we give our agent more tools, more
ability to take actions, access to your
code base, ability to put up PRs,
ability to fix incidents, so that you as
a human developer can just become the
oversight and watch over the agents as
they take action, and you no longer have
to go through and do manual steps like
actually following the agent's
instructions here to fix the root cause
of the incident.
So another key component of what we've
built here on Cloud Manage Agents is
session persistence. So when I come in

[00:26]
and hit hard refresh on the screen,
we're seeing that the agent is listing
the sessions and everything is retained
from all the sessions that we just ran.
We also have the previous sessions that
we ran all retained in the cloud. Looks
like this one actually came back to us
as well.
Um and the previous sessions where we
just said hi, everything is retained in
the cloud, and we didn't have to deal
with things like database and deployment
of our agent and moving it from our
laptops to production. Everything is
already maintained server side.
We can also see the ability to delete
sessions come in. So I've run that
delete, and now we have that um running
the session here. Now we have that
removed from our list here.
Another thing that I want you to take a
note of, which we'll talk through a
little bit in just a second, is the
states of the session. Here we can see
that the sessions are now idle. Just now
as they they running, they were in a
running state.
We have the sessions managed by state
here as part of that same durability and
maintenance and reliability of the
session. So, when I come in and ask the

[00:27]
agent something else like, "Who are
you?" I was able to easily resume the
session and execute as it goes along
within that same session window. So,
state management here is really
important to how manage agents works
under the hood.
All right.
So, now as if we just take a quick step
back and look through everything we were
able to accomplish. We started with an
empty agent here just built on a couple
of primitives on Cloud Managed Agents.
We then went and defined the agent
definition, the persona, the
capabilities. We gave the agent an
environment. We gave the agent data and
context to operate over.
We then gave the agent sessions
combining the agent definitions to an
environment so the agent can think
through which tools to call from an
agent loop perspective. And then it can
actually call those tools and take
action on our behalf.
We then came in and streamed the
responses to the user into our logs,
implemented some local tools as well as
the ability to delete sessions. And
within this Streamlit app here, we saw

[00:28]
how that actually affected from a front
end perspective how our agent was
actually able to be presented to our
users by adding all of these primitives
together.
So, now let's go ahead and move back
over to the slides to do a quick recap
and talk through some of the lessons of
what we learned about how Cloud Managed
Agents works under the hood. But
hopefully for all of you who were able
to actually build on your laptops, you
all were able to just build a site
reliability agent. So, congrats to you
all.
But let's go ahead and dive in a little
bit here into understanding what
actually happened when we put all those
pieces together.
The first thing we saw is that we saw
session speak in events and not
responses in and tokens in tokens out
from a request response perspective like
we see typical with things like message
API or other APIs that we see.
With Cloud Managed Agents, instead of
just having a request response, we
actually have events appended to the
logs.
Again, this is a huge portion of why
Cloud Managed Agents is so reliable and
secure, because events are coming
through and just added into an existing

[00:29]
session logs, so that it's easy to then
resume a session and kick back off where
you left off, and it's easy to then come
in and look at everything from a log
perspective. This is also really
important from a reliability perspective
when we separate the hands from the
brain of the agent. If a container goes
down, we can just spin that container
back up again, and we don't have to
restart the entire agent loop alongside
that container.
The next thing here is that we saw the
ability to implement local tools.
And we implemented in our workshop these
local tools defined in JSON and loading
them in via our local files here. We
were then actually able to see how with
our Cloud Managed Agents Harness, the
execution of the agent is completely
separate from the agent loop.
We defined everything that executed
locally on our laptops and our scripts,
um and our agent loop ran on the cloud
inside of Anthropic's managed
infrastructure.
Again here, especially with what we just
released with bring your own compute and
bring your own sandboxing here, you can
swap out where you want that agent to

[00:30]
execute its tools in your own
infrastructure or on Anthropic managed
infrastructure, but within your own
environments and your own containers as
well as you spin them up. Moving from
things like loading our tools in from
JSON into anywhere you want to have your
tools run, like a Data Dog client using
the same wire protocol, making it very
easy to then go from initially building
the agent for Cloud Managed Agents to
then actually producing it and deploying
it on production-ready infrastructure.
Next thing we saw here as we thought
about how our sessions are being
streamed into our users and what we see
from a front end perspective
is that we saw when our events were
being able to be streamed to our users,
these were in the forms of actually
things we care about as a user. We saw
events come in and we saw the agent's
ability to actually log everything to
its observability console.
And another key thing here is that as we
think about how sessions are controlled
in Cloud Managed Agents, you can
actually think about the state as being
something very powerful when you can

[00:31]
start to take action on behalf of
events.
What that means is that we saw a couple
of key states for sessions in CMA or
Cloud Managed Agents.
We went from idle to running,
rescheduling if the agent needs to retry
anything, or terminated if any of the
sessions fail.
And so the agent is able to restart from
a reliability perspective, a
resumability perspective, but also it
can actually do some very powerful
things.
For instance, you can actually have a
webhook run, and when an event happens
from a webhook, the agent receives that
webhook in and can then do something
like resume a session or kickstart a
specific state based on external events.
So again, this powerful form of having
events and sessions be the core concepts
of how Cloud Managed Agents runs means
that you can make it very, very easy to
compose your agent however you want it
to, and have the agent listen for things
that happen both internally and
externally via webhooks to take actions
or resume your agent as you desire.
And lastly here, something that we saw

[00:32]
come through through the agent that we
all built for the site reliability
agent, is that everything lives in the
cloud from the agent loops perspective.
The conversation is persisted. When we
hard refresh the page, we saw that those
same sessions were maintained. And we
saw that if we were able to, let's say,
exit out of the agent and come back, we
didn't have to manage anything from a
database perspective or wire up where
the agent is stored. We were just able
to have all of that persisted in the
cloud, again making it very, very easy
to go to production-ready agents.
And lastly here, I just want to talk you
through we just built the very basic
form of Claude managed agents. We saw
what was possible with just the very,
very simple primitives that we all built
with, the basic level of what you can do
with Claude managed agents. And already
there we were able to have something
that would usually take us a lot of time
to spin up from a production
perspective. All of compaction, caching,
tool calling, all of that was handled
for us there's via Claude managed
agents.

[00:33]
And even if we wanted to go beyond that
to make our agent much, much more
powerful,
we can do things like add in skills, add
in subagents, add in memory, add in
outcomes. These are all core components
that we offer to developers out of the
box from Claude managed agents.
I'll just briefly talk you through a
couple of the key components, but want
to encourage everyone to check out our
documentation, what's publicly available
on Claude managed agents, attend the
session after this one on dreaming to
dive in deeper onto these topics.
Subagents or multi-agents is a way for
you to have an orchestrator agent spin
up context with other agents so that you
can manage it from a context engineering
perspective where subagents can then
handle tasks and have their own context
windows and contribute back to the main
agent making it much more powerful from
a parallelization perspective as well as
the ability for context management.
Memory is something that's always very
important as we're building agents. I
hear a lot of questions about how you
can build self-improving agents or
agents that learn from user corrections,
agents that start to remember user
preferences. That's where we're offering

[00:34]
memory and a dreaming service for Claude
managed agents out of box.
What dreaming means for managed agents
is that Claude can actually come in and
also look through its own memory logs
and determine what to keep and determine
how it can actually start to memorize
and manage context for its own memory.
So, it can actually be able to really
accurately remember which parts of your
user preferences matter and which part
of user corrections you want to retain
for future sessions you run on that same
agent.
Outcomes is another one of my favorites
where for Claude managed agents, this
means that you can actually define a
rubric for your agent outcomes. So, you
can start to think of your agent's tasks
as something where you want the agent to
reach a desired outcome instead of just
executing calls and doing things on your
behalf, but not associating that to a
result that you want.
So, with outcomes, you can define a
rubric of exactly what you want the
agent to produce, and it'll figure out
along the way which tool calls and what
it needs to do to execute towards that
final result.
Vaults is something also that I hear
come up a lot as of interest for Cloud

[00:35]
Managed Agents because managing user
credentials is something that's very
painful from an access management
perspective, making sure that your
agents are secure and safe to run.
So, for vaults and Cloud Managed Agents,
there's actually an encryption that
happens between where the credentials
are stored on a separate endpoint and
what the agent is actually able to
access. So, you can manage these
credentials on a per user, per session
basis, all very safely and securely. And
this relies in large part during to that
architecture that I described earlier of
how the brains and the hands of the
agent are separated, so that credentials
can be stored very securely in these
vaults. This means that you don't have
to set up your own secret stores or your
own credential stores, and you can just
rely on the built-in capability here.
There are a couple other things here
that I won't have time to go through in
depth. So, again, encourage everyone to
check them out in more detail. There are
things like the ability to do web hooks
and really make this agent run on
external events, things like detailed
and fine-grained permission policies,
the MCP servers that I mentioned where
we just released new MCP uh server

[00:36]
controls as well. And something that I
also love just to briefly touch on is
the console agent builder where we have
built in a lot of capability and
functionality into the default developer
console, where you can start to see a
beautiful observability dashboard come
through and other ways for you to define
Cloud Managed Agents right there on your
consoles.
So, just as a quick recap to end us off
here of what we were able to accomplish
today, hopefully everyone leaves here
with a bit of a mental model about how
manage agents actually works under the
hood and be proud of yourselves for
everyone that was able to come in and
build on your laptops and actually ship
a site reliability agent so you can all
leave here being very happy with
yourselves that you were able to come in
and save future developers hours of time
of being woken up at 3:00 a.m. or 2:00
a.m. in the morning and being able to
handle incidents for them.
And next you also learned a little bit
about where to go next for how you can
really start to unlock the power that
comes with manage agents and think about
how your agents can become super powered
with all of these additional
functionalities.
So that is where I'll end up today but

[00:37]
thank you all so much for coming. I'll
be around on the side.
>> [music and applause]

</details>
