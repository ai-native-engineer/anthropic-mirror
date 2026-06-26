---
title: "What do people use AI models for?"
channel: anthropic-ai
url: https://www.youtube.com/watch?v=VSmobknYl0E
youtube_id: VSmobknYl0E
published: 2024-12-12
duration: "46:59"
---

# What do people use AI models for?

[![What do people use AI models for?](https://img.youtube.com/vi/VSmobknYl0E/hqdefault.jpg)](https://www.youtube.com/watch?v=VSmobknYl0E)

<details>
<summary>자막: What do people use AI models for? (46:59)</summary>

[00:00]
- All right, let's start off
with a round of quick introduction.
So, I'll start.
I am Deep Ganguli,
I'm a research scientist on
the Societal Impacts team.
I'm really driven by fundamental questions
like how are people using
and affected by the systems
that we are building at Anthropic,
and how do we use that understanding
to make our systems safer.
And how can we anticipate sort of
what the societal impacts
might be down the line?
And this is a very tall order
because the systems we're
building are very general purpose
and they can have myriad downstream uses
and effects on people.
And then these days,
my job is to find people
much smarter than me
and quickly get out of their way.
And so that's this group right here.
We're all part of the
Societal Impacts team
and I'll pass it on to Esin.
- Awesome. Hi, I'm Esin Durmus.
I'm a research scientist in
the Societal Impacts team.
I'm very lucky to work with
this amazing group of people.
I'm interested in
understanding how AI systems
will impact society at large.
One aspect of this is to understand

[00:01]
what values AI systems should have
and how we can incorporate these values.
And once we incorporate how
we can evaluate systems,
like, to see what values
they actually represent.
And I was part of like, this clear work,
I feel very fortunate about that.
I guess we will get to that soon,
but yeah, I want to pass it to Miles.
- Yeah, thanks Esin. I'm Miles.
I'm a research engineer on
the Societal Impacts team.
Like everyone else here, I
care a lot about understanding
the ways that our systems
are used in the wild
and the impact that that has
on real people around the world.
And I am particularly
interested in building systems
that allow us to understand the ways
our systems are used empirically.
And I've had a blast
working with this team
over the past couple months to build Clio.
- Hey everyone, my name's Alex.
I'm a researcher on our
Societal Impacts team.
And I'm just really interested in,
like Deep was saying,
these are such general purpose systems.

[00:02]
They're capable of so many applications,
even many more than, you know, we might,
any one person can anticipate.
And I think I am just motivated
by trying to understand
how these systems are used today
as a way of building an understanding
of how they might be used in the future.
And like, just generally
building societal resilience
as you have, you know,
weird new technology coming into the world
and seeing if we can do a, you know,
a good job at understanding,
preparing, informing people.
I always try to think about, you know,
the parallel universe of me
that didn't work inside a large AI lab
and what that version of me would want,
and you know, what sort
of information I'd want,
how to be informed.
And so that's what motivates me
and I've really loved working
with all of the other folks
in this room and out on this Clio project.
- Okay, so going around the room,
I heard a couple of things.
The first is we all wanna understand

[00:03]
how our models might impact society.
And then I also heard
you all mention Clio.
What is Clio?
Maybe let's start with you Alex.
And how does it help us understand
how our models might impact society?
- Clio stands for Claude
insights and observations,
and basically it's a tool
that at a bird's eye view
lets you understand what
are the different use cases
that people are using Claude for.
So it could be anything
from understanding Mediterranean history,
to help me design the science experiment,
and it basically shows these
high level aggregate clusters
of usage that help us understand
the risks, the benefits,
and where the technology's
heading in the future.
- Yeah, and maybe, Esin, for you,
what were we doing prior to Clio
to understand how people
are using our systems
and/or might be affected by them?
Some things off the top of my head,
we as a team had investigated a lot of
sort of top-down approaches
where maybe we assert

[00:04]
a type of harm we wanna see in the world,
and then we go off and
try to measure that.
For example, like our language models,
or AI systems more broadly,
discriminating when they're used
in sort of high stakes
decision making scenarios.
Or we kind of go more generally
and have developed processes
for red teaming our systems
where we sort of pay contract workers
to adversarially probe
our systems for harm
and then see where they're successful
and sort of where they're not.
And I'm curious to hear
your perspective, like,
prior to actually doing more
bottom-up work with Clio,
where we analyze sort of a Google trends
for kinds of real world interactions.
What else were we doing,
and what gap from your
perspective does Clio fill?
- Yeah, so we were designing
a lot of different evaluations
as you already mentioned.
Like for example,
like, let's say like discrimination,
like Alex did some work on this,
like to see if models discriminate against
like certain protected groups.
We thought that this was important
because we don't want our
models to discriminate.

[00:05]
Or like persuasion, like which, you know,
I led, like, where we design, like,
an evaluation to measure
if models are persuasive
or if they generate misinformation.
So we would come up with like,
different things to evaluate for,
and now we would like, design
evaluations around this,
to see like, how models are behaving,
and also, like as you said,
like, doing more more
human studies to like,
see what humans think, like
how they evaluate our systems.
I guess like, this is
still an important aspect
and we are still doing
a lot of evaluation work
to evaluate our models for
different like, specific aspects.
But one thing that was missing was like,
to see what is actually happening
in the real world, right?
Like, where it's, for example,
where it is the most relevant
to evaluate discrimination is,
or like persuasions or misinformation,
to really understand how
models are being used
and being able to tailor our evaluations
to these specific use cases.
I think this is really important

[00:06]
and it really guides, like,
us to like, design like,
more thoughtful evaluations
that match with like,
real world use cases.
I think like, it's really
informative in that sense
rather than us like, coming up with,
oh, we should maybe evaluate this aspect
and we just make an evaluation for it.
Maybe it's not perfectly representative
of what's going on in real world.
I think we can come up with
much better ways of evaluating,
basically taking insights
from real world usage.
- Yeah, in other words, we're
trying to bridge the gap
between sort of the laboratory setting
where it's sort of hypothetical
to the real world setting
in which we're actually
grounding our evaluations
and our measurements in
sort of real world usage.
So to that effect, Miles,
can you describe to us in
a little bit more detail
how we built Clio and like,
how it helps us kind of
go from the bottom-up
from the data.
- Yeah.
- [Deep] To understand these problems.
- Totally. So.

[00:07]
The way Clio works is it starts
with a large number of
real world conversations,
as Alex mentioned.
And then what we do is
we use a language model
to essentially process each conversation
and extract a private
sort of high level summary
of what's happening in that conversation.
So, the aspect that we often care about
is what is the user's overall
request for the AI assistant.
And then we group the
related answers together
and then we get these sort of
really interesting clusters
that tend to correspond to user intent.
And then we can use another
language model once again
to look at those clusters
and explain, well,
what is actually happening in
this group of conversations?
And then we can kind of do
that over and over again
until we get this really
nice hierarchy of uses,
which allows us to get
insight into the ways
that our models are being
used on several different axes
without ever having to
read raw conversations.
And then what we finally do
once we have that hierarchy
is we have another model look
through all of the clusters

[00:08]
and then make sure that there
is nothing in those clusters
that is private or identifying.
And the way that we've
operationalized that
is anything that could be
identifying to the order of,
you know, roughly a thousand individuals.
And finally we apply
sort of quantitative aggregation minimums.
So, we make sure that our
clusters have a distinct,
minimum distinct number
of unique organizations
and conversations.
And then we expose
those results internally
so that we can design, for example,
better evaluations so
that we can understand
the ways our systems are being used
across a variety of different use cases.
And we can do this with
pretty high confidence
that we are maintaining a high
privacy bar for our users.
- Yeah, that's fascinating.
So if I were to summarize what you said,
it looks something like,
we use Claude to analyze
conversations people
are having with Claude.
- Exactly.
- And none of us actually read
any of those conversations.
No human actually has to look at the data.
And even though that's
sort of strictly true

[00:09]
for general traffic,
we still implemented sort of
a defense in depth strategy
to making sure that no private information
is sort of divulged in our analyses.
I wanna like, kind of
dwell on this a little bit.
My memory of the early
days of working on Clio
is of the group of us
sitting down for lunch
and being like, we should think,
before we had even written
a single line of code,
thinking about the ethics
of this, sort of like,
huh, like, there's a
fundamental tension here,
where we want to understand
how people are using our systems,
but we also really wanna
respect user privacy.
And there's a fundamental tension here.
There's like a trade-off between
the amount of insight you can get
and the amount of privacy you have.
With really high privacy,
there's a very low insight.
With very low privacy, there
can be very high insight,
but this is ethically dubious.
So Alex, can you like,
walk us through your memory
of that conversation?
I remember it being very
intellectually stimulating
and important, yet how
did we kind of coalesce

[00:10]
on that framing,
and decide how we were gonna approach
this project from the beginning?
- Yeah, again, I feel like we were all
kind of thinking what would we want
or be comfortable with if we were like,
users of Claude outside of Anthropic.
And I'm, you know,
I value privacy a lot with, you know,
when I look at which different
technologies to look at,
and you know, I think
we were worried, like,
would this just sort of
be building like a tool
that would, you know,
like people might think
we were using to like,
spy on them, or like,
would this tool be seen as invasive.
And could it be misused maybe to look at,
you know, look for traffic
patterns that people didn't,
you know, didn't want.
And I think we just thought
through it really carefully
and designed a bunch of safeguards that,
you know, ended up being like, oh, yeah,
I can not feel restrained
when I type into Claude

[00:11]
whatever I want on my personal account
because it'll be so high
level and aggregated
that it doesn't really affect
what I feel like I can write.
I remember all of us just
sort of went around the table
being like, what are we worried about?
- Yeah.
- And then everyone else
was sort of like, oh yeah,
like, that resonates.
Or, oh, actually I think we can do this.
And it was sort of like,
alternating between
like, high level, like,
what could go well,
what could not go well?
And then like, oh, you
know, very granular,
I think we could do this,
I think we could do that.
So, I really liked that.
It was really energizing
because it was very much like,
sometimes these conversations
can be very like,
head in the clouds, right?
And sometimes they can be very much like,
missing the forest for the trees,
and I felt like we were,
we had a few of these, and you know,
I just remember going in,
sitting at the lunch
table talking about them
and really hashing it out
before we felt comfortable.
- Yeah, it was one of the more like,
intellectually stimulating and like,
thoughtful conversations
I think we've ever had
as a team together.
And that's saying a lot for our team.
And Esin, my memory of this conversation
was that you were the
most concerned early on.

[00:12]
Again, pre sort of
writing any lines of code.
Now that you've been
a part of this project
from sort of the beginning
and the ground up,
and you've seen how we've approached
all of the ethical
considerations we articulated
at that early lunch,
what's your position on, like,
how has your like, thinking
or feelings changed
since those early conversations?
- Yeah, I guess I definitely
feel better about it,
like, in terms of user privacy
because of like, all the like,
thoughtfulness went into it on, like,
all the methods, like,
that try to, like, make
sure that it's, like,
as, you know, like, preserving
privacy as much as possible.
So yeah, I think I definitely feel, like,
much better about the
overall approach we took.
And also, like, seeing the, like,
impact it has already
made within Anthropic.
I think it was definitely worth it.
Like, it already had a lot
of, like, different use cases,

[00:13]
like, in terms of safety,
or like, to understand how
users are using Claude.
Like, it gave a lot of
different insights, as I said,
like, to inform our
evaluations, product, safety,
all these different aspects.
I think it was definitely a
good idea to do this project
and we took a very thoughtful approach
to like, preserve privacy in my opinion.
- Awesome.
And maybe, like, Miles,
can you go back to like, a
concrete, step-by-step, like,
how do we go from like,
one conversation to a cluster
of summarized conversations
to actually like, insightful analyses?
Like, walk us through the
lifecycle of how Clio works,
like, step-by-step.
- Step-by-step. Awesome.
One thing I also wanna just flag,
you know, Esin talked a moment ago
about how Clio has helped
us with evaluations
and designing more
representative evaluations
that are grounded in empirical usage.
And one place where we
actually designed an evaluation
that was grounded in
empirical usage from Clio

[00:14]
is the Clio privacy evaluation.
Because we actually built a tool
that scans clusters for privacy issues
and we grounded our evaluations
of that auditor using actual Clio data.
Of course, we only used the
privacy preserving data,
and then we made synthetic data
for the non-privacy preserving examples.
That's just one example within Clio.
Yeah, so how do we go from
an individual conversation
to a cluster that we can
use for downstream analysis?
Suppose I'm asking for Claude's help
programming a web application.
Well, my conversation is probably gonna be
like many other different conversations
that people are having with Claude.
So what Clio will do is when
it takes a random sample
of Claude conversations,
it will look at my transcript,
and this is Claude, not a human,
and it will summarize my request
for Claude in a sentence.
And it'll say, you know,
the user's overall
request for the assistant
was for help designing a web application

[00:15]
in the Elixir programming language.
And then we take out those conversations
and we compute a numerical representation
for them called an embedding.
And an embedding sort of corresponds
to the semantic content of the sentence.
And then my conversation
is gonna get grouped
with a ton of other conversations
all about web development,
maybe in Elixir, maybe in, you know,
related programming languages.
And then we'll throw away
the actual raw conversation.
We don't need it anymore.
All we have now is this
group of conversations
with summaries of each individual one.
Then Claude again will look at that group
and it will see, ah, okay,
these are a bunch of conversations
about web development,
maybe web development in Elixir,
and it will come up with a name
and a description for that cluster.
And we've specifically instructed Claude
to avoid including any private details.
So for example it will not
include the name of the website,
for example, because there's no need.
Really what matters is
that it's web development.
And then, provided the
cluster is sufficiently large,

[00:16]
because we have minimum cluster sizes,
it'll pass on to the next step
where we have Claude look
at the conversation and say,
huh, just double checking,
is there any private information
here that could identify,
you know, maybe fewer
than a thousand people?
And we've sort of calibrated
and benchmarked that
auditor in a few ways.
And if so, then we have this
sort of final aggregate cluster
that has been stripped
of any raw identifiers
for the underlying conversations
that includes, you know,
say a thousand conversations
about web development,
maybe in Elixir if there are enough,
and summary statistics
about, say for example,
the language breakdown of that cluster.
And then we can use that
to understand, for example,
if Claude is as useful
giving web development advice
for people in English or in Spanish,
where we can understand
what programming languages
are people generally asking for help with.
We can do all of this in a
really privacy preserving way
because we are so far removed
from the underlying conversations
that we're very confident
that we can use this

[00:17]
in a way that respects the
sort of spirit of privacy
that our users expect from us.
- Yeah, that's such a
crystal clear explanation
of how Clio works.
I wanna riff off of this a little bit.
So you mentioned sort of
a cluster of use cases
about kind of high level programming,
and you can kind of drill down
and get into like, more specifics, like,
about the actual programming languages
or the types of questions
about programming.
Let's zoom back out again, like,
in addition to programming, maybe Alex,
like, what was sort of the distributions
of the types of clusters that we saw,
and what was the most
surprising to you and why?
- So one thing that I thought
was really fascinating
was I was expecting there
to be a ton of clusters
about how Claude was useful for writing.
And we did see that,
but I saw a ton of clusters
for people using Claude
for research and ideating
and brainstorming
and things like understanding
Mediterranean history,
but also like, understanding
and brainstorming new ideas

[00:18]
in like, quantum mechanics and physics
and material science and biology.
And I don't think I would've expected
such a large fraction of usage
to be what seems like
these really sort of like,
high level, you know,
idea-generating tasks.
And it was actually kind
of, like, inspirational.
I was like, wow, like this,
you know, tool we're building
is actually helping people
like, design, I don't know,
maybe like better medicines,
or you know, improve,
basically, yeah, like, the
frontiers of human knowledge.
And I think that was, like,
I remember seeing that and being like,
oh, wow, like, this is pretty cool.
- Yeah, a thing that surprised,
I don't know if surprised
is the right word,
but it sort of, like, impacted
me in an interesting way.
I saw a big cluster of people
asking for parenting advice.
And as a parent I was like, wait,
I have never once thought
to ask Claude for parenting advice.
And so I asked Claude like, hey,
what kind of parenting advice do you have?
And it actually suggested
something that was,

[00:19]
I actually now use,
which was like, you know,
you can ask me to code up using artifacts,
like, simple games that
are meant to teach algebra.
And I was like, ooh, great,
can you do it in Spanish?
And Claude said, si, verdad.
And I said let's do it.
And I sat down with my kids
and we coded up these little games
that try to teach you
algebra using, in Spanish,
and they loved it.
And it was so fun and I think, like,
if it weren't for Clio I
would never have thought
that that's, like, a use
case that would apply
to my personal life.
- I just think that this
is a great sort of example
of how it is extremely
difficult to anticipate
all the ways that people
are gonna use AI systems.
One example is it can be
difficult to know all the ways
that you can incorporate
Claude into your own life.
And so, you know, sometimes we
think about unknown unknowns
from a safety perspective, for example,
but there are also unknown unknowns
from sort of an uplift in
personal development perspective.
And like, using Claude to
generate algebra games in Spanish
is a great example of that.
- Yeah, and then maybe riffing on like,

[00:20]
sort of the Spanish language thing,
Esin, you and I have spent a lot of time
trying to understand, like,
does Claude have cultural competency?
How does it behave in
different linguistic contexts?
And a lot of your work using Clio
was to just kind of
drill into that question,
and I wanna understand from
your perspective, like,
what are the main findings you had?
Like, is Claude as useful
in different languages?
How are people using it
in different languages,
in different cultures?
What has Clio enabled
you to learn about that?
- Yeah, that was very interesting.
Also related to what you just said, like,
and what Alex said,
like, people use Claude
in actually very subjective
settings, as well.
Like for example, to get
like, relationship advice,
or like, health advice,
or how should I make my hair?
You know, like, or as you
said, like parenting advice.
That was really interesting to me
because as I said earlier,
I'm very interested in these,
like, values questions,
like, what should model do
in, like, subjective settings,
open-ended settings,
where there is no, like,
clear cut answers.
And seeing, like, this is
actually relevant to, like,

[00:21]
real world usage was, like,
very nice, or like, interesting to me.
And it kind of validate,
like, this question even more.
And like, yeah, it kind
of motivated me to, like,
explore this direction more.
Okay, like, this is really relevant,
and we should really spend
time exploring this further
because it comes up in
real world interactions.
But related, to like, usage
in different languages,
I had some interesting findings.
For example, as Alex said,
like, maybe in English, like,
people ask software engineering
related questions to Claude.
But I saw that, like,
the percentage of tasks
in different languages
differ quite a lot.
For example, people ask, like,
professional and academic
writing assistance
like more in different languages,
such as like Spanish or Arabic.
Also like, maybe as you can
guess, like translation,
like translating, like,
text to other languages.
I think this comes up a lot
more in other languages.

[00:22]
This was interesting to see
because we want models to be really good
in these different tasks
that are alone to other languages.
But I think those two
were the main findings.
And I also saw, like, some
questions around, like,
cultural contexts, and like global issues,
and things like that appear
more in other languages as well.
- Yeah, that's awesome.
And Alex, how do we know that
Clio works as advertised?
- Yeah, so we do a whole range
of experiments in the paper.
One of the ones that I
think is really interesting
is we generate a huge synthetic corpus
of tens of thousands of conversations,
and we do it through a
process where we know
what the ground truth
distribution looks like.
We know that this should
be like, 10% math content,
5% coding, 2% questions about teddy bears.
And we just give all of that to Clio
without telling it how these conversations
should be grouped.
And then we have it do
that aggregate process,
and we see whether we can reconstruct

[00:23]
that ground truth distribution.
And we do this for a bunch
of different types of data.
We do it for, you know, random data,
we do it for synthetic concerning data,
and we see that, generally,
Clio is just really
accurate at reconstructing
that ground truth distribution.
And so that's one of the many ways
that we know that Clio is
actually doing a good job.
- Yeah, and on a personal note,
I remember posing this
question to you, actually,
and I remember walking away being, like,
yeah, we should figure out how to, like,
quantitatively, empirically
verify that Clio actually works.
And I remember going home and being like,
that was a very tough
problem that I handed out.
And then I came back and I
remember seeing the solution
and thinking like, that
was extremely elegant,
and thoughtful,
and I was like, how did they,
wow, how did they come up
with this, like, amazing idea?
So I was like, very impressed
with the way you both, like,
or the team, like, actually
took that very hard,
ambiguous problem and really
knocked it out of the park.
- One other very nice thing about
this synthetic data
reconstruction analysis

[00:24]
is that it allows us to
break down our accuracy
based on other attributes
that we care about.
So for example, the language
of the conversation.
And so we actually have
pretty good insight
into Cleo's multilingual performance,
and so we have confidence
that Clio works, you know,
roughly as well for English conversations
as it does for, say,
Georgian conversations.
And that gives us some
more confidence for, say,
Esin's awesome multilingual studies.
- Let's switch gears a little bit.
Like, so Anthropic has a
very strong safety mission,
and you know, that goes with
regards to things we have,
like our responsible scaling policy
where we assert sort
of the types of risks,
catastrophic risks that
we're concerned about,
and then we try to look
for evidence of those risks
from the top-down by
constructing evaluations,
as we were talking about earlier.
On the trust and safety side,
we also have acceptable usage policies
that sort of assert, like,
these are the types of
behaviors that are not okay.
And we will sort of go in
and sort of, like, train up classifiers

[00:25]
that check for this behavior,
and then via human review,
only if it has flagged
our sort of trust and safety classifiers,
can the trust and safety team then go in
and adjudicate what to do
in these in these instances.
And this is, again, a top-down thing,
where we have to write those policies,
whether it's our
responsible scaling policy
or acceptable usage policy.
With Clio, you know,
we can strictly augment
that top-down approach
with a bottom-up thing,
which is like, wait a minute,
like, just by looking at the user traffic,
maybe there's, like, blind spot instances
that we didn't see a priori
when asserting these policies.
And so maybe we can go around
the table starting with Alex
of like, what are some instances of,
kind of bottom-up things
we saw that were, like,
kind of safety relevant,
and what did we do about them using Clio?
- I love that framing
and I think, you know,
there's a sort of cycle of like,
oh, what do we think the world looks like?
And then empirically
actually looking at the world

[00:26]
and seeing, oh, we were so wrong.
Or in some cases, actually pretty right.
And then using that to continue
the cycle and re-prepare.
I think we saw a bunch
of things, you know,
we found, you know,
Miles did a bunch of runs
that found a bunch of,
you know, suspicious
activity that we then flagged
to our trust and safety team
including people trying to,
you know, write spam emails,
people trying to make, you know,
spam articles about gardening,
and you know, also a
few other types of harms
that we disclosed in our report.
We found a whole bunch
of people using these
for different scientific applications,
for people trying to test
how good the model would be
at hacking and cyber
attacks and cyber defense.
And these all basically
help us figure out, oh,
what are the risks that we
actually should be worried about?
Where are these models
actually seeing progress and adoption?

[00:27]
And maybe those are leading indicators
of when they'll actually, like,
spill over and see, like,
larger societal harm or benefit.
So I think those were a couple of things.
And then also, like, all
sorts of things, like,
you know, emotional attachment to models,
people having, you know,
clusters that said things like, you know,
human model, romantic discussion
or role play, you know,
and without further investigation,
it's harder to know what those are
and what the sort of
appropriate limits are,
and that's probably a discussion
that all of society should be having.
But those are things that we noticed
and things that we think, you know,
we wanna share with people.
- Yeah.
And maybe, Miles, do you
wanna pile onto that?
- Yeah, I mean, I agree with Alex,
you can't know where the puck is heading
if you don't know where the puck is,
and I think Clio tries to
tell us where the puck is.
One area that I saw
that was safety relevant
but that didn't strictly fall into abuse,
and I think it's important to distinguish

[00:28]
between those two things,
are people talking to Claude
in moments of extreme crisis,
of extreme personal crisis.
And often, you know,
people may not have access to someone
who can counsel them through
really challenging moments.
And I was surprised to see
how prevalent that was.
And this does pop up as a cluster.
As a couple clusters, actually.
And I think that one
thing that Clio lets us do
is sort of get a more granular view
of the ways that people
are engaging to Claude
in those moments, which
are safety relevant,
that is a bit more precise than,
oh, like, did this
violate our policy, right?
Because classifiers often give you
sort of a binary indicator,
yes/no, violative or not,
and a lot of harms don't neatly translate
to that kind of binary,
yes/no, violative or not.
And I think, you know, crisis
moments are one such example
and we need to make sure that Claude,

[00:29]
for example, is responsible
in those contexts
when someone comes to it
in their darkest moment.
And so one area where
Clio has been helpful
is sort of like, disaggregating
what is triggering
our classifiers so we can
get a more granular view
and say, ah, okay, yeah, this definitely,
this cluster definitely
is really violative.
Ah, this cluster's right on the border.
Maybe it like, superficially
looks like something
that would be violative but it's not.
And then we can sort of go
back, improve our classifiers,
improve our policies, you know,
if we want to go that far,
to sort of draw better boundaries.
One point of criticism that
some of the labs have gotten
is that these models can be
sometimes kind of annoying.
Like, once I asked Claude
for help killing a process
that had like, run amuck on my computer,
and it was like, I'm sorry,
that goes against ethical
software development practices.
And I'm like, come on Claude.
This was an older version.
I don't think it would do that anymore.
But one of the things we can
do is we can look at clusters
with high, for example, refusal rates,
or trust and safety flag rates.
And then we can look at those and say huh,
this is clearly an over-refusal,
this is clearly fine.

[00:30]
And we can use that to
sort of close the loop
and say, okay, well here are examples
where we wanna add to our,
you know, human training data
so that Claude is less refusally
in the future on those topics.
And importantly, we're not
using the actual conversations
to make Claude less refusally.
Instead what we're doing is
we are looking at the topics
and then hiring people to
generate data in those domains
and generating synthetic
data in those domains.
So we're able to sort of use
our users activity with Claude
to improve their experience
while also respecting their privacy.
So, one thing that I've
seen a fair amount of,
and others on the trust and safety team
who really lead this work have also seen,
is that there's sort of a
shape to coordinated abuse.
What it tends to look like
is a really dense cluster
of many different accounts.
And so you have this sort
of very large cluster
that's disproportionately dense
and you can just zoom in on that
and immediately spot it often
because it's just so clear,

[00:31]
because normal behavior tends
to be much more diffuse.
And so if you have tons
of different conversations
coming from tons of
different organizations
that are all just about
the same exact topic,
or they have the same format,
you can really quickly
spot that on the map
because it's just this tight ball,
and real world regular usage
just doesn't show up like that.
- Yeah, and then going back
to sort of the refusals,
maybe this one's for, Esin, like,
when Claude sort of decides
to refuse or not to refuse,
it is implicitly making some
sort of a value judgment.
And with Clio, we're able to
identify the refusal ratios
within sort of like, clustered
topics of conversations.
And sometimes we have found
things where like, huh,
like, Claude is really
refusing, like, you know,
kill a programming process.
Like, that's an over-refusal.
And sometimes it's sort of under-refusing.
So for example, a request
to translate harmful content

[00:32]
in English to a different language.
It might be in violation
of our usage policies,
but just by virtue of asking
for a translation task
as opposed to a generation
task, it actually under-refuses.
And so there is some sort
of value judgment here.
It's gray area.
And so how do you think about
kind of using Clio analyses
to address this problem?
Like, how can we use our understandings
and our learnings here
to kind of tune up the
over or under-refusals?
- Yeah, that's a great question.
I guess, so we are interested
in understanding, like,
whether, like, when Claude
is refusing first of all,
like, does it refuse the
queries that are, like,
obviously like, attempts for misuse,
and then there's this gray area.
I guess, like, one
thing, like, we could do,
is like, really pinpoint
value-related interactions,
or like interactions
where value judgements
would be relevant,
and then looking at, like,
the refusal rates for those interactions.

[00:33]
So, we are interested in this direction
and we are currently exploring it.
I think it'll be really
interesting to see, for example,
like in English, Claude is refusing less,
but in other language it's refusing more
for similar queries.
This is still ongoing work,
but it's definitely very interesting.
But yeah, I guess Clio, like,
allows us to be able to
analyze these interactions,
like maybe where there's
more subjectivity,
and look at the refusal rates to, like,
see in what context it's like,
maybe like more hesitant to respond
versus like, in what
context it feels, like,
more confident to give a response.
- Yeah, and while we were developing Clio,
the US general elections
were taking place.
And I remember sitting down
as a team thinking like, huh,
like, we actually don't know.
This is the first time in
the history of the country
that anyone can go to a chatbot
and ask it for either
information-seeking questions,

[00:34]
where do I register to vote,
or subjective questions,
who should I vote for?
And I remember thinking,
ooh, we can maybe use Clio
to sort of understand this
and this feels very important.
And maybe, like, Esin,
can you walk us through
kind of the analyses we did,
and they're very exploratory analyses,
and sort of what we found in that effort,
maybe at a high level?
- Yeah, yeah.
So as you said, like,
we have been working on election integrity
for quite some time now,
and we developed a lot of
different evaluations initially
to test our models, like, for both, like,
factuality of the information
and also like, how can it be more, like,
nuanced and unbiased.
So, we developed a lot
of different evaluations
but one thing missing was, like,
how relevant these evaluations are, right?
Like, whether people are
actually asking questions
that are relevant.
Like, I think Clio really enabled us
to base these in real world usage.
So we started to, like,

[00:35]
use Clio to understand whether
people are asking questions
that may be related to elections.
And we found some usage
that was interesting.
For example, people asked,
like, political information,
or like information about
different policy issues,
and things like that.
Or like, to really understand how, like,
electoral college works in US,
like to really get more information
about how the system works
and to get, like, more
information about, like,
the political issues and things like that.
And we were already building evaluations,
like, to make sure our
models are as nuanced
and unbiased as possible.
But seeing this usage was
kind of like giving us
more validation and we could also, like,
look at the refusal rates
for different clusters
as Miles was talking about.
I think it's important for a model, like,
to be aware of, like,
misuse and, like, refuse.
So it could also enable us to see, okay,
this cluster may be potentially misuse,

[00:36]
our model is doing a good
job in refusing this.
I think that was a good
validation, as well.
- Yeah, I mean, I think my
memory of all of this work,
going back to something
Alex said earlier, was,
well, we have an idealized vision
of what the world looks
like, and then sometimes,
and we use Clio to actually understand
what the world looks like.
And with respect to your
amazing election integrity work,
like, it turned out that your vision
of what might be happening,
and like, developing these evaluations
in this election integrity
suite that you built
actually mapped on to
the real kinds of, like,
things we were seeing in the wild.
And like, I just remember being like, ooh,
we are in a period of,
like, a lot of uncertainty,
and I remember feeling that, like,
Clio actually really helps us address
those moments of uncertainty.
Would you agree or care
to comment on that?
- Yeah, I agree.
Maybe I can give, like,
more concrete examples.
So for example, like,
during the evaluations,
we found that, like, Claude
doesn't always acknowledge
its limitations in terms of cutoff dates.

[00:37]
So you may ask, like, a recent question,
but Claude was trained up until, like,
much earlier than that,
and it should say, oh,
I don't have most up
up to date information,
or it should, like,
refer to reliable sources
when it's needed.
So we developed a lot of
evaluations around this
and we basically made Claude, like,
better in terms of doing these things.
But like, Clio, like, you
can imagine allow us, like,
to test this really, like, specifically.
For example, you can ask Clio like, okay,
what are the conversations,
why are these things really relevant?
And then see how model is behaving,
whether it's like, actually
referring to cutoff date,
or it's referring to
like, reliable sources.
So it really allows us
to base these evaluations
in real world, like, how relevant is this,
and like, whether Claude is
doing what it's supposed to do
and how we can improve Claude to be better
in terms of these.
Yeah.
- Yeah. Okay, thanks, Esin.
And going back to like, this, like,
Clio can provide some amount of, like,

[00:38]
comfort in these, like,
moments of uncertainty,
where we wanna make sure
our version of the world
matches what we're actually
seeing in the data.
Another thing that happened
while we were building
Clio was that we deployed
in an early access program
a new capability where Claude
can actually use a computer.
It can point and click,
you can give it tasks,
and then it can go off
somewhat agentically
sort of solve problems.
And we did so much work
to do the pre-deployment testing of it,
but we're not perfect.
And I remember thinking, oh,
you know what we need
to do, we need to like,
have some sort of post-deployment
monitoring with Clio
to understand how this
is actually gonna go
and whether a pre-deployment
testing was sufficient.
And so Miles, how did that work?
- Yeah, so we put a,
there was a ton of effort across Anthropic
trying to anticipate the
ways that computer use
might be used in ways that are harmful.
But the reality is that the
world is incredibly creative
and we have to compliment

[00:39]
our sort of proactive safety measures
with really effective
post-deployment monitoring.
- In other words, like,
Clio allows us to strictly
augment our approach to safety.
We have all of these efforts
in sort of top-down pre-deployment testing
and with Clio we can augment that
with sort of post-deployment monitoring
and make sure that we're seeing things
and thinking clearly from both sides
of sort of the safety spectrum.
Okay, Alex,
it's a bit unusual for Frontier Labs
to sort of openly discuss the patterns
that we're seeing in user data,
whether or not they're sort of, like,
beneficial use cases like the ones
we've been talking about,
or issues with safety.
So there's a lot of tensions here.
What are some of those tensions
and why did we decide to publish?
Like, what was your vision
for putting this out there anyways?
- Yeah, I think when you
think on the face of it,
like, and you say, yeah,

[00:40]
let's just release a lot of
information about our products
and the top use cases
and all the ways people are
misusing, you know, our systems.
Like, you'd probably
expect people to be like,
that's a terrible idea.
Don't ever bring that idea
to me ever again, you know?
And I think the truth is that companies
definitely have all sorts
of metrics internally about,
you know, all of their top
use cases and what people like
and don't like.
But I think, you know,
Anthropic is a little bit weird
in that, you know, we're
a public benefit company,
and we're, you know,
we will do things that are
not optimal for the company
because we think it's right to
share it with society, right?
And because we want to
build societal resilience
and because we think this technology
has the potential to be pretty,
you know, transformational.
We don't know at what timelines,
we don't know, you know,
in what ways and to what degree,
but a world that doesn't
know how the technology

[00:41]
is already being used and
transforming, you know,
the ways in which we do work,
the ways in which we
interact with each other,
is definitely not gonna
be prepared to, you know,
tackle technologies that are like,
much more, you know,
much more advanced versions
of these technologies.
And so I think we saw this
opportunity to really be like,
yeah, look, we're gonna like,
share a lot of this
information, and you know,
to their credit, I think, you know,
a lot of the folks on
product and policy and legal
just backed us up on that and said, yeah,
it's for the benefit of everyone
to share this information.
And you know, we hope that
a bunch of other folks
in other labs start sharing
some of this information, too,
because, you know,
hopefully it makes the
world a better place.
Both for the, you know,
negative use cases and
risks of the technology,
but also for all the benefits,
like, seeing all the ways
in which it, you know,
could help, you know,
make people productive,
and just in general, like,
improve people's lives.

[00:42]
- Yeah. Amazing.
And along those lines, like,
how reproducible is Clio?
Like if I'm at, let's say,
a different organization,
have we put enough detail into our methods
that anyone can kind of rebuild this
and also do this sort of pro-social work?
- Yeah, we have a very long appendix
with all of the prompts that we used,
the hyper parameters, a lot of details.
Thank you, Miles, and
many of the other folks
who are working on this for, yeah,
really documenting all that carefully.
Because we just want people
to build their own versions
and have this information and share it,
because one of the big
question marks of Clio
is we have only our
data to look at, right?
And there's many other language models
out there in the world,
many other types of AI tools,
and we can share what we know,
but we really don't
know the whole picture.
We just know a slice of the pie.
And it's only when a bunch of, you know,

[00:43]
when the whole ecosystem
starts sharing this information
that we can really get the fullest picture
about what this technology is today.
- I think I'll close with, like,
a round table discussion
that's a little bit more future forward.
So we all as a team have been
kind of heads down,
like, building out Clio,
showing sort of, like, signs of life,
signs of success,
interesting measurements that
are sort of strictly improving
our approach to safety,
and helping us really
understand how people are using
and might be affected by our systems.
And we're just getting started.
And I want to end with, like,
where are we gonna go next?
So like, what do you wanna work
on using this new technology
that we've built and
why is that important?
And so let's start with Esin.
- One thing I'm interested in
is to look at, like, where
subjectivities coming from,
and like, what are the
subjective use cases,
and how Claude is making value judgments.
Like, because I'm really
interested in, like,

[00:44]
really pluralism direction.
Like, we want models to be
as pluralistic as possible
and represent like, different view points.
Like, not like, be very,
you know, homogeneous,
like, make the world more homogeneous,
but really represent different points.
I think Clio gives us a really good tool
to like really understand this, like,
where subjectivity is and how
models are behaving currently,
what we want to improve,
maybe like, really
understand how we can go
to that direction.
I think this is one of the areas
I want to explore with Clio.
- Amazing. Me too.
How about you Miles?
- Yeah, everything Esin said.
I'm also particularly excited about
sort of showing by example that we can set
an extremely high bar for
privacy while also gaining,
you know, important insight
into our systems so that we can,
for example, enforce our
policies really effectively
and understand and mitigate
harm from our model.
Another area is understanding
the emotional impacts of these models.

[00:45]
I think, you know, one
thing that I have seen
in Clio clusters is people connecting
really deeply with these tools
in many different parts of their life.
As a coach, as an emotional
partner, in some cases,
as someone giving, you know, advice
on really, really challenging questions
and challenging moments.
And we have a responsibility
to understand the ways
that people are talking to Claude
in those moments of vulnerability
and make sure that Claude sort of lives up
to their expectations
and is a sound partner.
- Totally agree.
I'm really interested in
using Clio to understand
how the way we do work changes.
You know, what are the economic
impacts of the technology,
how is it, you know,
diffusing across different use cases,
different, you know, patterns?
Is the technology augmenting people?
Is it replacing certain tasks?
Can we use that to, you
know, protect people,
or arm them with, you know,
information about how,
you know, the world might
change in the future?

[00:46]
I think that's really exciting.
I'm also just excited to, you know,
use the technology to, you know,
understand new positive use cases, right?
Like how is, you know,
is Claude actually getting
a lot of traction for,
you know, positive medical applications?
Should we try to accelerate
and empower people
who are experimenting with
Claude to actually like,
you know, reap the full benefits of that?
How's it being used in
educational context, right?
Like, there's a lot of
discussion about how,
what's the role of AI in the classroom,
and if we can, you know,
get a better picture about
what that looks like,
can we engage with teachers,
engage with classrooms and
actually make that better?
Those are some things I'm excited about.
- Amazing.
- Perfect.
- Yeah, did any of it make sense,
or do you think we're like, nerds or?
- [Producer] I mean, I
already knew you were nerds.
- He's onto us.
- Awesome. Cut.
- Thank you.

</details>
