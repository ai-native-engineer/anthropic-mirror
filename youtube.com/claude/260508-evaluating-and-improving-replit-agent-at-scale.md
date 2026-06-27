---
title: "Evaluating and improving Replit Agent at scale"
channel: claude
url: https://www.youtube.com/watch?v=snroDwX1-JU
youtube_id: snroDwX1-JU
published: 2026-05-08
duration: "27:42"
captions: en-orig
---

# Evaluating and improving Replit Agent at scale

[![Evaluating and improving Replit Agent at scale](https://img.youtube.com/vi/snroDwX1-JU/hqdefault.jpg)](https://www.youtube.com/watch?v=snroDwX1-JU)

<details>
<summary>자막: Evaluating and improving Replit Agent at scale (27:42)</summary>

[00:00]
All right. Hi everyone. I'm Mikael Cata
president and head of AI at Replit. And
today I'm going to be talking about our
both evaluating and improving on a daily
basis Replit agent at scale.
And as you know, Replit is a back-coding
platform for knowledge workers. We're
one of the top players in the space and
we've been literally battling with this
problem for the last you know almost 2
years.
The key difference between I would say
back-coding has a very broad definition.
It ranges all the way from being used by
software developers. But in our specific
case is even more of an extreme
definition where you start from just a
natural language specification of what

[00:01]
the user wants and literally nothing
else. So the user expects to go from a
prompt to a working application, but
they don't tell us what kind of
framework they want to use. They don't
write tests. They just expect things to
work after you know our the agent run.
So it means that a lot of the
evaluations and a lot of the ways in
which we've been building agents in the
past especially for software developers
has to fundamentally change.
Now,
how do we track internally the fact that
the agent gets better on a daily basis
and is actually aligned with all with
what our users want?
This is especially challenging because
if you think about it, models are
changing almost constantly and if
anything the pace of evolution is even
faster than it was a year ago. So we are
always sit on shifting grounds. Models
change fast. We have to change our
prompts, system prompts, user prompts
very often, you know, to comply to the
new features that we're building in
product. Of course, the tools

[00:02]
definitions are changing as well. We're
adding more of them, we're simplifying,
and we're shipping constantly. Every
single day we have multiple releases of
wrap agent, which we put in front of,
you know, millions of users.
So, my argument today for this talk will
be that we have to fundamentally rethink
how we do evaluations.
On the left side, you can see how evals
look like for basically, you know, since
since we've been working on AI. Um they
you run your evaluation, you they
produce a single score, and that score
is produced by a human. And what the
human decides based on the score is, my
agent harnesses better than it was
before or it regress, or my model is
better than before, or we should be
doing, you know, more post training.
That's how how we've been doing this,
you know, for a for a long time.
I argue that we should move more and
more towards a continuous setting of
evaluations, where especially when you
actually have something runs in
production, and in our case it generates
millions of traces every day, there is a

[00:03]
lot of hot fat to be extracted from the
traces themselves.
So, what we do is we have a combination
of fine evals, so very similar to sweet
bench and other benchmarks that are very
famous in the space, as well as online
evaluations based on the on the system
usage.
What do we want our evals to capture?
Fundamentally, first of all, they need
to optimize what our users care about,
you know, rather than just telling us if
the agent is editing code correctly.
They should also highlight immediately
what is breaking, and they should inform
us where what we should be shipping next
in terms of improvement for our agent.
What goes into this
box, this black box? So, we're building
a new system that allows us to do these
constant improvements.
The system looks in the following way.
We have two pillars. On one end, we have
the standard old-school benchmarks. They
are usually employed before shipping a
new version of the agent. Think of them

[00:04]
sort of as a boolean flag. It's a
gatekeeper before deciding if you should
be launching a new version or not. So,
if there is a major regression on an
offline benchmark, of course you stop
your release. If you see no changes or
positive changes, you know that you can
go on.
But the part that is more intriguing and
is what is helping us to make constant
progress is the fact that we do a lot of
baby testing and we also cluster all the
traces that we obtain in production and
we try to gain insights from them. So,
in this case,
the online pillar actually works after
you ship a version of the agent and it
forces you to react as fast as possible.
And the loop here is, once I have these
two pillars in place, you reflect on the
results that both of them are giving
you, you likely change the code once
again, run your eval, rinse and repeat.
And this is the cycle that we go we are
going through every single day at
Replit.
I mentioned before SweetBench and I want
to give you a quick understanding why

[00:05]
we work on something, you know, more
powerful than SweetBench or at least
like more tailored towards our use case.
Um something as SweetBench, HumanEval,
they played a key role in our space, you
know, to allow us to air climb them and
make models more powerful. But
eventually, they all follow the same
protocol.
Uh you make sure that the code that is
generated complies with the user prompt,
then you apply the patch on your
repository, you run the test. If the
tests are passing, you know, you you
have a higher score on the benchmark.
This does not reflect what happens in by
coding. As I was mentioning before,
users are not writing the tests. They
often start from a completely empty code
base. So, there is not a scenario where
you can just apply patches. You're
building things from the ground up.
So, what we need to capture in instead
is does the app do what the user asked?
So, there is a functional correctness
gap between what SweetBench provides and
what we were working on.
And today on stage, I'm launching
ByBench. It's a new public benchmark for

[00:06]
back-coding end-to-end that we worked on
at Raptic for several months. I'm going
to give you all the details after the
URL and so forth, but let's start from
the setup of the benchmark. The input is
just a PRD. It's literally like a long
prompt that describes how to build an
application.
Rather than crafting them from synthetic
data, we pick 20 real-world traces from,
you know, usage of Raptic, just plain
English specifications
without any implementation constraints.
Then, we have an harness that builds the
application end-to-end. So, it goes from
an empty repo into something functional.
And then, the key insight is rather than
stopping the benchmark here and then
having humans evaluating the output of
those PRDs, we built automated
evaluators. This is what allows you to
go from a benchmark that you run maybe
on a weekly basis into something that
you can run every single time you
literally have a new PR merge in your
repository. So, of course, as you can

[00:07]
imagine, we have AI running all the
evaluations on our behalf.
The
the setup is the following. There is one
core, and the protocol is you have an
you have a input, you have an
implementation strategy, and then you
have a set of our core, sorry, our wired
evaluations that you run on your app.
And we came up, you know, with five
different pairings, but in reality,
there are a lot more pairings that you
could come up with yourself. The most
basic pairing is the input is the PRD,
and we build the application single shot
zero to one.
Then, maybe in order, you know, to go
from uh less complicated to more
advanced, we have something called by
bond ref or like the reference
implementation where we start from
something is already working and we
build a feature on top of that.
Let's make it more advanced. We have by
bond vibe where we start from an agent
on MVP and then we build a new feature
on top of that. Maybe this is something

[00:08]
that in the X lingo you would call slop
on slop. So if we have something that's
been built by the agent not verified and
then you had more agent code written on
top of that and then you run the
evaluations to see if it's working or
not. You can keep making this
arbitrarily more complex. Uh for example
on in agent four that we launched a
couple of months ago, we completely hide
the complexity of doing task
decomposition and running agents in
parallel and then merging all the
patches together. So
we can also take as an input the PRD, we
do the task decomposition, we run all of
that in parallel and then we run the
valves after that. As you can imagine
the parallel plus merge scenario is far
more uh you know, challenging for a
standard coding agent.
I give you here some more ideas we
describing in the paper, you know, but
you can even start from a buggy
application, build a feature on top of
that and see how much your agent
struggles, you know, to actually make it
make it work correctly.
So the the key question or the
complexity here is how do you actually
do the grading? And that's what I told

[00:09]
you before, you know, was where we spent
most of our effort. It turns out that
when we're working on our previous
version of the agent, we put quite a lot
of effort in building an automated, you
know, app testing feature which
literally doesn't know anything about
the app per se. Cuz if you think about
it, when it comes to web coding, you we
don't give any level of
uh you know, guardrails to our users.
They can decide the language they want
to use. We can decide a different
framework. So the evaluator has to be
totally agnostic on how the
implementation looks like.
And what our evaluator
evaluator agent does is it reads the
code base, it then opens a browser and
points it to the application that our
agent has built and then step-by-step
goes through our testing plan. And even
the testing plan is expressed in natural
language and the actions are like open
the admin dashboard and log in with a
certain account and click on this
toggle. And if any of those steps fails,
then you know, we collect all of them
together and we generate a score. So, we

[00:10]
go through all these test plan and then
we decide ultimately if the score is
good or not. So, this is the key
complexity. When it comes to SweetBench,
we always had a fixed surface. We know
the repositories, we know the task
hardness, we know exactly how to make
this work. In ByBench, the surface is
completely green field and that's why it
took us several months of work to get
there.
Now, as I mentioned, we're announcing it
today. Here's the QR code. You can find
the entire benchmark available open
source on bybench.ai.
I'll let you to dig into the paper. You
know, we
it's going to be presented a couple of
weeks from today at the conference on AI
and energetic systems.
Peter, the you know, lead of the project
and first author of the paper is sitting
here. So, after my talk, please come and
have a chat with him if you want more
details.
I'm just going to give us sneak peek of,
you know, the most notable results
there.
First of all, we are noticing almost a
2x gap between the frontier models and
the open weights models.

[00:11]
And
the reason why I want you to pay
attention there is how I think it
because we know that
every single model player as every
single model builder is hit climbing
specific benchmarks. That's why we
release this open source. I want the
entire community to embrace it across
open weights and closed weights and make
sure that you know, we make progress
overall on by coding as well.
The other one, possibly not very
surprising is most models do a worse job
when extending their own code. So, the
slop on slop or by bomb vibe scenario
that I was describing to you before is
by far the most challenging. And that's
the reason why I always advocate to have
a testing step in between every time you
create a new feature, otherwise you keep
building on shaking foundations and
eventually your vibe coding application
is going to fail.
I'm going to give you back the QR code
later on. But, you know, let let's move
to the to the next step.
We talk about offline eval. I talked to
you about vibe bench, but as you recall

[00:12]
there were like two main pillars that we
care about. And the reason why we also
care about the online one is because
there is a great difference in terms of
volume of signal that we can collect.
So, on the offline or right now we're
working roughly 20 applications. The
reason, by the way, why we made it open
is because we are more than welcoming
contributions from the community. So,
more applications, harder prompts, we
can keep making this benchmark arbitrary
harder so that we make our traffic's
life harder to actually come with over
time.
But,
when it comes to Rabbit Engine instead,
you know, we're we're collecting
millions of sessions every day and
they're very valuable because they
capture what our users actually do on
the platform. And they're completely
unscripted, the agent is always running.
So, how do we distill useful information
out of them?
Well, it turns out that we run a lot of
AB tests. It's basically our way to keep
ourselves honest because vibe bench only
tells us part of the story.

[00:13]
And I invite every agent builder out
there to start to invest on their AB
testing infrastructure as soon as
possible. It's the best way in which you
can make steady progress.
Now, we ask a wide variety of questions
for ourselves. So, we we built a lot of
different instrumentation and metric in
our agent so that for instance, we can
find out is there a normal span ongoing
or is the agent running for longer than
expected? Or we constantly keep track of
the user sentiment. It's it's a very
easy thing of to collect because every
time you receive a prompt, you can do
sentiment analysis on it and then
receive the user is getting frustrated
or not. And last but not least, this is
very idiosyncratic to Rapid. Our users
can also publish their application on
our product. So, it's a very strong
positive signal if they decide that
whatever they built is worth to share
with their colleagues or to put it in
public in front of everyone. So, all
these signals clustered together gives
us something like this. If you have ever
done an AB test in your life, I'm sure

[00:14]
this looks familiar.
And
it might look familiar especially
because not everything is either green
or red. This is the, you know, hard
harsh truth about running an AB test.
They never give you a crystal clear
signal of what you should be doing. So,
in this case for example, uh the average
run duration of our agent, you know,
went up by 7% but conversely is 8%
cheaper and we saw the fluctuation in
terms of positive and negative
sentiment.
What shall we do in this case? This is
where human taste and product philosophy
still plays a key role. You will never
get or very rarely do we get like a
crystal clear configuration of the
results of your AB test.
And
to make our life a bit easier on how to
generate these AB test candidates, what
we do is we cluster all the traces that
we receive every single day and night as
you can imagine and we try to identify
first of all, which cluster are

[00:15]
capturing normal nominal behavior of the
agent. And as you can imagine, there are
plenty of them because the vast majority
of times the application is actually
successful but of course there is a long
tail of problem that it happens to
surface.
In case we find a problematic cluster,
then what do we do? We embed all the
failure summaries.
We
we cluster them by type so that we find
out the different failures that are
happening at a certain point in time.
Then we pass them through an LLM to
classify exactly what is going on. And
the fact that we do this
not based on regex on logs or like very
deterministic techniques is what
actually makes a difference because you
will be able to cluster things that are
semantically close to each other even
though the agent doesn't give you always
the same type of output.
And you know, once once we find these
uh cluster configurations, we are forced
to retrain them every single night
because we are running several versions
of the engine in parallel. We ship many
versions every single day, so we can't

[00:16]
live with a fixed cluster configuration.
And aside, you know, from also helping
us to identify the failure modes,
another interesting feature is the fact
that once we retrain those clusters, we
can go back and see if after we believe
we fixed a problem, a certain cluster is
actually disappeared. So, say you have a
certain tool failure that is happening
only a limited amount of time. So, not
something that will show up in your
DataDog dashboard, for example, not a
failure that happens 50% of the times,
but maybe it was happening 1% of the
times in certain specific conditions.
And from here, you will start to
realize, okay, I shipped my new PR and
that cluster is disappeared. So, you
start to have some evidence that you
mitigated the problem.
The
The technology that we built internally
was called Telescope and it's a fairly
simple loop, I hope, after I explain
everything. Uh first of all, we start by

[00:17]
discovering the problems. And this is
based on the trace clustering that I was
talking about before.
Then, based on that, we create code
changes. So, it's completely automated.
We basically cut PRs with a coding agent
based on the information we got from the
trace, based on information we collected
from the logs, from all the different
different dashboards that we had.
Then we evaluate if the change we
generated, first of all, is is is a
breaking change. So, we rerun by bench.
By bench is kind of like a litmus test.
If the score drops by 10 points, we
decide that the change is bad.
If it's a controversial change that we
believe could affect also negatively our
agent, we run an AB test. So, we put it
in front of the users and we try to find
out what are the trade-offs. If it's a
clear sure shot, then we just ship it in
production.
And
few times when we believe that the
hypothesis was correct and maybe the PR
was not perfect, we keep iterating on
the problem. Maybe maybe we run another

[00:18]
AB test until we are in a good
configuration and then we actually ship
it.
If you think about it, this is very
similar to the work you do as an AI
engineer all the time, but 90% of it is
now aided by an agent in the loop, you
know, rather than you having to sweat
about every single step of the process.
Let me give you all an example of, you
know, what we actually experienced, you
know, once in production.
Um
Rabbit Agent immediately starts an
execution environment the first time you
submit a prompt. And of course, to set
up everything, especially with the level
of complexity we built, requires, you
know, quite a few seconds.
We had a degradation in the long tail
where our, you know, setup time was
longer than expected and our agent was
ready to roll before the environment was
fully set up.
As you know, agents have become really
eager to fix problems. So, Rabbit Agent
went on a tangent and started to try to
fix the environment, you know, on the
spot. Um
it turns out that by the nature of
agents not being deterministic, every

[00:19]
single debugging session looked a bit
different. So, if it tried to find out
this long tail problem just by grabbing
the logs, it would have almost not
appeared.
But the moment we cluster all the
traces, you know, with basically with we
we through the semantic layer, then we
started to figure out that this problem
was happening quite often, and we
immediately able to create a patch and
fix the issue. In this case, we didn't
have to run an AB test because it was a
pure regression case. But in case it was
a problem that required testing, of
course, we would have put an additional
step in between.
And even though I'm a big fan of
trying to optimize as much as possible
the life of an AI engineer with agents,
I do think that there is a lot of
intellectual work to be done by humans
still in the kind of loop that I
presented to you.
For example, whenever we find one of
these clusters that I was talking about
before, as a team, we always focus on

[00:20]
formulating an hypothesis on what could
be possibly go wrong there. Cuz the
truth is when running in production,
you're going to get a really a large
amount of candidates of what you could
be fixing. So, you need to prioritize
where you put effort, where you put
resources. So, if the hypothesis is
intriguing enough, then we move forward,
and we don't just let the agent write a
PR without any kind of supervision. We
actually try to feed some of our
understanding of what is wrong. So, we
give it more guidance.
And ultimately, if you think about it,
every single time we decide of working
on a PR and doing an AB test, we're sort
of like shaping the hill that we try to
optimize. Cuz if we only care about,
say, making the product more affordable,
we're going to go and try to fix all the
anomalous spend problems, and then we're
going to do our best to optimize that as
much as possible. So,
all these choices really determine the
product philosophy of what you want to
put in front of our users. And then,
last but not least, as I was showing you
before on the AB test dashboard, if

[00:21]
there is not a clear result, ultimately,
if you decide to launch or not, is still
a choice that a human does. Often times,
that's that's on me in the rabbit. And
again, that determines really what's
going to be the ultimate product
experience.
So, my In closing, what I want you to
have as a takeaway today is don't think
of evaluation just as this last check
before shipping. It shouldn't be just a
boolean flag, but rather think of this
as an engine that allows you to ship a
better agent every single day.
Thanks, everyone. And
I'm going to invite Hannah on stage so
we can have a chat about how we've been
working together in the last few months
to go. Thank you.
>> [applause]
>> Awesome. So, my name is Hannah. I'm part
of the Applied AI team at Anthropic, and
I work with Michele
on the Replit agent and on everything
that they build with Claude. So, I want
to ask you a few questions about what
you built here. My first question is

[00:22]
Vibez is something that we've seen a
couple times. You've used it with us to
give us feedback on research models that
we're testing. But, what was was your
vision from the beginning to make
something that you were going to open
source and make available to the
community? I think a lot of people may
be trying to build evals like this for
themselves where they see holes in the
public benchmarks, but I think this is
kind of a unique approach, and I'm just
wondering if you could talk about that a
little bit.
Yeah, I've been asked this often, why
don't you keep this as a private appeal
of your company? Fundamentally, I
believe that
we should try to give back as much as
possible to the community. And we all
have to benefit from creating public
evals. It helps you to make better
models. It helps us to make a better
agent. It helps everyone to create
better products. And I I don't believe
in competing on evaluations. I come from
a research background where everything
should be open.
So, we'll we'll keep doing this for as
long as we can in Replit. And And again,
I I really invite people to collaborate
on Vibez. I I tried to instill this idea
in the community several times when I

[00:23]
was giving talks in the past and at a
certain point I realized we have to
build it ourselves rather than just
trying to invite others to do it. Mhm.
Well, I'm really excited to see what
people do with that. Um
I also want to ask you about the second
pillar, telescope. This is um you know,
a pretty sophisticated system that
you've built. It sounds incredibly
useful. It sounds like something you've
tuned quite a lot over time.
For people in the room who might be
trying to build something similar like
this, what lessons did you learn along
the way? What kind of tips could you
give them about how they can build
something useful like this?
So, first of all, if you try to do this
even, I don't know, 6 months ago and you
got discouraged because you didn't get
like a return on your investment, uh
definitely try it try it again. The same
inflection point that you experienced
with coding agents back say in November
with Opus 4.5 and and similar frontier
technology, uh it also reflects to what
I just talked about now. So, the the

[00:24]
fact that long context and models that
are really capable of reasoning on a lot
of content means that you can
practically inject an entire trace of
your agent into Opus and get fairly
sophisticated feedback about it. Um so,
you at the same time you should really
be investing in collecting all the
signal that you can from your agent and
as well as you know, the environment
where you're executing it. So, I know
that I I had to run fast during the
talk, you know, but I couldn't go in
depth on all the different signals that
we bring into telescope. It is not
purely
what's coming from the trace, it's also
the feedback that we collect in product.
Like we have a feedback form, so every
time the agent doesn't behave correctly
and the user complains, we have the user
point of view, we have the trace of the
agent, we have everything we instrument
in the platform in DataDog.
Unsurprisingly, all of that together,
put, you know, in context, helps even
more to pinpoint where where the issues.
Yeah, I think that idea of building the

[00:25]
clusters, like you were saying that a
single trace, it's very hard to debug
what might be going wrong there, but
when you are able to group them all
together and get these other signals in,
really reveals a lot more information
and something actionable. Makes a ton of
sense. Yeah, it does and I think it also
makes the life of an agent builder less
overwhelming because it really is when
you start to get a lot of usage, the
amount of feedback you receive is
actually overwhelming. And it's a good
It's a good signal. It means that people
care about what you're doing, but at the
same time it's hard to prioritize what's
actually important versus what doesn't
move the needle.
What I showed today is also a way for us
to try to understand, okay, this cluster
keeps showing on a daily basis and it's
fairly large and it has a lot of volume,
so we should actually fix that first of
all and then there is the long tail of
problems to fix will always be there
with agents given the fact that they're
non-deterministic. Yeah, that really
makes me think about the third thing I
wanted to ask you, which is what you
said about taste.
Uh, I think this is really interesting
point um that the taste of the AI

[00:26]
engineer is very important and could you
talk about how your team develops that
taste? Have you always had this taste or
have you improved your taste over time?
Like what's the process of building that
and developing that for people who might
be trying to build their own taste?
I think we all brewed it over time
because you know, when we launched
these, you know, was more than a year
and a half ago, agents were way less
powerful than they are today.
Uh, maybe not much taste to be applied.
It was more like a survival game just to
make sure it was barely functional. And
now that they're becoming so powerful
and you have such a wide variety of
choices you can make, um then you you
start to develop a taste that should
really be in tune with your actual user
base. Like if if you're building an
agent for software developers, maybe 80%
of the choices that we make every day in
the team will be almost the polar
opposite of what we do.
And you always want to keep in mind that
it's being used by personal likeness
different from you. Especially in our
case, like everyone at Rabbit is very

[00:27]
technical and we are giving the product
to knowledge workers who have never
written a single line of code.
So, it's a it's a very good trade-off to
to learn.
Awesome. Thank you for sharing that.
I'm sure people are going to have lots
of questions for you and for Peter, who
is one of the authors of Vibrent. So,
everyone please come find them and thank
you so much for coming for
>> Thank you.
Have a good one.

</details>
