---
title: "How we Claude Code"
channel: claude
url: https://www.youtube.com/watch?v=IlqJqcl8ONE
youtube_id: IlqJqcl8ONE
published: 2026-05-23
duration: "31:43"
---

# How we Claude Code

[![How we Claude Code](https://img.youtube.com/vi/IlqJqcl8ONE/hqdefault.jpg)](https://www.youtube.com/watch?v=IlqJqcl8ONE)

<details>
<summary>자막: How we Claude Code (31:43)</summary>

[00:00]
Hello, hello, hello. Welcome all. Thank
you for joining the workshop.
We have a pretty, pretty full house here
today. I'm very pleased to see that. Um
quick show of hands
who here loves Claude Code?
Okay. Yeah.
You're in the right place. Yeah. Yeah.
Lovely to meet you all. My name is Arno.
I'm a member of the Applied AI team. I'm
an architect there. I'm here today to
tell you how we Claude Code at
Anthropic.
Do a workshop and uh
you can code along. You'll get some
credits. I think there'll be a QR code
in just a moment, so make sure to grab

[00:01]
that. Uh there'll be people floating
around that might support you. So, if
you have technical difficulties, we can
we can help you out.
Um
Anybody here in this room who hasn't
used Claude Code before?
Okay, great. Good, good, cuz this is uh
there's more to do. There's more to find
more more to find out. I'm happy you're
here. Let's get started. So let me get
my clicker.
Ah, yes. Excellent. Yes, please, please,
please
grab the QR code
set yourselves up.
There'll be a repo here as well that you
can clone.
Uh there are three phases in it. We're
going to work through.
There's an interesting verification
setup that you can work through
alongside me and it's quite detailed, so
you probably will want to investigate it
a bit later yourselves.
What we're covering today
is based on uh this version of the talk
that Tariq gave in San Francisco just
about a week and a half ago. Who here
follows Tarik on on Twitter?

[00:02]
Fantastic. Great. Yeah. Yeah. So, he
published that as a blog post called The
Unreasonable Effectiveness of HTML
files. And um
he's basically pitching that moving on
from markdown files, we're going to be
using HTML instead. And we're showing
some of that today. Like I said, there's
a repo to go along.
Uh
in enjoy that along the way and later on
in the in the week as well.
Where are we now? Where's this all
going?
I think everybody probably notices that
agents are becoming more and more
capable. Why is that happening? That's
happening because the models are
becoming more and more capable. And so
if the models become more capable, it
means agents can run for a longer and
you can give them more and more complex
tasks. But that also means that we have
to change our way of working. You have
to change our habits. That's part of
what today is about. How can you change
the way that you're working with cloud
code to get more out of it?
If you're going to let your agent run
for a longer period of time,

[00:03]
then you can burn through a lot of
tokens if it does the wrong thing.
And you want to avoid that ideally at
the beginning.
And so that's where the idea came from
to to to push more and front-load more
of the verification that the human would
do in the spec into an HTML file because
it's a more rich and more
um
more human ergonomic way of engaging
with the content that your agent is
going to be building for you.
And we'll see how that works.
There are a bunch of things around
agents that are worth reading. We have a
lot of engineering blogs on our web
page.
Um we also have the the standard blogs.
You should check all of those out.
There'll be a lot of information there.
There's a lot of interesting information
about harnesses, about long-running
agents. All of these things are
important. Today we'll focus on
three levels. Um and there'll be some
something a bit more basic, something a
bit more next level, and then something
that's quite interesting and that'll be
a bit more in-depth.
The first thing is

[00:04]
the more capable the models get
the more you should try to resist
constraining them. Who here, by the way,
has heard of the bitter lesson by
Richard Sutton? Great. Fantastic. This
is This is great. So, I'll I'll I'll For
those who haven't raised their hands,
uh, Richard Sutton is basically the the
father of reinforcement learning. If you
were reading a book about reinforcement
learning, it's probably authored by him.
And, um, his idea was basically that
you know, you could spend all your time
trying to
with your human capabilities hardcode up
front and constrain the system,
but in in the end, pouring more data and
more compute at it
ends up getting more capability than
anything that you could have come up
with. And there's a similar analogy
here, right? The The models are becoming
more and more capable.
And so,
you should accept that the model is
probably better at extracting
requirements from you than you are at
defining your requirements. The The
requirements are latent within you, just
like when you talk to your users. Your
users, they have an idea of They know it

[00:05]
when they see it,
but they're often not very good at
articulating what they need. And
likewise, you probably know what you
want when you see it, but Claude is
likely better at extracting what you
want and what you need from you than you
are in specifying it to Claude. That's
another direction to take this in.
So, we'll talk about that, removing
ambiguity, letting Claude
prompt you and interview you in
prompting.
Then, how to then understand and plan.
We used to do this all with with
Markdown files. We still do it with
Markdown files. Colleague of mine once
said,
"The Markdown file is the lingua franca
of the AI native software development
life cycle." That was pretty poetic.
Um,
but it seems like that format is a bit
constrained. It's getting too long with
a lot of lines of markdown file to read.
We can condense more information into
HTML files, and that's what we're going
to do today.
And then, how to verify.
Not test, actually, but just to verify
in this context. Um

[00:06]
how to make verification native to the
thing itself, so that the agent can
drive it alongside a human. Or
eventually not, headlessly as well.
That's where this is all going as well,
right? The agents are going to be doing
more and more of this natively. And how
can you set the artifacts up
to
natively be testable and verifiable in
the way that you need.
So, we'll do an example.
By the way, has everybody had a chance
to get grab that QR code and uh set
themselves up? Very good. There'll be a
link to the repo eventually as well. I
think that comes in a bit.
Uh let's say we want to do a bill
splitting app.
Uh
very simple, um you know,
you want to
you go out with friends, you want to
find out who owes what. Yeah.
Um let's let Claude interview us around
doing this. Uh so, in this case, I'm
actually going to
Yeah, before I do that,
give you an example of how you would do
this and how you could do this better.

[00:07]
Yeah?
What's good prompting? What's bad
prompting?
Bad prompting is when you say, "Just
make it better." And a lot of people
that I watch uh using Claude code just
type, "Make it better." Um make no
mistakes. Yeah.
Uh that's not good prompting. Um
you want to incorp-
you want to encourage Claude to extract
from you specific details. So, you give
give the domains. Don't over specify
the outcome, but specify the areas that
you are interested in, right? That's
what makes this good prompt on the side
different and better. Um
Remember
you know, focusing on the audience, for
example,
or
uh suggesting an open-ended way to
answer the question as opposed to
predefining it up front. And then that
will prompt Claude to iteratively
interview.
All right. So,
um I've got a Claude open here, two
different Claude's.
Who here has used fast mode?
Okay, not that many people use fast

[00:08]
mode. That's why set it up here.
Um
and
who here uses auto mode?
Oh, I'm very happy that you all use auto
mode. You need to be using auto mode. If
you're not using auto mode, you need to
be using auto mode. It makes it so much
easier. Um
yeah, use auto mode. Good. Who here is
setting their effort parameter?
Good. Good. Our recommendation is X
high, but you can also set max effort. I
mean, in my case I think I kept it at X
high for this.
Um
yeah, yeah, yeah.
So, just to touch on how those look,
right? Like we've got forward slash
effort,
which is the effort parameter, forward
slash fast,
which is the fast mode, which is I've
I've turned it on.
And then uh we have uh
the auto mode, which we cycle into like
this, shift tab, yeah? Auto mode is the
best. So, I'll copy-paste my my You all,
when you have the repo,
will see um
one of these prompts is in there. So,
I'll just copy-paste the prompt in here
on the the bill splitting app.

[00:09]
So, okay. Claude's going to ask me uh
you tap through these, right? Like
you'll tap through these like this.
Uh and in my case, I want to
uh I want to just for friends.
And
I wanted
uh
Is there a secondary audience? No, no
secondary audience. And we'll leave that
as that.
The key thing here in the prompt is that
you want to use You want to prompt
Claude to use the ask user question tool
that you saw me use in the prompt
earlier before. Let me submit those
answers.
And then it'll write that spec, right?
So, you you saw me in my prompt
explicitly referring to the
ask you a question tool. That's what
triggers this workflow, and you know,
depending on how well you specify that
prompt, you'll get better outcomes. So,
it'll generate a spec. We could then
turn that into
a bunch of different ways of of of
building the app.
It's going to take a while, so we'll go

[00:10]
back to my slides. Could I go back to
the slides, please?
Great. So, let's say we have a plan.
Generates a plan. We've answered some
questions. It
it's getting better at extracting turn
by turn from me what I actually want
without me having to
up front verbalize everything myself.
Then I want to be able to check, is it
what I want?
Well,
an HTML file is more dense,
much more information dense, much more
ergonomic for you
to understand what the thing is going to
look like. You can even use a screenshot
with it. You can use the Playwright MCP
later on for that as well, right? You
can interact with it much more
richly than you could with a very long
markdown file. And especially if the
markdown files get, you know,
they get more than about 200 lines long,
it's unlikely you're going to read it,
and certainly unlikely that your
colleagues are going to read them.
Before we started here, I had Claude
with Opus 4.7 generate a few examples
for me of what this could look like with

[00:11]
my bill splitting app, and we'll look at
those now.
We have them here.
The prompt I used is in the repo that
you'll have access to. I asked Claude,
"Give me a few different directions,
four different design directions,
explore them, generate them as HTML, and
let me explain it explore them across
each other." And they came up with these
different ones. So, one sort of
brutalist, one Tokyo fintech.
We'll we'll click them all one by one.
So, this is what this one would look
like.
Uh and then this one this one might look
like this.
Completely different aesthetic, right?
And I click around and
And this is much better for me to give
feedback to Claude on than it would be
to just try to infer from a markdown
file what the thing is going to look
like. I could go in and like I said,
take screenshots, feed them back into
Claude. Who here
regularly takes screenshots to give
information to Claude? Very good. You
should be doing that. That's very good.
Um especially when you're when you're
doing front end, it's really hard to
articulate like
the thing is slightly off or there's a

[00:12]
misalignment here and it's like you'll
find that you run into the limits of
what you can express and it's actually
easier for especially Opus 4.7, which
has a much better vision model than
before, um to extract from you what the
problem is and proactively.
Great.
So, a few examples. Tariq has a lot more
in his repo, which you'll find in the
repo as well online. So,
so far,
we've covered
letting Claude extract information from
you interactively
as an interviewer because
the longer you let a run an agent run,
the more important it is that the spec
is comprehensive, the less likely it is
that
you will be able to upfront define
everything and it's better for you to
iterate with Claude
in that manner.
Then, what's a better and more efficient
and ergonomic form factor?
Um
it would be the HTML file.

[00:13]
And now,
the more important part from all of this
is how to verify what Claude has done
and how to make it agent native. And
that's what we're going to cover with
the repo.
I think we have uh
I think there'll be one slide where
you'll get to see the actual slides to
to engage with uh the actual URL to
engage with. So, what you want to do is
make it part of the artifact. And that's
what we're going to cover today. In
fact, there's part of what we're doing
today is we're going to we're going to
use
Storybook fixtures, a testing library,
sort of data emissions,
and attributes,
and Playwright MCP for a React
uh for a React app um
with with components that you will have
seen before,
but remixed in a way to make it easy for
Claude as an agent to
extract the data contracts in the DOM,

[00:14]
and then run verification, and then even
record the verification, which is how
the Claude code team that Tariq is on
runs this, and that's what the demo that
he built refers to, right? Like it'll be
a generation of verification steps that
get run through, they get a recording,
and that's then put on S3 or uh shared
somewhere else with colleagues, and
that's how you turn these verification
steps
into something that is generated by the
agents, and then that you
have fewer and fewer touchpoints with.
That's something that you can replicate
especially from that repo.
The way to do that is to sort of
sensibly modularize, uh but that becomes
really clear when we look at the actual
the actual thing.
So, I encourage you
to
go to that link.
There'll be a repo.
This is the repo
under CW you see workshops, Claude with
Code workshops.
And there's the one for today's session,
which is how we Claude Code.

[00:15]
What's covered in there is phase one,
which we just covered, right? The simple
prompt to say, "Hey, I'm writing a bill
splitting app. Interrogate me on the
requirements so that I don't have to
miss any in my upfront description to
Claude." The second one is
generating four different HTML design
directions that we could explore
uh for me to then feedback on and for
for me to decide. And then thirdly, we
have a verification framework here.
Uh
and it's in a different context. It's
not to do with the
bill-splitting app. It's regarding a
to-do app, a small to-do app uh
uh written in React. And
we're going to show how we built
verification entirely into that
along the way. That's described in
detail
in the readme for phase three and then
also in the verification detail as well,
which is here. So, if you want a deep
dive
on how this is set up,

[00:16]
you can read this.
And it's all provided in the repo. It's
pretty cool. What is it focused on?
We've written a
a small to-do list uh
app here.
I can add an item.
test
It's hard to see. There we go. Very
good. And then I could tick it off and
drop it as well.
And I could clear the finished items.
And so, many things are happening here
in terms of the state. And we'd like to
verify that it's all working alongside
the tests that are already defined.
Uh but these verification steps, we'd
like them to be driven by an agent. And
there are three ways that we're going to
do this. So, we're going to do this in a
human-readable way.
Um but then that same way of doing it in
a human-readable dashboard, we're going
to verify uh
in an agent-first way um and let Paul do
that separately. And then there's a
separate way in the in the repo as well.
You can just run um
run run verify and then it'll just run

[00:17]
the test matrix there. You'll get a
slightly different result if you do it
from the repo versus here, but
the the principle is the same. So,
human-readable,
agent-driven if you're doing it from
from cloud code or somewhere else, and
then also just generally headless like
you might do it in in CI.
We'll have a look at it in a bit more
depth. We'll go here into the app
and we'll actually look at
There we go.
We'll look at elements.
We have here
the actual emitting so the the emitting
different data data aspects, the data
verify unit, the total done and active.
Um the component itself here is
publishing its state to the DOM.
Uh
and so if I change my if I change my
state here, if I make I might add
test again.
See that updates. And then I drop it, it
updates again.
So, this is what
the agent can read later as opposed to

[00:18]
having to scrape the DOM. You can just
if you publish the state here separately
from the React internals,
you'd be able to
run the verification independently of
what whatever the state of the app is.
Um and that's how this is set up to
work. Uh
and then you can run this
further down the line as well.
Each one of them gets this, right? If
you look at um if I if I pull up the
That's a bit hard to read. Let's do that
here. Um ev- every every component gets
one of these, right? There'll be
schemas, there'll be fixtures, um the
known states, and then there's the
invariants. Uh
There are particular ones here that that
always have to hold have always have to
hold. You'll test them with probes. And
we'll do one example which we've
hardcoded but we've hardcoded an example
that will fail the verification and
we'll let
the human verified dashboard catch up
and then we'll also let the agentic way
of doing it catch up as well and we can

[00:19]
let Cloud Code find it and diagnose it
for us.
So, that same approach also works here.
So, I've got the dashboard
defined here.
And what we see here is, there you go.
Um
like I said, we've got the different
schemas, the the invariants that we've
defined.
And we can run these, right?
Individually, we can see
how they would execute here.
Got an example here.
Or also
I could run all of them. In fact, I'm
going to do that now.
I run them all. One of them triggers
artificially
because we planted it before.
Going to scroll down and find out what
that is.
And it's here.
Uh
we will actually look at how
we can replicate this for an agent as
well.
And we would do that like this.
Go here.
Inspect.

[00:20]
And we could run
basically the manifest of all the
different verification steps that are
defined here as state in the DOM.
We can get them in the same way that we
have them here.
We expand that. It's getting a little
bit small.
As an example like that.
And then like that as well.
Great.
If we do that,
then we can also actually run them uh I
just specifically here.
I'll do it manually first.
Let me reply.
Uh we play them all.
Close that.

[00:21]
In this case, we're running this
not to perform the verification, but but
to provide the evidence of the
verification. We can later on record
this. We can record these as clips which
will just be videos we capture. And then
we would
uh store them, share them with
colleague, put them on S3 or whatever it
might be.
Let me pause that here.
There we go. So, here's our summary.
We have one that's deliberately failed.
I'll explain that in a second.
But in each case
you can also see
the details of how this was done.
The key thing here is that we want to um
it's important to include the probes to
to push off the happy path. And then
a lot of this will be generated by
Claude for Claude, right? So, there's
there's a way of scaling this further.

[00:22]
Um in the end, we'll go to the one that
didn't work.
So, the one where we hard-coded that the
sums do not match. In this case, the the
state doesn't match. Uh 3 +
uh uh
3 + 4 does not equal 10
in this case.
And
we'll get the same result if we
run
verify all from from the Claude here as
well.
And we'll let Claude do that in a moment
as well.
There we go.
Then it's a little bit hard to see what
there's
pass pass pass pass pass and fail.
So,
there we go. Okay, good.

[00:23]
We can change this, right? I can
the point here is that I'm I'm trying to
show that the
the idea is to let
something agent native be read as the
DOM contract here.
Um that's what we established earlier
that the state is managed here or well
not managed but at least um
viewable to an agent that it can then
run the verification end-to-end itself.
And we can let Claude do that afterwards
as well.
In this case, we can also make a change
that will break more. Let me see if I
can break
the chain. I'll break the contract but
not the app.
And I'll do that here.
So I could change for example here.
Under
Exactly. Under to-do app, total stats,
I'll delete that.
I'll do undo that afterwards as well.
And

[00:24]
if we now we run
then all of these ones at the bottom
here
will fail.
And we'll get the same
when we run this again from here as
well.
Oops.
There we go. All of these are failing.
Not because we broke the app but because
we broke the contract.
That Claude can then
natively verify.
Excellent. Great.

[00:25]
I want Claude to tell me what's going on
with these ones. List the Well, not the
ones that I broke, but I'll undo the
ones that I broke. But, I'd like it to
tell me what's going on with this one.
And so, let me correct
the change that I made before.
Control Z.
Auto save.
Rerun.
And there we go.
So, we've done it manually and we've
shown how we can match what the agent
would see versus what we would do. But,
we can let Claude run this headlessly
itself as well. So, I'll do that and
I'll pull that open.
So, let it run.
This one's broken deliberately.
And the rest works.

[00:26]
Great.
So, we have Claude running here.
Uh I mentioned fast mode before. I
mentioned auto mode, which is great. I
mentioned forward slash goal.
In this case, what we're going to do
is let Opus 4.7
help us find out
why that particular verification failed.
I've already connected the Playwright
MCP for this.
Uh oh,
um it's going to use that.
And it's going to run. Schema got
rejected. 4 + 3 does not equal 10. Uh
yes. If you were to run bun verify,
uh
run bun verify, then you would actually
pass the tests in this case,
uh because we deliberately put the
verification in wrong just to
demonstrate, but then the test metric
itself will actually pass.

[00:27]
Um
But the idea here is to separate out
what you could do as a human versus then
what you could do
the end agent directly from the browser
using
basically these
the commands that you saw. And then also
what you could run headlessly directly
from the CLI.
If you wanted to do it
like this as well,
then you could record the outcome that
we talked about.
Yes. So here,
I in this particular setup, you've
actually got the ability to to show how
you would record these. Um the same
delayed running that we've shown, you
could run and record
as evidence. Basically to show that it
would work,
and then you could store that.
Uh
and then you could run
like that.

[00:28]
This is very common right now.
Um
the
the cloud code team
uh records basically all the code
changes that they do like this. Um all
the front end changes at least.
Uh
especially on the run there
at the pace of the shipping that we have
at the moment.
Are people able to pull up the the repo
and get the verification set up working?
Yeah, very good. Very good.
Hm?
Yes, you can store them. I mean, like
you can just put them in S3 or whatever,
or short share them with colleagues, or
um in our case we have a version we have
a we have a internal This is more of an
automated than what I'm showing here. Uh
in our case we do record them. Um not
certain for how long or in what context,
but uh it's part of a regular cadence.
And then you get the
In fact, you get the
I should have triggered that.
Did you all see that?
There we go. So, you can you have each
clip.

[00:29]
You could download all of them or
download them individually and then
that's basically the bundle that that
that proves the verification worked.
Um
So, I guess
to
bring it around to what we've covered so
far and then where it's going.
Three different surfaces, the the human
surface, right the
um
and then the the agent first from the
browser
um mapping on the same way.
And then you can also run it in CI with
just run bun verify.
The
objective here at the end is to figure
out how do you embed
the
verification into the artifact itself.
There's more detail. I encourage you to
check out the repo itself.
Um and actually run a few examples
yourself and run a few tests. Right, you
can change the code, see what breaks,
rerun it yourselves. Um

[00:30]
it's quite detailed and it's what Tariq
and and team use in the Cloud Code team
uh for their work already. This is a
this is this came
uh pretty quickly um just a week and a
half ago into this demo. Um
So, I encourage you to check this out.
What's new really is the remixing
and the the new arrangement of of
of of
of primitives that you're already
familiar with that you're already using
just to make it available to the agent
first.
That concludes really what I wanted to
cover.
Um
I encourage you to spend more time on
the repo.
There's great documentation there and
you can actually
um
get a lot out of it with Opus 4.7. Opus
4.7 works really well because it has a
better vision model. That's where this
really excels.
If you use Sonnet, I I wouldn't
recommend that. I'd say try using Opus
4.7 for it.
Try using fast mode for it. Fast mode is

[00:31]
great, costs more, but it's great for
iterating quickly on specs.
People will sometimes ask, "Well, isn't
a HTML spec
more token inefficient?"
And the answer tends to be no.
And the reason is that in the long term
you iterate less if you have a good and
rich
HTML spec, even if and one-off instances
you spend more tokens to generate it.
So,
you can even try it with fast mode. So,
that would be it. That's my
recommendation to you.
I enjoyed speaking to you and thank you
for your attention.

</details>
