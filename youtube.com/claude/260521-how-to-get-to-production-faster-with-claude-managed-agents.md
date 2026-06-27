---
title: "How to get to production faster with Claude Managed Agents"
channel: claude
url: https://www.youtube.com/watch?v=zenIB7XLZxQ
youtube_id: zenIB7XLZxQ
published: 2026-05-21
duration: "29:04"
captions: en-orig
---

# How to get to production faster with Claude Managed Agents

[![How to get to production faster with Claude Managed Agents](https://img.youtube.com/vi/zenIB7XLZxQ/hqdefault.jpg)](https://www.youtube.com/watch?v=zenIB7XLZxQ)

<details>
<summary>자막: How to get to production faster with Claude Managed Agents (29:04)</summary>

[00:00]
[music]
>> Hi everybody.
Um, I hope everybody's having a good
time today. I am Michael. I'm a member
of technical staff here at Anthropic
working on Claude managed agents.
>> What's up everybody? My name is Harrison
and I'm also a member of technical staff
working on Claude managed agents.
>> Lot of members of technical staff.
>> Yeah. Yeah.
>> Um, okay. So, uh, today we want to talk
to you about Claude managed agents. Um,
but before we do that, we wanted to do a
quick recap over the last couple of
years and the exponential that we've, I
think everybody in this room has been
experiencing.
After that, we'll, uh, talk a little bit
about the motivations behind why we
built Claude managed agents,
um, followed by a deep dive into some of
the primitives that we offer with Claude
managed agents.
Um, and then afterwards, we will, uh,

[00:01]
bring out some of the partners that
we've been working with on some of the
new features that we announced today.
Um, and then we'll wrap it up with a
little bit of a getting started.
Cool. So,
uh,
AI capabilities over the last couple of
years have been on like an absolute
rocket ship of like an exponential. I
think, like I said, everybody here has
been kind of experiencing that.
Um, we started with like the Claude 3
kind of family of of uh, of models.
Um, and even back then, like you were
starting to see the the semblance of of
really capable things starting to
happen. Um, but really you you could
only really get like very simple, short
things, uh, going.
Uh, then with Opus 4, we went on an
absolute tear, um, and things like
Claude Code, uh, started like becoming
really, really prominent. Um, and then,
uh, these days with some of the newer
model families that we have, um, we're
seeing that like the bottleneck towards
increasing capabilities is really the
infrastructure around these models and
not so much the intelligence for them.
So, yeah, like I said with uh, Opus 3,
you could maybe have Claude like

[00:02]
generate a test function for you. Maybe
you you would steer it a lot throughout
and you were like approving every single
tool that you were doing. And then with
Opus 4 and Claude code becoming around,
you were able to maybe have it drive an
entire feature. It could maybe put up a
PR for you, but you were still steering
it a lot throughout the way.
Um and then with Opus 4 .7, the the the
newest model that we have, like Boris
mentioned earlier, people are clearing
their entire backlogs and are waking up
to like a bunch of merge-ready PRs,
which is amazing to see. Who doesn't
love waking up in the morning to a bunch
of PRs that you have to review.
Um and what we think we're seeing things
going in the future is entire quarters'
worth of work being able to be getting
accomplished within a couple of hours.
So, you can imagine a full M&A pipeline
being done end-to-end with like a a
swarm of agent teams.
And when these agents work for like a
couple of hours,
things like prompt plus tool use are
okay, but really where we start or we
need to start getting going is towards
like task completion and overall agent

[00:03]
infrastructure pipelines.
>> But in order for your agents to be able
to accomplish more, they need access to
more. And that's where Claude Managed
Agents is here to help you manage some
of the complexity. You can imagine that
if you have an entire team running an
M&A deal, they need access to secure
credentials, internal systems. If you're
making code changes, you need access to
your private GitHub repositories and the
credentials that allow that kind of
access. And additionally, you need
identity and off for your agents. This
is essentially an identifier for who
they are. Like you know, I I as an
engineer have access to Slack and my
email and a bunch of tools internally
like that. Our agents are going to need
access to those systems as well.
But additionally, there we're seeing
more and more different conversational
methodologies for interacting with our
agents. The first is probably the most
familiar with a lot of folks, which is
you send the agent text and it gives you
a response conversationally. But we're
seeing more of a transition towards
outcome-oriented agentic activity. So,
this is again, give the M&A deal that
needs to happen to the agent in the
agent set, and have them just go off and

[00:04]
accomplish the task, coming back to you
only when they feel relatively confident
that the entire activity is complete.
Additionally, as an agent platform, we'd
be remiss to not support other
methodologies of interacting with your
agents, like starting an agent and then
picking it up later on, maybe weeks or
months in the future when you want the
agent to pick back up right where it
left off.
So, it was very clear that um we're
going to start expecting a lot out of
these agents, and uh our developers will
as well.
Um when we were doing a bunch of
research as we were starting to develop
something like Cloud Managed Agents, um
we saw a lot of key sticking points
around infrastructure and primitive
development that um
uh really stood out. So, the first of
which was uh figuring out things like
context management and memory. Um these
things are things that work really,
really well if they are working, but if
you get it wrong, it can like completely
destroy how well your agents are going
to work.
Um and infrastructure concerns was
another kind of like big sticking point.
It was actually the number one thing
that was cited as preventing people from
being able to like skate the exponential
and like really benefit from these

[00:05]
improved model intelligences. Um you
need things like reliability,
scalability, security, um even latency
starts mattering when you're having
these things running prod.
Um and then finally, uh
none of this really matters if you don't
have observability into what these
things are doing. Um if you can't tell
whether or not your agent is succeeding
uh or doing things successfully,
uh it doesn't really matter. Like, how
do you can how can you even assess that
the the thing is good? So, with Cloud
Managed Agents, we did all of that
platform work um so that you don't have
to, so that you can kind of pick and
choose the primitives that we have
available out of the box uh around
infrastructure, agent primitives, and
observability, all available on the
Cloud platform um where you can kind of
pick and choose the the composable
primitives that we have um and and kind
of like build your product on top of
them. Cool, so that's a lot. How do you
actually get started building with
Claude managed agents? The first step is
just to define an agent. This is
essentially a bundle of configuration
that identifies who your agent is and
what it can do. It's a system prompt,
model, skills, tools, permissions, and

[00:06]
generally just the identity of the thing
that's actually taking the action.
Second, you need a
you need an environment in which the
agent will actually run. So, really
helps to give Claude access to a
computer. In this case, your agent needs
a sandboxing environment where you can
configure the network allow list and
pre-installed packages within that
environment.
When all that's ready to go, you can
actually kick off the session. Ask your
agent to go and complete some piece of
work and then come back to you when it's
ready to rock.
And through it all, if you want to
observe the agent as it's doing its
thing cooking, you can just listen to
the event stream and understand what the
agent is doing, why it's doing it, and
generally interact with it in whatever
way you see fit. So, let's demystify
what we mean when we're talking about
this event stream. Every session that
you start in Claude managed agents is
effectively a log of events that you
have where you or your end users are
interacting with Claude and Claude's
responding. So, we kind of like split up
the domains of events that we have
within the platform so that it's easier
for you to kind of understand what each
event means. Um the first of which is

[00:07]
user events. These are things that your
own end users or maybe your platform is
sending to Claude managed agent
sessions.
Um these could include text messages, um
images, documents. Um you can interrupt
your agent if you see that it's going
off course and you want to steer it back
onto onto its tracks.
Um tool results for custom tools that
you implement and uh execute on your
end. Um and even confirmations for human
in the loop controls for any tools that
are executed on Anthropic servers. And
then finally, we have outcome
definitions, which we'll go into a
little bit more detail about later.
Next, we have agent events. Agent events
are uh anything that Claude is really
doing um on on its side. So, this could
be responding to the user with a
message, um executing tools on its end,
um or coordinating with other agents,
which we'll go into a little bit more
detail later.
Next we have the session events. These
are just like the overall life cycle of
the session itself. So any descriptions
around the status of the session
changing from idle to running,
error recovery and information about the
sort of sorts of errors that Claude is
running into and outcome processing. And

[00:08]
then finally we have span events which
make it really really easy to understand
when certain things are starting and
ending like Claude starting to write
together really really long response.
>> So we know that's a ton of information.
So let's make it concrete by doing a
quick demo of Pascal, a fictitious agent
that's responsible for understanding a
little bit more about grocery shopping
habits of our users. So if we jump into
the demo, we're going to we're going to
start by showing our dashboard that's
integrated with manage agents. And we're
kicking off an analysis run where we've
clicked this analyze button in the top
right. Jumping back to the console where
we can see everything that the agent is
doing in real time. We can see the list
of events that are coming through the
event stream, tool runs, agent events,
generally understanding what's happening
in real time. On the right side, you can
see our agentic definition. This
includes the system prompt, model and
all of the MCP tool configuration that I
was talking about earlier.
And as we click into the environment, we
can also see our networking
configuration as well as the packages
that we've installed into our
container. Jumping back to our
application, we can see all of this
shown on our surface because all of this

[00:09]
is exposed via an API. And what's that?
Claude came back found some bits for us.
Looks like bananas are super popular I
guess.
>> I like bananas.
>> Uh and also jumping forward, if you want
to avoid the crowds, it turns out that
Sunday is not the right time to go
shopping for groceries. But then that's
not enough for us. We want to understand
more about how our shoppers are going to
behave in the future. So we had our
agent go ahead and kick off a predictive
analysis and reorder probabilistic
understanding of our users.
But again, that's not enough for us. We
want our agent to get even better over
time and we want to improve the way that
it interacts with these sessions. So
we've clicked this ask Claude button in
the top right, where Claude is actually
reading the transcript of our session
and is offering inputs for how we can
optimize the way that we've configured
it. So, in this case, it's a little bit
small, but on the right side, we'll see
that a Python script ran for over 20
seconds. This is a Python script that we
uploaded to the session, and maybe
there's a chance for us to
optimize that run time so things can
feel a little bit snappier for our
users. So, in a nutshell, that's a a
whirlwind tour of the console and many

[00:10]
of the features that we support out of
the box with managed agents.
So, as we jump forward, as developers,
you might want to go ahead and figure
out how to get started. If you have
Claude Code installed, which I I hope
many of you do, it's my favorite tool of
all. Uh feel free to just jump in and
use the skill that we ship with our
with Claude Code directly, the Claude
API skill. It knows all about managed
agents and will make getting integrated
an absolute breeze. Second, we also have
shipped a CLI that lets you interact
with your agents and your sessions
extremely seamlessly via a very simple
command line interface. And lastly, if
you just want to see some examples of
real code, copy-paste ready, you can fit
for whatever your needs might be, we
have a set of cookbooks that'll show off
what it looks like to integrate with all
of our API services.
So, we covered a lot of the basics, but
I wanted to go over some of the more
advanced features that we've been
releasing over the last couple of weeks,
just so that you're all kind of aware of
them. So, the first is probably my
favorite, is multi-agent orchestration.
It allows Claude to spawn other agent
threads with their own context windows

[00:11]
in order to delegate work to them. And
the cool aspect of it is that Claude can
pass these messages back and forth
through other Claudes in order for them
to do whatever specialized work they get
to do.
Um outcomes allows you as an end user to
define a rubric or a set of goals for
Claude to be able to iterate towards
getting towards. Um so, after it does
its kind of first pass iteration of
something, it'll start triggering its
outcome grading and will keep going like
that in a loop until it feels like it's
satisfied with the outputs it's given
you.
Memory allows Claude to kind of get
better over time by reading and writing
from these long-lived memory stores,
which makes every session kind of better
than the last that it's had.
And then finally, we have dreaming,
which we announced in research preview,
which allows Claude to kind of like
reflect and codify over like thousands
of sessions all at once in order to
produce new memories, edit existing
ones, and really make sure that the
memories that we're dealing with are are
top-notch.
>> And earlier this morning, you heard us
announce two new features that'll make
your agents even more powerful. The

[00:12]
first is self-hosted sandboxes,
effectively giving you the option to
bring your own compute infrastructure to
Claude if you want to run tools within
your own VPC.
Shout out to our partners at Cloudflare,
Daytona, Modal, and Vercel, who we've
been working with to support support
this seamlessly out of the box. And
second, we shipped a feature in research
preview called MCP tunnels, which is
basically a way for you to expose your
private MCP servers directly to Claude
via managed agents without ever having
to expose anything over the public
internet directly.
>> And just diving a little bit deeper into
how self-hosted sandboxes work, you can
bring your own kind of sandboxing
infrastructure fleet where you can
contain your own private files, your own
services, packages. You get to kind of
kind of control how these sandboxes are
provisioned
without using our kind of like native
Anthropic Cloud sandboxes. Inside your
own perimeter, you can control things
like network policies, your audit logs,
when these sandboxes are spawned and
idled.

[00:13]
Um and and everything if there is kind
of in your control without kind of
having to cede that over to Claude
managed agents.
All we'll do is just send you a signal
whenever we need to have a new sandbox
be provisioned because Claude needs to
do some some work in there.
And the nice aspect of it is that you
can either use your own sandboxing fleet
or use one of the partners that we just
mentioned earlier today in order to get
started with all of this.
>> And let's talk a little bit about MCP
tunnels. MCP tunnels again are basically
just a way for you to get your private
MCPs in your network exposed to Cloud
Manager agents without having to do any
fancy network configuration on your
side. Essentially, all you have to do is
expose a fairly basic proxy layer uh to
our to our uh MCP tunnels, enabling your
network infrastructure to speak directly
with Cloud via secure tunnel in the
middle. Okay. So, in order to get a
little bit deeper about private
sandboxes or uh self-hosted sandboxes,
um I wanted to welcome to the stage Mike
from Cloudflare, Yvon from Daytona,
Akshat from Modal, and Luke from Vercel
to talk a little bit a little bit more

[00:14]
about this. MY HAIR'S ON.
>> [music]
>> HEY.
>> HI.
>> GOOD TO SEE [music] YOU.
>> HI, FRIENDS.
>> AH.
>> HOW WE DOING?
>> HEY THERE.
>> Do you guys mind if we like take a
selfie real quick? I think that's like a
trend here.
>> Are we allowed to?
>> I I think it's mandatory, right?
>> Okay.
Here.
>> Nice.
>> We look great.
>> Okay, cool. Um thanks everybody for
joining us. Um you all run uh
companies or work at companies that run
sandboxing fleets for Agent, but you've
all built them slightly differently, and
I'm curious what you are each
individually kind of betting on here.
Luke, do you want to go first?
>> Yeah, I think one of the um things
that's foundational to us is we build
all of our infrastructure on top of like
the same foundation, so we kind of
talked about this as fluid compute. Um
internally, we've kind of called it a
system of hive.

[00:15]
Um and that allows us to give everyone
basically just like the full VM um
that's for yeah, whether you're running
a build, a sandbox, or a function.
Um and for us, that really means that
all of these things interoperate well.
We can reuse like the same features
between them. Um so, stuff like we've uh
just made public our like firewall for
sandboxes where you can filter traffic
and um, inject secrets and stuff like
that. Well, we can build that for one
thing and and reuse it across it all.
So, the same primitive is really
flexible from that way.
Um,
and I think that's really powerful for
when you're building something like
cloud managed agents and you can call it
from a function into a sandbox and vice
and verse.
>> Yeah. Nice. Um, Akshay?
>> Yeah. So, Modal is a compute platform
that we've built for today's use cases.
Uh, and one of the things we are really
good at is um,
we run a lot of compute across the

[00:16]
world. Uh, so we can uh, since we have
our own scheduler, we can spin up uh,
hundreds of thousands sandboxes in uh,
in order of minutes, which uh, we're
betting on the fact that people need a
lot of scale and they want to get to
that scale really quickly for use cases
like RL.
Uh, we also run in every region uh, that
you can imagine, so you can get low
latency if you care about low latency
from US West or US.
Um, and [clears throat] uh, we were
really designed around flexibility. Uh,
so one of the things we have is uh, we
we think a lot about persistent volumes.
Like, how can you customize that? How
can you customize your images? Um, and
also we have GPUs. Uh, and GPU sandboxes
are are actually a pretty big growing
use case for us.
>> Nice. Um, Yvan?
>> Yeah, so for us, so Deta Una, we are
a company that started out building
sandboxes from scratch and so we had one
definite principle that we were thinking
about when we were building this or
inside, it was that agents will need

[00:17]
what humans need. And so, when we think
about when we started this, at that
time, a lot of people were just doing
code execution boxes for for for the
most part, but what we sort of
understood was that agents like humans
will need like different sort of size
and specs, CPU, RAM, memory, different
operating systems, CPUs, GPUs, like
everything that a human needs for
agents.
They the humans need to get their job
done, agents will need as well.
But the difference is you have to have
that at insane amount of speed and scale
and things like, you know, pausing,
resuming, forking so that agents can try
multiple outcomes. And so when we were
building out Daytona, we're like, oh,
nothing that exists
in the market today can offer that from
an infrastructure perspective. And
similarly to you guys, we built our own
schedulers to basically enable this.
>> So, yeah.
>> Nice.
It's amazing. Um Mike.
>> Yeah. Um so Cloudflare, we're kind of uh
one of our big bets is actually on like
two different sandboxing primitives. So,
we have the the micro VM
which is, you know, if if your agent is
acting like a developer, you give it
everything a developer has. You can run

[00:18]
CLI tools, compile Rust, or whatever. Um
but we also have this different isolate
which is a or different sandboxing
technology called isolates,
which we think in the long term, like as
the price of intelligence drops and, you
know, 2 years from now the Sanitas the
world are running at Opus scale, we're
just going to get a massive, massive
amount of agents, and we're we're just
going to run out of compute, right? And
like we need something that can scale
even more aggressively than a micro VM.
And so we have this other technology
that can still do sandboxing, it can
still isolate your processes, but it
spins up in in, you know, milliseconds,
you can still write files, you can still
execute arbitrary code, um but it's
actually like much more lightweight.
You're actually like, you know, running
multiple tenants in a single process.
So, the ability to kind of flex between
these two different uh sandboxing
technologies is, you know, a big part of
what we're focusing on at Cloudflare in
the future.
>> Oh, that's that's awesome. Wide variety
of answers, too. Um I'm curious now that
uh self-hosted sandboxes are kind of out
and we partnered with all of you, um is

[00:19]
there anything that you're like really
excited to see people starting to build
on your platforms with managed agents?
>> Um I think for me
the like I'm in the management chain and
so one of the things I've been thinking
about is this idea of
everything that was asynchronous is now
synchronous and vice versa, right? And
that vice versa is like really
important. So
all of the synchronization that you used
to have to do that you would spend time
coding and then you'd have to find time
to like take a meeting to get the
product alignment or something like
that.
Now that's kind of where I spend the
majority of my time and agents allow me
to delegate all of that kind of
asynchronous work into the background
like much more effectively.
The way I've kind of been thinking about
this is like everyone now has a chief of
staff
where you that used to be like an
executive role. Every engineer can have
a chief of chief of staff like doing
market research trying to understand the
product that they're working on more how

[00:20]
customers are using it and stuff like
that. And so I think that that for me is
where I'm like super excited to see
essentially people have talked about
this as like personal software or
something thing but I really kind of
think about it as like that everyone's
now got a personal assistant
and I think that that's just going to be
super powerful for everyone in the
future. Yeah.
>> Yeah, there's so many use cases. Like
for example, we have DoorDash as a
customer.
They're automating account management
with agents.
But one thing that I am personally very
excited about is um
I don't know if you guys have heard of
Karpathy's auto resource thing.
But it's
basically Claude can optimize training
loops and um
what we found success with on our
inference team actually is they can have
Claude
optimize inference. So you can give it a
a workload and a benchmark and it'll
basically hill climb it and and make it
better.
It'll run like the Nvidia profiler.
It'll read the profiles and it'll just

[00:21]
go ham and and make things better.
And it all runs on modal because we have
GP sandboxes. So this is something that
people are running right now manually,
but with CMA I'm excited to actually
make this uh
a background agent that that just works
in Slack.
>> Yeah, you can give it something like
outcomes and it can it can go ahead and
iterate on it.
Um Yvan?
>> Yeah, so um there's so many things being
built that we're excited about and so I
don't know if I have enough time to talk
about that. Um
I can tell you the most exciting and
then we can loop back on on on the less
so, which is for me
uh which is essentially
that right now we I feel that the things
that are stopping the progression of
agents getting tasks done is essentially
infrastructure now, not the models
itself. Whereas we can now and I've seen
this people have maybe heard of it, not
heard of it. The the term is like the
human emulator. Essentially anything
that a human can do digitally or digital
knowledge knowledge worker, you can now
have an agent do if you give it a
sandbox. So for example, um
you have agents that can do, you know,

[00:22]
reporting or whatnot, but they can't
give you an actual end-to-end report
because some of the data might be locked
in a legacy application inside of a
Windows machine or Windows desktop
application. Um and so having an agent
spin up a sandbox that it can access the
things through an API for the most part,
but if it doesn't it can actually
install the application or log into the
system and then give you an end-to-end
result is something that I think is
insanely fascinating right now and I
think that is a big unlock going
forward.
>> Yeah.
>> Mike.
>> Cool. Um yeah, so when we launched the
advantage agents integration, we we
really like it leaned into
programmability and customization. So
you can like reach like very easily
write tools that now reach into like the
rest of Cloudflare. And I'm really
excited to like have all of that just
very readily available and programmable.
So um I don't know, I'm just thinking
personally like we have our new email
service and so we wrote something that
gives every agent an email address and
it can send email and you can customize
this. Or we also have our browser
rendering service. So you can uh you
know, run a browser and run like

[00:23]
arbitrary control and have audit logs
and whatnot. And so, I'm excited for
just like the toolbox of all these other
things being very readily available and,
you know, just write a little bit of
JavaScript and and customize it for your
needs.
>> Yeah. Um very exciting.
Um so, we Yvon, you know, we I I just
felt like 2 minutes earlier talking
about the exponential and how
uh it it's just wild these model
intelligences uh increasing that this
this quickly. Is there anything that
you've seen your customers building now
that they weren't able to build like 6
months ago?
>> So, the one I mentioned is probably
that, but another thing that's
interesting for me is essentially the
idea of continuous learning, which is um
essentially So, Daytona and a few others
here, we have two basic use cases. One
is background agents and one is
reinforcement learning. And we have some
customers that are essentially enabling
their customers to against the data that
they have every day, every week, every
month, essentially take that data and do
[clears throat] um
RL. And then in the morning or the next

[00:24]
day, they actually have a more
intelligent model, right? And so, I
think that is actually quite interesting
and we see that being built on the
platform today.
>> Yeah. Wow, that's that'll be really
really cool to see. Um Akshat, I'm
curious uh
like from your perspective at Modal,
like what do you what do you think is
the next like infrastructural like thing
that we will need for agents um after
sandboxes?
>> Yeah, I'm sure you guys are thinking
about this a bunch as well, but uh we
uh we're really interested in figuring
out how do we improve uh isolation and
permission boundaries for agents. So,
for example,
uh can you run Claude agent SDK in the
same sandbox as code execution, but
actually have better isolation between
the two?
Uh it's more of a short-term thing. I
think longer term there's so much stuff
to play with with like
compute and uh storage in particular.
It's like the I think the design space
of uh persistent storage is there's a
lot more stuff. Like can you spawn sub
agents that fork off like where what you
have right now? And maybe they can time

[00:25]
travel back and visit previous states.
Uh another thing we're thinking about is
like
um people deploy stuff from sandboxes to
modal functions. So, once something
works, you then make it a
deployed endpoint, but then how do we
equip the agent to actually sort of
reify its own code and like update it in
place?
Uh there's a lot of cool stuff coming.
>> Yeah. Yeah. Um and Mike, I think we were
talking about this a little bit
backstage. Um but what do you think is
like one of the harder problems with uh
running agents at scale?
>> Yeah, I mean I I think there are some
infrastructure challenges with scaling
up, but actually when we uh you know,
are like talking to companies and like
trying to deploy these things and we
even feel it internally, like it it's
very easy to get some like vibe coded
platform where people are spinning up
agents internally, but actually like
deploying that means that there are all
these security challenges that you have
to face and there are like so many
layers to it. So,
uh you know, how do we properly filter
egress? How do we properly uh you know,

[00:26]
assign identities to agents? And if that
agent then go creates another agent that
goes and creates a site, like how do we
properly assign identity all the way
down the chain such that it's only
getting access to the right data? And
like there are some protocols that that
are going around that like I don't think
the the industry is unified on that we
we should. Uh and then lastly, like how
do you get every service behind
something that understands that
identity, right? Like whether it's a
private service, you you all have the
MCP tunnels that you just launched.
There There's lots of challenges like
that where hey, I have to I have to
expose all my data across my company
across a a bunch of different platforms
to all speak the same language off wise.
So, I think that's one of the bigger
challenges right now.
>> Yeah, it's um it's very interesting
seeing how like everybody across the
entire tech industry is trying to solve
a lot of the same problems right now.
Um well, with that Luke, um I'm curious
what assumptions have been like breaking
over at Vercel when like the end user
that's like emitting the traffic for you
is is not a human but is instead like an
agent.
>> Yeah, I think there's

[00:27]
like so many different avenues that you
really have to like rethink when agents
are doing the majority of like your
compute your requests.
Um to kind of like touch on what Mike
was just saying is like
authentication is like one of these
things which is like if I have
permission to do something like should
an agent have permission to do on behalf
Should we distinguish between those two
things? Um one of the things I was just
like thinking about as well was um
this idea of we kind of mentioned like
storage and stuff like that of well when
I pause a task I can kind of like keep
where I am in memory
um and so that like resume-ability of
tasks is just like something that
everyone is still like really
um working to solve. And I think one of
the things that um
stuff like managed agents does really
well and a lot of these um kind of
harnesses that we have already for doing
work um they're still that like very
synchronous single player activity and
so what I expect to see is kind of the

[00:28]
multiplayer game completely change um
and that will also be something that
again like [clears throat] we haven't
really understood how to do like we
can't all get around a program a a
laptop like we used to and mob program
um
kind of as we did 10 years ago. Uh and
agents kind of once they're on a track
they're like oh got a plan I'm just
going to like execute like I just want
to um
kind of hit that function of achieving
what I've what I've set out to do.
Whereas humans have the ability to kind
of
uh go off of each other and say oh I
think the plan has changed and we should
we should diverge.
>> Yeah.
>> Um so I think there's there's a lot that
we still have to to answer and the
harnesses are still very powerful in
that regard. Um but yeah we're
definitely not completely solved yet.
>> Yeah. Totally. Um okay. thank you
everybody for joining me. Uh And thank
you everybody for joining me. I hope you
learned some stuff and had some fun.
Go try cloud manage agents.
>> [applause and music]

</details>
