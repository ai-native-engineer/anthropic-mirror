---
title: "Build a production-ready agent with Claude Managed Agents"
channel: claude
url: https://www.youtube.com/watch?v=jWWsLe4Gh5Y
youtube_id: jWWsLe4Gh5Y
published: 2026-05-21
duration: "27:23"
---

# Build a production-ready agent with Claude Managed Agents

[![Build a production-ready agent with Claude Managed Agents](https://img.youtube.com/vi/jWWsLe4Gh5Y/hqdefault.jpg)](https://www.youtube.com/watch?v=jWWsLe4Gh5Y)

<details>
<summary>자막: Build a production-ready agent with Claude Managed Agents (27:23)</summary>

[00:00]
[music]
>> Hi everybody. [music]
How's everybody doing?
Yeah? Okay, cool. Um,
raise your hands if you've heard the
phrase Cloud Manage Agents get brought
up like 50 times today.
Okay, and keep your hand raised if you
has have any idea what Cloud Manage
Agents even is. Okay, not a lot of
hands. Cool.
Um, and raise your hands if you're
excited to learn about Cloud Manage
Agents today. Okay, there we go. I like
that.
Um, hopefully this will be a little bit
more of a technical deep dive. Um,
myself and a couple of my uh, peers
earlier today talked at a very high
level. We showed you some slides.
Um, we talked about the primitives and
whatever. And we'll we'll do a little
bit about it here today, but uh, really
what I want to make sure that we do is
like have our laptops out, start coding.
I have a little starter repo for us to

[00:01]
kind of go through together. Um, and my
hope is that by the end of the session
you will be able to go get started with
building on Cloud Manage Agents today.
Does that sound good to everybody?
Cool. Quick agenda. Uh, we'll do a quick
overview of what Cloud Manage Agents is.
We'll go over a lot of the same kind of
um, discussion points from earlier
today.
Um, and then we'll we'll spend some time
actually building something um,
relatively from scratch.
Um, and we'll actually get something
that it you could be deploying to
production today if you wanted to.
Um, and then we'll wrap up the session
with some more advanced topics around
Cloud Manage Agents and just the the
composable things that you can do with
it.
So, um,
Cloud Manage Agents at a high level is
just a set of API endpoints that we've
developed and released. Um, you can go
use them with any API key today,
um, that give you
uh, access to uh, like scaled ready,
production ready uh, agents uh, and all
of the primitives around it that you can
just build your own products on top of.
You can pick and choose whatever
primitives you need
Um, and ditch the rest and then build

[00:02]
whatever product experience you need on
top of. So, we took care of a lot of
things like giving Claude access to a
computer,
giving it access to credential vaults if
you want to inject things like MCP
authentication for your own end users.
If you need to like get access to their
linear MCP or Claude more accurately
needs access to that.
The tool calling harness and everything,
retries and error recovery that might
happen
in production. As well as a bunch of
really nice primitives around like
memory and context management and
multi-agents that make it really really
easy to be able to really like escape
the exponential and like just benefit
from each increased model
family as they come out.
And then the really nice thing with
Claude managed agents which will show a
little bit later today is that we built
a lot of really nice observability
views into our developer console that
you can go to today in order to like
just live debug what these agents are up
to and we'll show a little bit of that
as well.
Cool. So, the the main kind of like

[00:03]
building blocks for Claude managed
agents are the agent itself which is
really just like think of it as like a
template. You want your agent to have a
certain system prompt. You want it to
have access to certain skills.
Maybe you want to define what tools you
want that agent to have access to.
Some agents you want to have access to
the bash tool and web search. Some
agents you want to really make sure
don't have access to the web because you
don't want them to get prompt injected
or whatever
and you can like really pick and choose
which which tools they have access to.
And you can also choose which MCP
servers they get connected to which is
also really really nice.
Another really nice added aspect of like
setting up all these agents is that you
can also define certain permission
controls on a per tool basis. So, you
can decide that something like the file
read tool can just auto execute whereas
something like executing bash or
calling your databases MCP server
requires explicit approval from from
your own end users. Um once you
configure that agent, you also can
configure an environment.
Um these environments kind of define the
template for how the sandboxes the cloud

[00:04]
has access to behave. So, you can define
whether or not you want those containers
to have network access. Maybe you want
to pre-install certain packages from NPM
or from uh pip. Um so, you can kind of
define that in your environment level.
And today, since we announced uh
self-hosted environments and sandboxes,
you can also bring your own sandboxes uh
that don't just run on Anthropic's
infrastructure. You can use something
like Cloudflare or Modal or Vercel
um and use those out of the box or even
your own um sandboxing fleet.
Um once you configure those two things,
you can then just like get started on
talking to to that agent, right? You you
have an ID for your agent, you have an
ID for your environment. That's kind of
all you need to get started with a
session. Um and a session is just you
can think of it as kind of like an
ongoing conversation with you and
Claude. It's the equivalent of going to
claude.ai and clicking new or uh
entering Claude code from your terminal.
Um once you do that, you can like start
submitting events from your own end
users, something like them asking for
something to happen. Um maybe you that

[00:05]
that end user is asking for a PR to get
put up. And that that all of that kind
of happens on the session layer.
And when you create these sessions, you
can also include certain GitHub
repositories that you want Claude to
have access to or
um certain files that you might want to
be preloaded into the container itself.
Um so, all of those will kind of be
downloaded and and provisioned on on
your behalf.
Um and then finally, there's just like
the events, right? Like these sessions
are just like ongoing event streams uh
where you submit messages from your
client um and we return responses that
Claude is processing them, doing
whatever it is that it's it needs to be
doing.
Um and that's that's effectively like
the the four major aspects of Claude
managed agents. There's a couple of
other things um alongside, but those are
like the main primitives that that you
kind of have to worry about.
So, diving a little bit deeper into the
events that we have, um, like I
mentioned, there's like user events.
These are things that you might want to
submit from your own application. Maybe
your user said something, or maybe your
platform just auto submitted some sort
of, um, user event. Um, these can
include images, documents, text,
whatever it is that you need.

[00:06]
Um, you can also send interrupts from
your own, uh, product, your your own
platform. Um, and you can use those in
order to cut off Claude if if it was
like going off on a bad tangent, or or
doing something wrong, and you wanted to
steer it. Um, so you can kind of use
that to prevent it from doing any sort
of like dangerous action. Um, you can
also submit, uh, tool results for custom
tools that you define and execute in
your own, uh, platform, um, or
confirmations for human-in-the-loop
controls for any sort of server executed
tools. Um, and then you can also define,
uh, outcomes, which allow you to like
essentially pass us either a file, or
like a blob of text that you, um, wrote
that, uh, it is almost like a spec that
Claude will like try to do a first pass
at implementing, or or doing the thing
that the spec defines, um, and then it
will launch, uh, it will essentially
enter a mode where it tries to like
iterate and check its work against that
rubric over and over again until it
finds that it can like it actually
satisfy that rubric, um, which we found
to be really, really powerful. Um, it is

[00:07]
it's a really, really great way to like
set up, uh, your agents for success.
Um,
next we have agent events. Agent events
are just anything that Claude is doing.
So, these are like messages that Claude
is sending back to the user, compaction
for if Claude is, uh, needs to like uh,
you know, compact its context window
because it got too large. Um, the tools
that it's kind of executing on your
behalf, whether those are MCP tools, or
the, uh, default agent tools that we've
defined. Um, and then there's also
multi-agent coordination events for when
Claude decides to spawn other agents to
help it in doing its work. And we'll
show a little bit of what that looks
like, uh, during the live, uh, demo.
Um,
next we have session events. Session
events are just like life cycle events
that let you know when the status of the
session is changing. Maybe it entered a
a retry loop. Uh maybe there's some sort
of error. Maybe there the the the
session needs to like idle for whatever
reason
um or if it needed to terminate. So,
they're they're just like a a bunch of
like state transitions um and error uh

[00:08]
events. Um and then there's also like an
event for like outcome processing. So,
you just know when Claude is entering
this mode of like iterating against that
outcome rubric. And then finally, we
have span events, which are just used to
like let you know when certain things
are starting and ending that we know are
going to be long long-lasting. So, like
everybody here has probably experienced
uh Opus 4.7 like you know generating an
entire document that's really really
long. So, we just wanted to make sure
that you know when that's kind of
starting and ending so that um you don't
think things are like just getting stuck
on our end.
So, um in addition to kind of like those
core primitives and the events that I
went over, like I mentioned uh earlier
today we launched uh self-hosted
sandboxes, which allow you to bring your
own containers um instead of using the
ones that we provide. Um a lot of people
already have existing uh like accounts
with Cloudflare or Vercel or Modal. Um
and uh a lot of the time you have your
private data up there and you just don't
want that to like exit your own VPC or
your own perimeter. So, um to get to get
around that, we uh are able to like

[00:09]
connect to those sandboxes natively um
and use those instead of using the ones
that we had on our own end. Um and then
you can kind of kind of configure how
those sandboxes operate and and, right?
Like at that point that that's entirely
up to you. We'll just let you know when
Claude needs a new sandbox and then
that's it. You just spawn one and
connect it.
Um we also launched MCP tunnels, which
very similarly allow you um if you have
like a, you know, private MCP servers
within your private perimeter, um you
might not want those exposed over the
internet. So, we set up a way for you to
have a secure tunnel
um that accesses those MCP tunnels or
those MCP uh servers that you have
privately in your own network. And then
Claude can directly connect to that
safely without those MCP servers ever
being exposed on the internet. It's a
really really nifty way for you to be
able to connect more private
data sources to to Claude and to Claude
manage agents.
So,
that's pretty much all I have for
slides. Maybe we'll get back to them a
little bit later, but let's let's

[00:10]
actually do some like fun stuff. So,
I'm going to be working out of this
repository. I want to zoom in on the
screen a bunch so you guys can see it.
It's a public repo if you guys want to
go clone it, get started with it today.
There's a bunch of really interesting
content in here from some of the other
workshop presenters. So, highly
recommend going through a lot of this.
There's a lot of really interesting
patterns here.
>> [snorts]
>> Today we're going to be focused on on
the production-ready agents.
And in this directory I included both
like a starter version of this web app
that I'll be showing you shortly.
And then the solution version of it if
you want to, you know, cheat skip to the
end and just see how things work end to
end.
>> [snorts]
>> So, what what are we actually building
here?
I built this very contrived deal desk
product.
You can imagine that we work on some
mergers and acquisitions. We have some
data available maybe in linear or maybe
in our private data sources. And we want
to use Claude in order to like help us
make decisions on whether or not we
should invest or maybe acquire certain

[00:11]
companies. I'm going to show you a kind
of like a finished version of this demo.
There's nothing like particularly fancy
here. There's just like a very basic
chat UI with all of my sessions on the
side
and some information about the session
itself on the right side.
But really the main thing is kind of
like this ongoing conversation between
me as an end user and Claude. And
the way that we set up this deal desk is
to actually use the new multi-agent
feature that we launched
2 weeks ago and uh that in order to like
have various agents with their own kind
of personas and their own ways of doing
things. So, maybe one agent is like in
charge of figuring out macro trends in
the overall in the overall industry that
you're working with. Whereas, another
one is like really good at like
financial analysis. Maybe it has access
to a bunch of tools that uh make it
better at that or a bunch of MCP
services it has access to. So, these are
all just like individual uh threads that
are happening here that like our main
agent thread like kind of kicked off um
in order to like answer a question that

[00:12]
we that we gave it earlier on. Um but
this is kind of like the finished
version of this demo and and I want us
to actually like take the time to learn
how to build something like this or
build even something more advanced than
this if you were to go home and get
started with Cloud Manage Agents today.
Um all the companies that I've made here
are obviously fake and Deal Desk is not
a real product, but I'm hoping that you
guys build really really interesting
things with this. So, um
let's get let's get started on doing
that. So, we're in the
This is too small, isn't it?
Okay. I'm going to zoom in a bunch.
Um
So, we're in this starter, you know,
directory of this uh of this code base
and I'm just going to start my uh
server for it so we can test it locally.
Um I'm using Bun because we all love Bun
here. Um and because it's the starter
version of this code base, immediately
we run into some problems. Uh
something's not implemented. Um and I
did this very intentionally because I
wanted to walk us through some of the
APIs that we have to use in order to

[00:13]
build something like this product. Um
so, very very basic at the beginning, we
just want to have a sidebar that lists
all of the sessions that we have, right?
So,
What?
Yeah, of course.
How's that?
Of course.
Um not really optimized for being super
big, but that's okay. We're going to
deal with it. Um and here's my code
here. Is this big enough?
Yes? Okay, great. So, first thing that
we ran into is we stubbed out some sort
of endpoint for listing all of our
sessions. So, obviously that's not going
to work.
Um and I'm going to try to implement
this function. I haven't written code by
hand in a little bit of time. I don't
know if you guys have, but please
forgive me if this is wrong.
client beta sessions
.list
I guess I have a little bit of a hint
off top.
Okay.
Yeah.
Let's copy paste this.
Um

[00:14]
And really what what am I doing here? Um
I'm using the Anthropic SDK that I've
imported.
Uh and all of these endpoints are kind
of available in production right now.
So, I just set up the SDK
um and I'm calling the list sessions
endpoint within the the SDK
um and just returning that data.
Relatively straightforward.
And I didn't even have to refresh the
page. That's how amazing Bun is. We we
now have uh we now have a
uh like the sessions listed from my my
workspace.
Um and we'll go over and talk about what
these look like in the developer console
shortly.
Um next, maybe we want to implement
I don't know.
I wrote a bunch of to-do's that are
numbered, but I don't think we should do
these in this order.
Um let's retrieve the session. So, to-do
number four.
Why not?
Cool.
Are you going to refresh? There we go.

[00:15]
And now we have all of the data
available here. Really, this is just the
API response from get session. That's
that's really all I'm doing here, right?
Like you you list the agent here.
Uh you can see all the tools that it has
available. It's connected to the linear
MCP.
Um and maybe we would have had some
outcomes defined for it, but we didn't
in this case.
Um now we want to implement the chat
view. That this is kind of the more the
more interesting aspect out of all of
this, right? So, there's two kind of
aspects to it. There's one, there's like
sending session events,
uh which is just like the, you know, a
very relatively straightforward endpoint
that we have. And then the other one is
the the streaming endpoint, which like
streams the events that uh Claude is
generating or the session is generating
from the server to our client. Um this
one might be a little bit more
complicated. So, instead of actually
doing this myself, I'm going to be
extremely lazy and I'm just going to use
Claude here. Um the really really nice
thing
is that uh Claude code ships by default
with the Claude API skill.
Claude API skill, uh which makes Claude

[00:16]
really really good at using all of the
Anthropic APIs, uh specifically the
managed agents APIs that we have. Um and
that's really all you have to do to like
make Claude really really good at at
using this thing. So, um I'm just going
to tell it, "Hey, I have a bunch of
to-do's in this code base for using
Claude managed agents. I think there
were some about
streaming events and sending events.
I don't know. I'm lazy. Look through
the to-do's and figure it out. Make no
mistakes. We all know that works so
well.
Okay. So, while while Claude is doing
this for us,
um it's going to it's going to read
through this skill. It's going to kind
of like learn, all right, this is how
the managed agents endpoints work. Um it
might even help me like optimize things
and make them a little bit better. We're
probably going to see over time this
thing kind of build and and become more

[00:17]
live as we go through it. Um
and yeah, that's pretty much all I had
to do to like set up this demo. Like
literally when I was setting up this
demo, I did a very very like I did a
version of what I'm doing right now on
this stage, where I just like asked
Claude to to me with building this
thing, which is really really nice,
right? It It It means that like Claude
can help you build your own Claude. Um
but uh while while this is like really
interesting and we can sit here and
watch Claude process things all day
long, we know Opus is a little bit slow.
So, while Claude is doing all of this,
um I wanted to quickly go over some of
the docs and APIs that we have available
today for Claude managed agents. Um so,
this is our like official developer
documentation. I know nobody really
reads docs these days. Everybody just
points Claude at them, but um I wanted
to make sure that everybody here kind of
knows that these are available. We have
a a bunch of endpoints for each of the
primitives that I defined earlier for
like creating an agent and and updating
it and fetching it and everything. Um
same thing for our environments. Um and
same thing for sessions as well. Um

[00:18]
including a bunch of like sub endpoints
for like listing all the events in an in
a session or listing all or streaming
those. Um you can also list all of the
uploaded resources uh in that session.
So, if you included a file in your
container or you included a GitHub
repository, you can kind of like list
those and add those over time to make
sure that your um session really stays
alive. And then with multi-agent, um
Claude can like spin off individual
threads of other agents, kind of like
what I showed earlier. Um so, there's a
bunch of endpoints that are associated
with that as well. Um
and then finally, there's a bunch of
endpoints for uh credential vaults and
for memory stores. And credential vaults
allow you to um provision a bunch of MCP
servers' authentication tokens one time,
store them very very securely on uh
within Anthropic. Um and we will make
sure that whenever Claude wants to use
one of the MCP servers, like the linear
MCP or the Figma MCP,
um we will inject those authentication
tokens if you like include that vault in
your session without Claude ever seeing

[00:19]
what those tokens are. So, we make sure
that like Claude it it never enters
Claude's context window or anything like
that um and makes the whole thing a lot
more secure.
Um with memory stores, we give Claude
access to like one or several memory
stores that it can then read and write
memories from over time so that every
session that it interacts with can like
read from those previous memories and
get better than the one before. Um and
we use all of these things within this
this demo that I've been working on.
Hm.
Let's see how Claude is doing.
Why would you not implement the rest of
these?
Finish the rest.
Dude.
Hm.
Um Claude Claude sometimes gets a little
lazy. Anyway,
um
there's a bunch of APIs here. I highly
recommend you read through these. I
highly recommend you read through some
of our like more long-form docs on
Claude manage agents as well. They do a
great job of kind of outlining all of
this stuff. Um but
uh you know, beyond just like reading
the static information, you can also

[00:20]
like really use the Claude console uh to
like monitor uh and get better
observability around what each of these
sessions is doing um and use a lot of
this UI for driving what your manage
agents integration looks like. Um
if you just want to get started really
quickly, you want to have some a more
guided experience, um we built this
quick start that allows you to actually
have a chat with Claude and Claude will
like help you build your agents and your
sessions uh with you. Um you also have a
bunch of like you know, predefined
templates that you can use as a as a
starting point. Um here you can like go
browse to like the actual agents that
you have. So, here I have a bunch of
test ones. Um clearly I made a bunch of
these. Um and like you can actually see
what each one like looks like. Agents
are versioned, so if you ever feel like
you made an update that you're not happy
with to like the system prompt or the
list of tools that it has access to, you
can always go back to use a previous
version
um and we never like get rid of that. Um
and this is kind of like where you see
the the certain things that it has
configured. So, in this instance, I
configured it with a linear MCP. I

[00:21]
didn't give it any skills, but I gave it
access to a bunch of other agents that
it can interact with
um and we'll see shortly what that looks
like in our sessions.
Do we think Claude finished yet? Do we
Do we think it's still working?
Okay.
Claude says it's done. I
we'll see we'll see about that.
Okay, sweet. Uh, refreshing the page.
Looks a little awkward with uh, with the
zoomed in screen, but um, generally
speaking, it seems like we can like go
and create new sessions. Everything here
looks good. I'm seeing all of my events.
Everything looks pretty good. So, let's
let's actually run this thing.
So, we're going to create a new session.
In this instance, I want to use the
linear MCP, and I want to use memory
stores for this uh, demo.
Um, and this is just calling our create
session endpoint. Um, and here I stubbed
out a couple of like, you know, uh,
like suggestion chips for myself for for
this demo. Uh, one is just a regular
message, uh, like just give me a quick
read on Acme Robotics, in order to get

[00:22]
uh, information about their financials,
I guess.
Um, but that's kind of boring. What I
really want to show you is uh, outcomes.
So, I have this other suggestion chip
that I set up that uh, includes a bunch
of information about like, hey, like
there's like three companies that we're
looking at, Bridgewell Dynamics, Norwood
Automation, and Acme Robotics. Uh, we
have a bunch of data about them all over
Linear and some files that we uploaded.
Um, but like we really we we want to
make a a good decision here. So, like
can you please like iterate on like
finding information about it and then
like criticize your own work and like
let us know whether or not this uh,
these these findings that you're saying
are like actually like satisfied to to
the rubric that we gave you. So, let's
use that. So,
all I did was just send uh,
outcome event or an outcome definition
event. And now Claude is just like off
to the races. It's going to start using
a bunch of tools. Um, I guess it's going
to try to delegate to a bunch of other
sub agents. Uh, and maybe read some of
the files that we have uploaded. Um, but

[00:23]
this is nice and dandy, but like
I don't know. I feel like I am not
understanding what's going on under the
hood here. So, maybe we can go and
monitor what the session is doing live.
Um, and to do that, we can go to the
sessions view
um, for this uh, agent
and actually click into a running
session
and see the the model kind of like
processing things live, right? So, it it
looks like it's already spawned the four
other agents that we wanted it to work
with. And each one of those has their
own context windows and they can like
chat with their coordinator and like
give it updates as as they're coming
along. So, they might say like, "Hey, I
don't know. I found this in a in the
financial or maybe I looked this up on
the internet. Um, you should know about
this." And maybe give another agent uh,
that information. Um, so you're going to
see each one of these uh, kind of like
horizontal lines is an independent like
agent that's running on its own.
Um, and then here you can kind of like
take a peek at like individual events
that are happening. So, I guess this
agent is doing some web searches. You
can see the actual inputs and and

[00:24]
outputs from those web searches. Um,
I don't know what it's actually looking
for, but it's looking for something. Um,
and then yeah, this these things are all
like iterating with one another. Um, you
can also like monitor how long these
things are taking. So, if you find that
a tool call of yours is taking a
particularly long period of time, you
can also just go and debug that and say
like, "Okay, maybe maybe there's a file
that is like really inefficient."
Um, I see you kind of have a question.
What's up?
So, you uh, the question was uh, can you
put plugins into these agents? Uh, we're
working on something along the lines of
that. We want to make sure that like the
Claude ecosystem is kind of like all
cohesively make sense. So, uh, we will
have started thinking about what these
things look like to make things a lot
more extensible and like open-ended. Um,
we don't have anything quite yet, but
the agent definitions themselves kind of
operate like these plugins. Um, there's
a lot of like similar uh, uh,
ideas behind a lot of them. So, we're
we're going to have something there
soon.
Yeah.

[00:25]
It's a good question.
Um, anyway, that's kind of like the main
like console view that we have.
Um, you have a bunch of like other tabs
for, you know, the environments that you
create. If you created a self-hosted
environment, you can see those here. Um,
or the credential vaults that I
mentioned earlier.
Um,
and then really what I love doing is
going and reading through these uh,
memory stores because you'll see what
Claude is like filling in as information
for itself. And sometimes I I want to
just edit that information if I feel
like it got something wrong. Sometimes
Claude messes up. Um, which is really
really nice here. Or you can generate
and add your own memories uh, by
default.
Um, so that's kind of like it for this
demo. Um,
you know, at the end of all of this
Claude is probably going to have
something like a like an outcome event
where it said like, "Okay, yeah, like I
feel like I have enough information for
you about these um, individual agents."
Um,
and then it gave me some sort of like
uh, like outcome evaluation. It seemed
like it it it seemed like it was able to
get to a conclusion for its uh, for its
uh, things that I asked it to evaluate.

[00:26]
So,
um, getting back to
the slideshow.
I probably skipped ahead a little bit,
but if we were to do all of this by
ourselves, we would have had to build
our own agent loop or maybe use the
agent SDK, figure out a way to host it
somewhere remote, um, figure out things
like context management and handling
state transitions and recovery from
those state transitions or integrating
something like skills and MCP servers.
We would have had to figure out a
durable storage layer,
um, where you can store all of the
events and all of the data about all of
your agents or all of your threads.
Um, we would have had to figure out a
sandboxing fleet, uh, like using
something like Cloudflare, but like
figuring out how to make that react to
what Claude is doing. Um, and then we
would have had to figure out the world
of like end-to-end user uh, or end user
authentication, which like
is not easy to figure out uh, or or do
in a secure and reliable way.
Um, so all those things are things that
we would have had to build by ourselves
if we were to get started on it today.
With cloud managed agents, we kind of
were able to get all of these things out
of the box. We didn't use all of these
primitives immediately in this demo, but

[00:27]
if we wanted to, we could have.
It would have been a very complex
looking demo, but that would have been
it.
Anyway, that's all I have. We finished a
little bit early, but if anybody has any
questions, I'm happy to answer them, or
we can leave a little early.
>> [music]
[music]

</details>
