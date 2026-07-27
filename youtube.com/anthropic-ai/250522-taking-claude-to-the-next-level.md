---
title: "Taking Claude to the Next Level"
channel: anthropic-ai
url: https://www.youtube.com/watch?v=nZCy8E5jlok
youtube_id: nZCy8E5jlok
published: 2025-05-22
duration: "22:35"
captions: en
---

# Taking Claude to the Next Level

[![Taking Claude to the Next Level](https://img.youtube.com/vi/nZCy8E5jlok/hqdefault.jpg)](https://www.youtube.com/watch?v=nZCy8E5jlok)

<details>
<summary>자막: Taking Claude to the Next Level (22:35)</summary>

[00:00]
[Applause]
good morning everyone welcome to Taking
Claude to the next level i'm Lisa Crowoot
i'm a research product manager here at Anthropic
and today I have the pleasure of introducing you
to our newest models Claude for Sonnet and Opus
so we're going to start by talking about what
the next level of AI agents looks like i'll
go through new capabilities in the Claude 4
family and then we'll talk through some practical
tips for how to get the most out of Sonnet and
Opus before we dive deep on Claude 4 I wanted
to paint a picture of what we think our next
generation next generation agents really
look like we really want Claude to be great
at three things claude should be able to
work alongside you and adapt to the ways

[00:01]
you work claude should be able to work entirely
independently on tasks that require many steps
and in both of these cases Claude needs to
sustain performance over hours of continuous
work imagine this you've been assigned a new
project to refactor your O system to support
OOTH 2.0 so you decide to work with claude
on this to make faster progress you might
choose to write the requirements and the plan and
update the documents but decide to delegate the
implementation to Claude what is most interesting
in this collaborative mode is that we don't
envision this being like clear human AI handoffs
we really want you to be able to work with Claude
so for example when Claude is reviewing the
codebase and documents it might find out that
you missed a requirement in your PRD so Claude
should challenge your assumptions just like

[00:02]
working with a great engineer together you can
achieve a higher quality outcome faster than you
would have on your own this is what augmentation
not automation will look like we do also envision
that Claude will be able to operate on tasks
like this entirely independently so take that
same refactor and imagine that you just assign
the whole thing to Claude even without tight
human oversight Claude will create comprehensive
plans for the refactor it will use tools like web
search and document search to make sure that it's
up operating from the most up-to-date information
and it will use your company standards and best
practices to write production ready code claude
writes tests recognizes and fixes its mistakes it
can take feedback and remember your feedback so
it doesn't make the same mistake twice so when
models work independently like this we really

[00:03]
think trust and communication are paramount so
Cloud needs to follow your instructions it also
needs to communicate its decisions with you in a
way that you can review them it needs to be able
to adapt to changing inputs and new information
so in both of these examples Claude would need to
work over many hours to complete the task if you
use Cloud.AI or Claude Code regularly you might
be familiar with Claude doing in seconds what
takes you minutes or hours but our vision goes
beyond that we want Claude to be able to take
on tasks that will take it hours to complete
and we think that when this is possible it will
dramatically expand what AI agents can do so this
is our vision an AI that works alongside you
builds trust while working independently and
can take on complex tasks that require sustained
focus so let's dive in on how Cloud 4 is making
this a reality as you heard earlier from
Daario we launched two new models today

[00:04]
claude Opus for and Claude sonnet for and I'm
going to talk through four main improvement areas
thinking and tool use memory instruction following
and reduced reward hacking we'll discuss how these
improvements contribute towards our agent vision
let's start with extended thinking and tool use
earlier this year we launched Claude 3.7 Sonnet
which was our first hybrid reasoning model and
what that means is the model can respond nearly
to your request or think deeply before responding
with Cloud 4 we're expanding on thinking by
introducing a new beta capability for Claude
to alternate between thinking and tool use let me
walk you through an example so here I've provided
Claude with a CSV of bike rental data and I gave
it a very open-ended prompt i told it to just tell
me the most the three most interesting things
about this data claude has access to a ripple

[00:05]
tool which lets it run code autonomously to
analyze the data but it's never seen this
data before so when it first thinks it's actually
thinking quite tactically about how to handle the
large file and the first thing it does is print
itself out the headers so that it can understand
the data structure and like what is even in this
data it's only in the second and third thinking
block that it starts to actually think about the
prompt and the problem at hand so um it starts
to plan where it's going to find interesting
patterns it decides to look for hourly patterns
in bike rentals different patterns for casual
versus registered users and seasonal and weather
patterns oops sorry
it runs through its plan completing the analysis
and Claude was able to find interesting patterns
like the fact that ca casual versus
registered users have different time of

[00:06]
day usage it found a clear evening commuting
pattern and kind of no surprise to any of us
it found that bike rentals were 1.8 times
more common on sunny days versus rainy days
the next capability I want to talk about is memory
we think memory is critically important for our
next generation agents vision for two reasons
first no one wants to work with an agent that
you have to keep reminding the same things over
and over again but secondly and more tactically
if Claude is working over hours it can't keep
every single detail in its context window
it needs to be smarter and only remember the
most salient and important facts claude Opus
4 demonstrates remarkably better memor memory
capabilities so when given an external file
system with which it can read and write
memories Claude Opus is able to come

[00:07]
up with a plan remember that plan and track
progress against that plan over hours of work
so we're going to take a slight detour and
talk about the game of Pokemon as a way to
illustrate uh this memory capability so if you're
we've been using Pokemon as a practical prototype
for testing Claude's agent capabilities for
a while if you're interested in learning more
about this my colleague David will be giving a
talk later today and I recommend checking it out
uh for the purpose of this talk today I want
to talk about uh how Claude is using memory in
Pokemon so if you think back to your game boy days
uh the game of Pokemon is really you go around and
catch Pokemon and then you train them up so that
they can win battles and this concept of training
is like really core to the game you need to teach
your Pokemon how to win battles and that takes
time where you go around and uh have the Pokemon
battle other Pokemon to level up prior Claude

[00:08]
models would recognize this and decide that they
had to go train their Pokemon but would quickly
like lose track of their plan uh and start doing
something else before their Pokemon were able to
level up opus 4 on the other hand is meticulously
tracking its Pokemon's training progress so here
in its memory file it keeps track of the fact
that it has uh played 64 battles and to put that
into context 64 battles would take Claude about 12
hours of continuous gameplay claude Opus remains
focused on its training goals logging Pokemon
level improvements in this file so memory is a new
model capability we're excited about because of
how it will unlock longer arc agentic trajectories
a third improvement I want to highlight is
improvements in complex instruction following

[00:09]
this one is near and dear to me because I've
spent many hours working on Claude's system
prompt and we're finding that as agent
systems become more complex the system
prompts and sets of instructions that govern
Claude's behavior are getting longer so for
example our own CloudAI system prompt is
about 16,000 tokens right now so that's
16,000 tokens of instructions that Claude needs
to be able to follow for Claude to work in these
systems it's important that its behaviors are
steerable by you the developer so you're each
building different applications that may have
different requirements and principles that
govern Claude's behavior we've trained Cloud
4 models to specifically to be able to follow
instructions within long and complex system
prompts longer than 10,000 tokens for example
it's easier to steer Claude when to use tools and
when not to use tools and in our own system prompt
this improved instruction following has actually
allowed us to reduce the size of the prompt by

[00:10]
70% finally I want to highlight improvements
on a behavior we call reward hacking so reward
hacking is when models take shortcuts to achieve
an outcome or a result without actually solving
the problem at hand you can think of it like hard
coding tests or commenting them out this behavior
is extremely trust busting for users so when you
see it happen it makes you feel like you have to
meticulously review everything Claude does and
every line of code while we don't consider this
an entirely solved problem Cloud4 models show
significantly reduced tendency to reward hack on
an evaluation set of problems that were selected
due to this tendency in past models claude 4 shows
more than 80% less tendency towards the behavior
and this means you can better trust Claude to
complete your task the right way while being
honest about its limitations and uncertainties

[00:11]
so these four improvements thinking and tool use
memory improved steering and reward hacking work
together to create a claude that is more capable
coherent and trustworthy over longer time horizons
now I want to spend the last few minutes getting
practical and providing you and your team's tips
to get the most out of these models when you get
back to the office tomorrow the first decision
you'll have to make is which model to use and our
recommendation is always to test the models within
your evaluations and your product to ultimately
make this decision but to give you some highle
guidance here Opus is our most capable model with
frontier intelligence it will be best for the
most complex tasks you have so think coding within
large and complex code bases ch uh code migrations
or refactors long horizon agentic tasks and
planning and orchestration a good rule of thumb

[00:12]
here is that if sonnet 3.7 is getting 60 or 70%
on your evaluation it will be a great use case for
testing opus sonnet 4 is fast and efficient and
is great for use cases that sonnet 3 is excel 3.7
is excelling at today it spikes at agentic coding
and will be awesome for app development and green
field coding generation kind of vibe coding um
as well as any use case that has humans in the
loop when upgrading to the new models you may need
to adjust your prompts to get the best performance
so those of you familiar with Sonnet 3.7 might
be aware of its ability to go above and beyond
the given user request i've seen this described
as something like you ask it to change the color
on a button and it codes you an entire new app uh
we call this behavior overeagerness and cloud for

[00:13]
models are much less overeager by default so what
this means is if you have language in your prompt
that aims to dampen sonnet 3.7's proclivity
towards overeagerness you'll want to remove
that language we don't think it's needed anymore
and if you have an application where you think
this above and beyond behavior is beneficial
to users you should just tell the model to go
above and beyond in the prompt cloud for models
are more than capable of delivering that as well
we are also finding the models have better
attention to detail in the prompt this goes
along with the improved instruction following but
you might need to audit your prompt to make sure
that you're actually encouraging the behaviors
you want to see so for example when we were
testing this model on claw.ai we couldn't figure
out why occasionally it was using the wrong XML
tag for citations and we root caused it to
one single typo in our prompt with examples

[00:14]
if you're using Cloud 4 with tool use
you can prompt Cloud 4 models to call
tools in parallel so this lets Claude
parallelize tasks uh running more than
one thing simultaneously when using interleaf
thinking and tool use you can actually tell
Claude specifically what to think about
in between tool calls so you might tell
Claude to carefully reflect on search result
quality and plan next steps before proceeding
and finally if you're using tools it's a good
idea to tell Claude when and when it should not
invoke those tools within your prompt we found the
improved instruction quality instruction following
qualities of Claude 4 have been very effective
at addressing tool overt triggering problems
so to recap we're building towards a long-term
vision where Claude can work alongside you
complete work for you over long sustained
durations we think you'll find Cloud 4 models

[00:15]
great for agents because of interleaf thinking
and tool use memory improved instruction following
and reduced reward hacking so what can you do
tomorrow when you get back to the office start
experimenting try building with both models using
Opus for your most complex and ambitious tasks and
Sonnet for everything else invest some time in
prompt engineering very small changes to your
prompt can make a large difference to performance
all of these models are slightly different and
share your feedback with us because it will help
us make the next generations of Claude even better
thanks for joining me today we're really excited
to see what you build with these new models and
I'm happy to take any questions you'll need
to walk over to the microphones in the aisles
[Applause]
here no questions you're all good to go awesome

[00:16]
so uh both uh Opus 4 and Sonnet 4 are doing
really well on Sweetbench and some of the
other benchmarks however most folks realize
that like benchmarks and practical use is not
really comparable are you also developing
new benchmarks for software development as
these things get better and are there things
like uh evaluations for overeagerness and
things like that where we can get a sense of it
beforehand before the product actually releases
yeah great question we test these models quite
extensively before we release them through what
we call like a Swiss cheese of testing methods
so benchmarks are only one thing we look at um
we also use them internally quite extensively
before launch so anthropic employees have been

[00:17]
using these models on cloud code for weeks for
example and that helps us better understand how
they perform in practical use we do some
testing with early access customers and
so we do we like are interested in developing
more and more benchmarks but we don't think
that benchmarks are the only way to look
at how good these models are let's go on
this side yeah so I was curious uh in all of the
demons and use cases that you presented so far
uh it seems to be very centered on text right
uh coding and text in general so uh I wanted to
ask you if you can comment on uh you know your the
multimodel capabilities of the model in particular
uh images and and audio yeah we actually think
images um uh the models can see images and respond
to images we think it's pretty important for agent
capabilities we see image use even within coding
for example when people share with the model the
front end that the model designed then the model
can go back and fix things so we're continuing
to improve on our multimodal input capabilities

[00:18]
um because we we think it's going to be
really critical for um cla to be able to
do these complex tasks on on its own hello um
hey so sometimes uh I use cloud tool calling
not as an execution mechanism but more so as a
survey mechanism for instance I'm like analyze
the situation here and the tools are like option
A option B option C uh have you guys factored that
use case for tool calling like into your training
for instance um that is not something I've heard
of before but sounds really interesting we if
you find me after the break I'd like love to
learn more about how how you think about that
yeah absolutely it's a great use case thanks
so I'm I'm really enjoying all the focus
on practical software engineering tasks
one thing that is difficulty with LLMs on a large
legacy codebase is no matter how good it is at

[00:19]
reading just a blob of text the actual structure
of the situation that it's involved in is is just
so vast that like you kind of need to represent
it some other way in order to navigate around so I
wonder what kind of patterns you have found useful
in navigating these these larger legacy contexts
i think our general philosophy is that um we're
trying to improve Cloud's ability to do agentic
search so you can think of agentic search like you
search for something and then you can think about
it a little bit more and then search again um and
use the information over time to like inform what
you're doing and that applies to both code and
like the deep research capabilities which we have
on cloud.ai um and so uh that combined with this
memory capability where maybe Claude can write
down where certain information is in the codebase
we think will help solve that problem hello um
so in your presentation you mentioned something
about uh being able to specify like what the model

[00:20]
should be thinking about in between tool calls how
controllable is like the length of thinking tokens
in terms of like how much the model should
be thinking or like being able to specify
um yeah like length of that or also like specific
tool calls within the actual like chain of thought
process is that possible with the model so
you have control over the maximum thinking
length but the model adapts its thinking length
to how much it actually needs to think to solve
the task so you kind of have like a thinking
budget which you give the model and the model
won't go over that budget but might be under
that budget okay okay so if I wanted it if I
wanted to ask the model to think for like a
specific number of tokens that's not possible
right now you can tell it to think for less than a
certain number of less than a certain number okay
two questions the first one is a gimme what is
the preferred mechanism for feedback because there
are lots of ways to get in touch with you and then
the second is does the increased steerability mean
that we can finally ask um Claude not to generate
insane numbers of inane comments when it writes

[00:21]
code um I hope so um actually I hope that they're
better at that by default because of this like
less overeager tendency um and it should also
follow your instructions better um on feedback
uh I think like we love just talking to people
so if you find an anthropic employee today that
would be excellent um and would love to hear
more about your experiences and then I think
we have some like online uh uh feedback
forms as well awesome i think we'll call
it here but thanks everyone for joining me
i hope you're excited about Cloud 4 uh and
uh come find us after the break uh to chat more
about these great new models [Applause] [Music]

[00:22]
[Music]
nobody

</details>
