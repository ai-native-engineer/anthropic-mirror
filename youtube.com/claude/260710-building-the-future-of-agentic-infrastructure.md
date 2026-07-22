---
title: "Building the future of agentic infrastructure"
channel: claude
url: https://www.youtube.com/watch?v=ksfm6jeTg3Q
youtube_id: ksfm6jeTg3Q
published: 2026-07-10
duration: "16:33"
captions: en
---

# Building the future of agentic infrastructure

[![Building the future of agentic infrastructure](https://img.youtube.com/vi/ksfm6jeTg3Q/hqdefault.jpg)](https://www.youtube.com/watch?v=ksfm6jeTg3Q)

<details>
<summary>자막: Building the future of agentic infrastructure (16:33)</summary>

[00:00]
You can tell
we’re API nerds,
because we're saying
agents
should talk to each other
through API.
It's been a crazy
six months.
Because I think
if we look back
six months,
most of what
the Claude Platform
was, was an API
that got you
access
to inference
and tokens.
And out of the
model and
sure, we had
started to build
some interesting
tools around the model
that could get you
more intelligence,
or could help you
lower your costs
or get more speed.
But I think of late
we've started to launch
some really rich features
within the platform
that help you get
a ton
more out of the model
that help
take infrastructure
problems off your hands,
and help
take harness
engineering problems
off your hands
so that you can really
get that intelligence,
at a much lower
cost for your team.
Angela, what has been
some of the most
interesting
feedback patterns you've
seen from customers?
I think
the most exciting ones
have been around
managed agents,
which has been
really awesome,
and I know you,
obviously product manage

[00:01]
to manage agents.
But it's been great.
I think the feedback,
has been really awesome,
especially around
concepts
like memory and concepts
like outcomes
and dreaming.
But I think my favorite
one actually
is a bit old school, but,
I did hear
a developer
who was using it
say they just really love
the abstraction levels.
And, that always warms
my heart a little bit.
Even as these workflows
are evolving,
there's still
this concept
of agent identity.
And so how do we think
about the idea
of workflows combined
with agent identity?
Yeah,
I think agent Identity
will actually probably
need to be
almost somewhat separate.
Like almost
the agent needs
to have its own identity.
I think today it's
still a little bit early.
People are still
discovering
interesting use cases,
and there's
still a lot of trust
that you need
to give an agent.
But I think increasingly
that agent identity
is closer
to something
where the agent listens
to an outcome
that you want,
and then it probably
comes back to you
and asks like, hey,
in order
to accomplish the outcome
that you gave me,
I need access
to A, B, C, and D,
and you may say,
you know,
A, B, and C
are okay,
but I don't want
you to touch D,
and then the agent
is able to go
and see if you can
accomplish that.

[00:02]
And then when it does do
that,
it's able
to kind of almost create
a service account
for itself.
And in that world
then you can audit it.
You can make sure that,
it's successfully doing
the things that you want.
And I think that is
probably closer to the
operating model
we’ll see
with the
identity layer
kind of evolving.
So a lot of what's
interesting
about
how agents can talk to
each other is like,
you can build an agent
and you can
expose an API,
or you can expose
just some mechanism
by which,
like another agent
can talk to that agent
the same way
that a person
might interact
with that agent.
And we've seen people
doing
some really
interesting stuff
from this perspective,
like,
some folks have built
on Claude managed agents
within the platform,
and then have
built like a nice
thin MCP server
that they can go
and expose,
and then
you can have another
agent just know
exactly how to call in
to you
talking to that agent.
And so, I think that is
extremely helpful.
And, you know,
just people
have been able
to do really creative
stuff like that.
So, why are these kind
of workflows
legitimate now?
Like what had to change
at the model
or at the infrastructure
layer
for this to be possible?
Models have obviously
just gotten better.

[00:03]
I think
that's a huge part of it,
because I think
previously
you would have had to
maybe build a whole ton
of scaffolding
around the model
and, standard operating
procedure type stuff
that make sure
that you have,
this stuff happens
and then that stuff
happens, right?
Like
the nondeterminism
of the model used to be
a lot more problematic
than it is today.
I think today
the models
are really great
and can actually
figure out
within some reasonable
guardrails,
like what are the steps
I need to take?
And what are the
things that I need to do,
I think they've also been
able to run for longer.
Like we have the right
infrastructure to
let an agent be, ambient
within a workspace,
and it can get triggered
by something,
and then it can go off
and run
at some workflow
for some period of time.
And, you know, come back
when it's actually ready.
So I think some of
this is
evolution of the model.
I think some of this is
evolution
of the infrastructure
in the way
that people are able
to actually stand up
and build agents
around it.
Angela,
I would love to hear
your thoughts
on how this, like,
nondeterminism that
Katelyn is talking about
has really evolved
the harness layer.
Yeah,
I think in the past,

[00:04]
it just felt like
a couple months ago,
really,
where people would
actually create these,
like,
very complex boxes of
business processes
that they'd put together.
So first
it needs to go through
step A and then step A
can only go to B
if and only
if all this kind
of stuff.
And it's a very complex
web of things.
And it ended up
being like very fragile,
I think.
in terms of an agent
actually
being able to exhibit
the intelligence
that you were
hoping it to have,
and you were obviously
trying
to automate something
or make it a you know,
a little bit more useful.
And we've kind of tried
to box
in a lot of the model.
As Katelyn mentioned,
with the model
getting smarter
and I think more
and more capable
more agentic in its
tool calling
and also deeper
in it's own
reasoning.
It's actually able
to get to a place where
you can kind of start
to delete some of those,
you know, restrictive
parts of the harness.
And so I see harnesses
actually
getting thinner
and thinner over time.
The other thing I see
is that with harnesses
getting thinner,
you almost have like,
meta harnesses.
I don't know what
to call those things.
Maybe
they're like saddles
or something
in the future.
But, I do think they,
they tend to combine
strategies.
So, for example,
we've seen
people do really
innovative stuff
where it's

[00:05]
multiple agents,
and this is built into
the harness in itself,
but multiple agents
actually compete
to go try and solve
a problem together.
And there's another
instance in which,
you spin up two of them,
and one of them
generates an idea,
and then the other one's
adversarial to it.
And there's
so many other strategies
you can build on
top of it.
We recently did
advisor strategy
as an example, where
if the model can't
figure out what to do,
it actually just goes,
reaches out,
and calls a friend,
and that friend
is hopefully smarter
and helps it figure out.
So I think things like
that is increasingly
where harness
innovation will go.
And we'll see a lot of,
incredible ways
where agents, through
that expansive
architecture,
are able to solve
more and more complex
problems.
Yeah.
I think this is, really
getting to the heart
of how we think
about harness evolution,
because, ultimately
you have all these
different composite
strategies, and over
time, we'll be evolving
to having hybrids
of these strategies
like you could start
with, the best of end,
sort of like
expansive approach.
And then
once you decide
on the right, framework,
then you can iterate on
that, single framework.
So you mentioned complex
problems.
Tell me about
a particularly
complex problem
that has inspired
you recently.
There was this one
really great hackathon
winner that was
super inspirational.

[00:06]
I believe
it's called Urrea.
I might be mispronouncing
that,
but they, you know,
had this problem
where inside
a bunch of different
manufacturing facilities,
there is this
need for an expert
who really understands
the machinery.
And then you have to kind
of listen to
and monitor
whether or not
certain machines
are going up or down.
And then you also have to
then read the manuals
for like that
specific component
inside the machine.
And traditionally
there's one person
in that factory
who has figured that out
over the course of maybe
like 10, 15, 20 years
working in that plant,
and then they retire
very reasonably.
And then you just,
you don't have
that expertise anymore.
This person
was actually able
to take all of these
types of pieces and say,
okay,
if I upload the standard
operating procedure,
if I build in monitoring,
I just attract signals
from all the different
types
of parts of the plant.
Then I can actually have
agents
try to mimic
that human judgment.
And it was really cool
to see them
actually be able to take
a significant
proportion of that
and then build in
what is basically
redundancy in,
you know, that person
retiring and actually
being able to return to
that agentic system
and say, okay,

[00:07]
I can rely on this
as a place to accumulate
the really important,
you know,
factory knowledge
that's necessary.
What about you, Katelyn?
What's
an interesting problem
you've seen solved
recently?
Yeah.
I think one of the cool
things
that's happening
within
engineering team
specifically, or
not even actually
engineering teams
just like
development teams
that are trying
to get work done,
is people are coming
up with agents
that are just
more powerful than just,
I can get some code
written, like
we have excellent
like, Claude Code
is an excellent product,
a whole bunch
of excellent
products around,
how can you actually
write code?
And I'm seeing people now
go further than that
and say,
okay, if I'm starting
from the very beginning
of a project,
what are all the things
that are going
to have to happen
in order for
that work to get done?
How do I need to think
about running my
development environment
to actually test the code
that I'm running?
Right?
Like,
How do I,
you know,
actually
write the PR up front,
like the requirements
documents
and then like
later on
verify all the
QA testing
sort of things
that need to happen.
And so there's
a few examples
out there right now
where people,
in larger companies
have actually
put together full agenda
systems and platforms.

[00:08]
That help them do
pretty custom
end to end development.
And I think a really
good example is
Shopify recently talked
about doing this with,
I think
they called it River.
And, you know,
there's been a few other
examples like this.
And I think this is
one of the evolutions
that has been made
possible
by just the evolution
of what
agents are capable of.
So it's clear
that some organizations
are seeing
a massive amount
of ceiling
raising on the problems
that they're
able to solve.
But not all organizations
are feeling that.
So what do you think
is the biggest barrier
to that?
Actual boundaries,
like the things
that can get in the way
for people.
Security
and compliance guardrails
that they need
to have in place in order
to feel comfortable,
like having agents
do the work
that they're able to do.
Evals, I think
is a big one, too.
In order to actually get
the most out of
the technology.
Security and compliance
is definitely a big
one here,
because I think that a
lot of teams
are operating on,
security assumptions
that prevailed,
you know, 20 years ago.
And now agents are
fundamentally
changing everything.
And along with
that comes security.
So I think that we have

[00:09]
a pretty fundamental idea
of what makes a
safe agent
with strong guardrails.
I think pushing that
concept uphill and
revising the checklist,
has been a bit of a,
a bit of a journey.
Yes. Yeah.
And Curious
for how you think
about ROI of agents
and how enterprises
can manage that?
Yeah,
I think it's a very,
top of mind question
for a ton of
different companies
right now as they
look at
how everything
is accelerating
and how they can
accelerate themselves.
I think,
you know,
there's a couple
different ways
to think about this,
but I tried to kind
of encourage
a slightly more like
simplified mental model.
I think oftentimes
people
want to jump to like,
how do I agentify
gigantic
old school processes
that I have,
and maybe
they have 120 of them
and they want to go down
the laundry list
or they're like, great,
this is my moment.
If consumer preferences
are changing
to fundamentally
transform
our entire product
service.
And I think all those
things are great,
but it's obviously
very hard
to go
through all of those.
And there's a very,
very wide
array of things there.
I do think that
from an ROI
point of view,
it's easier
to almost start
from the individual,
actually,
and to be focused

[00:10]
on how much faster that
individual is getting.
And it sounds really
almost like simple
and kind of,
you know, like
not sophisticated enough.
But I actually think
if you start there
and you are able
to accelerate
that one individual,
you can move from that
to then a team.
And as you get to
the team level,
you start to think about
the speed
that you're
generating there.
And then,
and probably only
then I would
actually start then
to encourage say,
okay,
if I can make this
team faster,
now what is my ability
to take this team
and think
through a process
across my company?
And realistically,
a process
typically requires
many different teams
and many different
individuals
who don't share
standard
operating procedures,
who don't share maybe
the exact same expertise.
And that's why we have
all them together
probably, you know, duct
taping a bunch of things
together.
But if you go through
that kind of phase
where you think about
speed
at the individual layer,
team and
their productivity,
and then lastly
followed by
how you're able to
string these workflows
together.
I think you're able
as a company,
to basically almost
light up
every single bar
that you eventually
care about,
so you can eventually
make your way
to that kind of list
of 120 workflows
that you wish
you could be agentifying.

[00:11]
And I think
if you think about it
from that point of view,
most of your ROI
calculations should
probably be on speed
first and foremost,
and productivity.
It tends to be much more
leading and successful
as the primary
mechanism
to take a look at
as that starts to,
I think, flower
a little bit
inside of a company,
then it makes more sense
to kind of transition
a bit to be like,
okay, well,
you know, maybe there are
financial metrics
that I wanted to push.
Maybe there are, user
metrics
that will help drive
the overall
like outcome productivity
that I care about.
And I think if
leaders and companies
are able to follow
that kind of process.
They're actually able to
drive more of that ROI.
And see,
it's stage by stage.
Katelyn, you keep saying
engineering teams
and I want to double
click on that
and say what is an
engineering team anymore?
So engineering
team for us
is a set of humans
that actually doesn't
look that different
than an engineering
team looked
6 months ago,
12 months ago.
You still kind of need
that set of humans
to understand the system
that they are building,
how to operate it,
how to be on call
when something's
going wrong, all of these
sorts of things.
But each of those humans
is just insanely turbo

[00:12]
charged by agents
that can help them
get their work done.
And so what we're
kind of seeing
is a bit of a shift
from an engineering team
that was maybe, like one
technical lead who's got,
you know, opinions on
how we should design
the system, right?
And then a whole bunch
of engineers who are,
you know,
picking up tickets
and getting work done
to almost the whole team
are people
who have strong opinions
on here's
how we end to end
build a product
or build a system.
Here's
what the technical design
needs to look like.
And then they're kind of
orchestrating
their Claudes,
for lack of a better
term,
to get the work done.
And so, for us,
our engineering teams
actually
look pretty similar.
But they're able to just
get so much more work
done, than
they were in the past.
I'm curious
how you think about
potential failure
modes of reliance on
agents
in an organization?
I do think
it does create a
sense of like,
hyper independence
in a way that is
maybe slightly false.
Like, you think that.
Of course, now
everyone's a builder,
so I can go
and build and yes,
I can like spin up
like ten prototypes.

[00:13]
And for you, normally
you'd be like, well,
which of these options
is the best option?
You do a little bit
thinking you
now have the ability to
be like, well,
this is cheap.
Like,
why don't I just like
launch all ten
and then whichever one's
the winner
is the one
that they will pick.
And so I do think
it creates this like
hyper independence
on every single person.
But oftentimes,
you know,
I think the quality
that comes together
from something
that's like
more systematic,
more holistic tends to
then be a little bit
harder to coordinate.
So I do think that's
a little bit of
the failure mode is like
if by giving everyone
hyper independence,
but not necessarily
organizing them together
to a concrete direction,
you might see like sprawl
that looks a little bit
like this.
And that can have pros
and cons,
but I think there's
definitely failure
modes that result
from things like that.
So where do you think
the puck is going?
What is the future
of agentic development?
I think it's like
deeply embedded
inside the organization
to a point
where you probably don't
really use tools
in the way that's like
so obviously
instantiated.
And what I mean by
that is you know, today
we all are reaching
for this
agentic tool
or that agentic tool.
And this one's
good at this
and that's good at that.
And I think in the future
it'll be closer to like

[00:14]
maybe there's
some common substrate
where we all kind
of engage.
It's like
familiar interfaces
and everything like that.
But you kind of
are just able
to kind of tag an agent,
spin it up
and down as you see fit,
and it just does a lot of
like work by itself
invisibly.
And so and it might even
actually be proactive.
Maybe it's the one coming
to you and saying, hey,
you know, we noticed
this thing went down.
And so
I dug into the details
and I figured it out
and I fixed it.
And here's the PR maybe
you want to review it.
And maybe
you even told it,
like next time
in the future
for things so small,
don't bother me.
Just go ahead
and, like, ship it.
And I think it'll look
a little bit like that
where it almost
feels like,
almost like an invisible
like substrate
that you engage with.
And in that world,
I think that every person
ends up
being at a place
where they
almost kind of like,
are able
to build kind of team
oriented agents,
but maybe not
in the sense of like
it's like another team
mate,
but more that
like the team orientation
of some workflow
that say, you and I have
there's an agent
for that,
and it's able
to actually map
to the kind
of preferences
the two of us
have been in.
The three of us
have a team based agent
and it like,

[00:15]
understands a slightly
different preference,
and it starts
to kind of fill
in a lot of the gaps
that are necessary.
And again,
I think still have
the common interfaces
and things we have,
but we might see it
a bit more of
as like
an operating system or,
or something like that
instead of,
specific tools that we
actively reach out for.
And how do you think
Claude Platform
will help us
get to that vision?
Yeah,
I think one of the bigger
things that
we've been kind of trying
to push the boundaries
on recently
are some concepts, like
outcomes is a big one.
Like we shipped in Claude
managed angents
this idea of an outcome
where you tell
Claude, like, here's
what good looks like.
Give it a rubric.
How many times
can it iterate
to go and try and get
that outcome successfully
before it stops, right?
And I think as we evolve
that concept,
we'll probably get closer
and closer to a world
where you're talking to
Claude and you're saying,
I want this outcome
and here's a budget.
Go.
You know,
and you don't really have
to think beyond that.
And I think
the idea of what
we're trying
to get out with
the platform
is make that so easy.
And being in a world
where you're spinning up
an agent every day
because you're like,
today,
I have to summarize
some interview notes

[00:16]
and put together a packet
of feedback, right?
Or something like that.
You can say, okay, great
agents, I want notes
look good,
looks like this.
And you can spend
this amount.
Go. Right?
And then you'll get back
what you want
and making it
so that you don't
have to work harder,
think hard to
actually create that,
is the gap that
we're trying to fill.
Making
that super easy.
This has been so
much fun talking
about the future
of agents.
Thanks so much, guys.

</details>
