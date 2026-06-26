---
title: "Code with Claude Tokyo 2026: Opening Keynote"
channel: claude
url: https://www.youtube.com/watch?v=N4efO8viXXo
youtube_id: N4efO8viXXo
published: 2026-06-12
duration: "42:25"
---

# Code with Claude Tokyo 2026: Opening Keynote

[![Code with Claude Tokyo 2026: Opening Keynote](https://img.youtube.com/vi/N4efO8viXXo/hqdefault.jpg)](https://www.youtube.com/watch?v=N4efO8viXXo)

<details>
<summary>자막: Code with Claude Tokyo 2026: Opening Keynote (42:25)</summary>

[00:00]
Heat.
[music]
Heat.
Heat. Heat. Heat.
Heat

[00:01]
up
here.
Hey, hey, hey.
Please welcome to the stage head of
engineering for the cloud platform at
Enthropic, Caitlyn Les.
Sto

[00:02]
anthropic
engineering
Caitlyn le
[applause]
Tokyo. This is the first time that we've
brought Code with Claw to Japan and
we're grateful to spend the next couple
of days with all of you. This morning
we'll be talking about our models, our
platform, and our products. But before
we get into it, I want to start by
sharing that just a few hours ago, we
released the fifth generation of Claude
models, Claude Mythos 5 and Claude Fable
5. These are our two most capable models
ever. [applause]
[cheering]
>> [applause]
>> Diane, our head of product for research,
will join us shortly to share a lot more
about why these models are so special.

[00:03]
I lead engineering for the Claude
platform. The platform gives developers
the tools they need to build systems on
top of Claude to harness its
intelligence. This is the highest
leverage way for us to help solve the
world's most important problems. And
this is why Anthropic is a platform
company. developers
all over the world, many in this room
today, produce far more value on top of
the platform than we could ever build on
our own. So, let's start with what I'm
seeing from our customers lately.
There's an incredible volume of powerful
application shipping right now, and a
lot of it is coming from right here in
Japan.
Rakutin is one of our favorite customers
to work with. Their team went from using
cloud code to accelerate development to
building on cloud managed agents to
power custom internal agents across
engineering, product, sales, and
finance.
One of their product managers
coordinates teams of agents exactly the
same way a leader manages teams of

[00:04]
humans. Now, they're shipping major
releases every two weeks instead of only
once per quarter.
And it's the same across Asia-Pacific.
Another great customer is Canva, the
Australian design platform that hundreds
of millions of people use. Most of their
users have never written a line of code.
But with the help of Plaude, Canva code
changes all of this.
Within a design, you can just ask for
something interactive like a map, a
calculator, or a widget. And Claude
built it into a working mini app ready
to drop right into your page.
All around the world, people are
building new systems and applications
powered by Claude that nobody could
build before. And we're all feeling this
shift. The landscape is changing faster
than ever. Things that weren't possible
yesterday have become possible today.
We're on a mission to keep raising the
ceiling of what's possible to build by

[00:05]
making models that are increasingly
capable.
A couple of years ago, the frontier of
model development was just the ability
to draft a really simple commit message.
And then one year ago, we were standing
on stage at our first ever code with
Claude event. Opus 4 was the headline.
And it was mind-blowing at the time that
Claude could build an entire feature on
its own.
And then six months ago, agents were
able to run overnight to complete
longrunning and autonomous tasks.
Two months ago, Mythos read the entire
OpenBSD source tree and found a
27year-old vulnerability that had
slipped past human reviews and static
analysis for almost three decades.
And earlier today, we released Mythos 5
and Fable 5.
Fable 5 is state-of-the-art on nearly
all tested benchmarks of AI capability,
showing exceptional performance in
software engineering, knowledge work,

[00:06]
scientific research, vision, and more.
These jumps keep getting bigger, but the
time intervals keep getting shorter.
But even though these model capabilities
are improving on this exponential, most
business capabilities are still on a
linear. So there's this growing gap
between what AI can do and what it's
actually doing for people. Closing that
gap is our collective opportunity.
And that is why we've built the cloud
platform. It gives developers the tools
they need to build more powerful agents.
Year-over-year API volume is up nearly
17 times on the platform.
We've been shipping a lot and there's a
lot more on the way. Over the next
couple of days, we'll share where we're
headed and we'll learn more about what
you're building.
Our goal is to make our models, our
platform, and our products work better
for all of you. So this morning, we'll
dive into each.

[00:07]
First, Diane will talk about our models.
She'll share more about our latest
frontier models, Mythos 5 and Fable 5,
and what's coming next.
Next, Angela and I will walk you through
how you can build and deploy agents at
scale on the Cloud Platform using Cloud
Managed agents. And today, we're excited
to share that we're shipping brand new
cloud managed agents features. You can
now schedule deployments to have your
agents run on whatever cadence that you
need. And you can store environment
variables in vaults so your agents can
securely make authenticated API requests
without giving them access to the keys.
Finally, Cat will walk you through the
latest in Cloud Code where the average
developer is now spending 20 hours per
week with Claude. She'll cover the
latest features like the new agent view
and dynamic workflows.
And all of this comes back to you and
what you're going to build. Because most
people will never integrate with the
Claude API themselves.

[00:08]
They'll never open a terminal and type
Claude. They'll experience AI through
something that one of you built on the
Claude platform
like a saleserson walking into a high
stakes meeting fully briefed by Slack
agents
or a lawyer getting a brief out the door
faster than ever with Lagora.
or a developer using any one of the
world's best coding agents.
This is why we're a platform company.
Every day I'm amazed by the collective
impact that you're all having building
solutions to the world's most important
problems.
So, thank you for being here, for
partnering with us, and for showing us
what's possible. Aratu goas.
>> [applause]
>> Please welcome Diane from our research
product team for your first deep look at
our newest models.

[00:09]
>> Please welcome to the stage head of
product management for research Diane
Penn sto
anthropic research product management
Diane Penn sama [music]
[applause]
>> [music]
[applause]
>> Hi, good morning Tokyo. I'm Diane and I
joined Anthropic in 2023 and I've been a
part of every version of Claude since
Claude 2. For those of you who are
counting, that's bringing 21 versions of
Claude across Haiku, Sonnet, Opus, and
now Fable, and Mythos to end users and
developers like you.
Our most recent launch happened just a
few hours ago. We released Claude Fable
5 and Claude Mythos 5, the first
generation of our fifth models.

[00:10]
Fable 5 is the most capable model we've
ever made generally available. It's
based on the same foundations as my 5.
These models are already accelerating
our work at Enthropic.
And for developers like you, Claude will
be able to be stronger and your starting
line will move forward.
We talk a lot about the exponential at
Enthropic, but what does this actually
mean?
For us, as model intelligence increase,
we believe the value of use cases it
creates increases exponentially.
For example, agented coding that many of
you are using today is far more valuable
than simple autocomplete from just a few
years ago. And we are already seeing
this with Fable 5.
Let's start with coding because we
believe that's where most of you will

[00:11]
feel the magic first. Fable 5 performs
the highest on Sweepbench Pro. But the
benchmark itself underscells the story.
The longer and the more complicated and
sophisticated the task, the farther the
gap between Fable and every other model
out there.
Two things drive that gap.
The first singleshot correctness.
Give Fable 5 a complex wellsp specified
problem and it will nail it on the first
pass. Early testers have told us about
single prompts that essentially create
work that would have taken days or even
weeks for a group of teams.
The second is long horizon autonomy.
Fable 5 can run for days on a single
goal and stay coherent the entire way.
It'll remember your specifications
even on tasks that span millions of
tokens. And it can dispatch sub agents,

[00:12]
keep them on track far more dependably
and with more cost consciousness than
any other model we shipped.
One more thing, Fable 5 isn't just good
at writing code, it's even better at
reading it. It's better at tree outing
outages and better at digging through
your repo history to figure out what's
broken when, and also to proactively
surface suggestions for making it
better.
Fable 5 is just as much of a step
outside of coding. Start with a work
that your organizations and companies
actually run on. Whether that's
financial analysis, documents, slides,
spreadsheets, Fable 5 manages that work
end to end. It'll stay follow
instructions, stay on scope, and what it
creates back for you will be
professional grade because this is a
model that we built for workflows at

[00:13]
scale.
It's also better where requests aren't
clean. What we've seen is that when you
give Fable 5 something messy,
multi-threaded, and ask it to figure out
what to do next, it could do that work
and outshine other versions of Claude.
Fable 5's version is also the best in
the industry. It can read dense
technical images, web applications,
plots, diagrams, charts far more
accurately than any other version of
claude we've shipped before.
Now, everything I've talked about is
about the upside of a model of this
capability. But intelligence of this
magnitude cuts both ways.
Two months ago, we launched Project
Glass Wing and made Mythos preview
available to a small group of partners
because its capabilities in cyber
security were strong enough to be
potentially misused.

[00:14]
Since then, we built a new safeguard
system and that safeguard system allows
that same intelligence to be shipped and
created and used by everyone with Fable
5.
This is a little of how it works. When a
request first touches cyber security,
biology or chemistry topics, Fable will
route it to our next most capable model,
Opus 4.8.
The response is clearly labeled and your
charged opus prices.
We know this is not perfect yet.
researchers doing legitimate work in
these fields will sometimes hit a block
and reroute. And we're continuing to
work on that.
But that's the type of trade-off that
allows our most capable models to be in
everyone's hands today as of this
morning instead of months from now. And
our customers are already finding value

[00:15]
with Fable.
Rakutin found that the highest effort
levels Fable 5 reflects validates his
work and for them that makes autonomous
automated operations possible at scale.
Cognition ran Fable 5 against their
frontier coding eval Crunchier bench and
it scored the highest of any model
they've tested.
They highlighted the long horizon
reasoning and how it generalizes to
unfamiliar tools, complex context right
out of the box.
And Jensen Spark told us that Fable 5
came out number one in their evals,
winning head-to-head against every
version of model they've tested. It's
actually the strongest on the hardest
tasks such as UI design and game coding.
So what about Mythos 5? It's the same
underlying model as Fable 5, but with

[00:16]
the cyber and bios safeguards lifted.
For Mythos preview, we showed what this
model class can do, and Mythos 5 is a
step beyond that.
It's available today for our CL
glasswing partners as part of Project
Glasswing.
Later this month, we'll begin enrolling
more researchers from life sciences to
access Mythos 5 because those same
capabilities that make biology risky are
actually the same ones that have the
highest impact for real good with AI.
So, as developers, what can you do with
Fable 5?
One metric I like to look at to make
sense of all of this change is time
horizon.
which is how long a model can work
autonomously before losing coherence on
what to do next.
With Fable 5, we've seen agents that are

[00:17]
proactive and know what to do without
being told. These agents can be
responsible for higher level goals,
responsibilities that require judgment,
collaboration, and proactive taste.
For example, instead of asking Claude to
write a project update, you can now ask
Fable to make sure the project stays on
track for the whole week.
Instead of asking Claude to produce a
financial forecast, you can tell Fable
to own, update, iterate, and improve on
the forecast to keep it accurate.
As you've seen today, the exponential
keeps moving. We need to build for
emerging capabilities, not just for
today's current models.
We expect future versions of Claude to
be more capable than the one that even
we are releasing today. And Fable 5 and

[00:18]
Mythos 5 are just a glimpse into that
future.
So, as developers, how do you take
advantage of all of this change ahead?
First, you should design for the next
version of Claude, not just the current
one. What we've seen is that countless
times, the developers who win are the
ones whose architectures, harnesses, and
product experiences are ready to absorb
this next jump in intelligence.
Claude is intelligent and resourceful.
And as models become more intelligent,
they can actually dig farther with more
basic primitives such as a file system
or sandbox computing environments and
far bless with sophisticated or too
complex harnesses.
As models get more intelligent, you will
also need to start making harder eval
prototypes for experiences that may not
work yet.

[00:19]
This is how you actually know that the
exponential is moving underneath you.
When a task or a prototype or a product
experience that wasn't quite always
working well starts working, that's a
signal to ship something magical that
you couldn't have done before.
And finally, as the pace continues to
accelerate, the teams who win are the
ones that get the most out of quad with
model upgrades and treat them as
business opportunities.
You should make model upgrades easy.
This means things like automated evals,
testing processes, and making sure that
you stay hands-on testing, pushing,
creating new things with new versions of
Claude. And this is how you'll know new
capabilities will be enough to deliver
new experiences for your customers.
We're seeing the exponential continue,
which means that Claude will get smarter

[00:20]
and be able to pick up new capabilities
for at scale.
And you as developers are some of the
first people to feel that. You're the
ones who actually can experiment, build
new products, and are the first to find
opportunities for new markets that
others don't see. And we can't wait to
see what you'll build next with Fable 5.
And now, Angela and Caitlyn are going to
show you a bit of how the Claude
platform can make this a reality come to
life. Thank you so much.
Please welcome to the stage head of
product for the Claude platform, Angela
Jen.
Stage
Claude platform
Angela Jang.

[00:21]
Last night, while we were all asleep, a
product somewhere noticed that it was
broken. This product read its own error
reports. It found the bug and it wrote
the fix and rolled it out to all the
users.
By the time the team actually woke up,
the problem was gone and the change log
was already written.
Now, in this situation, there was no
standup. There was no ticket. And this
is what a native AI company looks like.
This is not a company where people just
use AI to do their work. But instead,
it's a company where work itself runs on
the substrate of AI and people decide
what the outcome should be.
Now, this story can be a reality if you
have the right ingredients. And there's
three things to that. The first is the
harness, the second is the context, and
the third is the infrastructure.
These three are what turn raw
intelligence into true business
outcomes.
And that's exactly what the Claude
platform provides. We give you agentic

[00:22]
harnesses, context management tools, and
production-grade infrastructure that
allows you to become truly AI native.
Recently, we packaged all these together
through Claude manage agents, our new
product offering.
Fable 5 is the best model for building
longunning agents, and manage agents is
purpose-built for Claude. This means
when you put these two together, you're
able to actually get better agent
outcomes with significantly less effort.
Okay, let's talk about the harness. So,
the harness is what gives claude models
the ability to actually do work. It
includes tools, an environment, and the
permission to act. With a harness, the
model doesn't just tell you about the
fix. It actually makes it happen. You
don't want AI that just gives you
helpful suggestions. You want AI that
can actually do the work.
With cloud manage agents, we offer an
agentic harness that separates the brain
from the hands. The brain decides what
to do and then we spin up sandboxes or

[00:23]
hands to execute the work as needed.
Our harness also has an iterative based
ability to operate on an outcome. You
specify what that outcome is and then a
managed agent is able to iterate until
it actually achieves it for you.
Second, let's talk about context. Now, a
model is only as good as the context
that you actually give it. We offer a 1
million context window so that you can
have agents that consume high amounts of
content without any degradation.
But that's not all. We also offer our
agents memory so they can actually
remember what they've been doing. We
also give our agents the ability to read
and write skills of their own so they
can fill in the knowledge gaps that
they're missing. And lastly, we give our
agents the ability to dream so they can
inspect over their own previous
trajectories and identify how to
self-improve.
And lastly, let's talk about
infrastructure. Now, if you build really

[00:24]
longunning autonomous agents, this
requires extreme scale and reliability.
This is one of the hardest parts to get
right. Cloud manage agents automatically
spins up and down sandboxes and has the
ability to generate multiple agentic
fleets when needed to help you optimize
for reliable and persistent agents that
just get the work done without all the
hard work.
Building self-improving companies is
something that can happen today.
And we've worked with so many companies
that have built agentic systems on cloud
managed agents. And they've been able to
do that 10 times faster because they
didn't have to roll their own harness or
manage their own context or honestly
build up all the infrastructure that
they need.
Notion actually used manage agents to
power agent orchestration directly
within their product. As a result, their
users can delegate complex longunning
work to claw directly inside their
workspace.
And Notion isn't alone. ASA used managed
agents to build AI teammates. These are

[00:25]
collaborative AI agents that work
alongside humans inside Asa projects.
And these agents can take on tasks and
complete deliverables.
Now, I'd love to welcome Caitlyn back to
the stage to show what an AI native
company can look like if you build on
Cloud Manage agents.
Back in February, Claude became the
official thinking partner of the
Atlassian Williams Formula 1 racing
team. Competing in F1 racing requires a
great driver who knows the track really
well. But it also takes a team of
engineers and researchers to build a
rocket ship on four wheels that can go
almost 400 km hour.
To show you an example of Claude managed
agents in action, we worked with a
fictional racing team called Shankiro

[00:26]
Racing. Um, and we helped them build a
dashboard to analyze their car. Let's
see it in action.
Here we have the dashboard that we built
for the Shankiro racing team. And you
can see on the side we've got four
research projects. Each of these
research projects is backed by a claw
managed agent. So we have aerodynamics,
we have tire temperature, we have our
power unit, and we have driver safety.
And the goal for each of these projects
is for our agents to be able to figure
out what needs to change in order to
better optimize our car. And in this
we've used the cloud managed agents
feature called outcomes which means that
when an agent is doing its work we can
use a rubric to define what good looks
like and the agent can iterate until it
does its work incredibly well. So we
could go ahead and kick off any one of
these agents and that will start a run
of the agent in this case the driver
safety. And what's cool about this
dashboard being fully powered by AI is
we can go ahead and ask a question like

[00:27]
how much does a car currently weigh? and
how is this weight distributed and the
dashboard will go ahead and refresh with
this information. So now we know our 800
kgs are approximately broken down
between our power unit, our battery and
other components.
So if I were a developer working to
build this dashboard, what I would use
is the claw developer console as my home
base for developer productivity,
observability, and all the tooling that
I need in order to create these managed
agents. And so you can see we have all
of our sessions from our past runs of
our agents. And if we check one of these
out, we can open it up and see we get
really rich observability for everything
the agent is doing. We can see its
responses. We can see its tool calls and
ultimately when it finished its work.
Starting today, you can even schedule
these agents to run at any cadence that
you want. So we can come in here and
click create deployment. And maybe we
want to run a nightly safety check. And

[00:28]
we'll do this using our safety agent.
And so here we can decide when should
the agent trigger. And we can choose a
schedule such as every morning at 9:00
a.m.
But it's not enough for us to have
agents that are really easy to build and
to run. What's also really important is
for these agents to be really powerful.
And so we've done this in a couple of
ways like Angela mentioned earlier.
First, we have memory. With memory, our
agents can choose as they're working to
write their findings or write their
learnings to a file system. Then when
the agents run in the future, they can
look back into this file system on
things like decisions or findings in
order to do a better job the next time
around.
On top of this, we've built a feature
called dreaming. And so if memory is
real time deciding to write to a file
system, dreaming allows the agent to

[00:29]
look back over all of its past sessions
and update its memory and its skills so
that it does even better next time
around. [snorts] So if we come back to
Shankiro's dashboard, we can hit this
button that says dream. And this will
kick off a session for a new agent to
look back on all of the sessions for the
old agents and write its findings to
memory and to skills.
So everything you just saw like
outcomes, schedule deployments and
dreaming are available today on the
cloud platform. Developers everywhere
can start building with Fable 5 and
managed agents today.
Now Cat will talk about how cloud code
is making it even more fun to ship as a
developer.
[applause]
Please welcome to the stage head of
product for Claude Code, Cat Woo.
code.

[00:30]
[music]
[applause]
Caitlyn and Angela just showed you how
to build production agents on the Cloud
Platform. With Cloud Code, we're bring
that same leverage to your work as a
developer. Not agents you ship to
customers, but agents that ship code for
you.
First, I want to thank all of the
developers in the room today here and
watching online. Thank you for trusting
Quad Code back when sonnet 3.7 was our
frontier model and when our product was
rough around the edges. Your support is
what makes the team so excited to come
in every day and make the product even
better.
Let's back up to why Quad Code exists.
The mission of Quad Code is to bridge
the difference between an idea and a
shipped product. The way that we enable

[00:31]
this is we build tools that elicit the
frontier intelligence from our models.
And we make these tools accessible to
every builder.
And we we don't think of ourselves as
having a finished road map to share with
you. We think of ourselves more like
mountaineers climbing alongside you in
terrain that none of us has fully mapped
yet, figuring out what works together as
we go.
And we're growing with you with
increasing AI capabilities and helping
you navigate new challenges that emerge.
I remember just last year I would give
Cloud Code a task and I would review
every single edit that it made, giving
it detailed instructions about what it
should do instead, walking through on
every little detail of these simple
tasks.
Now, many of us are using auto mode to
delegate permissions to Claude and only

[00:32]
checking in after Cloud Code has already
tested its changes and put up a PR
that's ready for our review.
Cloud Code started in the CLI and this
is still the place for Power users who
want a minimal text interface and the
most control and customizations.
Then we added the IDE for users who want
the same powerful agents but want to
follow along with all of the code
changes.
Then we heard from many of you that
you're running multiple quad codes in
parallel which you've affectionately
called multi-clotting.
And we've added two new interfaces to
help make that easier.
The one that I use most frequently is
Claude Code on Cloud Desktop. It's
designed for people who want this full
screen graphical interface with built-in
previews, a sidebar control plane, and

[00:33]
the ability to render images and rich
outputs.
We've built desktop to be a single view
across all your local and cloud sessions
with visual indicators of which agents
are working and which ones need your
input.
Next is our newest surface, Claude
agents view in the CLI. For those of you
who want a control plane without having
to ever leave the terminal,
you can see what's waiting on you,
what's running, and what's already done.
You can reply in line to unblock or jump
in and out of any session without losing
your place.
The VS code IDE extension and the cloud
code on cloud desktop app are built on
the cloud agent SDK. The same one that
many of you are building on today.
Many enterprises have now adopted these
cloud code tools wallto-wall.

[00:34]
At Enthropic, engineers on average ship
8x more code than they did in past
years, even as the size of our
engineering team has grown
substantially.
Together with you all, we're excited to
discover and redefine what the future of
engineering looks like by embracing new
challenges that come and by building
automations powered by Quad to attack
each one. Here's some of the feedback
that we've heard from our users and the
products that we've built to address
each one with the help of folks in this
community.
We heard from you that you want to spend
less time on code review. So, we shipped
a code review product that deploys a
team of agents to catch critical bugs in
your PRs.
Thousands of companies use this every
day and this includes all internal
anthropic teams.

[00:35]
We heard from you that you really want
to code on the go. So, we launched
remote control and quad code on iOS and
Android.
Now, you're no longer walking around
with this laptop that's half open or
stuck at your desk. You can now go to a
park, touch grass, and still get your
coding tasks done.
We and we heard from you that you want
to run cloud code on new tickets and so
we built routines. You can configure
this once and it'll run on a schedule, a
web hook or an API call to kick off
cloud code on the right task. So the
work that used to require a human to
manually kick off, routines can take
care of for you.
and we heard from you that you're
landing so much code that your security
teams are having a hard time keeping up.
So, we built cloud security. It scans

[00:36]
your codebase overnight. It flags a
range of vulnerabilities, including the
ones that it believes are most critical,
and lets you kick off a cloud code
session to tackle each one.
And then finally, we heard that you want
better ways to run ambitious large-scale
tasks across your codebase like major
refactors and migrations.
So we launched dynamic workflows. This
lets you kick off cloud code to run in
parallel across tens or hundreds of
agents in a deterministic structure to
get your most ambitious tasks done.
Each of these primitives composed
together so that we can more easily
adapt to the future of engineering.
Everything I've covered is something
that an individual developer can pick up
today. But it's especially exciting to
see how a range of companies are
adopting this at the scale of entire
engineering orgs.
For instance, Spotify uses Quad to

[00:37]
migrate thousands of repos. The team
built a background agent on the quad
agent SDK that reads a migration plan in
plain English and then kicks off a fleet
of agents that opens PRs.
They're merging over a thousand PRs a
month into production and they've cut
migration time down by 90%.
Another example is Merkari, Japan's
consumer toconsumer marketplace. At
Merkari, the entire engineering team
runs on quad code and they've measured
that engineering output is up 90%
year-over-year using the tool.
We see this across the industry.
Millions of developers are getting more
done and at higher quality than before.
Now, let's see what this actually looks
like in practice. I'm excited to show
you one of my favorite new features in

[00:38]
Cloud Code.
For this demo, let's imagine we're
Kaizen operations and we create apps for
engineering teams. Right now, our
marketing website is in English only,
but we want to launch to 13 additional
markets. So, we need to localize our
site before the launch.
Let's start with how we would normally
do this with one quad code agent.
We'll run this prompt asking Quad to
convert our website to Japanese and
we'll speed things up as it works. Quad
explores a codebase, creates a language
picker for the website and translates
all the text to Japanese.
So quads finishes work and let's check
out the results.
Here we can see a full marketing site
and view the new Japanese translation
from Quad. It took Quad about three

[00:39]
minutes to complete this one
translation. And we have 12 more to go.
If we did this one at a time
sequentially, it would take us almost an
hour and lots of manual prompting with
Claude. So instead, we'll use a dynamic
workflow which will let Claude create a
repeatable process and run each of the
new translations at the same time in
parallel.
We'll prompt Quad to use a workflow for
our translation to these 12 new
languages.
Quad creates a workflow and once it's
ready, we can open it in the side pane
and watch as it works.
This is a powerful feature of the call
desktop app. You can see all 12
translation agents running at the same
time.
After the translation agents complete,
it's going to create 12 more agents to
verify its work across these new
languages.
This work would have previously required

[00:40]
us to run 12 separate tasks and it can
now be done in just one prompt. And we
can also save this workflow as
JavaScript code and reuse it for future
translations.
Let's check out the output.
Quad has now created 12 new versions of
the website, all localized with one
action. We can see them all in the drop
down and check out some of the different
languages to see its work.
This is just one example of dynamic
workflows. We can use them for
large-scale migrations, codebased
audits, or doing performance
optimizations.
Any large job that requires running many
agents at once in its terministic
structure.
Everything you just saw is available
today, including dynamic workflows and
cloud code in the Cloud Desktop app.
And our newest model, Quad Fable 5, is

[00:41]
available to all Quad Code users. So you
can use the latest intelligence wherever
you use Quad Code.
We're so excited for you to try out
these new features and for you to let us
know what you think. We hope they
continue to help you close the gap
between idea and a shift product.
And this is really what every talk today
was pointing at. Dian's capability
curve, Angelo's agents that run on
infrastructure that you control, and
what I just showed you. These are three
layers to one story. The remaining gap
is just how fast we can put these great
capabilities to work for us.
I encourage you to spend the rest of
today exploring these layers. Join
research talks if you want to learn more
about the latest model capabilities.
Join cloud platform sessions if you're
building your own agents for your end
users or join quad code workshops if you

[00:42]
want to learn more ways to bring quad
code into your day-to-day development
work.
All of this runs on Quad Fable 5, the
best model we've ever shipped for aentic
work and it's live today. Thank you all
and enjoy Code with Claude.
[applause]

</details>
