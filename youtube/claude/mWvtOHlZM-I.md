---
title: "Tool, skill, or subagent? Decomposing an agent that outgrew its prompt"
channel: claude
url: https://www.youtube.com/watch?v=mWvtOHlZM-I
youtube_id: mWvtOHlZM-I
published: 2026-05-23
duration: "45:06"
---

# Tool, skill, or subagent? Decomposing an agent that outgrew its prompt

[![Tool, skill, or subagent? Decomposing an agent that outgrew its prompt](https://img.youtube.com/vi/mWvtOHlZM-I/hqdefault.jpg)](https://www.youtube.com/watch?v=mWvtOHlZM-I)

<details>
<summary>자막: Tool, skill, or subagent? Decomposing an agent that outgrew its prompt (45:06)</summary>

[00:00]
[music]
>> All right, fantastic. Can everyone hear
me? Thumbs up, all good? All right.
Everyone, I hope that you have had a
fantastic day at Code with Claude London
and so far today. My name is Will. I'm
on our engineering team at Anthropic. I
sit on a team called Applied AI. What
that means is I essentially split my
time between internal engineering work
and time spent building agents with
customers. So, folks, imagine that you
built and shipped an agent to solve a
problem. I'm sure that's something that
a lot of the folks in this room have
actually done. And imagine this that
this agent worked fantastic, right? But
it works so well that a few weeks after

[00:01]
shipping,
you were asked to add some additional
capability to the agent. A few weeks
after that, you received more business
requirements and you added additional
capability. This pattern continued and
continued until before you know it, your
system prompt had grown to become
several hundred lines long. You have
dozens of tools and sub-agents that
exist for your agent. And because of the
complexity,
you've started to see regressions in the
areas that your agent was previously
accelerating in. So, if this is you,
you're not alone. We see this type of
scenario happen pretty commonly with
customers and actually with ourselves
included in that. So, within this
workshop, we are going to simulate an
agent that is essentially grown to a
complexity where we start to see
degradation in its performance. We're
then going to walk through some of the
decisions that we as engineers and

[00:02]
architects make
in order to improve the design of our
agent to restore the performance that we
expect with the additional capability.
Specifically, we're going to make some
decisions around tools and skills and
sub agents.
As we modernize the stack of our agent,
we want to make sure that we're using
the right agentic primitives at the
right time. So, when do you use a tool,
when do you use a skill, and when do you
use a sub agent? We're going to talk
through all of that in this session. As
I mentioned, folks, this session will be
hands-on. So, let's go ahead and get
started. I first want to walk you
through our problem statement in our
agent. So, for the purposes of this
session, we're going to be focusing on
an agent called Stock Pilot. This is an
inventory management agent that was
designed by and for a mid-size uh uh
retailer.
The agent that you see on the screen can
do several things. It can flag low
levels of stock. It can forecast demand.

[00:03]
It can pick suppliers. It can file POs.
And ultimately, it can write weekly
reports for the employees of this
retailer. Now, none of these
capabilities are particularly complex on
their own. But again, the issue is that
we've essentially bolted capabilities
onto our agent over time without
modernizing our architecture. This
complexity has started to cause some
problems. Let's take a look at the
actual architecture today of the agent.
Folks, today the agent is facilitated by
a single orchestrator. So, you see the
Stock Pilot orchestrator sitting at the
top of the screen.
The agent has a system prompt, as I
mentioned, that's grown to be about 400
lines long. It has 12 different tools.
Three of those tools happen to be
wrappers around sub agents with
completely isolated context windows. So,
if you have the repo pulled up,
which we'll go into more detail in just

[00:04]
a bit, there's an agent that's under a
folder called before, which essentially
walks through this this agent exactly.
So again, orchestrator, long system
prompt, a lot of tools, we have a lot of
sub agents.
The result of this is that our evals
have started to dip. So, let's imagine
how we got here for a moment. Again,
like we built that agent up front to
solve a really specific problem.
We received business requirements to say
add maybe some forecasting capability to
our inventory management agent. So, what
we decided to do was essentially just
spin up a forecaster as a sub agent.
Again, later on we we received more
requirements to add report writing
capability to our agent. So, we decided
to add another sub agent for that report
writing capability.
Again, our evals started to dip over
time because we added more and more
complexity while just bolting this
capability on. So, let's take just a
little bit of time and talk about evals

[00:05]
specifically.
For this agent, folks, we have 12
different eval tasks across five
different types of graders. So, my
colleague gave a talk on evals shortly
before this. Evals will have a component
within this workshop, but it won't be
the main focus. I'll give you a quick
summary of the tactical evals that we're
using for this agent.
On the left side of the screen, you see
some IDs. You see several evals that
start with the letter R. This stands for
regression. These are more realistic
single-turn tasks that we grade the
model's capability on. So, imagine I
give the model a task, the model
comprehends that task in the form within
the agent, uh calls some tools, and then
provides a response back to me. We're
essentially evaluating that response.
We also have some more complex tasks
that we're grading the model on. So, you
see those F
IDs, the IDs that start with F on the

[00:06]
left side of the screen. That stands for
failure mode. In this case, we're
evaluating the model over a more
complicated multi-turn task that we're
grading. Now, again, I won't go into
evals too specifically. We have a number
of different types of graders that are
both deterministic and
non-deterministic.
Right? When I talk about not when I talk
about deterministic evals, we're grading
things like turn count and like latency
and like the number of tokens that are
used as our agent is completing a
particular task and we're tracking those
deterministic metrics over time.
We're also using the idea of LLM as a
judge to evaluate the non-deterministic
characteristics of our agent. So,
personality and tone and style and
output quality, we're using a
non-deterministic grader as a part of
our eval to evaluate our agent's
non-deterministic characteristics.
Now, we're going to run the evals for
our agent in just a bit, but when you

[00:07]
do, you'll find that the agent is
struggling a bit. I'll talk about some
of these evals in just a little bit more
depth. So, F1 on the screen, third from
the bottom, this is essentially
simulating a daily low stock sweep. this
is an inventory agent. We're simulating
our ability to look through all of our
inventory and pull the low levels of
stock.
This eval you'll find will actually fail
because the agent is going to do the
right thing, but it's going to take a
very winding path to do so. So, instead
of taking the straightest line from
point A to point B, the agent is going
to take a very inefficient path. It's
going to get to the right end, but it's
going to fail the eval because it's not
at the efficiency that we'd like.
F2 on the screen is another eval that
you'll see fail.
This eval actually evaluates the
ordering process under a particular
promotion package. This is going to fail
because we are using a sub agent for
this particular task. The sub agent is

[00:08]
actually getting the task right, but
there's a communication breakdown
between our sub agent and our
orchestrator. This is a really common
point of failure that we see when
customers have have really complicated
systems with a lot of sub agents. It's
important to get the communication
between your sub agents and your
orchestrator just right. In the case of
F2 like you see on the screen, this is
an eval that's going to fail because we
have a breakdown
in that communication.
The last one that I'll highlight that
you'll see fails is R8 on the screen.
R8 will essentially check the
forecasting during a particular
promotion month.
This eval is also going to fail because
we have two different policies that live
in very different parts of our system
prompt and actually end up contradicting
each other. So, I mentioned over time
our system prompt has grown. We start to
have some conflicts and the model gets
confused leading towards a failure for
this particular eval.

[00:09]
Now, in the repo, you'll see it in the
read me when we run these evals, you'll
see that they're going to pass up front
at about 83%
which is okay, but if you work in the
world of manufacturing, that is not
okay. 17% failure is a really expensive
failure percentage.
Now, let's double click on R8 again just
so that we can understand a little bit
about what's happening behind the
scenes. Again, R8 is where we're
essentially calculating the forecast
during a particular month with a
promotion. And so, in my
uh on my screen here on the right side
where you see kind of the simulated
terminal window.
Uh within the first block under the
commented text, we can see that the
agent pulled the right forecasting
baseline and also pulled the right
promotion multiplier. So, forecasting
baseline 12 units a day, promotion
multiplier 3.1x.
This is all correct. But, in the
calculation part below that, we can see
that there was actually some kind of

[00:10]
hallucination that happened. Instead of
using that 3.1x promo multiplier,
the agent actually ended up using 1.35.
So, something happened along the way.
A hint here is that the reason for this
is that we have context problem. So,
this isn't a model problem. It's an
issue with our the information that
we're surrounding the model with. Our
system prompt has grown to be really
long and is very confusing for the model
and has some conflicts in it, which lead
to the issue that shows up within this
eval.
So, folks, our objective in this
workshop will first be to run our suite
of evals.
We're going to triage the issues and
we're going to update the design of our
agent accordingly. And then, we're going
to do something that we call internally
hill climbing towards eval improvement.
Right? So, we run our evals, we get a
baseline. It's going to be about 83%.
We're then going to optimize the
architecture of our agent and we're
going to continue then running our eval
so that we climb on them, hopefully

[00:11]
seeing the success percentage uh improve
over time. In this lab, we're also going
to start with an agent that is
self-created on our messages API. Um
again, if you have the repo and you
click on the before folder, I'll show
you this in just a bit.
This is an agent that is built from
scratch on our messages API. We're going
to actually migrate that that agent to
Claude managed agents.
Claude managed agents essentially allows
us to offload the messiness that comes
with maintaining an agentic harness in
scaling agents safely and securely to
thousands and tens of thousands of
users, right? Like if I want to build my
agent locally and run it locally, I can
do that pretty quickly and pretty
easily. But the moment that I need to
take that agent, I need to host it
remotely, and I need to allow hundreds
and and and and thousands of users to at

[00:12]
the same time engage with that agent,
there's an infrastructure problem,
there's a scaling problem, there's
memory, there's security, there's so
much that I have to account for. So, in
order to offload that, so I can just
worry about the architecture of my agent
itself and make decisions around tools,
skills, and sub-agents, I'm going to
offload everything else to Claude
managed agents.
So, again, to break that down just a
bit, um there's been a few talks on CMA
so far today, but this is really where
we're able to separate the agent from
the session details, from the sandboxed
environment where tool calls are
actually happening.
Um again, this allows us to offload
particular parts of the stack to then
worry about the to then only worry about
the design of our agent itself.
All right.
I mentioned that we're going to get

[00:13]
hands-on in this workshop. We are going
to go ahead and do that right now.
Now, what you see on the screen here
is the workshop URL as well. Um if you
haven't had a chance to grab it, feel
free to go ahead and do so. Um this is
where we're keeping all of the different
workshops throughout Code with Claude
within London, so you can go back and
revisit them if helpful. Within this
workshop, we're going to be working on
agent decomposition. So, that's going to
be the name of the folder that we're
actually going to be working within.
Great.
Let me jump forward here.
Perfect. So, the first thing that we're
going to do
as a part of this workshop is we're
first going to get a baseline. So, when
you open up that link,
you'll first clone the repo. So, we're
going to clone the repo locally. We have
a UV project that's set up. So, we're
going to run UV sync in order to make

[00:14]
sure that we have all of our packages
and our dependencies to be able to
invoke the Anthropic SDK and then
eventually deploy our agent to Claude
managed agents. So, we can run UV sync
to do that. I mentioned previously that
we're going to need an API key for this
workshop as well. So, using those
credits that you got at the start of
this session, you can go to your Claude
console account and create an API key.
If you copy the ENV example, you'll just
have to manually copy your API key into
the ENV file that's created for you.
Now, all the 12 evals that I previously
walked you through, we have all of those
set up already. So, in order to get a
baseline and run those evals, you have
to run UV run evals {dash} {dash} agent
before. This is all in the read me, but
if you just run that command, you will
be able to
actually go about running your evals.
Now, in terms of our building here,
we're going to take a number of steps to
actually go about running our evals

[00:15]
using Claude code to triage the results
of them and then climbing accordingly on
our agent.
So, we're first going to take some We're
going to take a look at our the system
prompt that we have for our agent
itself. So, I mentioned earlier that our
system prompt is currently sitting at
about 400 lines long. We've been
stacking information on our system
prompt over and over again as we've
continued to get more business
requirements. So, our system prompt is
very long. We'll take a look at that.
We are then going to take some time to
evaluate the tools that we're using.
Right now, as I mentioned, we have 12
different tools. Three of them are
actually kind of wrapped sub-agents, so
we'll take a look to see what we can do
to make that more efficient. And then
lastly, if there are any sub-agents that
we really need to make our agent
effective, we're going to take a look at
the best way
um to actually construct sub-agents with
Claude managed agents.
I'm going to jump back just for a
moment. There's one thing that I forgot
to mention for you as you get started.

[00:16]
Um within the repo folder, there's two
different uh folders that you'll see.
There's a before folder, and then
there's a starter folder. Those contain
two separate agents. So, if you want to
view the messages API version of the
agent, again, this is just me building
my own agent loop and my own agent
harness around the Anthropic messages
API to invoke Claude, you'll see that
within the before folder.
If you want to view what that agent
looks like when deployed on Claude
managed agents, um you can look in the
starter folder, which exists right below
that. If you want to deploy your agent
on Claude managed agents, you can run UV
run deploy a starter. So, again, run
your evals using the messages API
version uh {dash} {dash} agent before,
you can then deploy your agent on Claude
managed agents. We already had it built
for you, and it's really easy to use
Claude code to kind of compare the two

[00:17]
um and understand exactly what's going
on and what some of the differences are
uh with Claude managed agents.
Okay, so I'm going to jump over here,
and we're just going to open up Claude
code,
and we are going to build together. I'm
I'm to zoom in very far so that you can
see everything and so that I can see
everything and we'll just talk through
exactly what happens when I run some of
these evals and we'll talk through the
process that we usually go through to do
what I just called hill climbing on the
evals themselves. Okay, so if you're
looking at Claude code here, again, I
just used Claude code to actually run my
evals because I want Claude's help in
triaging what's going on.
Um, so this is me. I'm using Claude
code. I have Opus 4.7 running as you can
see on the screen. Uh, my effort level
is set to extra high. I usually set
effort as extra high with Opus 4.7 and I
forget about it. That's the effort level
that I usually stand. We find that it
gets great performance
um, with extra high effort all together.

[00:18]
Now, you can see on the screen the first
thing that I did was I ran my eval. So,
I used the bash capability in Claude
code and I ran UV run evals {dash}
{dash} agent before.
Claude actually went ahead and ran my
eval. So, I'm going to scroll down and
we're going to look at what Claude found
while actually running those. So, you
can see the response that we got, the
results that we got from this eval run
was actually lower than what I told you
before. So, we ran them and we got 62%
which is worse than the 83% that we
started with.
So, we passed seven out of 12 of them
and it looks like Claude has provided us
with a diagnosis for the different evals
that we actually failed.
Let's scroll down just a bit more.
And we are going to use Claude to
understand a little bit more about why
this actually happened. So, you can see

[00:19]
here I am using Claude
to provide me some of the themes around
why we actually failed some of these
evals. Again, this is a a technique if
you have evals for your agent. Um again,
as Geary showed before this session, you
can use Claude actually go about
triaging these. So, it looks like
there's a few different themes that
Claude is figuring out based on this
agent. So, the first thing Claude is
seeing that our model is taking on a lot
of work that it should have tools in
order to do. So, our model is doing a
lot of reasoning across information that
it just doesn't have the tools to be
able to complete.
It looks like there is some issues that
we have with the enforcement of output
structure. So, our model and our
sub-agents are producing information in
a particular output structure that
doesn't align um exactly with uh what
we're looking for with um
to to pull the best performance from uh
from our agent.
If I continue to scroll down here, you

[00:20]
can see there was some policy issues,
etc. Um as I mentioned before, we have a
system prompt that's really long right
now. Um and so, Claude is seeing some
confusions based on the information
that's found within the system prompt.
So, again, you can see Claude has found
some root causes.
Now, we're going to do a few different
things here. Again, we're going to go
one-by-one and address some of the areas
um that we're seeing issues on within
our agent. So, I'm going to scroll down
here and we are going to use um Claude
code to triage some things within our
agent. Okay. So, the first thing that
I'm going to ask Claude to do, we're
going to talk through this. Claude is
making some changes, which is great. Um
system prompts tend to get very, very
long when we accumulate agents over
time. So, the first prompt that I ran,
if you're following along, feel free to
go ahead and do this. I encouraged
Claude to look at my agent.py file,
which is where our main CMA um agent
loop is located. Again, that's agent.py.

[00:21]
And I essentially said, "Hey Claude, do
you have any thoughts on the system
prompt? Maybe I can use skills instead
of a long-running system prompt for
progressive disclosure. So, the first
thing that we'll talk about is skills.
There's been a few other sessions on
skills. The short definition that I like
to use is that skills are packaged and
composable information that Claude has
the ability to pull into context
whenever Claude realizes that it needs
that information to complete a
particular task. Right? Skills are
really useful with Claude code. Like if
you need to provide Claude information
on your testing process, or if you want
to package up your brand and your UI
components, and bundle them into a skill
that Claude can pull into context
whenever needed, skills are fantastic.
Skills are also useful within the agents
that you're building for your customers.
So, if you're building a product, and
you are going to give that product to
customers, you're building an agent,

[00:22]
skills are great within that.
In the case of the agent that we have on
the screen here,
um again, we have a lot of different
policies and a lot of procedures that go
into our inventory management system. As
I accumulated requirements over time,
instead of building skills, I decided to
take all of that information and keep
appending it to my system prompt. So, my
system prompt got longer and longer and
longer over time.
This is not something that we recommend
you do based on the introduction of
skills. Right? Leave the system prompt
only for the information that Claude
needs in its mind, regardless of the
task that you give it.
Skills are fantastic for packaging
information that Claude is going to need
some of the time, not all of the time.
Right? So, if I ask Claude to go build a
forecast, Claude is going to um go ahead

[00:23]
and do that. Let's see, I lost my
computer just for a second. Here we go.
If I ask Claude to go ahead and build a
forecast, right, Claude is not going to
need forecasting information unless I
specifically ask it to go ahead and and
build that forecast, right? So, in the
case of that particular task, I want
Claude to pull forecasting information
into its context window. Skills are also
fantastic for making sure that you are
being efficient with context because if
you stuff all of this information into
the system prompt, you're polluting that
context window with information that
Claude does not need
>> [snorts]
>> um, in order to complete a particular
task. So, again, the first thing that I
did, I'll zoom in just a bit more so
that you can see this, and I'll scroll
up just a bit.
I said, "Hey Claude, can you help me
take a look through my system prompt?
Can I use skills instead?
My system prompt is too long and I need

[00:24]
some help." And so, Claude did an
analysis of this and realized that I
have some pre-built skills that I can
use to supplement information in my
system prompt. So, the first correction
or fix that we're going to make to
modernize our architecture here
>> [snorts]
>> is we are actually going to um, remove
uh,
many of much of the system prompt and
we're going to put that information into
skills. And so, you can see here the
first thing that we're doing with Claude
is we are activating a number of
different skills that previously were
not there before, and we're actually
swapping our system prompt to be a short
prompt instead of a long one. So, if
you're curious, if you feel like you
have a long system prompt within the
agents that you're building, feel free
to take a look at this to see the
differences between what was like a
400-line system prompt compared to about
a 50-line system prompt, we've
supplemented that and we've switched a
lot of that information to skills.

[00:25]
Great.
I am now going to continue working with
Claude. You can see we made those
changes here, which is fantastic.
There's some evals that I can go rerun.
I'm going to ask Claude to do one more
thing, and then we're going to we're
going to rerun some of our evals to see
where we've improved.
So, I mentioned before that we have 12
different tools. You saw those on the
screen in the second slide that I
shared. As a part of this inventory
management agent, we have we have tools
that we've created for everything. So,
whenever Claude needs to retrieve data,
we have a tool. Whenever Claude needs to
analyze data, we have a tool for that.
We have tools for everything. So, I'm
going to ask Claude to take a look at
the tools that my agent has and help me
think through how I can optimize here.
So, right now Claude is running an
analysis across the different tools that
I have for my agent.
And we're going to get to see what some
of the results for.
Now, while this is working, I'll give

[00:26]
you a tip when it comes to building
agents that we carry with us at
Anthropic for our agents internally and
the agents built with customers.
Whenever we build agents, we lean into
the same primitives that we as humans
have access to. So, imagine yourself
when you show up to work, right? You
have a computer that's sitting in front
of you. You have the ability to navigate
files on a file system. You can type in
the browser and you can search the web.
If you're an engineer, you have the
ability to write and execute code.
When you think about Claude code as an
agent, we've effectively given Claude
access to all of the same primitives
that you and I have access to when we
show up to work every single day. Like
Claude code is a great coding agent
because Claude is really good at code,
but essentially what we've done with
Claude code is we've just given Claude
access to a computer.
Right? And this is really powerful
because this allows us to drop in better
versions of Claude as we continue to

[00:27]
release new models, and Claude just uses
those primitives better than it did
before.
Right? Like imagine yourself after this
conference compared to yourself when you
walked in. You're going to have the same
tools at your fingertips, but you're
theoretically, your brain's going to be
a little bit bigger, you're going to be
smarter based on what you learned here,
and you're going to be more effective
while using the same tools. Claude works
the same exact way.
Right? And so whenever we build agents,
we lean into human-like primitives
first. These primitives are things like
code execution
and the navigation of a file system, the
keeping of a to-do list, the ability to
search the web. These are foundational
tools that we always start with when we
build agents, and we remove them as
needed. An example that I like to give
is with file, uh, like document
analysis.
If you're building an agent that
requires document analysis, maybe you
have a lot of

[00:28]
CSVs or Excel sheets that your agent is
going to be looking over, code
execution, so the ability to write and
run code is one of the best ways of uh,
uh, doing data analysis and working
across lots of documents, right? Like if
you need Claude to look across the CSV,
giving Claude a bash tool so that Claude
can write a quick Python script and
reason across the results after running
that Python script is much more
effective than just uploading the entire
CSV into Claude's context window.
Right? So again, we lean into these, uh,
computer-like primitives first when
building an agent.
So if If scroll down here, that's
exactly what we did here. You can see we
took a lot of steps and we actually
removed most of the tools that exist
within our agent and we replaced them
with some of the primitives that I
talked through previously. This is an

[00:29]
inventory management agent that leans
really well to this. Um I have the
ability to consolidate and remove a lot
of the tools that I'm using to reason
across Excels and reason across
forecasting data and just give Claude
access to the same tools that Claude
code has in order to do that. What's
cool about this is that when you build
using
Claude managed agents,
these tools are actually included by
default. So if you want to give Claude
access to those same tools that Claude
code has and use them to drive powerful
capability within your agent, you don't
have to worry about writing a tool that
gives Claude the ability to write and
run code. Or you don't have to write a
tool that gives Claude the ability to
use the file system. You can just rely
on those built-in tools
that we have built ourselves for Claude
code that we just make available through

[00:30]
Claude managed agents.
I'm going to ask Claude to rerun an
eval.
The evals to see if we are getting
better.
Now with your agent, there's always
going to be the need to add some custom
tools as well. Like you're not you're
only going to get so far by giving your
agent the same tools that we give Claude
code.
So we always start with those primitives
like code execution and web search and
to-do lists, etc.
We always start there and then we either
remove those tools as we don't need
them. Right? There might be some agents
where we just don't need web search, so
we'll go ahead and remove that tool. Um
Um and then we'll add custom tools
whenever we need them, right? So again,
when you think about tools, I encourage
you to start with those Claude code
primitives, those human-like primitives,
and then add custom tools only as you
need them. In the case of this specific

[00:31]
inventory agent, um we were able to
remove most of the tools and replace
them with Claude codes. So you can see
right now, Claude is redeploying my
agent to Claude managed agents. So
again, I have my agent locally. I am
redeploying it based on some of the
changes that we've made, and now I can
rerun some of my evals to see the
result. So you can see in that last
command, I'm rerunning uh the F1 eval,
and we're going to see what happens as a
result.
Now, we always get a lot of questions
when it comes to MCP. So in the case of
CMA here, you have a couple different
options when it comes to tools. You can
first lean on those Claude code
primitives, things like web search and
code execution and file system. Again,
that's what we start with. You can then
create uh just custom tools, so
standalone tools that only your agent
has the ability to use.
Then you can connect your agent to MCP.
We see a lot of folks run towards MCP
first, and a lot of our customers end up

[00:32]
in this ecosystem where there's a lot of
kind of chaotic MCP servers that exist.
A lot of times they have overlap, um
which can create some problems. So when
we build agents, again, we start with
those Claude code tools.
We then create local tools only for our
agent. We don't run to MCP. And then
only in the case where we have a common
collection of tools that multiple
clients will benefit from accessing, do
we go about the process of collecting
those and publishing them as an MCP
server. So only when we have multiple
agents, maybe multiple Claude code
clients that need to access the same set
of standardized and governed tools, we
run towards MCP.
Something else that's becoming
increasingly common throughout the
industry is leaning on Claude's ability
to effectively use code execution as a
means of executing tools. So, we see a

[00:33]
lot of capabilities coming out around
just giving Claude access to uh use CLIs
and invoke APIs using code and actually
run tools using code instead of MCP. One
of the drawbacks of MCP is that it does
um cause some uh it can cause some
context issues just in terms of
polluting context and taking up a lot of
space. So, there may be some cases where
you can just rely on code execution
either through CLIs or just by giving
Claude the ability to invoke APIs using
code as a means of um creating more
flexibility for your agent where you do
not have to use MCP. So, just something
to keep in mind as you're building.
Great. Okay, so Claude just got done. Um
looks like we have the before and after
from some of the changes that we've made
and I think that this is pretty
compelling, right?
The first thing that jumps off the
screen to me is the token usage. So,

[00:34]
before I was using over 200,000 tokens
for a particular task, after leaning in
on some of those file system primitives,
you can see that that went down
dramatically. This is a direct result of
giving my agent code execution. So
again, imagine instead of giving my
agent a full CSV that needs to be read
into context, I just give my agent the
ability to write and run Python as a
means of kind of navigating across all
of that information. The agent uses a
lot less tokens when it can write code
and then run code and then read the
results instead of having to consume all
of that data in Claude's mind and then
use all of that kind of collective
brainpower to then make decisions based
on the results. Um a few other things.
Um we can see that our cost went down as
well because we're just not using as
many tokens, which makes sense.
Um our our our execution time went down
as well. So, this was a pretty good case
where I think we got better overall, but

[00:35]
this is not something that will happen
all the time, right? We like we might
see some cases where we regress, but
this was the case where using some of
those primitives as opposed to some of
our more stagnant tools was clearly the
uh the right decision.
Great. Okay, we're going to jump back
and we're going to talk about subagents
for just a bit.
I'm going to copy another prompt to
Claude and we are going to um
investigate subagents.
Now, I mentioned before that we had 12
different tools. Three of them were
effectively wrapping subagents. So, if
I'm Claude, I have the ability to call
on a tool, that tool's a wrapper for a
subagent. I can then go and invoke that
subagent.
See, Claude's doing a lot here. I'll
scroll up just a bit and then we'll talk
through it.
The two main use cases
where or the two main instances where we
see subagents initially as being really
effective is first when you want to
throw a lot of Claude at a problem,

[00:36]
right? So, let's say that you're trying
to do deep research or like web search.
Um let's say that you're trying to do in
the case of Claude code code-based
exploration. That's a great case where
like having many different minds running
at the same problem makes sense. So,
subagents are a great way to parallelize
and throw a lot of Claude at a problem
to get it done faster and more
effectively.
The second case where it's really common
to use subagents is when you need a
fresh mind to look at a problem. So, I
use the Claude code example first. If
I'll use my example as a developer, if I
am writing code, I do not want to be the
same person that is writing and also
reviewing my code. I'm going to have
somebody else review my code. So, in the
case of Claude code, it makes a lot of
sense to have one instance of Claude
doing the writing of the code
and then another instance of Claude
coming over the top and reviewing that
that does not have context about the
initial
instance of Claude. This is a great case

[00:37]
for a subagent. Using just a code review
subagent and layering it over the top is
a great way to do this.
We also have a
subagent within
our
our agent here, our inventory management
agent, that we've actually kept as the
result of
of some of the changes that we made and
that's for forecasting specifically. So,
again, I have a forecasting capability
that's within my inventory management
agent. I do want to keep my forecasting
separate from my main instance of
Claude. I don't want anything in my
initial context window to distort the
forecasting process. I do have a skill
that kind of walks through the
step-by-step sequence and the guidelines
that I prefer Claude use when writing
and building forecasts, but again, I
don't want the same Claude that I'm that
my customer is talking with to also be
the Claude that writes the forecast,
right? So, I want to divide that. So,
I'm leaning on that second example of
when to use a subagent as the place

[00:38]
where we'd like to go about doing this.
So, in this case
we've removed our other subagents and
we've just replaced them with primitive
tools,
but we are going to leave the
forecasting subagent. Now, we're not
going to expose our subagent as a tool.
Using Claude managed agents, there's a
native capability for sub agents
um that allows the logging and the
observability of your sub agents um to
be really effective. One of the problems
with sub agents is that when you have
multiple instances of Claude running,
first off, it's difficult to make sure
that the communication between your
orchestrators and your sub agents is
accurate and is seamless, right? There's
a lot that can get lost in translation.
Just like when I'm talking to one of my
colleagues, I might be thinking
something, they might be interpreting it
completely differently. The same thing
happens with orchestrators and sub
agents.
The um

[00:39]
the other thing that can happen is
logging is really difficult in some
cases, right? Because then you have to
worry about collecting the transcripts
from multiple different agents. So,
within Claude managed agents, we've
added this native sub agent capability.
I saw it on here. Let me scroll up just
a bit.
I think Claude found it. Yes. So,
there's this callable agents capability
that exists within Claude managed
agents, which is essentially just like
managed sub agents, so that within your
session information, you have
observability and metrics about what
exactly your sub agents are doing that
is as accurate as your initial
orchestrator.
Right? Um this is again meant to solve
one of the common problems of just
having uh a lot of information that is
hard to track with sub agents.
We did some building. Again, I'm going
to skip through these because we spent
some time talking about them. We just
talked about sub agents. Again, there's
a few different cases where you can use
them. We just talked about callable

[00:40]
agents. You can also just define your
sub agent as a tool, which is what we
did previously, but we actually moved
away from that and we decided to use the
CMA native capability.
Um there are a lot of cases where you
can just now scrap the sub agent
entirely and just give more flexibility
and capability to your main agent. So,
what we have a lot of customers doing is
actually just consuming capability into
their main, in this case, orchestrator,
because frontier models have gotten
intelligent enough to manage across more
information where you just don't need as
many sub-agents. So, again, when you're
thinking sub-agent, I had a lot of cla-
or I have a big problem that I want to
throw a lot of Claude at, or I want a
separate Claude to kind of look at um
the work of either me or of a different
instance of Claude. Two great times to
use sub-agents.
Okay. So, let's look at the architecture
that we ended with. Again, refreshing
us, we started with an orchestrator
system prompt of about 400 lines long.
We had 12 tools, three of them were

[00:41]
sub-agents. What did we end with after
this exercise? We still have an
orchestrator,
but we deployed that on Claude managed
agents because I didn't want to have to
worry about infrastructure, scaling,
security, etc. I just wanted to worry
about my agent, right? Like in in Will's
simple terms, like that is when I reach
for Claude managed agents because I just
want to worry about building the best
thing possible and not all the messiness
that comes with it. We simplified our
tools. We now have uh we have
right now three different tools. So, we
actually simplified everything to just
use bash, read, and write.
>> [snorts]
>> Now, when our agent starts executing, we
sync some data into the Claude managed
agent's environment so that it can
reason across that data.
We actually simplified our system prompt
to 15 lines long, and we replaced all of
our business logic with skills. So,
again, I was just stuffing requirement
after requirement into my system prompt.
I decided to take that, package it up as
skills so that Claude could pull that

[00:42]
information into its brain only when
Claude realized that it needed it in
order to solve a problem.
As a result of this, we showed how we
can then start hill climbing on evals to
see improvements over time.
So at the end of this, my eval score is
about 92%. I've simplified my design.
I'm leaning into some of the primitives
um that make uh Claude great
um and I'm seeing the positive results
after doing so.
Again, some of the eval results, you see
that here after running this, um we're
getting faster, we're using fewer tokens
because we're leaning into code
execution. Um our turn count is
remaining sort of the same, but again,
because the token usage and the cost is
going down, I'm actually okay with
Claude taking more turns. There are some
cases where we'll see the latency not
drop maybe as much as you would expect,
but for some of these more sophisticated
high-intelligence agents where like
forecasting is at play, I'm willing to

[00:43]
take a little bit higher latency um at
the expense of seeing my performance
improve and my costs go down.
All right, let's wrap with some some
takeaways here in our last minute.
When we build agents, we start with a
single agent loop that it that is
equipped with very simple primitives
that give Claude some of these
human-like capabilities like the ability
to use the file system like the one that
you have on your computer, web search,
code execution,
um
sometimes a to-do list. Again, we start
there and then we build accordingly.
The next thing that we did is we use
progressive disclosure through skills.
Instead of stuffing our system prompt
with a lot of information, we made
information accessible to Claude
whenever Claude realized that it needed
that information in order to solve a
problem. This is great because we can
run more efficiently
and uh we're not polluting our context

[00:44]
window um and we're giving Claude more
flexibility to make decisions. The last
thing that I want you to walk away with,
write evals in general. This idea of
hill climbing is a concept that we lean
on really heavily at Anthropic. Right,
you have evals as you establish a
baseline, you then tweak your
architecture and you rerun evals and you
get better over time. Now, as a result,
it's important to make sure that your
evals are updated as your product
capability expands. Always make sure
that your evals are encompassing the
things that you care about and that
you're measuring within your agent so
that you can actually make sure that
your agent is accomplishing the thing
that you set out to accomplish.
With that, folks, we're going to go
ahead and wrap. I really appreciate your
time today.
I'll be in the back after the session
just outside of this room in case you
have any questions at all.
Thank you for spending your day at Code
with Claude in London. I hope you have a
great rest of your day. Appreciate it.
>> [music]

</details>
