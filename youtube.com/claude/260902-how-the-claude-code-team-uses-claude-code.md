---
title: "How the Claude Code team uses Claude Code"
channel: claude
url: https://www.youtube.com/watch?v=S-sYlFiGFv8
youtube_id: S-sYlFiGFv8
published: 2026-09-02
duration: "22:23"
captions: en
---

# How the Claude Code team uses Claude Code

[![How the Claude Code team uses Claude Code](https://img.youtube.com/vi/S-sYlFiGFv8/hqdefault.jpg)](https://www.youtube.com/watch?v=S-sYlFiGFv8)

<details>
<summary>자막: How the Claude Code team uses Claude Code (22:23)</summary>

[00:00]
Do you guys have any thoughts
about your next year?
I feel like it's hard for me
to think about the
next two months.
Let alone the next year.
I don't know
if you guys know it.
It's been almost a year
since I joined
Claude Code.
It’s crazy to think about
how far we’ve come
from a year ago
when we were like
prompting Claude Code,
giving it feedback,
accepting permission
prompts, to now.
So, like,
tell me about how you work
with Claude Code right now?
Yeah.
Now I'm doing so
much of my work
Through Claude Tag,
actually.
And the kinds of problems
that I'm giving to
Claude Tag are just worlds
more complicated
and challenging than,
you know, implement this class
or write this function,
which is kind of where
things started at
with Claude Code.
I think that's
really complementary
to the sort of the shape
of like Claude
Tag living in Slack
as like a Slack native agent,

[00:01]
because it means they can go
and look up
all this additional context
around like,
hey, what's the product
context?
Like, what are the decisions
that we as a team
have made about
what this product should be?
And that just makes its
decision making a lot better.
Having access to all that
information and understanding
how to incorporate that
into the choices
that the agent is making.
Yeah.
My work feels pretty similar too.
I think, 70 to 80% of my work
happens on Claude Tag now,
and for 20% of the work,
I will maybe
open up the TUI
or the desktop app to like,
refine something.
Or if I want to be
micromanaging
my Claudes,
I will do that.
I think we've gone from just,
you know,
caring about the transcripts
so much and like,
caring about each individual
tool call
and each individual decision
that the model makes
to just a zoomed out
view of, like,
I have a goal and
I'd like to achieve this goal.
And you just kind of give
that goal to the model
to achieve for you.
You know,
what I've been reflecting on
is just how much.
the software development,
life cycle has changed
and how we've sort of like,

[00:02]
learned all these lessons
along the way,
you know, like building
Claude Code, building
all these primitives
that tie together.
Eventually into Claude Tag,
which is like,
how we're doing everything
from like verification to code
review, like brainstorming,
monitoring.
Tell me about how working on
Claude Code
compares to working on,
previous software products?
I mean, there's always
a shelf life on any product,
or the technology underneath
the products rather.
I think the shelf life for
the technology
used to be
in the order of years.
So it used to be like,
I'm going to make this product
and I have high confidence
that this is going to
be a thing for,
you know, a few years or more.
With models and AI models,
it's like the technology
fundamentally
shifts underneath you
every two months
and it's like,
maybe it's
getting compressed
as time moves forward too.
And so it's kind of hard
because you have to stay
at the frontier
and you have to kind of
go past the frontier really
to like, feel that edge.
But at the same time,
you have to provide value

[00:03]
to people
using the models today.
And in the now.
And so it's
this like balancing act,
which is part art, part
science stuff, like how do I,
how do I build
for this technology
that's moving
so fast underneath me?
Is there like, a moment
where you felt like
you just caught
the wave in the right part?
I think the first time
I felt,
the “ride the wave”
feeling was maybe to do lists.
Oh, okay. Yeah.
Like, that was, this was like,
maybe Sonnet 3.5.
And the models just
were not able to do
any kind of long horizon work.
And you would give it
like five things to do,
and it would do three things
and just give up.
And so that's
when we were like, oh,
maybe you give it a to do list
and it'll do really well.
And it did really well.
It was just like,
whoa, this is
exactly the thing we need
for this moment in time.
But you know, a year from then,
like, it's disappeared,
like you don't really need the
to do list anymore.
Like, there's, like,
you know, more complex
memory states
and things
that you can rely on.
And I think this is
the perfect
example of how,
you got to be very
unattached

[00:04]
to the things
you're building.
Because they're going
to go away fairly quickly.
I think that it's like,
the fact that
we build these things
into the Claude Code harness,
and a lot of that
is just to cover
for some of the failure modes
that the current state
of the model has.
And as the models get better,
we have the freedom now
to say like, oh, actually
all these like features
that we built, like
it's not relevant anymore.
We don't need those.
We can get rid of them.
And the thing that
balances that out
is, okay,
well now we're doing
even bigger, more challenging
tasks in Claude Code.
And what are the tools
that the model
needs to be able
to stay coherent
and do a good job on those
even bigger tasks.
And the tools
that we need to give it
start to look different
as the scope of the
task changes.
A lot of people ask me,
how does the
Claude Code team work?
And I think one thing
that's unique
about the Claude
Code team is like,
we have to keep up with
the models really closely.
So we need to, like,
you know,
sometimes make big changes

[00:05]
very quickly where we're like,
oh, the model is so good,
now we need to make
a whole new proactive agent,
and it needs to be like
a small team
that does it while it's also,
while we're also like,
rewriting the permission
system
and creating artifacts
and things.
So I think in some ways
we're this
like hyperbolic time
chamber of like,
where software
development is going.
I don't think most products
hav as short a shelf life.
You know, and have to keep up
on the edge much.
But definitely
as an engineer,
you kind of have to do
some of this, right?
You have to sort of like,
you know, understand where
the capabilities are going.
And obviously
we try and help with that
as much as possible
through the product.
But, yeah, it's
also good to like keep
like your mental model
of Claude as well.
I mean, I think when you added
the ask user question tool,
that was another kind
of example of
like riding through the wave,
what were you thinking
when you created
that tool and
what was going on
through your head?
I wanted Claude to be interactive.
And initially I had it
after planning basically.
And then I was like,
oh, wait, what
if it's just a tool
that it can call?
And it took me so long
to design the tool.

[00:06]
Like it was really hard to get
Claude to call the tool well,
and then eventually, I designed it.
And then it just started
getting really good
at calling the tool.
And then recently
I'm just like,
I don’t even use the tool as much.
I just create an artifact.
And the artifact
asks me questions,
you know,
and it's like in HTML,
it has diagrams and mockups
and things like that.
I'm like, it happened
so quickly, right?
Where it was like,
the tool could barely do it
and now it can.
But yeah, I think this
happens a lot in Claude Code.
I think that
the way I think we go
about is like,
we create these primitives
where it's like, okay,
how do permissions work?
How do visualizations work?
All of these things.
And then they sort of
layer together.
Tell me about loops, like,
how do you use them?
I mean,
I think it's interesting
to track the journey of
how we arrived at loops
in some ways. Right?
It's like, we like,
I used to run everything
locally on my laptop,
and at some point I had
to go back home,
you know, from the office.
And so I would have
to shut down my laptop
and I'd be like,
that sucks.

[00:07]
Like, my agent’s not
running anymore.
You didn’t leave it open?
Yeah, you could do that
but then I’d have to go
to the parking lot and like,
people would look at me funny.
Yeah, yeah.
But what
I started doing then,
was I started using like,
our remote hosted
developer boxes.
Yeah.
And so, like,
those were my way of,
okay, I don't need my laptop
on at all times.
It's just,
it's running and it's running
in a hosted environment,
so I can just do my thing.
Yeah.
But that's also unsatisfying
in some ways,
because then, like,
you got to, like,
you know,
ssh into your environments
and kind of get back
to your hosted surface.
And so that's when,
I guess,
Claude Code on the web
was created. Right?
So it's like hosted containers
that you have,
that can just keep running
in the background.
But even then, like it was,
it was a little tricky
to get started
because if you want to use
a container to host your,
host your dev environment,
you need to give it access
to your dev environment.
And setting that up
is a bit of a pain.
Yeah. It's totally worth it,
in my opinion.

[00:08]
I think it's like, you know,
10x my productivity
ever since we did that.
But that was kind
of the challenge there.
And so I think
that's the origin story
of like how
we kind of came across this,
Claude running locally,
to Claude needs to run on the cloud.
And now if it’s
running on the cloud,
you can do
really interesting things,
like you can have routines
and you can be like,
you know, every day go and
look at all the feedback
that we're getting
and look at, you
know, bucket them into
buckets of importance
and fix the ones that
it actually has
high confidence in fixing.
This is the whole like,
loop journey
that Boris talks
about a lot too.
It's like, you go from,
you know, prompting a model
in a session,
and you do,
like breaking that
boundary of like a session
and instead
prompting something
that's one level above that.
Yeah.
That's then going and fixing
bugs or, like,
doing your bidding for you.
Yeah.
I actually wanted to talk
more about code review
you know, and security,
because I think
this is one of those things
where, okay, you're
writing a lot more code.
More code
is being generated, and

[00:09]
you don't want your job to be,
like, reviewing code, right?
So, yeah,
obviously we have like,
our code review bot right now.
But generally I
wanted to ask you guys
about like how, you know,
code review has changed
inside of the team and like,
how we do it right now?
I think one big thing actually
has been, Claude
really helps human reviewers
choose where to focus
their time and energy.
I think like a common thing
that I saw happen
in traditional human
code review is
you would have someone go
and review the code
and they would like,
pick out, like,
you know, three
little nit picks to post.
And it was kind of just like,
I'm signaling to you
that I read this code.
It’s like, here's
my like three little things
that I want to point out
to prove that I actually
was like reading
through this carefully.
Now you can have Claude
figure out those little things
and address them autonomously.
So I was like,
that's not really
the important part
of human code review anymore.
Yeah.
What is important

[00:10]
is understanding
maybe the bigger picture.
It's like,
maybe Claude doesn't
have a full understanding of
why is this API structured
the way it is?
Or, you know,
the service boundaries
are drawn in a particular spot
for a reason
that maybe Claude,
hasn't fully internalized
when I was writing the PR.
So being able to pull
information
like that into code review,
and then hand that
information off to a human,
I think is a really valuable thing
that Claude can do
that keeps you from getting
pulled into that little, like,
oh, I'm just going to, like,
nit pick something
because I'm, like,
reading through the code
line by line and,
just level up the
abstractions
that you're thinking
about as a human code
reviewer.
I think code
review was the first time
where we did
this big fan out
where we're like,
okay, like,
how do you find,
you know, every bug, right?
Or how do you like search
across potential bugs?
And we do this big fan out
and then,
you know, coalesce it,
which is like,
you know, what we call
test time compute, right?
Like how we use
a lot of inference time

[00:11]
to put a lot of thought
and compute into a problem.
And this led to workflows,
right?
So could you tell me
about that Sid,
and how you built workflows?
Code review was a big part of
how workflows came about
in the first place.
Yeah.
Like we
we have this,
as you were saying,
like massive, fan out thing
where it was
kind of like a,
almost like, a custom harness
where you tell Claude to go out
and fan out and find bugs.
And then for each bug,
you might
do an adversarial review
where you ask it to
look at the bug
from three different,
you know,
opinions or
perspectives and
see if the bug is
actually real.
What that does is like it
filters out
all these bugs for you
and gives
you just
the most important ones
that require
or need your attention.
And it's not just code review.
Like you could do
the same thing for many,
many different types
or classes of problems.
Yeah.
You could do the same thing
for performance bugs
or performance issues.
You could do the same thing
for just general purpose
deep research. Right?

[00:12]
Like I want to figure out,
like, you know,
I'm taking my parents to Tahoe
next week and, like, okay,
where do I, where do I stay?
And you could do, like,
a fan out there and
that's helpful too.
Claude is actually really good
at making its own harnesses.
Yeah.
Like Claude
can figure out
what this fan out
should look like,
what the topology
should look like,
how it should kind of wire
in the output of one agent
into the next level,
and then, like,
finally summarize it
and give it back to me.
And so that was kind of
the origin story of that as.
And an example is,
okay, you're planning a trip.
So you have it like
do like ten different search
requests across like Tahoe,
like bathhouse Tahoe, Hotel
Tahoe, Airbnb or something.
Right?
Places to go.
Yeah.
It gives you
a bunch of results.
And then you have
some agents
that sort them or
figure out the most
interesting results
and then maybe
some agents who
verify them.
Is that right?
And then it gives you
an end result.
Exactly.
Like the problem
is really it's,
it's like you're fanning out
and once you fan out,

[00:13]
you just have so much
information,
that you need to
then filter back.
It's like a MapReduce problem.
Yeah.
And you need
to filter back
for human consumption,
because if I read the fan out
output I'm going to go crazy.
Right?
So you need something to help
build confidence
and the way to build
confidence in this case
is just to throw test time
compute at the problem.
And so you kind of build
more confidence that way.
I think the other thing
that's really interesting
about workflows is because
the agent is writing code to
orchestrate the sub agents,
it's this cool mix of
deterministic code
defined behavior,
as well as the, you know,
agentic LLM behavior.
And I think that that helps
give me confidence
when like Claude writes
a workflow to iterate,
you know, it's like,
here's a for loop that's going
to run over these items.
I'm like,
oh yeah, the for loop, it's
not going to skip
one of the items like it's
going to apply
the same technique
to all of these things
equally.
I find that that's really,
that really improves my,

[00:14]
my trust.
Like, oh,
I know that Claude is doing
what I want it to do here.
Want to talk about
Claude Tag.
Like, I know Robert, you're
building Claude Tag right now.
But. Yeah.
How are you using it? Like,
Tell us about it.
Yeah, yeah, I think,
so I mentioned earlier,
but we're using Claude
Tag to build Claude
Tag really aggressively.
Yeah.
And that's actually been
a lot of
my focus is making sure
that, like, Claude Tag
is unblocked
on being able to develop
Claude Tag itself.
Making sure that
the development environment
and dev loop are really,
really easy for Claude to use.
It can just, like,
do everything that
I, as a human need to do
to build the software and test
that it's working end to end.
As we build more and more,
complex, heavily
integrated pieces of software,
that job gets harder, right?
So that making sure that
Claude is able to do that
sort of thing has been
a big focus for me.
This is the first time
we've had the user interface
more fully decoupled
from the transcripts.

[00:15]
Okay.
So it's like,
we're actually like,
we are working now at a level,
one level of abstraction away
from, like the actual tokens
that are being output
from Claude.
So when you see a message
from Claude Tag in Slack,
it's calling a tool
to send that message to you.
Yeah.
But its internal monologue
essentially
is not visible to you
in Slack.
Like there is a link to view
the full transcripts
from Claude,
but the primary user interface
is through a messaging tool.
And that abstraction
was, like, a little scary
to get through at first.
We're like, oh, like,
I can't see everything
that Claude is thinking
as it's like thinking it.
Yeah.
But it's also been,
I think, really freeing in
terms of just like, oh,
Claude is choosing
what to say to me and when.
And I'm not thinking
about the details of like,
which tools is it calling,
what parameters is it
sending to the tools
as it's using them?
And like being forced
even to let Claude cook.
And seeing that the models
now are good enough.

[00:16]
Yeah.
That I'm getting back
good results without needing
to supervise the transcripts
in detail.
Right.
Is like, it has been a forcing
function of like,
Oh, yeah,
these models are actually
getting really good now.
Claude Tag
really clicked
for me
recently
because I've been
developing
a new tool.
I actually need
a lot of buy in from people.
So the first thing I tried
was like,
hey, like, I'm
thinking of this idea,
who should I talk to
who might be interested
in it? Right?
And then so
I get these stakeholders
and then I do some mock ups
and it's all in Slack.
So I can, like,
view it on my phone even,
it makes mocks
up for me.
It does the implementation,
you know, and then,
but the implementation
is like, you know,
I don't know if this
tool really works or not.
So I add a lot of like
events to it. Right?
And then I,
you know, deploy it internally
and see like kind of how
people are using it.
Then Claude Tag
is like monitoring it for me.
And I'm like,
oh, hey, like,
how are people using it?
Is anyone giving me feedback?
And then I can just like
drop in instantly
and be like, yes.
Like, you know, like
Claude tags me
when someone else
gives me feedback about it.

[00:17]
And so I can be like
more responsive,
I can have a higher
confidence that it works.
Right.
And then sometimes
I was looking at the events
and I wanted to improve
some of the funnel.
Like I felt like users
weren't going all the way.
And initially I was like,
I have an idea.
I'm going to like,
ask it to do this idea.
But then I was like, wait,
let me ask Claude
to improve the funnel.
You know,
like come up
with some ideas here.
And maybe I can give my idea
as an example,
but I want to sort of,
like, work with it at that
higher level,
and that, like, really
clicked for me.
I think you're touching on
some great points here, right?
Because effectively
there's verification,
there's code
review,
and there's getting feedback.
So it's like connecting
to your data store
or your event store
where you get feedback in
some ways, like maybe metrics
or maybe it's a Slack,
maybe it's a GitHub issues,
whatever else it is.
And all three of these
are primitives in Claude Code.
Yes.
Like verification
is so important
because like I think we,
for our team especially,
we have, you know,
really paid a lot of attention
to verification.
And so when Claude creates
a PR for me for Claude Code.

[00:18]
It tests it, it sends me screenshots
from what it would look like.
And then
you kind of get confidence.
So in your case too,
like when you were,
you know, asking you
to verify, like you didn't,
did you have to open up,
did you open up the TUI?
Only to like,
so first
I asked if to record itself
using the TUI, you know,
and then after I did that,
I was like,
I’ll like clone it myself.
And then try it out.
Just for sanity’s sake
I wanted to make sure that I
at least check.
Yeah, just to like,
you know, use it myself.
I feel like eventually,
you know,
I’ll just let Claude,
not even clone it.
I think looking back
at the evolution over the past
over the part year,
to me it’s
sort of like
we started with
Claude Code and then we
started adding
these primitives
that would work
like auto mode and memory
and workflows.
There was a lot to keep track
of as a developer, right?
To just be like, oh,
what's all this stuff
happening?
But you kind of
have to do that.
I do think that's like
the hard part about
being a software engineer
these days is like,

[00:19]
it's like
freeing your mind
kind of like,
there's so much.
I think you always
had to do is,
you always have to be like,
okay, what is possible now?
How do we like, automate more?
But I think, like,
how do we, you know,
step back and think
bigger, right?
I think is a really
important part,
but I am curious
if there's, like, anything
you guys miss about
the old part of software
engineering?
And how things used to work.
For me, I used to get a lot of joy
from performance engineering.
And so that means, like,
really digging into a system
and increasing
its performance.
I think Claude is much better
at that than I am now.
But I still get to reap
the benefits
of the actual performance
improvements, which is nice.
The other thing that I think
I've been focusing a lot on
is just creating
new ideas quicker.
So if I have an idea,
going from idea
to prototype to production
is much faster.
Yeah.
And so I think more of
my attention is now going
on, like new ideas
and how quickly
I can bring them to life.
And so it's like
I've had to shift
my kind of like paradigm from,

[00:20]
you know, getting really deep
into the weeds to like,
more zoomed out
over time.
Yeah. Yeah.
Like less mastery
in that specific thing,
of performance that you’re
spending a ton of time on.
Exactly.
I think kind of
a similar thing for me.
I'm a very, like detail
oriented.
I love to get into the
weeds of UI design
for my personal website,
like, I made this,
like super detailed
CSS recreation of the Mac
OS 10.4 aqua like buttons.
And I probably spent
like a day
like getting the exact layer
of, like, radial gradients,
like stacked up to make
this perfect recreation of it.
And like,
that's the type of thing
where I'm like,
oh, Claude
can just do that for me now.
And like, I wouldn't ever go
and do that manually now.
It kind of brought me
back to thinking about
when I was probably 7 or 8.
I really wanted to make
a video game.
Yeah.
And, like,
I didn't know how to code yet,
but I was just like,
you know what?
I have, like, PowerPoint

[00:21]
and I can use, like,
PowerPoint to like,
make, like,
clickable things and like,
draw these shapes and stuff.
Yeah.
It was like
that was a tool that
I was able to use at that age.
Thinking now
about how Claude kind of makes
the entirety of software
engineering accessible to me,
it's like whatever
idea I have
I can,
I don't have to be like, oh,
I don't have the technical
skills.
Like I'm not able
to solve this problem.
Like, I can say, here's
what I want to accomplish.
Let's like break it
down and figure out
how to work with Claude
to make it happen.
Yeah.
Just everything
kind of inside of that,
realm of software
engineering feels like
it's within my grasp now,
which is really exciting.
I feel like software
engineering
is like the profession
of change.
You know, like,
I think you look back
like 10 or 20 years
and you're like,
oh, like, you know.
You're like handwriting
JavaScript without like,
any sort of frameworks.
And then you invent
frameworks and,
you know, compilers
and all of these things.
And, it's happening faster
now, but it's still like

[00:22]
fundamentally
software is about
how do you use these things
to create something
incredible and
make more
and more great software,
right?
It's like problem solving.
Like you say.
Exactly.
You're solving
different problems,
but you're still problem
solving.
Totally.

</details>
