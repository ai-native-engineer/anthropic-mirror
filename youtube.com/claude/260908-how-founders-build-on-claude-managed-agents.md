---
title: "How founders build on Claude Managed Agents"
channel: claude
url: https://www.youtube.com/watch?v=hm8NzEd5io0
youtube_id: hm8NzEd5io0
published: 2026-09-08
duration: "34:42"
captions: en
---

# How founders build on Claude Managed Agents

[![How founders build on Claude Managed Agents](https://img.youtube.com/vi/hm8NzEd5io0/hqdefault.jpg)](https://www.youtube.com/watch?v=hm8NzEd5io0)

<details>
<summary>자막: How founders build on Claude Managed Agents (34:42)</summary>

[00:00]
All you guys are using
Managed Agents in different ways.
Maybe, Sahaj, I'd love to hear about how
you're using Managed Agents
in your new meeting product.
Absolutely.
For us, we think about meetings in terms
of the full journey of the meetings.
There's what happens before it,
during it, and after it.
Almost everybody confines their thinking
to literally just the period during it.
But the place where agents
become the most interesting
are thinking about how
do we help you prepare
for the conversation
that you're about to have?
How do you make sure
what you actually want to get done
happens in that conversation?
Then how do you execute on the things
that are supposed to happen after?
We've been using Managed Agents to build
and design a lot of new features
that we're building,
both on the briefs side
of getting you prepared,
and on the tasks and task automation side
of handling your work after for you.
Then, Mihir, how about yourself?
Our product is agents for sales teams,
and the core of the product is this idea
of an agent on every account
that's always working
and building memory and figuring out
what to do to progress it.

[00:01]
But there are
a lot of workloads for sales teams
that are not just restricted
to one account.
If I'm a sales rep, it's like,
what are the top five accounts
I should go after today?
Or if I'm a manager, it's like, what deals
should I forecast for the next quarter?
So on.
We wanted to build, we call it Watchtower.
We wanted to build this product
that's cross-account reporting
and aggregation and roll-ups.
That agent is fairly different
than the shape of our per-account agent.
It needs a bunch of different tools
and features and so on.
We spun that up in Managed
Agents in 2 weeks.
That is now one of our most used features
and also powers a lot
of other parts of the product.
Then Todd, rounding it out.
We have a product analytics solution
that integrates into applications
and captures what users
are actually doing in it
so you can feed back data
on how to make it better.
As people have moved faster
and faster, as we can imagine,
it gets harder and harder to instrument
those applications and understanding
where that analytics drifts
from what's going on.
We built a new agent
which sits in front of our platform.
What it does
is it integrates the codebase
and connects what the codebase is doing
to what's actually happening in reality.

[00:02]
We're using Managed Agents to actually
snapshot a version of the codebase,
compare it to what's actually happening
in the application,
start proactively sending insights
and even fixes to the application.
Nice.
I'd love to hear more about the details
and the features you're actually using.
We were talking a little bit earlier
about outcomes
being really important to you.
Tell me a little bit
about how you think about outcomes,
and why it's such
an important feature in Managed Agents.
Let's talk about briefs
as a feature for what we're doing.
Briefs are meant to surface to you
who is the person you're about to talk to?
Why are they relevant?
What did you agree to talk about?
What's important to get out
of the meeting, for example,
pre-context from what you might
have forgotten from weeks ago.
Briefs are awesome when they're correct.
If they actually tell you
who you're talking to correctly.
If you're talking to a person named Tom,
and it gives you information
about the wrong Tom,
it's actually almost destructive
because the moment you end up
in the meeting, you click to learn more
about them, and you end up confused.
Being able to correctly identify whether
the agent produced the right outcome

[00:03]
and literally choose not to show
the user anything at all,
if it didn't, is way better than giving
the user  false positive information.
Outcomes is super helpful because we
can literally just take the agent,
and have a complete independent assessor
of whether the agent actually produced
the right outcome
in that case in question,
and then make sure the attribution
of sources is actually correct.
This means that when we
show things to our users,
they're correct all the time.
It also helps drive feedback loops.
The more you can assess that on the fly,
the more you can
bake into the initial agent loop,
making sure it
gets it right from the get-go.
But it guarantees, essentially,
good product experience.
Maybe specify a little bit.
An outcome is basically
supplying a rubric to the agent
and allowing the agent
to iterate until the rubric is satisfied.
In this case, how do you
structure and set up the rubric?
For the rubric, we're looking
at all of the different things
that are important to the end user
to determine whether or not
the pre-read was effective.

[00:04]
This depends a lot on the type.
For example, there are aspects of it
where it's, did you literally just pull
the correct LinkedIn for the right person?
That's a very objectively verifiable thing
that you can actually assess against.
There are aspects where it is
about the way it's presented to the user.
That information ought
to be presented to you
in a way that's easily
scannable and readable.
The rubric will
also assess for things like that,
where you're actually
making sure it's consumable.
Otherwise, you get
a five-page pre-read before a meeting,
nobody is going to look at that.
Even if it's structured in the wrong order
of it doesn't first tell you
who the person is,
then why you're meeting them,
then what to do, even then it's hard.
We'll look at each of the things that,
from a UX perspective,
we want the user to experience,
turn that into part of the rubric,
and then hill climb against that rubric.
That makes a lot of sense.
One clarification, though,
is basically this is at runtime.
Basically, if I have a meeting, I guess,

[00:05]
say it's in an hour,
your agent might kick off
some period of time prior to that.
Spin up, create this, for example,
I guess it would be a brief,
and that is graded
against the outcomes iteratively
in some time period before the meeting.
-Is that right?
-Yeah.
But then how do you inject ground truth?
You said you can verify the LinkedIn,
but you have to go fetch that.
How are you actually doing verification
when external information is being met?
Absolutely.
We run these, for example,
24 hours before the conversation.
It gives you a pretty long time window
over which things can be assessed.
Cool.
In terms of verification here,
I think the interesting thing
is agents that do the work
and agents that evaluate the work
tend to just have decoupled assessments
of whether things are correct or not.
Even an agent that is doing
independent work can look at the LinkedIn
and can look at the email
and can look at the calendar invite,
and make its own judgment of,
was this probably correct or not?
Even I, when I show up to cold email,
cold meeting, I can look up the LinkedIn

[00:06]
and be like, "This does not
look like the right person.
I'm not sure why,
but it doesn't look right."
This is the value of having something
independent from the trace
doing the work, evaluating the work.
With Managed Agents, we actually
use an independent context window,
independent verifier agent,
and that's baked into outcomes.
That's the thing that's helpful about it.
Otherwise, it would just be
part of the agent loop itself.
That's good,
and it's going to be part of it.
But the fully independent
clean context window
means that you can assess the quality
of the work as part of deploying it.
For us, we actually just use it more
simply as we don't necessarily
have to iterate until it's perfect.
You can just choose not to tell people
something when you don't know
if your information is correct.
That's actually fine in our situation
when you're building something
that's proactively helpful.
Help when you can
and do not cause harm or annoyance.
That's really cool.
I want to ask you about memory.
We were talking earlier
about your Watchtower product
and how it's using memory.
I'm really interested in this topic.

[00:07]
Maybe tell me a little bit
about memory and dreaming,
and how you're thinking
about these things.
One of the things that's hard about this
problem is there are so many concepts
within a company that are
specific to that company.
For example, how a sales team defines
ownership or how they do their forecasting
or whatever,
how their deals work, et cetera.
That's especially hard because a lot
of the source data is pretty messy.
Everybody's Salesforce
has 30 different fields
that mean the same thing
that were deprecated, whatever.
The idea is if someone asks a question,
if I ask a question
about what are the deals
I should forecast for next quarter?
That's a pretty, A, an important
question to be able to answer correctly.
There's a lot that goes into that.
The way that we figure that out is, one,
as people interact with the product,
we learn those concepts
and then store them in org-wide memory.
That then enables us to give better
and better results for everyone else.
That's one of the things that saves us,
A, from having to go in,
and do a bunch of config at the beginning.
We don't have to do that,
but then the system can just very quickly

[00:08]
pick up those concepts
and get interaction.
We'll do some things
where when you first ask a question,
we'll ask user question and clarify
and then save those.
That's one thing.
Then the second thing that we do,
not just memory, but the second thing
we do that I think Managed Agents
has been pretty helpful
for is some of these queries
or use cases are pretty complicated
and require pretty deep work
across a bunch of accounts.
If I have 500 deals
and I want to do some deeper work,
I can do some basic filtering,
but maybe the system wants to go deeper.
It'll actually write code to be able
to answer the question,
and it can even do
programmatic tool calling.
It can go and narrow down a candidate set
and then fan out more work
to independent agents
that work on every single account,
and roll up feedback back.
It's both the concept of learning
all of these org-wide business logic
in a way that generalizes
across every team is different.
Then also being able
to write code to be able to handle
arbitrarily really complex queries

[00:09]
across relatively large sets
of accounts and things like that.
You were telling me earlier
about the setup of your product.
It's basically, I'm an account executive
and I have some number of accounts.
Let's say it's 100,
you spin up an agent for each account.
That's right.
Basically, a team of agents
that's servicing me
as an account executive or salesperson.
As I'm interacting, like you said,
you're learning memory.
You're learning things about maybe
my preferences or org-wide preferences.
But then this new product
is you have this memory
collected across this team of agents,
and it seems like it's doing "dreaming"
where it's looking across
all those memories and suggesting things.
Tell me about that specifically
and what it's doing.
There are two parts of the memory
that are interesting.
One is on each account,
there's an agent that runs forever
because it follows the account
throughout the entire life cycle.
It both builds context on the account
and then learns, picks up
these other concepts
that can get rolled up.
That's the first part of it.

[00:10]
The second part is even
while doing cross-account work,
you will learn
about these cross-account concepts.
How forecasting works,
or how other processes within an org work.
That's a second class of memory
that's less relevant
maybe on the individual account,
but it's more relevant within the context
of this Watchtower product.
We use both.
On every level, you can think about almost
this two-by-two where it's like
some things you learn,
you have memory on an account
and across accounts, you have memory
on a user level and an org level.
We learn all of those things
in different ways and then use them
to enhance all different
parts of the product.
I want to talk to you
a little bit more about that,
but I want to talk to Todd first.
Todd, we're talking about sandboxing,
and how are you using it?
This is a really cool
use case for sandboxing.
As I shared in the description
of what we're doing,
we're actually
snapshotting people's source code.
In general, that should be sandboxed.
As you can imagine,
if people are interacting with an agent
and you get access
to someone's source code,
you can potentially get secrets.

[00:11]
There's just a lot of interesting things.
Then you also have to be very thoughtful
about what tools are exposed
that's interacting
with that source code as well,
what data is sent to it?
Then what actions happening.
At the end,
often the result of an interaction
is essentially generating a pull request,
pushing it to the actual repository.
I think that was the piece where we'd
spend some time rolling our own,
but you're just covering
every single edge case,
and doing all that work,
it's not core to our value prop.
It just needs to work.
It needs to be safe and secure.
It needs to make sure, frankly,
everyone from small businesses
to large enterprises will trust it.
I think we're able to get there
pretty quickly with Managed Agents.
We also have a diversity of sessions.
We have overnight batch systems
which are looking for issues at night.
If you're trying to look at large-scale
funnel changes or other things,
you don't want to do that in real time.
You want to do that in a cron process.

[00:12]
Then we also have sessions
where if someone's asking a question,
we may want to quickly look
at the source code
to understand the source of truth
to then answer
the question more accurately.
All those are happening
in Managed Agents right now.
Cool.
Essentially, we have three different
examples of agents,
Managed Agents with sandboxing,
Managed Agents with outcomes,
Managed Agents with memory.
How do you think about the decision
to roll your own harness
versus use a managed solution
like Managed Agents?
I think all of it comes back to whether
that's part of the core competency
of the feature that you're building.
For example, when we're building new
features like briefs,
that's something where the harness itself
is not a core competency of that feature.
The thing that really matters is,
are we delivering the end user
the value that they need?
Whereas for other types of things,
for example, if we were thinking
about building
a fully voice-controlled Jarvis system,
there the harness itself might be
the core competency of what we build,
and it might allow us to deliver
completely new capabilities.
It's a question of basically
control versus cost and time.

[00:13]
It really comes back to if you don't need
to roll your own infrastructure for it
because it's not the thing that defines
the quality of what you're building,
choose to buy.
In the case where it is,
build it yourself.
Todd, you mentioned a similar point
about when you're in this regime
of rapid experimentation and exploration,
it's like speed
is where it really matters.
In the early days of any product,
you're trying to validate
product-market fit.
You're trying to validate certain core
features that make your product special.
All of us are solving some hard problem
and trying to solve it in a 10X better way
than traditional solutions.
You don't need to roll your own
infrastructure to solve those problems.
None of us in this roundtable,
we're not infrastructure folks.
There may be one day when the problem
we're solving necessitates building
our own infrastructure because we need
a little more fine-grained control,
maybe cost in a certain area,
we can't get to where we want it
from an operating perspective.
But in the early days,
you want to innovate.
You want to get features
in front of customers fast.

[00:14]
You want to be able to change
really, really quickly.
For that,
this is a perfect solution to make sure
that you're focusing
on the right things for your team.
It's not for everyone,
but I think if you're
in the startup phase, absolutely,
it's the right way of thinking
about and prioritizing your time.
You mentioned for you it was like 2 weeks
from experimentation with this
to shipping something.
Look, we had a solution,
obviously running.
That was our own
homegrown solution for a while,
but we started running
into issues with it.
We all know shipping something is easy.
Once you start seeing a set of issues,
we started to understand,
we have to rebuild this whole thing
because it's not where we want it.
Then we baked it off against,
let's just use Managed Agents.
It was so fast to get up and running,
and it covered a lot of the edge cases
that we were hoping to cover ourselves.
Just made a lot of sense.
Within a few days,
we had working infrastructure.
Within a few weeks, we had
the whole product rolled over to it.
-That's pretty compelling.
-How about for you?
What was the time frame
for you ramping up on Managed Agents

[00:15]
for the meeting assistant in particular?
It allows us to build a first version
of the feature in a day
and then ramp up with 100
to 1,000X scale-up in the user base
over the course of a few weeks within,
again, a couple more days
of iteration on that part of the system.
The primary thing that required work
was figuring out exactly
what a user wants out of the feature,
and that required a bunch
of cycles of build it, dogfood it,
test it with other people,
and then iterate that.
But even that could be done over
the course of 2 or 3 weeks.
During the iteration phase, what surfaces
did you find you're modifying a lot?
Was it the prompts, the skills, tools?
All those.
Then the orchestration
of the loop really is, for example,
when are you doing search,
then retrieval of different things,
then ranking of the relevant parts of it,
then what do you surface back to the user,
then how do you orchestrate
that across different sources?
That also process of what's the most
effective way to gather the information
that you need to drive that outcome

[00:16]
is in the example of the thing
that we would iterate on.
Makes sense.
How about you with Watchtower?
What was the time to ramping
that up and getting it deployed?
It was like 2 weeks from coming up
with the thing
to shipping it to customers.
Like dogfood somewhere,
maybe like a week in or something.
-Similar kind of-
-Yeah, superfast.
Within that regime of rapid iteration,
what are the levers that you feel
like you're tuning very, very frequently?
It's obviously things
like skills, prompts, tools.
What are the configurable surfaces
that you found to be most useful?
It's all of those without
having to worry about handling things
like compaction ourselves,
all of the other aspects
of building up the harness.
Because the question
that actually comes up is,
depending on the meeting you're entering,
what's the most important information
you present to the user?
If we don't have to worry about the rest
of it, we can literally just iterate
on that question,
which goes back to the outcome.
Does the outcomes feature allow us
to guarantee that for this conversation,

[00:17]
we've assessed the most important
information and structured it that way,
and then rapidly iterate towards it?
I think I remember reading something
about Claude Code in the early days
where in the very early days,
Claude Code didn't have evals.
-You can iterate your way to-
-Vibes-based.
You can iterate your way to getting
a thing to be sticky, vibes-based.
Then the moment it's sticky,
then you have to have evals.
You'll be really sad as a person
if you don't have evals
in a systematic way to iterate towards it.
Can you figure…
If the thing is not sticky,
no amount of evaluation
is going to make the thing sticky.
You got to figure out
how to make it sticky first.
It's a good clarification.
In this regime,
where your very rapid iteration
using a managed harness is quite nice
because it's giving you
managed infrastructure.
It's things like prompt
caching are just solved.
-Exactly.
-Although it's very important for cost.
-For sure.
-Tell me about how this plays into memory.
Memory is one
that I've actually thought about a lot,
and I've worked on quite a bit.
It can be quite tricky to get right.
For Watchtower,
you're using memory in Managed Agents.
Tell me about how you're using it,
and how you've configured it.

[00:18]
What are the configurable surfaces
from memory that you think are important?
Maybe walk me through that a little bit.
There are parts
of memory that are very core,
and we need a lot of customization over.
That's the memory on every account.
There are a lot of levers we need
to pull there to make that really stable.
It lasts forever.
It's pretty detailed on every account.
It can get corrupted over time.
There are a lot of things that we do
that we manage ourselves,
because we have to index it in certain
ways to make it efficiently queryable.
We do a lot of work on that to make
sure that that's really good.
But then there's all this other memory
on what your different fields mean,
and how your org works,
and user preferences
and all these sorts
of things that are less core.
It's like they need to work,
and they need to be good,
but they don't need to work
any differently for us
than they need to work for other people.
For us, the managed memory
just unblocks a lot of that.

[00:19]
Similarly, part of it
is just being able to iterate
and get this to be
a valuable product for people.
But even longer term,
I think it's like for us,
a large part of how we view our job is
to make tokens useful for salespeople.
In our view, a lot of that just comes
from the actual product,
and the product experience
and the surface that you build
around it and so on.
It also lets us both
get it off the ground.
We built this thing in 2 weeks,
and so it lets us get it off the ground
pretty quickly and make it good.
But then also,
longer term, we haven't rebuilt it
or felt the need to go
off of Managed Agents.
It's been a few months
because we're just focusing.
There's so much on top of product surface
that we can build that's valuable.
That, I think, just creates
a lot more value for customers.
That's how we think about it.
Just to clarify slightly.
Every agent has memory,
and that's what you internalize.
These agents are built,
they're not in Claude Managed Agents.
Correct.
They have a memory architecture that you
own that's completely independent.

[00:20]
Then the managed agent,
this Watchtower product,
basically can access that memory
that you've built
across this fleet of agents.
Say I'm one account executive,
I have N agents, one for each account.
The Watchtower can access the memory
across that whole fleet
and then do what specifically?
If I ask a question, if I go to Watchtower
and ask a question,
"What are the five accounts
I need to work on today?"
That's a function of a couple
of different things.
A, there's like, obviously,
it's a function of the account.
If you own 100 accounts,
then it's some function
of those accounts' memory,
but it's also a function
of a lot of preferences that you have
and a lot of knowledge
about how your organization works.
Meaning how you prioritize,
what accounts you go after, and so on.
There's the account-level memory
is one of the inputs,
and this managed agent
will actually write code
to be able to query those
and can even do fan-out,
and all these different things on top.
But then it's also a function.
The other half of this is a function
of you and your company
and how you work and so on.

[00:21]
That's all in this managed memory.
That makes a lot of sense to me now.
The Watchtower product
is like an account executive-facing,
and that's the interface
that they might use
to access all these different
individual account agents
with their own memory.
Exactly. You can do work.
Obviously, there are parts of the product
where you can just say,
"I'm going deep on this one account,
and I want to just do work
on that one account."
But there are a lot of other things
that require going across accounts
or prioritizing them and so on.
Both for individual users as well as it's
been a big thing for us to expand beyond
ICs to leaders as well.
Where a sales leader,
if they manage five different AEs,
now manages 500 accounts,
and they're responsible
for those and works up the chain.
This product has been useful
for building useful stuff for them.
Then Todd, with sandboxing,
I wonder how you think about that?
It sounds like basically
the analytics product has access
to not only the application
and all the telemetry
coming off the application,
but also the actual source.
Correct.
The customer is actually giving you
that access, which is pretty interesting.

[00:22]
You're taking that code,
and you're sandboxing it,
and then you're interrogating it jointly
with telemetry off the application
to do what then?
Tell me about that. How do you make-
There's a variety of use cases
that we're using it for.
I think one of the key things
around Managed Agents,
which you heard just earlier,
was the speed and time
to market was pretty compelling.
I think under 2 weeks, we actually
had a solution leveraging Managed Agents,
where we were working on ourselves.
We had a few teams working on it,
but the speed
in which we can just check that box
for this infrastructure
is handled, this is done, it works.
Of course, there's some
iteration and some tweaking,
and some tuning that we had to do
to get it within our operational controls.
But generally speaking,
it was a positive surprise.
But from there,
there's just a number of use cases
that can spin up.
For example, we are integrated
into a source code repository.
Every time there is a change
to the source code,
pull request submitted,
we're firing off a managed agent session
to review the code,
understand what's changed.

[00:23]
We're actually
applying a lightweight UX review
to make sure we're preventing,
honestly, bad UX from being
committed in the first place.
But then once something's merged,
we're looking at, what happened now?
This is merged.
We need to go potentially
update analytics.
Maybe we need to create
instrumentation for them.
We'll fire off our own pull request on top
of the ones they just submitted
so they can have accurate instrumentation.
At night, we have processes which are
looking at what happened the previous day.
Did a funnel drop
in conversion rate overnight
or even across the 30-day period,
do we see a slight
degradation week over week?
In which case, we're going to look
at what changed 4 weeks earlier,
and how do we start suggesting
a fix for it.
We're also assessing things
like agentic conversations.
We're looking at how are
if humans are interacting with agents,
how is this conversation going?
Are there higher error rates than usual?
We may suggest a prompt fix
based on what we're seeing.
I think the goal is, how do we ultimately
get to a self-healing piece of software?

[00:24]
Where, as people go fast,
as people check in more and more changes,
we're seeing what actual users
are doing beyond just our eval sets,
you have to have those as well,
but what actual users are doing
or how it's actually operating,
how do we understand
and then suggest fixes
and allow you to continue
going as fast as you want to go?
You actually made an interesting
point about evals.
I'm curious to hear how do
you think about evaluations.
You referenced this earlier.
Maybe in the very early stages,
like vibe-based and ensuring
you have product-market fit
can be quite important.
I've seen this myself.
You can have
a very carefully curated eval set
that is not
on distribution for your users.
You will hill climb on it,
and then it doesn't matter.
Your users don't care.
How do you think about this,
evals in general?
Phase zero is vibes-based.
Once you have a thing that feels
sufficiently good that you like it,
then that's when you're trying
to hill climb to make it really great
in the whole distribution of cases.
It's really easy to start internally
and gather feedback internally
on a lot of different data points
for what's good and bad.

[00:25]
That runs the risk, though, of overfitting
to your own users at your own company.
From there, it's just a matter
of gathering data points
and feedback from people externally.
You got a thumbs up, thumbs down
on the outcome of the feature.
With enough users,
you're going to get enough examples
that curate a pretty
decent eval set pretty quickly.
That allows you
to think about building evals
for just different types of scenarios.
There's going to be a cohort
of evals for regressions.
There's going to be a cohort of evals
for hard, challenging scenarios
and different
kinds of partitions of your data.
There's going to be cohorts of evals
depending on the type of task
being assigned to the agent.
Then there's going to be the rubrics
that you assign to each of these things.
As much as you can sync up your rubrics
for your offline evals and outcomes
is also ideal for these kinds of things.
That's overall how I think about evals.
Do you have any particular
thoughts on evals?
Or I actually have a different
question I want to ask.
There are two things for evals.
One is we struggled for a while to come
up with good evals because of the thing.

[00:26]
We would dogfood.
Obviously, we're vibe-based.
Our sales team dogfoods the product.
That was good.
But it's just not representative,
like what you said, of actual customers.
One thing that we did
that has been helpful
is actually looking
at real customer queries
and talking to the user,
that person, and understanding
why did you run this,
and what were you looking for,
and what did you want,
and then building evals around those.
We can do it, obviously,
within that customer's data and so on.
That's been really helpful
to avoid the abstraction risk.
Because what we were finding
was our evals were just too abstracted
and not representative.
That's one thing.
I don't think we found
a good way to eval given memory,
a system that's very stateful
with this memory that is live.
Obviously, you can do trajectory evals
on how well does it
interact with the memory.
But doing these offline result evals
given this external state has been…
I don't think we've
fully figured that out.

[00:27]
Same for us on MCPs with tool calls
to third-party services
with mutating state over time.
If these evals are going to rely
on Slack MCP to produce information,
it's really hard to get
a good systematic suite of it
that doesn't just drift over time
because of things
that are outside of our control.
Unless you mock the whole thing,
which is just a lot.
Mocking a customer's Slack
I'm not getting in that territory.
That's not too tractable.
How do you think about model migrations?
Opus drops, what do you do?
How do you think
about updating your prompts
if you think that's necessary?
How do you think about testing new models?
Are there things that you think
that could be better communicated,
maybe from us
in terms of how to use models?
We have prompting best practices.
I think it's mostly that.
If you have a good eval suite,
then you do the model migration.
Hopefully, the way
that you've done your prompting
has not done historically
too much hyper-optimization
to a specific model family.
What I've found, though,
is a lot of new models at different points

[00:28]
have different gotcha scenarios
where they do bad things
in different ways.
The whole five series of models
tends to produce writing
in a way that has actually
a lot more AI telltale signs
than previous series of models.
More em dashes.
More of all of that,
the sentence structures
that are just like
unreadable sentence structures.
If there are things
where there are known failure modes
of the new category of models
that you're trying to hedge against
versus trying to optimize your prompts
to get the last 1%
out of the model family.
I don't care
that much about the latter thing
because that'll keep
improving with each generation.
But if a new model introduces
new failure modes
that are specific to it
that you have to avoid,
that's probably the most valuable to us.
A few of you were mentioning this point
about cost and attribution
as being one of the major challenges
and pain points broadly
when building agents.
Tell me about that.
I think nobody working
on agents right now

[00:29]
is not worried about cost to some degree.
If you're fully not worried about cost,
you're probably not going to build a thing
that scales long-term in terms
of a sustainable business structure.
I think one of the questions
that often comes up for us internally
of how long do we rely
on Claude Managed Agents
is when does the cost trade-off
versus value trade-off of control
for doing things in-house
mean that we should do things in-house?
I think on the surface,
the markup of Managed Agents is pretty low
in terms of the amount of CPU overhead
that you're paying
for running the infrastructure.
For example, you can't run batch mode
that easily today with it.
If we're running things 24 hours
in advance, we could probably save
50%-75% on cost and make that possible.
Today, for us,
it still comes back to that question
of if we have a lot more value,
we know we can create for our users
in the short to medium term.
Cost optimization
is something where it's be mature,
be mindful, and spend well,
and then come back to actually
optimizing all of the details over time.

[00:30]
Hopefully by that point,
you will have built features for us to do
all those things directly
within Managed Agents.
I think both you, and you had
mentioned previously to me
that it's also a point about attribution.
Where specifically in agent harness
are you accumulating cost?
Is that something
that you guys think about?
You're looking at this combination
of cost and flexibility and control.
You're ceding control.
Managed Agents,
we're using infrastructure like this.
Over time, of course, your roadmap will
give us more control in certain key areas.
But right now, it's obviously, I think,
the best solution for us to go forward.
Getting really fine-grained
telemetry of what calls cost what.
When you have something,
we have large batch processes
that happen in the evening,
which process lots of data.
It gets expensive,
or it can get expensive.
We can do some
really inexpensive things right now
in terms of engineering time
to just cut this,
do it less frequently, send less data.

[00:31]
We can do things like that just
because we don't have to over-optimize.
But when you get
to a certain level of scale and maturity,
you're going to want to have
a little more control over that.
Hopefully, we'll have that ability
when we get to that point.
We'll see.
What do you think?
What can we do better, generally?
Anthropic, it could be Claude broadly,
or also Managed Agents.
Maybe there are a couple of things.
I think one is cost,
and then two is for us,
ways to improve the user experience.
On the cost side,
I think it makes total sense for us today
on parts of the product
that need truly frontier intelligence.
If we're running Opus or whatever,
then it's just a really good model,
and I think it's relatively well priced.
But there are other parts of the product
that don't need as much intelligence,
or we just can't do
that because we run over such a high end.
For example, even this Watchtower thing,
the agent that coordinates
the search or the main agent
needs frontier intelligence.
But if you're fanning out
across 500 different accounts,

[00:32]
you can't do the same thing there.
That is a place that we've
had to cost-optimize.
We'll use much cheaper models
and so on to do that.
That's one side.
I think the inherent structure
of the product makes it hard,
of Claude Managed Agents
makes it hard to get…
When you have to do the cost optimization,
it's very constraining
because it's all or nothing in some sense.
That's one side.
There aren't that many levers for cost.
Yeah, I see. That's good.
Better surfacing of levers for cost.
We have things like effort,
we have multi-agent,
we have obviously many models.
Some flex or batch mode would help.
That's a 2X, 50% right there.
Things like that would
help a lot on one side.
I do think there's a class of things,
and I don't know
how important these are yet,
but there are other things we want to do
to improve the user experience for people.
For example, in latency-sensitive parts
of the product,
we want to pre-warm sandboxes in different
clever ways to reduce cold start latency.

[00:33]
Those are things also just the nature
of the managed agent product.
The way we think it works really well now
is when you need frontier intelligence,
you're relatively price insensitive,
and the task is hard,
so it runs for minutes or something,
and then you don't really care
about seconds here or there.
For those things, it works very well
and totally makes sense.
It just lets us get
those out really quickly.
But for anything else, there are
not that many levers to improve UX
or make it cheaper, things like that.
Cool.
Anything on your side?
I think that's the bulk of it.
It comes back to if optimizing cost
or optimizing control
allows you to build a thing
that you otherwise can't,
then it makes a ton of sense.
If you can't build a certain feature
without reducing the cost by 90%,
then you got to figure
out a way how to do that.
If we're building our Jarvis
voice-controlled chief of staff over time,
odds we're going to probably have to roll
our own harness
for that thing seem quite high.

[00:34]
But that doesn't mean
that we roll it for everything.
The same way
that you have parts of your harness,
and I'm sure you have parts of your system
that you build entirely yourself,
and you have parts of your system
that you rely on other things.
I like your three criteria.
I think our fourth criteria
is when you're validating viability,
where, again, the cost of an experiment
is in the time it takes to learn.
That's the only other case
in which I think it really shines
in addition to the ones
that Mihir mentioned.
Thank you all for being here.
Really enjoyed the conversation.
-Likewise.
-Thank you.

</details>
