<!-- source: https://claude.com/customers/spotify-boris-office-hours -->

Q&A | Spotify

# Office Hours: Asynchronous coding and the end of the IDE with Spotify

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Office Hours with Boris Cherny

[Office Hours with Boris Cherny](https://claude.com/office-hours)Office Hours with Boris Cherny

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7cbcd161e079777f192c2f_26-115-CustomerConvo-Spotify-THUMBNAIL-04.jpg)

Office Hours with Boris Cherny

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7ceba17e3c474c1e3f0fde_og_office-hours.webp)

The best engineering teams are rethinking how they work with AI. Boris Cherny talks with technical leaders to uncover what's changing for their teams, from how they’re building with Claude Code to organization design, and the shifting workflows that come with it.

Read more

[Read more](https://claude.com/office-hours)Read more

Office Hours with Boris Cherny

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

The best engineering teams are rethinking how they work with AI. Boris Cherny talks with technical leaders to uncover what's changing for their teams, from how they’re building with Claude Code to organization design, and the shifting workflows that come with it.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Office Hours with Boris Cherny

The best engineering teams are rethinking how they work with AI. Boris Cherny talks with technical leaders to uncover what's changing for their teams, from how they’re building with Claude Code to organization design, and the shifting workflows that come with it.

[Prev](#)Prev

[Next](#)Next

At [Spotify](https://www.youtube.com/watch?v=9DHZLw5653E&t=34s), 73% of pull requests are now AI-authored, and anyone with an idea can have a working prototype in an hour or two. Boris Cherny sat down with Chief Architect and VP of Engineering Niklas Gustavsson to talk about life after the IDE, throwing agents at 20 million lines of code, and why the fundamentals still apply.

<!-- yt-inline:9DHZLw5653E -->
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


### Read the full transcript:

**Boris Cherny, Creator of Claude Code, Anthropic:** Niklas, thanks for joining me for this conversation. I wanted to start with: how did you get into coding?

**Niklas Gustavsson, Chief Architect and VP of Engineering, Spotify:** My formal background is actually in biology, so I’m a molecular biologist by training. In that area, when I was doing my PhD studies, we started having what was then considered big data. We had a lot of data from genome sequencing. So I felt that I needed to improve my ability to do programming essentially. So I switched over — what was intended to be a sabbatical year ended up being, I guess, now close to 30 years of being in this industry. That then led into working primarily with backend distributed systems type of engineering for a bunch of companies around where I live, and then joined Spotify in 2011. And yeah, I’ve been there since then.

**Boris:** So fast forward to today, with all the change right now with agents and LLMs, I feel like your personal usage—and Spotify’s usage—is on the frontier of what I see in the industry. What was your first “fueled AGI moment” personally?

**Niklas:** I think I have had a few, depending a little bit on the problem that we were trying to solve. We started pretty early as LLMs came about to try to use them to automate code changes, and that was a real struggle to begin with. But after a while, as we started figuring out how we can use LLMs and judges and whatnot, we started getting some pretty inspiring results from that.

**Boris:** And this was like a few years ago. **Niklas:** It was pre-Claude. It was like early GPT days, something like that. We were struggling. But after a while we started figuring out how to tack pieces together. And yeah, that was super inspiring. And again, the results we got then weren’t like—we can fix all our problems—but it was giving an insight of where this is heading in the future. So that was certainly one. For my own personal coding, the real breakthrough moment was probably Opus 4.5, back in November/December. It went from being this smart autocomplete to something that I could actually throw real problems at. And I didn’t have to do all that much prompt engineering. It was just: tell it roughly what I wanted it to do, and it was able to do a pretty damn good job at it.

**Boris:** It felt like a pretty fast shift.

**Niklas:** Yeah, I actually remember talking to you back in, I think, September last year, and you said something like, “I don’t think at the end of the year anyone is going to be using an IDE.” And I didn’t say this out loud, but in my head I was thinking—that’s crazy. That’s never going to happen. I could imagine that happening on maybe a two year timeframe, something like that. But two months seemed a little bit extreme. And then two months later I found myself not using an IDE anymore. And the way that I was working had completely changed. A change that I had not seen in, again, the 30 years that I’ve been doing this. **Boris:** The biggest thing for me was also just not having to edit code anymore. My workflow up to then was — I have the model write, like, maybe 80% of the code or 70% of the code depending on the model. And then I always had to go into an IDE to do the last mile edits, and I just stopped having to do that. And that was crazy. Yeah. But I think that’s a big part of the reason that it felt like such a— **Niklas:** Yeah, it completely inverted the way I work. It’s been very initially strange. But now it feels very strange to go back.

“I found myself not using an IDE anymore. The way that I was working had completely changed. A change that I had not seen in the 30 years that I've been doing this type of work.”

Niklas Gustavsson

Chief Architect and VP of Engineering, Spotify

**Boris:** I think that’s right. What’s your workflow like today? How do you use Claude Code? How does Spotify use Claude Code? **‍
Niklas:** I use it in a—I’m going to say fairly vanilla way. I run it in a bunch of Max sessions in a terminal, usually have a bunch of agents running in the background whenever I do some work.

**Boris:** How many terminal tabs?

‍**Niklas:** I will have anything between 5 and 10 tabs, and then I use some panes because I like to have a terminal where I can actually get diff and whatnot. So I have this setup with a matrix of Claude sessions and matching terminals in a set of work trees that I work in. The way that we’re set up is that we have a few very large monorepos which we’re gradually moving towards, but we still have thousands of small polyrepos—that remains. So most of my work happens in those monorepos, so I usually have a few Claude sessions and terminals going on there. And then when I need to dip into one of our polyrepos, I will open up a more temporary Claude session.

**Boris:** Do you feel like a monorepo is a better fit for Claude, or—

**Niklas:** I was a bit worried, to be honest, about the monorepo setup and agents originally, because I think with some of the prior tools we’ve been using, we’ve been seeing issues with indexing and things like that, and these are fairly large repositories—our backend is more than 20 million lines of code. But turns out it works amazingly well in those repositories. And I think one of the things we found is how good Claude is at looking at other code in the repository to get, I guess, inspiration for the problem you’re trying to solve. It has required iterating on our CLAUDE.md files and whatnot to get it to understand the tooling we use and whatnot. But generally speaking it works really well.

**Boris:** Yeah. I wanted to ask about some of the infra that you built. Obviously you built Honk. Feel like from the earliest days of experimenting with models, to building Honk, to building background agents on the Claude Agent SDK—you see the future before other people do. What is it about the culture or the people working on it that kind of leads to this? Just tell me that story. How has it been going?

**Niklas:** 5 or 6 years ago now, we identified that our code base was growing much, much faster than the number of engineers we had to support it—like seven times faster. The statement was that over time, we just had more and more code that we needed to maintain. And Spotify, as a company that has an endless source of ideas of things we want to ship to our users—being bogged down by maintenance was not a good place to be.

We started automating, trying to automate as much of that maintenance as possible. A lot of that was pretty dull work, like migrating to the latest Java version or a library update or whatever, and a lot of it was moving from some API to some other API across all our code.

So we built out this infrastructure that we call fleet management, which is all about—instead of imagining before that, when we were doing a migration, we would send out the migration description or tutorial to all our teams and ask them to do that migration manually for all their components—instead of doing that, we imagined: can we find ways where we can do mutations towards our entire code base, living in thousands of repositories?

**Boris:** Because every team was kind of doing the same thing.

**Niklas:** Yeah, yeah—hundreds of teams doing the same operation manually over thousands of components. So each of these migrations took months and months and months to complete. We could maybe do ten of them a year, and we were barely keeping up with being on the supported version of the framework that we’re on. And in our internal surveys, migrations was top of the list of all the things that people were annoyed by.

So again, we started automating this. We built out all of this infrastructure to do this. We’ve merged millions and millions of those types of PRs, but they all relied on these deterministic scripts that you would apply and that would make those code changes or configuration changes. And one of the things we found pretty early was — code has an enormous API surface, so trying to make changes to code gets very complicated very quickly. We pretty quickly ran into a ceiling of how complex the changes we can do were. Even switching out a method in an API becomes pretty complicated when you can call that in five different ways—like if it’s a lambda or a call in different types of ways depending on what the code looks like.

**Boris:** So doing this with just traditional static analysis—like AST transformation.

**Niklas:** Exactly.

**Boris:** Because let’s say there’s an API and you alias it to a variable or something. Now you need variable and state tracking. That’s exactly right. It’s messy.

**Niklas:** So each script that we had to migrate code turned into thousands of lines of taking care of every edge case in that code. So that inspired us—pretty much as soon as the early LLMs came along, of like, hey, can we apply these to this problem? And early on it didn’t work all that well, partly because the models weren’t good enough, partially because we were very naive in how we were trying to do it. We were basically just putting the code in front of the model and trying to get it to one-shot that change.

So that didn’t work. Over time, models improved and our thinking about how to do this improved. We started applying LLMs as judge to make sure that the output was as intended. We started breaking down the problem, decomposing the problem in various ways. So many, many, many iterations of this and many internal hacks to try to take on this problem in different ways. We started consolidating that, and that then became what we now call Honk. And it was a very different beast originally. It was not on top of Claude, it was more a bunch of homegrown things. But it was the first sort of light in the tunnel of like, yeah, this is actually a problem that we can solve.

Then we’ve done many, many iterations on Honk. So today we released what we call V2. But I think in reality it’s V8 or something like that. We just didn’t keep track of the iterations we did on it. And it started out as this ‘automate these code changes, schedule and orchestrate over all our repositories.’ But pretty quickly engineers figured out that, hey, this is useful for other things as well. I want to mention this thing on Slack and have it do a task for me, or all of those types of things. So today, Honk has grown into being a much more ubiquitous tool for us.

**Boris:** Tell me about the architecture of Honk. What are the big pieces? You talked about: there’s the agent that codes, and this is just built on the Claude Agent SDK. And then you also have a verification step, like an agentic verifier. Tell me more about that.

**Niklas:** So we used to have a judge in Honk. But we actually removed that because we found that the agent and models — going back to Claude 3 or 4 — got good enough that we didn’t need the judge anymore. The judge was very important in the first iterations of it. It made us go from, if I remember the numbers correctly, roughly 20–30% success rate on PRs to 80% success rate. So it was a big, big change. But then again, as we talked about, the models caught up and the agent harness caught up. So we have now eliminated that judge from Honk.

Honk architecturally is fairly simple. It’s the Claude Agent SDK running in a Kubernetes pod. It has access to a set of tools. It used to be prior to V2 that those tools were predefined: an allowlisted set of tools that we trusted to give to that agent. Now users can add their own tools, just those tools. So now the agent can use any of our internal tools.

And one of the most important tools that it has access to is that it can run verification—like, run CI builds—and it can run those both on Linux and macOS. macOS is particularly important to us because iOS development, for example, needs macOS builds.
‍ **Boris:** And is this just building, or are you doing a full — like, open up the iOS simulator, have the model start the app — how deep does it go? **Niklas:** It can do those types of tests. We definitely have cases where we integrate the simulator and Claude to automate things like going directly from designs in Figma to UI implementations, and we’ve been using that for porting, for example, our TV apps from our iOS apps. So it’s been a very effective way for us to work. **Boris:** I feel like verification is one of these things that we talk about a lot, but I think when you’re doing this kind of closed-loop development where it’s an agent that’s given a task and then has to maybe fan out and break down the task, and just needs to do a lot of work without a human in the loop—yes, it’s just the single most important thing. And I feel like one of the common mistakes I see is companies under-investing in how well that verification loop works.

**Niklas:** I think that’s very true. And I think it’s true for us as well. One of the major changes that we did in our engineering practices as part of that was to strengthen our test automation, because part of that fleet management was prior to that.

So we have a very strong notion of software ownership within Spotify. We have divided our code base into many thousands of components. Each of those components has well-defined ownership—it’s owned by a particular team, and that team is fully responsible for it. They probably designed it originally, implemented it, and they operate it.

And part of that, prior to the investments we did in fleet management, was around—that team was in the loop for every change that got merged to their code base. And that meant that in some cases, we could be a bit sloppy on test automation, because that team could always check every PR if they needed to. But with starting to automate PRs towards our source code, one of the things was — we needed to change the expectations for teams: you might no longer be in the loop for these changes, we’re going to be auto-merging most of these changes without you ever seeing the PR. So that meant having to build out much better test automation to make sure that all our software could survive those types of automated changes. Now, zooming into where we are today, that’s been very, very helpful for us, because now we can throw agents at that and use the same verification that we had in place before. That being said, we are still improving our test automation because—I agree with you—it’s one of the most important aspects we’ve found to make agents effective, but also for us to feel comfortable throwing agents at our source code.

**Boris:** One of these trade-offs that people talk about all the time in engineering: reliability and quality on one side and speed on the other side. And to me, it feels kind of like a false dichotomy, because if you want to go faster, the thing that you need to do is automate your quality practices so that they’re better encoded. It’s not in someone’s head. It’s actually in a skill, or in a CLAUDE.md, or in some set of instructions. It’s something that Claude can do. And that’s ultimately what lets you go faster. And this is just another example of how in engineering, productivity is always about investing in infrastructure. It’s not about working more hours, it’s about just making the infrastructure better and better. And that sounds like what you were talking about.

**Niklas:** But you need to be very conscious about both the quality aspects while you’re trying to get the speed. And I think there is a real risk of slipping up on the quality if you’re not very actively investing into it. And we’re seeing that we’re keeping our quality metrics neutral while significantly improving our speed. But that does not come for free. We’ve needed to make these investments into test automation that—as we talked about—I think we’re going to have to continue our investments into our reliability practices as well. Some of those are changing as part of this transition.

**Boris:** And I guess as you try to go faster and faster and faster, you have to invest even more in reliability just in case.

**Niklas:** That’s exactly right. We make something like 4,500 production deployments every day. So there’s a lot of opportunities for things to go wrong. We need to have good practices around making sure that everything that ships into production has the quality that we want.

**Boris:** What’s the story with doing this many deployments? Is it kind of—in the past it was just continuous deployment and now maybe it’s faster signal for the agent? Or how are you thinking about it?

**Niklas:** This is something we’ve always been optimizing for, for as long as Spotify existed. I think we want to be able to have a developer take an idea and ship it into production as quickly as possible. That used to be weeks or months back, a few years ago. And we’ve continued to try to optimize that. And now it’s an hour or something like that. As I mentioned before, we have lots of ideas. We want to validate and explore those ideas. And the faster we can get feedback on that — in some cases that might be feedback from our internal users, in some cases it might be feedback from our external users. But in both of those cases, the faster we can iterate, we’ve found that we both build better products and we’re able to ship them faster to our users. Not every idea ships in an hour. Many ideas take lots of exploration before we’re able to ship them. But the notion of being able to get that quick validation is super important. And yeah, agents are certainly part of that loop as well. **Boris:** So for Spotify, the engineering org is very big, it’s like thousands of engineers, right?

**Niklas:** Yeah, it’s 2,900 engineers.

**Boris:** 2,900 engineers. How do you think about ROI and measurements, just making sure you’re moving in the right direction?

**Niklas:** So in terms of measuring ROI, it’s been relatively easy and we’ve seen very clear signals in that space. We’re seeing a 75% plus improvement in PR frequency, for example, that we can directly attribute to AI tooling. And I think by now 73% of PRs are directly attributed to being AI-authored. So those types of metrics we’re doing pretty well on. But then of course, we want to connect that to user value and revenue.

**Boris:** And how do you measure something like that? Is it an A/B test or some kind of holdout, like case studies? How are you thinking?

**Niklas:** Yeah. So we want to basically be able to connect the deliverables that engineers do—PRs, deployments—into what we call a work item. Basically the planned work that we have. And then that connects to A/B tests and rollouts. And then we’re able to, from that, attribute back and say this PR contributed to this DOD that we have, and that contributed to this user value. That’s the idea, and we’re trying to build those connections right now.

**Boris:** Yeah. I feel like back in the day. like we’ve worked in developer productivity for a while, when you have a big team, you want to make them more productive. And back in the day, a big win was like a few percentage points. Exactly, exactly. If you were lucky enough to be able to measure that. And with improvements nowadays, it’s just so obvious to everyone. Yeah. As engineers, we still want to measure it.

**Niklas:** Yeah. The discussion initially was fairly easy because we could see such large improvements. But as the maturity is getting there and the costs have been improving, I think the precision around those ROI estimates—the expectations on the precision—is going up as well. So that’s why we’re trying to improve how we can do that type of measurement.

**Boris:** Part of it is about the improvement in productivity. And then part of it is how much does it cost to get that improvement. And now people are seeing these like many dozens or hundreds of percentage points of improvement. And now you really want to attribute it — figure out how many tokens did it take, how many hours did it take? What was the productive output?

How Anthropic teams use Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6905133b69fcac6a5cbadb2f_og_how-anthropic-teams-use-claude-code.jpg)

From debugging production issues to navigating unfamiliar codebases to building custom automation—here's how teams across Anthropic use Claude Code.

Read more

[Read more](https://claude.com/blog/how-anthropic-teams-use-claude-code)Read more

How Anthropic teams use Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

From debugging production issues to navigating unfamiliar codebases to building custom automation—here's how teams across Anthropic use Claude Code.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

How Anthropic teams use Claude Code

From debugging production issues to navigating unfamiliar codebases to building custom automation—here's how teams across Anthropic use Claude Code.

"You need to have the same engineering practices that we had before. There’s a new actor in your code base, but the fundamentals seem to apply equally well."

Niklas Gustavsson

Chief Architect and VP of Engineering, Spotify

**Boris:** I want to end on maybe one question. What advice would you give your peers? What advice would you give to other CTOs and engineering leaders, like VPs of engineering at other companies?

**Niklas:** What we found is that these investments in foundational capabilities—we talked about test automation and verification—I’m going to say the same is true for another aspect that we’ve seen, which is standardization. So we’ve been driving more consistent code bases, more alignment on the tools that we use, the frameworks that we use. And we’ve seen, this was originally an investment we did to simplify things for humans and make humans more productive. But we’ve seen the same thing transition really well to agents as well. So as I mentioned before about Claude being able to find inspiration from other pieces of code in our repos, if they look ten different ways, Claude is going to be more confused. So we’ve been seeing the more consistency we have, the better our agents work. So I think if there’s one piece of advice I would give, it would be to not ignore those types of investments. You need to have the same engineering practices that we had before. They still apply in this new world, they might look different. There’s a new actor in your code base, but the fundamentals seem to apply equally well. At least that’s been the case in our environment.

**Boris:** What’s your advice for engineers that maybe have been doing engineering work for a while? I know Spotify has talked about engineers shipping on the subway, which is really cool. Obviously engineering is changing. What’s your advice to everyone that’s in the middle of it and trying to figure it out?

**Niklas:** Yeah. Let me talk about this from a more personal angle. I’m someone who’s always truly enjoyed the problem-solving part of coding. This is going to sound as nerdy as it is, but in my spare time I will do competitive programming at times because it’s just a fun mental exercise. In the back of my head, I was always a bit worried, like we were talking about before. about how this was completely changing the way we were working. And I was pretty worried about that from just my personal point of view. Like, am I not going to get that part of the hard mental challenge of solving problems?

Now I find myself having five agents working in the background, and my way of interacting with them is very different from the way that I was working a year or two ago. And for me, it’s turned out that I was wrong. The thing that I like to do is solving problems. And the way that I solve those problems turns out to not be the most critical piece for me. This is always going to be personal—different people are going to have to make that transition in different ways. But I think: focus on the types of problems that you’re able to solve. I find myself both more productive in that I can bring more value from the work that I do, and I can also solve problems that I really couldn’t solve before. I can jump into code bases that would have taken me days or weeks to get into before and be contributing things that I just could not do before. So for me, that’s been amazing. And again, it’s going to look different for different people. But I think give it a shot and find a way that you can use those tools in the way that you like.

**Boris:** I feel like for me, I’ve seen this big shift from implementation time—because now Claude Code does it in the background while I do other stuff. And instead, what’s filled up that time for me is thinking about what’s next, talking to customers, and also actually much more prototyping than I expected. Some of it is for external products, some of it is for internal automations. How has that change worked for you?

**Niklas:** I think it’s been similar for me. And we didn’t talk about this, but one thing that we’re making a big investment in is prototyping in particular. And this is targeted both towards engineers but also the non-engineering cohort.

One of the things that Claude and similar tools have unlocked is to allow anyone to take their idea, whatever that idea is, express that in natural language and have Claude go implement that. So as folks started figuring this out, including non-engineers, they started trying to do this in our real apps. And they’re pretty complex beasts of code. But they were starting to see signs that they could do it. So we started, a few months ago, basically building out the infrastructure to make that simple. So today we have a very simple way to get going and build an end-to-end prototype in our mobile apps and our backend. We have an internal app store for those prototypes where you can share them and take a look at someone else’s prototype or try your app.

And that’s been a real unlock for folks that—maybe before, including engineers that maybe weren’t super familiar with how to build something in our mobile apps—to be able to express ideas that used to take motivating a bunch of engineers to try to build that for you. And now you can go in and within an hour or two, you have a working prototype that you can start sharing with people to show what that actual idea looks like in real life, with real users, real data, and so on. So yeah, those types of things were unimaginable a year ago, and now we’re doing them every day. **Boris:** Yeah, I love that. Have you seen a shift in who’s producing this? Is it like engineers doing it, or is it mostly coming from designers and product managers? How has that changed? **Niklas:** It’s everyone, up to our co-CEOs, who have prototypes in that app store at the moment. So it’s actually been a bunch of our senior execs have built prototypes that are good. An idea that they always had in the back of their head. They have an entire engineering team that could build that out, but that team is focused on other things. So for them to then be able to try something out more quickly than they could before and get a touch and feel for what this thing is going to look like. It allows you to test out an idea in a day instead of weeks or months.

**Boris:** Niklas, thank you so much.

‍

Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525504b02eec936ac51b_68c469d41149ace562bfd24d_og-claude-product-claude-code.jpeg)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Prev](#)Prev

[Next](#)Next

## Related stories

[How Notion ships and scales agents with Claude Managed Agents](https://claude.com/customers/notion-qa)How Notion ships and scales agents with Claude Managed Agents

How Notion ships and scales agents with Claude Managed Agents

Customer story

[Customer story](https://claude.com/customers/notion-qa)Customer story

[Deepgram ships 4–10x more durable code with Claude](https://claude.com/customers/deepgram) Deepgram ships 4–10x more durable code with Claude

Deepgram ships 4–10x more durable code with Claude

Customer story

[Customer story](https://claude.com/customers/deepgram)Customer story

[Office Hours: Building the case for leaders who ship with DoorDash](https://claude.com/customers/doordash-boris-office-hours) Office Hours: Building the case for leaders who ship with DoorDash

Office Hours: Building the case for leaders who ship with DoorDash

Customer story

[Customer story](https://claude.com/customers/doordash-boris-office-hours)Customer story

[Office Hours: Building for the model that doesn't exist yet](https://claude.com/customers/ramp-boris-office-hours)Office Hours: Building for the model that doesn't exist yet

Office Hours: Building for the model that doesn't exist yet

Customer story

[Customer story](https://claude.com/customers/ramp-boris-office-hours)Customer story
