---
title: "Running an AI-native engineering org"
channel: claude
url: https://www.youtube.com/watch?v=IA5LWIGqnyM
youtube_id: IA5LWIGqnyM
published: 2026-05-22
duration: "26:38"
---

# Running an AI-native engineering org

[![Running an AI-native engineering org](https://img.youtube.com/vi/IA5LWIGqnyM/hqdefault.jpg)](https://www.youtube.com/watch?v=IA5LWIGqnyM)

<details>
<summary>자막: Running an AI-native engineering org (26:38)</summary>

[00:00]
[music]
>> Hey everyone.
Aw, thank you. I didn't expect applause.
Well, thank you so much for joining me
today. I'm excited to speak with all of
you about, you know, some lessons I've
learned as I've been leading uh
Claude Code and Co-work. So, actually
first I should do an intro. So, yeah, my
name is Fiona Fung and I lead
engineering and product for Claude Code
and Co-work. And before Anthropic, I had
also built and led teams at Meta and
Microsoft.
So, with that, let's dive into some
lessons I'm excited to share with all of
you. Hopefully, maybe you'll find a
couple of tidbits that may be helpful to
you.
So, there are five topics I really want
to cover today. The first is the
bottlenecks have moved. And so, when the
bottlenecks have moved and it's shifted,

[00:01]
what are all the team norms that we
felt, "Oh, yeah, we have to rewrite some
of these because it's changed." How we
rolled it out, I'll talk about like how
we rolled out some of these updated team
norms.
And in terms of the proof, what were
some signals that I feel, "Okay, this is
giving me confidence that we're trending
in the direction right direction." And
maybe I'll help you as well.
And lastly, I'll leave you all with
maybe a topic for you to all take back
to your team to discuss cuz I'd love to
hear about um yeah, whether any of this
resonated.
So, with that,
let's touch on this first topic, which
is the shift. So, the bottlenecks have
moved. And you notice there's that
little subtitle there of what served you
prior may no longer. This is one of my
favorite sayings. Like, actually, I
think this is the muscle that has really
helped me weather at Anthropic, but also
before at the other companies. Always
being of that growth mindset. Like, you
know, from all the talks this morning,
you see our rate of change is just
increasing. And so I found it's always
helpful to look at what are either team

[00:02]
norms that you've set up for your team
or team processes and always ask
yourself, is it still serving its
purpose?
So for years, many years, engineering
bandwidth was expensive thing. And when
you think about how do we all do
software engineering, everything was
around kind of like protecting this
resource, right? Like we want to do a
lot of planning cuz we want to make sure
when we're building that we have high
confidence that we're building the right
thing or we want to do reviews. Like
there's a lot of action around when
engineering bandwidth was a limiting
factor.
And maybe I'll pause there. Like when
you think about our industry, this is
not the first time that the bottleneck
has shifted. Come I'll I'll take you all
back in a time machine with me. We'll go
all the way back to the early 2000s.
And if you all remember, so back then I
had just joined Microsoft. I was working
on Visual Studio. There was no such
thing as cloud. It sounds crazy now,
right? Like now cloud is so ubiquitous.
But back then there was no cloud and I
remembered how we built Visual Studio

[00:03]
was this one server room and everybody
had to be on call for a week and then
you'd just go into this room and I
remember the whole build process. It was
a queue. We can only merge six PR's at a
time and anytime, you know, one of the
tests would fail, you have to debug
which of those PR's caused that failure.
So back then, that was actually a big
bottleneck. And then now with cloud and
with continuous build, that bottleneck
has also shifted. So this is just
another shift for us to think about of
when coding is no longer the bottleneck,
what changes?
And so on the cloud code team, coding is
rarely the slow part anymore.
And so like that's why all the upstream
and all the downstream kind of like
processes, we felt like we've had to
change a little bit.
So as an example, what were some of the
old bottlenecks, right? Like writing
code, writing tests, refactoring. In
fact, I'll share a story with you all.
When I first joined Cloud Code, I wanted
to onboard and fix some bugs, and I

[00:04]
thought, "You know what I'm going to
try? Test-driven development." I
remember that was a really big thing a
while back. You know, the idea is write
the test first, make sure it fails, then
do the change, then now you already have
a test. But, it was kind of like eating
broccoli, you know, like even though I
actually really do love broccoli, but I
use it as an example. Uh but, I remember
you It feels like eating broccoli to
write the test first cuz it's not always
the most enjoyable part of the process.
And I remember always itching to build a
product and get to, you know, playing
around with it. And so, now with Claude,
I remember the first bug. I'm like, "You
know what? I want to try test-driven
development again. Let's write the test,
but first it will fail. Let's verify it
fails cuz that's how I could verify the
test is actually testing something." And
then we we, you know, like I remembered
like making the bug fix, and then we
already had a test. And I remember that
first experience, test-driven
development was actually so much more
fun and so much more pleasurable. It
kind of took the tax out of test-driven
development. So, that was a big aha for
me. Refactoring is another fun topic.

[00:05]
Like, I don't know if you all felt this
before, but, you know, I've been on a
teams before where we have to either do
like some big refactoring or some
software architecture cleanup. And it's
always a debate of when would we find
time to do this work, this work that we
know is so important, but it always has
to come off at the cost of trading, you
know, time to build product. So, again,
thanks for the models, and with Claude,
refactoring is also no longer a
bottleneck. So, now when those shifts
happen, what am I starting to see that
as the new bottlenecks? Uh verification.
That's a big one. A lot of it's because
the bandwidth has just increased so
much. We have to pay even more attention
to is it correct? And I'll talk about
this in a little bit, but also when
roles are blurring and more people are,
you know, checking in changes, we also
want to make sure everybody feels
confident that their changes are
correct.
Who reviews? That's a really popular
topic. And also, how is it maintained?
And this one is interesting because
again, the throughput is now so much
more. Also, have to think about, you

[00:06]
know, the cost of maintenance as well.
So, these were some of the old processes
that we felt quietly stopped working.
And I love that phrase quietly stops
working cuz actually, if I step back,
anytime, you know, hopefully when
somebody puts a process in place, it's
to solve a problem. But very often, we
forget to audit to go, "Wait, are those
processes still required?" Or is it
still serving its purpose? So, for
example, what were some of the things
that we had to change? Planning norms.
When coding is no longer, you know, the
the the bottleneck and and not a like
and you have like much more coding
bandwidth, how did we rethink through
planning? Uh code ownership is also
another interesting question. Almost all
the cloud code commits now are also, you
know, co-authored by Claude. I don't
think I've in the last few months ever
saw a commit that wasn't. A code review
is a good one like that's a lot of
questions I get a lot as well.
Also, team makeup. Roles are blurring
and what are the skill sets that we're
thinking, "Hey, you know what? These are

[00:07]
actually skill sets we're kind of like
doubling down into." And also, knowledge
sharing. What happens when maybe
documentation is no longer your source
of truth?
So, given some of those shifts, these
are some of the team norms that we had
to rewrite.
We talked about code review. And
actually, Cat this morning in the talk
really talked about cloud code review as
well. That was a really like that's how
an amazing tool for us to make sure
we're also doing the right thing.
Onboarding has also changed. I'll share
with you all my onboarding story.
Planning, I've talked about this already
of when coding is no longer bottleneck,
how does that shift our planning?
Hiring and also, org shape. Org shape is
a fun one like, you know, we really want
to keep everybody more agile and flatter
orgs, but every manager on Claude code
actually start as an IC first.
So, with that, how have our planning and
technical debates changed?
So, in technical debate code wins. You
know, it's like building is cheap,

[00:08]
arguing is expensive.
I'll actually share with you all like I
remembered, you know, as I was
onboarding I also wanted to do some code
refactoring. I was kind of like, "Hey,
what's some refactoring that we think is
good to do but we haven't yet done?" And
I remembered me and Boris had a couple
of debates of approach. And in the old
days, I remember and I almost did this.
I almost said, "Hey Boris, let's just go
to this meeting room and go to
whiteboard and whiteboard it out."
Almost did it and I'm like, "Wait, if
if, you know, with thanks to Claude, I
can actually generate." I remember
generating three different versions of
the PRs. And actually that's what me and
Boris used to have a really good
technical debate cuz I wanted to not
look at how the code was implemented,
but also impact to the colleagues. Uh
prototyping is another good one. So, now
like anytime we're really having idea,
go ahead and prototype and let's
actually go ahead and dogfood it and
then we'll try. I remember many years
ago also having this uh prototyping
conversation in another team I was at.
Um you know, cuz there was a debate.
There were kind of two camps. One camp

[00:09]
of prototyping is great. It allows you
to move quickly, to build, you know,
kind of like a wireframe skeleton and
get a feel for the product. But on the
other camp, I think there was a concern.
Well, you know, code prototyping you're
kind of doing it with speed, you're
cutting corners, and there's concern of
what happens when you show a prototype
that kind of works and then, you know,
maybe you get hung up on it, you don't
want to throw the code away, and then
you end up trying to ship that thing.
It's not built to scale.
Again, with Claude, now actually
prototyping is a great way to get
started cuz we could iterate and learn.
And then thanks to, you know, the models
help, we can also then actually scale
out a prototype to production a lot
faster.
So, what's one thing we reduced on the
Claude Code team? It's you know, I might
have been on teams before maybe y'all as
well like design docs like really
in-depth planning and design docs. Most
of our discussions actually happen in
PRs or prototypes. And again, that's
just because the engineering bandwidth,
you know, is is now increased and coding
is no longer a bottleneck. Uh what do we

[00:10]
really want to double down on?
Verification. And this is something that
I want to make sure, you know, me and
our team keeps keeps doing better as
well because now with all the bandwidth
is even more important to how do you
verify quality? And I call this like,
you know, like shift left. So, for
example, what's better than you running
it really sucks for me when I hear from
our customers and developers and you all
run into a code. I'm always like, "Ah, I
wish we caught it first." But you know
what's actually better than me running
into the bug first? Us having automation
in place actually catch it closer to the
source. So, that's like that's something
that we're really constantly looking at
as well of how to make sure we keep
shifting left and automating more.
Who made this change? This used to be a
question that a lot of folks would ask
of, "Hey, who who who was the last
person that touched this or who's a code
owner?"
And now I encourage you all like if you
find yourself asking that question to
get to the root of the question. Like
what are you trying to answer? Is it Are
you looking for someone that caused a
regression? Are you looking for someone

[00:11]
to answer a question? Are you looking to
gain context? And is there a way that
Claude could actually help you with
that? Uh Cat actually talked about
routines as well like earlier today.
That's one of the routines I have set up
like automatically, you know, in the
morning I like over my morning cup of
coffee I like to review all the feedback
in our various feedback channels. So, I
have a routine that will go through to
kind of amalgamate all the feedback for
me and help me to identify themes.
How do you keep up with code reviews?
Before we actually shipped Claude Code
code review, this was a question that I
would get all the time and I can share
that answer with you all. Like
definitely Claude code code review is
one one tool that has really helped us
to make sure we keep up with the coding
bandwidth. And so where Claude is really
good, right? Like the style and lint,
obvious bugs, um anytime that you
actually have like like if if you there
is a spec, I encourage you to actually
check the spec into your code base cuz
Claude is very good about verifying
against spec drift. But the still really
important to still have a human in the

[00:12]
loop. So where do we find even in code
reviews is really important for humans
still? Legal reviews, anything that is
actually about risk tolerance. So
especially when you look at trust
boundaries, it's all about that trust
but verify and where humans bring a lot
of the needed expertise.
Product sense and taste is another fun
one. So last uh December, I wanted to
update Claude in our CLI to, you know,
give Claude a little holiday theme and I
was ambitious. I wanted to turn Claude
into a snowman. I you know, like I I
coded up an example and I asked her
designer, "Hey, can you go ahead and
review this for me?" And she gave me
such excellent feedback of no, this
looks nothing like a snowman. You you
you create you turned Claude into Mr.
Peanut. I don't know if Mr. Peanut's an
American brand and and in the US we have
this jar of peanuts and you know, their
their mascot is this little peanut
character and I was like, "Holy crap,
that's totally right. I I thought it was
a snowman but you're right, it's a
peanut." And so that's where like humans
also like with that product sense is

[00:13]
really important to keep that expertise
in the loop as well.
Now, what should my team makeup be cuz
roles are blurring and Claude is
augmenting.
And so when it comes to engineering,
these are the two profiles that I now
really like focus on. One is creative
builders with product sense
um and then another is deep system
expertise. And so this is definitely
like, you know, the hard part. Want to
make sure that we can still have that
trust but verify. Maybe I'll talk a
little bit about product sense. When I
gave this talk in San Francisco,
afterwards a lot of engineers came up to
ask me a question of how do I build this
product sense muscle? So, I figure I
will share with you all of what I have
found helpful and it's helpful for me
and maybe it will resonate with you all.
Like, for me it's this muscle that you
build with it first starts with dog
fooding. And especially for managers,
actually like making sure you're
spending time using the product that
you're building and your team is
building. In fact, most of the time
anytime I join a new team, like that's

[00:14]
one of the first things I do. I'm like
dog fooding the product to make sure I
understand it. Cuz this way you really
start feeling your product in your bones
and you remember you always ask
yourself, "Wait, when I was building
this product, what problem were we
trying to solve? Like, what experience
was I trying to enable for our users?"
So, with that in mind, like dog fooding
is a really good way, especially for
managers who before Cloud, you may not
have time to be in the code base
anymore. Um but yeah, like actually
anytime I join a team and I would dog
food, a lot of team members would always
come up to me and say, "It's so awesome
to see you using our product cuz you
really care." Cuz that's a way for you
to experience the work as well.
So, for me product sense comes from a
lot of dog fooding and then also like
iterating, shipping and then going out
to speak to customers. One of my
personal passion projects is working
with small businesses. I love small
businesses. I feel small businesses are
the lifeblood that forms our community.
And uh we actually just announced Cloud
for small business, which is a product
I'm so excited at um but I have a lot of
friends that run restaurants. They and
they work incredibly hard. And so, I met

[00:15]
with a lot of them to onboard them onto
Cowork cuz I wanted to see how, you
know, like outside of enterprise with
small businesses, how do our users
actually onboard? And I got such
valuable feedback. It's actually really
humbling to see where in the onboarding
flow we there was so many things that we
could have been doing better.
So, I really encourage you all to to dog
food your product so then you really I
call it like feeling it in your bones
cuz really get keeps you um giving you a
sense of what your product is doing. If
not, after a while, you might find
yourself making product decisions that's
all just based on either metrics or
dashboards or PowerPoints. So,
definitely dog food, dog food, dog food.
Or as we call it in Anthropic, ant food.
So, filling cross-functional gaps with
Claude. This is interesting cuz I
actually see this for all roles. So, for
example, designers on Claude code team
previously, you know, anytime we wanted
to make polish or UX fixes, designers
would go ahead and create that red line
and then hand it off to engineering. And

[00:16]
it's always a wait, you know, for cuz
engineering is always about I have to
build this product, I have to fix this
bug, when will I time to actually do
this polish. Designers on Claude code
actually, you know, use Claude to make a
lot of those polish fixes. So, then it
really closes that iterative loop a lot
faster. And again, this goes into why
it's so important to do the
verification.
On the flip side, for me, like for
example, one time I was fixing a bug and
I needed a little bit of content help. I
I don't know about you all, but as an
engineer, I tend to be very verbose. And
when I'm like, you know, if you ask me
to write a very short sentence to
describe what something's supposed to
do, I tend to go too much into the
weeds. But Claude was a really great
content design partner for me.
And so, that's what I found really
interesting on Claude code team. For all
roles, Claude is actually augmenting uh
all the areas where you may not be as
strong.
So, this was the manager slide that I
was like, "Oh, this was, you know, maybe
a good spicy topic." But when I first
joined Claude code, this was one of the
first things I changed. I'm like, "Hey,

[00:17]
I I was working with the recruiting team
to go because I believe so much in dog
fooding. And on Claude code, we're using
Claude to build Claude, we're using
Claude code to build Claude code. And uh
so, every manager started as an IC
first. I actually felt this worked
really well cuz it enabled managers
before you have to worry about the
responsibility of supporting people
actually having time to, you know, like
roll up your sleeves and get into the
code base and learn what it's like to be
an engineer on the team.
Um maybe I'll also, you know, like touch
on this is also a great time that if
you're a manager to actually get some
maker hours back and actually get back
into the code base cuz the onboarding is
a lot less daunting than it used to be.
Um actually even before Anthropic, there
were different roles I've had where I've
switched between manager and IC. And I
think every time I switched to an IC, it
really helped me build up the
engineering toolbox. But that onboarding
was always a little like, you know, that
slight hesitation cuz it could be
daunting if you haven't done it in a
while. But like speaking for myself, I
remember when I onboarded to Claude, it

[00:18]
was uh it was such a different
experience. And actually, that's what
I'll go into next.
So in terms of knowledge sharing, what
becomes a new source of truth? So when I
was onboarding to Claude, the code is
our source of truth. And so I again,
like in the old days, anytime I joined a
new team, I'd meet with all the
engineers to I still do meet with all
the engineers on the team, but now we
talk a lot more about what's on top of
minds and
because before I would always so like do
these tech deep dives.
And now I actually did my first, you
know, like tech deep dive just with
Claude like because Claude has is really
good at answering all these questions I
have. So even when I was doing that
first bug fix, I remember asking Claude,
"Hey, before I dive into this bug fix,
can you actually teach me a little bit
about the surface area and also what are
what about all the areas around that bug
as well?"
And so for Claude code and co-work team,
our code is a source of truth. I would
encourage all of your teams like if
whatever is your source of truth, where
whether it's a spec, you might actually
change that into a skill that you check

[00:19]
into the code base. Like whatever you
can make sure becomes your source of
truth, keep it in the code base cuz this
way you can actually keep it up to date.
Cuz that's the other thing when coding,
you know, bandwidth is so much, you
know, like so much more. It also makes
it easier for any documentation that
also doesn't isn't part of the update
loop to get out of date.
So, how did we roll out all these
changes on the Cloud Code team? There
were things that we it was really
important that we aligned as a team. And
then there's also I want to make sure we
also give space for bottoms up because
each team is focused on different things
and there might be, you know, like
different tool chains or anything that
resonates more with each team.
So, what did we align with kind of like
the teams as a must do? These are some
of our Cloud Code team principles and
what we call forcing function. And this
slide is out of date. Like I shouldn't
put every engineer, it's every teammate
uses Cloud Code. And also co-work,
actually. So, like us using our product
day and day has been really important.
Cloudify everything we can. And so, like

[00:20]
anytime we have a question of, you know,
what? Yeah, I'm doing this. What's
better than me doing it? Can Cloud do it
for me? Cuz then it actually frees up
more of my bandwidth for other problems
to solve.
And my last one is a explicit permission
to kill old processes. Again, it's the
e- even our team principles and even
processes as we put on, even after a few
months when we notice, "Hey, is this
really serving its intended purpose?" We
really always give ourselves permission
to always critique and make sure to
always revisit.
And the bottoms up, there's a lot of
freedom for, you know, like, you know,
team or pods to adapt. So, for example,
how Cloud shows up in team triage or any
teams like planning rituals or stand-ups
or which workflows get cloudified first,
that is a a lot of bottoms up. So, I
found that this balance of make sure you
align with the team of in terms of like
what's important in terms of team
culture and also update those as you go,
but then leave some room for each pod to
adapt.
So, if I zoom out, what were the three

[00:21]
things that I prioritize for Cloud Code
and co-work that I think has worked
really well? A number one, it was, you
know, like keeping the org as agile and
as flat as possible, having managers
also, you know, like support parts of
work, but also really get into the code
base and be directly responsible for
parts of the product as well.
Uh number two, that's our Claude-ify.
So, if Claude can do it, Claude should.
So, that's always a question we're
asking. And And maybe that's the other
interesting, too, like um you know, this
morning you heard the talks about the
models. The models are improving at an
amazing pace. So, sometimes we might
find even if Claude wasn't good at doing
something two or three months ago, now
with like a model update, it's actually
gone really good. And this is why again,
it always goes back to that whole like
always revisit and always have the
growth mindset cuz the models are also
improving really fast.
And again, you know, people don't delete
processes on their own, they tend to
pile up. I remember I was on a team
where we had so many different SLAs.
There was an SLA for P0 bugs, an SLA for

[00:22]
incident response. And after a while,
I'm like, with all these SLAs, I need a
stacked rank list to actually have cuz
even the engineers are coming to me
going, "There's only 24 hours in a day,
like which SLA am I supposed to do?" And
but that's why it's always so important
to audit. I remember that time, I'm
like, "You know what? We really should
be auditing. Are all these SLAs still
really necessary?"
So, now for the proof. What are some
signals that we're seeing of like is it
actually working? So, these are some
numbers that I find as helpful that I
wanted to share with you all.
And so, these were some of the shifts
we've seen as we've been kind of
improving our workflows. Onboarding
ramp-up time goes down. Like I think
that's actually a really good signal of
like we used to have this thing of like
what's the span of time it takes for the
engineer to land their first PR. The
onboarding ramp-up time and also like
costs to other team members we noticed
keeps going down. Like I I I even like a
lot of times sometimes when a person
joins a team, they'll ask me a question,
I'm like, "That's a great question. We

[00:23]
should ask Claude. Like that's how we
kind of
like Claude has really helped us to
onboard and answer a lot of questions.
Which is also why for the managers, I
it's why it's fun for me to actually get
back to the codebase cuz in the old days
I would actually feel bad cuz I feel
like, oh, I need to learn this area. I'm
going to ask an engineer and take time
away from their day cuz they're all so
busy. But now thanks to Claude, I don't
feel like I'm wasting anybody's time.
The PR cycle time should also go down,
but this one's interesting. I'm going to
say it's important for you to not just
look at the end-to-end, but actually
break it out into like what are all the
different funnels in terms of a PR. Cuz
if your PR cycle time isn't going down,
it might not mean you're not adopting
AI. It could be other parts of your
queue is actually getting jammed up
because of all the throughput. So for
example, are your build and CI systems
keeping up? So for PR cycle time, I
think it's actually really healthy to
break it down into all the different
chunks and seeing which of those you
might be able to improve or automate.
And lastly, Claude-assisted commits go

[00:24]
up. As I mentioned, I don't think I've
ever like in the last few months I've
not seen a commit that wasn't you know,
like assisted by Claude. But if I step
out, like I would say what's even more
important than just throughput is
whatever, you know, you and your team
are trying to solve, whatever the
product or problem. Find some way to
measure that cuz outside of just
throughput, hopefully we're also making
meaningful change to make the product
better or improve quality.
Okay, so now it's time for me to maybe
share like a little takeaway home
exercise that might be fun for you to
take back and go have discussions with
your team. But first I want to be really
transparent. I still have questions as
well. So I'll share with some of those
that we're still working out through the
Claude code team.
So for example, do you still need
separate iOS and Android orgs? Like that
was kind of like more of the traditional
org approach if you would usually have
like one for iOS, one for Android. But
now with Claude and enabling our
engineers to go flex across different
mobile platforms, we're thinking, "Hey,

[00:25]
do we really still need you know, two
separate mobile teams?"
Uh how far do you push fully automated
reviews? We always want to make sure
we're striking that right balance
between kind of speed and fast enough
and make sure we're not losing something
important.
And roles are blurring. And how do we
make sure everybody is productive? And
that's why we're we're right now looking
through verification is a big one. So
that hey, as we're going through, make
sure everybody that makes a change has
confidence in their change. But also,
what are all the different parts of the
workflow too? Like I'm working with my
designers. We actually just, you know,
announced Claude design. Also thinking
through how can we make sure that we're
also improving the workflows of all the
functions on the team.
So with that, this is what I would love
to leave you all with. Pick your
noisiest workflow. Or it could be just
some workflow or team meeting that you
don't particularly enjoy or is really
high tax on the team. Like I remember it
I was on another team where we would
have this really expensive weekly
meeting and I noticed everybody's on
their laptop. And you know, except for

[00:26]
when they have to pop their head up to
give status and then they go back to
their laptop. I'm like, this is when you
count, you know, like how many people's
in this room, this is a very expensive
room. So always like kind of like pick a
workflow and always ask yourself, "Is it
still serving its purpose?" Or if it's
like really expensive, is it something
that Claude might be able to help you
with? And kind of like do this one step
at a time.
And with that, thank you so much for
listening to my talk.
>> [applause]
>> It's been a pleasure.

</details>
