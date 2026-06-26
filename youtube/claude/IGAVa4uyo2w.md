---
title: "How Emergent is making app building more accessible with Claude"
channel: claude
url: https://www.youtube.com/watch?v=IGAVa4uyo2w
youtube_id: IGAVa4uyo2w
published: 2026-05-13
duration: "16:39"
---

# How Emergent is making app building more accessible with Claude

[![How Emergent is making app building more accessible with Claude](https://img.youtube.com/vi/IGAVa4uyo2w/hqdefault.jpg)](https://www.youtube.com/watch?v=IGAVa4uyo2w)

<details>
<summary>자막: How Emergent is making app building more accessible with Claude (16:39)</summary>

[00:00]
We are building for small
businesses today.
Small businesses globally account
for 70% of employment,
accounts for 50% of GDP of the world.
But they've never had the tools
to really express themselves
because there are a million niches
in small businesses.
But for the first time with AI,
you can actually serve
all of these million niches
at zero marginal cost.
And that's what we are trying to enable.
Hi, my name is Carly,
and I'm on the Applied AI team
here at Anthropic,
specifically working with startups.
Today, Mukund has joined me.
He is the CEO and co founder of Emergent.
So Mukund, let's bring it back
to the beginning.
Emergent's growth has been
one of the standout stories of this year.
Why don't you walk me through your journey
with YC, some of your pivots,
and how you landed on the product
that you have today.
Thank you for having me here.
Super excited to be here.
So I'm doing this startup
with my twin brother.
Madhav and I actually started programming
at age 12, and we have then—
Love it.
We love sibling founders here.
Totally, and we actually
have been obsessed
with this problem of automating
software engineering from the beginning.
Before this, I was running
a startup called Dunzo,
where I had a 500-people engineering team.

[00:01]
When we entered YC, our first insight
was to automate software testing,
because I had seen at Dunzo
that how testing was the bottleneck
for shipping software fast.
We started with this problem
of how do we automate
all of the software testing,
including mobile apps, web apps.
When we started building that out,
we realized that to automate testing,
we had to build our own
container technology,
our own coding agents.
We stumbled upon this insight that
if you can actually solve
for the verification loop,
you can actually make agents run longer.
On the day one, we told our YC partners
that testing is great,
but we want to now build
general coding agents.
We were almost
like an applied research lab working,
just building high production grade
quality agents.
Invented a bunch of things
like test time compute.
How do we solve scale,
the memory across agents?
How do we solve
our agent-to-agent communication?
We were one of the first team
to productionize multi-agent systems.
When we launched, our first approach
was to go to enterprise.
We had an enterprise customer,
started working with them,
but realized the adoption
of the enterprise is going to be slow.

[00:02]
At the same time, we started using
these internal coding agents
to build everything internally.
In fact, there were few non-technical
people on the team who were using it
more than developers were at that point.
We truly realized that the power
is actually to democratize
software engineering for everyone.
That's when we, in June, launched
this almost like a research preview.
At that time, agentic
coding was not that popular.
When we launched, it just took off,
and we were actually surprised.
Everybody else at that time was building
for front-end heavy applications.
They were building for more demo kind of things.
We had fundamentally approached
the problem thinking that,
what would it take for actually anybody
to ship production-ready software
that will actually have real use cases,
will have business-critical apps running?
Our insight was to automate all of this
testing, linting, deployment, security.
How do you solve for code reviews?
That actually really resonated
with users because most of the users
that were coming to Emergent today
are serious builders.
These are small businesses,
entrepreneurs who actually want to see
an economic value
from the software getting built.

[00:03]
Yeah, that's awesome.
So it's basically democratizing.
It's taking natural language.
It's for non-software engineers,
but it's also building durable products.
It's not just for prototyping.
It's really cool.
So you've been building on Claude
since the really early days.
We met about a year ago.
What made that the default choice,
and what's kept that all the way through?
Why have you stayed on Claude?
I think we were almost lucky
to get started when Sonnet came out.
I think in AI, I think everybody needs
to imagine the world six months ahead
and build for that versus building
for what's available today.
Imagine the world from the lens of what is
available and what's going to come next.
So people who would have started
with the previous generation of models
would be solving a different problem
versus us because for the first time,
I think Sonnet had really good
instruction following
so that you could actually really imagine
what long-running agents would look like.
It was really good at programming.
It was really good at front-end as well.
That actually really gave us a little bit
of futuristic view of what the world
of programming could look like and what
could agentic programming look like.

[00:04]
Our users are actually
comparing us against a dev shop.
They're not comparing us
against an IDE or a tool.
To them, outcome matters a lot.
We really focused
on what would give us the highest quality,
what would give us
the highest probability
of getting to the right outcome,
versus a speed.
Most of the other players who are focused
on front-end or design,
to them, speed matters a lot.
But for us and our users,
what is important is that
are they able to reach
the outcome that they want?
And that's why Opus
has been our work horse,
and it's really great
at instruction following.
And if you have the right tight
feedback loops
that we have been able to build
using our multi-agent systems,
you can actually keep them running
for a much longer time.
Today, our agents can run for hours
trying to build the software.
And we run very tight evals internally.
And of course, you've been really helpful
in helping us get them.
I know about your evals for sure.
I remember when we were about to launch,
we had this 2:00 AM meeting
just to get started on things.
Totally. Well, I mean, a lot
of your engineers are in India.
So one day when I was like...
It was Friday at 2:00 PM for us,
and it was the middle the night
for you guys.

[00:05]
I was like, "Of course,
they're going to answer the next day."
Then one of your engineer was like,
"Yeah, let's get on a call in 15."
I was like, "Is it not
the middle of the night?"
Your team during YC built
this internal coding agent.
Maybe you didn't know
what it would become.
What did you learn from that?
What shows up today in the product?
And then maybe what are learnings
that you really scrapped?
Yeah, I think our first insight
was to really build
an automated
software engineering platform.
You will have to own
every layer of the stack.
You have to almost co-build
the infrastructure to support your agent
and agent to support the infrastructure.
At that time, everybody
took this shortcut.
Hey, what is the third
party that is available?
Let's use that.
When we started, there were no
good container technologies.
We had to actually really invent and build
our own container technology on top
of Kubernetes, which does
the snapshotting, memory snapshotting,
so you could actually save the states
and run parallel agents.
For us, what's been
really insightful
has been that agent is the product
in many ways,
and the harness quality
really matters.
We build this multi-agent system.

[00:06]
We're one of the first teams
to productionize it.
Many learnings, including
how do you solve save for memory,
how do you do
agent-to-agent communication,
how do you do better
context management,
how do you effectively use caching
to keep the cost down,
and tightening all the feedback loops
from the container.
And all of the infrastructure
that you've built is really important.
The other thing that really was important
to us from day one
was to own the entire stack,
because the last mile
is where most solutions trip.
We spend a lot of time just to make sure
that our production quality
is really high.
What you can see
in the development environment
is something that replicates
in the production.
Today, I think we're probably one
of the deepest logs in app building space,
and that allows us
to compound our learning.
For example, a lot of the errors
actually don't show up in the dev side.
They'll only show when your app
is live and real users are using it.
We're able to pipe all of that back
to our development environment
and allow our agents to learn.
We also have built this,
what we internally call long-term memory,
where an agent is not just learning
from within the user session,
but is learning across all of the apps
that are getting built.
So first time it sees an error,
a new error, or a new library upgrade,
it's going to learn that and do that
in the next iteration

[00:07]
in much fewer tokens
with much more accuracy.
I think building this co-agent
and such together
has been really helpful for us.
I guess because you own the whole stack,
up to the hosting as well,
that gives you all this proprietary data
that you can feed into the next parts
of the agent and the future of the agent.
How do you think about model selection,
especially when your users
can't debug the output?
I mean, a lot of the burden lies on us
today, to make our users successful,
and we take that very seriously.
That's what we are
extremely obsessed about.
How do we get users to success?
A couple of months back,
our deployment rates were 84%,
now it's closer to 98%.
So 98% opeople on the platform
were able to build something,
are able to deploy to productions.
That's been amazing.
And that's just tightening
all of these feedback loops,
making sure that your agents
are extremely reliable and self-learning.
In terms of the model,
the way we think about it,
we are getting compared to a dev shop.
So when a user comes to us,
they're comparing us
to a $250,000 price point
that they would have paid
if they had gone and hired a dev shop.

[00:08]
They're not price sensitive.
They're also not latency sensitive
that much because they're comparing us
to a three months project
that would have been executed outside.
We are very, very obsessed
on the quality of the product
and not so much about the cost as much.
For us, being on the frontier,
the highest reasoning possible
is something that we index a lot on.
Internally, we index a lot on just highest
quality output versus the fastest output.
We are not trying to do one-shot solution.
We're trying to build
really reliable production system
that can be added to the point.
Instruction following
should be really good
because the error compounds
and even small errors
as you run 10,000 steps,
they compound very quickly.
Because the outcome matters the most,
we rely on the best possible models
for reasoning and coding abilities.
I think that's been a through line
that I've observed with you guys
where it's like
you really put accuracy top,
and that's why you've had so much success.
This is a question we ask
our founders often.
The AI builder space
has gotten a bit crowded.
Curious to hear from you,
what has Emergent built
that's genuinely hard to replicate?

[00:09]
Yeah, I think first of all,
I think we're at the beginning
of a very, very large market
that's opening up.
I think the market is actually growing
faster than all of us can serve right now.
The pie is getting bigger.
Way bigger, way faster
than all of us can serve right now.
We are actually not so much worried about
what is competition doing?
What are labs doing?
We just generally think that the market is
so big, and it's going so fast that us
being able to serve the customer
that we want to serve
is generally not really important.
For us on the technical side,
I think our approach has always been
to really build very closely
with the customers.
We understand our customer
really well.
We know what their needs are.
For example, they really don't care
about demos, front-end prototypes.
They care about real production use cases.
They care about third-party
integrations working.
They care about payments getting through.
They care about authentication working.
A lot of our users early on
started uploading really large files.
We had to think about
how do we support
large file systems
on our production systems?
They care about scalability.
When we write code,
we make sure that these codes are written
in a horizontally scalable manner.
As traffic grows,
the infrastructure grows with them.

[00:10]
For us, I think the technical mode is one,
our agent quality.
The harness quality is really strong,
and it's continuously evolving.
Second is all of the provided data
that we are collecting right now.
I think all of that feeds
into our long-term memory
feeds into our self-learning agents
feeds into our RL systems.
Because we are solving only for one stack,
we are almost like a vertical agent
for coding because our users
don't really care
about what technical choices
are being made.
They leave that onus on us,
and we make the right choice for them,
and we are solving
for just one kind of tech stack.
That allows us to really accelerate
our learnings on that tech stack.
Lastly, I think the code generation
is only 20% of the problem.
The 80% of the problem is actually
how do you take it to the deployment?
How do you make sure it's
maintained in production?
How do you make sure that security
is really high?
We are solving for all of those deep
infrastructure problem where not only your
code is written, but does it work in the
dev environment when it works in dev?
Does it replicate in the production?
Do you have the feedback loop?
And solving for the full stack
is really important for us.
Yeah, really cool.
I think one of the early differentiators
I saw from you guys is that third point,

[00:11]
building durable, reliable apps
that can be built on later.
It's for actual business owners and not
necessarily just people prototyping.
I remember in one of our early calls,
you were talking about you have your agent
that initially builds the prototype
or the product, but then you later have
another agent that comes back
and cleans up the code
and makes it such that people
can build on it later.
We take code quality very seriously.
We have refactoring agent that will come
and refactor your app.
We have a post-deployment agent
and a pre-deployment agent.
They'll check for all security flaws.
They'll make sure that there are no
key leakages, a bunch of those things.
Approaching the problem
from the outcome first perspective
allows us to really design
the system for that.
What do you think are most defensible?
What are you seeing, you guys?
Yeah, this has always
been true for startups.
It's deeply understanding your users
and deeply building a product
that you can iterate on quickly
that really captures
your users' needs and problems.
Then related to that is building a brand
and a go-to-market strategy

[00:12]
and a user experience around those people
that you understand so well.
The second thing is moats
that intelligence alone can't overcome.
That's proprietary data or infrastructure,
building in a highly regulated space
That's something that AI is not going to
automate compliance regulation fully soon.
The final one is human trust.
This is also in regulated spaces,
but anywhere,
human trust is not something
that's going to be automated soon.
So these motes that model intelligence
can't bridge that gap yet.
Then the final thing,
which I see you guys doing,
it's the most exciting for me
to see a customer do,
is build a beautiful product right now,
but then also build a product
that's looking towards the future.
We are seeing models consistently
get better at longer horizon tasks,
more autonomous tasks.
A year and a half ago,
someone probably didn't think
Emergent's product could exist.
Text to app builder,
truly democratizing software,
and then continuing to push that forward
of, okay, today we know a product
like Emergent that can exist.

[00:13]
What's the next thing ahead
of the frontier for the models?
I mean, internally,
we have actually rewritten our systems
four times over nine months.
We almost feel that
with every new model launch,
we have to delete everything
that we have learned so far
and re-imagine the world.
I work with you on it.
For example, Opus really feels like
a different class of model
and much more capable
of longer horizon tasks,
especially now we can have multiple agents
coordinating on the same task.
My belief has always been that, okay,
every time a new class model shows up,
let's delete everything we have done.
Let's re-imagine the world
from this lens of the new model.
I think that's been really helpful.
I'm curious to transition into your users.
We've talked about how most
of them have never written code.
Who are these people,
and what are they building?
I'd love to hear some user stories, too.
When we started, we thought that we were
building for mostly semi-technical users.
It's going to be mostly program managers,
product managers, designers
who are going to use us initially.
But we were surprised to see
when we launched that a lot of our users
were actually business operators who were
using us to build serious applications.

[00:14]
Essentially,
we're actually built for domain experts,
people who really understand their domain
really well but never had the tools
to express themselves,
can now just come in and describe
the problem in-depth, and agents will
go and build the application for them.
The gap between communication
has been reduced.
And build out and have
the site feedback loop
to iterate on the software themselves.
And we have users across the globe,
190 countries, almost seven million users.
My favorite example
is this user, Christie.
She's in Alaska,
and she is a clinical psychologist
and also an equestrian coach.
She had been waiting for 10 years
to marry these two fields.
She had gone to a dev shop in Nova Scotia
and got a quota for $1,000
to build this app and tried it with them,
but it didn't work out.
Discovered Emergent,
started building on it,
has her app live on the App Store today.
It's called EquiMind.
For the first time, she was able to marry
these two fields of psychology
and her sports coaching has hundreds
of users using right now.
She was telling me, "I've been waiting
for 10 years for this opportunity
to really build something."
We're building for small businesses today.

[00:15]
Small businesses globally account
for 70% of employment,
accounts for 50% of GDP of the world.
But they've never had the tools
to really express themselves
because there are a million niches
in small businesses.
Traditionally, when you had SaaS,
well, they were forced to move up market
for economic reason.
But for the first time with AI, actually,
you can actually serve all of these
million niches at zero marginal cost.
That's what we're trying to enable,
really empower these small businesses
to accelerate their businesses.
What do you think Emergent
looks like a year from now?
What are you most excited to build next?
Yeah, I think a year is a long time.
Yeah, in this world, definitely.
I think all of us have seen
that meter chart
where the long horizon agents
are going to be.
For us, the market segment
is really clear.
We want to serve these small,
medium businesses.
We want to serve new entrepreneurs.
We are very focused
on making them successful.
We're coming out with a new agent,
which we think is infinitely better
than existing ones.
One of the other things
that we are really excited about
is with especially long horizon agents
coming online,
we especially think that there's a way
for us to automate all of the businesses,

[00:16]
operations for small businesses.
We want to move from software to actually
automating their entire business
and allow for these autonomous businesses
to happen on the platform.
We are very soon launching a new product.
We're very excited about it.
It's called Wingman.
It's agents for businesses,
and it's going to automate
all of your business processes,
including finances,
including operations, sales, marketing.
2026 is going to be a year where people
start automating large part
of their businesses,
and Emergent wants to be the platform
for businesses to come and automate
all of their businesses on top of us.
Well, thank you
for being here today, Mukund.
-It's been such a pleasure having you.
-Thanks for having me.
It's been a great chat.
Thank you so much.

</details>
