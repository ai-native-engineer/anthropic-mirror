<!-- source: https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

# Code w/ Claude London 2026: Rethinking how we build

Couldn't make it to London? Keynotes and breakout sessions are now live.

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Code

* Date

  May 26, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build

This week in London, we brought [Code w/ Claude](https://claude.com/code-with-claude/london) to Europe. The event brought together builders, developers, and founders for two days of keynotes, breakout sessions, and workshops with the teams building Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a162288008621ab8a976251_image3.jpg)

*Cat Wu, Head of Product, Claude Code, chats with an attendee between sessions.*

Boris Cherny, Head of Claude Code, kicked off [the keynote](https://www.youtube.com/watch?v=6amLO7I9xdg) by describing the first time he felt the “magic” of coding. In secondary school, he wrote TI-83 programs that solved his math homework and tests, and taught himself HTML to make his eBay listings for Pokémon cards sell better. He learned by tinkering, and when something ran, it was exciting.

<!-- yt-inline:6amLO7I9xdg -->
[![Code with Claude London 2026: Opening Keynote](https://img.youtube.com/vi/6amLO7I9xdg/hqdefault.jpg)](https://www.youtube.com/watch?v=6amLO7I9xdg)

<details>
<summary>📺 자막: Code with Claude London 2026: Opening Keynote (46:27)</summary>

[00:00]
Heat.
Morning
London.

[00:01]
>> Hello.
>> This is uh this is the first time that
we've taken Claude uh Code with Claude
outside of San Francisco and uh I'm very
excited to be here with everyone. Um
before we jump in, can I take a quick
selfie?
>> Is that okay?
All right.
Ready?
All right. I think we got it.
I um I want to start today by telling
you how I originally got into coding.
I actually learned on a scientific
calculator
and uh I found out that I could program
my calculator to help me pass math tests
and do well on homework.
I was using a TI 83 calculator. I think
in the UK use Casios uh Casios for this.

[00:02]
And I found out that you could write
little programs in TI basic. This is
like the basic dialect for for TI
calculators.
And um I could reference the little
programs when I couldn't remember what
to do.
It worked beautifully.
I got great scores on my math tests and
my homework.
And then I taught my classmates how to
program their calculators
and they also got great scores on their
math tests and their homework.
At some point I even published a guide
on the internet for how to program
scientific calculators.
I was uh I was 13 when I wrote this.
That was my introduction to software. It
was very practical and um as as a kid it
just it felt like magic.
Around the same age, I figured out HTML,

[00:03]
not to build a startup, but to make my
eBay listings look better than everyone
else's so I could sell Pokémon cards.
There were tables, blinking text, the
whole thing. And uh and it worked.
I sold three legendary birds for 99
cents each.
They were all holographic
and uh in hindsight I wish I would have
held on to those.
There was a whole generation of us like
that, right? We didn't learn to program
from a textbook. We learned from
tinkering.
And I still remember the giddy feeling
that I got when one of my calculator
programs ran. You made the thing and it
did what you wanted.
And then somewhere along the way,

[00:04]
programming got complicated. Uh,
compilers, type checkers, build systems,
package managers,
12 config files before you could write a
single line of code. The distance
between I have an idea and it runs just
kept getting longer.
What's happening now is that distance is
collapsing again.
You describe a problem
and the program shows up.
It's the calculator feeling except the
calculator can write a distributed
system.
Now I get to watch people experience the
same feeling of bringing ideas to life
and it's happening on a scale none of us
imagined even a year ago.
It's so gratifying to talk to people
experiencing this every day from

[00:05]
individual indie devs to our biggest
customers that are taking on significant
challenges. For instance, Spotify uses
cloud code to migrate thousands of
repos. The team led by Nicholas
Gustiffson built a background agent on
cloud. It reads a migration that's
described in plain English and it runs
it across a fleet of agents opening PRs.
It's now merging over a thousand PRs a
month into production and it's cutting
migration time by over 90%.
That's real engineering hours back.
And sometimes speed isn't just about
efficiency.
It's about delivering on a mission.
Felicia Coruru is the co-founder and CEO
of Binty. Her software runs the systems
that case workers use to place kids in
foster care.

[00:06]
the paperwork, the home visits, the
licensing process. And this year, her
team used the Quad API to give case
workers back hours that they used to
spend on paperwork.
And they took 20 days off the process of
licensing a foster family.
20 days.
It's not just an efficiency metric.
That's a kid connecting with a family.
That excitement of solving problems is
something I hear from people all the
time. And I'm going to guess that
everyone here experiences this
differently.
Some of you are living on the frontier.
Some of you are bringing along the
people around you.
Many of you can feel the ground shifting
under us and you want a view of maybe

[00:07]
what's coming next
and all of us at Anthropic can feel that
shifting happening too. The industry is
moving at incredible speed
and that makes sense when you look at
the exponential and how fast these
models are getting better.
Remember a couple years ago, the
frontier of model development was so
good that Quad could draft a pretty good
git commit.
A year ago, we were sitting on stage at
our first ever code with quad event in
San Francisco. Opus 4 was the headline.
And the idea that Cloud could run for a
few minutes and build an entire feature
without a human checking in, that was
crazy.
Six months ago, agents started running
end to end overnight and I started being

[00:08]
able to wake up to finished work.
Then uh last month, Mythos read the
entire open BSD source tree and it found
a 27y old vulnerability that survived
every human reviewer, every fuzzer,
every static analyzer that was thrown at
it for almost three decades.
The jumps keep getting bigger and the
intervals keep getting shorter.
But even though model capabilities are
improving on an exponential,
most organizations are still adopting AI
on a linear path.
That means there's a growing gap between
what AI can do and what it's actually

[00:09]
doing for people.
Closing
that gap and translating model
capability into something that people
can actually use is what you all as
developers do. And you're doing it
year-over-year. API volume is up nearly
17x on the cloud platform. And on cloud
code, the average developer is now
spending over 20 hours a week running
cloud.
Like you, we've been shipping a lot
lately
and we want you to walk away today with
a clear picture of where we're headed.
So you can plan for it and you can ride
the exponential with us.
This event is how is about how we're
making our products work better for all
of you.
And this morning we're going to show you
what that looks like.

[00:10]
First, Lisa is going to talk about our
foundation. That's the model layer. And
she'll explore more about what what
going on with our frontier models and
what's coming next. On the cloud
platform, we're shifting updates to
cloud managed agents. And Angela and
Caitlyn are going to walk you through
how you can securely build and deploy
agents at scale. And then finally on
cloud code, CAD and I will walk you
through the latest features like uh the
new agent view and then important new
primitives like routines to let flood
prompt itself even when you're away from
your computer.
All of it comes back to you
and what you're going to build
because most people are never going to
call the cloud API. Most people are
never going to run Claude in a terminal.
They're gonna experience AI through
something one of you built on the cloud

[00:11]
platform.
A designer exploring new directions with
Canva.
A lawyer getting a brief out the door
faster with Lora.
Or a developer using any one of the
world's best coding agents.
You all shape what AI feels like for
everyone else.
We'd never be able to build something
build everything that people need to
solve their problems. This is only
something that you all can do.
So, uh, thanks for being here today.
Thanks for partnering with us to shape
what AI looks like for the world and for
joining us as we all reexperience those
feelings of learning to code and solve
problems again. Up next, Lisa from the
research PM team.

[00:12]
Hi. So I joined Enthropic in 2023 and
have been a part of every model launch
since Claude 3. That means I've been
involved in bringing 17 different
versions of Claude to end users and
developers.
Claude has come a long way. Opus 3
launched just over 2 years ago and was
our first model that was proficient at
writing long form code.
Sonnet 3.5 new sonnet 3.6 six really was
the first model that could use a
computer safely.
Sonnet 3.7 was our first model that
would think before giving answers. And
last year at this event, I introduced
developers to Opus 4. Opus 4, we didn't
know it really at the time, but it was
our first model that could write complex
Excel files and PowerPoint documents.
And now with our most recent models,

[00:13]
Opus 4.7 and Mythos preview, we're
seeing Claude is able to own outcomes
end to end and apply judgment to
complete tasks with high ambiguity.
So we haven't slowed down. In fact,
we've been accelerating.
We shipped eight Frontier models in the
past 12 months.
Each one builds on the last, helping you
write better code and deliver more
advanced experiences to your end users.
Claude's behaviors and capabilities
underpin everything else you're going to
hear about today. As Cloud gets
stronger, your starting line moves
forward.
Like Boris mentioned, we talk a lot
about the exponential adanthropic.
We believe as model intelligence
increases the value of use cases
increases exponentially.
So consider coding agentic coding is far
more impactful than code autocomplete.

[00:14]
In this way incremental intelligence
creates new markets and grows the pie.
As we build better versions of cloud we
are excited to see benchmarks improve.
But what's really exciting is when
Claude can do something that it couldn't
do before.
Tool use, computer use, thinking that
adapts to the task at hand, agentic
plans that hold agentic loops that hold
a plan over hundreds of steps,
long context windows.
We pioneered these areas. So when you're
building on cloud, you're building on
the model family that shipped these
capabilities first. and has had the
longest to make them reliable.
These capabilities are essential for
code, but the foundations of model
intelligence have gotten strong enough
to support a diversity of tasks in a
range of domain verticals.
So Claude can iterate on designs for

[00:15]
marketing presentations, can redline
legal documents, can build financial
forecasts, and even analyze genomic
sequencing data.
Let me share some examples of how
customers are using our latest model,
Opus 4.7.
AMP, the coding agent, moved their smart
mode to Opus 4.7 after it outperformed
on their internal benchmarks.
They also simplified their tooling since
the model no longer needed as much help.
Rakutin ran the model on their internal
benchmark and found it resolved three
times more production engineering tasks
than the previous model.
In it saw opus 4.7 catching its own
logical faults during the planning phase
and accelerating execution far beyond
previous cloud models. We also recently
launched cloud design by anthropics labs
powered by Opus 4.7.
Customers are using claw design to build

[00:16]
production interfaces in a single
sitting and we've heard that Opus 4.7
has a taste for visual design.
Developers building on the model
directly are seeing the same. We
continue to hear from everyday users
that Claude understands the assignment.
Users view Claude as a valued thought
partner since it's willing to challenge
their beliefs and push back when they're
wrong.
So, we've made tremendous progress, but
models are still imperfect.
Claude absolutely still has verbal
ticks, can be stumped by viral common
sense questions, and sometimes does more
than you asked for.
Watching Claude improve is what makes
this industry, this moment, and my job
exciting.
So, here's what to look forward to from
here.
Higher judgment and code taste. This

[00:17]
means models you can trust with complex
autonomous engineering.
Context windows that feel effectively
infinite as models take on longer
continuous work without losing their
core intent.
and multi-agent coordination, powering
teams of agents that can collaborate on
goals too big for any one agent or
model.
One metric I look to to make sense to
all of this change is task horizon. So
how long can a model work before losing
the thread?
Last year at this time, models could
reliably work for minutes. And today,
most users have agents that run for
hours.
We expect future generations of Claude
to run continuously.
So, we will have agents that are
proactive, that are always on, that know
what to do without being told. These

[00:18]
agents will be responsible for highle
goals that require judgment and
collaboration.
So, let me give you some examples.
Instead of asking Claude to write a
project update, you would ask Claude
keep the project on track this week.
Instead of asking Claude to produce a
financial forecast, Claude would own and
update the forecast to keep it accurate
over time.
So what should you as developers do with
all of this change?
Since the exponential keeps moving,
cloud models, future cloud models will
be more capable than Opus 4.7 and even
Mythos preview.
You need to build for emerging
capabilities, not just what works today.
That means designing for the next
version of Cloud, not the current one.
We've seen countless times that the
developers who win are the ones whose
architecture is ready to absorb the next

[00:19]
big jump.
Scaffolding is what we call the parts of
the agent that aren't Claude. So the
loops, the instructions, the tools.
We're seeing that as models get smarter,
the scaffolding that used to help can
hold Claude back.
Claude is intelligent and resourceful
and more intelligent models can al often
get further with generalized primitives
like a file system and sandbox computing
environment.
As models get more intelligent, you will
also need to keep making harder evals
and product prototypes.
They were they are how you will notice
that the exponential is moving
underneath you.
When a task that used to fail starts
passing, that's your sign to ship
something that you couldn't ship before.
And finally, as the pace continues to
accelerate, the teams who are getting
the most out of Claude are the ones who
treat model upgrades as a business
opportunity.

[00:20]
You should make the upgrades easy by
testing by automating your evaluations
and testing processes. And you should
test models hands-on to better touch and
feel how the improved intelligence and
capabilities will help your end users.
We are seeing the exponential continue,
which means Claude will keep getting
smarter and keep picking up new
capabilities.
You as developers are the first to feel
that you're the first to experiment,
the first to build new products, and the
first to find markets that nobody else
sees yet.
Now, Caitlyn and Angela are going to
show you how the Claude platform can
make this reality come to life.
So model capabilities are on this
exponential, but most businesses are

[00:21]
still on the linear. It's never been
more important to take advantage of
growing model intelligence to drive true
business impact. But what's preventing
these businesses from snapping to this
exponential themselves?
Well, it boils down to two key problems.
The first one is just getting the right
outcomes can be too difficult to build
an agent that does exactly what you need
to do. You need to do things like prompt
optimization, tool construction,
hardness engineering. There's just so
much you have to do to get it just
right. That's right. And the second
problem is you need to ship fast, but
you need to ship scalably at the same
time. Everybody is moving insanely fast
right now, and you've got to keep up.
But to win, you need quality, too. It's
really easy to build prototypes, but
it's hard to scale in production.
So, we've built the cloud platform to
give you everything you need to ship to
get the right outcomes quickly and for
scale. The platform gives you API
primitives that are tuned to cloud
models. It gives you infrastructure to

[00:22]
build and scale agentic systems and it
gives you controls to operate those
systems. That's right. Now, let's go
back to one of the most common problems
that Caitlyn and I hear all the time
from businesses. Businesses need
frontier level intelligence, but at
lower costs.
One of the ways that we're solving this
is with the advisor strategy. So, this
is really easy to implement. All you
have to do is update your tools and your
tools array on the messages API. And
what we're doing behind the scenes is
that we're splitting execution from
advising. So, in execution, you can use
a smaller model. This will make it a bit
cheaper. But when that small model needs
help, it can reach out to a larger model
for advice. Yeah. So in practice, this
means you can have a haiku or sonnet
class model do your executing and use
opus as an adviser. So we used the
adviser strategy. We ran this with
sonnet as an executor and opus as an
adviser. We found that sonnet performed
way better than sonnet alone. And
actually we found that sonnet performed
even more cheaply than on its own

[00:23]
because opus advised it to get its work
done better.
Eve Legal, for example, used the advisor
strategy and they told us they got
frontier model quality at five times
lower cost. And that's awesome. This is
a perfect situation where you can apply
it to a premium model. For example,
you'd want to put your best foot forward
with your product, but you'd have to be
conscious of your costs. It's also
really great in situations where you
have a extremely high volume of agentic
workloads. So, you have to keep an eye
out on your ROI.
All right, now let's talk about speed
and scale. those two things that Caitlyn
was saying that you have to do at the
exact same time. Recently, we introduced
Claude Manage agents. Claude manage
agents is an agentic harness paired with
production grade infrastructure. It
allows teams to ship literally 10 times
faster. You can now build a production
grade agent in days, not months. One of
our favorite examples of a customer who
built on cloud managed agents was Asana.
Asana built AI teammates so that humans

[00:24]
can collaborate directly with agents
within Asauna projects delegating tasks
and things like that. And Asana wanted
to build for speed and scale at the same
time. So they built on cloud managed
agents. And recently we introduced a
couple of key features that were
upgraded for cloud managed agents.
Multi- aent orchestration which allows
you to build fleets of agents. outcomes
that allow you to specify what success
looks like for Claude and Claude just
iterates to get it done and dreaming
where Claude can basically introspect on
its previous transcripts and learn and
self-improve. And today we're
introducing two more new features. The
first one is self-hosted sandboxes. So
this means that you can now have Claude
execute work on your own server. The
other thing is MCP tunnels. And for many
people who build internal agents, being
able to access your internal MCP servers
securely is now possible on Cloud Manage
agents through MCP tunnels. Cloud manage
agents spawn sandboxes when it's time to
execute work like editing files. And you

[00:25]
can still choose to use our sandboxes to
do that work, but starting today you can
also use your own. And we're introducing
this with first class support for
Daytona, Cloudflare, Verscell, and Modal
Sandboxes with super easy integration.
So, it's easy to get started with any of
these providers. With MCP tunnels, you
can have your MCP servers hosted behind
your firewall on your private network so
that Cloud Manage agents can access them
without exposing them over the public
internet. Should we check them out?
Let's do it.
So, Caitlyn and I have been working with
a fictional company called Counter.
Counter offers software for small
businesses to be able to build up a
digital storefront. Encounter really
wants to become an AI native business
and one of its most common workflows is
that it's constantly running growth
experiments to optimize its merchant
onboarding. Kalin has graciously offered
to help build a growth agent on cloud
manage agents for counter.

[00:26]
So here we are in counter slack
workspace. I'm in here with my colleague
Gabe. We're wearing our super cool
counter hats and we're ready to go. So,
we're really excited to see how our
latest growth experiment on our
onboarding flow has performed. And you
can see that our new growthbot came into
the Slack channel and it told us there's
actually a really clear winner in our
most recent experiment. The simpler
version of the onboarding flow is way
outperforming the older, longer version
of the flow where merchants were kind of
dropping off before they ever finished
signing up for counter. The agent is
proactively telling us it's calling the
experiment and it's going to get started
on cleaning up the old variant. which is
awesome. So, let's take a look at how
this agent actually is set up. And to do
that, I'm going to use the cloud API CLI
and the cloud developer console.
So, first let's check out the agents
configuration. You see here we've got
our system prompt, our skills, our
tools. Well, let's take a look at the
MCP servers. First, we've got Slack.
Makes sense, right? That bot was talking

[00:27]
to us in Slack. Then we've got our data
warehouse so that the bot can go and
read data about the experiments and be
able to determine what might be winning.
We've got our feature flags MCP server
so that the bot can call experiments or
start new ones and and take actions like
that. But let's look at these URLs. So
for Slack, regular public MCP URL, but
for the data warehouse and features flag
services, you might notice something
different here. We've got these URLs
that are behind tunnel.anthropic.com.
And what this means is both of these MCP
servers are behind counter's firewall
and only accessible via the tunnel so
that counter can kind of meet those
requirements of making sure that its MCP
servers stay on its private network. And
so let's pop into the cloud developer
console and see how this is set up. So
for counter, they set up a gateway in
their own private network. Then they
establish a secure connection to
Anthropic. As a result, any agent that
Caitlyn builds that uses the MCP tunnel
is now able to securely access internal
MCP servers.

[00:28]
You can go ahead and create these MCP
tunnels directly in the cloud developer
console. And we give you a couple of
different configuration options so you
can adjust them accordingly.
So counter's next big requirement is
that agent when it goes to do things
like write code and execute code, it it
wants us to do those things on a
self-hosted sandbox. it doesn't want to
run these things on public
infrastructure. So what we do is for our
cloud manage agents, we can set up our
environment to make sure that we're
using a self-hosted sandbox. So with the
self-hosted sandbox, now what's going to
happen is when the agent actually needs
to execute work, it's going to put a
work item in a queue. And here counter
is actually using Verscell's uh
self-hosted sandbox. And so what will
happen is that Verscell will actually
pick up that work item and then they
will actually spin up a sandbox in
counter's versell account in order to
execute the work. So one of the cool
things about cloud manage agents is that
we've got a whole bunch of really rich
observability within the console
experience. And so let's actually go

[00:29]
check out the session that ran that
resulted in that Slack thread that we
saw earlier. And so you can see here
that this agent is running a whole bunch
of different tools. But we can briefly
take a look and make sure that some of
the things that we cared about around
MCP tunnels and self-hosted sandboxing
are working the way we want. So first
we've got this set flag winner tool
call, which means that the agent was
able to work through the MCP tunnel to
call that MCP server for the feature
flag service. And then you can see here
too when the agent decides it's time to
write the code to clean up the old
variant, it checks out a new git branch
and it's doing this work on our Versell
self-hosted sandbox. Awesome. Let's head
back to Slack and take a look at what
this Growthbot agent has been doing. So,
first off, Growthbot is very proactive.
Not only has it figured out that it
should default the uh simplify variant,
but it also put together a PR in order
to actually do that defaulting and clean
it up. And when that work gets executed,
it's done on counter servers via the
self-hosted sandbox. Another great thing
in its productivity, you can see it also

[00:30]
gave us a little screenshot. So you can
see the old variant, which is a bit
messy, and the new one, and that
definitely looks cleaner.
Not only is this agent proactive, but
it's also collaborative. You can see
here, Caitlyn asked, "What next?" And
Growthbot was actually able to detect
that another great opportunity could be
to solve this 46% drop off that it found
in the onboarding flow. Now, Growthbot
was able to calculate that because it
was able to query the data warehouse
securely through an MCP tunnel. and we
love that it ended up by asking us, do
you want me to get started on that?
Thank you very much, Claude. All right,
let's wrap up.
So, today we introduced two big upgrades
to Cloud Manage agents with self-hosted
sandboxes and MCP tunnels. With this
collection of feature upgrades, it's now
easier than ever to become an AI native
business yourself and build agents for
all of your workflows and ultimately
accelerate whatever you are building.
And now Kad and Boris are going to come
and talk to you about how Cloud Code is

[00:31]
making it even more fun to ship as a
developer.
Thanks. Angela and Caitlyn just showed
you how the Quad platform bridges the
gap between what models can do and what
agents businesses ship. We see a related
challenge on cloud code to bridge the
gap between model capabilities and how
every developer can benefit from them.
First, I want to take some time to just
thank all of the builders in the room
with us today and watching online. Thank
you for trusting us and your production
codebase back when Sonnet 37 was our
frontier model and back when our product
was rough around the edges. Your support
is what makes the team so excited to
come in every day and make Cloud Code
better.
Let's back up to why Cloud Code exists.
Our mission is to help every builder

[00:32]
close the gap between having a great
idea and having a shipped product. The
way that we enable this is by building
tools that elicit the frontier
intelligence from our models and making
these tools accessible to every builder.
And we don't think of ourselves as
having a finished road map to hand to
you. We think of ourselves more like
mountaineers
just climbing alongside you in terrain
that none of us has mapped before,
figuring things out as we go. And we're
growing with you with increasing AI
capabilities and helping you manage
these new challenges as they emerge.
I remember looking back to last year
when I would give quad code a task and I
would read every single edit it tried to
make every permission prompt. I would
give it superdetailed guidance about
what to do and what not to do. Just
walking it through the details of the
change.
Now most of us are running in auto mode
to delegate permissions to Claude and

[00:33]
we're checking in after Quad has already
tested, verified its changes and has a
PR ready for us.
Looking back, Quad Code started in the
CLI and the terminal is still the
interface for power users who want a
minimal text interface and the most
control and customizations.
Then we added the IDE. This gives you
the same powerful agent, but you also
have the ability to follow along with
all the code changes as the agent is
working.
And we heard from you that many of you
are now juggling multiple cloud code
instances which we've affectionately
been calling multi-clotting.
We've added two new interfaces to help
you manage more agents.
One that I use frequently is quad code
on desktop.
It's a full screen graphical interface.
It has built-in previews, a sidebar

[00:34]
control plane, and the ability to render
images and rich outputs.
We've built desktop to be a single view
across both local sessions and your
cloud sessions with visual indicators of
which agents are running, which ones are
blocked, and which ones need your input.
Next is our newest surface, cloud agents
view in the CLI for people who actually
just prefer to stay in the terminal.
In this view, you can also see what's
running, what's waiting for you, and
what's done in one glance. You can reply
in line to unblock. You can jump in and
out of sessions, all without losing your
place.
The VS Code IDE extension and desktop
app are both built on the Cloud Agent
SDK, the same one that many of you are
building on as well.
And many enterprises have now adopted
quad code wallto-wall anthropic. We've
seen that this has driven a 200%

[00:35]
increase in the number of PRs per
engineer even as our engineering org has
scaled substantially.
Together with all of you, we're
redefining and discovering what the
future of engineering looks like by
embracing these new challenges that
we're encountering and building
automations powered by Quad to tackle
each.
Here's some of the feedback that we've
heard from our users and what we've
built with the help of everyone in this
community.
We heard from you that you want to spend
less time on code review. So, we shipped
a code review product that deploys a
team of agents to traverse all your code
changes and auxiliary files to catch
critical bugs. Thousands of companies
use this every day, including every
internal anthropic team.
We heard from you that you want to code
on the go. So, we launched remote

[00:36]
control and quad code in iOS and Android
so that you can fire off a task no
matter where you are. You're no longer
needing to walk around with this open
laptop or you're no longer stuck at your
desk. You can now go to a park, touch
grass, and still get your tasks done.
We heard from you that you're also
spending a lot of time babysitting your
PRs, fixing flaky CI tests, addressing
code review comments, and resolving
merge conflicts.
So, we added autofix. It listens for
these events and proactively fixes each
one so that your PR is always green.
And we heard from you that you want to
run cloud code on new tickets and on new
customer bug reports that are coming in.
So we built routines. Configure once and
cloud code can run on a schedule or in
response to a web hook or API request.

[00:37]
The work that used to require you to
manually kick off now just happens on a
schedule.
And last, we heard from you that you're
landing so much code that security teams
are struggling to keep up. So, we built
Cloud Security. It scans your codebase
overnight, flags vulnerabilities ranked
by severity, and lets you kick off cloud
code to address each one.
Each of these primitives that we've
built composes together so that we can
together
easily adapt to the future of
engineering.
Everything I've covered is something an
individual can pick up today, but it's
especially exciting to see how a range
of companies have adopted cloud code at
the scale of their entire engineering
orgs.
First, Shopify powers e-commerce for
millions of merchants worldwide and has

[00:38]
built AI use into its entire engineering
culture.
They use quad code across the entire
company, both across the engineering
org, but also non-engineers, so product
managers, designers, data scientists,
and they're bringing it directly into
their platform to stand up tools at
scale.
Andrew McNamera is the director of
applied AI at Shopify and in his words,
the speed is just crazy and quad code
has transformed how they build their
internal tools.
Another example is Marcato Libre.
They're Latin America's most popular
e-commerce site with over 100 million
buyers.
They have a team of 23,000 engineers and
their org runs on cloud code. When that
happens across an org, the work itself
changes. Engineers are pointing agents
at debt, tech debt that people haven't
had the time to fix themselves. It's

[00:39]
reviewed more than 500,000 PRs with
human oversight and modernized more than
9,000 of their apps.
Oscar Mowen leads technology and is
aiming for 90% autonomous coding in a
fully agent-driven PR loop by Q3 of this
year.
But the detail I love the most isn't
just the number. It's that managers and
VPs who haven't committed code in years
are now shipping again.
Quad code is putting coding back in the
hands of people who've spent the last
decade in reviews and roadmap sessions
instead of in their codebase.
And we see this across the entire
industry. Millions of developers are
getting more products shipped at higher
quality and at faster speeds.
Now let's see what this actually looks
like in practice. To take you through
it, please welcome the creator of Quad
Code, Boris Churnney.

[00:40]
I just realized we're matching.
Thanks, Cat. Um, I'm going to jump into
the demo in a sec, but um, first I just
want to say everything that we're
showing still feels magical to me.
using cloud code, I still get those same
feelings that I got when I programmed my
first calculator. And even inside
Anthropic in Slack, all day we're
trading screenshots of things that
engineers are doing in the wild with
Cloud Code. It's it's just so exciting
to see.
Um, and so today I'm excited to share
some examples of Cloud Code's magic with
uh with all of you. For this demo, let's
imagine that we're an engineer at Acme
Pay. It's a payment infrastructure
company. We're gonna start in the Cloud
Code desktop app. And we're gonna start
by working on just one single task. And

[00:41]
in this session, Claude is working on
adding refunds to Acme's merchant
dashboard. It's working on a full
implementation. Item potency so a
duplicate web hook doesn't double refund
a merchant. multicurrency handling
across all the regions that Acme serves
and uh audit logging for the compliance
team.
It writes the implementation and it's
going to verify its own work. Quad pulls
up the merchant dashboard in the
browser, triggers a refund,
and the modal closes before the success
toast appears.
It's a real edge case.
Claude sees the failure. It traces it
back to a race condition in the
optimistic update. It fixes it and it
verifies it actually works in the
browser before calling the task done.
Now let's zoom out.

[00:42]
Cloud code isn't running just one
session here. It's one of many sessions
all running and being managed in
parallel.
In the cloud desktop app, you can now
see all your cloud code sessions. Which
ones are running, which need your input,
which have PRs that have already been
merged and closed.
Synchronous coding is now just a slice
of what's happening at any given moment.
And we think that going forward more
code is going to be written in an async
way. And this is why we keep talking
about verification. If cla can check its
work, you can just let it run while you
work on something else and you can come
back to a fully working result.
A lot of my code these days is written
by routines. I'm not the one doing the
prompting. I'm the one that creates a
routine that does the prompting.

[00:43]
For the engineers in the room, think of
it like a higher order function.
Routines are a higher order prompt. For
example, let's go back to the refund
session we just looked at. A teammate
found a GitHub issue overnight. A
routine watching the repo picked it up
async and then it kicked off the working
clock.
With routines, developers can set up
async automations and wake up to PRs
that are ready to merge. Here's
our routines view.
Routines can be run on a schedule. They
can get kicked off by web hooks or even
kicked off by arbitrary API calls. And
you can run them locally on your machine
or on remote cloud compute.
Let's look at one more feature in
desktop.
This is CI autofix.
What it does is it watches the PR that

[00:44]
the last session just opened and its job
is to babysit the PR to production. It's
going to autofix any comments from code
review and security review, autofix CI,
auto rebase if there's any merge
conflicts.
And look at what just happened. CI
flicked on a network timeout. The
routine woke up, diagnosed it as a known
infra issue, and retried the job.
And actually in the cloud code code base
we we tell it to fix the root cause
instead, not just retry.
And CI is green. The engineer that owns
the PR is never going to see the red X
and that work is off their plate.
That's the shift. The default isn't I'm
going to prompt Claude code. The default
is now I'm going to have Claude prompt
Cloud Code.

[00:45]
Everything you just saw is available
today, uh, including routines and all
the latest updates to the Cloud Desktop
app. We're excited for you to try them
out and let us know what you think. We
hope these features continue to let you
close the gap between your ideas and
shipping products.
And that's really what every talk today
was pointing at. Lisa's capability
curve, Angela and Caitlyn's agents that
run on infrastructure that you control.
What Cat and I just showed you.
These are three layers of one story.
The capability is already here and the
remaining gap is how fast we put it to
work.
I encourage you to spend the rest of
today exploring these layers, research
talks if you're evaluating the models,
uh cloud platform sessions if you're

[00:46]
building for your users,
and cloud code workshops if you want to
learn more ways to bring cloud into your
day-to-day development workflow.
Dive in, go deep, and start building
with us. Thank you.

</details>


Somewhere along the way, he suggested, programming got complicated. Compilers, typecheckers, build systems, and each layer pushed the distance between "I have an idea" and "it runs" a little further out. With agents, that distance is collapsing again: you describe a problem, and the program shows up. It's the calculator feeling, except the calculator can write a distributed system.

From workshops highlighting how to [go beyond the basics](https://claude.com/code-with-claude/session/ldn-beyond-the-basics-with-claude-code) with Claude Code to optimizing [thinking budgets and effort levels](https://claude.com/code-with-claude/session/ldn-the-thinking-lever) across our models, we demonstrated how Anthropic and customers like [Spotify](https://claude.com/code-with-claude/session/ldn-coding-is-no-longer-the-constraint-scaling-devex-to-teams-and-agents-at-spotify), [Base44](https://claude.com/code-with-claude/session/ldn-from-one-person-to-80-scaling-a-hypergrowth-engineering-org-with-claude-code), and [Legora](https://claude.com/code-with-claude/session/ldn-what-legal-agents-inherit-from-coding-agents-lessons-from-legora) are already recapturing this experience.

## What was announced

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1623afcae08af4b3a9de5e_image1.jpg)

*Katelyn Lesse, Head of Engineering, Claude Developer Platform, and Angela Jiang, Head of Product, Claude Developer Platform, demo some of our new Claude Managed Agents features during Code w/ Claude London.*

Announced at the conference, Claude Managed Agents can now operate in a sandbox you control and connect to your private Model Context Protocol (MCP) servers. Now both the environment where an agent executes tools and the services it reaches run within the established boundaries of your enterprise. These two [new capabilities](https://claude.com/blog/claude-managed-agents-updates) are available on the Claude Platform:

* **Self-hosted sandboxes** (public beta). Tool execution moves to an environment you configure—your own infrastructure or a managed provider like Cloudflare, Daytona, Modal, or Vercel—while the agent loop that handles orchestration, context management, and error recovery stays on Anthropic's infrastructure. Your network policies, audit logging, and security tooling apply, files and repositories don't leave your perimeter, and you control compute sizing and the runtime image for compute-heavy work.
* **MCP tunnels** (research preview)*.* Your agents reach MCP servers inside your private network without exposing them to the public internet. A lightweight gateway you deploy makes a single outbound connection: no inbound firewall rules, no public endpoints, and traffic encrypted end to end. MCP tunnels are supported in Managed Agents and the Messages API, and are managed from the Claude Console by organization admins.

Teams including Amplitude, Clay, and Rogo are already building on Managed Agents with self-hosted sandboxes. To get started, explore the [docs](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes), follow our [cookbooks](https://github.com/anthropics/claude-cookbooks/tree/main/managed_agents/self_hosted_sandboxes), or [request access](https://claude.com/form/claude-managed-agents) to MCP tunnels.

## In case you missed it

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1623c3214b8b8cf8f378e7_image2.jpg)

*Lisa Crofoot, Research Product Manager, presents during the Code w/ Claude London keynote.*

If you missed the livestream, check our keynote and breakout session [recordings](https://claude.com/code-with-claude/london).

Code w/ Claude heads to [Tokyo](https://claude.com/code-with-claude/tokyo) next (June 5–6). All Day 1 keynotes and breakout sessions will be streamed live.

*Stay tuned for technical tutorials, guides, and customer stories inspired by our talks.*

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Jun 17, 2026

### Secure access to the Claude Platform with Workload Identity Federation

Product announcements

[Secure access to the Claude Platform with Workload Identity Federation](#)Secure access to the Claude Platform with Workload Identity Federation

[Secure access to the Claude Platform with Workload Identity Federation](/blog/workload-identity-federation)Secure access to the Claude Platform with Workload Identity Federation

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

May 7, 2026

### Collaborate with Claude across Excel, PowerPoint, Word and Outlook

Product announcements

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](#) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224ef32980bc807847d_a683fdcfe3e2c7c6532342a0fa4ff789c3fd4852-1000x1000.svg)

May 19, 2026

### New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

Product announcements

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](#)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](/blog/new-in-claude-managed-agents)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Apr 30, 2026

### Claude Security is now in public beta

Product announcements

[Claude Security is now in public beta](#)Claude Security is now in public beta

[Claude Security is now in public beta](/blog/claude-security-public-beta)Claude Security is now in public beta

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Claude Code
