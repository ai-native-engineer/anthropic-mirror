<!-- source: https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

# Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

* Category

  [Agents](https://claude.com/blog/category/agents)

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)

  [Product announcements](https://claude.com/blog/category/announcements)

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  [Claude Tag](https://claude.com/product/tag)
* Date

  August 13, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
* Author(s)

  Clement Peng

  Lily Zhao

In our [previous post](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude), we described how we enabled Claude to answer data analytics questions with ~95% accuracy through three primary artifacts:

* A governed semantic layer;
* A set of skill files that encode our analytical conventions; and
* An evaluation suite to measure performance.

That post focused on [Claude Code](https://claude.com/product/claude-code) (the primary development surface for our data scientists and data engineers), and best practices for improving agentic accuracy.

This post discusses how the data team at Anthropic applies that foundation to where the rest of the company works using [Claude Tag](https://claude.com/product/tag)(public beta), which is the foundation for our data analytics agent in Slack. Anyone can ask it data-related questions and receive answers backed by **the same governed definitions analysts use**.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7e018507d3cd146d296978_11388c5c.png)

Fictional recreation of a Claude Tag conversation for illustrative purposes. Details, names, and tools are not real.

## Best practices for deploying a data analytics agent in Slack

Getting an agent to be *accurate* and getting it *deployed where non-analysts can use it* turned out to be quite different motions. We won’t rehash our recommendations on accuracy from our prior post as they’re still applicable here.

Rather, we’ll cover our five most important learnings over the past year for how to deploy a data analytics agent in Slack and how you should think about distribution, permissions, freshness, and observability.

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

### Refresh skills as often as you refresh your data models

You can teach Claude how to do a task aligned with your style and requirements using a [skill](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more), which is a markdown file with natural language instructions and files Claude can reference when needed.

The single most important architectural decision we made was to treat skill files as **served content**, refreshed continuously, rather than something shipped once and forgotten.

Data models can change several times a day. For example, a column gets renamed, a metric definition is corrected, or a table is deprecated. Every one of those changes needs to land in a skill file in relatively short order. If Claude is reading last Tuesday's copy of the skill, it gives last Tuesday's wrong answer with full confidence.

This tendency can be especially damaging since the data consumer is now completely separated from the context they need to judge the accuracy of the response. They aren’t looking at a dashboard with trend lines or associated metrics that can guide their “sniff test.” They may receive just a single data point or two in Slack, and if it's not data they look at regularly, they are likely to accept that confidently wrong answer.

To control this ever-changing environment, Claude Tag's runtime mounts our data repo's skills/ directory and **re-reads it on every conversation**. The skill files are just markdown on disk; the agent reads them the same way it would read any project file.

### Give the agent skills beyond knowing what to query

Our initial instinct for deploying our data analytics agent using Claude Tag was to create a “knowledge skill,” which teaches Claude which tables to use and how our semantic layer is organized, and call it a day. We quickly determined that approach would provide *correct* *numbers*, but stop short of *useful* *insights*.

Most data consumers tend to ask open-ended and ambiguous questions like "what's driving this dip?" or "can you forecast where this lands at month-end?" or "show me this data as a funnel." Answering those requires the agent to know not just *where the data is* but *how an analyst would work with it*.

So alongside this knowledge skill, we mounted Claude Tag with additional analytics or runbook skills, including:

* **Forecasting**: when and how to fit a simple trend, seasonality assumptions, and when to refuse because a series is too short or too noisy.
* **Cohort and retention analysis**: standard cohort definitions, the retention curve template reported to leadership, and any gotchas (left-censoring, survivorship) that trip up naive implementations.
* **Funnel analysis**: the canonical stage definitions for key product funnels, so "where are users dropping off in onboarding?" is consistent across responses.
* **Charting**: visualization conventions like which chart type to use for which question, color palettes, and when a table is clearer than a plot.
* **Analytical writing**: how to structure a finding (TL;DR first, number, mechanism, caveat), and the level of hedging that’s appropriate given the degree of confidence.

Every data team likely already has these conventions; they just usually live in someone's head and are only occasionally documented. Writing them down as skills ensures Claude applies them as consistently as your data scientist would.

### Connect to business context, not just the warehouse

Even this combination of knowledge skills and runbook skills is not always enough to answer a question. When someone asks "why did sign-ups drop on Tuesday?", the answer often isn’t in the data model, but rather is frequently spread across Slack threads, incident trackers, release notes, and docs.

To account for these gaps, we wire Claude Tag into our internal knowledge index, which catalogs documents, discussions, and events across the company. When the agent sees a metric move, it can search that index for *contemporaneous context*: an incident opened that morning, a feature flag flipped, a competitor announcement someone shared in a channel.

The answer now would look like "sign-ups dropped 12% Tuesday: there was a payment-service incident open 9-11am that morning, and the dip is concentrated in the affected region."

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7e018507d3cd146d2969dd_0990031b.png)

If your organization has a knowledge graph, internal search, or even just well-organized incident and changelog feeds, connecting Claude Tag to them is the highest-leverage information you can add after the warehouse itself. You can also [connect Claude Tag so it can read and get context from key channels across Slack](https://claude.com/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel).

### Permission the service account deliberately

Claude Tag queries your warehouse as a service account, not as the human who asked the question. While that's the right design (since you don't want every Slack user requiring direct warehouse credentials), [**everyone who can mention the bot has the bot's data access**](https://claude.com/blog/agent-identity-access-model)**.** There is no per-user row-level security: what the service account can read, anyone in the channel can ask about.

We approach this in five ways (and we recommend taking this seriously as it’s easy to get wrong and hard to undo):

**1. Scope the service account to governed data only.** At Anthropic, Claude Tag's service account can read the semantic layer's output tables and the curated marts that feed them. It cannot read raw event streams, staging schemas, or anything in a personal sandbox. If a question requires data outside that boundary, the agent says so rather than guessing. That is also the right user experience because data outside the governed layer hasn't been validated.

**2. Classify PII at the column level and deny the service account clearance.** Governed data isn’t automatically PII safe data (e.g., a curated table can still carry an email address). We maintain a data catalog with column-level lineage, so every column’s origin and downstream flow is known. When new columns land, Claude scans them and flags likely PII candidates for human review. A human then applies the classification in the column’s metadata, and lineage propagates that label to derived tables. Given Claude Tag’s service account holds no PII clearance, the warehouse’s column-level access controls make any PII columns invisible to the agent. It can query the table, but the sensitive columns simply aren’t readable.

**3. Document the connection path in the skill itself.** Our warehouse skill has a dedicated section on *how* the agent connects (whether via CLI, direct API, or an MCP server) and exactly how authentication works for each path. This prosaic feature allows us to differentiate between the agent failing cleanly ("I can't reach the warehouse from this surface; here's why") versus failing confusingly (a query that silently runs against the wrong project, or an auth prompt relayed somewhere it shouldn't be). When the connection mechanics are in the skill, the agent can explain its own constraints.

**4. Treat Claude’s channel membership as an access grant.** Adding Claude Tag to a Slack channel is, in effect, granting that channel's members read access to whatever the agent can query. We made this explicit: Claude is added to a channel by a data-team member, and the data team owns the list of channels.

**5. Label every query.** For every warehouse query, Claude Tag carries labels identifying the surface, the conversation, and the requesting user (where Slack provides it). This doesn't enforce anything at query time, but it provides cost attribution and audit trails (you can determine who asked the question that scanned 4 TB after the fact).

Our general posture is that a data analytics agent in Slack is a **shared read replica of your governed warehouse,** and we try to scope it as such.

### Instrument every answer

Determining whether the agent gave a sufficient answer is not something you can eyeball.

We log a structured event for every question Claude Tag handles. This includes:

* Which skill files were loaded and at what version;
* Whether the user reacted with 👍/ 👎 or replied with a correction; and
* Any open data quality warnings on the tables it touched. We also surface any data quality warnings in the answer's footer, so a stale-data alert appears next to the number rather than being invisible.

This telemetry feeds two views. One tracks **adoption** or what fraction of agent queries route through the governed layer rather than ad hoc SQL by surface and domain. The other tracks **correctness** measured by the rate of 👎 reactions and corrections by domain. This is the online proxy for accuracy between eval runs.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7e018507d3cd146d2969e3_07987b0d.png)

The adoption metric turned out to be the single most actionable number we tracked. When it dips for a domain, it almost always means either a skill file has drifted or a new class of questions has appeared that the semantic layer doesn't cover.

## How this accelerates self-service analytics adoption

### Claude Tag threads become the new meeting

Our favorite, most effective Claude Tag threads usually have multiple people in them. In these cases we see people contributing ideas and context while Claude handles the legwork.

For example, a data team member asked Claude why a revenue dashboard was taking a few minutes longer than usual to load. Claude discovered query results weren't being cached and a bug was slowing down how results reached the page.

Claude notified the dashboard owner who decided to fix the cache immediately while handling the bug in a separate motion.

The owner then asked what other dashboards had slowed, and it turned out dozens were impacted by the same caching error. Claude wrote the caching fix, the data team member reviewed it, and all impacted dashboards were functioning at full capacity in less than an hour.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7e018507d3cd146d2969e0_0dceb0a6.png)

Fictional recreation of a Claude Tag conversation for illustrative purposes. Incident details, names, and tools are not real.

These threads are open which is helpful for multiple reasons. People reading along pick up context (what broke, why, how it got fixed) without anyone writing a summary for them. More importantly, they don't have to remain passive readers. Anyone who knows something useful can jump in and contribute, the way the team members did in the example above.

So keep the agent in shared channels and keep the work in threads instead of DMs, as the thread can function as a reviewable historical record.

### Claude Tag handles repetitive tasks

A lot of data work is recurring: pipeline health checks, KPI monitoring, etc. You can ask [Claude to create loops](https://www.youtube.com/watch?v=SlGRN8jh2RI) that can handle cyclical tasks on schedule or in response to unusual changes. Some data specific examples we’ve implemented include:

<!-- yt-inline:SlGRN8jh2RI -->
[![Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next](https://img.youtube.com/vi/SlGRN8jh2RI/hqdefault.jpg)](https://www.youtube.com/watch?v=SlGRN8jh2RI)

<details>
<summary>자막: Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next (24:36)</summary>

[00:00]
Okay, I'm excited to introduce our next
speaker. Show of hands, who here uses
Claude code?
Okay, show of hands, who here has Claude
code psychosis?
Come on guys, [clears throat] it's okay.
It's okay. Um my my my team lovingly
says I have Claude code psychosis, which
may or may not be true. Um we are
delighted to have Boris Cherny with us
today. Uh Boris is the creator, the
father of Claude code. Um and uh in the
process of doing that has just had a
front row seat to to reinventing uh the
modern way of of software development.
Um and we're we're really grateful to
you, Boris, for taking the time to speak
with us today. We know that um the
entirety of software development kind of
rests on your shoulders. So, thank you
for taking it out of your time to be
with us today. And interviewing Boris is
Lauren Reader from our team.
Thank you.
>> [applause]
>> Giving our chairs.
Um you took my you took my opening line,
Asia. We asked who here uses Claude
code. There's a lot of hands. That's

[00:01]
awesome.
Thank you for joining us, Boris. It's
very special to have you here. Um
as a roomful of builders, I think you
are changing building entirely. And so,
I'm very curious to explore how you
think about the future of software,
coding, and what we should spend all of
our free time on. Um but I'll give you a
me a tiny bit more background on you so
that everyone has a little bit more
context. So, beyond creating Claude
code, Boris is very much an engineer's
engineer. You were writing a lot of code
through your whole career, writing
textbooks about code, including
programming in TypeScript. Um and I
think last time we chatted you hadn't
written a single line of code in the
last year, or at least so far in 2026,
which is quite the change. Um There's
also a a little known thing back in
middle school, I wrote a guide about uh
writing BASIC for TI-83 Plus
calculators.
And I I just I I searched for it, it's
actually still on the internet. It's
extremely embarrassing, so please don't
search it. But it [laughter] exists. We
will definitely be finding that. Um so,

[00:02]
we're going to do I'm going to start
with a few questions here. Maybe we'll
start with a little bit of the history
of Claude code, how you started it, and
then we're going to have a lot of
audience Q&A for this one. And so, start
thinking about your questions in the
back of your head, uh and would love to
turn it over to you all soon.
Yeah. Um and also real quick, so for
people that use Claude code, do people
use the CLI mostly? Like okay, majority
CLI?
Okay. That's a lot. Majority desktop?
Okay. Majority VS code or JetBrains IDE?
Okay. That's actually not a lot. Okay.
Other?
I'm like iOS mostly these days. Yeah.
>> [laughter]
>> Okay. Cool.
Um yeah, so I started Claude code kind
of accidentally in a in a lot of ways.
Um I joined this team back in late 2024.
It was a sort of this incubator within
Anthropic called Anthropic Labs.
And uh the team kind of served its
purpose. Um we created Claude code, uh
MCP, and the desktop app. It was a team
it was just a few of us.
So, very much like innovation team.

[00:03]
We built the thing that we wanted to
build, we disbanded the team. Uh now the
team's actually back together for round
two. Mike Krieger, who's the you know,
like the chief product officer at at
Anthropic and used to be one of the
founders at Instagram, so he's leading
that right now.
Um so the kind of the the the the reason
that I started to work on coding is we
felt like there was this product
overhang. And I I'm guessing people here
use that word a lot. Uh but we
definitely use this word a lot in kind
of within the lab.
Uh there's this idea that the model can
do all the stuff that no product has yet
captured. And in late 2024, when we were
looking at coding, the way that we did
coding, the state of the art at the time
was type ahead. It was you open your IDE
and you press tab and you can like
complete like one line at a time. And
that was the thing that Sonnet 3.5
enabled for the first time. But the
feeling was we could actually go a lot
further than that. And the model was
almost ready for the next big step. So,
we don't have to do type ahead anymore,
we can just have the agent write all of
the code.

[00:04]
And so, I built it, and it just really
didn't work for the first 6 months. It
was like not very good. It was barely
usable. I wrote it from I used it for
maybe 10% of my code or something like
that. And even after we released Claude
code initially, it was not a hit.
There's a lot of people that used it,
but it did not have this exponential
growth that it has today.
Um that started with Opus 4 in May. And
I I remember that very clearly. That's
like when the exponential growth
started, and then it kind of inflected
with every model release. Uh like it
started with Opus 4, then 4.5, then 4.6,
now 4.7. It just kind of keeps
inflecting.
But essentially, we were trying to build
this thing that was like pre-PMF, and we
knew that it wouldn't have PMF for 6
months because we were building for the
next model. And that was the idea the
pretty much the whole time.
And you know, for Anthropic in general,
we've always just been very focused.
We've always cared about business and
enterprise and safety and coding. That's
just always been kind of the way that we
wanted to build. And so, at some point
we kind of knew that we wanted to build
a product. We didn't know exactly what

[00:05]
we wanted. So, this kind of ended up
being the the product bet.
It's an incredible story, especially
that it was an accident.
Um
so, you've said on the record that you
think coding is solved. Uh if this is
one of the three best from Anthropic,
can you tell us more about what you mean
by that, and what might still not be
solved, or what second-order problems
might come? All right. I can ask another
question for the room. Who writes 100%
of their code by hand?
Who writes 100% of their code using a
agent like Claude code?
Okay. Who's like somewhere in between?
Okay. So, like 50% solved.
>> [laughter]
>> I mean, for me it's for me it's like for
me it's 100%. Like the the Claude code
code base, um you know, it leaked, so
you know, people know. Uh it's pretty
simple. It's just like TypeScript and
it's React. Like there's no big secret.
There's there's nothing really
complicated. The the reason we picked
TypeScript and React is it's very on
distribution for the model. So, when we
started, you know, building the code
base, the model was not as intelligent

[00:06]
as it is today, so the language and the
framework mattered a lot. Nowadays, you
know, it can write whatever, and it can
pick up new languages, new frameworks it
hasn't seen. But back then, you wanted
to use something pretty on distribution.
Because of that, I think fairly early we
got to the point where the model just
wrote 100% of the code. And for us, this
happened sometime in October, November
last year.
And so, for me today, you know, like the
model writes 100% of my code. I write
somewhere, you know, usually a few dozen
PRs every day.
Uh there was a day last week I did like
150 PRs in a day. That was like that was
a record. I was just trying to kind of
push to see how far I can get it.
Um but yeah, it's like for me for me
it's just solved. Um but this is not the
case everywhere. There's very big
complicated code bases. There's kind of
weird languages the model's not good at
yet. Um and you know, as everyone here
knows, it's it's getting there. Usually
the answer is just wait for the next
model.
Can you actually tell us about your
personal setup? You walked us through it
the other day. It is pretty wild.
Yeah. Um so, I shared my personal setup
like 6 months ago or something on on

[00:07]
Twitter. And it it's funny, I actually I
shared it I didn't realize that it would
be surprising for anyone. That was just
like the way that I coded.
>> [laughter]
>> And it's changed since then. It's
changed. Um and so, now actually most of
my work I do from my phone.
Um and so,
I don't know if like you guys won't be
able to see this, but I have um
so, I have like the Claude app, and if
you open the Claude app,
on the left-hand side, there's this
little code tab,
and I just have a bunch of sessions
going.
Um
you you probably can't see it.
>> How many sessions?
Uh usually have like maybe like five to
10 sessions. Uh and then the sessions
usually have a bunch of agents, so I
think currently probably like a few
hundred agents going.
Um usually every night I have like a few
thousand that are doing kind of deeper
work. There's a few ways to manage it.
One is that you ask Claude to use a
bunch of sub-agents to do work.
Actually, the the thing that I've been
finding myself using more and more is
the loop. So, this is {slash} loop, and
it's just like the coolest thing. It's

[00:08]
like the simplest thing that works. All
it is is you have Claude use cron to
schedule a job for some point in the
future, and it's a repeat job.
And it can run every every minute, every
5 minutes, every day, kind of however
often you want to schedule it.
And at [snorts] this point, I have like
dozens of loops that are running for
stuff. So, I have one that's babysitting
my PRs, like fixing CI, auto-rebasing. I
have another one that keeps CI healthy.
So, like if there's like a flaky test or
whatever, it'll it'll go and fix it. Um
I have another one that grabs uh
feedback from Twitter and kind of
clusters it for me every 30 minutes. So,
I just have a bunch of these loops
running at any time. I sort of feel like
loops are the future at this point. If
you haven't experimented with it, highly
highly recommend it. And we also just
launched routines, which is the same
thing but kind of on the server. So,
even if you close your laptop, it it
keeps going.
So, that's your personal setup. Tell us
about what you think teams will look
like in the future. How do you
extrapolate from all the work you're
doing to keep everyone on the team
moving forward, understanding the
context, or do you think we need to let

[00:09]
go of a lot more to agents to make it
work?
Um I think so I you know, it's like it's
so hard to make predictions, but um
I'm here to make predictions, so I'll
try to make some.
I I I feel like the way that things are
going is generally there's going to be a
lot more generalists than there are
today.
And
today when we talk about generalists, I
think largely we're talking about people
that are still engineers. So, they're
still writing code, but maybe they're
kind of product engineers. So, maybe
when we say generalist, it's like a you
know, they do iOS and web and server,
for example. That's like a generalist in
engineering.
But I think the thing that we're going
to start to see a lot more of is
generalists that are cross-disciplinary.
So, this is engineers that are really
good at product engineering, but also
really great at design. Or really great
at product and data science and
engineering.
Um
I don't know. It's it's something that
we're starting to see on our team. So,
actually like a lot of people on the
Claude code team
are generalists across disciplines.
Everyone on our team codes. So, like our

[00:10]
engineering manager, our product
manager, our designers, our data
scientist, our finance guy, our user
researcher, every single person on our
team writes code.
And so, you know, like they're
specialist in something, but now also
everyone's just coding.
And you know,
I'm seeing some nods, but I bet also
it's actually not that surprising to
people in this room cuz I bet you're
seeing the same things.
Um [clears throat] I'll have one more
favorite questions then we'll open up to
the audience. So, we talked a bit about
what's changing with coding. I'm curious
about what you see changing in the world
of software or software products.
Um
I think as we see AI making writing code
10 or 100x cheaper,
what happens to the value of the
products that are produced with
software? Do we have a SAS apocalypse on
our hands? How do you think this plays
out? And again, you're going to have to
make another prediction.
The SAS apocalypse question is my
favorite question then.
Um
I think there's two things that are
going to happen and I I don't think
either of them is the thing that people
have been talking about.

[00:11]
I think one is Is anyone here an
acquired listener? Like the acquired
podcast?
Yeah, it's like the best podcast.
Uh
I actually I I got to do a unplugged
with them the other week and I I just I
I felt like I got to like meet my heroes
cuz they're they're just like the hosts
are the best.
So, they have this idea of uh seven
powers and and this is a this is like
Hamilton. He kind of wrote he wrote a
book about this and this is kind of the
seven modes in business. And I think
what's going to happen is because of AI,
some of these modes are going to get
more important and some are going to get
less important. And so, like for
example, one that gets less important is
uh switching costs because you can just
use the model and you can kind of port
from one thing to a different thing.
Another one that gets less important is
process power
because for companies whose mode is like
workflows and process and things like
this,
Claude is getting really good at
figuring out process. And especially
with 4.7, it can just hill climb
anything. So, if you give it a target
and you tell it to iterate until it's
done, it will just do it. I think this
is the first model like that.

[00:12]
So, I think these are going to get less
important, but I think the previous
modes actually still matter. So, this is
like network effects, uh scale
economies, cornered resources, things
like that. These are not really changing
with AI.
I think the second thing is if you look
at the number of startups today or like
maybe in the next you know, the past 10
years, I think the number of startups in
the next 10 years that are just going to
like disrupt everything is going to
increase like 10x.
Because right now you can be a tiny
startup, you could build a thing that's
as valuable as a large company and you
can actually compete head-to-head
because the large company has to evolve
their business process, they have to
evolve the way they work, they have to
retrain everyone to use technology,
they're going to face a lot of internal
resistance to that.
But
you know, no one here has that problem.
If you're starting fresh, then you can
kind of build with AI natively from the
ground up.
So, I don't know. I I think it's the
best time to build. It's the best time
to be a startup. It's there's so much
disruption coming.
So, there is hope for us after all.
Thank you, Boris.
Um I would love to open up to audience
questions if anyone has anything they

[00:13]
would like to ask.
Dan?
I Yeah, I'm curious.
Um you said that you built uh
6 months before there was product market
fit, but now given that the models are
good enough, how much do you attribute
the success of Claude code to the model
versus like product decisions in the the
like
field of product?
Uh I think it's probably a mix.
Yeah, I think it's a mix. I think I
think if you asked me maybe a year ago,
the ratio was maybe something like
50/50.
Um maybe I don't know. If you asked me 6
months ago, the mix would be 50/50.
>> What about in 2 years?
Oh, 2 year I don't know, dude. We plan
in like we plan in 1 week out.
>> months. Sometime in the future.
>> [laughter]
>> And by the way, I think the reason it
was 50/50 is um
you know, I I I like I I did YC back in
the day. I was like the first hire at a
YC company and like I did a bunch of
startups.
And in startups like the thing that they
drill into you and then especially in YC
over and over is build something people
love.
And so, it it doesn't matter what the

[00:14]
product is, it doesn't matter like the
model and all this stuff. You still in
the end have to build a thing that
people love. And I think that's that's
why the product matters is we we pay so
much attention to the little details so
that as you use it all day, it's a
really great experience.
I think as the model's gotten better,
the harness kind of gets less important.
And I I think like I think that we're
thinking about right now is like how do
we evolve the harness? So, like how do
we make loops more of a first class
thing? How do we make it easier to run a
lot of agents? Uh you know, beside you
know, like sub agents is one idea.
There's a bunch more stuff that we're
cooking.
But I think in a year, the model will be
much better aligned. And so, all the
safety mechanisms that we have today
around
uh prompt injection and kind of static
verification of commands and uh
permission modes, human in the loop, all
this kind of stuff is just going to be
less important cuz the model will just
do the right thing.
Um So, yeah, that's that's my
prediction.
Thank you.
You want to toss the box, Dan?
>> [snorts]
>> Great.

[00:15]
Um To zoom to zoom out a little bit from
software, I think Claude code did a
cultural change a few months ago where
it democratized like building software.
You can see uh shop owners building
their own
um software for themselves or even uh
programming microcontrollers to control
the light when someone opens the door.
Um do you see in the future um
building software becoming a skill like
uh I know uh Microsoft Office? Um so,
it's a thing that ev- everybody can do,
not just people in the tech industry? Oh
my god, yes. Yes. Yes. I I I think it's
going to be even more than that. I think
it's going to be I don't know. It's
going to be a skill like yeah, like I
know how to send a text message.
I I I think um
you know, like I I read a my my two
genres are essentially sci-fi and tech
history. This is what I read a lot of.
I I think in tech history, there's one
thing which I think to me is the
clearest parallel for what's happening
right now. And this is in the 1400s,
the printing press in Europe.
And what what happened was before the
printing press, essentially 10% of the

[00:16]
European population was literate. They
knew how to read and write.
They were often employed by like kings
and lords that were not literate.
And their job was to you know, their
their job was to read and write and this
is not something that everyone knew how
to do.
>> [snorts]
>> The printing press was invented, then
there were two more presses and in the
50 years after the first printing press,
there was more literature published in
Europe than in the thousand years
before.
And over the same period, the cost of
literature, the cost of a book went down
like a 100x. And then, you know, it took
a couple hundred years cuz you know,
learning to read and write is hard. You
need education systems and government
and everyone can't be working on farms
and so on. But over the next few hundred
years, literacy globally went up to like
70%. And so, you know, now we can all
read and write and you don't need a a
degree in reading and writing to know
how to read and write. Although still
there are professional writers and that
is a thing that you can do.
So, I I think the thing that's about to
happen and it's going to be much faster
than 50 years is software will be a
thing that is fully democratized, that
anyone can do.
And you know, there's a lot of

[00:17]
corollaries to this. So, for example,
let's say you're writing accounting
software.
The best person to write accounting
software, I think maybe even today, is
not an engineer, it's a really good
accountant because they know the domain
really well and coding is the easy part.
It's knowing the domain that's the hard
part. And I I think this is just
obviously the the future.
So, uh one of the things Greg said was
that you guys are living in the future a
little bit cuz you get to have access to
the models and the agents. Claude code
was an internal tool before you released
it. Um is the gap between where you guys
are in engineering and the rest of the
world, is that a month? Is it 3 months?
Is it 6 months? And is that is that gap
getting bigger or smaller over time?
Yeah, so so internally, we use the same
models everyone else does.
Um for us, the dog fooding is really
really important. So, we use the thing
that everyone else here does. Um you
know, we use like a little bit of mythos
to try it and then we use a lot of Opus
4.7 to to dog food it and to write most
of our code.
Um I think on the model side, there

[00:18]
isn't really a gap. Um you know, it's
like it's pretty much mythos and you
know, that will become some version of
some descendant of that will become
available at some point to everyone.
I think on the product side, there's
probably a far larger gap. And that's
just related to us changing all of our
processes. Like if you talk to people at
Anthropic, we use Claude for literally
everything. And our Claudes are talking
all day like as as I'm coding, as my
Claudes are coding in a loop, they will
communicate over Slack to talk to other
people's Claudes that are also running
in a loop to kind of figure out
unknowns.
We have no more manually written code
anywhere at the company. All of the SQL
is written by uh by models. Everything
is just built by the models. So, I I I
think actually the place that we're
ahead is not the technology cuz the same
technology available to us is available
to everyone here because fundamentally,
we are building a platform. And so, for
us, it's really important that
developers can use the same thing that
we're using and that we we dog food
everything that we put out there.
But I think there's actually a far
bigger weed in kind of the
organizational structure and
organizational process. And this is a
place where you know, hopefully we can

[00:19]
talk about it in places like this and uh
everyone can kind of learn from it and
and also evolve.
Yeah, and I think that's one of the
advantages startups have. It's so much
easier to start there.
Jared?
Yeah, um last time we talked, I think I
think you'd mentioned we talked a little
bit about multi-agent and it was very in
code at the time at a prior Sequoia
event and you mentioned that there were
some things going down the pipeline and
thing you're talking you're thinking
about. Now obviously there's slash
batch, there's slash loop, there's sub
teams, there's teams. Can you speak some
to either at the model level and at the
harness level, how you're injecting
priors in the harness level, how the
objective function is changing the model
level to kind of make this experience
around delegating work, spinning up
agents better? Cuz so much of the work
is parallelizable. You can do so many
things so much faster and I feel like I
have to overlay my own intuition for
when to parallelize things rather than
the model kind of understanding that you
can spin up 10 sub agents for something.
Yeah, I mean on on the product side, it
really just comes down to prompting.
That's That's how it is. And so, you
know, we we tweak prompts to kind of
help the model do stuff in parallel
more.
But also, honestly, as the model gets

[00:20]
better, it just naturally does this. And
so, something like loop, I found
actually 4.7, it just starts doing. Uh
which is really cool. It's like it does
something like uh you know, I'll I'll
I'll tell it, "Go uh
pull this data query." And it's like,
"Hey, I noticed that the data is
changing over time. I'll start a loop
and I'll give you a report every 30
minutes." And I'm like, "Great. Can you
send it to me over Slack?" And then it
uses the Slack MCP to do that. So, so I
think actually over time, it's not on
users to figure out how to hold the
tools better. And if that's the case,
it's actually a product design problem
and like I'm not doing a good job.
It's really on the model to do this
stuff better and on us kind of prompting
it so it naturally does this.
Um so, right now it seems like a lot of
us use um like Claude or Codex or these
uh tools in the cloud to do a lot of our
computing. But then, there are some very
vocal advocates of uh having your AI be
local. And I could imagine over time as
um open way models and other things
catch up that this could be more of a

[00:21]
possibility for people get really
high-quality coding assistance. So, I'm
curious your vision of say over the next
like
years or something like that. Do you see
the trajectory of everyone still really
relying on the like cloud centralized
compute or uh is there a pivot to oh, we
all just have our local agents that we
can rely on and they don't get throttled
and other benefits?
Yeah, I think it um
I don't know. There's maybe a few ways
to answer that. I think maybe like kind
of the the most fundamental way to
answer that is it doesn't matter.
Cuz Cuz I think now we're getting to the
point where the model is just able to
figure it out. So, I think like by a
couple years from now, the model is just
going to be doing all the code. It's
going to be starting the agents. It's
going to be building the environments.
And so, like if it decides like actually
I'll use like local models to do this,
then you know, that's what it'll do.
These I I don't think these will be
decisions that we are making as
engineers anymore.
We have time for a couple more
questions, so I can toss this out.
Jamie.
Nester. Thank you.
It feels like one of the great uh

[00:22]
decisions with Claude Code was making
use of the fact that a lot of
developers' tools and workflows are
local.
But um that isn't necessarily always the
case for sort of general knowledge work
with, you know, cloud tools. I'm curious
how you're thinking about this with
Co-work of how do you give Co-work
enough access to the tools that we use
to be powerful the same way that Claude
Code is for developers?
Yeah, it's That's a really great
question. Um I know I know when I was uh
when I was at a big company, we took
like 5 years moving all the environments
to remote. It's just like so much work,
especially at a big scale.
Um but for knowledge work, largely, it's
there already with like Salesforce and
Docs and things like that.
Um for us, it's always just the simplest
answer. It's just MCP.
So, the same MCP connector that you have
in Claude AI, you hook up like, you
know, Salesforce, you hook up Google
Docs, Google Calendar. Uh and then
Co-work can use that. Claude CLI can use
it. Claude Code everywhere can use it.
And for the for the systems that don't
have MCPs, like do you think that's
where computer use is going to be a big

[00:23]
opportunity?
Yeah, I think computer use is kind of a
catchall. Um so, I think currently, for
as far as I know, I think Anthropic is
like pretty far ahead on computers. And
so, like if you use it through Co-work,
it's quite good. Um so, it's able to use
pretty much any piece of software that
you have on your computer. It's very
slow, but it does it quite well now,
especially with 4.7.
Um Yeah, but I think I think otherwise
like MCP is is kind of the answer. It's
And you know, all this stuff just
doesn't matter that much. It could be
MCPs, APIs, just some sort of
programmatic access cuz the the model
doesn't care. It's to mo- To the model,
it's just tokens.
All right, we have time for one more
question.
Um Ryan.
Sean, do you want to toss the Thank you.
Um you've kind of alluded to this, but
if like sometime ago you saw the
probabil- the product overhang and
thought to build a product that would
then become more interesting once models
got better,
could you just talk even in vague terms
about the shape of a product you'd build
today that you think could becomes a
much more interesting as models get

[00:24]
better in 6 months to a year?
Yeah, Claude design I I think is a
really good example. It's uh it's pretty
good today. It's going to get a lot
better.
Um there's also a few things that we're
cooking up for Claude Code uh that are
going to be landing over the coming
weeks. So, you'll see those.
Um and then I think uh I think loop and
batch and things like this around like
massively parallelizing agents, that's
going to get better.
And computer use is another good one.
All right, Boris. Thank you so much for
joining us. I think we'll be here for a
little longer if anyone has questions.
>> [applause]
>> Thanks, guys.

</details>


* **Proactive Readouts**: Claude provides a summary before a weekly standup: what moved last week, how it compares to the week prior, and what’s worth noting.
* **Test Monitoring**: When we’re monitoring a launch or an experiment, Claude provides readouts multiple times a day. During one recent experiment, it noticed the settings had changed partway through and helped us catch and fix it early.
* **Observability**: Other loops monitor our pipelines and dashboards. If a pipeline fails, Claude starts investigating, drafts a fix, and pings the person on call. If a KPI moves unexpectedly, Claude provides likely explanations: a holiday effect? an upstream data change? and checks them before anyone opens a dashboard.
* **Triage**: Another loop tracks our data questions channel. For each new question, it makes a call: answer it directly, start a deeper investigation, or bring in a human. By the time someone from the data team checks, most of the work is already done.

Claude can also help design the loop. Ask @Claude what repetitive jobs it’s seen in your channels and how it can help.

### Stepping in when needed

You can allow Claude to be more proactive in any channel you choose, reading along and stepping in to help when needed. In one of our data channels over the last month, Claude Tag answered more than 75% of questions people posted, typically within a minute or two, even without being called.

For example, an Anthropic team member asked in a public channel whether a dashboard included a new usage category. Within 90 seconds Claude answered how the data was defined, confirmed the new segment was missing, proposed a fix, and drafted a PR. A data scientist reviewed and approved. Claude then merged the PR and refreshed the dashboard.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7e018507d3cd146d2969f4_e14fa07b.png)

Fictional recreation of a Claude Tag conversation for illustrative purposes. Incident details, names, and tools are not real.

## Getting started

If you've already done the work from [our first post](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude), the Slack deployment is mostly plumbing, though the order is important:

1. **Permissions first.** Decide what the service account can read before you write a line of agent code. It's much easier to widen access later than to claw it back.
2. **Distribution second.** Pick mounted-repo or skills-over-MCP and verify freshness end-to-end: change a skill file, and confirm Claude Tag picks it up within your SLA.
3. **Telemetry from day one.** You will not retroactively instrument month-old conversations. Log the structured event on the very first question.
4. **Knowledge index when you can.** The warehouse answers *what*; your internal docs and incident feeds answer *why*. Wire them in as soon as the data path is stable.
5. **Analytics skills last.** Create the data-access skill first and then let real questions inform which analyst skills (forecasting, cohorts, funnels) your co-workers actually need.

*This article was written by Clement Peng and Lily Zhao, members of Anthropic's Data Science and Data Engineering team, with contributions from Josh Cherry and Michael Segner.*

‍

FAQ

No items found.

- Ready to try it? Add Claude to your Slack workspace and tag @Claude in any channel.

Add Claude to Slack

[Add Claude to Slack](https://api.anthropic.com/integrations/v1/slack/install)Add Claude to Slack

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Aug 21, 2026

### Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders

Product announcements

[Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](#)Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders

[Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

Jul 24, 2026

### The new rules of context engineering for Claude 5 generation models

Claude Code

[The new rules of context engineering for Claude 5 generation models](#) The new rules of context engineering for Claude 5 generation models

[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) The new rules of context engineering for Claude 5 generation models

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Aug 21, 2026

### The AI-Native SDLC playbook

Enterprise AI

[The AI-Native SDLC playbook](#)The AI-Native SDLC playbook

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)The AI-Native SDLC playbook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

Aug 20, 2026

### How monday.com transformed its platform into an agent-first product where humans and agents collaborate

Agents

[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](#)How monday.com transformed its platform into an agent-first product where humans and agents collaborate

[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate)How monday.com transformed its platform into an agent-first product where humans and agents collaborate

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Tag
