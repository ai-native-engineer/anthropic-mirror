---
title: "How Ramp engineers work with AI agents at every step"
channel: claude
url: https://www.youtube.com/watch?v=i4odXOmgMLw
youtube_id: i4odXOmgMLw
published: 2026-08-06
duration: "21:59"
captions: en
---

# How Ramp engineers work with AI agents at every step

[![How Ramp engineers work with AI agents at every step](https://img.youtube.com/vi/i4odXOmgMLw/hqdefault.jpg)](https://www.youtube.com/watch?v=i4odXOmgMLw)

<details>
<summary>자막: How Ramp engineers work with AI agents at every step (21:59)</summary>

[00:00]
I told Fable to fix
all our import cycles.
I also told it
to make our app lazy.
So the app boots up,
and it’s
So the app boots up,
and it’s
an enormous amount
of Python modules
and Fable made
a lot of progress
in both of these.
A lot of this
code was merged.
Really understanding
what the boundary of
where these models break
is very important,
because those sets of
problems are
the problems that
we would want our people
to try
when the next Fable comes out
or the next
release comes out.
One of the first things
I tried
when I got my hands
on Fable
was I wanted to find
a use case in Ramp
that we can
empirically verify.
So it must be a large
piece of code
that I haven't read,
that Fable wrote.
It must be
in a non-product place.
So something in CI.
So this is for us
in our testing suite.
And I wanted
to empirically verify it.
To be able to produce
a lot of data and check
if the code is acting
like it should.
It's been working
really well.
We're running it
for a few weeks
in shadow, and it's

[00:01]
been consistently faster
than what
our current
implementation is.
But I threw the deep
critical problems
in our codebase.
So we have this large
monolithic
Python code base,
and I told Fable to fix
all our import cycles.
I also told it
to make our app lazy.
So the app boots up,
and it’s
an enormous amount
of Python modules
and Fable made
a lot of progress
in both of these.
A lot of this
code was merged.
Really understanding
what the boundary of
where these models break
is very important,
because those sorts of
problems
are, the problems that
we would want our people
to try
when the next Fable comes out
or the next
release comes up.
I have these tests
that I give every model
when they come out,
and I just sort of,
you know,
no model ever
just was able to do
all of these things.
But this is
the first model that just
did all the things.
And when Fable struggled,
I just used a dynamic
workflow,
you guys have used it.
This is like
where Claude
has a bunch of sub agents
that it orchestrates.
And using this sort of
like algebra
in the sandbox.
But essentially
it's like a new form
of test time compute.
And so you just
tell Claude,
you know,
use a workflow and
Fable does it.

[00:02]
Just yesterday,
it actually reduced our
CI time from,
I think,
18 minute P50
to 6 minute P50.
Wow.
And it just like
optimization
after optimization.
And they just kept
profiling it.
The code landed
then it waited a day
and used a routine
to schedule itself
to run a day later
to get that
real production data.
And then it just like
repeated
this for days on end
until it landed
all these wins.
And then it showed me
a chart when it was done.
Rahul loves that.
He’s a huge CI time
minimization advocate.
It's all I think about.
I just have a follow up
question for you.
So when
you're doing these,
dynamic workflows,
I would have to expect
that you've already
built up the familiarity
with Fable
as a main
agent?
Like a foreground
agent, right?
Because there's like
a lot of learning
from what
the 40 or 100 different
agents are doing
in the background
that maybe
you're not seeing,
but you do have to have
comfort by that point
because that's a big
workload.
Because the agents are,
you know,

[00:03]
able orchestrate,
so the agents
might have like
work translation
they might not,
they're executed,
you know, in
parallel or serial.
You might add more rounds
of like
adversarial verification
or whatever
it feels this task needs.
So yeah, I just trust it.
Essentially
my mental model
for dynamic workflows
is the test time compute.
It goes from
like low to medium
to high to extra
high to max.
And essentially
the way to think about
this is the maximum
amount of thinking
the model can use.
It won't always use a,
but it's the maximum.
That's why you have it on
the thinking dial at
the very end, right?
Exactly.
And for me, dynamic
workflows
are just like it's
a next level.
It's like another form
of test time compute.
It's new.
How do you think about
loops
versus dynamic
workflows
for achieving some sort
of long horizon thing?
So loops are kind of like
repetitive work.
And dynamic workflows
are like dynamic work.
Like you don't
you don't exactly know
what the steps
are ahead of time.
Like,
I use a loop, for
example, for babysitting
my pull requests,
to fix the CI,
and rebase them
automatically.
But then I use dynamic
workflows for things
like system optimization,
where you don't
necessarily know what

[00:04]
the next optimization is.
It's a total mental model
shift.
It does feel like
using Claude Code
for the first time,
where you have to start
relinquishing
a lot of the software
engineering workflow,
including running
commands
to this agent, right?
I sort of feel like
for me loops is,
if you have a bunch
of engineers doing work,
loops are kind of slicing
a horizontal off of it.
Like if there's one task
every engineer
does every day,
you can maybe take that
and put it in a loop
or in a routine.
And this is something
like a code review,
babysitting a PR,
addressing feedback.
You know, like we just
have dozens of these.
Like, I have one,
for example,
for deleting dead code.
This is a routine
that runs every day.
And then on the flip
side,
you can do this
vertical slice.
And for us
this is like Claude tag.
And you know
an example of
that is I'll have tag
ship and experiment.
It'll make
the experiment,
it'll land the PR,
and then it'll set
a reminder for itself,
using a routine
to monitor
and check
in the next day,
it'll make sure that the
exposures are balanced.
It'll crank up
the exposure,

[00:05]
make sure the experiment’s
running,
and maybe a couple weeks
later, it'll be like,
all right, I'm going
to ship this variant
and it puts up another
PR for that.
And I wasn't in the loop
at all.
Like at the beginning
I asked Claude to do this.
I stamped
the pull request,
but the rest was just
Claude.
Okay, I want to like
detour a little bit.
I want to hear
about your coding setups.
So iTerm2,
pretty vanilla.
No IDE these days.
And as many pains
as my monitors
can handle.
Pretty barebones
Claude Code set ups.
so not a lot of plug ins
or skills or MCPs,
pretty simple
CLAUDE.MD,
inspired by your,
you know,
your Twitter posts
for the vanilla setup.
I think it's the best
way to learn the models.
And then
good amount of subagent use,
adversarial review.
Yeah, mine’s
gotten increasingly
background heavy,
and almost
most of my sessions are
information gathering.
It's like,
why is the memory
spiking on the service?
Or how can we get this
project done faster?
And it's
a great way to like,

[00:06]
fan out a lot of sessions
and gather
a lot of context.
When I do local things
local with Claude Code,
it's usually maybe more
hands on programing
where I, it's closer
debugging, or
I need more services
or context
on my computer.
Has that changed a lot
over time?
Like do you start
with a sort of,
you know, like an
Austin set up of like
just terminal, terminal,
terminal, terminal.
And then you kind of move
to this?
I mean,
we have so many services,
a lot going on
databases and message
queues and Reddits
and all that.
And so
having multiple instances
of local dev running
can become a constraint
very quickly.
Especially
with the latest models,
I think they require
much less hand-holding.
And sometimes you just
gotta let them cook,
get out of the way.
And so I found myself
carrying my laptop
with the lid open
a little bit too much.
And so then we decided
to move.
That’s funny. I know
exactly what you mean.
Yeah, make sure
Caffeinate is running, right?
So we've implemented
agents
at pretty much every
part of our business,
but especially in the
engineering lifecycle.
So if you take the process
of building and shipping
software,
everything from coming up
with ideas,

[00:07]
figuring out
where the bugs are,
getting notified
when there's problems
in our logs
and our systems,
to writing the code,
to reviewing them.
And sometimes
when they're after
deployed,
looking for
how they're
doing in production
and seeing if they're
doing the thing you want.
We've tried
to build systems
along this whole stack.
We've
also thought about it
from the lens of security,
trying to find bugs
and other issues.
Okay, so now you're
at the point where
you're using the model
kind of everywhere
throughout
like the whole lifecycle.
How did you get there?
What was like,
what was the first place
where you started
using Claude Code?
And then how did agents
kind of expand
out of that?
We were seeing and
slowly realized,
clearly this thing's
going to
continue to improve
and maybe we shouldn’t
build for 2.7,
maybe we should build for
whatever is coming next
or the model
after that.
And over time
as we built
these harnesses,
we’ve learned to step back
and just wait it out
because a lot of time
we end up
removing this scaffolding
over and over again
because the model is just
like outgrown harness.

[00:08]
At any given point,
when there's
a shortcoming
with the harness
or the model,
we've tried and
we're not perfect,
we also
need to make
the product work today
because otherwise
we won’t have business,
but we've tried our best
to go
the other direction
and give the model more
tools, more context,
more agency
with the goal of almost,
being able
to treat our agents
like a coworker.
So, hey, can you go
figure this out?
Like there seems to be
some sort of exception
that's popping up.
Or maybe this customer
is complaining
of a certain issue.
And we want the models
to be able
to access
the right systems,
the right level
of access,
and produce the right
amount of right code.
And so just wanting
that simple goal
allows us to
figure out what we need
to do to give the model
enough access
to do these things.
I think it's a
velocity bet
in a lot of ways.
Right?
Because you're
basically saying,
I think the stuff
we would put in place
to make this work now
really well is going to
become technical debt

[00:09]
really quickly.
And that's
going to slow us down.
If we aim
a little further
in the future
or sometimes a lot
further in the future,
you know,
we'll actually
make it further
with the resources
we have.
I have so many questions.
But maybe like
one direction
we can take is,
how do you make sure
they have the right
guardrails?
Like, you know, like
they can access this
data, but not this data,
or how do you make sure
the cost
is under control?
How do you make sure
the code quality is good?
And how have you guys
thought about this,
like as you
scale up the systems?
Yeah, so
we've also,
at various levels on
the stack, tried
to implement safeguards.
We also studied the trace
a lot.
One of the things that
I think we've tried to
focus more on is studying
individual traces
and less on aggregate
level benchmarks.
Benchmarks
do give us a lot
of information
cross model,
but a lot of the time
there's usually
a correct trace.
It's like,
what is the command
the model should have run
in this scenario,
and why did it
not get there?
Is this a context issue?
Maybe it does not have
access to the right tool?
And just following
these simple traces
for workflows
that should work
allows us to like get
there in the right way.

[00:10]
We've implemented
a lot of layers
of defense across,
I mean we’ll
continue to do that.
It's how,
how many layers
we have also
allows us to move faster
and give it more agency
and more access.
And so again, at
every part of the stack,
we've done everything
we can to give the model
what it needs,
but nothing more.
So you're essentially
like, you go to BigQuery
or Data Dog or whatever.
And you give it like a
read only service key.
This is essentially
how you think about it?
That's right.
Yeah, exactly.
So a lot of the time
so let's say that, you,
I just want to be able to say
like, talk to my agent,
like I talk
to my coworker.
And so
we're almost focusing on
the default experience,
the iPhone experience.
Where you open it
up, there's a text box.
You just say what
you need to get done,
not how to do it.
The prompts
must be declarative.
So we're not
we don't want people
to instruct the agent to
do it in a certain way.
We just want people
to say,
implement this feature,
or fix this bug,
or help this person out.
And over time,
especially when you focus
on the correct trace.
So what must the agent do?
It must first query
the source

[00:11]
and then it must query
these other sources
and read the code in this
in these repos.
Just by focusing on
what the correct
trace in your head is
you can then shape
the agent trace
purely through prompts
and tools and skills
to get there.
And thankfully
we're also on
this exponential increase
in model capabilities.
So maybe if it's not
working right now,
you just got to trust
that it will get there.
And just with that
belief alone,
just ship
it and just wait.
And the one thing
I'll add is good
old fashioned
hard controls
on top of that,
like you said,
like principle of least
privilege stuff.
The basics of
just not even giving it
the opportunity
to be able to do
certain things.
And how do you think
about like enforcing it?
Is it like the security
team's job to do this
or are you like
federating out the design
of these sort of systems?
How do you think about
that?
The really exciting part
about this is
the infrastructure
has been built
by the security team,
and it's been,
the security team is very
closely related to this.
So they helped us
set up the network
access policies.
They helped us
get the keys.
And they're also regular
users of these agents.

[00:12]
How do you think
about cost controls?
How do you think
about code quality?
What else do
you think about
as you scale it?
We're continuing to find
and look for cases
where, again,
we can guarantee
we know for sure
the worst thing
that could happen
if, for example,
this code has a bug or
something like that,
the effects
are extremely constrained
and we do have an upside
and we're finding
more problems like that.
And we're trying to use
this hammer for that.
We're also expecting
a massive increase
in the amount
of productivity,
especially with the next
few models coming.
And so we're
readying our
verification loops
especially
with CI and CD.
I think also changing
what our reviewers
look out over time
because as the
models get smarter,
they stop making certain
classes of mistakes.
And so you,
it's not worth spending
your reviewer tokens
on that anymore, right?
Yeah. I mean,
we've invested
in our own code
review bot as well,
which is also built
on Inspect or our
background agents API.
We pull from some
memories of things
that we especially
want to look for.
We have certain teams
that write their own,
skill files that look
for certain things

[00:13]
so that they can codify
the knowledge
that they have built up
over the years
into these files
that allow people
to move
a little bit faster.
It sounds like it's
not like Austin
and Rahul
that are going in
and just like breaking
down every bottleneck.
Although I'm
sure you're
doing a lot of this,
like how do you create
a culture
where engineers
feel empowered
and have like
the visibility
and the tools,
whatever you need,
to find the bottleneck
and to break it down?
It's just Ramp, right?
Yeah.
I mean,
I think a lot of it is
the culture
that the company has
built is a culture
of experimentation,
a culture of
like building something
that maybe didn't
pan out, and that's okay.
We've tried something.
You move quickly.
I think
one of the things that
has been helpful
is, because
we've had free access
to all the tools,
to all our engineers,
we don't really like
to impose
a certain
token budget
or a tool budget,
or tell people that they
should use this thing
or that thing.
And in general,
it becomes a lot easier
to speak
the same language.
I mean, it
sounds like
you guys just built
like a huge number
of these, like background
agents, like various CPIs
and systems internally.

[00:14]
So you mentioned
Project Glass,
you mentioned
Inspect,
walk me through these.
What are these tools?
How do you use them?
How are they built?
Yeah.
So Glass is where our,
it's the home
base for our non-technical
folks.
It's where they interact
with the coding agent
on a daily basis.
And it's been our belief
since,
since the beginning
that everybody
should have access
to this power.
And this velocity
increaser.
But you got to meet
people where they are,
you know,
they don't want to be
looking at code.
All the technical detail
is not going to help them
go faster.
And some things need to
be set up ahead of time.
Yeah.
Inspect,
at this point,
is basically a digital
coworker.
We've tried to give
Inspect all the tools
that a Ramp builder,
so product engineer
design person, would have.
So this includes access
to GitHub,
and Linear, and Slack,
and Datadog, and Sentry,
and various other tools.
And at this point
you can ask Inspect
to solve a support ticket,
or fix a GitHub issue, or
look at a Sentry error,
or Linear ticket

[00:15]
or Zendesk ticket,
whatever it may be.
It runs on
Modal in the background.
Your access it
via web.
Yeah.
And a lot of people kick
off stuff from Slack.
So if you're
in a conversation
with someone
about something
and you @Inspect,
can you go handle this
or can you put up a PR
to fix this
or investigate this?
And that actually
ended up being
the main way that
adoption was spread,
because you would hop
into someone else's
thread
and @Inspect.
Can you help them
with this?
And they’d see it and go, oh,
you can just do that?
Oh. Great.
Yeah.
And every PR
now comes with its own VM
and it’s like running for
a little while
so people can take over
sessions, collaborate,
it's all link
based.
It's all multiplayer.
It just works
out of the box.
And again
we've tried to focus on
the correct trace, like,
what should this agent
have done?
And try to shape it,
to that way,
so that it can
do a lot.
At any given point,
sometimes
people feel the urge
to move back to local dev.
We haven’t fully finished
this project,
but we've tried to
give Inspect
that additional tool,

[00:16]
that additional repo
or dependency
that allows people
to stay
a little bit further
in the background.
I also do want to mention
on call assistant.
So on call assistant
has been running on
and always ran on
Claude Code.
And that's another
instance of just taking
what works really well
locally, proving it out
building up the skills
and MCPs and prompts
that make, essentially
like an AI SRE
run really
well on incidents to root
cause them
and put up PRs of fixes
and then just packaging
that and
having it run
in a container
with safeguards
and guardrails.
So on call assistant
runs on every instant
that gets assigned
to our engineers.
So that includes customer
tickets, customer
support tickets
that require an engineer,
but also includes system
level incidents.
We're working on it.
And then comes back in
with a really solid root
cause analysis
in the Slack channel
that we have
for every incident.
And then the incident
responders
interact with it.

[00:17]
And we've had that
running since
late February or March.
The stuff
you can build
on the primitives
on this sort of Unix
philosophy,
Claude Code executable,
it's just wild.
Yeah.
We have a bunch of really
similar tools internally.
And, now Claude tag,
which sounds pretty
similar to Inspect.
It sounds like.
In a lot of ways.
Yeah, it's also
multiplayer.
It's also
kind of proactive.
You know, it's in Slack.
It’s sort of taken
over a lot of these
special purpose
bots.
I wonder if you guys are
seeing the same thing?
Yeah, we're
seeing something similar.
So more Inspect
sessions are coming from
automations than humans
at this point.
So every time something is,
there is some sort of trigger.
Sometimes
they're scheduled
at a certain
time of the day,
sometimes they're from
other external systems.
Then a session kicks off
and sometimes notifies
people and channels
or by DM.
And I guess for this one
also organizationally,
culturally,
how do you do it?
Is it like
each of these
automations is built
by different teams
that's closest to it?
Or do you have like
a central dev infra
or like AI team

[00:18]
that is responsible
for all of these?
It’s been very, surprisingly,
very decentralized,
and we're very happy
about that.
I mean, there are teams
that maintain certain
abstractions,
in the Inspect team,
as you mentioned,
the Inspect abstraction,
that is a bedrock
for a lot
of these automations.
And if you let everybody
build
what they would like to build
we’re okay with that.
And we want that,
we want more of it.
All we can do
is build a great product,
so other teams
are incentivized
to build on top of us.
It's also a mix of, like,
desire paths of people
wanting the same,
expressing the want
for the
same sort of thing,
or building the same
thing separately,
and then the sort of
platform team going,
okay, let's make a solid
thing for this.
And vision
from the platform team of
we're going to need this
when the model gets smarter.
Yeah. I mean, so
taking a step back,
one of the things that
we've tried to do
is not impose
limits on how much,
how many tokens
or dollars
each individual spends.
We want them to be able
to access
any level of intelligence
without limits.
So because of that,
we've tried

[00:19]
to do everything else
in our power
to make sure
that people can step up
and get that intelligence
where they want.
So that includes things
like defaults.
It's using batch and flex APIs.
It's using cheaper models
for automations
when they're not
human controlled.
So we always expect
to stay on the latest
frontier.
And so
we don't want features
or people
overfit on a certain
model's behavior.
And then there's
a good amount
of just
talking to people too.
I think you and I have
both done this
where we see
someone suddenly
become a top spender
on a certain month,
like way
above what
they normally do.
And we reach out to
them and say, hey,
what are you working on?
You know, it looks like
you're spending a lot.
I'm curious.
And if it's
something
that you're not planning
on platformizing,
but is platformizable
let’s work together,
let's do that,
let's expand the impact.
And if it's a mistake then
I'll help you with that.
And then
we can work on getting
the costs down later
if it's something you do
want a platformize.
So essentially

[00:20]
it's like this,
this culture of, like,
experimentation
and innovation.
It's letting you just
totally automate,
like a big swaths of work
that used
to be manual before.
So obviously it works.
And so then kind of
your job
is to support people
and optimize the use case
after it takes off.
Yeah.
And so the other way to
look at it
almost is like if you are
in the positive
ROI section
where you know that
every dollar
you spend on tokens,
you're actually
making more than $1,
you actually don't want
to be minimizing costs anymore.
We also expect the level
of intelligence
that fable has,
the cost of that
to decrease over time
as it has for the
last few years.
It's not anything new.
And we rather have,
everybody at Ramp
be familiar
and really good
at pushing the frontier
and pushing
with intelligence,
making it sweat
on hard problems
sooner than later.
What is your advice
to your peers,
to other CTOs
that are trying
to figure out,
what do you do?
How do you adopt agents?
make your way
through this thing
that's happening
in the industry?
We've made
a lot of progress

[00:21]
in the models today.
We have great
tools at our disposal.
But I think the thing
that people don't pay
as much attention to
is also
the rate of change
and how much things
are changing,
over the last few years.
And if you pay more
attention to that
as opposed
to the current snapshot,
then you begin to see
the pattern of
like rising intelligence
and agency,
the ability for models
to do more things.
And I think we've tried
to build for what comes
3 to 6 months
later down the line,
because sometimes
when you're playing catch up
and you’re building for
what's available today,
it might
already be too late
by the time you ship.
And so,
paying attention
to the scaling itself
has been very helpful
for us.
All right.
So with that,
Austin, Rahul,
thank you guys
so much
for taking the time
and for hosting us
in this beautiful space.
Thank you guys so much.
Thank you.

</details>
