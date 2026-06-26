<!-- source: https://claude.com/blog/code-w-claude-sf-2026-sf -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

# Code w/ Claude SF 2026 recap: Building on the AI exponential

Missed our SF Code w/ Claude developer conference? Keynotes and breakout sessions are now on YouTube.

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Code

* Date

  May 12, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/code-w-claude-sf-2026-sf

This week in San Francisco, we hosted [Code w/ Claude](https://claude.com/code-with-claude/san-francisco#agenda), our annual developer conference. The event brought together developers, engineers, and founders for two days of keynotes, breakout sessions, and workshops with the teams building Claude.

From prompting and [model selection](https://www.youtube.com/watch?v=OXJO4LldSnc&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=12) to architecting skills and [scaling AI-native engineering teams](https://www.youtube.com/watch?v=igO8iyca2_g&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=11), every session circled the same shift: the distance between an idea and production software is narrowing, and the teams getting the most leverage are designing for the AI exponential—not reacting to it.

<!-- yt-inline:OXJO4LldSnc -->
[![The thinking lever](https://img.youtube.com/vi/OXJO4LldSnc/hqdefault.jpg)](https://www.youtube.com/watch?v=OXJO4LldSnc)

<details>
<summary>📺 자막: The thinking lever (24:02)</summary>

[00:00]
All right.
Hello everyone and welcome. My name is
Matt Bleifer. I am a product manager on
Anthropic's research team. And today I
will be sharing a little bit how
Claude leverages compute at inference
time, otherwise known as test time
compute, in order to break down and
solve some of your hardest software
engineering challenges.
Along the way, I'll share a little bit
about what levers you have at your
disposal in order to influence how
Claude spends tokens, and I will also
share some best practices to help you be
able to get the most out of it.
So one of the key developments in large
language models over the last couple of
years has been the scaling of test time
compute, creating something that we've

[00:01]
all come to know as reasoning models.
Similar to how we can scale compute at
training time by training bigger models
over longer time horizons using more
data, we can also scale compute at test
time by allowing those models to spend
more time working on a problem.
So if you look at this graph on the
left, you can see that when we move from
Haiku to Sonnet to Opus, as the model
gets more intelligent, it's able to get
a better score on our agentic coding
evaluation.
And then similarly in the graph on the
right, as that same model Opus actually
just spends more time working on a
problem, it's able to correspondingly
get better and better scores. This is
what we mean by scaling test time
compute.
Now this This true just of software
engineering, It's really true of a whole
variety of knowledge work domains,

[00:02]
whether it's agentic search, computer
use, or PhD level academic reasoning. If
we can allow models to spend more time
working on a problem, they can achieve
better and better results.
So, looking at a bunch of charts and
graphs is always great for understanding
the data and the different correlations,
but nothing really beats seeing a
tangible example of what this looks like
in practice. And so, what I went ahead
and did is I ran Opus 4.7 on a few
different effort levels, scaling the
amount of time that it works on a given
prompt.
Where in this case, I asked it to create
a realistic simulation of cars going
down a one-way street at a traffic
light.
So, the first result we have here is
Opus 4.7 running on low effort.
You can see in the simulation, it took
about 50 seconds to produce a result for

[00:03]
us and worked for about 4,600 output
tokens.
And I'd say it accomplished something
that was fairly reasonable. We do in
fact have cars going down a one-way
street.
Uh they are stopping at the traffic
light.
But overall, it's a pretty basic
simulation. The traffic flow is fairly
basic.
Uh the graphics are limited. And for
some reason, Claude thought it would be
a great idea to put the traffic light
right in the middle of the road, which
maybe wasn't the best design decision,
but we will still call it functionally
passing.
So, the next thing I did here is I went
ahead and I cranked that effort dial up
a bit. So, when I moved effort up to
high for Opus 4.7,
it took about twice the time working on
our traffic simulation and double the
output tokens. But as you can see, it
was able to achieve a better result.
It has cars of different types. It
smartly moved the traffic light over to

[00:04]
the side of the road. And Opus told me
that it even implemented what it called
an intelligent driver model where every
car would more uniquely respond to the
dynamics of the car around it, doing a
better job simulating simulating a
realistic traffic pattern. So again,
twice the amount of time, better
results.
Now, the last thing that I did here is I
cranked that effort dial all the way up
to max.
And in this setting, Opus 4.7 took 10x
the amount of time that it did when
executing this same prompt on low effort
and 10x amount the amount of tokens.
But as you can see, it was able to
achieve the best results yet. We have
the best graphics, my favorite traffic
light of all of them, and really
realistic driving patterns.
This is all an example of how when you
allow Claude, even on the same model, to
just spend more time working on a

[00:05]
problem, it can get better results.
As we continue to scale test time
compute further and further, Claude
isn't just going to work for seconds or
minutes or hours on a problem. It's
going to work for days, weeks, months,
even years, spending tokens to try to
solve some of humanity's toughest
challenges.
So when I talk about test time compute,
I really mean any form of Claude
spending tokens at inference time in
order to solve your problem.
However, we can break these token types
down into three a of distinct buckets.
The first bucket that we have is
thinking tokens. This is the classic
form of tokens that underlying
underlies what we know as reasoning
models.

[00:06]
Thinking tokens represent Claude's
internal monologue. It's Claude's space
to reason step-by-step, to consider
different potential options, do some
chain of thought reasoning, create a
scratch pad where it needs to work
through a problem, and ultimately spend
time thinking through what it needs to
do in order to take the best actions and
deliver the best results.
The second form of tokens that Claude
can spend when taking on a task is tool
calling tokens.
Tool calling is Claude's way of
interfacing with the rest of the world.
Whether it's using tool calls to execute
a search in this example, giving me more
information about the Code with Claude
conference,
or reading and writing files in order to
build out software engineering projects.
There's really millions of different
tools that Claude can call, but in all
of these scenarios, tool calling tokens
are Claude's way of interfacing with its
environment.

[00:07]
The last type of tokens that Claude can
spend is text. And this is Claude's way
of interacting with you.
Whether it needs to give you updates as
it's working on a really, really tough
problem and let you know how it's
progressing,
give you a summary at the end to explain
all of the things that it did in
response to the tough task that you gave
it, or simply just responding to a
simple question that you have, text
tokens are Claude's way of communicating
with an end user.
So again, we have three different types
of tokens: thinking, tool calling, and
text. And all three of these we think of
as really fundamental to the way in
which Claude works and the way in which
Claude responds to problems.
But all of these tokens that we're
spending have really direct costs to
users in the form of both practical
token costs that we pay for,
as well as waiting time when Claude
spends more tokens, it means that we as

[00:08]
users have to wait longer for our
result.
And so, we think it's really important
that we give users the ability to
influence or constrain how Claude spends
tokens.
Using Claude,
users can express their preferences and
constraints in a couple ways.
The first way is with that effort dial
that I talked about.
Effort is a way for you to tell Claude
how you want it to trade off time, cost,
and quality when responding to your
task.
Should Claude spend more time in order
to get a better answer?
Should it spend less time in order to
get a faster answer? These are all
preferences that you can give to Claude
as a user that it will take into account
when it goes and it spends these tokens.
Another form of constraints that users
can provide is in the form of budgets.
Recently, we launched a feature that we
call task budgets, which allows you to
tell Claude an upper bound of the amount

[00:09]
of tokens that it will spend when
working on a task. So, you might say,
"Hey, I want you to build out this
particular software engineering feature
for me, but I don't want you to spend
more than 100,000 tokens before you stop
and check in with me as a user."
Budgets could come in the form of
tokens,
but they could also come in the form of
time or cost. And I think this will get
increasingly important as we continue to
move up that exponential and Claude is
working for days, weeks, months, or more
to be able to give some guidelines about
how long it should work on a particular
problem before it stops to check in.
Now, given all of these preferences and
constraints,
it's really up to Claude to figure out
the best way to spend those tokens in
order to maximize outcome. So, given the
user's effort settings, given a
potential budget setting, how does
Claude allocate tokens across thinking,
tool calling, and text in order to
maximize its performance and its user

[00:10]
experience?
When reasoning models were first
introduced, they followed a really
specific pattern in terms of how to
spend these tokens.
The first thing they would do is they
would think, and they would spend those
thinking tokens to work through a
problem, and then after that, they would
move on to tool calling, and then
lastly, they would move to text.
We improved on this when we introduced
interleaved thinking, which allowed
Claude to actually use thinking and
reasoning in between tool calls.
In this mode, Claude could call a tool,
get a result, think about that result,
then determine what it wants to call
next, so on and so forth, all the way
until it decides to give a final answer.
Recently, we launched adaptive thinking,
and adaptive thinking is the next
evolution on top of interleaved
thinking.
In this new paradigm,

[00:11]
Claude is free to think whenever
appropriate. There's really no
constraint on when Claude needs to
think, how much it needs to think, or in
what order it spends any of these
tokens. It can leverage thinking, tool
use, and text in whatever order is
needed in order to best meet the
requirements of your task.
Claude could choose to start with a text
response in order to acknowledge the
user request. It could stop to call a
tool. It could then think about that
tool, respond to the user to give an
update, continue to call tools, so on
and so forth, all the way until it
provides that final answer of the work
that it did.
Claude could also choose not to think at
all for simple queries that don't
require it. Now, in practice, Claude
will typically think more often and
longer in response to higher effort
levels, but everything is really prompt
dependent. You can imagine that if I
were to survey someone in the in the
crowd here and say, "What is 2 + 2?" and

[00:12]
I ask them to spend a little bit amount
of time on the problem versus a lot of
time on the problem, you're roughly
going to spend the equivalent amount of
time working on that problem.
However, the story would change a lot if
I asked you to conduct a really
sophisticated research task. The
difference between your thinking on
low-effort and high-effort there could
be quite dramatic.
Now, adaptive thinking is not a model
router, and it's not an automated
thinking toggle. So, it's not taking
your query, classifying it based off of
difficulty, and figuring out whether it
should use a thinking version of the
model or a non-thinking version of the
model.
Rather, it's the difference between
telling Claude, "You must spend at least
one thinking token at the start of this
response." and telling Claude, "You can
spend thinking tokens whenever and
however needed in order to solve this
problem."
It's really about Claude having the
option to think at every single step of

[00:13]
the process.
We run all of our benchmarks on adaptive
thinking since Opus 4.6, and it's really
our intelligence maximizing setting that
shows performance parity or better with
inner leaf thinking while delivering a
better user experience.
So, I want to dig a little bit more into
effort and contrast it to the ways in
which we've used thinking in the past.
Historically, users have used thinking
toggles a lot like an effort dial. So,
if you wanted Claude to spend more time
working on a problem, you might turn on
thinking inside of Claude.ai or Claude
Code, and you would expect that it would
spend more time working in order to give
you a better result.
That's a pretty reasonable instinct.
However, thinking toggles are kind of a
poor proxy for an effort dial.
Rather than expressing how hard you want
Claude to work, what you're really doing
is you are turning on and off a really
core capability of the model. You're

[00:14]
constraining how it's allowed to work,
not how hard you want it to work.
An effort dial is a much better
expression of the idea of spend more
tokens in order to get a better answer.
It moves thinking, tool use, and output
text all together instead of just
toggling one of them.
As an analogy with tool use, we don't
tell Claude to always search or never
search. We tell Claude to figure out
when it should search based off of the
problem at hand, and that's really what
allows Claude to be agentic in response
to your query.
In a similar way, when we work with all
of our teammates, uh we don't ask them
to turn their inner monologue on and off
in response to a question. Uh we ask
them how hard to try, and then our
teammates decide how hard they are going
to think on that problem and what
actions that they will take in response.
So, I wanted to dig in a little bit more
on effort and give you some practical

[00:15]
guidance of how you should think about
setting these effort levels depending on
your use case at hand.
First, whenever possible, it's always
best to run evals and then chart
performance where you compare on your
x-axis here something like total tokens,
time, or cost, and on your y-axis
performance.
This allows you to create an effort
curve like this and get a better idea of
what trade-offs you might make by
selecting a given effort level.
Higher effort is going to improve
performance on most intelligence-bound
tasks,
but it also may show diminishing
returns. For your use case, you might
look at a graph like this and say, "I
will spend whatever tokens I need in
order to get the best intelligence." Or
you might say, "The relative improvement
in performance between extra high and
max is not worth the difference in
tokens that I will spend, and so extra
high is a better setting for my use
case."
Low effort can instead help accomplish a

[00:16]
task much quicker and save you a lot of
tokens, but it's also going to limit how
thorough Claude is in accomplishing the
task at hand.
As a quick tip, my advice is that when
using low effort, Claude is really
trying to save tokens as much as
possible, and so sometimes you may catch
it taking unexpected shortcuts that you
didn't expect it to. And so, in addition
to looking at evals, we always think
it's a best practice to spend time
reading your transcripts and better
understand exactly how Claude is
responding at a given effort level for
the thing that you're asking it to do.
On the flip side, uh low efforts have
also surprised us in some really
interesting ways. So, one of my favorite
evaluations that we've created is called
Claude Plays Pokémon, where uh Claude
gets the opportunity to work its way
through the original Pokémon Red game
that many of us uh grew up knowing and
loving.
When we ran Claude Plays Pokémon on low
effort, something really interesting

[00:17]
happened, and it actually ended up
treating the game much like a speedrun.
So, it would skip trainer battles in
order to save itself some time. It would
use healing items that it stocked up on
instead of wasting time going back to
Pokémon Healing Centers, and it would
spam an item called a repel that would
limit disruptive encounters with other
Pokémon, making it through caves much
more quickly.
And what I find most interesting about
this is often times we might correlate
low effort with lower intelligence, but
for any of us that grew up playing this
game, what you really realize is this is
a super clever strategy. It takes a
certain amount of intelligence to figure
out how you might minimize token spend
in order to get through these levels as
fast as possible. And so it was
interesting to see how Claude's
interpretation of low effort translated
to beat the game as fast as possible
employing actually very clever
strategies along the way.
So Evals are always ideal. I'll always

[00:18]
champion them anytime that you have
them. But I wanted to just give you some
quick rules of thumb on how you might
select an effort setting in the absence
of Evals or even if you have them. This
is just a good way to think about
things.
First, max effort, no surprise, can
deliver gains on your hardest tasks. But
as I mentioned before, it can sometimes
show signs of diminishing returns.
I recommend testing it for your most
intelligence demanding use cases, but
don't always assume that this is going
to be either the ceiling on performance
or really the best bang for your buck.
It could be the case that a level down
is going to give you roughly equivalent
performance at a real fraction of the
cost.
Extra high effort is a new setting that
we introduced with Claude Opus 4.7, and
we found this to be the best setting for
most coding and agentic use cases.
This is currently our default in Claude
Code and Claude.ai for Opus 4.7. And
like I said, it really does a good job
maximizing intelligence without kind of

[00:19]
going overboard.
High effort is a great setting if you're
trying to balance token usage and
intelligence, and this is probably the
value that I would recommend for any
intelligence sensitive use case. High is
a good place to start and test up from
there.
Medium is good for cost-sensitive use
cases where you're willing to trade a
little bit of intelligence
in order to get a much faster result.
And then low is good for reserving for
kind of your short-scope tasks and
latency-sensitive workloads.
However, as I mentioned before, it's
always good to just put it in practice
and see what actually happens because it
might surprise you.
I mentioned at the start of the talk
that test time compute is a second way
of scaling intelligence as compared to
training time compute.
So, it kind of begs the question if both
give similar tradeoffs with respect to
performance, speed, and cost,
when should I use a smaller model or
when should I use a lower effort level

[00:20]
on a bigger model?
As some quick guidelines, I would say
first, low effort on a bigger model is
good for an intelligence-demanding use
case where you're trying to optimize for
speed.
Going back to our example here of our
traffic light simulation, you can see
that Opus 4.7 on low effort spent about
the same amount of output tokens and
only took a little bit longer than Haiku
4.5 on max effort, but I would say it
achieved a much better result. So, often
the low effort on the larger more
intelligent model can give you a better
bang for your buck when trading off
speed versus intelligence on
an intelligence-demanding use case.
On the flip side,
smaller models can be really good if
you're trying to optimize cost and your
use case is not too
intelligence-demanding.
So, if you have some simpler LLM tasks,
especially if you need to do them in
bulk, something like classification,
information extraction, basic
summarization, that's where small models

[00:21]
are going to come in handy and they're
going to be able to save you a lot of
cost when you don't need peak
intelligence.
Another case where small models are
really useful is if your application
demands a really low time to first
token. So, if you want Claude to give
responses as fast as possible in
response to a user query, the nature of
the smaller models means that they will
produce tokens often times much sooner
sooner and give you a better time to
first token. The way that I think about
this is use small models for a fast time
to first token, use bigger models at
lower effort for a fast time to last
token.
Wherever possible, as I said before, I
recommend evaluating both. It's good to
build these eval curves across a few
different model types and across various
effort levels and then look at what the
tradeoffs give you for your use case
that you're trying to optimize.
All right. So, before closing the talk,
I wanted to just summarize three key
actionable items that I hope that you

[00:22]
take away from this.
One, enable thinking whenever possible
in order to give Claude that space to
reason. Thinking, like I said, is really
core to how Claude works and gives it
that space and that inner monologue to
be able to work through your problem as
efficiently as possible.
If you want to modulate the amount of
time that Claude is spending thinking on
your problem, I recommend using effort
levels or budgets as your way of
influencing Claude's behavior.
Second, I might sound like a broken
record here, but if you have evals, use
them.
Use that to find your ideal balance.
Chart your curves, test on different
effort settings, test with different
budgets, test with different models,
look at what the performance gives you
and decide what makes sense for your use
case without forgetting to always dig in
and read those transcripts.
And lastly, if you're not going to do
any of that and you just need to make a
choice and you're working on anything
coding and software engineering related,
my advice would be go with extra high.
It's a pretty good setting and gives a
great bang for your buck while

[00:23]
delivering great intelligence.
Our North Star for Claude overall is
that it allocates compute incredibly
well when asked for it, and that you can
set a quality bar and a budget, and
Claude will just go ahead and figure out
the rest and give you the best
performance for your use case.
Adaptive thinking and effort levels and
budgets are all a step in this
direction, but they're really just the
beginning and there's a lot more to
come. I'm excited to share more with you
in the future, so stay tuned and thanks
so much for taking the time.
If you want to chat more about this,
I'll be around the conference in the
audience. I'm always happy to nerd out
about these things, so thank you.

</details>


<!-- yt-inline:igO8iyca2_g -->
[![Running an AI-native engineering org](https://img.youtube.com/vi/igO8iyca2_g/hqdefault.jpg)](https://www.youtube.com/watch?v=igO8iyca2_g)

<details>
<summary>📺 자막: Running an AI-native engineering org (28:38)</summary>

[00:00]
[music]
>> Hey folks, do y'all hear me okay?
Okay, I I I swear this is not a Claude
Code thing, but do you guys mind if I
take a photo? Cuz cuz Boris and Jared
had their session at 2:00 and I really
thought this was going to be empty. I'm
like, there is just no way people would
still be coming in from that session.
So,
Oh my gosh.
>> [screaming]
>> Thank you, prompt. I promise me and
Boris don't just do selfie words all the
time.
>> [laughter]
>> But good afternoon and thanks for
attending. So, yeah, my name is Fiona
Fung and I lead Claude Code and Cowie
engineering and product. So, I work
really closely with Boris and Cat. And
before Anthropic, I had led and grown
teams at Meta and then also Microsoft.
And so, for today's talk, this is kind
of like overall agenda, but the whole
idea is what are some of the lessons I
learned and helping Claude Code and

[00:01]
Cowie kind of like grow and as we're
building out this team. And kind of like
what things I and it's it's interesting
as lessons I learned even if I think
about my time at Meta or even Microsoft,
but even Anthropic. Like it's funny, I
did this slide deck maybe like a month
ago and also already I've had to change
some of the content cuz for example,
when I started this deck, there were no
routines and that even like that way of
working was different for me.
And so, yeah, like we really want to
like I want to kind of cover five themes
that I've noticed. One which is the
bottlenecks have moved, they've shifted.
And so, when bottlenecks shift, what are
then some of the team norms that we had
to rewrite within the Claude Code team?
I also wanted to share a little bit
about all these team norms we had to
rewrite, how we rolled them out, and
also what are some of the proof as some
of the you know, like some some signals
that I get of well, yeah, we're trending
in the right direction. And it's always
going to be important for me to kind of
look at to see is it still serving us,
trending in the right direction? And
then I'll end it with a few kind of like

[00:02]
questions that I still have for myself,
and then also some suggestions for you
to maybe take an action and embark uh to
your teams to have conversations
together.
So with that, the first section, the
bottlenecks have moved. I call it the
shift. But you'll probably hear me
repeat this kind of subtitle text a lot,
which is what served you prior may not
serve you any longer. And when actually
even when I think about all my
experience, whether it was like at
Anthropic or Meta or Microsoft, the
constant growth mindset is just a muscle
that has served me really well. And
especially right now when the rate of I
don't know if y'all are feeling it, the
rate of change is just a little bit
crazy, right? Like I remember the first
time I started doing some live coding
was last year, and it was still making
some some, you know, bugs that I'm like,
"Ah, why why are you using constants
everywhere? That's not good engineering
practice." And now it's it's, you know,
just become so much more capable. But
that's that's what I I'm seeing as this
interesting shift of when the
bottlenecks moved, how do you think
about adapting uh in terms of everything

[00:03]
else around that bottleneck?
So maybe y'all are feeling this too, but
like for years engineering bandwidth was
the expensive thing. Like coding
throughput was really expensive. And
when you think about all the processes
we have of shipping software, a lot of
it was around Hi, welcome. There's a
chair. Take away those reserved tags.
There's no one sitting.
>> [laughter]
>> And there's another one right here, sir.
Welcome. Um but yeah, like all of that,
like even when you think about how we
used to do planning, like remember we
used to do like waterfall and then
agile, everything was used to be because
engineering bandwidth was really
expensive. Actually, I'll take a little
segue here.
This is not the first time our Like when
you think about our industry, we've
always had to adapt. Like I'm going to
put you all in a time machine. Come back
with me all the way to the year 2000s.
That was when I started my career. I
worked on Visual Studio, and we were
shipping Visual Studio 2005.
And I kid you not, in those days, if
folks remember, we used to ship software

[00:04]
on like CD-ROMs. Before CD-ROMs, it was
actually floppy disk. And so, I still
remember VS 2005, there were really hard
deadlines. We had to hit those deadlines
cuz we had to get the software to the
manufacturing lab to print on the CDs,
to put in the boxes, to ship in the
stores. And so, when you when you even
think about that, when we were able to
distribute software online, that also
changed how we ship software. And so,
that's what I'm finding really
interesting of this this new, you know,
shift that I'm seeing is engineering
bandwidth. It's no longer the expensive
thing.
So, for example, on the Cloud Code team,
for sure, coding is rarely the slow part
anymore.
Um and I would say it's not even that
it's not the slow part, it's just also
the throughput has really, really
increased. So, it's not only like, "Yay,
we're all all getting to build more."
It's just the amount that we're
generating has also changed a lot.
And so, what we saw was, you know, when
your your bottleneck shifts from kind of
the coding and the actual act of typing,
like if you remember, it used to be
writing code was expensive or writing

[00:05]
tests or refactoring. I remember all of
these conversations of, "We have to
schedule some time to do refactoring.
Oh, but we have to do product work, and
this is expensive. When are you going to
find that time to do it?" All of that
has shifted now. That is no longer the
bottleneck. And so, when that happened,
sometimes I notice the bottlenecks end
up shifting towards other areas.
And so, what happened? Like, for
example, verification, review,
cross-functional partners, security.
Because coding is no longer the
bottleneck, and also we're doing so much
more of it, these are some of the new
bottlenecks that we're seeing. So, it's
really always us asking, "Is this code
correct? Who reviews this code?" That's
like probably one of the top questions I
get from all fellow end leaders. Like,
"How are humans keeping up with how you
guys are doing like code reviews.
And interestingly, also how is it
maintained? Because now it is also a lot
easier for us all to generate a lot of
code. So also thinking about that
maintenance cost, too.
So with that, these were some of the

[00:06]
processes that I noticed quietly stops
working. And I love that phrase quietly
stops working cuz I don't know if you
all like a lot of times we all put in
processes hopefully for a reason, right?
Like we're thinking, "Hey, there was a
gap here or we want to improve." But
what I've found over the years is rarely
do processes kill themselves. We tend to
just layer more and more and more
processes on. Like I remember that on
one team, we had so many SLAs. Like
there was a P0 bug SLA, a high pri- like
sub review instead of like Anyways,
there's so many SLAs. After a while I'm
like, "Oh no, we need to stack rank
priorities so that all the engineers
knew which SLA was going to be even more
important." And I remember even at that
time I thought, "Hey, we should start
thinking about what things we should
defrag a little bit." But um yeah, so
these are the processes that might have
served you. Do you remember again is
that line of what may have served you
may not serve you any longer. But like
the planning norms. We used to spend a
lot more time, you know, pre-planning
because coding time was expensive. Uh
code ownership, there used to also be a
lot of questions of who who who wrote

[00:07]
this code? Who owns it? That's a little
bit of an other question now. Uh code
reviews what we'll get into a little
bit.
Team makeup is interesting, too. It's
not only like roles are blurring, right?
Like so between like engineers can also
So now now have AI to help augment
non-engineering roles. My
non-engineering partners are also all
shipping code. So what happens when
roles start blurring and you don't have
those, you know, like the silos anymore?
And then that also goes to knowledge
share. Knowledge sharing and onboarding
and everything is another signal that
we're noticing at Cloud Code how we used
to do things change a little bit, too.
And so, you know, in the first section
we talked about the shift. So, within
the Cloud Code team, what are some of
the norms that we have to rewrite? So, I
want to share some of those with you and
then, you know, hopefully some of them
will resonate with you or you might find
helpful.
And so, number one is code review. Uh
like human judgment of like who actually
needs it and we'll kind of go through

[00:08]
all of these, but you know, like the
onboarding is also changed, how we do
planning, you heard about me talk about
like planning a lot, hiring, especially
with roles blurring and kind of team
makeup how that has changed for us, too.
And also org shape, that's kind of one
of my favorite spicy topics. I'll share
that story with y'all when I start
proposing that at Anthropic. I love my
recruiting partners, they're awesome,
but I remembered, you know, one
recruiting partner really did think I
was crazy. Um so, I want to share that
with y'all, too.
So, how have planning changed? But also
technical debates.
Planning, we do a lot less of it. Like I
would also say and also the timing, I
call it like JIT planning, almost like
JIT compiling because even when I first
joined, I'm like, "Don't we need a
six-month roadmap?" And we, you know, we
put some effort in, we wrote it, it was
pretty good for three months, and then I
came back over the new year and and so
many things had changed already. So, I
realized well, six-month roadmap just
seems like a little bit too long. So,
again, it's how do you make sure you
kind of like do just the right amount in
the right time because again,

[00:09]
prototyping and code generation is just
not the bottleneck that it used to be.
The technical debate one is a fun one,
too.
So, in technical debates, code wins.
I'll share with y'all when I first
joined the Cloud Code team, I wanted to
do a refactoring. I wanted to like get
to learn about the code base. And me and
Boris had a healthy technical debate of,
you know, which which way to go, and I
almost leaned into my old toolbox. I
almost tapped him on the shoulder to go,
"Let's go to that room and have a
whiteboard and we can and I'm like, wait
wait wait wait wait a minute. Nowadays,
I can just generate all the different
options we've been discussing. I
generated three PRs. And the cool part
about that for the technical debate is I
really cared not only about the
implementation of the API, but also the
impact to all the callers into the API.
And so when I can have Claude help me
generate the three different versions,
it allowed us to have a debate of not
only implementation, but also impact to
the colleagues. So I think that's
another really interesting kind of

[00:10]
pivotal change. Um so yeah, like you
know, when building is cheap, arguing
expensive, again, how does that shift
your team norms a bit? I do want to call
out this makes it even more important to
make sure you set up team culture for
how you think about alignment. For
example, what totally won't fly is
because code is, you know, so much
faster for us to generate, it shouldn't
be like the last person who check in
wins, you know, like I'm going to stay
up at 3:00 p.m. to submit this PR. I set
up a routine so that I get the last word
in. So definitely a no-no. That makes it
even more important to make sure you
have good team culture that can have
open, honest technical debates, but also
a good team alignment.
Uh so I talked a lot about kind of what
we reduce in in planning. On Cloud Code,
we definitely have reduced the design
doc before every code ritual. I would
say certain teams and for definitely
certain scenarios it's still really
important to think about design docs,
especially as we're doing like kind of
like async discussions. But on Cloud

[00:11]
Code, most of our discussions is like
instead of a doc, a PR. That's kind of
like one of the word we have of "Hey, we
found an idea, go prototype." That's the
other thing. We don't really do a lot of
product reviews because the landscape is
changing fast. So let's prototype, let's
actually get a lot of internal ants
using it, and I'm really a big fan of
shipping it out to all of you, and then
hearing all the excellent feedback so
that we can really And And again, like
that that has changed our planning
ritual to be a lot less design docs, and
mostly discussions are in PRs or
prototypes.
Um so we reduced that, but what did we
double down on? And I think this is an
area where we actually need to do more
and continue to being better, it's the
verification. Cuz again, it's like the
throughput is different. Um, and there
are new ways to break. So, how can you
scale out? And I call it kind of shift
left. Like in the old days, you would
get code out and and I would love to for
me to find bugs before any of you find
it. And what's better than me finding a
bug is actually what I call shift left,
like more more automation, so we catch
it earlier to the source. So, that is

[00:12]
something that I think we need to
continue to double down on. And the
other thing that's interesting is also
because roles are blurring. For example,
my designers like I would love to have
more confidence that when I checked in
this code, I don't break something. Like
I remember it, I fixed a I fixed a bug
in resume or something and the next day
I was catching up on Boris's, you know,
threads and I saw someone tag him up,
"I'm noticing a bug." I remembered
having that sinking feeling. I don't
know if y'all have ever like
Did I just catch a bug? Like so because
of the throughput like I just really
want to make sure everybody, regardless
of roles, just has a lot higher
confidence um for the change that
they're putting in.
Who made this change? And so my advice
here is again, because a lot all our all
our PRs are assisted by Claude, it's a
little bit of an odd question. And so
for us, what is more helpful than just
that question is what I call like double
clicking into it. Like so in the old
days, when you used to ask, "Who made
this change?" What question are you
really trying to answer? Are you looking
for who caused this regression?
Definitely don't want to blame, but just

[00:13]
want to know who was the last person
that touched this code that might have
caused this break. Or are you looking
for an expert to answer customer
question? Or are you looking to gain
context? So, whatever is that double
click question, also think about is
there a way you can automate. It's
funny, I mentioned that to change this
slide deck. When I started this talk
about a month ago, part of my every
morning is I would, you know, bring up
my desktop code and go into here's a
customer feedback channel and I kind of
want to ask it to summarize and and that
was just a morning ritual I would do
with my morning cup of coffee. Now it's
routines, right? Like I can set that up
and then even better than what I had
done before, which was how I kick it
off. I'll be like, with my morning cup
of coffee, I always get to kind of a
pretty good overview. So that's my point
of like code ownership is a little bit
more fuzzy, but on the flip side, double
click to what question you're really
trying to answer and seeing how Claude
can actually help you with those.
How do you keep up with code reviews? So
I'm really glad if y'all saw uh the
keynote this morning, Kat talked about
it. We definitely leverage heavily

[00:14]
Claude code review. Now what's
interesting is going to be where do you
trust Claude like a lot,
but then where do you still want a
human?
And so for sure like, you know, and
actually Claude also, as Kat showed
y'all the the Claude also does a great
job babysitting PRs. And so we
definitely have Claude handle all the
styling and lint and PR feedback
requests, even like maybe catching some
bugs and fixing them before it even uh
does a full commit. And also uh adding
tests. That's what like really what
we've leaned heavily into Claude for.
But where I still definitely want a
human is that expertise. It's all about
trust but verify. So for example, legal
review, I always definitely want to make
sure I'm getting my legal partner still.
Uh it's you know, like risk tolerance.
So for example, trust boundaries and
security sensitive code, I still want to
make sure I'm pulling in the experts. Um
the other area which which is kind of
fun is also that product sense and
taste. Like I remember one of the hobby
like one of the fun things I like to to

[00:15]
use Claude for is that I like to
decorate Claude for the holidays or the
seasons. And I remember last uh holiday,
I wanted to update Claude in the
terminal to, you know, give him a little
holiday theme. And I asked Claude code
to you turn Claude into a snowman.
Claude wasn't that good at ASCII art in
those days. And I remembered asking,
that's where product sense really comes
in. I asked my design partner, "Hey, can
you review this for me?" And she gave me
such good feedback. She's like, "You
turned Claude into like the Mr. Peanut
character." Cuz I was trying to
make him snow match. I was like, "Okay,
I'm going to do something more simple."
So, Claude was like ice blue with
snowflake, but keep in mind kind of that
product sense as well.
Which leads me to what should my team
makeup be? Because roles are blurring,
Claude is augmenting.
I'll share with you on Claude Code,
there's two profiles for engineers that
I'd really heavily indexed on. One are
like creative builders with product
sense. Usually, you'll see these are,
you know, the dreamers. There will be a
big sense of curiosity. They're really

[00:16]
passionate about, "Oh, here's a problem.
Here's a Maybe I could, you know, ship a
product that solves that problem." But
then there'll be a lot of iteration to
make sure you're delivering a delightful
experience. Um the other one is deep
systems expertise. So, when I first
joined Claude Code team, I noticed
actually we were pretty good with
product generalists and creative folks,
but we were missing folks with like
distributed systems expertise. And when
you're building things like Claude Code
remote to ensure we can run Claude's
everywhere, you really still need um
those expertise. So, I would say, you
know, whichever software engineering
lead you're part of or or supporting,
think about those hard parts of where
you might want to continue to still
double down. But for sure what I index
less on is raw throughput because thanks
to the models, we just saw a lot more uh
efficient.
The cross-functional gaps is another
interesting one. So, for example, I
remember that I wanted to do an update
to how we do survey responses, but I
didn't have a dedicated content designer
to work with me. And I'm a engineer, my
writing skills are quite terrible. I I

[00:17]
struggle to write things in a short and
succinct form. I don't want the surveys
to like, you know, overload you all in
the terminal of cuz every line space is
really important. But that's where
Claude, like in the old days I would be,
"Who is a group of content designer I
can work with?" And I can can of changes
back and forth. But now Claude has
really helped me to augment that role
and was a really good content design
partner for me to kind of like make sure
the verbage is is good and succinct. And
on the flip side, like I say a PM our PM
code a lot, which is really fun to see.
So again, like I I would say with Claude
like you have non-traditional coders now
being able to do more engineering, but
you also have engineers that we can also
now lean in to do things that was
traditionally, you know, like not on the
technical side but more of where the
content or design. So it's very
interesting. I found that Claude and AI
has really augmented roles kind of like
all around.
This was a spicy one. Uh
so I'm definitely like I remember when I
first joined Claude Code everyone's

[00:18]
like, "Okay, you're going to grow the
team by certain amount." and I could
tell recruiters were still using the
typical, you know, 10 ICs to one manager
and then how do you start think about
nesting? Um I really have leaned into
keeping it really scrappy. And actually
maybe I would step back to whether it's
at Anthropic or Meta or Microsoft,
whether it was like Visual Studio or
Facebook Marketplace or AR/VR devices or
Claude, like what I have found to really
help me ship great product is heavy
heavy heavy dogfooding. Especially for
leaders where nowadays it's actually
fun. I can still be in the code, but for
a while it wasn't. And when you can't
get your hands on the code, I would
always make sure I would make your time
so that I'm actually using my product
days in days out. And so that's why I
wanted every manager in Claude Code to
start out as an IC first. And also like
earn some street cred with the team and
and really learn how to be an effective
engineer.
Uh and and then I really structured the
org to be as flat as possible cuz I want
us to be super agile. This was just my
my recruiters had some concerns cuz I

[00:19]
remember they said, "You want to hire
managers and they will start as an IC
first. No manager would be interested in
that." I'm like, "Well, this is what
dogfooding on the Claude Code team's
about. And this is what I expect. And if
someone's not interested, it's better
for us to do uh earlier separation. But
also again, this is like there's no way
I would have been able to ramp or be
able to do code cuz my time is, you
know, there's just a lot of context
switching without Claude. And so for
those of you in the room who are
managers, I really, you know, like
encourage y'all to kind of like lean in.
It's I'll I'll be honest for for a long
time at Meta, I would still try every
year to do one PR a year just to but the
the code the the workflows would always
change. Like I all the internal tools,
like by the time I learn one command, it
would have changed. Nowadays, I don't
even remember get commands. I just
always ask Claude to to help me out out
with all of that.
Now with sharing, what becomes your new
source of truth?
So for example, on our team on Claude
Code, the code is the source of truth.

[00:20]
That's why I would go back to when I'm
like answering customer requests. I just
have my desktop Claude with desktop
Claude Code and then I have all my, you
know, like local repository so actually
answer a lot of customer questions. So
for us, just having that code base be
the source of truth also like prevents
some of the lag that you might have had
before of how to keep up the
documentation, you know, correct with
the code. But I would say this is where
it's like do what makes sense for your
team. So for example, if you still have
a lot of really good specs, check those
into the repositories and then have
Claude lean in to help, you know, like
hey, you know, like take a look at how
verify my code execution so matches what
I expect on the spec.
And so how did we roll it out? Cuz these
were like I had just gone through some
of the norms that we had changed. And I
think it's interesting, there's a blend
of what do we kind of like mandate as
team norms? Like make sure you're
gaining alignment with the team. And
then where do I really enable each, you
know, like we have pods within Claude
Code. Want to make sure I enable each
pod to do what makes sense for them as

[00:21]
well.
So in terms of the balance, in terms of
forcing function, it's align with the
teams on the must do. So, these are a
few of the core Claude code team
principles that we really live and
breathe. And by the way, if you remember
again, I I'll go back to that growth
mindset and always think about something
still serving you. We keep these up to
date. So, every few months, we'll be
like, "Hey, is this still having, you
know, the same effect or serving the
purpose that we wanted when we started
it?" So, for example, and I should
replace this slide. It's not every
engineer uses Claude code. You know,
that's obvious. It's actually every
Claude code team member, including
cross-functional partners. And actually,
we all use co-work quite a bit, too.
Uh Claudify everything you can. This is
one thing where we're like, "You know
what's better than one of us doing it?
Having Claude." So, always think about
Is there some way for you to automate,
whether it's verification, more shift
left, but always be thinking what you're
doing something right now? Is there some
way that Claude could actually help you
do it?
And the last one's my favorite, explicit
permission to kill old processes. Cuz

[00:22]
again, processes will kill themselves.
But as your supporting teams is really
important to always get that fast
feedback for your team of what are the
things that, you know, like are we spend
We're spending a lot of I'm actually I
remember when I first joined Claude
code, we used to do stand-ups. And then
the team got a little bit big, so then
we had a spreadsheet where we would all
put up our, you know, like weekly
process progress. And then I was like,
"Oh, wait, we should just do a
skill, right? like a a stand-up script.
So, then we can just run Claude and all
of us can always be very be much more
kept aware of what everybody else is
doing." So, that's just something
another example of one day I remember
spreadsheet Wait, "Does this still make
sense anymore?" So, always question and
always look to defrag and kill old
processes.
What I want to make sure that I leave a
lot of room for pods to adapt. It's For
each team really has a lot of high
agency for how, you know, they do triage
or leverage Claude to do triage, any
planning rituals or stand-ups, how they
think about on-calls, and also which
workflows to Claudify first. So, we

[00:23]
don't usually mandate thou shalt
automate this. We have some suggestions
and learnings, but always give room to
your team, especially they may be, you
know, touching on different problem
areas.
So, if I zoom out, what were the three
things I prioritize on, you know, I I
when I joined Cloud Code that I felt has
to make the biggest difference? Keeping
the team as flat as possible.
Um like managers release a pop pods of
work, but really keep it agile. So, for
example, on on Cloud Code and co-work,
we have one overall team mission. Cuz
sometimes when you start creating pods,
each pod then wants maybe to set up
their own mission, and then anytime you
have to shift, it might be take a lot of
time to to walk people through that, but
it's really as flat as you can. I felt
that served us really well.
The cloudify everything better than you
doing it. I see how Cloud can help you.
It really frees us up to do more of the
harder work. And again, the processes,
they do pile on. So, I encourage you to
kind of like work with your team to see
what are the processes that actually you

[00:24]
should be able to let go.
So, does it actually work?
I can't go into the explicit numbers,
but I think these are three general kind
of metrics that you can look at as
you're rolling out, you know, changes on
your team that might start steering you
to yeah, this seems like it's kind of uh
starting to be successful. The
onboarding ramp-up time that has
dramatically reduced. Uh so, that's an
interesting thing like like how soon an
engineer or a designer or, you know,
like a PM can start being effective on
your team.
Uh the PR cycle time shortening. I think
this one's interesting to double click
into a bit cuz it's it might actually
help you identify a gap that's not just
in terms of lack of AI adoption, but
where the rest of the pipeline might be
struggling to scale. So, for example,
again, as as we're now like, you know,
just putting in some through so much
more code, sometimes a product
infrastructure can build and CI still
keep up with the amount uh that
engineers are checking in.
Uh so, both of those should go down, but
then what should go up a little bit is

[00:25]
cloud-assisted commit. For example, for
us, it's by default every commit is
cloud-assisted. I don't think I've seen
a non-cloud-assisted commit probably in
the last 4 months or so. Um, but
hopefully these three things are are
kind of like metrics that you can kind
of take a look at at your team and see
how it resonates. I would also say
though, um, outside of just number of
commit, also think about the end goal.
Like if you zoom out,
what is the product that you're trying
to make more delightful for users? Or
what is the problem you're trying to
solve? Cuz sometimes you see it on all
the headlines of this company said X
percent of code is now generated by AI.
I think throughput is great, but really
think about how you measure what it is
that you're actually really trying to
solve. Like for example, we really want
to make sure we're keeping an eye on
quality and reliability, so those are
some of the things that we're paying
more attention to as well.
Okay, so the my last section is to audit
your own effort. I'll share with you
transparently, actually, I still have a
couple of questions that I'm still
asking myself. Um, the iOS and Android

[00:26]
org is a very interesting one. Like when
engineers can now more efficiently kind
of flex across different mobile
platforms, does a more traditional way
of, you know, uh, having an iOS team and
an Android team still make sense? That's
something that I'm still kind of
thinking through. How much do you push
that fully automated review? Again, like
when do you kind of strike that balance
between fast enough and we lost
something important? It goes back to the
trust but verify. And what's interesting
is you even might have heard today in
earlier during Danella's talk, the model
capabilities do keep improving. So also,
even if you might need to do more verify
than than trust for a certain section of
work, that might also change with the
next model. So it's why it's always
important to re-evaluate. And roles are
blurring, so how do you make sure that
everybody feels equally uh, productive?
So if I were to leave you with one, you
know, thing to take back of is, you
know, pick your noisiest workflow. And
by noisiest workflow, it could be most

[00:27]
expensive, what's something that, you
know, what you yourself might be
dreading, or even your team might not
really look forward to it. And ask, is
it still really serving what's the
purpose of there? Like, actually, I'll
share another funny story. There was a
team I was on where we used to have this
weekly review. It's a very expensive
review, like 50 people, you know, in
this large room. And then I noticed
everybody's on their laptops. Except for
when it's their time to give status
report, and then they they pop their
head up, say the status, and then go
back down. And I'm like, this is a very
expensive meeting. And I just asked that
simple question of why are we having it?
And just that one question, everybody's
like, yeah, it's true. And so we
canceled it. So, that's why it's always
important to to think. And And so, yeah,
like I I figured this might be something
fun for you to take back and look and
see what's one piece of workflow that
you might consider, can you either
automate, or maybe even is it still, you
know, proving is it still serving its
intended purpose.
So, with that, that's the end of our
talk. I'm like, thank you.

[00:28]
>> [applause]
>> Thank you.
Thank um thanks a lot for thanks a lot
for attending. I really, really for sure
thought this room was going to be empty.
So, thanks for not having by myself. And
I'm around here today and tomorrow. So,
if you have any questions or want to
chat more, feel free to introduce
yourself. I'm happy to chat.
Thank you.

</details>


We demonstrated this through [live coding sessions](https://www.youtube.com/watch?v=DlTCu_pNDHE&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=5), [customer deep-dives](https://www.youtube.com/watch?v=EdmuYPBt_EM&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=2), and hands-on tutorials highlighting what this looks like today.

<!-- yt-inline:DlTCu_pNDHE -->
[![Live coding session with Boris Cherny and Jarred Sumner](https://img.youtube.com/vi/DlTCu_pNDHE/hqdefault.jpg)](https://www.youtube.com/watch?v=DlTCu_pNDHE)

<details>
<summary>📺 자막: Live coding session with Boris Cherny and Jarred Sumner (32:00)</summary>

[00:01]
Please welcome to the stage head of Claude
[music] Code of Anthropic, Boris Churnney,
and creator of fun at Anthropic, Jared Sumner.
[music]
Hello.
All right. So, this is a developer conference.
We're going to be doing a little bit of talking,
but mostly we're just be like coding. So,
this is for the developers in the room.
I'm going to start by talking
a little bit about how uh
how bun uses cloud code to to build and and
maintain bond and also kind of how our setup
uh works and because it's kind of a a slightly
more advanced setup than uh what's common today.
Um but first I'm going to get a few agents
running to just fix some GitHub issues. Uh

[00:02]
this is classic Jared doing work during a talk.
Um so so in buns repo uh every time somebody
submits an issue uh we have a cloud bot
automatically run and try to reproduce
the issue. So you can see this person has
uh this this side effects and this is
like one of the most recent issues. Um
and and we can see that Robun which is our our our
bot uh uh went and managed to reproduce the issue
uh and submitted a PR automatically. Um and
and this PR is like it has uh it all these
PRs always have tests. Um it's one of the actual
hard requirements before it can submit a PR. Um uh
and so so the challenge here is like does
this code look correct? Um and one of the
things we do to to check that is does the test
fail in the previous version of bond and pass

[00:03]
uh in the in this debug branch. And it the
bot actually can't submit a PR without that
uh being the case. And so this is just to make
sure you understand. So this is like every single
issue that goes up in the bun issue tracker, you
have Robo Bun automatically try to reproduce it
before anyone looks at it. Yeah. And this saves
a lot of time because we have so many open GitHub
issues. Um it it really moves the challenge from
is from just fixing and debugging the issue to
is this the right thing to merge? Like is
this the right fix? Um how how good is it?
Is it is this doing like a 100% of yours?
Is it like 10%. We can go to the insights
uh uh and go to contributors and then if we
go uh last three months uh uh and this is
specifically to main we can see that Robbun is now
a bigger contributor to Bun than I am [laughter]

[00:04]
and that's with merging not all of its
PRs for sure. You can see we have a lot
of PRs open right now. Um the the challenge
is really how do we know can we merge the PR?
Um, and that's the tests. Um, and then the other
thing that's really interesting about this is uh
uh we have automatic code review bots that
that run. Um, and then they're going back
and forth. So like Code Rabbit leaves a
comment and then Roboun leaves a comment
and then they go back and forth and
they and Code Rabbit did the [laughter]
I love this. And it also marks the
comments as resolved when it's done. Um,
and you you can see they actually went a lot like
there's a lot of back and forth here. There's like
30 comments or something. And so you're using
like a combination of agents. So this is like
code review. This is like quad code review and
then also code rabbit and like you're using
them together. Yeah. And I I think basically like
code rabbit is is good for like kind of stylistic

[00:05]
issues and things that are like make sure that
it follows the cloud MD and then the the cloud
code review is really good at here's this really
subtle edge case that would have taken me like 30
minutes of reading all the code and having all
the context to to like figure out and and so so
it's really good at surfacing bugs that you you
need the full context to really understand. Um,
and I think basically it's it's really hard to
to actually have all this automation without
having code review that is in the loop with the
with claude there replying or replying is like
very performative but like at like fixing um and
that's also a big part of like what used to take
so much time uh when like why PRs would take so
much time to merge is because you'd have to like
like check out the branch locally, fix a
lint error, then run the llinter locally,

[00:06]
then push it back up. And there's all this
switching cost that's constantly there.
And so when you So I think this is like an
especially good use case for for LLMs because
otherwise like it just takes up so much time to
to ship and and I guess like especially for the
bun codebase because it's like it's systems code.
It's, you know, it's very easy to repro issue and
then see if the issue is fixed because this is
kind of back to what we were talking about before
with like this kind of verification loop. It's
all systems code. So, it's really like a test case
on a particular architecture and you can
essentially like repro or verify anything.
Yeah, that's one of one thing that makes it easier
in buttons codebase is because it's a a CLI tool.
um because uh we don't need to run a browser
to test things, but you can also just like
have something set up to like take a screenshot
or record a video or those sorts of things.
Um in Bun's case, we don't need that, at
least not yet. Uh uh there's a couple things

[00:07]
we could do that for like we have some
front end stuff that would be nice. Um
but yeah, I think this is like the the direction
that I think is really interesting is because
it saves so much time. Um and this is not this is
something that like this is specifically for bun
but the more generalizable thing when because most
products are not open source um uh is like instead
of an issue maybe the starting point is like a
customer support ticket. So like you could you
could imagine automatically uh h passing customer
support tickets to a cloudbot to then go and try
to reproduce the issue and then submit a PR and
then uh having code review go back and forth. Um,
and that's where I think for a lot of companies
it becomes a lot more impactful because it just
saves so much developer time. We should think
of some kind of name for this pattern. It's
like adversarial code review or or something like
that. Yeah, I don't know. Um, but I do think like

[00:08]
there's also a few other things about this that's
uh like the if you just do this then it doesn't
quite work. the very first step you need is
to like make sure the development environment
is set up. Um like I I think this has been talked
about before but like uh like cloud MD is uh
very important um because otherwise it's going to
just submit PRs that don't quite make sense for
you to merge. Um so like we very much emphasize
in buns codebase that it runs this special command
to do the build. Um and this both builds and runs
the command. So it like forwards the arguments. Um
because that's also one confusing thing is like
uh because bun has to be compiled uh you want to
make sure that it's running the actual changes
and not like a debug build that's like stale. Um
we also go into a lot of detail about how to run
tests, how to write tests, um where to put the
test, um uh and a lot of like here's how here's
all the issues that we've run into previously.

[00:09]
Like basically the the pattern here is like every
time that you find yourself repeating something
it should probably go in cloud MD
because the the question now is like
how do you make it maintainable to have
lots of claws running all the time and uh
and to do that it needs to be written down. It
needs to be documented. Um so like a really small
detail is like we we check the we have it like to
make sure that claude sees the error message uh we
make it print the air message before uh the like
less informative uh conditions. So, so this is
sort of like you have quad write a test and then
the test is bad or something about it doesn't work
and then you see this kind of repeated like once
or twice and then you just tell Quad add it to the
quad MD so that every time in the future when you
write a test you do it correctly the first time.
Yeah. So this is like uh like compound
engineering. It's kind of this.

[00:10]
Um and then also it's helpful to like give
it an overview of where all the folders are
like what all like how the code is laid out.
Um, and like about dependencies. Um, uh, uh,
another thing I think is interesting is like
making sure that it can read your CI errors
and like build logs. like you want to you
want to set up the agent to be able to
be able to read the code
like to do the full loop of
make of like writing the code testing the code
works checking CI monitoring CI um and uh uh
reading all the errors so that way by the time
it gets to a person everything is like set up
like the ideal is that you read the code and you
you have very clear indications that you can be
high confidence to merge it And the only way for
that to be true is if it is set up for success.

[00:11]
It's interesting. I remember when we when we first
met, you were talking about like your vision of
like everyone being able to run hundreds of agents
in parallel and how that would work. And I feel
like I didn't really get it at the time. Although
now like every night I I'm I'm running like
hundreds of agents every single night. And I feel
like now I'm finally there. But this is a thing
that you've been thinking about for a long time.
So it feels like this is sort of like the setup
in order to be able to kind of scale up agents
way more like you need the self-verification so
that agents can run autonomously. Yeah. Like this
has gone through many iterations in buns codebase.
Um we previously just had a discord bot where I
could just at mention the bot and it would spin
up a container. Um uh it didn't have like the CI
stuff. It didn't have uh the code review stuff.
Um, and it's so much better now,
especially with like Opus 47. Um,
uh, uh, it's all this stuff is getting so
much better. Um, oh yeah, we can also check on

[00:12]
how, uh, how it's going. It looks like
it created a PR, the first one. Um, uh,
and it wrote tests. Um, so maybe while we
look at this, I'm curious for like just to
get a show of hands for people in the room, like
as people think about their development process,
raise your hand if it looks something like this
where you have like a bunch of terminal windows
or desktop tabs and you're kind of pasting in
issues. Okay, so that's like maybe half of people.
And then what if it looks like Roboun or
something more like that where it's like
closing the loop a little more? It's like the
next level of abstraction starting to get there.
Yeah, I think it's like it's not surprising
because I think model capabilities are just
getting there. Like I think 47 is the first model
where it's really felt like it's able to do this.
And in the past maybe you could do it with
like a bunch of scaffolding like you just
throw a bunch of tokens at it and it can kind
of work. But now it's like efficient enough.
You can actually do this dayto-day. Yeah.
Um let's see. So the first PR is there. Uh

[00:13]
let's see if it did any others.
Uh okay. It did two PRs. Um uh
this looks very plausible. It's cool. And
this like this before after is this like
do you tell it to do that or sometimes it does
it? Um uh it's it's pretty good about knowing
like when it should do that like when it's like
a string formatting thing. Mhm. Um uh it's also
it also kept like bun style of the label which is
good because node style is slightly different. Um
let's see does this change look good? Um
yeah. Uh mostly what I'm thinking right now is
uh it it's it did this. This is good because like
you don't want to write one bite
at a time. You want to write uh
in in chunks um and then it used uh
saturation uh to to but I don't like

[00:14]
that or like it shouldn't have to do that.
Does anyone here actually know Zigg sort of
I feel looking at this code and and you can see it
followed the patterns from the from the cloud MD
await using and then that that pattern of of
uh reading all the pro like resolving all the
promises at the same time and so like what's your
workflow like when you when you see something like
this are you usually going in and like commenting
or are you just going to wait for like code review
to come in and and drop a comment? Um, usually it
depends on that like how complicated it is. Um,
in this case, I'll usually I'll wait for like this
one is actually pretty simple. I feel pretty high
confidence that if the test pass then uh I would
probably merge this. Um but I still would wait for
uh the code review for for at least for
the cloud code review one to run um uh

[00:15]
just in case because what I really like
about that is it will find things that
like from from that aren't in the diff that
are like from tracing the control flow. um
which is what you want when it's like a
human reviewing it is like somebody who
has a lot of context who who can think what are
all the edge cases that this might run into and
and the signal to noise ratio is pretty good. It's
something maybe like 10% of the time it's wrong
like that's and and for like how that used to
be like with other code review products that
we've tried it was like basically you
had to ignore most of what it said. Um
it's pretty cool. How how long how long has
something like this worked? Is it like a latest
model thing or like have you had like like Robo
Bun or this kind of like automated repro automated
fixing like this whole pipeline? Like how how long
has that been actually possible? We can probably
like see this in a chart somewhere. Um that's
kind of a lot of commits but I think that's
that might not be on main. That might
be that the the Rust thing. Um uh uh

[00:16]
yeah I heard bun is going to be written
in Rust soon. Is that I don't know.
We're there's a I just have a quad
running and we'll see what happens. Um uh
but you can see like the the the volume of commits
there. It's like kind of lower and then it it's
it's definitely gotten up a lot and then it's gone
up a lot. Uh now really the bottleneck is like
do I feel good about merging this? Am I confident
that its changes are correct? And that's new
because it used to be like the code wasn't
good enough. What do you think? What do you
think is left like like what's it going to take
before well like is there like a missing tool
or like a missing model capability or model
version or something for you to kind of feel
like Robban can fully close the loop. Issue comes
in and then like fix goes out automatically.
I think it needs a little bit more uh it needs
it takes a lot of time to verify the changes

[00:17]
are correct. M um this was kind of already true
like when it's a person pushing up a PR. Um uh
but I think the the challenge is like how do
we make it how do we make sure to communicate
sufficient proof that the changes are correct.
Um or making it easier to like roll back things.
Um that's I think those are kind of
the two directions. But I think like
for the majority of like simple issues, we should
probably be pressing merge a lot more. And the
bottleneck now is actually like CI and like
making sure that uh like like the and and having
like fully running the code like the the
making sure all the test stuff works. M um
but I think it's like basically there for like
and the large projects are still non-trivial

[00:18]
but also I've been doing some pretty large
PRs lately with with cloud mostly with in the
not as much with Robo Bun but with like cloud
code um like uh we recently added support for uh
a built-in image processing library to
bond. I could probably pull up the PR. Um,
uh, and that was Claude. Um, uh, and also we
did a bunch of follow-up PRs, too. Uh, yeah,
it's like it's interesting because I think like
when I look at different people using quad code,
everyone is like at a kind of different level
of like sophistication or kind of like adoption
of this. And I think for me the hardest thing
is the model changes very often. So I have to
like constantly reune and kind of recalibrate to
what it can do. And like as an engineer, it's hard
cuz it's like a very weird technology. It's like
the first technology I've used that's like that.
And I I sort of feel like this is actually the
way that you do it is ahead of how the quad code
team does it for quad code itself. And to me like
that that like the way the quad code team does it
is actually very automated. But this is like
even further ahead. This is like almost like

[00:19]
full liftoff like full fully closed loop. Like
in the last two weeks we've added an HTTP3 server
to bun. Uh there's a PR for an HTTP2 server.
There's uh fetch support for HTTP 3 and HTTP2.
Um there's this image processing API. There's
the ongoing Rust rewrite which may not ship. Uh
uh uh that that's like the most
ambitious one I've done so far.
Uh and I done is too strong of a word because
it's very much not done. Uh uh so and so even
something like this like this is like a benchmark.
So Claude ran this benchmark for you. Yeah, Claude
ran this benchmark. Uh I gave it like a this ran
on like a separate like uh on like a Linux box. Um
uh yeah and it and I was like make it faster
than sharp and that's basically what I did. Um
I gave it like a few ideas like oh you could try
like read this code in JavaScript core to like
figure out the how to like avoid cloning the
type array when it's not strictly necessary. Um,

[00:20]
but like it it then went and did it and figured it
out. Um, uh, and like uh, yeah, it's pretty crazy
honestly because it was these this wouldn't none
of this would have worked uh, several months ago.
Yeah. I I feel like like within like
within anthropic like within an AI lab,
you call this kind of thing hill climbing. And
this is this idea that like if you give the model
some sort of metric and then you give it a way to
verify its result, you can just make it iterate
and keep going and keep going until it hits
that metric. Um, and this is something like
47 I think is uniquely good at. And I think
it's something really underutilized because I
think it's the first model that's actually very
good at that. And if you just give it a target,
you give it a way to like improve the performance
and you give it a way to measure, it'll just like
keep going until until it's done if you let it go
in auto mode. Yeah. And we can also see like uh

[00:21]
this is another case where like the code review
comments was really really helpful because like
there was like in this PR there's
like 100 comments or something uh
and it's just going and fixing everything.
Um uh uh like it goes on for a while and
in the meantime you're just working on something
else. Yeah, I was this was not like my the thing I
was 100% focused on. I was maybe like 10% focused
on this. I was doing like five things at once. Um
uh uh and this definitely wasn't possible like
6 months ago. Um 3 months ago like this is like
very recent that this is doable. Okay. So how
how are our sessions doing? Yeah. So we have
one PR there. There's almost another PR
coming up it looks like pretty soon. Um uh
this one is should be the trickiest one. Uh
um it mostly looks good though. Um like the
or like it looks plausible based on this

[00:22]
these changes. I wouldn't exactly do it this
way, but I think that's we need like a better
more optimized way to do this because that's
a lot of checks. Um and and looking looking at
your setup here, so you're using you mostly use
CLI. Yeah. And um do you always use auto mode
for permissions? Auto? Yeah. And then before
that I used dangerously skip permissions. Um
[laughter]
no you guys can delete stuff if you do that. I
don't I think I'm not supposed to recommend that.
Um but I think it's just not fun to wait for
Claude to like press approve because then you just
like go off and do something else and then it's
just been sitting there. So that's why auto mode
is really good because it's actually like a real
way to fix that instead of just like trusting.
And I I also noticed like the the input like the
little composer it's stuck to the bottom of the
screen. So you're using no flicker mode. Yeah, I'm
using no flicker. Honestly, I think we should just

[00:23]
like make that the default because it's so much
better. Um like you can see I can scroll really
fast and like like you could scroll fast before
but like sometimes there would be a flicker and
now there's not. Um, have have
folks tried no flicker mode for CLA?
Yeah, a few people. So, it's like
we launched it on April Fools. So,
you can think it [laughter] in hindsight
it came across as a joke a little bit, but
if you actually do quad code, no flicker equals 1
quad. So, just like set that environment variable,
we totally rewrote the renderer that's running
in the CLI. So, it's using virtualized scrolling,
virtualized selection. And so what this means is
like constant memory usage, constant CPU usage,
and also some nice stuff like uh like if Jared
types, he can actually like click around the
composer. And so you can actually click and mouse
events work, which is pretty crazy for a terminal.
So I'm just also having it monitor
the PR. Um, and you can see it's uh

[00:24]
it ran some commands and then it's going to go
to sleep for 20 minutes and wake back up. Um,
20 minutes is probably a little
bit too long, but it's okay. Um
uh oops. And what's that? Is that like using
like a loop or something? I think so. Uh uh. Uh
yeah. And then it's let's see how else is
it doing. And then the other ones are still
uh apparently it fixed an extra bug as well. Uh
uh. Okay. So we got Okay, so it's been what? It's
been like 20 minutes or so. 25 minutes and we
got one. How many PRs have we gotten? Two. Uh,
three PRs. Three PRs. That's not bad.
Yeah. And I think we'll get a fourth one
once it finishes running the tests. And then
in the meantime, Robo is still running and
kind of like generating even even more PRs.
Yeah. Every time somebody submits an issue,

[00:25]
it it tries to reproduce it. Yeah. I I kind of
feel like every like the the way quad code makes
you think is every time there's a new bottleneck,
you have to kind of automate that bottleneck and
then there's always some other bottleneck after
and you kind of move on to that and like it
started like writing code was the bottleneck and
now it's no longer the bottleneck and then like
verification and running tests that was like the
bottleneck and it's no longer the bottleneck and
now there's like a deeper layer of verification
maybe that maybe that's it. What do what do
you think are the bottlenecks remaining? It's
definitely this deeper layer of verification. Um I
feel like the bottleneck after that is going to be
like planning like what should we do, what should
we not do and what is the right way to fix this.
Um and like ideally Claude would be smart enough
or like we could trust Claude enough to to merge
the PRs by itself. Um and I think like in a in
certain projects you could pro probably do that
um and just have that be automatic completely.

[00:26]
Um, I think Bun is not yet or like it's not
yet there for Claude or sorry for for Bun. Um,
but I think it'd be really cool if if like we had
the tooling uh for us to feel confident enough
to do that. So So like right now Robbo it doesn't
like build features. It it doesn't do like feature
requests yet. It it that's true. Yeah, it doesn't
do feature requests but it we do also use it
sometimes. We we so we can also uh uh appmentntion
it in either discord or slack and it will like
try to implement the feature. Um uh so sometimes
when people are like hey bun is missing this thing
um then I just at mention the bot and
maybe like an hour later there's a PR. Um
a bunch of times I've somebody's
like tweeted at me something like
this can you fix this bug or whatever
and that's basically what I do. Um,
and then I reply with a link to the PR. Um,
should we add a Robbo account on Twitter? Um uh

[00:27]
and I think like so like it can do feature
requests, but I'm I'm hesitant for it to
implement literally everything anybody asked for
in a GitHub issue cuz that's kind of a lot cuz in
some ways it's it's kind of crazy to put something
like an image processing library inside a bun,
but like we talk about engineering taste and
there's like an element of taste that goes
into that. you felt like that's a good idea and
like we're not sure yet if Quad is at the point
where you would also think this is a good idea
but you know at some point in the future it'll
get there maybe it's starting to get and I do
think that like PRs become suggestions like
having uh like not merging PRs used to be like you
feel bad if you don't merge like a co-orker's PR
uh because like they put work into that but you
don't have to feel bad when it's like claude
Um uh so like if the PR is wrong or or or or
for for or whatever reason then you can just
not merge it. And uh but it does mean that like
the like the the bar for uh what you merge is like

[00:28]
should should it be there because I think that's
also a difference with with when it's like people
because with people you want you don't want
people to feel bad about their like lost work.
Um, so sort of in some ways it does actually end
up raising the bar for what you decide to merge.
Yeah, it's interesting how like as the bottlenecks
move, the dynamics change a little bit.
It's sort of like having to trust each
other, having to trust people on the
team. This kind of changes a little bit.
Now it's a little bit more about like do
we have the right automation and like do we
trust automation like as as a group? Yeah.
So I think we're almost at time. Is there
any like maybe one last thing we want to
we want to show people where we can kind of check
in on kind of like the progress that we've made?
Um I don't think so. Uh uh yeah,
it's it's still going one last

[00:29]
onto that fourth PR and it's going back and
forth like found a bug and then fixed a bug. Uh
looks like it's about to submit the
PR now. Okay, let's wait for this one.
Love to have one more. This is like the cool thing
about auto mode. It's like in auto mode I can let
like cloud runs like for hours and hours at a
time. Like I run it almost every night. I'll
just have a bunch of quads running in auto mode.
And I was like before this it just didn't work
cuz it always got stuck at some kind of
permission request. And that was crazy.
Like this entire thing was one prompt and and that
just ran for 30 minutes. Yeah. This is all I said.
Okay. So, it's pushing at
it's about to submit the PR.
That sounds like the right fix, too. This has
been an issue that's been open for a long time.

[00:30]
Okay. And we got a PR
Yeah, we can go to this issue and
we can see how many up votes it has.
20. Yeah, it's kind of a lot.
Cool. Maybe we can pause there. Um, but to
me, this is just like such a cool vision
of where engineering is going, I think,
for everyone in this room. And, you know,
we're going to see this first. we're going to
have to figure it out first and then everyone
else is going to have to figure this out. So, you
know, like we were talking about this morning,
just excited to be on this journey together. And
like you can see, we haven't figured everything
out yet. Um, but I think like the mode that
we're in is just constantly experimenting,
constantly trying to to see what the
next bottleneck is so we can solve it.
It's very exciting. This is
so cool. Like this stuff.

[00:31]
[applause] Cool. All right. Should
I like Yeah, you can weave it.
Come on,
bro.

</details>


![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a02b62b0fd6f5b85ee0bea3_CwC.jpeg)

Daniela Amodei, Co-founder and President, and Dario Amodei, Co-founder and CEO, participate in a fireside chat moderated by Ami Vora, CPO.

## What we announced

Announced at the conference, we [doubled rate limits on Claude Code](https://www.anthropic.com/news/higher-limits-spacex) and raised API limits for Claude Opus so developers, startups, and enterprises can build more reliably at scale. Both changes are now live.

We also introduced new capabilities to [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) on the Claude Platform aimed at helping teams build and deploy cloud-hosted agents at scale. Four [new features](https://claude.com/blog/new-in-claude-managed-agents) are now available to all developers:

* **Dreaming.** A scheduled process that reviews past agent sessions, surfaces patterns, and curates memory, so agents improve between runs. Recurring mistakes, shared workflows, and team preferences get pulled into a more useful memory store.
* **Multiagent orchestration.** A lead agent can delegate to specialist subagents working in parallel on a shared filesystem, each with its own model, prompt, and tools. The whole flow is traceable in the Claude Console.
* **Outcomes.** Developers define a rubric for what a good output looks like. A separate grader evaluates each result in its own context window and sends the agent back to revise until it meets the bar. On our internal benchmarks, outcomes lifted task success by up to 10 points on the hardest problems.
* **Webhooks**: Once you’ve defined an outcome, you can let the agent run, and get notified by a webhook when it's done.

## In case you missed it

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a02b5708e141ac8abcd4968_Exec%20Boris%20Cherny.jpg)

Boris Cherny, creator of Claude Code, presents during Code w/ Claude 2026 in San Francisco.

If you missed the livestream, check out our keynote and breakout session recordings, [here](https://www.youtube.com/playlist?list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR).

Our talks go behind the scenes of building Claude with Anthropic teams and share how customers like [Asana](https://www.youtube.com/watch?v=BrpB-h1e--k&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=10), [Cursor](https://www.youtube.com/watch?v=BbYSGxtsMic&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=15), [GitHub](https://www.youtube.com/watch?v=y5TmF_6o6xk&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=7), [Replit](https://www.youtube.com/watch?v=snroDwX1-JU&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=14), and [Vercel](https://www.youtube.com/watch?v=bJKdXhnw7NU&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=3&pp=iAQB0gcJCQMLAYcqIYzv) about how they’re designing production-ready agents and pushing the boundaries of agentic development.

<!-- yt-inline:BrpB-h1e--k -->
[![Building with Claude Managed Agents and Asana AI teammates](https://img.youtube.com/vi/BrpB-h1e--k/hqdefault.jpg)](https://www.youtube.com/watch?v=BrpB-h1e--k)

<details>
<summary>📺 자막: Building with Claude Managed Agents and Asana AI teammates (24:57)</summary>

[00:00]
Hi everyone. I'm Arnauld from Asana and
I'm here to talk to you about how we've
built Asana's AI teammates on Claude
managed agents.
Our vision at Asana is to bring forward
this promise of the agentic enterprise
where human beings and AI agents can
work together to get complex multi-step
work done. Whether you're in IT or
operations or product or marketing, our
vision is the AI agent is an actor in
the system. It's got a deep set of
skills. It's got all of the context
required and it can work hand-in-hand
with other human beings to get
multi-step work done. Things like
approvals, complete end-to-end
workflows, getting to real-world
outcomes.

[00:01]
So, that's what we've been building and
AI teammates within Asana are generally
available as of March.
What we see today though in the
enterprise is
almost everybody is experimenting with
AI agents. They're building AI agents.
There's a lot of like utilization of
them. But, most most companies are still
using AI agents in the single player way
where an individual can go ahead and
interact with the agent, get an outcome,
and then they pass it on to someone else
to complete those multi-step processes.
You don't end up with compounding
knowledge. You don't end up with this
concept of a a shared enterprise memory.
Uh you don't end up with concepts like
uh true multiplayer multiple
human-in-the-loop interactions.
And uh throughout this presentation I'll
showcase like what have we done that's
sort of set this up and how does
Claude's managed agents capability help
us complete these complex multi-step uh
multi-step workflows. So, our vision is
like full multiplayer mode. You have
agents that are real actors in the
system. They've got sharing and our back

[00:02]
controls just like you would be
onboarding a new teammate, a new human
teammate into the system. They have the
contacts. Uh they can work with multiple
people. They can get nudges and
interactions with multiple people and
they can complete uh complete these
end-to-end jobs to be done. In fact,
like one funny anecdote is I was just
chatting with Hannah before I got on
stage and there are a bunch of like
former Asanas who are now at Anthropic
and one of them had built an AI uh
teammate for us uh that's a competitive
intelligence researcher. And so now,
even though they're no longer at Asana,
uh we still use it on a day-to-day basis
and all of the historical interactions
that he had to set up the context and
the knowledge when, you know, we were
doing competitive responses to RFPs, is
ingrained in that agent and it's just
getting better and better as more people
join the team and keep using it. So,
that con- that concept of uh enterprise
memory
uh and then the shared ability of the
the ability for multiple people to use

[00:03]
agents has been phenomenal for us
internally in our use.
The The other concept that we've been
working on and, you know, again, is
available is this ability to ensure that
the agent gets
complete context about how your
enterprise works. Who does what by when
and why, historical decisions,
approvals, ways in which people have had
back and forth on a particular campaign
brief or a project plan that have
finally led to its approval, those
decisions are tracked inside Asana and
we provide those to the teammate in a
way, again, that preserves security,
guardrails, auditability, so you can get
real-world results and action.
So, Asana is the system of action for
work and it's that so binding layer
where, once you start introducing
agents, you can treat them like human
beings in your team. You know, like we
have a work graph that we've been
building for over 17 years. And it's

[00:04]
this idea that every company has a
mission and vision that is tracked by
goals. Goals are in portfolios.
Portfolios are delivered by a multitude
of projects. Each project has a set of
tasks. And those tasks could have
approvals, workflows, and other things
embedded in them. And as you build out
this context graph that is uh designed
for both human beings and AI agents,
human beings have a easy to comprehend
way, a UI, to interact with like how
your work gets done. And then agents
have a way to represent themselves and
get that uh get that context they need
to get work done and perform in a true
multiplayer way across multiple human
beings following the right security and
guardrails required by your enterprise.
So, we've been building all of this out
for context, shared memory, and ensuring
agents are real actors in the system.
The place where we leverage Claude's
managed agents capability is to complete
those multi-step actions in a way where
where Anthropic's tooling is allowing us

[00:05]
to go complete the task. So, in the demo
that I'll showcase, what you'll see is a
multi-step interaction between a
marketer who's releasing uh a new
campaign as well as multiple people on
their team. And that campaign requires
them to not only write a brief, but also
start producing a few mock-ups for what
that landing page is going to look like
so that the human beings on the team can
get to a shared understanding of whether
that's good to go or not.
So, it involves creating, you know, a
complex document using the right set of
enterprise context uh required to
produce it, as well as creating multiple
iterations of what that landing page,
the public website, should look like.
So, it's like generating HTML. It's a
multi- It's a multi-step action.
So, with the managed agents capability,
there's a few different things that that
uh we use to make AI teammates far more
powerful. So, it helped us reduce our
prototyping costs. Like, we got much
faster prototyping for these actions and
skills.

[00:06]
It comes built in with a verification
loop, so we know that the quality of the
content we'll get at at the end of the
process is high. And then it has this
built-in grader, where once Asana passes
in the outcome it wants to Claude
managed agents, you know, we know that
the grader will go ahead and iterate
through that outcome multiple times to
ensure that we're getting a high-quality
output. So, again, this is allowing us
to focus on the things that is unique to
Asana, the human interface layer to go
ahead and coordinate across multiple
people, the system of context that we're
building out, the security that we're
building out, so that if you're using
the same agent as me or Nigel or Tony,
and we are, you know, we're in different
work graph objects or different
projects, the agent won't leak
information across the other. So, we
focused on that, and the quality of the
output is something we're leveraging
Claude managed agents for.
So, again, like if I compare and
contrast the way in which uh
AI teammates is working today with
Claude managed agents versus the

[00:07]
messages API that we're previously
using,
uh we're getting, again, faster
prototyping because we're not having to
build a manual agent loop, file
management, code execution.
Uh the verification process has gotten
way better with this uh with this sort
of built-in product. And then we can
also enable multiple agents in parallel
to work independently, because a lot of
these like knowledge worker actions like
require multiple agents to work in
parallel to produce a full plan and to
iterate through it.
So, uh again, like as of today, there
are over 21 pre-built agents uh called
AI teammates within Asana. Uh we
designed the pre-built ones to match our
ideal customer profiles across the uh
office of the PMO within marketing,
within IT, within HR, within R&D, and
they can do things like they can help
you with launch planning, they can help
you with
writing specs, they can help you with
goal management, they can help you with
resource management and capacity

[00:08]
planning. And so they're using all of
these existing constructs within Asana
for tracking portfolio goals, for
tracking timeline updates, and they're
taking real action within them as well
as in downstream systems. So they can
pull in data from Google Drive and
Office 365, and we're adding a whole
bunch more integrations over the coming
weeks, and they can take action within
them as well. They can produce slides,
they can add comments, they can create
full HTML, and a lot of those like
capabilities are possible because we've
invested in managed agents, and it sort
of allowed us to run that verification
loop and and multi-step multi-step
workflow.
Um
So like another example I'll give you is
we've been obviously dogfooding this
internally at Asana for months now, and
over over those months I have an agent
for the product management team, which
is me and my directs, and it's like a
it's the product or thought buddy, and
it's got all of the context around you
know why we made certain trade-off
decisions, what the strategy is, and

[00:09]
things like that. And so when our
marketing team for example has questions
about hey, we are planning Work
Innovation Summit London, which is our
next event that's coming up. Here is a
draft of the keynote speech. Could we
get the product team's input on it? The
first thing they do is actually they
create a task in Asana and they assign
that to the product or thought buddy,
and it has all of the trade-offs, the
current roadmap, all the
context for how our roadmap works within
Asana, and it produces a plan, and it
produces
a set of feedback on that on that
keynote speech that is like highly
optimized for the way in which we work
and is
is correct and is accurate from the
perspective of it's using all of the
real-time context.
And again, it's done in a multiplayer
way. So, everybody in the product team
can see that response and they can react
to it. They can give it nudges and it'll
remember that across multiple runs.
So, that's a lot of talking about like
what we've done with pre-built agents,

[00:10]
the multi-step workflows, and outcomes
that are possible with Claude managed
agents,
enterprise memory, shared memory. We
should see it in action to like really
get you a sense for what we're talking
about.
So, let's let's roll the video and I'll
talk you through it. So, in this video,
the the human the human being is is a
marketer and they're trying to launch a
new campaign and they're going to use AI
teammates that are leveraging Claude's
managed agents under the covers. And the
way they'll kick it off is you'll see
them in a Kanban board inside Asana and
they'll just create a new task saying,
"Hey, I'm going to go ahead and and plan
for a new campaign brief." So, let's
roll the video and see that in action.
Yep. So, this is a person.
They're like, "Okay, I've got this like
task to go ahead and create a campaign
brief and prototype a landing page."
Like, it's not only a document, but it's
also a product for a landing page. And
perhaps they haven't used AI teammates
before. They go to the teammate gallery.
They choose one of the pre-built
teammates that have all of their

[00:11]
behavior guidance and description in it.
And when they go in over here and they
customize it for their use, it will
automatically pick up the right work
graph objects, like the previous
campaign projects or portfolios
to add to that teammate's memory so that
it can it can go ahead and produce
better content. So, it's the teammate
has gone ahead and and sort of first
planned out its response
and it's created a
a document which is its campaign brief.
And you'll notice it's also created
an HTML file, which is the landing page
mock-up for this new campaign.
And again, because if you track all of
your processes in Asana, it'll
automatically pick up that context. This
is showcasing what you would see in the
cloud console, right? So, in the console
we pass in the outcome as to the manage
agents product. And then
what we can see is
the runs in within the console to to
highlight that manage agents is is

[00:12]
actually running the greater to to
ensure that the verification loop is
complete and the outcome is is as
appropriate. So, again, like the
combination has an allowed our
development team to ensure that we're
getting high quality outcomes. That's
delivering on the customer promise that
we have, which is you're getting all the
security benefits of our back controls
and app actors, like agents is a true
actor within the system. You're getting
the enterprise context, and then manage
agents is delivering on the outcome. So,
they've gone from just an idea or a
task, which would have taken them a
bunch of time to create the brief, maybe
send it over to creative, and get a
mock-up in place for what that landing
page should look like, down to a land to
to a a page immediately.
Um and then interacting with the agent
and asking to iterate on it is as simple
as talking to it via comments, right?
So, let's say
it picked up green as the primary color,
but the primary color has now changed

[00:13]
based on the summer
whatever team. You can say this is
great, but let's make the primary color
blue,
and you can give it some feedback that
this is our new company sort of primary
color. This will actually get ingrained
into the agent's memory, so if a
different marketer picks up and uses
that agent, it will not make that same
mistake again. It will remember that the
new color scheme is blue.
Uh and so you can see that the campaign
brief writer is working on behalf of
Sushi admin.
Um,
and you'll notice that the memory is
getting created. That's the reason why
we're sort of expanding that. It's not
something that an end user has to go
care about, but we highlight that the
memory is getting created. And boom,
you've got like a blue uh, campaign
brief landing page.
Now, I want to showcase multiplayer in
action. So, uh, this is great. So, maybe
the marketer feels like this is a a good
starting point. They've got a brief.
They've got a mock-up of the page. Now,
they want to bring in uh, somebody else
on their team who can review it and give
them feedback. And you'll notice the

[00:14]
teammate is going to work in multiplayer
mode. So, this new person comes in um,
and they're like, "Okay, uh, teammate,
uh, thank you for doing this, but I
would pref- I would love to see a- an
iteration of it that is more
minimalistic in its uh, in its look and
feel." So, again, just just type it out
as if it's a it's a comment, and it is a
real comment. You can hit go, and then
again, like the cloud manager agent's
functionality will run in the background
and create that minimalistic view.
The other things to call out is because
this is a shared workspace, everything
that's happened, the interactions
between the human beings and the AI
agent is also tracked in the task, and
it's fully auditable. So, at some point
in time, if you need to like bubble this
up to your manager or your lead and get
their approval, you can simply convert
it to an approval. They'll see all the
prompts that have gone in. They'll see
the back and forth between the AI agent
and the multiple humans, and it gives
them that much more confidence that
confidence that the right questions have
been answered, and they're getting the

[00:15]
the best possible outcome without a
bunch of back and forth, right? Like,
"Did you consider a minimalist version?
Did you consider that the the decision
was made to go ahead and move to the
blue color, etc."
Um,
and again, I'm not showing it here in
the demo, but if you go into the the
teammate's detail page, uh, there is
also a concept of uh, who owns or
manages that AI agent. So, these are
back controls and calling out mean that
there's a definition of the human beings
who are the agent sponsors and who can
manage it. And so, those human beings
get a chance to delete memories or
change the parts of the Asana context
graph that the agent has access to to
ensure that it continues to behave
consistently going forward.
Okay.
So, again, like what you're seeing here
is what we have generally available
today. It's using uh it's using these
sort of multi-step actions. It's
documenting everything. It's working in
a multiplayer way. The future for us is
thinking about more capable, more more

[00:16]
multi-step workflows, right? Like uh
what what about entire launch planning
processes? What about resource
management and capacity planning across
hundreds of people? How do you make that
better? How do you how do you generate
dynamic dashboards? How do you generate
risk reports? How do you automatically
alert uh end users on what remediation
steps they could take to go fix issues
and things like that. Uh we're
partnering with Anthropic on learning
faster from team patterns and agent
skills. And we're also identifying
opportunities to move work forward more
proactively. So, proactivity is
something we're working on where if an
agent is uh or an Asana AI teammate is
part of a project or is like looking at
your Kanban board, even if you haven't
assigned it any task, it can
automatically wake up and be like, "Hey,
I can pick that up." or "I've seen uh
this particular issue in a different
project before and this is how you go
ahead and resolve it.
So, what this has allowed us to do as a
company is, you know, we've been able to
focus on all of the aspects that make

[00:17]
Asana great, like the fact that you can
define in a human-readable way what your
multi-step processes as a marketing team
or the office of the PMO or in IT.
And you can interact with these agents
in a way that is very human. It feels
like you're onboarding a new person onto
the team. You're giving them the context
with these projects or documents. You're
giving them feedback. And multiple
people can use them. So,
even in my example of like this person
who's like no longer at Asana, all of
the work that they've done and those
memories are reusable by people on the
team to keep doing that work faster and
doing that work better going forward.
Okay. So, that was
a primer on how we're using managed
agents to deliver Asana AI teammates.
We have about five-ish minutes left, so
I can open it up and take some questions
if there's any in the audience.
Yeah.
Thank you.

[00:18]
Cool, there's a person in the back.
>> Great talk again.
Um, just quick question for you. You
mentioned earlier that the validation of
the like the agent itself happens on the
Anthropic side of things. Just curious
what that looks like and what you folks
would encode in there. Like you
mentioned that Asana has a bunch of
domain knowledge. Does that go into the
verification? Sorry, I didn't realize I
was talking outside of it. Does that go
into the verification process also?
>> So, I I only heard parts of the question
about how do we run the verification
process. Do you Do you mind just
>> Yeah, I can rephrase the whole thing.
So, you mentioned the verification
process happens on the Anthropic side of
things where with they're looking at the
outputs of the managed agents and seeing
if it's in alignment with what like the
spec is for the output. Is there Asana
domain knowledge being injected there as
well? How do you folks go about managing
the contract between the managed agents
and what you folks want it to actually
providing you?
>> Yeah, it's a good question. I think at a

[00:19]
high level what we're doing is we are
passing in the Asana context as part of
the outcome definition.
Uh, as well as um, yeah, yeah, that's
the place we're doing that. And then as
we've been testing it out internally
before we release like a pre-built uh,
capability to our customers, that the
there's like there's like another level
of QA that happens obviously within
Asana like with by our engineering team.
And then in the the the real world use
case and utilization of this is again
because we are a very like human in the
loop system, if there's any issues with
the quality of the output for a
particular customer because perhaps
their context stuff isn't as fully
fleshed out or isn't as detailed, the
more you use it and the more nudges you
give it across multiple people, all of
that compounds and just keeps getting
better. So because we record that back
within Asana and we put it put push it
back as part of the call to run the
managed agent every single time.
>> Yeah, makes sense. Thanks again, great
talk.
>> Yeah. Yeah.

[00:20]
>> Hey, thanks for your talk. Uh
really insightful. Uh could you speak a
bit more about how you designed the
rubric uh on like your like the rubric
that your grader sees to iterate uh on
the uh outputs that it generates?
Were there any learnings there?
>> Were there any learnings about on the
rubric that the grader sees?
Um
I'm curious like do you have a do you
have thought Bradley on our engineering
team? Hi Bradley.
>> [laughter]
>> Um do you have any thoughts on that
Bradley that I mean I don't know if you
learned anything unique as part of that.
>> Sorry, could you repeat the question
again?
>> Uh the question was
um
the question was if I understood it
correctly like uh
the the grader exact how do are there
any unique ways in which you've been
using that? Is that correct?
>> Yeah, how was your experience writing a
a rubric for the outcomes grader uh and
having it iterate on problems?

[00:21]
>> I I think we want to approach it like we
approach any other prompt. So it I think
in the end uh all the text that you
provide to the model is a different form
of prompt and you want to have different
evaluations for the outcomes for
different things that we're trying to
achieve. So, if you're able to
instrument that just like anything else,
you're able to iterate quickly and make
confident decisions.
>> Great.
Any more questions?
Right.
There's one over here.
>> Thank you.
Um thanks for the talk today. I was
curious how you're thinking of skill
maintenance over time.
>> Uh how are we thinking about scaling
teams or
>> Skill maintenance. So, skill maintenance
for mock-down files.
>> Yeah, so uh again like we're a product
for like knowledge workers. We want to
make it as simple and straightforward
for our customers to deploy and use this

[00:22]
as possible. And so, the way in which
I'm thinking about it from a product
strategy perspective is Asana will
decide what skills get baked into the
uh the finished like generally available
product and we're adding more
and we're designing those based off like
working backwards from our ideal
customer profiles and the the advances
we're seeing in the in the underlying
sort of model provider.
Um and that allows us to be very like
prescriptive about okay, here are the
additional capabilities that will be
available in a GA way, like a generally
available way, that to the end user,
like if you're in IT or operations,
you're thinking about the job to be done
for the teammate. Like I'm trying to go
ahead and produce perhaps like a Figma
design output or something of that sort.
And so, it'll be marketed and messaged
in that way and it's a shrink-wrapped
product. So,
again like over time we might open it up
so that customers can design their own
skills and like highly customize their
AI teammates, but the the
sort of primary go-to-market motion and

[00:23]
the primary sort of use cases, we
pre-design these AI teammates and the
value from a skills perspective. So,
they're like shrink-wrapped.
And then that way we get we get to
control on the R&D side the quality
level, which ones get released,
how that what the life cycle is, and so
on and so forth.
>> Thank you.
>> Yeah.
Great.
We have one more, okay. So, maybe this
is the last one because I see the
counter clock is showing about a minute.
>> So,
I'm also also building my my product
with the CMA as well. And one of the
problem I'm facing is
integrating with the third-party tools.
Like customer always want to integrate
to some other things beside beyond our
platform. How do you manage that? Like
you integrate that with the Asana level
or at the agent level or how do you
manage the third-party integration?

[00:24]
>> Third-party integrations for the grader.
Um Bradley, what's what's been our
experience so far? Like we've we've got
a few of those built out, so I'm kind of
curious, yeah.
>> Yeah, in terms of third-party
integrations and managed agents, we
integrate them at actually both levels.
So, we integrate them directly with our
own AI teammates agent loop, and we also
integrate them at the MCP level with
managed agents. So, we want to make sure
that the managed agents when we're using
them have the you know, all of the
context that they need
and that we're also supplying context
when we're not using managed agents.
>> Awesome. Well, thanks everybody for
joining us. We're at the end of our time
today. And yeah, if you have a chance,
give AI teammates a try.
Thank you.

</details>


<!-- yt-inline:BbYSGxtsMic -->
[![Giving coding agents their own computers: How Cursor built cloud agents](https://img.youtube.com/vi/BbYSGxtsMic/hqdefault.jpg)](https://www.youtube.com/watch?v=BbYSGxtsMic)

<details>
<summary>📺 자막: Giving coding agents their own computers: How Cursor built cloud agents (14:35)</summary>

[00:00]
Hello.
Um, okay. So,
uh
models are getting really good.
And for more and more work, the
bottleneck is no longer the model
intelligence.
The bottleneck is humans giving the
models the tools and the contacts and
the increasingly ambitious uh tasks and
objectives to go flex their potential.
So, um at Cursor, we've been working on
removing that bottleneck and I'm going
to share a bit about how we've been
doing that um and hopefully it's helpful
to some of you in in your work.
Uh with models this good, we kind of see
the job that we have as setting our
agents free um safely uh uh and and
having them go off and work on bigger
bigger tasks. So, we've kind of gone
through three stages of uh the process.
The first was um giving our agents the

[00:01]
tools and the context to be more
autonomous. The second is um we had to
learn how to take advantage of these
more capable models. There's actually a
lot of work in figuring out how to
update your your sort of patterns uh and
behaviors.
And as you do that, as you're leveraging
more more agents and uh getting more
work done, you start to see the places
where uh there's stress and strains and
where the agents fall over and you work
to to uh improve that and that brings
you to the third stage which is building
the system that builds the system. So,
instead of spending your day uh
hand-holding agents from task A to D,
you take that time to uh build the
system that can solve for A to Z.
So, we started thinking about how to
make our agents more capable, how to
make them work more like we do.
Uh we started with
uh looking at what we do with humans to
onboard people to to uh Cursor. So, when
a developer joins Cursor,
they get a computer.
They are uh we help them set up their

[00:02]
dev environment. We have a ton of
documentation, maybe too much, about how
to do all the different things that uh
developers need to do in their daily
work. Um so, we give them all this all
this context and all this material. And
and uh crucially their computer.
If you imagine if we thought
think about what the the we were doing
with the the models, we were kind of
just like throwing the onboarding
process was you throw them into a code
base and from the model's perspective,
you have that thousands of lines of code
whizzing by, you don't know like what
you're doing, you just have some task
you have to go solve, uh and it's kind
of incredible that this works as well as
it does. Um I know if like I had to work
this way and I was just site reading
code and I couldn't test the
application, um I would also probably
frustrate and annoy uh the humans who
did have to do the testing for me.
So, um
we decided to build an onboarding agent.
And we built a a Claude onboarding
agent. Anybody can go to um
uh cursor.com/onboard.
You can put set up your repo and the

[00:03]
Claude onboarding agent gets to work and
it starts exploring your code base not
to make a change but to figure out how
to run it.
And this is a little bit about how it
goes. So, it's exploring, it's looking
around,
um and depending on how fast this one's
playing, you'll see it can start uh
using the app and it'll come back with a
demo. And it's not just looking to
figure out like what to run, what the
services are, um but there are sort of
these complex things it needs to do like
figure out their different environment
variables, what permissions does it
need. Um so, it's this interactive
process with with the uh developer to
make sure the services are are running
properly.
So, once we have the agents onboarded,
we realize there's still quite a bit of
work to do because you have all these
developers uh running many Claude agents
every day. So, any problems are
multiplied out across all those those
runs. And so, every time the agents run,
they have to start their dev environment
from scratch. When you're doing local
dev, you probably leave things running.
Um not true for the cloud cloud agents.
So, we wanted to optimize their dev X.
They were spending a lot of time

[00:04]
sleeping, uh waiting for things to start
up. They didn't uh have good ways of
waiting for things, so we built an an
any dev CLI tool. Um so, they were able
to start services, wait for the services
to start, check on statuses. They had
sort of a Swiss Army knife for things
like uh creating test accounts and
signing in for services, third-party
services, things like that. So, what we
saw was uh as we made the dev
environments better, more developers
started running more cloud agents and
getting more out of it. So, there's sort
of a positive feedback loop that starts
to take place.
Um and then of course, we also had to
give them uh all the sort of
documentation that we give our our human
developers. So, we made sort of
simplified versions of this so they
could get uh when they find themselves
in sort of these edge cases or hard
problems, they have the materials there
to to lean on.
So, uh in doing this process, we sort of
derived these kind of basic principles
of autonomy. Um the first is you have to
give your agents eyes. So, everything
that you can see, the agents need to be
able to see, too.
Uh basic version of this is if, you

[00:05]
know, the agent's running an app, you
should be able to see that app. If you
go and make changes and you use that app
yourself and change something in the
state, the agent needs to be able to see
what you changed. Another sort of
interesting one is uh that we found is
the the agent chats where you wind up
needing to debug what happened in a
chat, and you want the agent to be able
to see the same uh the other agent's
chat uh just like you do.
Uh the next thing is giving the agents
uh tools so that they can do all the
things that you can do with sort of
reasonable security constraints. Um this
is like, you know, basic basic one,
really important one is they should be
able to run the applications that you
can run, and they should be able to use
the services that you should you can
run.
Um
agents are auto regressive, so it is
also very important that you have a sort
of high-quality codebase and and
instructions and everything else so that
uh you get high quality and high quality
out.
The foundational primitive we believe
for human autonomy is computer use.
Um
So the first domain where agents have
really excelled has been coding and we

[00:06]
think computer use is is the next really
important domain.
Um and this is raw pixels in, mouse and
keyboard out.
Um and the Claude family of models are
really good at this. And this is this is
not the hard part of this is not
clicking in the right place. The hard
part is uh
sort of better explained is like if
coding is like chess where you can see
all the pieces out on the board,
navigating these GUIs is more like a
video game where you can only see a
little slice at a time. There are
one-way doors. There are game over
states that you can get into.
Um and so you need this sort of
higher-level metacognition and
backtracking and the sort of general
general intelligence uh uh
skills that the Claude family's really
good at. So uh
uh Claude's Claude 47 is our computer
use model. Here's an example. It was
told to go off and build this private
marketplace feature.
Um
So it goes off and records this demo
where it's implemented all the little
pieces. We have like
uh this
URL input and there's CSVs it needs to
add. Um

[00:07]
And what's great is that it's not just
using that to do its own end-to-end
testing to make sure that the changes
that it made works. You as the developer
get to uh have a really high bandwidth
method of reviewing the work of the
agent before you get into code. And this
becomes really really valuable when you
are running many of these agents um
simultaneously in the cloud and bouncing
between them. So that's the next thing
is once you have these autonomous agents
onboarded, you need to learn
to give them more work and give them
bigger bigger challenges to go tackle.
Um two sort of basic modes. The first is
uh you have like a lot of tasks and a
lot of bugs and issues and you kind of
have to learn when to just uh
like stop putting those in your notes or
start stop putting them in your two
tracker and just kick off prompts. Put
them right into a prompt box and kick
them off. And when you do
uh you then have a bunch more of these
agents running and again it's great to
be able to have those demos that come
back instead of having to review lots
and lots of code.
Um and the sort of second pattern is
much bigger projects um where you can
give a cloud agent autonomous agent much

[00:08]
larger units of work and have it work
for much longer.
Um one of the things we were surprised
by we kind of knew that if we made the
agents more powerful developers would do
more exciting things. Um and we were
sort of surprised by the extent to which
this was true. And um one of the sort of
really important things was the security
that the cloud provided for for
developers. Um there's sort of this idea
of like security through freedom which
sounds like Orwellian propaganda but uh
in the same way that you're sort of
setting your agents free to go take
things on in the cloud um on their own
you also sort of set yourself free as a
developer where you don't have to worry
as much about uh you know resource
management and context switching. Um you
don't have to worry about the agents
going and doing things that they really
should not with your environment
variables.
Um
and there's there's a way in which we
were all surprised by how much more
enjoyable this made programming.
Um

[00:09]
really really important skill that we we
are still working on learning
um when the agents fail
is really worth it to take time out to
figure out what went wrong, debug it
and implement a fix that's again going
to be sort of multiplied out across your
whole team and your company. Um it's the
same sort of dynamic where so failure
modes if they persist make the agents
sort of continually uh
uh compounding failure across the entire
company. Um and people don't want to use
the the agents as much and they don't
lean on them as much. But the inverse is
also true when you invest in them
uh and you you make them work better
everybody wants to use them more. People
are building trust with the agents.
They're finding that they can sort of
one-shot bigger and bigger tasks, and
then they want to invest more in it. So,
this is a really important change in how
you think about your work, where you're
kind of programming programming the
system.
And so, you've onboarded your agents. We
gave them the tools to make them really
powerful.
Uh we started learning how to leverage
them and scale them up, and we were

[00:10]
seeing where they they fell over. We
started working on this sort of loop of
how you teach them to work better.
And we realized that it does start to
feel like coding again.
Um so, of course, we thought, well, the
agents should do this.
Um we've got a few ways that we're
trying to have the agents do this. This
is uh sort of the most important one and
the one I'm going to talk about today
um is agents iteratively improving their
own workflows.
And so, we call this the agent
experience. There's the developer
experience. So, you have the agent
experience, and you need to care just as
much if not more about the agent
experience.
Um the way that our system works is
agents uh go about their business, and
they are told to report issues as they
come up. Um it's really just like what
we do with uh the pattern I was
describing for humans, where if you see
something wrong, say something, uh
report it, and and try to work on a fix.
All those reports are accumulated in a
system of record. It's really again very
uh
similar to how human human systems work.
Um managers will go in and review all
the issues and categorize them and

[00:11]
dedupe them um and bucket them into
their issues that can be sort of their
technical problems that can be
addressed. Then there are issues of um
permission, where the agents just don't
have access to something. Uh so, they
need to get permission. There are issues
of ignorance, where the agents need uh
they don't still know what to do, and
they need the humans to come in and tell
them what the right right right way to
solve the problem is.
Um so, then in the last step, of course,
these are then fixed by both agents and
humans, and the goal is to over time
have a less and less human involvement,
so we can have those issues that the
agent solve are solved end-to-end. We
don't really need to review. We can have
really high trust in their work.
Um and they have all the context that
they need, and they don't need uh
anything else from us.
So, I'm going to go through a couple
examples. So, this is our most important
skill. It's the WCF skill,
which of course stands for work on the
factory.
And you can see it's like uh
every every cloud agent gets this skill.
Um
and it's almost the exact same prompt
that I was just showing in the previous
slide. Work on the factory is the idea

[00:12]
that when something is annoying, broken,
or confusing, you take a moment to
report it, so we can improve the tools
and workflows rather than just grinding
through.
Um
models a while ago would not have been
doing a very good job of this, but today
uh
they get annoyed, and they find things
broken, and they get confused, and they
like realize that, and they report it.
Um so, we get this this uh system of
record where they go and report all
these issues.
Um of course, you then have to solve the
issues, and this is its own uh really
important challenge if you want this
whole system to be sort of uh
self-improving.
And so, we were finding with these these
agent development experience problems,
having the agent just go solve them and
and try to one-shot was not that
effective because there's a lot of flake
in those problems.
So, something only happens once in a
while.
And so, we taught it to actually have
the cloud agent that goes and solves it
kick off a bunch more cloud agents with
the change in the development
experience, and make sure that across
that sort of eval set that there's a
robust solution. And so, then when the
problem when the solution and uh the PR

[00:13]
comes back to the human's review,
there's a high degree of trust that
actually this uh is is well validated
well validated well validated solution.
Um
This is slightly premature.
Um
Yeah, so I think that these are both
really good examples of where there's
how these sort of skills can work as um
uh sort of background uh a garbage
collection processes or cleanup
processes in the operating system. Uh
And we think that these while these are
sort of clearly applied for the the
coding domain,
in the same way we sort of speed run a
lot of AI development in coding, these
patterns are going to generalize
well outside of coding and to other
domains. And even if you think about it
already, cloud development experience is
not really a coding problem. There are a
lot of variables in that and very few of
them really are are just sort of coding
issues.
Okay, so now now the thank you slide.
If you'd like to talk more about
self-improving identity systems,
please talk to me. You can find me on X

[00:14]
at my name.
And if you'd like to set your agents
free, you can go to cursor.com/onboard
and have Claude onboard to your codebase
and maybe ship your next ambitious
feature.
So, thank you very much.

</details>


<!-- yt-inline:snroDwX1-JU -->
[![Evaluating and improving Replit Agent at scale](https://img.youtube.com/vi/snroDwX1-JU/hqdefault.jpg)](https://www.youtube.com/watch?v=snroDwX1-JU)

<details>
<summary>📺 자막: Evaluating and improving Replit Agent at scale (27:42)</summary>

[00:00]
All right. Hi everyone. I'm Mikael Cata
president and head of AI at Replit. And
today I'm going to be talking about our
both evaluating and improving on a daily
basis Replit agent at scale.
And as you know, Replit is a back-coding
platform for knowledge workers. We're
one of the top players in the space and
we've been literally battling with this
problem for the last you know almost 2
years.
The key difference between I would say
back-coding has a very broad definition.
It ranges all the way from being used by
software developers. But in our specific
case is even more of an extreme
definition where you start from just a
natural language specification of what

[00:01]
the user wants and literally nothing
else. So the user expects to go from a
prompt to a working application, but
they don't tell us what kind of
framework they want to use. They don't
write tests. They just expect things to
work after you know our the agent run.
So it means that a lot of the
evaluations and a lot of the ways in
which we've been building agents in the
past especially for software developers
has to fundamentally change.
Now,
how do we track internally the fact that
the agent gets better on a daily basis
and is actually aligned with all with
what our users want?
This is especially challenging because
if you think about it, models are
changing almost constantly and if
anything the pace of evolution is even
faster than it was a year ago. So we are
always sit on shifting grounds. Models
change fast. We have to change our
prompts, system prompts, user prompts
very often, you know, to comply to the
new features that we're building in
product. Of course, the tools

[00:02]
definitions are changing as well. We're
adding more of them, we're simplifying,
and we're shipping constantly. Every
single day we have multiple releases of
wrap agent, which we put in front of,
you know, millions of users.
So, my argument today for this talk will
be that we have to fundamentally rethink
how we do evaluations.
On the left side, you can see how evals
look like for basically, you know, since
since we've been working on AI. Um they
you run your evaluation, you they
produce a single score, and that score
is produced by a human. And what the
human decides based on the score is, my
agent harnesses better than it was
before or it regress, or my model is
better than before, or we should be
doing, you know, more post training.
That's how how we've been doing this,
you know, for a for a long time.
I argue that we should move more and
more towards a continuous setting of
evaluations, where especially when you
actually have something runs in
production, and in our case it generates
millions of traces every day, there is a

[00:03]
lot of hot fat to be extracted from the
traces themselves.
So, what we do is we have a combination
of fine evals, so very similar to sweet
bench and other benchmarks that are very
famous in the space, as well as online
evaluations based on the on the system
usage.
What do we want our evals to capture?
Fundamentally, first of all, they need
to optimize what our users care about,
you know, rather than just telling us if
the agent is editing code correctly.
They should also highlight immediately
what is breaking, and they should inform
us where what we should be shipping next
in terms of improvement for our agent.
What goes into this
box, this black box? So, we're building
a new system that allows us to do these
constant improvements.
The system looks in the following way.
We have two pillars. On one end, we have
the standard old-school benchmarks. They
are usually employed before shipping a
new version of the agent. Think of them

[00:04]
sort of as a boolean flag. It's a
gatekeeper before deciding if you should
be launching a new version or not. So,
if there is a major regression on an
offline benchmark, of course you stop
your release. If you see no changes or
positive changes, you know that you can
go on.
But the part that is more intriguing and
is what is helping us to make constant
progress is the fact that we do a lot of
baby testing and we also cluster all the
traces that we obtain in production and
we try to gain insights from them. So,
in this case,
the online pillar actually works after
you ship a version of the agent and it
forces you to react as fast as possible.
And the loop here is, once I have these
two pillars in place, you reflect on the
results that both of them are giving
you, you likely change the code once
again, run your eval, rinse and repeat.
And this is the cycle that we go we are
going through every single day at
Replit.
I mentioned before SweetBench and I want
to give you a quick understanding why

[00:05]
we work on something, you know, more
powerful than SweetBench or at least
like more tailored towards our use case.
Um something as SweetBench, HumanEval,
they played a key role in our space, you
know, to allow us to air climb them and
make models more powerful. But
eventually, they all follow the same
protocol.
Uh you make sure that the code that is
generated complies with the user prompt,
then you apply the patch on your
repository, you run the test. If the
tests are passing, you know, you you
have a higher score on the benchmark.
This does not reflect what happens in by
coding. As I was mentioning before,
users are not writing the tests. They
often start from a completely empty code
base. So, there is not a scenario where
you can just apply patches. You're
building things from the ground up.
So, what we need to capture in instead
is does the app do what the user asked?
So, there is a functional correctness
gap between what SweetBench provides and
what we were working on.
And today on stage, I'm launching
ByBench. It's a new public benchmark for

[00:06]
back-coding end-to-end that we worked on
at Raptic for several months. I'm going
to give you all the details after the
URL and so forth, but let's start from
the setup of the benchmark. The input is
just a PRD. It's literally like a long
prompt that describes how to build an
application.
Rather than crafting them from synthetic
data, we pick 20 real-world traces from,
you know, usage of Raptic, just plain
English specifications
without any implementation constraints.
Then, we have an harness that builds the
application end-to-end. So, it goes from
an empty repo into something functional.
And then, the key insight is rather than
stopping the benchmark here and then
having humans evaluating the output of
those PRDs, we built automated
evaluators. This is what allows you to
go from a benchmark that you run maybe
on a weekly basis into something that
you can run every single time you
literally have a new PR merge in your
repository. So, of course, as you can

[00:07]
imagine, we have AI running all the
evaluations on our behalf.
The
the setup is the following. There is one
core, and the protocol is you have an
you have a input, you have an
implementation strategy, and then you
have a set of our core, sorry, our wired
evaluations that you run on your app.
And we came up, you know, with five
different pairings, but in reality,
there are a lot more pairings that you
could come up with yourself. The most
basic pairing is the input is the PRD,
and we build the application single shot
zero to one.
Then, maybe in order, you know, to go
from uh less complicated to more
advanced, we have something called by
bond ref or like the reference
implementation where we start from
something is already working and we
build a feature on top of that.
Let's make it more advanced. We have by
bond vibe where we start from an agent
on MVP and then we build a new feature
on top of that. Maybe this is something

[00:08]
that in the X lingo you would call slop
on slop. So if we have something that's
been built by the agent not verified and
then you had more agent code written on
top of that and then you run the
evaluations to see if it's working or
not. You can keep making this
arbitrarily more complex. Uh for example
on in agent four that we launched a
couple of months ago, we completely hide
the complexity of doing task
decomposition and running agents in
parallel and then merging all the
patches together. So
we can also take as an input the PRD, we
do the task decomposition, we run all of
that in parallel and then we run the
valves after that. As you can imagine
the parallel plus merge scenario is far
more uh you know, challenging for a
standard coding agent.
I give you here some more ideas we
describing in the paper, you know, but
you can even start from a buggy
application, build a feature on top of
that and see how much your agent
struggles, you know, to actually make it
make it work correctly.
So the the key question or the
complexity here is how do you actually
do the grading? And that's what I told

[00:09]
you before, you know, was where we spent
most of our effort. It turns out that
when we're working on our previous
version of the agent, we put quite a lot
of effort in building an automated, you
know, app testing feature which
literally doesn't know anything about
the app per se. Cuz if you think about
it, when it comes to web coding, you we
don't give any level of
uh you know, guardrails to our users.
They can decide the language they want
to use. We can decide a different
framework. So the evaluator has to be
totally agnostic on how the
implementation looks like.
And what our evaluator
evaluator agent does is it reads the
code base, it then opens a browser and
points it to the application that our
agent has built and then step-by-step
goes through our testing plan. And even
the testing plan is expressed in natural
language and the actions are like open
the admin dashboard and log in with a
certain account and click on this
toggle. And if any of those steps fails,
then you know, we collect all of them
together and we generate a score. So, we

[00:10]
go through all these test plan and then
we decide ultimately if the score is
good or not. So, this is the key
complexity. When it comes to SweetBench,
we always had a fixed surface. We know
the repositories, we know the task
hardness, we know exactly how to make
this work. In ByBench, the surface is
completely green field and that's why it
took us several months of work to get
there.
Now, as I mentioned, we're announcing it
today. Here's the QR code. You can find
the entire benchmark available open
source on bybench.ai.
I'll let you to dig into the paper. You
know, we
it's going to be presented a couple of
weeks from today at the conference on AI
and energetic systems.
Peter, the you know, lead of the project
and first author of the paper is sitting
here. So, after my talk, please come and
have a chat with him if you want more
details.
I'm just going to give us sneak peek of,
you know, the most notable results
there.
First of all, we are noticing almost a
2x gap between the frontier models and
the open weights models.

[00:11]
And
the reason why I want you to pay
attention there is how I think it
because we know that
every single model player as every
single model builder is hit climbing
specific benchmarks. That's why we
release this open source. I want the
entire community to embrace it across
open weights and closed weights and make
sure that you know, we make progress
overall on by coding as well.
The other one, possibly not very
surprising is most models do a worse job
when extending their own code. So, the
slop on slop or by bomb vibe scenario
that I was describing to you before is
by far the most challenging. And that's
the reason why I always advocate to have
a testing step in between every time you
create a new feature, otherwise you keep
building on shaking foundations and
eventually your vibe coding application
is going to fail.
I'm going to give you back the QR code
later on. But, you know, let let's move
to the to the next step.
We talk about offline eval. I talked to
you about vibe bench, but as you recall

[00:12]
there were like two main pillars that we
care about. And the reason why we also
care about the online one is because
there is a great difference in terms of
volume of signal that we can collect.
So, on the offline or right now we're
working roughly 20 applications. The
reason, by the way, why we made it open
is because we are more than welcoming
contributions from the community. So,
more applications, harder prompts, we
can keep making this benchmark arbitrary
harder so that we make our traffic's
life harder to actually come with over
time.
But,
when it comes to Rabbit Engine instead,
you know, we're we're collecting
millions of sessions every day and
they're very valuable because they
capture what our users actually do on
the platform. And they're completely
unscripted, the agent is always running.
So, how do we distill useful information
out of them?
Well, it turns out that we run a lot of
AB tests. It's basically our way to keep
ourselves honest because vibe bench only
tells us part of the story.

[00:13]
And I invite every agent builder out
there to start to invest on their AB
testing infrastructure as soon as
possible. It's the best way in which you
can make steady progress.
Now, we ask a wide variety of questions
for ourselves. So, we we built a lot of
different instrumentation and metric in
our agent so that for instance, we can
find out is there a normal span ongoing
or is the agent running for longer than
expected? Or we constantly keep track of
the user sentiment. It's it's a very
easy thing of to collect because every
time you receive a prompt, you can do
sentiment analysis on it and then
receive the user is getting frustrated
or not. And last but not least, this is
very idiosyncratic to Rapid. Our users
can also publish their application on
our product. So, it's a very strong
positive signal if they decide that
whatever they built is worth to share
with their colleagues or to put it in
public in front of everyone. So, all
these signals clustered together gives
us something like this. If you have ever
done an AB test in your life, I'm sure

[00:14]
this looks familiar.
And
it might look familiar especially
because not everything is either green
or red. This is the, you know, hard
harsh truth about running an AB test.
They never give you a crystal clear
signal of what you should be doing. So,
in this case for example, uh the average
run duration of our agent, you know,
went up by 7% but conversely is 8%
cheaper and we saw the fluctuation in
terms of positive and negative
sentiment.
What shall we do in this case? This is
where human taste and product philosophy
still plays a key role. You will never
get or very rarely do we get like a
crystal clear configuration of the
results of your AB test.
And
to make our life a bit easier on how to
generate these AB test candidates, what
we do is we cluster all the traces that
we receive every single day and night as
you can imagine and we try to identify
first of all, which cluster are

[00:15]
capturing normal nominal behavior of the
agent. And as you can imagine, there are
plenty of them because the vast majority
of times the application is actually
successful but of course there is a long
tail of problem that it happens to
surface.
In case we find a problematic cluster,
then what do we do? We embed all the
failure summaries.
We
we cluster them by type so that we find
out the different failures that are
happening at a certain point in time.
Then we pass them through an LLM to
classify exactly what is going on. And
the fact that we do this
not based on regex on logs or like very
deterministic techniques is what
actually makes a difference because you
will be able to cluster things that are
semantically close to each other even
though the agent doesn't give you always
the same type of output.
And you know, once once we find these
uh cluster configurations, we are forced
to retrain them every single night
because we are running several versions
of the engine in parallel. We ship many
versions every single day, so we can't

[00:16]
live with a fixed cluster configuration.
And aside, you know, from also helping
us to identify the failure modes,
another interesting feature is the fact
that once we retrain those clusters, we
can go back and see if after we believe
we fixed a problem, a certain cluster is
actually disappeared. So, say you have a
certain tool failure that is happening
only a limited amount of time. So, not
something that will show up in your
DataDog dashboard, for example, not a
failure that happens 50% of the times,
but maybe it was happening 1% of the
times in certain specific conditions.
And from here, you will start to
realize, okay, I shipped my new PR and
that cluster is disappeared. So, you
start to have some evidence that you
mitigated the problem.
The
The technology that we built internally
was called Telescope and it's a fairly
simple loop, I hope, after I explain
everything. Uh first of all, we start by

[00:17]
discovering the problems. And this is
based on the trace clustering that I was
talking about before.
Then, based on that, we create code
changes. So, it's completely automated.
We basically cut PRs with a coding agent
based on the information we got from the
trace, based on information we collected
from the logs, from all the different
different dashboards that we had.
Then we evaluate if the change we
generated, first of all, is is is a
breaking change. So, we rerun by bench.
By bench is kind of like a litmus test.
If the score drops by 10 points, we
decide that the change is bad.
If it's a controversial change that we
believe could affect also negatively our
agent, we run an AB test. So, we put it
in front of the users and we try to find
out what are the trade-offs. If it's a
clear sure shot, then we just ship it in
production.
And
few times when we believe that the
hypothesis was correct and maybe the PR
was not perfect, we keep iterating on
the problem. Maybe maybe we run another

[00:18]
AB test until we are in a good
configuration and then we actually ship
it.
If you think about it, this is very
similar to the work you do as an AI
engineer all the time, but 90% of it is
now aided by an agent in the loop, you
know, rather than you having to sweat
about every single step of the process.
Let me give you all an example of, you
know, what we actually experienced, you
know, once in production.
Um
Rabbit Agent immediately starts an
execution environment the first time you
submit a prompt. And of course, to set
up everything, especially with the level
of complexity we built, requires, you
know, quite a few seconds.
We had a degradation in the long tail
where our, you know, setup time was
longer than expected and our agent was
ready to roll before the environment was
fully set up.
As you know, agents have become really
eager to fix problems. So, Rabbit Agent
went on a tangent and started to try to
fix the environment, you know, on the
spot. Um
it turns out that by the nature of
agents not being deterministic, every

[00:19]
single debugging session looked a bit
different. So, if it tried to find out
this long tail problem just by grabbing
the logs, it would have almost not
appeared.
But the moment we cluster all the
traces, you know, with basically with we
we through the semantic layer, then we
started to figure out that this problem
was happening quite often, and we
immediately able to create a patch and
fix the issue. In this case, we didn't
have to run an AB test because it was a
pure regression case. But in case it was
a problem that required testing, of
course, we would have put an additional
step in between.
And even though I'm a big fan of
trying to optimize as much as possible
the life of an AI engineer with agents,
I do think that there is a lot of
intellectual work to be done by humans
still in the kind of loop that I
presented to you.
For example, whenever we find one of
these clusters that I was talking about
before, as a team, we always focus on

[00:20]
formulating an hypothesis on what could
be possibly go wrong there. Cuz the
truth is when running in production,
you're going to get a really a large
amount of candidates of what you could
be fixing. So, you need to prioritize
where you put effort, where you put
resources. So, if the hypothesis is
intriguing enough, then we move forward,
and we don't just let the agent write a
PR without any kind of supervision. We
actually try to feed some of our
understanding of what is wrong. So, we
give it more guidance.
And ultimately, if you think about it,
every single time we decide of working
on a PR and doing an AB test, we're sort
of like shaping the hill that we try to
optimize. Cuz if we only care about,
say, making the product more affordable,
we're going to go and try to fix all the
anomalous spend problems, and then we're
going to do our best to optimize that as
much as possible. So,
all these choices really determine the
product philosophy of what you want to
put in front of our users. And then,
last but not least, as I was showing you
before on the AB test dashboard, if

[00:21]
there is not a clear result, ultimately,
if you decide to launch or not, is still
a choice that a human does. Often times,
that's that's on me in the rabbit. And
again, that determines really what's
going to be the ultimate product
experience.
So, my In closing, what I want you to
have as a takeaway today is don't think
of evaluation just as this last check
before shipping. It shouldn't be just a
boolean flag, but rather think of this
as an engine that allows you to ship a
better agent every single day.
Thanks, everyone. And
I'm going to invite Hannah on stage so
we can have a chat about how we've been
working together in the last few months
to go. Thank you.
>> [applause]
>> Awesome. So, my name is Hannah. I'm part
of the Applied AI team at Anthropic, and
I work with Michele
on the Replit agent and on everything
that they build with Claude. So, I want
to ask you a few questions about what
you built here. My first question is

[00:22]
Vibez is something that we've seen a
couple times. You've used it with us to
give us feedback on research models that
we're testing. But, what was was your
vision from the beginning to make
something that you were going to open
source and make available to the
community? I think a lot of people may
be trying to build evals like this for
themselves where they see holes in the
public benchmarks, but I think this is
kind of a unique approach, and I'm just
wondering if you could talk about that a
little bit.
Yeah, I've been asked this often, why
don't you keep this as a private appeal
of your company? Fundamentally, I
believe that
we should try to give back as much as
possible to the community. And we all
have to benefit from creating public
evals. It helps you to make better
models. It helps us to make a better
agent. It helps everyone to create
better products. And I I don't believe
in competing on evaluations. I come from
a research background where everything
should be open.
So, we'll we'll keep doing this for as
long as we can in Replit. And And again,
I I really invite people to collaborate
on Vibez. I I tried to instill this idea
in the community several times when I

[00:23]
was giving talks in the past and at a
certain point I realized we have to
build it ourselves rather than just
trying to invite others to do it. Mhm.
Well, I'm really excited to see what
people do with that. Um
I also want to ask you about the second
pillar, telescope. This is um you know,
a pretty sophisticated system that
you've built. It sounds incredibly
useful. It sounds like something you've
tuned quite a lot over time.
For people in the room who might be
trying to build something similar like
this, what lessons did you learn along
the way? What kind of tips could you
give them about how they can build
something useful like this?
So, first of all, if you try to do this
even, I don't know, 6 months ago and you
got discouraged because you didn't get
like a return on your investment, uh
definitely try it try it again. The same
inflection point that you experienced
with coding agents back say in November
with Opus 4.5 and and similar frontier
technology, uh it also reflects to what
I just talked about now. So, the the

[00:24]
fact that long context and models that
are really capable of reasoning on a lot
of content means that you can
practically inject an entire trace of
your agent into Opus and get fairly
sophisticated feedback about it. Um so,
you at the same time you should really
be investing in collecting all the
signal that you can from your agent and
as well as you know, the environment
where you're executing it. So, I know
that I I had to run fast during the
talk, you know, but I couldn't go in
depth on all the different signals that
we bring into telescope. It is not
purely
what's coming from the trace, it's also
the feedback that we collect in product.
Like we have a feedback form, so every
time the agent doesn't behave correctly
and the user complains, we have the user
point of view, we have the trace of the
agent, we have everything we instrument
in the platform in DataDog.
Unsurprisingly, all of that together,
put, you know, in context, helps even
more to pinpoint where where the issues.
Yeah, I think that idea of building the

[00:25]
clusters, like you were saying that a
single trace, it's very hard to debug
what might be going wrong there, but
when you are able to group them all
together and get these other signals in,
really reveals a lot more information
and something actionable. Makes a ton of
sense. Yeah, it does and I think it also
makes the life of an agent builder less
overwhelming because it really is when
you start to get a lot of usage, the
amount of feedback you receive is
actually overwhelming. And it's a good
It's a good signal. It means that people
care about what you're doing, but at the
same time it's hard to prioritize what's
actually important versus what doesn't
move the needle.
What I showed today is also a way for us
to try to understand, okay, this cluster
keeps showing on a daily basis and it's
fairly large and it has a lot of volume,
so we should actually fix that first of
all and then there is the long tail of
problems to fix will always be there
with agents given the fact that they're
non-deterministic. Yeah, that really
makes me think about the third thing I
wanted to ask you, which is what you
said about taste.
Uh, I think this is really interesting
point um that the taste of the AI

[00:26]
engineer is very important and could you
talk about how your team develops that
taste? Have you always had this taste or
have you improved your taste over time?
Like what's the process of building that
and developing that for people who might
be trying to build their own taste?
I think we all brewed it over time
because you know, when we launched
these, you know, was more than a year
and a half ago, agents were way less
powerful than they are today.
Uh, maybe not much taste to be applied.
It was more like a survival game just to
make sure it was barely functional. And
now that they're becoming so powerful
and you have such a wide variety of
choices you can make, um then you you
start to develop a taste that should
really be in tune with your actual user
base. Like if if you're building an
agent for software developers, maybe 80%
of the choices that we make every day in
the team will be almost the polar
opposite of what we do.
And you always want to keep in mind that
it's being used by personal likeness
different from you. Especially in our
case, like everyone at Rabbit is very

[00:27]
technical and we are giving the product
to knowledge workers who have never
written a single line of code.
So, it's a it's a very good trade-off to
to learn.
Awesome. Thank you for sharing that.
I'm sure people are going to have lots
of questions for you and for Peter, who
is one of the authors of Vibrent. So,
everyone please come find them and thank
you so much for coming for
>> Thank you.
Have a good one.

</details>


We’ll be taking [Code w/ Claude to London](https://claude.com/code-with-claude/london) (May 20-21) and [Tokyo](https://claude.com/code-with-claude/tokyo) (June 5-6). All Day 1 keynotes and breakout sessions will be streamed live.

*Stay tuned for technical tutorials, guides, and customer stories inspired by our talks.*

‍

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Jun 17, 2026

### Secure access to the Claude Platform with Workload Identity Federation

Product announcements

[Secure access to the Claude Platform with Workload Identity Federation](#)Secure access to the Claude Platform with Workload Identity Federation

[Secure access to the Claude Platform with Workload Identity Federation](/blog/workload-identity-federation)Secure access to the Claude Platform with Workload Identity Federation

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

May 7, 2026

### Collaborate with Claude across Excel, PowerPoint, Word and Outlook

Product announcements

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](#) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224ef32980bc807847d_a683fdcfe3e2c7c6532342a0fa4ff789c3fd4852-1000x1000.svg)

May 19, 2026

### New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

Product announcements

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](#)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](/blog/new-in-claude-managed-agents)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Apr 30, 2026

### Claude Security is now in public beta

Product announcements

[Claude Security is now in public beta](#)Claude Security is now in public beta

[Claude Security is now in public beta](/blog/claude-security-public-beta)Claude Security is now in public beta

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Claude Code

Coding
