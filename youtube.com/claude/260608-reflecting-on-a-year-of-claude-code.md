---
title: "Reflecting on a year of Claude Code"
channel: claude
url: https://www.youtube.com/watch?v=Hth_tLaC2j8
youtube_id: Hth_tLaC2j8
published: 2026-06-08
duration: "18:07"
captions: en
---

# Reflecting on a year of Claude Code

[![Reflecting on a year of Claude Code](https://img.youtube.com/vi/Hth_tLaC2j8/hqdefault.jpg)](https://www.youtube.com/watch?v=Hth_tLaC2j8)

<details>
<summary>자막: Reflecting on a year of Claude Code (18:07)</summary>

[00:00]
When we first released Claude Code,
it was like a little video
and I remember posting it to Slack,
and there was like two people
that gave like the reactions
and like people were like excited.
I thought it was really cool,
especially for my very easy
engineering tasks.
It was quite good at it.
That's like a really nice way
to say that
it wasn't really good.
I can't believe
it's only been a year
since we first launched
Claude Code.
It's hard to remember what
what that was like.
Like, it’s so different
than what we're doing today.
Like, now I just have, like,
armies of agents
that are doing stuff like I'm
prompting one agent
or I have like an agent
that's like prompting agents,
that's prompting agents.
And it's like a tree
of like thousands of agents.
But I think it's just like
the most important idea
when working on this stuff
is like, every single time
Claude makes a mistake.
I don't tell Claude
to do it differently,
I tell it to write it
to the CLAUDE.md,

[00:01]
or to like make a skill or
or something
to do it differently.
And if you can do this,
then Claude
can just like run forever.
And I think the other thing
that we kind of realize is
the verification
is really important.
Like we didn't realize that.
I hear this come up
a lot with developers
and enterprises
that we meet with.
What are your tips for making
a really good
making Claude Code really good
at verification?
I sort of feel like this
is this thing that
just like everyone misunderstands
because whenever we talk about
verification,
people are thinking like unit tests
or they're thinking like lint
or like type check.
These are the things that are
obviously really easy to automate.
And these are the things
that were already automated.
But actually when we talk
about verification
for agents, it's
something slightly different.
It's like can the agent run
the thing?
It takes a little bit of
mental work
to figure out
how exactly do you do this,
because it's often
not straightforward.
And I think that's like,
that’s one of the challenges.
I remember
I remember with Opus 4
Claude tested itself.
And we just like
hooked it up to Opus 4
And I was like, Claude
build the feature
and then test yourself
in like bash.

[00:02]
And it opened a little Claude
CLI and tested
its own feature.
And I was just like, whoa.
It's crazy!
Like now,
now we're so used to it.
Like now, you know, now
we have these loops going for,
you know,
like the iOS simulator
and the Android simulator
and like computers
for desktop,
like it's not surprising.
But back then that was crazy.
How are, like,
how are you doing it?
So I've been mainly
hacking on the desktop app
these days.
And one of the engineers
on the team
actually added this desktop
development skill
that teaches Claude how
to run the local desktop app.
And I've been having it
use it,
and it still runs into issues
or like bugs
with the staging environment
sometimes.
And so what I have it do
is in those cases,
I have it read
Slack and understand, hey,
is staging down right now?
Or has someone
else already hit this?
And then when it
debugs the whole issue,
I tell it to update
the desktop development skill.
What the skill does is
Claude actually spins up
a local desktop app,

[00:03]
and it uses computer
use to click around on it.
And so when I add a new UX,
it clicks around
to invoke the new UX.
It also tests edge cases,
and when there's an issue
it fixes it and re-checks.
This is like honestly,
one of my favorite things
about this team
is everyone codes.
I've never been on a
team where, like,
my PM would code
and it's like crazy and like
your code is like really good.
You’re too nice.
But I also just feel like it's
it's also just becoming easier
because it's like essentially
Claude writes the code.
And so what matters
a little more is like,
what's the idea that you have?
And I feel like
if you're a person
that has like
the product context
and the business context
and you're thinking
about the design and the user,
you're just going to come up
with better ideas.
It's kind of like
all the roles are merging.
I remember seeing Megan
our designer’s PRs
and I was just horrified
at the beginning
I was like, oh my God, why is
Megan putting up PRs?
And then she was like,
yeah, yeah.
I'm just like,
I'm fixing the button.
And I was like,
okay, all right, well,
the code looks good,

[00:04]
so maybe it's maybe it's fine.
And I feel like now it's
just like it's totally normal.
Yeah, and we see this across
all the enterprises we talk with.
Like, it's the engineers adopt
Claude Code first
and then the, the eng adjecent
roles look over their shoulder
and they're like, whoa,
this thing is very powerful.
Let me try it out.
And we found it's crazy.
We found that, like,
our designers are more
productive making prototypes
and making changes
directly in the app
instead of pinging an engineer,
PMs are making changes in the app.
Our finance team runs
and in Claude Code,
they do their projections there.
Data science.
Like if you talk with our
data scientists, it's so cool.
It's just like everyone just has
Claude Codes up on their screens.
I feel like it's remarkably versatile
for different roles.
What do you feel like nowadays,
are the use cases
that are pushing the limit?
One that I'm super excited
about is routines.
There is one engineer
on our team
who launched voice mode across
all of our products.
And, he has his routine set up
that just listens for

[00:05]
every ticket that comes,
every GitHub issue, every
bug report about voice mode.
And his Claude just picks it up,
proactively puts up a fix,
and then pings the PR to him.
And when he got that working
for voice, he thought, okay,
we're getting a lot
of other feedback
that isn't being responded to.
So, he also set up a routine
to listen for that.
So I ship this, small feature.
And there was like an edge
case in it that I didn't see.
And so someone filed
a bug for it,
and I was going to
get to the bug that night.
And my Claude was working,
it said, wait a second,
another Claude
has already fixed this.
And I was like,
how is this possible?
Like, I've never talked to him
about this feature before
and so I pinged him,
and I was like,
how did you fix this
so quickly?
And he said,
he has another routine
that just looks
for bug reports
that haven't been responded
to in five hours
and puts up a fix,
and he merges the ones that
are easy to verify.
Claude tells me this
like all the time now.
That someone else
has already fixed it?
There's always like
another person’s

[00:06]
Claude that's working on it.
It's like, yeah, that's
been one of the changes.
I feel like we're,
a while ago
we were trying to figure out,
like, how to use routines,
and I feel like
just like the agent SDK
was this first idea
that we could use Claude Code
programmatically. But
I feel like at the beginning,
it just wasn't obvious.
How do we use it?
What do we use it for?
And I think routines are
the first
really obvious application.
And I don't know, like
it just does like all the code
review,
it babysits like every PR,
you remember back in the day
you used to actually
have to like respond to code
review comments.
You used to have to like
fix CI. You used to have to rebase.
Yeah. Like I haven't done that
in a long time.
Yeah.
When you're in the CLI
and you're synchronously
working with Claude,
what are your go to features?
Okay.
What they used to
be is plan mode.
I don't use that anymore.
What do you use instead?
Auto mode.
Auto mode?
It’s the best.
Instead of plan mode?
Instead of plan mode.
Yeah because the newer models
they don't actually need
like a planning step anymore.

[00:07]
I think this was really
important for like Opus 4
through maybe 4.5.
Then I think starting with
four six and definitely with
four seven, it just doesn't
need that planning step.
I think some people
still use it.
They like to have that artifact.
I don't use it
And I just do
auto mode for everything
because then I start my Claude,
it starts to work
and then I just like move on
to the next Claude
and I don't have to sit there
and watch it.
But from the very early
stage we had this
like permission prompts model
for Claude Code, right?
Like it runs a tool
and then it asks you like,
hey, are you okay
running this tool?
And you had to say yes or no.
And at the time,
that was kind of the best
we had a year and a half ago
because we didn't have,
you know, classifiers.
The model was not as well
aligned as it is today.
So auto mode was just such a
it was such a big step up
because actually
you don't want to read
most of these requests.
Just routing it
to a different model
and having it check for
security works so much better.
Yeah.
And if a thing like
is a little suss or,
you know,
this isn't the command that
you think you want to run
or it's not safe,
the model will just deny it.
And then you can go back
and you can allow it later.

[00:08]
I think this has been
one of those, like, step changes.
We just, there's no way
we could have done this a year
and a half ago.
It's just human nature,
when you accept
99% of requests, that your eyes
just glaze over
when you read it.
And so actually, we feel
that auto mode is more safe
than reading
every single
permission prompt,
because it means
that your only paying attention
to the most important thing
and not like being spammed
a bunch of things
that are just 99% yes.
I think security
is one of these things.
Like you can talk about it
and then
it's a totally different thing
to actually do it correctly,
because it just doesn't
always look
the way that you think
it's going to look.
And it's just all about
like always red teaming,
always pentesting
always looking,
you know,
always having a threat model
and then using that
to figure out,
you know, how is this thing
going to get attacked?
How are people going to get
prompt injected?
And I just feel like
like the team
is just like obsessed
with this.
And it's so important
because as a result,
I just trust the agent to run
and I can move on
and I can just have
like a second agent.
And if I didn't trust it,
then I just wouldn't
have been able to do that.

[00:09]
And internally,
to actually get auto
mode out to our users,
we needed to really
trust it first.
And so what we did
was we collected thousands
of transcripts
of like an entire agent
trajectory
and a permission prompt
and had auto mode classify
whether or not it was safe.
And it was extremely good
at this.
So then we got red teamers,
and we asked them
to try to prompt inject,
and try to hack
the code base.
And we use this
to create evals
and make sure
that all of these were denied.
And then we had our own
internal teams
try to prompt inject and
hack Claude Code’s auto mode.
And then we improved auto mode
to make sure
that we caught all of these.
So it's not only just protecting you
against the vulnerabilities
that are out there
in the wild today, but,
the most intelligent attacks
that we can construct.
Yeah. I mean, it's like,
it’s honestly
like a weird approach.
I feel like there's, like,
all these features
the last year
where the first time
someone pitched it,
I was like, no way,
that's not going to work.
And I feel like over time
I just learned,

[00:10]
like I'm actually wrong,
like so often now.
Because, like, building on
the model is so weird.
It's just like all this,
like, engineering stuff
that I've learned over the
years.
So much of it I just have to, like,
throw out.
And this is just like part
of what the job is now.
We're building on a new thing
and we just have
to relearn it.
And auto mode was
definitely one of these.
I was like,
the first time I heard it,
I was like, route
the prompt for a model?
No way.
That's not going to work.
And then it actually
turns out empirically,
it works really, really well.
But I heard you also love
loop.
Yeah, I love loop.
How do you use it?
I think for loop, there's
this transition
that we went through
like a year and a half ago
where we were like,
all right there’s source code.
But actually the thing
an engineer should interact
with, maybe
it's not the source code,
maybe it's the agent.
And so we made this leap of
I don't write the source code,
I talked to an agent,
and the agent writes
the source code for me.
And I think right now
what's happening
is we're making the next leap.
I don't talk to an agent
anymore.
I talk to loop or I talk to a routine
and it prompts Claude for me.

[00:11]
And it's just it's crazy.
I mean, it's been like,
it's a year and a half
and this was like
two big leaps.
If you take like, a step back,
how are you
seeing entire engineering
orgs change?
I'm going to put on my
business cat hat.
I have this, like,
favorite case study.
This is like a Harvard
Business Review from the 90s.
And they were talking about,
like, computers are here.
Why are we not seeing
the productivity benefits?
And it's just this, like
amazing snapshot into like,
what it actually felt like
at the time
because, like, you know,
people used to use mainframes.
At some point companies
switch to personal computers.
It was sort of a new thing,
and the companies were trying
to figure out
how to use it.
The same way
they're trying to figure out
how to use AI right now.
And it turned out that
to get the productivity
benefits from computers,
what you had to do isn't like
you have your paper
filing cabinet and your, like,
paper and pen
business process.
And then there's like
a computer on the side
that does something.
Actually, what you have to do
is you throw out the filing
cabinet,
you have to throw out all
your paper and all your pens,
and then you put a computer
in the center
and everything has to run
through the computer.
It has to be at the center
of every business process.

[00:12]
And I feel like at Anthropic
we do this thing
where when you on board,
you don't ask people questions
like no one asks me
questions when they on board.
You probably have
the same thing, they ask Claude.
And this
is kind of weird, like,
this is the first company
I've been at like that.
And I feel like for us, Claude
is just at the center
of everything.
Whenever I have a question,
I ask Claude.
Whenever I write code,
I use Claude.
Whenever I need a code
review, Claude does it,
whenever I need a security
review, Claude does it,
whenever I need to
you know,
fill out a form or something,
Co-work does it.
So it's just like Claude is
at the center of everything.
And I feel like the companies
that are really
figuring it out,
and there's
a bunch of them now,
they're just putting
Claude at the center of it.
And I think for computers,
the transition
took 10 to 15 years.
But actually for AI,
because so much of our work
is already digitized
and Claude can use a computer
and it can write code
and run code.
This transition is happening
a lot faster.
I think it's just like,
really, it's
just really exciting.
Like,
I feel like
now I don't
have to bug people anymore

[00:13]
and when I
interact with people, it's
because it's like fun
and I get to collaborate
with them on stuff
and we get to create something
together.
It's not that like,
I need them.
I need something,
you know, from them
because, like, Claude
can actually do
a lot of that stuff now.
And I also feel like
as an engineer,
I've just never had this much
fun doing engineering
because the
like the tedious part
I don't have to do.
Like I'm
just coming up with ideas.
I'm talking to customers
and every idea, like,
I don't have a
to do list anymore.
Like Claude
just builds everything.
And so my job is to come up
with these ideas
and it's just so fun.
Okay, so here's a question.
Is the future product or engineering?
Like, is everyone going to be a PM
or is everyone going to be
an engineer?
Everyone's going to be both.
I feel pretty strongly
that these roles are merging.
Like when we look at our team,
our product team
all writes code.
Our Devrel team all writes code.
Our design team all writes code.
And then we look at our
engineers and a lot of them
ship products end to end.
They have an idea for what
to build.
They build it.
They work with legal
and marketing to figure out

[00:14]
how we communicate this
to the world
and make sure it's safe
and with security, too.
And a lot of times
they just see through
this whole process end to end.
So I think right now
AI really benefits people
people who have a lot of curiosity,
have a lot of product tastes
who love to have this
like end to end ownership.
And now a lot of people
are running
like hundreds of agents.
What are the products
that you think
people should be adopting
as they transition from single
to multiple to hundreds?
Until recently,
the way that I wrote code was
I had like six terminal tabs
with six git checkout
on the same repo,
and then I would just like tab
between them.
Now it's pretty different.
I have like one tab,
I use the new agent view
that we just shipped.
It's like so good.
And I'm so glad
that we took a while
to iterate on it
to make that really good.
And I also use the desktop app
because I don't have to fiddle
with checkouts that way.
It just like, you know,
it does the work tree cloning
or the like, it
creates the work trees for me.
And the thing
that I would not have expected

[00:15]
six months ago is probably
half my engineering now
I do on my phone.
So I just have like
I have so many agents
running that
I just start for my phone.
I use a remote control,
which is like amazing now
and like I will start
something on my computer.
And then I’ll just remote
control in from my phone
and I’ll just like, walk around
I’ll get coffee,
and then I'll check in
on my agents
and maybe
I'll start another agent.
And sometimes I'm like,
talking to someone
and we come up
with a new idea.
I’ll just start an agent on the spot.
I like talk to it
with voice mode
and just have it build
something,
and I don't even have to go
back to my computer anymore.
I remember
when you started doing this
because you would actually
leave work,
have your computer
on your desk
open, plugged
in, screen locked,
and I just thought you would,
like, come back to the office
at some point
to get your computer,
but then it would be like
pretty late and I was like,
maybe he just left it here by accident.
And then it happened again
the next day.
And then it happened again
the next day.
And I was like,
wait, it's so weird
because you're landing PRs
but your computer is right
next to me,
and I remember you responding
and you're like, yeah,
I'm coding from my couch.

[00:16]
Yeah,
that was the week the remote
control got really good.
Yeah.
So another thing that users
are asking
about all the time is
how do you do
context engineering,
especially
in a large enterprise?
This is a thing.
You know, people used to talk
about prompt engineering.
They used to like work
context engineering.
This is sort of matching where
the model was at the time.
Back in the days
of Sonnet 3.5,
you had to prompt engineer
back in the days of Opus 4,
you had to context engineer.
But with the models of today,
you don't do any of this.
You give it the minimal
possible system prompt,
the minimal possible tools,
and then you let the model
figure it out.
Like you just have to give
the model some way
to pull in the context.
I think that's
the most important thing.
How do you think about it?
I see things very similarly.
I'm a context minimalist,
so my general philosophy is
tell the model
only what it needs to know
and let it figure out
the rest of it.
I think
when you give the model
too much context, it's
kind of like
you're micromanaging it.
And sometimes the model knows
a better way

[00:17]
to get to the same outcome.
And I personally prefer
to give the model that freedom
to do that.
And then in general, we're
also making our harness
more lean
so that you have more room
for your own prompts.
And so that follows
your prompts better.
There's all these
different ways to Claude now,
but I feel like in a year it's
going to be
a totally new set of things,
and it's
going to be so surprising
if it's still these
same things,
because I think, like
we're seeing
these giant trends happening
right now,
agents are running for longer.
They're more autonomous.
Very rarely am I running one
agent at a time.
It's usually like a few agents
or dozens
or hundreds or thousands.
And so like the form factor
for that, it's
going to be really different
than what came before.
And I don't know
what it's going to be.
And I think
in a large part, it's
going to be up to the team
to figure it out.
And this is,
this is why I'm like,
so happy we run the team
that the way that we do,
where everyone just comes up
with ideas
and everyone is able
to think about the product.
Everyone talks
to users all the time
because I don't think
these ideas
are going to come from us.
It's going to come
from the team.

[00:18]
Totally, and from everyone
in our community
building with us.

</details>
