---
title: "How Spotify runs agents across 20M+ lines of code, with Niklas Gustavsson"
channel: claude
url: https://www.youtube.com/watch?v=9DHZLw5653E
youtube_id: 9DHZLw5653E
published: 2026-06-29
duration: "26:11"
captions: en-orig
---

# How Spotify runs agents across 20M+ lines of code, with Niklas Gustavsson

[![How Spotify runs agents across 20M+ lines of code, with Niklas Gustavsson](https://img.youtube.com/vi/9DHZLw5653E/hqdefault.jpg)](https://www.youtube.com/watch?v=9DHZLw5653E)

<details>
<summary>자막: How Spotify runs agents across 20M+ lines of code, with Niklas Gustavsson (26:11)</summary>

[00:00]
[music]
I actually remember talking to you back
in I think September last year and you
said something like, "Yeah, I don't
think at the end of the year no one is
going to be using an ID." And in my head
I was thinking like that's crazy. That's
never going to happen. Like I I could
imagine that happening on a 2-year time
frame, something like that. But 2 months
seemed extreme. And then 2 months later,
I found myself not using an ID anymore.
And like the the way that I was working
had completely changed. It changed that
I had not seen in the 30 years that I've
been doing this type of work.
>> It's funny. Internally, it felt exactly
the same way that it did externally.
>> Okay.
>> But, you know, we had a head start of
like a few weeks.
>> Yeah.
>> That that was it. But it felt exactly
the same way. So okay here I I wanted to
start with how did you get into coding?
>> My formal background is actually in
biology. So I'm a molecular biologist by

[00:01]
training and in that area when I was
doing my PhD studies um we started
having what was then considered big
data. So we had a lot of data from um
genome sequencing. So I felt that I
needed to improve my ability to do
programming essentially. So I switched
over what was intended to be a sbatical
year ended up being I guess now close to
30 years of being in this in this
industry.
>> So fast forward to today with with all
the change right now with with agents
and LLM. I feel like your personal usage
and Spotify's usage is on the frontier
of what I see in the industry. [snorts]
What was what was your first feel the
AGI moment personally? I think I have a
I've had a few depending on a little bit
of the problem that we were trying to
solve. We started pretty early as LLMs
came about to try to use them to
automate code changes and that was a
real struggle to begin with. But after a
while as we started figuring out like

[00:02]
how we can use LLMs and judges and
whatnot, we started getting some pretty
uh inspiring results from that.
>> And this this was like a few years ago.
Yeah, it was pre pre-claw and pre it was
like early GPT days something like that
and again like the results we got then
wasn't like we can fix all our problems
but it it was giving an insight of like
where this is heading in the future. So
that was certainly one for I have to say
for my own
personal coding the real breakthrough
moment was probably Opus 4 or 5 back in
November December. It went from being
this like smart autocomplete to
something that I could actually throw
real problems at and I didn't have to do
all that much prompt engineering. The
biggest thing for me was also just not
having to edit code anymore cuz my
workflow up to then was I have the model
write you know like maybe 80% of the
code or 70% of the code depending on the
model and then I always had to go into
an IDE to do the last mile edits

[00:03]
>> and I just stopped having to do that.
>> Right.
>> And that was that was crazy.
>> Yeah. Um, but yeah, that I think that's
a big part of the reason that it felt
like such a leap. What's your So, what's
your workflow like today? Like how how
do you use Quad Code? How does Spotify
use Quad Code?
>> Yes, I use it in a I'm going to say
fairly vanilla way. I think I run it in
a bunch of T-Max uh sessions in a in a
terminal. Um, usually have a bunch of
agents running in the background
whenever I do some some work. Um,
>> how many terminal tabs? So I will have
anything in between five and 10 tabs. Uh
and then I use some panes because I like
to have a terminal that where I can
actually like get diff and whatnot. Um
so I have this set up with a matrix of
claw sessions and ter and m matching
terminals in a in a set of uh work trees
that I work in. The way that we're set
up is that we have a uh a few very large
monor repos which we're gradually moving
towards but we still have thousands of

[00:04]
small poly repos for that that remains.
So I'm most of my work happens in those
uh monor repos. So I usually have a few
clouds and terminals going on there at
any g given point in time and then when
I need to dip into one of our poly repos
I will open up a more temporary claude
session there. Do do you feel like one
like monor repo or poly repo is a better
fit for for quad or
>> I was a bit worried to be honest about
the monor repo setup and agents
originally because um I think with some
of the prior tools we've been using
we've been seeing issues with indexing
and things like that um and this these
are fairly large repositories that our
backend monor repo is more than 20
million lines of code but turns out it
cla works amazingly well in those
repositories and Um, I think one of the
things we found is how good Claude is
looking at other code in the repository
to get, I guess, inspiration for the
problem you're trying to solve.
>> Um, I I wanted to ask about some of the

[00:05]
infra that that you built.
>> So, you know, at at Spotify, obviously
you built Honk. Yep. I feel like from
the earliest days of experimenting with
models to building honk and building
background agents on you know on the
agent SDK.
>> Y
>> you see the future before other people
do. What what is it about the the
culture or the people working on it that
kind of leads to this and just tell me
that story and how how has it been
going? five six years ago now um we
identified that our code base was
growing much much faster than the number
of engineers we had to support like
seven times faster. So that meant that
over time we just had more and more code
that we needed to maintain. Uh and
Spotify is a company that has an endless
source of ideas of things we want to
ship to our users. So being bogged down
by our maintenance was not a good place
to be in. So we started automating
trying to automate as much of that
maintenance as possible. A lot of that
was pretty dull work like migrating to

[00:06]
the latest Java version or library
update or whatever. Uh a lot of it was
moving from some API to some other API
across uh all our code. Um so we built
out this infrastructure that we call
fleet management which all about like
instead of imagining before that when we
were doing a migration we would send out
the migration description or like um
tutorial to all our teams and ask them
to do that migration manually for all of
their components. And instead of doing
that, we imagine like can we find ways
where we can do mutations towards our
entire codebase instead living in
thousands of repositories
>> because every every team was kind of
doing the same thing.
>> Yeah. Yeah. Hundreds of teams doing the
same operation manually over thousands
of components. So each of these
migrations took months and months and
months to complete. We could maybe do 10
of them a year. we were barely keeping
up with um being on the supported
version of the frameworks that we're on.

[00:07]
So again, we started automating this. We
built out all of this infrastructure to
do this. We've merged millions and
millions of those types of PRs and but
they all relied on
these like deterministic scripts that
you would apply and that would make
those code changes or configuration
changes. And one of the things we found
pretty early was code has an enormous
API surface. So trying to make changes
to code gets very complicated very
quickly. So we pretty quickly ran into a
ceiling of
how complex changes we can do even
even switching out the method and API
becomes pretty complicated when you can
call that in five different ways.
>> So so doing with this with just
traditional like static analysis like as
transformation.
>> Exactly. Yeah,
>> because like let's say there's an API
you just like you a it to a variable or
something. Now now you need kind of like
variable and state tracking.
>> That's exactly right. That's messy.
>> Yeah. So each script that we had to
migrate code turned into thousands of
lines of taking care of every edge case
in that code.
So that inspired us as I mentioned

[00:08]
before as pretty much as soon as the
early LLMs came along of like hey these
things can we apply them to this problem
and early on it didn't work at all all
that well. Uh partially because the
models weren't good enough partially
because we just we were very naive in
how we were trying to do it. We
basically just put the code in front of
the model and try to get it to one shot
that that change. So that didn't work.
Over time models improved and our
thinking about how to do this improved.
So we started applying LMS as judge to
make sure that the output was as
intended. We started breaking down the
problem, decomposing the problem in
various ways. So many many many
iterations of this uh and many internal
hacks to try to take on this problem in
different ways. Uh we started
consolidating that and that then became
what we now call honk. Um it was a very
different beast originally. It was not
on top of claude. Um it was more a bunch

[00:09]
of homegrown type of things in there.
But it was the first sort of light in
the tunnel of like yeah this is actually
a problem that we can solve. And then
we've done many many iterations on on
Honia. So today we we released what we
call V2 but I think in reality it's V8
or something like that. we just didn't
keep track of the of the iterations we
did on it and it started out as this
like automate these code changes
schedule that and orchestrate over all
our repositories but pretty quickly
engineers figured out that hey this is
useful for other things as well I want
to
mention this thing on Slack and have it
do a task for me or or all of those
types of things. So today honk is has
grown into being a much more ubiquitous
tool for us.
>> Tell me about the architecture of Honk
like how what are the big pieces? So you
talked about having uh there there's a
there's the agent that codes and this
this is just built on the quad agent
SDK.
>> Yes.
>> Um and then you also have you have a
verification step like a agentic

[00:10]
verifier. Tell me more about that.
>> So we used to have a judge in honk but
we actually have removed that because we
found that the
uh agent and models just again going
back to four or five got good enough
that we don't didn't need judge anymore.
>> The judge was very important in the
first iterations of honk. It it made us
go from if I remember the numbers
correctly like roughly like 20 30%
success rate on PRs to like 80% success
rate. So
>> so it's a big big change but then again
as we talked about the models caught up
and and the agent hardness caught up so
we have now eliminated that judge from
from honk. So honk architecturally is
fairly simple. So it's the agent SDK
running in a kubernetes pod. Um it has
access to a set of uh tools. Um it used
to be prior to V2 that those tools were
a predefined allow listed set of tools
that we trusted to give to that agent.

[00:11]
Now in V2 um users can add their own
tools just off those tools. So now the
agent can use any of our internal tools
and one of the most important tools that
it has access to is that it can run
verification like basically run CI
builds. Um and it can run those both on
Linux and Mac OS. So Mac OS is
particularly important to us because any
iOS development for example needs Mac OS
builds. Mhm. And is is this just
building or are you doing like a full
like open up the iOS simulator, have the
model like start the app kind of how how
deep does it go?
>> It it can do those types of tests. We
definitely have cases where we integrate
the simulator and claude to automate
things like going directly from uh
designs and Figma to UI implementations
>> and we've been using that for porting
for example our TV apps from from our

[00:12]
iOS apps.
>> I I feel like verification is it's one
of these things that we talk about a
lot.
>> Yeah. But I but I think when you're
doing this kind of closed loop
development where it's an agent that
it's given a task and then it has to
maybe like fin out and break down the
task and it just needs to do a lot of
work without a human in the loop.
>> Yes.
>> It it's just the single most important
thing.
>> Yeah.
>> And I I feel like one of the common
mistakes I see is companies underinvest
in how well that verification loop
works.
>> I think that's very true and I think
it's true for us as well. One of the
major changes that we did in our in our
engineering practices as part of that
was to strengthen our test automation.
We have divided our code base into many
thousands of components. Each of those
components have uh uh well- definfined
ownership. So it's owned by a particular
team and that team is fully responsible
for that. They probably designed it
originally. They implemented it and they
operate it. And part of that prior to
the investments we did in fleet
management was around like the that team

[00:13]
was in the loop for every change that
got merged to their their code base. Uh
and that mean that that meant that in
some case we could be a bit sloppy on
post test automation because that team
could always check every PR if they
needed to. But with starting to automate
PRs towards our source code, one of the
things was we needed to change the
expectations for teams. like you might
not no longer be in the loop for for
these changes. We're going to be
automerging most of these changes uh
without you ever seeing the PR. So that
meant then having to build out much
better test automation to make sure that
uh [snorts] all our software could sort
of survive those types of automated
changes.
Now zooming into where we are today,
that's been very very helpful for us
because now we can throw agents at that
and use the same uh verification that we
had in place before.
>> There's one of these trade-offs that
people talk about all the time in
engineering of uh reliability and
quality on one side and speed on on the
other side.
>> Y

[00:14]
>> and to to me it feels kind of like a
false dichotomy because if you want to
go faster, the thing that you need to do
is you need to automate your quality
practices so that it's better encoded.
It's not in someone's head. It's it's
actually like in a skill or in a quad MD
or in some set of MCPS. It's something
that quad can do.
>> Y
>> and that's ultimately what lets you go
faster. And this is just another example
of how in engineering productivity is
always about investing in
infrastructure. It's not about working
more hours. It's about just making the
infrastructure better and better. And
that sounds like what you're talking
about.
>> We're seeing that we're keeping our
quality metrics neutral while
significantly improving our our speed.
Um but that has not come for free. We
we've needed to to make these
investments into into test automation
that we as we talked about. Um I think
we we're going to have to continue our
investments into uh our reliability
practices as well. Some of those are
changing as part of this this transition
as well.
>> And and I guess as you try to go kind of
faster and faster and faster, you have

[00:15]
to invest even more in reliability just
to keep
>> Yes, that's exactly right. So yeah, so
we make something like 4 and a half
thousand production deployments every
day.
>> Uh so there's a lot of opportunity for
things to go wrong. Uh so yeah, we need
to have good practices around making
sure that everything that ships into
production has the the quality that we
want.
>> What's the idea with doing this many
deployments? Is it kind of in the past
it was just continuous deployment and
now maybe it's faster signal for the
agent or how how are you thinking about
it?
>> This is something we've always been
optimizing for for as long as Polify
existed. I think we we want to be able
to basically have an idea and for a
developer to have an idea and be able to
ship that into production as quickly as
possible. That used to be weeks or
months back back um back a few years and
we've uh continued to try to optimize
that and now it's you know an hour or
something like that. Like as I mentioned
before, we have lots of ideas. We want
to validate and explore those ideas. And

[00:16]
[snorts] the faster we can get feedback
on that. And in some cases, that might
be feedback from our internal users. In
some cases, might be feedback from our
uh external users. But in both of those
cases, the faster we can iterate, we
found that we um we both build better
products and we're able to ship them
faster to our users. Not every idea ship
in an hour. many ideas takes, you know,
lots of exploration before we're able to
ship them. But, but the notion of being
able to
um get that quick validation is super
important to us. And yeah, agents are
certainly part of that loop as well.
>> So, for Spotify, the the engineering org
is fairly big. It's like thousands of
engineers, right?
>> Yeah, it's 2,900
engineers, something engineers. How how
do you think about as as you do all this
stuff? How do you think about ROI? Uh
like measurements, just making sure
you're moving in the right direction.
>> In terms of measuring ROI, like we've
been it's been easy and we've seen very

[00:17]
um clear signals in that space. We're
seeing a 75% plus improvement in PR
frequency, for example, uh that we can
directly attribute to AI tooling. And I
think by now 73ish
percent of PRs are directly attributed
to being AI authored. Um
so those types of metrics we're doing
pretty well on. But then of course we
want to connect that to user value and
revenue.
>> And how do you how do you measure
something like that? Is it sort of a
like AB tests or some kind of hold out
like case studies? Like how how are you
thinking?
>> Yeah. We want to connect basically be
able to connect the deliverables that
the engineer engineers do. So PRs,
deployments into we call them work
items. So basically like the the planned
work that we have and then that connects
to uh AB tests and rollouts and then
we're able to from that see like
[snorts] basically attribute back to say
this PR contributed to this uh uh DoD

[00:18]
that we have and that contributed to
this user value. That's the idea and
we're trying to build those connections
right now.
>> Yeah. I I feel like back in the day, you
know, like we we've worked in developer
productivity for a while. Like when you
have a big team, you want to make them
more productive.
>> Yep.
>> And I I feel like back in the day, a big
win was it was like a few percentage
point.
>> Exactly. Exactly. If you were lucky
enough to be able to measure that.
>> Yes.
>> And like with with the improvements
nowadays, it's just so obvious to
everyone. Yet, you know, as engineers,
we still want to measure it.
>> Yeah. I'm going to say like the ROI
discussion initially was fairly
easy because we could see such large
improvements and um but as the
maturity is getting there and the costs
have been improving. I think the
precision around those ROI estimates the
expectations on the precision is going
up as well.
>> So that's why we're trying to improve
how we can how we can do that type of

[00:19]
measurement. Part of it is about the
improvement in productivity and then
part of it is how much does it cost to
get that improvement.
>> That's exactly right.
>> And now you know people are seeing these
like many dozens or hundreds of
percentage points of improvement and now
you really want to attribute it to
figure out like how many tokens did it
take? How many hours did it take? What
was the productive output?
>> Yeah, that's exactly right.
>> Um I want to end on uh maybe one
question. What what advice would you
give your peers? What advice would you
give to to other CTOs and you know
engineering leaders like VPs of
engineering at at other companies?
>> What we've found is that these
investments in foundational capabilities
we talked about test automation and
verification. I'm going to say the same
is true for uh or another aspect that
we've seen is uh standardization. So
we've been driving you know more
consistent code bases more alignment on
the tools that we use the um frameworks
that we use and we've seen that this was

[00:20]
originally investment we did to simplify
things for humans and make humans more
productive but we've seen the same thing
transition really well to agents as
well. So if you have uh I mentioned this
before on claude being able to find
inspiration from other pieces of code in
our monor repos if they look in 10
different ways claude is going to be
more confused. So we've been seeing the
more consistency we have the more the
better our agents work. So I think if if
there's one advice I would give would be
to not not ignore those types of
investments. You need to have the same
the same sane engineering practices that
we had before still applies in this new
world. Might look different. The there's
a new actor being in your codebase, but
the fundamental seems to apply equally
well. At least that's been the case in
our in our environment.
>> What's your advice for engineers that
you know maybe have been doing
engineering work for a while? And I know
Spotify has talked about engineers, you

[00:21]
know, like shipping PRs on the subway,
>> which is which is really cool. So, you
know, obviously engineering is changing.
What what's your advice to everyone
that's that's in the middle of it and,
you know, trying to figure it out?
>> Yeah, let me talk about this from a more
personal angle, I think. So, I'm someone
who's always have truly enjoyed the
problem solving part of coding. This is
going to sound as nerdy as it is, but
like in my spare time, I will do like
competitive programming at times because
it's just like fun mental exercise. In
the back of my head, I was always a bit
worried like we were talking about
before of like how this was change
completely changing the way we were
working and I was pretty worried about
that from just my personal point of view
like am I going to miss that part of
like the hard mental challenge of
solving problems and now I find myself
having you know five agents working in
the background and my way of interacting
with them is very different from the way
that I was working a year or two ago and
for me that's um turned out that I was

[00:22]
wrong and I like the the thing that I
like to do is solving problems and the
way that I solve those problems turn out
to not be the most critical piece for
me. This is always going to be personal
for for different people are going to
have to make that transition in in
different ways. But I think focus on the
types of problems that you're able to
solve. Um I'm I find myself both to be
more productive in that I can bring more
value from the work that I did can do. I
can also solve problems that I really
couldn't solve before. I can jump into
code bases that I that would have taken
me days or weeks to get into before and
be be contributing things that I just
could not do before. So for me that's
been
amazing. Um, and again, it's going to
look different for different people, but
I think give it a shot and find a way
that you you can use those tools in the
way that you like.
>> I feel like for me, I've seen this big
shift from implementation time cuz now,

[00:23]
you know, Claude does it in the in the
background while I do other stuff.
>> And instead, what's filled up that time
for me is thinking about what's next,
talking to customers,
>> and also like actually much more
prototyping than I expected. And some of
it is for external products, some of it
is for internal automations. How how has
that shift? How how's that change looked
for you?
>> I think it's been similar for me. And
yeah, we didn't talk about this, but one
thing that we're
making a big investment in is is
prototyping in particular. Um, and this
is targeted both towards I'm going to
say engineers, but also the
non-engineering cohort. One of the
things that Claude and Similar tools has
unlocked is to allow anyone to take
their idea whatever that idea is express
that in natural language and have Claude
then go implement that. So, as we as
folks started figuring this out,
including again non-engineers, um they

[00:24]
started trying to do this in our real uh
apps and they're pretty complex beasts
of code. Uh but they were starting to
see again like signs of light that they
could do it. So, we started a few months
ago, we um basically built out the
infrastructure to make that simple. M
>> so today we have a very simple way of
getting going to build an end toend
prototype in our uh mobile apps and our
back end and we have an internal app
store for those prototypes where you can
share them and like take a look at
someone else try out someone else's
prototype in your um your app
>> and that's been a real unlock for folks
that maybe before and again including
engineers that maybe weren't super
familiar with how to build something in
our mobile apps
>> to be able to express ideas that used to
make, you know, motivating a bunch of
engineers to try to build that for you.
And now you can go in and with the
within an hour or two, you have a
working prototype that you can start
sharing with people to show what that

[00:25]
actual idea looks like in real life with
users, real data, and and so on. So,
yeah, those types of things are were
unimaginable a year ago, and now we're
doing them every day.
>> Yeah, I I love that. Have have you seen
it have you seen a shift in who's
producing this? Is it is it like
engineers doing it? Is it mostly coming
coming from designers and product
managers? How has that changed?
>> It's everyone up to our one of our
co-CEOs uh have uh prototypes in that
app store at the moment. So it's
actually been
>> is it good? Uh yeah yeah yeah there's a
bunch of uh like our senior exxs have
have built prototypes that are good like
again like ideas that they already
always had in the back of their head
they have an entire engineering team
that could build that out but that team
is focused on other things. So for them
to then be able to try something out
more quickly than they could before and
you know get a touch and feel for what
this thing is going to look like. Yeah.

[00:26]
allows you to test out an idea in in a
day instead of
>> weeks or months.
>> Nicholas, thank you so much.
>> [music]

</details>
