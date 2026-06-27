---
title: "Making agentic workflows trustworthy and verifiable with a custom DSL"
channel: claude
url: https://www.youtube.com/watch?v=qOjleN2-50c
youtube_id: qOjleN2-50c
published: 2026-05-22
duration: "29:39"
captions: en-orig
---

# Making agentic workflows trustworthy and verifiable with a custom DSL

[![Making agentic workflows trustworthy and verifiable with a custom DSL](https://img.youtube.com/vi/qOjleN2-50c/hqdefault.jpg)](https://www.youtube.com/watch?v=qOjleN2-50c)

<details>
<summary>자막: Making agentic workflows trustworthy and verifiable with a custom DSL (29:39)</summary>

[00:00]
My name is is James Brady. I work at
Allicit. And today I'm going to be
talking about how we make our agentic
workflows trustworthy and verifiable
with a custom domain-specific language.
Okay, so
uh in terms of the the structure of
today,
I'm going to start with a high-level
overview of why we went for a DSL in the
in the first place.
Talk a little bit about the language,
how we made the decisions we did
um in its design.
How we integrated it into Allicit. We'll
do a quick demo.
And then uh and then wrap up at the end.
But uh let me start with a question. So,
let's say that two systems produce
identical output.
Do you trust them equally?

[00:01]
And the answer is, of course, well, it
depends. It depends on
what went on inside of those systems to
produce that output.
I would say that the
the the mechanism, the how of how how an
answer is produced is as important and
important in a different way compared to
just the the final output itself. Let me
try and make this a bit more concrete.
So, let's say you're running a static
analysis tool over your code base.
And it runs for a while and in the end
in the end it says, "This code is free
of security security vulnerabilities.
Safe to ship to production."
I would contest that if you knew the
system
was built on, let's say, an older model,
3.5 Sonar, something like this. If the
system is using an older model like
that, this is option one.
And option two is it's a latest and
greatest state-of-the-art model. It's
done all sorts of tool use. It's done

[00:02]
critique and redrafting. That's just a
fundamentally different kind of an
object. The
The message might be literally
identical, but you would react very
differently to those two messages if it
came from a kind of older model that
was, you know, not so powerful versus
something that has a used a lot more
tokens and and intelligence.
So, the mechanism matters.
And there isn't a a sort of single
correct mechanism. There isn't a kind of
single canonical
um
best way of designing the internal
structure of of the systems that you're
building. I really think that it's a
it's a design choice. It depends on what
it's you're trying to do. It depends on
the domain that you're building with
building in. It depends on the user. It
depends on the task, like what it is
that the user's doing within the domain.
We found that there's definitely a speed
versus rigor trade-off. So, if you're
trying to do something which is
uh extremely in depth and extremely
defensive and extremely high quality,
that naturally takes a bit longer than

[00:03]
uh than than something a bit more
surface level.
And there's no, you know, there's no
correct answer. Sometimes you want you
want fast and sometimes you want really,
really high quality.
Uh the provider's brand and taste is
interesting here. So,
uh I don't know if I would have called
this before we started working this
ourselves, but Elicit prides itself on
super high reliability, really high
quality, data provenance. We really kind
of stand behind the results that we put
in in front of people. I'll show you a
demo of what I'm talking about a bit
later on.
And these are some of the some of the
concerns that we had in our mind when we
were thinking about, well, what is the
We know the mechanism matters, but what
is the right mechanism for us at Elicit?
And uh I think it came down to these
three desiderata when we were building
out our research agent, which will be
the demo in in a few minutes.
So, firstly, the research agent's
process must be legible. It needs to be
legible to the user and also, by the
way, it needs to be legible to other
agents. We want for um
the

[00:04]
the the process, the algorithm, the kind
of like internal set of steps that the
that the agent is taking to be
um spot-checkable by the human,
spot-checkable by other agents. We can
run you know, sort of critique agents
over it, that kind of a thing.
The second desideratum, the iteration on
the process retains fidelity. This is
maybe
Let me explain this a bit more because
it's it's a bit of a fiddly one.
What I've found and I maybe what some of
you found as well is that if you're
iterating on a piece of work and you're
saying that's not quite right, it's kind
of going this other direction. Oh, you
know, I I want to add this other layer,
this other consideration.
I found that you can sometimes drift a
little bit from what you were initially
trying to do and the model ends up
getting a bit confused and you have to
say, you know, let's start again or
backtrack or something. It's kind of
kind of kind of annoying. And it it
definitely harms trust. So, we want to
avoid that. We want to be able to add to
the work. We want to be able to add
layers. We want to be able to be able to
go in different directions without
losing that kind of

[00:05]
uh clarity and consistency of what the
user was initially interested in doing.
And lastly and certainly not leastly is
the process is followed faithfully. So,
let's say we've got the process, it's
legible, we've checked it, the user's
checked it. It's great. And we've
iterated on it and we've kind of stayed
true to what it is the user's interested
in. Well, we have to actually ensure the
system does in fact do that set of
steps, otherwise, you know,
what are we what are we doing here?
So, uh
those are the considerations that we
foregrounded when we we were thinking
about how we want for elicit elicit to
work. And that that led us to reaching
for a DSL. I'm not saying that everyone
should be using a DSL, you shouldn't.
What I'm saying is that these three
things really kind of led naturally
towards well, a DSL could be a great
choice for us. So our DSL is called Ash
PL. The kind of weird smushed together
AE thing is apparently called Ash. It's
like an old English um
diphthong or something.
Uh

[00:06]
so Ash PL and this is our domain
specific language for the agentic
workflows in the in the illicit um in
the illicit product.
And Ash PL has a few distinguishing
factors. So uh firstly it is Turing
incomplete. It's relatively simple.
There's no loops. There's no uh yeah
there's no there's no recursion. There's
no there's no mutation. It's purely
functional. It's a reactive language and
it's an opinionated subset of of Python
and the opinionated is is important
here. So it's not just a kind of generic
simplification of Python if you will.
Not like Python with couple of bits
taken off at random.
Um what we did is we
uh we disallow we sort of take out the
language features of Python that just
aren't aren't that helpful and we add
stuff in. We add some extra primitives
in which are specific to our domain. So
our domain is scientific research and uh
empirical decision-making high-stakes
decision-making.
And the primitives that we put into our

[00:07]
DSL match that. You know we've got
retrieving academic uh research papers
or clinical clinical trials. You know
things things like that are are built
into the built into the language.
Okay. Um
yeah let's have a look at some Ash PL.
So hopefully this isn't too small for
you all. Um you don't need to read the
the code obviously.
Uh what I'm trying to show here is that
the Ash PL on the right looks a lot like
Python because it is a subset of Python.
Uh we're keen on types. It's it's it's
typed. That lets us do uh fast kind of
redrafts if you've got a type error.
And I think this example program uh just
FYI was the
the process that we wanted to go through
to do a competitive competitive analysis
for illicit itself. So, we're looking
for other
academic search engines and AI
assistants. It looks like systematic
review tools. We're We're doing web
searches for those. We're joining the
results. We're enriching the sources,
you know, that This is the kind of the

[00:08]
set of steps that we want to go through
that we think is a good process for
doing a competitive
landscape overview.
And um
the core engine of what goes on within
an illicit user session is that we have
a component which I'll show in in in the
in the next slide, which is writing the
ASPL.
And then we interpret the ASPL. That's
just done in like plain old Python code.
And then we redraft the ASPL based on
what just happened. So, in a simple
case, you can imagine
we write we we we write some ASPL.
There's a type error. Okay, there must
be a problem. So, that gets kicked back
to the ASPL kind of writer component. It
tries again, fixes the type error. We
reinterpret the ASPL.
It runs this time. We get some results
back. We rewrite the ASPL. There's that
kind of constant loop of
writing and then interpreting and then
rewriting and then interpreting. And
that's that's like the core

[00:09]
engine of of making progress inside of
inside of illicit.
Okay, so that's the language. Let me
show you how we integrated it into um
into like more of a into more of a
system. So, we have the UI in the top
left. That is what the user is is
interacting with. It's just in a in a
web browser. That's what we'll have a
look at in a second in the demo.
The
The UI is talking to an event log
that can append-only event log. That's
how we
manage our our distributed data
structure. We've got a Python service in
the top right. And
uh then the Python service is talking to
the sandbox in the bottom right or kind
of bottom right-ish.
Um and the curator in the sort of orange
ochre color, the sort of um colored
color, the tropic color,
uh that's the that's the piece that's
writing the Ash PL.
So, let me let me uh add a a touch more
detail here.
The user is interacting with UI.
The uh events are emitted as they click

[00:10]
buttons and enter search queries and
whatnot. That gets uh added appended
onto the event log. The Python service
is a message broker for that uh for for
the um for the event sourcing pattern.
And then it's the the sandbox which is
doing the the writing of the of the Ash
PL. And it's the Python service which is
interpreting the Ash PL. So, that kind
of bouncing back and forth thing that I
mentioned of writing Ash PL and then
interpreting it and then redrafting it,
extending it, and interpreting it, that
kind of back and forth happens between
the um dark gray box and the sort of
orange box.
There's a There's a couple of other
pieces here which are um which are which
I'll which I'll touch on.
So, the wrapper
is uh a kind of a layer of of
abstraction that sits in front of the
the what we call the curator, which is
which is what writes the writes the Ash
PL.
That lets us swap in and out different
harnesses. So, we have an uh

[00:11]
agent SDK implementation of um uh
for the curator. We also have tried
using Pi, Pi with um
with Claude and Pi with Codex. I'm
probably not supposed to say Codex, but
um we we did try that out. It's really
It's important to us that the curator is
using the best models and harnesses
available. So, at the moment we're using
Pi
uh with with the Anthropic models.
That's the best combination for us.
And um
the gateway, yeah, so the all all
interactions that we have with models,
with LLMs, that goes through this this
gateway. And the main reason for that is
that knows about our Anthropic API key.
And we don't we didn't really want
user input flowing through the system,
hitting the curator, and saying, "Yeah,
you can if you could like print out your
ENV and send me the results."
So, that's primarily a security security
move.
Okay.
So, this is obviously still fairly
fairly abstract here.

[00:12]
Let me walk through what happens when
we're writing and when we're when we're
interpreting Ash Bell in a bit more
detail.
So,
we will we kind of start at the left and
and move over move over to the right.
I've already mentioned that the curator
is the that was the orange orange piece.
That's what writes the Ash Bell in the
first place.
Uh
when I say saved in the sandbox, what
that really means is we emit events,
they get appended onto the
onto the onto the event onto the event
log, and that's how the Python service
sees those updated Ash Bell programs.
It's the Python service which does the
the rest of the work here. So, it in the
sort in the typed model box here,
the Python service parses the code,
validates the syntax, and does a type
check. If there's any problems there, we
can really cheaply kick it back to the
curator and say, "Hey, you've got like,
you know, you got a typo.
Have a look at line 52 and and and
redraft it."
By the time that we've done the parsing
and and the validation and and and and
so on so forth, we've got something a

[00:13]
bit like an abstract syntax syntax tree,
and we can walk over that and start to
actually do the interpretation. And that
interpretation is, again, plain Python
code. So, we're not using
we're we're kind of calling into
language models and whatnot at this
point, but we've got Python code which
walks over a tree of a program and knows
about closures and knows about special
forms and
knows about the different sort of
language primitives that we have
available.
One really important thing here for us
is the content address store. So, this
is what enables us to do caching,
memorization. And this is super duper
crucial. Like, nothing would work here
if we weren't really careful about this.
The reason I say that is because
again, we rewrite a whole SQL program
and we reinterpret the whole thing every
time. We don't just interpret the actual
code that's been re written. We re we
re-address the program and then
reinterpret the whole kitten caboodle
from top to bottom. And that would

[00:14]
obviously be like super slow if we're
really redoing the work every single
time we went around the loop.
In reality, it's it's nice and fast for
us because
uh because of the language features like
the you know, it's a pure language that
that really helps to with memorization,
we can hash uh an expression and say if
this has been evaluated before, we just
store that away
in um
in a map. And if we if we meet that
expression again when we're when we're
walking the tree, we can say, "Oh, yeah,
this this like
this boiled down to 42 or something." We
can just use that straight away from the
hash.
Uh okay, I think that's all I want to
say on this one. So, I'm going to switch
to a demo now.
And um
the
uh
I said before that there's often a
trade-off between rigor and speed. On
that on that continuum, we are very much
focused on the rigor uh side of things.
We do do things quickly if it's a simple
query, but that's not really where

[00:15]
we differentiate ourselves. It's not
really where our special sauce is uh so
to speak.
So,
if you go to elicit.com, um you would
see something a bit like this. We have a
bunch of uh
sort of templates you can start with
creating table slides, drafting a
report. Um I'm going to show you a
research landscape,
which uh
again is like a much I think it probably
took in total,
I don't know, like a couple of hours or
something of of it doing work and me
adding layers on top of it, so can't do
it in a demo format. Uh, but I've got a
session saved away that we're going to
take a look at.
Uh, but yeah, yeah. It doesn't need to
take that long. It's just, you know, it
gets a bit a bit more interesting when
it's a more in-depth thing.
So, this is the research landscape that
we're going to take a take a look at
here. And my initial query was to map
the companies and institutions investing
in foundation model models for biology.
And you can see that the first thing
that we did here was Alissa asked asked
me a question. It was like, "Okay, I get

[00:16]
the kind of overall big picture. Let me,
um, narrow that down a little bit. Are
you interested in a broad landscape?" I
think the other options here were you
you interested in something,
um,
like a you know, a particular foundation
model in more interested in academic
institutions or companies, that kind of
a thing. And I just said, "Yeah,
the broad landscape."
Um, is is what I'm looking for.
And then the rest of, uh,
the rest of the steps here are driven by
Ash PL. So, this, uh,
first analysis step, you can see, if
anyone can't see this and needs to be
bigger, then please do say.
Uh, you don't need to be able to read
all the text in detail, but okay.
I'll go with that as it is.
So, this first analysis block, we're
doing a bunch of searches. We're looking
for academic papers relating to genomic
foundation model pre-training
transformer. We're doing some web
searches.
Uh, we're trying to fetch the full text
of papers when available. We're doing
some screening, like filtering. All of
these steps, all of these stages, uh,

[00:17]
are encoded into Ash PL, and then we run
they're actually, um,
the Ash PL is not just a representation
of a plan. It is literally the plan
which is executable, you know. Uh, that
that's what lets us really be be sure
that we're following through on the plan
as as stated.
Um so, let me go a bit deeper here.
That was the kind of first the first um
analysis stage of us looking for
organizations, looking for institutions.
Looks like we did Yeah, did some more
analysis here. I think this one is All
right, at this point we've got some
actual institutions. We've got Howard
Hughes Medical Institute, Stanford
University, et cetera.
Um again, this is all coming from HPL.
We're doing some more searches. We're
doing some more searches. We're doing
some more screening. Um yeah, you can
see we go pretty deep um when we when
we're in this mode.
Let me skip forward to the results here.
And I'll get this sidebar out of the
way.
So, uh after some humming and whirring

[00:18]
and um quite a few tokens, we end up
with a table like this. We call this an
artifact, and uh each row is a In this
case, an organization which has got some
kind of a interest in biological um
foundation models. Got GDM, we've got
Meta, Microsoft Research, et cetera, et
cetera.
And you can see that we've extracted
some
uh some attributes alongside that from
the foundation models that they've
created, uh the modalities that they're
that they're interested in, notable
collaborations, it looks like.
So, I've been saying that this is driven
by HPL, but um
how do you how do I know that? Uh
you know, what's the what's the
connection here?
For each of these artifacts, we can
actually look at the HPL code that was
used to to generate it. So, um this is
literally the the executable DSL that
was um
behind the creation of that table we
were just looking at.
And you can see that first of all, we're
doing some uh
some web searches for foundation models,

[00:19]
uh multimodal biology AI model that you
know, you can you can see this.
Uh looking for academic academic papers,
again.
We are I guess joining these together at
some point. Uh, yep, that's where the
join is.
Um, and uh,
as you can probably tell, looking at the
AshPL is not particularly fun.
Um,
most people don't do this and and that's
not really the the kind of the core
driver of why we have this. We we have
this because we want to know that a list
of the system is following and the the
following the instructions that we came
up with, right? Like that's the kind of
primary thing.
Um,
it is useful for other agents to be able
to look at this AshPL though and say,
you know, you've you've missed
something, you've overlooked something,
you have, I don't know, there's a
there's a a key search that you've you
should have considered or there's a part
of the user's query that that you didn't
uh, take into account. Uh, so that's
something which is which is really handy
when the plan is so legible in in this
format. Something which is a bit more

[00:20]
useful from a user perspective, a bit
more ergonomic, is a uh,
a graphical representation of what's
done within the system. So, this is um,
derived directly from, um,
you know, from from the AshPL.
This isn't just a kind of
um,
I don't know,
a made-up nice visualization or
something. It literally is derived
directly from the same thing that the
that the plan uh, was executing over.
And I think in this case it's it's
pretty pretty linear, so it's not super
interesting, but um, yeah, we start off
with a couple of searches,
did some enrichment, which means
fetching um, full text of papers, that
kind of a thing, extracting,
um,
curating, which means filtering, do some
more searches, etc. So, I I do actually
find looking at this to be quite handy
if I'm trying to
convince myself or not that I would
endorse the process that the that a list
of the that a list of took. Uh, and you
can quite qui- quite quickly notice when

[00:21]
there's something that looks a little
bit um,
skewiff.
But,
I wouldn't be I wouldn't stop here
necessarily, right? Like there's other
kinds of um
layers to this investigation that I
might want to add on. So,
I think I did a few things there. Yeah,
I asked for a comparison of open and
closed source strategies for the
different organizations. We did some
work for that.
I then asked for
the commercialization commercialization
strategy, the GTM approach, and we did
some work for that.
I then asked for
um I think you know, you can see where
another artifact was created.
Um I think the next thing I was
interested in was I missed a missed a
block here.
Here we go. Yeah. Mapping out the
different government orgs and other kind
of oversight institutions. I did some
work for that. And then And then at the
at the end of this user session of my
user session,
we have um
I asked for a join, right? So, we've got

[00:22]
effectively a table of data which is the
organizations. We've got a table of data
which is the oversight bodies. And just
in natural language, I can say I kind of
want to I want to join these together
and see how the labs have been have
interacted with the oversight bodies.
And uh that's come up with this table.
Uh we can see how Anthropic has
interacted with um US AI Safety
Institute and AC in the UK and and so on
and so forth.
Um
And if I look at the
uh AshPL for this
table,
what you might notice is that the top of
the program um is identical to what we
had before. So, this is this these are
the same web same same web queries and
paper queries that we had for that very
first table we were looking at.
And this is all the same code. It's got
the org mentions. The I guess the join's
going to be down here a little bit. Like
this is the same stuff as what we were
looking at before.
The difference is this program is now
a lot like a a longer. I think the last

[00:23]
one was
I don't know, 100 lines, 150 lines.
We're up to like a 1,000 or so, a bit
bit a bit more. And it's only when you
write down here
that we're starting to talk about
um yeah, you can see that we're looking
at the oversight
uh oversight bodies and the in and the
interactions between those and the and
the labs here. Here we're talking about
oversight. This is the sort of a
the the model for a lab interacting with
a with an oversight body. And at the
point of generating that last table, we
would have interpreted this whole
um program again from scratch, except
this that cache that I talked about. So,
the fact that we had already done
all this stuff up here, we'd already
done all these all these web queries web
queries and paper searches and and so
and so forth, meant we can interpret the
whole the whole um program from scratch,
but you know, the vast majority of it is
is just memorized and you get it back

[00:24]
straight away.
One of the reasons we took that design
design decision is because
um
it's easy to be confident about and and
and make statistical guarantees of of
kind of cohesion and correctness when
you're literally interpreting the whole
program every single time. You know, if
you're just interpreting little
snippets, that's where the drift can
come in that I mentioned before. That
That's one of the places the drift can
come in.
Uh
okay.
So, um can we switch back to the slides,
please? I think that's that's it for the
that's it for the demo.
Um okay.
Again, I'm not saying that everyone
should be using a DSL. It's
uh
it's not the easiest thing to build.
Uh I don't know, it wasn't it wasn't so
bad, but um
it's the kind of thing that you should
reach for if
the desiderata for your product and for
your organization points you in that
direction. And if they do, it's great.
We we're really really happy with how

[00:25]
it's working for us. But again, Ellicit
is uh based on and and kind of really
anchors around
high quality, dependability, robustness,
data provenance, all that stuff that I
was just talking about, and that's why
we went for it. If you're in a similar
position, or you can think there's some
other desiderata that could lead to a
different DSL that might be a good fit.
Here are some of the things that you you
should be should be thinking about.
So, firstly and most obviously, you need
a DSL. And the uh agent ergonomic piece
here, what I mean by that is
firstly,
we have found that
you'll have a better time if you base
your DSL on an existing language that
has a lot of
examples of in the training data because
then, you know, it doesn't the the the
model, the curator in our case, doesn't
need to like learn the syntax, uh right?
It just needs to know there's a subset
that it can go for.
Um
and um
I would say
a surprisingly small amount of work went
into the DSL compared to everything

[00:26]
else. Everything else is kind of like
conventional software engineering to
really turn it into a a system that
works.
And that's where the majority of the of
the work was there.
So, I mentioned the wrapper. Um yeah,
that's like letting you switch between
different harnesses
uh and models.
Um interrupt handling. So,
when you're in an Ellicit and you're,
you know, waiting for the results to
come back, you can add other things into
the chat, and we want for that to
gracefully flow back into the curator so
it can redraft its plan without stopping
the world. That isn't something that any
harness handles natively, so that's
something we had to build.
We can come back to sessions in the
future and like rehydrate them, so we
had to whole build a whole thing for for
that. That's not really a native
feature. Credential isolation is that
wrapper thing that I mentioned.
Um there's a
weirdly annoyingly amount of
an annoying amount of stuff to handle
messages coming out of the models and
make sure that they're not just like
lost to standard out. You know, just
like if you've worked with models a lot,
it's the kind of stuff that you're used
to being a bit annoying.

[00:27]
Um
And number seven, yeah, we use event
sourcing. We We're really happy with
that pattern.
Uh that's not a small lift. Um I guess
you don't need to I think I think most
people would probably need to do three,
four, five, and six.
Would recommend number two. I guess you
have to do one. That's obvious.
Um number seven, you have to do
something there. And eight,
I've not mentioned this, but yeah,
I I I guess I said before that we're
really pri- We really pride ourselves on
accuracy and um
uh and robustness and and truth- and
trustworthiness. And we have a dedicated
eval team who are great. Uh
It's so hard to do eval when the the
system is like writing programs and
executing them on the fly. Like it's
just a very complex dynamic um
domain to begin.
Um but we've invested a lot of time
there, and I'd really strongly recommend
that you do the same. Um
if you're doing a kind of DSL DSL-based
system.

[00:28]
Okay. So, let me uh let me finish where
I began.
The uh
example I gave at the beginning was
let's uh let's imagine two systems
produce identical output. And
should you trust it?
I think it's it's not crazy to imagine
Opus coming up with one of those tables
that I was just showing. I didn't show a
bunch of the fe- I just because of time,
there's a bunch of features there that
um
are really important to us, but at
certainly at least at a surface level,
the table itself isn't like a crazy
thing to imagine a state-of-the-art
model coming up with.
However, the fact that we go through a
very particular
um and sort of painstaking process to
generate it, and we expose that in a
ergonomic way to the user, you know,
right with the ASPL and that graphical
interface and a few of the bells and
whistles. I think that's the thing that
makes me think and know from
conversations with our users that they
hold they would hold those two things
quite differently. Like a a table like
that in in a lucid is a is a

[00:29]
fundamentally different thing to a table
that's just you know being bubbled out
from a from a model. Um and maybe
there's something that kind of
has that same dynamic for you for your
for your business and and for your
product.
So, yeah. My My pitch here is not that
you should go and use a a DSL.
Um
my pitch is that you should care a lot
about the mechanism.
Um because the mechanism the mechanism
matters.
Okay.
That's it for me. Thank you very much.

</details>
