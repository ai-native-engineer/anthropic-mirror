---
title: "The thinking lever"
channel: claude
url: https://www.youtube.com/watch?v=T7KqH7kYnE4
youtube_id: T7KqH7kYnE4
published: 2026-05-20
duration: "21:17"
captions: en-orig
---

# The thinking lever

[![The thinking lever](https://img.youtube.com/vi/T7KqH7kYnE4/hqdefault.jpg)](https://www.youtube.com/watch?v=T7KqH7kYnE4)

<details>
<summary>자막: The thinking lever (21:17)</summary>

[00:00]
Good to see you all today.
Uh I'm happy to have so many Claude
lovers in one room.
My name's Alexander Briken and I'm on
the applied AI research team here at
Anthropic.
And today we're going to be talking
about the thinking lever.
Specifically, we're going to talk about
how Claude leverages compute
at runtime, at inference time,
typically called test time compute, to
make more effective use of tokens in
solving some of the hardest problems
that Claude has in front of it.
And I'm going to share some of the best
practices when it comes to using
different levers and using different
tokens to essentially try to solve those
problems better and hopefully you'll
learn something as well.

[00:01]
So, looking back a couple years,
one of the key developments in large
language models has been this idea of
reasoning models,
which is using test time compute to
spend more tokens for a model to become
more efficient at answering a question.
Similar to how we can scale model
performance at training time, such as
train time compute, test time compute
also results in higher intelligence
results.
So, as you can see here on the left, we
have our different models in our typical
uh
range from Haiku, Sonnet to Opus. And as
you increase the size of the model
or the number of um
parameters, you can see that the
performance increases up to nearly
roughly below 80% for an internal
agentic coding benchmark that we run.
Equally, on the right-hand side here, we
have a logarithmic access on the on the
x-axis and you can see that as Claude
spends more tokens,

[00:02]
we see the actual performance increase
as well. And so both of these, the max
on the right and the result that you're
seeing here on the left, are actually
the same score.
So this is actually true of every
knowledge domain work. So you take a
reasoning problem in Deep Search QA,
which is a benchmark,
computer use through OSWorld,
or humanities last last exam, which is a
PhD level series of test cases.
In all of those results, we see that the
model becomes better at producing
outcomes when it uses more tokens to
think through the problem before
answering the questions. As a tangible
example,
and even though we love looking at
graphs at Anthropic, I wanted to show
uh this in real time.
And so I have this prompt in front of us
here, which is going to be run at three
different levels of effort for Claude.
Low, high, and max. And I'll show you
how the performance increases as Claude
spends more tokens. So this is our

[00:03]
prompt, creating a realistic simulation
of cars on a one-way street at a traffic
light. Note the one-way street and the
traffic light.
Okay, so our first one,
low effort on Opus 47.
It took roughly 50 seconds and there
were roughly 4,600
uh output tokens. And as you can see,
it's actually quite a good simulation.
We have a one-way road,
the cars are on two lanes,
um they're pulling up to the traffic
light, stopping at a regular cadence,
and then I think we have a few kind of
adjustments we can make in this
simulation to change the spawn rate of
cars or how often it turns red or green.
And so as you can see, the the cars are
kind of just moving through and then
stop when the the light becomes yellow.
Cool. It's quite simplistic, though.
Now let's move over to high effort.
Let's turn that effort level up.
Now you can see on the left Claude is
actually spending double the amount of
time it takes to run this

[00:04]
to create the simulation
and roughly double the amount of tokens.
And I would say that this simulation is
a little bit more detailed.
We now have same one-way road, different
types of vehicles showing up. There's a
few lorries in there for the Brits out
out in the crowd. And as well as that,
there's a traffic light, but the traffic
light isn't in the in the middle of the
road. Like if we flip back to the
previous example,
you'll see that the traffic light was
positioned in the middle road, which
makes absolutely no sense.
Whereas now Claude has sort of thought
to itself, okay, I should probably
position it sort of overhanging the
road. But it's sort of upside down,
which I don't love.
Um,
however, I would say it's a more complex
simulation.
One of the things when we ran this
prompt as well that Opus said in this
version is, "Hey, I've actually worked a
little bit through making the drivers a
bit more intelligent. So depending on
how the cars move, the cars around it
also react." Which is a more intelligent

[00:05]
simulation than the than the previous
version.
And finally, we ran Claude Opus 47 on
max effort.
This is using roughly 10x the number of
tokens and time to run
to create the simulation.
And as you can see, it's much more
detailed.
Arguably, this is the best traffic light
we've seen.
I like that it's sort of upside down
hanging following the laws of physics.
We also have this beautiful
sky scape in the back.
Um, and the cars also reflect this more
intelligent motion of vehicles.
So what does this mean?
Well, arguably, the more tokens it
spends, the more time it takes.
And so over time, we might see Claude
eventually go from seconds, minutes, or
hours of work to even days, weeks, or
months of work. And so this is the meter
benchmark we're showing that over
generations of models, and this is a

[00:06]
combination of both train time compute,
so larger models, as well as better test
time compute, so spending more tokens on
our higher reasoning models, we see that
Claude is able to work more autonomously
to cover human-level tasks to a higher
degree of of hours. And so Mythos, uh
which is one of our latest models, works
to a an extent of roughly 16 hours of
human work to a 50% uh level of
accuracy. Now, test time compute can be
any form of spending tokens.
This is typically at inference time, and
there's three ways in which we like to
break this down.
The first way
is thinking.
This is Claude's space for reasoning.
It's basically a scratch pad where
Claude considers the question that was
asked of it, uses whatever data it has
available to it in the prompt, and
thinks about the next steps it should
take to solve a problem. Equally,
there's tool calling right after.

[00:07]
This is Claude's interface with the
outside world. So in this example, we're
asking Claude to do a web search
learning more about the Anthropic
developer conference, funnily enough
we're all here right now.
And
tools can really be anything though.
It's, you know, 1 million types of
tools. Interact with your salesforce,
call the MCP server, even write into a
file system. All of those things are
tool calls. And finally, there's text.
This is the output that Claude makes
whenever you ask a question of it, and
it responds with something. It might be
a summary of all the work it did, it
might be a question up front in its in
its response to gather more information
from the user.
Test time compute has direct costs in
the form of tokens, token count, and
time that it takes. And so, naturally,
your might your minds might be coming to
the conclusion of, "Hey, wait a minute.
As a user, I want more control over what
Claude actually does on a day-to-day
basis."
So, using Claude, there's essentially

[00:08]
two ways in which users can change the
number or the amount of test time
compute that Claude leverages.
The first way
is using what we call effort, which I
talked through earlier. There's a dial
from low to max.
And depending on the effort you assign
model, it will work for a a longer
amount of time and spend more tokens.
So, often you're kind of asking yourself
the question of, "Okay, do I trade
intelligence off for speed?"
Secondly, we have budgets. Budgets are
basically a way of assigning more strict
constraints to the way Claude works.
That might be through max token
constraints or what we call task
budgets, which is another feature in our
API.
I'm going to spend the rest of the
session elaborating a little more on
effort.
Now, the ideal state is you ask Claude a
question, and it knows how much effort
it should put into it.
Uh but, humans always want to have that
additional lever they can pull to change

[00:09]
the effort over a period of time.
And so, when we first released reasoning
models,
the initial state was you would ask
Claude a question, and it would think
for a period of time
depending on how many tokens you
allocated to thinking,
and then it would execute a series of
tool calls, reading each one until the
output was formulated, and then you get
the response. Now, if you think of the
analogy of like how humans work,
typically, we don't do that. Someone
doesn't ask me a question, and I like
stand there processing it, and then
suddenly, I like go execute a bunch of
steps and come back with the answer,
right? Instead, which is how we resulted
in developing interleaved thinking,
you do something, you think about it,
you do another thing, you think about
it, and then you come back with the
result. And that's exactly what
interleaved thinking does. So, it allows
Claude to basically have thinking steps
after every tool call it does.

[00:10]
Now, let's take it a step further.
Adaptive thinking is basically an
evolution of interleaved thinking, where
you give even more control to the model
as to when it thinks and why it thinks.
And so, depending on the question at
hand, Claude will choose to call either
a tool call, output some text, like that
question I was referring to earlier, or
even think in it in whatever order it
likes.
And so, looking back to the analogy I
was talking to earlier, that actually
reflects even more of how humans work,
right? Sometimes I might take three
tasks at once and go, you know, if I'm
playing tennis, I go hit the tennis ball
then run back to the baseline. I'm not
thinking in that instance. If I'm doing
an academic problem set though, I am
probably thinking at every step of the
process.
Now, Claude can actually choose to not
think at all if it doesn't want to. So,
in this example, we could have no
thinking block.
Um
and that really just relates to the
question you ask of it, right? Even with
humans, if I asked you, "What is 10 +
10?" you'd immediately respond respond

[00:11]
with 20. Whereas, if I asked you,
you know, "Work through this really
difficult PhD level problem set." you'd
probably think a lot. But, different
members of the audience here might think
for more or less less time. So, it
really depends on the problem, the model
you're using, and how much context you
provided it.
Adaptive thinking isn't a model router.
We're not classifying the requests that
comes through the door.
Instead,
it's actually telling Claude, "Hey, you
have this thinking tool. You have the
ability to think. Use it whenever you'd
like." And the difference between that
and what we had before was, before we
would say to Claude, "You must think at
one point in time." Whereas now, Claude
doesn't have to think at all if it
doesn't need to.
We run all of our benchmarks that you're
seeing on screen on adaptive thinking,
and we've found that it's Pareto
efficient relative to interleave
thinking, the former way in which we
served our models.

[00:12]
So, historically, users have thought
about thinking as this effort dial.
If you want to wait longer, you can turn
on thinking for a better answer.
That's a reasonable instinct, but in
reality, a thinking toggle is actually a
poor proxy for the amount of effort that
a model should put in.
You're not expressing how hard you want
Claude to think when you turn a thinking
toggle on or off.
You're actually just turning off a core
capability. As I mentioned, there's
these three capabilities: thinking, tool
calling, and text. And so, when you
turned extended thinking off, you just
removed that capability from Claude.
Now, that's an unideal outcome, right?
Instead, I'd rather have Claude know
that it can think and work every time
using those thinking tools available to
it.
So, as an analogy with tool use, we
don't tell Claude to either never search
or always search the web. We just give
Claude a search tool and allow it to

[00:13]
reason as to when it should search.
In a similar way, when we work with our
teammates, I don't tell you, "Hey,
uh don't use your inner inner monologue.
Don't think about this problem set. Just
make come up with an answer for me."
I'll tell you the constraints of the
problem, some sort of knowledge worker
task. You'll go off and execute on it
pending who you are and what context you
have, and then you'll come back to me
with an answer, and we collaborate as a
team member.
Ideally, we want Claude to work in the
same way. So, I want to dig a little bit
more into some of the best practices
around using effort.
And
this graph is an articulation, as we saw
before, of effort levels increasing, and
so So, alongside that, the capabilities
of models.
So, the first thing to think about is
you want to evaluate model performance.
So, having a really good test set of the
problem that you're trying to get Claude
to tackle,
where there's really difficult

[00:14]
challenges that you're proposing to the
model, and evaluating at different
effort levels how well the model
performs, is one of the best ways to
just figure out whatever effort level
you should start with.
Now, one of the things you might notice
here
is there's diminishing marginal returns
to higher effort effort levels,
depending on the task.
And so, we In In this example, we even
see that, where max is
disproportionately, like, double the
amount of tokens as extreme extra high,
and it's only a marginal bump in
performance.
Now, low effort levels, I would say, can
accomplish a lot of things, but you're
often trading off intelligence for
speed.
And so, sometimes you might want to
think about low effort things as things
that aren't intelligence bound.
Things that you can simply accomplish
quickly without the model thinking that
much.
As a quick tip, um I'm going to give an
example of low effort actually coming up
with a really cool way of working

[00:15]
through a problem.
You all might be familiar with Claude
Plays Pokémon. It's probably my favorite
eval.
This eval is we put Claude into Pokémon
Red, and we gave it access to tools to
trigger buttons on, like, a Gameboy, for
example, and we gave it vision over the
game, and we had it execute and try to
beat the Elite Four, which is the
objective of Pokémon, if you're not
familiar.
And when we put Claude on low effort,
we actually found that it almost tried
to escapegoat the game. So, what it
would do is it would run all sorts of
mechanisms like using repels, using
potions to have to avoid going back to
the Pokemon Center, using escape ropes
to get out of caves quickly, running
away from poking Pokemon battles
whenever it encountered one in the in
the shrubs.
And this was really interesting because
when you put it on low effort, Claude
actually came up with this unique
solution to navigate the game and almost
complete it faster than it otherwise
would.
So, there are some benefits to doing low
effort because you're explicitly

[00:16]
constraining how much the model is
thinking through the problem set and
maybe it does end up in really unique
attractor states. Now, while evals are
always ideal,
I understand they're quite hard. I speak
to customers a lot and often they don't
have the perfect eval. And so, I want to
give you a quick, you know, rules of
thumbs that you can use when you think
about the different effort levels that
you use.
We're going to start on the right
looking at max. As I mentioned, max
effort can typically deliver gains on
the hardest tasks, but they might show
diminishing marginal returns. And so, I
wouldn't recommend starting here unless
you absolutely know that the
intelligence of your use case is
necessary. You know the problem set is
hard and you know Claude's going to have
to think a long time.
Extra high is where we've settled as
being the default for Claude code and
claude.ai.
We would argue that this is one of the
best tradeoffs between intelligence,
speed, and number of tokens. As you move
down to high,

[00:17]
this is a still a good balance of token
usage and intelligence and I would argue
that if your use case requires any
intelligence, you should probably land
here.
Um but it will be faster, of course,
than the other two I just referred to.
Medium and low are ways to just toggle
down that amount of tokens used. And as
a result of that, at low, as I
mentioned, you're really looking at
latency sent sensitive use cases where
maybe it's classification,
summarization, or data extraction. Now,
as I mentioned before,
we have these two levers that we think
about at Anthropic as we develop our
models. One is train time compute and
one is test time compute.
So, you might be thinking to yourself,
"Okay, well, how do I know whether or
not I should use a really small model
like Haiku
and make that effort level really high
versus having a really big model and
making the effort level really low?
Like, what are the differences there?"
So, I want to give you a few guidelines

[00:18]
for thinking through that.
On the left, you're seeing the Opus
simulation that we created before,
and on the right, you're seeing this
Haiku simulation,
uh Haiku 4.5. And as you can see, Haiku
spent roughly half the amount of time
developing the simulation,
but the same number of tokens, and I
would say the result is not nearly as
good.
I don't even know if those are cars, to
be honest.
Um and so, the conclusion that we come
to here is arguably if the if the
question you're asking of Claude
result needs any intelligence at all,
you're often better off using the larger
model.
And specifically, you're better off
using it even if you have the effort at
low.
Now, the way that you should think about
using smaller models, though,
is these low intelligence use cases,
where you're not really caring as much
about the outcome because the outcome is
so simplistic that you know Claude will

[00:19]
get it right most of the time.
Where possible, my recommendation is
probably use evals to figure out what
the best way to do things is. If you can
run Haikus on it and opus on across the
range for all effort letter levels,
that's the perfect world. Now,
obviously, you won't have
uh all of those resources every time.
And so, I'll try to give you some rules
of thumb in a second.
Now,
here's some summarized actionable
takeaways for you.
You should enable thinking really
whenever possible.
Give Claude that space to reason. Give
it the scratch pad so it knows that it
can use that thinking tool when it needs
to.
You can control that length through the
effort levels that I described.
Evals are often the best way to find
your ideal balance.
Finding the hardest evaluations are
always the best so that you can know
this is actually representative of the
things that I want Claude to do in the
field.
And then finally, when in doubt, go with

[00:20]
extra high. It's the default that we've
set for our products, and I would argue
that it's a great kind of Pareto
efficient outcome between latency and
number of tokens and intelligence.
The ideal world is that you set the bar
and the budget for the way Claude works.
So, let's say I want Claude to work on
some really long horizon task, a day,
maybe a week.
I want to be able to say to Claude,
"Hey, I'm only going to spend this
amount on whatever you do." Or, "Hey,
only take this long a week to do it."
And then eventually, Claude just knows
how to allocate that compute
appropriately. So, it knows how many
tokens it should spend, and then it goes
and executes returning the result given
the constraints you provided. And so,
over time, what we want to do is improve
the performance of Claude in recognizing
what tasks are actually important
and allowing Claude to appropriately
allocate its resources to solve them.

[00:21]
Thanks so much for listening.
I'm going to be around the conference if
anyone has any questions, and uh I hope
you enjoy the rest of the conference.

</details>
