---
title: "Patrick Collison on Claude Code at Stripe"
channel: claude
url: https://www.youtube.com/watch?v=S_lzYIvtEaQ
youtube_id: S_lzYIvtEaQ
published: 2026-09-24
duration: "17:50"
captions: en
---

# Patrick Collison on Claude Code at Stripe

[![Patrick Collison on Claude Code at Stripe](https://img.youtube.com/vi/S_lzYIvtEaQ/hqdefault.jpg)](https://www.youtube.com/watch?v=S_lzYIvtEaQ)

<details>
<summary>자막: Patrick Collison on Claude Code at Stripe (17:50)</summary>

[00:00]
- But our house, we
installed a weather station.
With Claude, I could design
from scratch a multimodal model,
and it predicts afternoon weather
better than the National Weather Service.
(bright pleasant music)
- I think a lot of people in the industry,
they tried to move to Claude VMs.
They tried to move to
these remote environments.
What gave you the conviction to do this?
- Well, reliability and security
are really important for us.
Stripe operates with five and
a half nines of reliability,
so extreme reliability for our core APIs.
But at the same time,
we want to be developing
and launching new products
and adding new features extremely quickly.
We want to have continuous
deployment of our API.
And across financial services,
the way things typically work is
maybe things get deployed
once a month, once a quarter,
certain places once a half.
And I mean, that provides
a kind of local stability,

[00:01]
but of course at two enormous costs
when you don't get quick
feedback from customers,
you can't ship things on a regular basis.
But then also it does mean
that these moments of migration
are incredibly fraught and scary
because you've this accumulated detritus
of months of progress.
And so we though that
was totally untenable.
In fact, when we're developing things,
we want feedback from our
customers multiple times a day.
And so we really weren't
willing to compromise on this.
And so in order to achieve
five and a half nines of reliability,
but with this continuous process
of feature evolution development,
we though we really needed to invest
in the end-to-end development
and quality assurance process.
And so the devboxes are
just the first part of that,
and we can have some instrumentation
there and observability
and operational
characteristics and so forth.
And then a whole process
of incremental deployment
where you first roll it out to, you know,
a handful of machines
and then 1% of machines
and some progressive
rollout strategy from there.

[00:02]
But I guess the general
reason for our conviction,
we needed extreme
reliability and security,
extreme velocity,
and I think it's the
only way to achieve both.
- It's incredibly impressive,
the bar that you've been able to hit.
And I feel like everyone in
the industry looks to Stripe
as the company that sets
the bar for reliability.
- That's very nice to hear.
We obviously were working
extremely hard to sustain that.
It's been interesting for us
in the era of agentic development
where obviously there's
a question of, well,
will AI be a tailwind or a headwind here?
And there are obviously
a lot of concerns of,
well, if people are
writing code so much faster
and maybe they're not
reviewing each line of the code
with quite as much scrutiny,
lots of speculation
as to which way this will cut.
I was speaking with one
engineer at Stripe this morning,
and over the course of H1,
he had more than 600 pull requests merged.
Every single one was written with AI,
and exactly one of those pull
requests had to be reverted,

[00:03]
which at least suggests
that it is possible
to have this enormously
accelerated development rate
and with still empirically
quite high reliability.
Minions of this thing on top of it,
which are a way to
orchestrate VMs with prompts
from Slack or from a web interface
or, in principle, from any tool,
you can just ask for some
feature to be implemented
or some task to be completed.
It will create a fully new VM for that
and then go and perform
all the tasks along the way
and then it'll package it up
and submit it and build it
and run it through our test suite
and the whole end-to-end process.
We have seen that quality per pull request
over the last 18 months has gone up.
Now, there's still some challenge
because the incidents per unit time
has gone up slightly.
And so now they're mostly
very minor incidents
and all of our secondary
mechanisms for catching things
before they become problematic have meant
that our total reliability
is essentially unchanged,

[00:04]
which we take as quite heartening.
And then I think the cool thing is
obviously with LLMs and
AI and everything else,
there's now of course
the possibility to build
new observability and new
instrumentation and new harnesses
and new kinds of automated scrutiny
that we couldn't build before.
And so I feel pretty confident
that over the next year
or two that AI on net
will make Stripe quite
a bit more reliable.
- So tell me a little bit
more, like, nuts and bolts.
How do you ship faster using AI
without trading off against
reliability and quality?
What are the specific
guardrails that you have?
We wanna ship a model
that's really aligned
and there's a bunch of protections,
there's a prompt injection protection.
And then also as the number
of pull requests accumulates,
how do you make sure that
everything remains reliable
and that code quality goes up?
- It does mostly come back to this idea of
relying on invariance and
hard barriers rather than
things that are somewhat more subjective

[00:05]
or discretionary or probabilistic.
And so obviously it's nice
if the model is aligned
and is more likely to write correct code
or secure code or whatever.
I mean, nothing's ever perfect.
You really do want to rely on guarantees.
- That's really interesting.
So what I'm hearing is,
before AI, there was a lot of benefits
to encoding guardrails and
constraints as infrastructure.
- Yes.
- Because then engineers
can make less mistakes.
And there's also benefits
to data segregation
and making sure that people just literally
can't access data they shouldn't access.
And now this is kind of paying dividends.
- Yeah. I mean, this is full
agreement with all of that.
And actually we started seriously
investing a lot of this,
the apparatus and the tagging
and the sort of semantically
aware guardrails
around our data back in 2017.
And it's been a multi-year journey
because there's a lot of annotating to do
and there's a lot of
granular permissioning to do and so forth.

[00:06]
And we did all of this
because we though the security
guarantees were so important,
but you're right that
it kind of accidentally
put us in a better position
when agentic development came along.
- Yeah, and then luckily Claude is great
at writing guardrails too.
- Indeed, indeed. Yes.
Well, let's go back to
the point where I really,
I mean, there's kind of a
general question in the world
about whether AI and LLMs will be on net,
offense advantaging or
defense advantaging.
But my guess is that in
equilibrium in a couple of years,
this is all going to be
substantially defense advantaging.
- I wanna come back a bit more
to how Stripe uses Claude Code.
Tell me about how do you use Claude?
What are some of the
products that you've shipped?
- Every devbox has Claude
Code pre-installed.
It's the first place people go when just,
the median person is going
to complete some task.
It really has delivered
meaningful acceleration.
One case that I though was
quite informative here was,
we had the idea at the
beginning of the year
of building a thing
called Stripe Projects.
And this was kind of
inspired by Claude Code

[00:07]
because when you're building
some project with Claud Code,
for anything of any
materiality or substance,
you invariably need to couple that
to some other set of services, right?
I want PostHog for logging
or I wanna host it on Vercel
or I want a database, whatever.
Because almost all these companies
are Stripe customers already,
we thought we could work with them
to expose their capabilities in a new way
and make it incredibly easy for an agent
to instantiate an account with them.
We had this idea at the
beginning of the year.
We decided to go and build it.
It was between two and three engineers
for about two months,
but from first idea to public launch.
And that's not only building
the internal APIs and services
and harnesses and all the things,
but also integrating with now
about 50 different services
and those services all have
their own idiosyncrasies

[00:08]
and occasional bugs.
And I don't think you could have done that
with two to three people in
eight weeks in the before times.
- What would that have taken before?
- So I asked one of the engineers involved
and his estimate was a bigger team,
didn't say exactly much bigger,
but a bigger team and six months.
Let's just say twice as
big a team, I don't know.
And I guess that would've been 3x longer.
So that's a 6x relative change.
Again, maybe that's an
underestimate, who knows, in that.
Software engineers are famously optimistic
when they estimate software projects.
So maybe we can say at least a 6x feed up,
which I mean Stripe has
thousands of software engineers
and who knows if every project
is being accelerated by that magnitude.
I suspect there's a distribution.
Some things are massively
faster, some things aren't.
But again, even we're really
pessimistic if it's only,
let's just say it's only a 2x improvement
across the entirety of what we do,
I mean that's obviously still
a preposterously large deal.
- Yeah, yeah, that's huge.

[00:09]
So it takes less engineers,
they do it faster.
What do engineers do to-
- Again, with higher quality,
at least per pull request.
- With higher quality,
maintain the reliability bar.
So what do engineers do?
You just do more projects?
You try more experiments?
- I think we definitely
create more products
and try more experiments
and we can see this in the numbers.
We just had our annual conference sessions
and the number of new products
and the number of new features.
And again, the quantum of a
feature is somewhat subjectively
and qualitatively defined,
but we try to be reasonably
consistent year to year.
The number of new products and features
at sessions this year was
wildly ahead of any prior year.
The engineering organization
was somewhat larger,
but clearly there's some
kind of productivity effect
happening there.
So we're certainly building
more for customers.
But the other thing that
I find kind of interesting
and that cuts against
some of the slop concerns
is we're undertaking more projects now
to improve our architecture
and improve our code base.

[00:10]
And the line from a friend
that we often mention at Stripe
is that every code base is now the prompt
for another code base.
And of course, Jared
Sumner, former Stripe,
has demonstrated this
with the Bun rewrite.
My estimate of the...
There could be a question
of, with AI and with LLMs,
should we expect the
quality of code at Stripe
to be higher or lower in three years?
And I think the answer has to be higher.
- It's interesting. There's
this sort of fluidity
between tokens and infrastructure.
You could use the tokens
to write product code,
you can use the tokens
to write infrastructure,
you can use it to write guardrails.
And I think people kind
of over focus on using it
to directly build product,
but it's all these intermediary use cases
that are some of the most powerful.
What were some of the barriers
that you hit getting AI
to this kind of scale internally?
- In general, it's been
adopted very enthusiastically
and very completely and
very quickly and so forth.
So in some sense, it feels funny

[00:11]
to ask out the barriers
given the adoption fervor.
The phase changes were definitely
Claude Code itself as a modality.
So thank you for that.
And the model improvements
of late last year,
another inflection point.
I think over the course of this
year, I think the main thing
that people had to wrap
their minds around is
getting a sense for what's possible
and how one can now work.
One person at Stripe, the way
he likes to work is he will
work with the smartest model available
to construct a very
complicated, extensive plan,
but really invest a lot
in the planning process
and then maybe dispatch
10 different devboxes
with different agents executing
different parts of the plan.
And they might work all day,
or in the extreme case,
even for multiple days

[00:12]
on implementing this.
That's a very different
way of working, right?
It's only very different to
how things worked pre-AI,
but it's kind of non-obvious
even given Claude Code
that, oh, I can,
the quantum of labor can
actually be so extensive.
And again, if properly orchestrated
and guided that the model is capable
of such extensive self-verification.
I think that recently I myself
undervalued the plan modality
and I guess goals have also
made a lot of progress over
the course of this year
and I've changed how I use the model.
So anyway, I think there's
just kind of getting intuition
for the ever changing and
moving target of the modality.
- Yeah, I have this giant
graveyard of these projects
that I started but never finished.
- Right.
- And that's just not
really a thing anymore.
You kind of finish every project
and then you decide,
do I want this or not?
- Yes, exactly.
And it's definitely the case that
shower thoughts now get
translated to actual existence

[00:13]
at a far higher rate.
I think the returns to being curious
have gotten much higher.
- I wanna talk a little bit
about what you're saying
on the Stripe side about
how AI is changing business.
One of the things I've
been thinking about is,
with AI, it is much easier for small teams
to compete against much larger teams
in a way that you just couldn't do before.
- Yep.
- And I do these talks
at Y Combinator every
three months or whatever,
and I used to ask, "Who uses
Claude Code? Raise your hand."
And when we first released Claude Code,
a few hands went up, then at
some point every hand goes up.
And now I ask a different question
'cause that's not a
useful question anymore.
I ask, who writes 100%
of their code using AI?
And now it's roughly, I think
like 70% of people write 100%
at these very small startups.
I think there's more startups than before.
They're moving more quickly
than they were before.
They're tackling more ambitious problems.
- Yeah.
- I'm curious if you're
seeing this in the data.
- Stripe launched 15 years ago, so we have

[00:14]
a decade and a half longitudinal
time series of firm creation,
but Stripe has been fairly
popular among developers
for a reasonable number of years.
And so I think what we
see in our time series
is some kind of proxy
for what's happening in
the ecosystem overall.
And for example, during March of 2020,
we saw a significant acceleration
in new business creation on Stripe
for kind of obvious reasons.
The reason I bring this up is
because the acceleration that
we've seen over the last year
is, on a relative basis, much larger
than any prior acceleration
that we've ever seen.
The number of new businesses
launching on Stripe
per unit time is up by
roughly a factor of two.
And again, as kind of a one
proxy metric for coverage,
about a quarter of all
Delaware corporations
are now incorporated with Stripe.
And of the ones that aren't,
lots of them are, like,
random subsidiaries for a,
you know, multinational or something.
So I think of the true startups,
it's an even larger fraction than 25%.

[00:15]
So I think we're seeing
this pretty representative
and what we see is this huge acceleration.
And interestingly, the acceleration is,
it's quite broad based in the sense
that we see the same
thing in most countries.
And in fact, in many cases,
government data hasn't
even woken up to this yet.
And we recently published a
piece in the Stripe economics,
Substack, about how the UK's
official company statistics
show a year-over-year decline
in new company creation.
Whereas in fact, and we kind of walk
through the methodology in the post,
we think the UK is seeing a huge surge
in new entrepreneurship.
And what we see is that the
average revenue per new business
is going up, not down.
So it's way more companies
and the average outcome is improving.
And if you partition it
to look at businesses
reaching 100K or a million
or again, any kind of
arbitrary revenue threshold,
those are also all up very substantially.
And so I think it's just

[00:16]
a straightforwardly better
time for entrepreneurship
than it was in the relatively recent past,
and that's pretty exciting.
And I think it's also one of
the concerns with AI is that
it will bring about a
more centralized economy.
But in the micro data that we observe,
we certainly see evidence for the opposite
where there is more new
firm creation happening,
those firms are more likely to succeed
and growth rates overall are improving.
So we're pretty excited.
- Has this changed the kinds of products
that you're building?
Has it changed how you think
about your own product?
- We're thinking about
how are all the agents
and the Claude Code instances,
how are they gonna use Stripe
directly themselves, right?
And both the Stripe product
and just how will they
transact more broadly?
And so we're just thinking
a lot about a world
where most transactions,
agents are the
counterparties on both sides.
And so how does an agent
sign up for Stripe?
How does an agent use
Stripe? Is MCP enough?

[00:17]
What should the Stripe CLI do?
How to make sure that
everything in Stripe can be
orchestrated and conducted from the CLI
or in some other way that
is accessible to agents?
How will agents pay each other?
What currency will they use?
- It's not just agent economy,
but it's like agent to agent economy.
- Yes.
Again, the Stripe house view is that
most transactions will
be between agents within,
call it three years.
It may not be the case that
most of the dollar volume
is directly between agents,
but I'll be sort of surprised
if there isn't just a whirling vortex
of reasonably small
agent to agent payments.
- Patrick, thank you
so much for coming by.
- Thank you for having
me. That's super fun.
- Yeah, that was great.
I think I got to, like, half
the questions. (chuckles)
(bright music)

</details>
