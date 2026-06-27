---
title: "Evals for taste: Hill-climbing a slide-generation agent"
channel: claude
url: https://www.youtube.com/watch?v=v9FTCvkV_a0
youtube_id: v9FTCvkV_a0
published: 2026-05-23
duration: "39:16"
captions: en-orig
---

# Evals for taste: Hill-climbing a slide-generation agent

[![Evals for taste: Hill-climbing a slide-generation agent](https://img.youtube.com/vi/v9FTCvkV_a0/hqdefault.jpg)](https://www.youtube.com/watch?v=v9FTCvkV_a0)

<details>
<summary>자막: Evals for taste: Hill-climbing a slide-generation agent (39:16)</summary>

[00:00]
[music]
>> Hello. Hello. Hello. Good afternoon,
everyone. I hope you all had a wonderful
lunch. Um there's so many of you as
well. I'm actually kind of surprised by
this. Um
happy to see that there's that much
interest in talking about uh Evals. Um I
personally am a big fan of anything
Evals related.
But I know not everyone's That's not
everyone's cup of tea, right? Um
so very happy to see this many people of
you. Um
So yeah, this So today's session is
really going to be about Evals. Um and I
guess my
goal for this session is for you all to
be afterwards to be inspired to build
Evals, to be like, "Okay, Evals are
actually really useful."
Um and how you can act on them, right?

[00:01]
Like, we're going to be building Evals.
I want you to get a better sense of
like, "Okay, how should I be thinking
about building Evals? What are useful
type of Evals? And then also, how can we
use and take these Evals to then make
better agents, right?" So that's the
main goal of this session.
Um and the way we're going to do this is
by building a slide generation agent and
then finding out like, "Okay, what are
some good Evals? What do we want to
measure? And then, how can we build now
better agents based on the feedback that
we're getting from our Evals?"
And the first thing that we all need to
set the stage on is, "What are Evals,
right?"
So Evals are systematic tests that
measure how well an AI system performs
on a specific domain or use case, right?
So they give you information about like,
"What's the quality of the results? Um
what did it do well? What was it not
good at? How can we improve, right?

[00:02]
And evals they are made up of tasks
define certain scenarios
that then encode certain expectations
through the grading logic. So, one way
that we're thinking about evals is
if you for example are building an AI
system and AI agent and you want to make
sure that the output adheres to like a
certain type of quality or you want need
to make sure like this must always be
present.
Evals are a way to kind of encode this
behavior in a way where then afterwards,
if your evals fail, you know like, okay,
my agent is not doing or behaving the
way it is intended, right? So, that's
the way how we can use these evals.
And then evals is also the bridge
between things like it seems to work or
like
we know it works or maybe it's all like,
ah, it kind of feels a little bit worse
today for some reason.
It's always very hard to act on these
types of vibes, right? Like I think
vibes definitely have their own place. I

[00:03]
think they're useful just to get like a
general sense check of like how people
are feeling. But they're not very
actionable, right? And that's kind of
what you want to get out of evals. We
want to have something that's
actionable.
So, then
we always ship eval. Like we always once
we release like a model, we always have
this accompanying benchmark scorecard,
right? And then we always list like, oh,
these are like a bunch of evals. This is
what we achieve, what our models
achieve. We compare them to other
models. We compare them to competitor
models, right? Um
And there's like always a few usual
suspects, right? Like for example,
um
SweetBench is a very famous one which
measures agentic coding abilities.
Terminal Bench is one that's also quite
popular. But we also have other types of
evals, right? We have like tool use and
agents like for example like Tower
Bench,
OSWorld, which are some other evals that
measure different things. And then we
also have like reasoning and knowledge
um like Arc-AGI too.

[00:04]
Um
Now, this is all fine and dandy, right?
And then you look at these evals and we
always every time a new model releases
like, "Oh, we stopped off the benchmark
for these and these um evals, right?" Um
and they give us like a general general
sense of like how well is the model and
how much did we improve upon previous
versions, right?
But
for you guys, if you're like building
something, if you're building an agentic
system,
this doesn't really say much usually,
right? Like
because like we we don't measure for
example like
a very specific use case that you guys
are building on, right? We measure these
generic general benchmark that measure a
lot of capabilities,
but they might not be applicable to your
specific use case, right?
So, that's why we always say build your
own evals,
benchmark the different models,
benchmark your AI agent, and make sure
that you get the most out of the models,
and make sure that you're also using the
right model for the job.
Right?
And so, why are these evals specifically

[00:05]
important? So, this is my pitch to you
of start using evals, right? So, without
evals, suppose you don't have evals. I
think we've all been into the scenario
where
you have like this agent and it's
working fine, and then you get like this
feedback of like a customer who is like
saying like,
uh it's it's not really up to par of
like this new model switch, ma it's
something is off, right? It's very hard
like to do anything with that
information, right? It's just like,
"Okay, um
do you have some logs maybe that we can
take a look at some specific instances,
right?" And then you try to like debug
it manually, right?
But in a way, you're still flying blind,
right? You're always in a reactive loop,
so you wait for the feedback and then
you're like, "Okay, let's see what we
can do about this, right?" So, you
basically only catch issues in
production. You can fix, for example,
like one issue, which then might, for
example, create multiple more down the
line by making, I don't know, prompt
change tweak that suddenly
degrades the capabilities on like other
tasks that you haven't even considered.

[00:06]
Um it's it's also quite annoying to
distinguish like genuine feedback from
noise, right? Um which is always you
don't want to act on every single thing
that you see because people have also
some um biases in the way they perceive
these things, right? Um
And then finally, I think which is the
most important one is there's no way to
verify improvements or regressions on
anything that you're building or that
you've done, right? So, you like need a
way to make sure that the changes that
you are making to your agent are
actually impacting the quality and
making sure that you improve upon the
previous versions, right?
And so, this is basically what evals do
give you. If you add evals, you have
clarity. You need to define what does
success look like, right? Because like
if let's say you don't have evals,
right? And you're not even able to
articulate like this is how the agent
should behave. This is what the
successful end product would look like
for my agent, then how can you make sure
that your agent's actually behaving
properly because you can't even vocalize
it to yourself like this is what it
should be. So, building these evals
forces you to define, formalize in a way

[00:07]
what you expect your agent to do.
Um
It also allows you, as I said, to
iterate on optimal agent configs.
Um
you can also adopt new models faster,
right? Instead of like saying like oh,
we might test out this new model and
then see if it's like okay. You now have
like some clarity to say like okay, this
is better on this and this is not better
on this and this is why we should or
should not migrate to a new model. Which
especially I think is quite relevant
with the pace of new models coming out.
I think it's also like just taking this
load off your back of always constantly
having to find like okay, what is the
new frontier, right? Um
And then finally, making problems
visible before launch, right? So, you
know, like, oh, if there's like a few
um cases that you have that we always do
well or that you trust to provide a lot
of insight,
that's where you get the most value out
of evals.
And so, how how do evals really fit in?
So, originally, um when we were like

[00:08]
thinking about like prompt engineering,
we had this basically this flow of like
how you should optimize a prompt, right?
So, first you develop your test cases,
which are the evals in the end. Then you
write like a prompt, you test out the
prompt against the tasks, you refine the
prompt a little bit, and then it goes
back, you run the prompt again, you
refine it until you're like, "Okay, I'm
doing good great on my evals. I'm
confident that my system is working
properly." And then finally, you can
like ship the post polished prompt,
right? Um over time, systems have gotten
a lit little Oh. Ooh, can I go back?
Can we go back one slide, please?
Thank you. Um so, over time, it has
gotten a little bit more complex with
now agents coming into the loop with
like tool calls, skills, all the
different ways to optimize your contacts
and all that stuff. So, over time, these
systems get more and more complex.
So, it's also way more levers that you
can pull to make changes to your agents,
which makes it once again then more
important to have evals

[00:09]
that forces you to have concrete way of
identifying these are the things that we
can change, and these are the things
that impact the system in a positive So,
once again, like with agents, it's the
same flow, right? Um
except now with just way more and way
more complex things.
Um
evals, when you create them, there's
basically a few graders. A grader is
what we consider basically
a way how we can judge the output,
right? And like one of those ways is,
for example, a code-based grader, which
is pretty similar to, for example, a
unit test, as you might know in like
software engineering, right?
It can be like a string match, rejects,
maybe a fuzzy fuzzy match,
but it's like a strict analysis, right?
It finds static
and tool code checks and the advantages
of this one is it's fast, cheap,
deterministic,
but it has a big drawback which is that
it's brittle and it also lacks in
nuance, right?
Um

[00:10]
And with this we mean like especially
brittle is quite an interesting one in
my opinion because like
these deterministic checks they force a
certain deterministic behavior, right?
But with and sometimes this is
absolutely the way we want an agent to
behave, right? Like for example, let's
say you have an agent that creates a
slide deck for example, you want to make
sure that in the end there is a slide
deck present, deterministic check.
But then if you want to have like a
check on what's the quality of the slide
deck, this is way more nuanced, right?
Like you cannot easily encode this in
like some deterministic checks, right?
And that's why we also have the second
type of graders which is the model-based
graders, right?
And this is like rubric-based reasoning.
Um
So you for example say like
is this slide high quality? Very
generic, but that might be for example a
rubric or like for example is this text
coherent?
Also a way to get some intel on how well
your agent's performing.

[00:11]
Um you can do some interesting things
with this as well.
Um pairwise comparison is in my opinion
quite underrated. Let's say you have two
examples, two outputs,
um and then you basically ask the model
which one of the two do you prefer and
why?
That's also quite interesting to get
some information out of especially
especially for these scenarios where you
don't really have a clear way of of
defining what makes the better one,
right?
Um
And and then another one is the
multi-judge consensus which is just for
example you take like best of three and
you say like three judges score
independently and say like majority wins
for example, right? Once again, that
this multi-judge consensus is
interesting because it allows you to
introduce some more determinism in a way
where if you have like we know that an
LLM is undeterministic, right?
And the same would be happening for this
model-based graders, right? Like if you
run them like 100 times, a few times it
might say, "Oh, this is great." And a
few other times it might say, "Ah, it's
not that good." If you have like this
multi-judge consensus, you basically are

[00:12]
assuming, let's put more compute into
this and let's see what the majority of
our graders consensus is, right?
And this is unlocks a lot of things,
right? Like this is flexible, this is
scalable, this is nuanced.
But as I said, it's non-deterministic,
it costs more money, and also it
requires some calibration, which we will
see is not easy at all.
And then finally, the most expensive one
are the human graders. And these are
probably the graders that
when you're building these agentic
systems, you will be using the least,
right? Because they're like
incredibly expensive.
Um you have like a whole subject matter
expert that will do like a whole review
of the system. It will It's expensive,
it's slow as well, but it is more It's
the highest quality. It is very nuanced.
Um and yeah, it's like really good for
like some AB testing and some spot
checking, right?
So, I'm not sure like how many of you
were able to clone the repo beforehand
and have this all set up. Um I actually
wanted to do this session a little bit

[00:13]
differently, but given the amount of
people, I will probably do a little bit
more um
myself instead of like letting you um
think about all of the things. Um but
I'll quickly give you an overview of of
what's in the repo, right? Um let me
make this a little bit bigger. Um
I have made some pre-made uh slides that
I will show you in a bit.
Um
The resources is the main thing where
you guys would be working in. So, you
have the I'm actually closing this
session for now. Um so if like the
agent.yaml and this is basically where
you would define your agent, right? Like
um I think before we did a session.
So this is basically what we're going to
do use like the manage agent. So for the
people who attended that session um
before lunch, it's basically the same
thing. We define here like an an an
agent in this case um and we have given
this uh the system prompt, right? So
this is a system prompt that we're
giving. So basically you are a slide
generation agent and when the user gives
you a topic, create a PowerPoint file at
this location. And then also we tell it
you have a shell um
with Python PPTX uh pre-installed,

[00:14]
right? Um so that's all we give it for
now. And then we also have like an
environment which we've defined um with
like few packages um what is it what it
needs to complete this session. Um
And then basically that's it. We also
have some other things defined, but I
will get to that. I think maybe the
first question that I have for the
audience today is
we want to make a slide generation
agent, right?
What do you guys think is
a good eval? What are you trying to
measure? What would be some good
information that you want to get out of
evals?
Sorry?
Number of words on slides is is it a
useful uh thing to track?
And anyone else with some ideas?
Sorry?
Yeah, absolutely valid. Absolutely
valid. Yeah, yeah, yeah. Um I I And this
actually I like these two examples
because they immediately give you like a
different sense of um how you can use

[00:15]
the type of grades. Like for example,
the number of words on a slide is
quantifiable, right? It's like easy to
say you can count the number of words
with like a deterministic grader with
like a code grader.
>> [snorts]
>> The one if it's like overlapping or if
it's overspilling, that one is harder to
at um
um encode in code, right? So for this
one you might for example use a model
grader. And that's exactly what we did,
right?
So we have actually defined for you guys
already a few graders beforehand.
Two specific
directories we have the code and we have
judge. So, the code one is as I said
it's like these these code graders
they're quite deterministic like for
example if we take a look at emoji count
for example is one
that we have defined where we basically
just count the number of emojis present
in the slide deck. Um because we we just
noticed that it's quite prevalent. Like
for example if I open the slide deck
um let me go with environment one in
this case. Um
so these are the slides that I it's
basically the agents running. Um it's
it's done beforehand just because it

[00:16]
takes can take quite a while um to get
the agents running. Um but this is for
example the result of the initial
agents, right? So, this is slide number
one.
Um slide number two
slide number three um with some
weird things on the bottom left. Um
slide four and slide five.
Now, I I think we can all agree like
this is not the best slide deck you guys
have ever seen. Um but it's a good
start. At least it does a slide deck
um
that's five slides. I think that's
exactly the prompt that we sent it. Um
so we have a few slides. There's a few
content on here it's like few boxes.
It's you know, it's a slide deck. Um
given these slides is there anything
else that you guys are seeing that like
this is something that we would never
want in a slide deck?
What was that? I
No teal No teal. We can if you

[00:17]
absolutely want to avoid teal that's
absolutely right. I think in this it
doesn't do that for every single slide.
Like let me see for the career one.
Um let me see what it is. Oh, okay maybe
it does always use teal actually. Um but
for example in this one we see like this
overlap of like words and and and this
this horizontal
what else do we have some weird
coloring.
Yeah, there's there's there's a few
weird things happening generally, right?
So yeah, based on this we take you take
a look at what it is what the results
are and you're like hmm what type of
graders do I want to define for this
specifically, right? And so we did that
and we noticed for example emoji counts
is one that's quite prevalent.
We want to check how many times do we
see an emoji popping up.
Another one is for example cluttered
slides like how many shapes do we see on
the slides like if there's just so too
many things it becomes cluttered.
Counting the number of slides for
example we always ask for five slides
making sure that you have five slides.

[00:18]
Do we have slides with image, small
fonts, text heavy slides. Now this is
this is in this case it's quite
arbitrarily chosen, right? These were
just like things that we like thought
were like this is quite representative
of what
a slide deck might have for graders,
right? It really depends like I want
really want to stress this like
it really depends from use case to use
case what makes a good grader, right? I
think generally the way I think about
this thing is if you have a grader
that you get no useful out of
information out of
then you should not have that part of
your evil, right? Like each thing you
should be able to tell like for each
single scenario that you're testing you
should be able to say like this is the
information that I want to get out of
this. This is the
type of this is the part of the system
that I'm testing and this is how I can
act on if it's being degraded, right?
So those were just like a few codes ones
and then we also have a few judge ones
for example the color judge which
basically judged what's the color

[00:19]
contrast and then it gives a score from
like zero to five. Same with image,
the layout, text. And this is the prompt
that we give. Let me close this one real
quick.
Oh.
So, let me keep it like this. So, this
is basically the system prompt
that we give it.
Um no.
So, we're saying, "Please evaluate the
slide based on each of the following
criteria. Text,
the title should be simple and clear to
indicate the main points. For main
content, avoid too many texts and keep
words concise. Use a consistent and
readable font size, style, and color."
And I mean, it it goes on and on, right?
So, we give like for each of the
different things that we want to measure
we give like a little information of
like "This is what you should be
focusing on when you want to measure
this."
Right? Okay, cool. So,
we have these evals.
Let's say you have now created a slide
deck and you now want to see like,
"Okay, what are the results, right? And
how can we act on these results?" So, in
this wrapper we also have created this

[00:20]
nice little script that will
automatically score your slide deck for
you. And so, at the top here we
basically have it all
listed out. So, we have like the slide
count which is being counted the slides,
the number of slides with image,
text-heavy slides, cluttered slides,
small font size, and so on. We also have
our judges over here which are saying
like they give a score from like zero to
five uh based on like how good is the
text, how good is the image at the
layout and the color, right? Um
uh
honestly like these scores you can
immediately note that these scores are
quite high. So, as we said like we
calibrated between zero and five. And as
we see like the scores are being given
you are like between 2.8 and four which
honestly I think are quite high given
the slide deck that we have seen, right?
So,
that's like the part of the calibration
that needs to happen as well, right? I
think there's also like one thing that I
maybe want to stress. It's not because
you have set up your evals once
that they are now like the ground truth,
you know? Um
evals over time they can evolve. They

[00:21]
need to be a living artifact. It's not
like something you make once and then
forget and then use it like to make all
of your future decisions on, right?
Because like we will see over time like
as I go through all of the different
examples that we have, we will see like
there needs to be a way also how we can
see how we can make sure that the evals
that we create are actually still
measuring something useful for us,
right?
If you ever hear people talk about
saturation of evals, that's basically
what they mean in a way that like the
eval is not giving any more relevant
information that we can act on due to
several reasons.
Cool.
So, we see this and I guess maybe the
first thing that we want to do in this
case is we want to make an agent that is
a little bit more polished, right? And
so for this, we actually just update our
system prompts.
So in instead of just having like, "Oh,
you are slide generation agent, make a
slide deck."
We now give it a little bit more
information of like what are the
expectations that we have of you in
terms of typography, right? Because as
we noticed, we said like, "Oh, the font
is too small. There's too many words on

[00:22]
there. It's not readable or it's too
big." Right? So we give it a little bit
more of information. So we say like,
"Slide title should be this size,
section header should be this size,
body this size, caption this size."
Right?
And we also give it some information on
the layout and density. Like here are
the things that we expect from the
layout and density point of view. For
example, we say, "Keep the body text
concise, leave breathing room, and left
align paragraphs." Right?
And then also we
I think everyone kind of
I mean I am at least getting like ticked
off like if I read something that's
clearly AI written, I'm always a little
bit skeptical of
if I can completely trust the content
and if the person sending me this text
is like has like read it himself or
themselves and is standing behind that
content, right? So we also say like
avoid these AI generated tells as well.
So never use a thin accent lines in the
titles and don't pepper slide with
emojis as decorative icons, right?
So this is based on the things that we
have seen in our eval, right? So we have
seen as I Let's go back a little bit.
We've looked at this slide deck.

[00:23]
And we're like, "Oh, this is not
properly done. These fonts are a little
bit off. Um, there's some emoji used in
here. It's like a little bit all over
the place."
And then based on the score, we were
like, "Okay, these are the things that
we're clearly failing at, right?" So, we
have like emoji counts four in this
case, small font slides also four as
well, cluttered slides two, and text
heavy slides, right? So, based on the
information that we have gotten from the
eval that we have run, we have made
these changes to our new agent, right?
Let me now pull up the result of the new
agent that we have created in this case,
right? Um, so this is slide one,
which I think is immediately way more
enjoyable to look at. Like, there's no
overlapping stuff. Um, there's no dollar
sign. There's just generally it's
cleaner.
This once again, I think this one still
has like quite small text, but at least
once again, we're like getting a little
bit more consistent with the coloring as
well.
Um, once again, like the whole slide
deck is more consistent. This third
slide,
the fourth slide, and the fifth slide,

[00:24]
right?
And this is just by basically
identifying, "Here's a few failure modes
of our original one. Here's how we now
make changes based on these things that
we found in the system prompt, and now
we run it back."
And now once again, we can do the same
thing. So, this is we're now basically
in this loop of finding what's wrong,
iterating, finding what's wrong, running
it again, and making improvements over
time.
So, now we can take a look back at what
we found over here.
Oh, and this is actually way worse
suddenly. We see like emoji count 20.
I'm wondering where they are. I haven't
seen them actually.
Wondering where that is at.
Hmm.
Wonder if this is like a mistake in this
case. Um, but generally we see like,
okay, small font slides, we've seen
that, but we've we've improved upon the
cluttering. Um, and let's see, text
heavy, is that still the case?
Um,
I think I think that's fine. I mean,
those are a little bit text heavy, but I
think it's acceptable, right?
So, now we're like

[00:25]
So, this once again shows the value of
like human review as well, right?
Because now we see, oh, these things
that we have defined in our evals
are maybe not as well defined as we
hoped them to be, right? Because now I'm
here arguing like, oh, this is not as
text-heavy as I expected it to be,
right?
So, that means that something is
actually wrong with the way we're
grading. So, now we go back then,
we would go back, go to our grader,
change the grader, update it, and make
sure that it better reflects the actual
thing that we want to measure, right?
And this is also not something to be
underestimated, like this calibration of
how your agent should behave um and how
your judges should judge the specific
output is really something very fickle,
right? Like you should spend like proper
time trying to
find the ways on how you should make
this happen.
Um
let's say now that we want to have an
agent. Like I I I I think with this one,
I mean, it's fun. I think it's nice, um
but it's still quite text-heavy and it's
only text, right? Um
let's say now that we want to have an
agent. Let's say that's one of our
requirements, right? That we have an
agent that we always want to have

[00:26]
includes diagrams. Once again, we go
back to our system prompt,
we update it, and we now say every slide
must include at least one generated
diagram or chart inserted as an actual
image, right?
Um
so, once again,
we update the system prompt or any part
of the agent that you can tune,
and then we go again and we check what
do we get.
Okay, so this one is quite interesting.
I'm I guess personally I'm not a fan of
having
an image on the opening slide, but once
again, it is what we defined that it
should do, right? So, I'm going to let
it slide. But it's it's a nice nice
graph. What is saying? It's like no
negotiation and active negotiation. So,
it's arguing that if you do active
negotiation for your salary, you can see
over time the gap widens between no
negotiation and yes negotiation
negotiation.
Some extra benchmarks. I I I this looks
immediately way
better just in the way that it's like
kind of grounded into some actual facts
right now instead of just waffling its

[00:27]
way through the slide deck, right?
Yeah, this one I'm not a big fan of. I
feel like it's a little bit stretched,
but that might also just be the
screenshot. Um
Yeah, and this one also not the best one
either, right?
Let me see like let's see what the
score.json also says, okay. No emojis,
great. No cluttered slides. Still quite
text heavy slides surprisingly. Um still
small font slide. I think that's fine. I
think we just say like with images I
think
Yeah, I think we we accept like
these types of things are fine. Um so
once again, shows you some um questions
regarding the grader that we have set
up.
But now we can also take a look at like
the judges, right? Like for example
because now we have images that we have
created, so now we can also consider how
does the image judge uh I think this is.
And it says it's 3.8 out of five. Um
doesn't say give us a lot to go off,
right? It just gives us a random number.
What does it mean? How can we improve
upon this? But that's fine for now.

[00:28]
Now one thing that we always see that
works just generally quite well, and
that's like it's transversal over every
single use case is adding
a QA loop, right? Um for coding this is
quite intuitive. That's basically saying
like you create an agent that actually
is writing the code, right?
And then you add the second agent that
is then looking at the code that has
been written and just criticizes it. So
it's basically saying this is bad, this
is bad, this is bad. This introduces a
bug, this introduces a bug, this is not
according to standards, whatever, right?
So it basically is criticizing the the
thing that has been created. And then
that part of the feedback you give back
to your original agent, the creation
agent.
The creation agent goes off again, does
the creation, does the fine-tuning,
makes the changes that were informed by
the criticizing, and then once again
after that is done, it goes back to the
criticizing agent. And that loop
basically goes on and on and on until
both sides are like, "Okay, this is
fine. We can ship this."
And that's basically what we now do in
this next step.

[00:29]
Um so, we basically say like, "Okay,
require QA loop. Um assume there are no
problems.
Um oh, assume there are problems, and
then your job is to find them. Approach
QA as a bug hunt, not a confirmation
step." And this is quite interesting,
because we're like actively instructing
the agent to behave in a way
adversarially adversarially, right? Like
we're saying like, "There are issues.
You need to find them." It's not It's
not like, "Oh, there might be something.
You might be interested in finding
something." No, it's actively saying,
"There are issues. Go find them." Um and
then we say like we instruct after
writing the deck, "Okay, convert it to
images. Inspect every slide image
yourself. Fix the issues, re-render,
re-inspect, and then do not stop until
you've completed at least one fixed and
verified cycle."
Cool. Now,
as I said, I think for coding this is
quite intuitive, but I think it's also
quite intuitive if you take a look at
like
um
the the slides that we have created,
right? Because that's basically what we
did. We have looked at the slides, and
we're like, "Ah, this is not good. This
is not good. Let's take that feedback,
update our graders, update our system

[00:30]
prompt, and let's run it back again,
right?" So, let's now see if we can
actually if this is actually showing
some improvements. Um
I think this is immediately a lot
better. So, the the the image is way
bigger now. I think it's way more
readable even from a further distance
away. Um still the slides are small, but
it's like for example, it's source
known. There's a source over here as
well, which is quite good. Um I think
this is also way better. It is
more clearly structured. I think the
image is also a little bit better as
well, right?
A quite interesting graph in this case,
uh your value profile versus team
average.
This one is still a little off in my
opinion.
Also, we now have like a little
introduction of like these weird ticks.
Um
And this one is also a little bit
better, I would say, but I think like
the just the image taking is um kind of
messing with the slide here. And so then
we kind of know the drill by now. We
take a look at the score.
We see like has it improved? Why do we
see still gaps? And now we see like for

[00:31]
all of the judges that we have created,
it is higher than uh the ones before,
right? We're now all good in the four
.2 to 4.4 now. Um so we're on a we're on
a good track, right?
And um
you can keep on doing this. You can keep
on doing this. Um
And you will always make like these
little changes, but sometimes
and this is I guess where it gets quite
interesting and more like more like
nuanced is you can also just
go to a smarter model, right? Because
like now you're like defining, oh, this
is what a good slide should look like.
This is what it should do. This is what
not what you should not do. But with
these models getting smarter and better
over time, you kind of expect them to be
like
able to figure that out on their own,
right?
Um I mean, that would at least be nice.
So, that's what we tried out as well.
So, now in the last one
we basically just changed our model to
Opus 4 7 instead of Sonnet 4 7, which we
have used up to this point. If you can
uh 4 6. Um

[00:32]
So, now we have switched to Opus 4 7,
and we have basically just given it a
simple prompt again. Like you are a
slide generation agent, and then when
the user gives you a topic, create a
PowerPoint file at whatever and then you
have a shell. So, it's basically just
the initial prompt that we gave to uh
our Sonnet model in the beginning,
right?
And then once again, let's now
consider taking a look at the results of
those.
And this is just a base prompt, right?
Like you can immediately see like it's
significantly better than the Sonnet
one, right? I think there's still clear
issues that we can iron out, but
generally like it's It's more
structured, right?
And then we can take a look at the score
as well. And I think this is quite
interesting and quite telling. Like for
example,
Opus just does not use any emojis. Like
it kind of knows like if you want to
make a slide deck about salary increase,
emojis are probably not right place to
put them, right?
Um it also has like fewer small font
slides because it's kind of has like
this innate knowledge of, "Okay, it

[00:33]
should be readable. This is how a slide
deck should function. This is what
people expect out of a slide deck."
Right?
And then we get to these judge graders,
right?
Um we see a 4.4. We see a five for the
images. Do we even have an image in this
one? I don't think it we do actually.
No, we don't. Okay, but then once again,
we got a five in this one. Layout judge
4.2 and then the color judge 4.8 and
title body coherence 4.4. So, this is
like immediately giving like extremely
high scores as well, right? Which I
think is quite interesting because like
this is once again showing that we might
not be measuring the right thing.
And this is not too unexpected for these
types of um graders, right? Or for these
judge graders. I think
one of these things with like
Okay, let's go to the code grades. I
think those are quite straightforward. I
think most people in the room would have
understood by now like how they work and
how what we can do with them.
Like for example, emoji count, it's
quite simple. Just count the number of
emojis
and that's it. But with this judging,
what we have done here is actually quite

[00:34]
problematic.
We basically say like give a score from
zero to five
and for text well, the text should uh
the title should be simple and clear to
indicate the main point for main
content. Avoid too many text and
keywords.
But it has nothing to anchor on, right?
Like it doesn't really know what good
looks like in this case. It doesn't know
what bad looks like.
So, there's still like this trade-off
between like
what does a model actually know
and what do we need to give more
information
on to the model to make sure that it can
give like a proper um
proper judging of what we actually have
produced, right?
So, for example, in this case,
I would for example say what could help
is say like, "Oh,
this is a bad example. Like let's say
you have a zero. Like everything is just
awful. These are some telltale signs
that you're dealing with an extremely
badly formatted
slide deck." And then like over time,
different
ranges you can kind of express.
And then once over time, and then once
again, like that doesn't mean it will

[00:35]
still be able to give like a good answer
because
we now have these results. We have this
number that our LLM decided to
output for some reason. Like for
example, in this in this case, it just
put out five.
Okay, what do we do with that number
now? Okay, it's a five. We we we just
said there was no not a single image in
the slide deck, right? So, how can we
interpret this five?
One way of doing this is just basically
always asking your
judge graders to give reasons why it
came to that conclusion, right? And one
thing that should be very like
cautious about is the ordering, right?
I've had it happen while I was like
setting this up. And I did like this
exact thing. So, I had like the number
and then I said like, "Okay, give me
also reasons why you did that." And so
then it said like, "Oh, it's a four and
the reasons for this are these these and
these."
But we know that an LLM it works auto
regressively, right? So, if it is
anchored on like this four, it will do
anything it can to argue why it should

[00:36]
be a four, right? Anything. Even if it's
like extremely bad. If it's like if it
should be like a one, it will still say,
"Oh, it is good for these and these
reasons." Because it needs to justify
the four that it put out.
So, once how you do it is you actually
turn it around. So, first you say like,
"Give me a bunch of reasons. Give me
pros. Give me cons. Give me reasons why
it should be high. Give me reasons why
it should be bad." And then based on all
of those reasons together, then you need
to make your final decision on the
output, right?
And that's also that goes also back to
like this QA loop as well. Um because
then once again, you can get a little
bit tricky where you have like multiple
agents also doing the verification part
where you have like one agent that is
like finding all of the issues, and then
the other one is like refuting those.
For example,
one example that I can give, which I
think is quite interesting. Let's say
you want to make um
a document for um
where you need to like some analysis.
First you need to get a lot of context
from the internet, for example, like on
a legal document, for example, right? Um

[00:37]
and you ask the you ask a model to like
make a summary of
um a certain case, what was decided,
what does this have for legal
implications for other cases, right?
You need to be very careful with like
all of these things that like legal
cases are generally like quite tricky.
And like an agent would love to create
like, "Oh, this and this." and jump to
conclusions like, "This is the reason."
and that's it, right? And then the
grader might be like, "Oh, this is
unclear. This is um maybe not as
this is maybe
uh untrue. This is maybe
uh maybe like glossing over the actual
facts." All of those type of things,
right?
But then once again, you can like apply
these multiple techniques. You can have
like multiple graders, for example,
seeing like um evaluating those and
seeing like what are the main ones
popping up. Um because once again, a
grader might still hallucinate things as
well, right? Especially in like the very
nuanced scenarios, right? So, there's
like different ways of how you then can
work with these judges
to make sure that you actually get like
good, consistent output that is
actionable, right?
And what I've shown you here today is

[00:38]
basically just a small introduction to
how evals can help you,
but it's definitely not the end. I think
45 minutes for a session on evals is, in
my opinion,
quite [clears throat] short because it
can get really deep, right?
Because like I started this off this
session with talking about benchmarks,
which are in the end just evals.
And every single time, why would every
single model provide or care so much
about benchmarks, so much about evils,
if it wasn't one of the main important
things when we are building new models,
right?
Exactly. We need to find the things that
we are failing at. Exactly. We need to
find things. What are we good at? What
are we bad at? How can we make the model
better in future generations? And that's
the same thing when building
applications that are consisting that's
using AI agents, right? It's the same
thing. It's just finding what works,
finding what doesn't, iterating, and
making sure that the changes that you're
making that you're informed on the
decisions that you are making, and

[00:39]
making sure that the changes you make
have actually positive influence on your
final outputs. Okay. Thank you guys so
much. This is all the time I have. Thank
you guys.

</details>
