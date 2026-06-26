<!-- source: https://claude.com/blog/product-management-on-the-ai-exponential -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2287f90c57df4c9dd97_c1ef4c0b6882dfe985555b52999d370ea88a3c50-1000x1000.svg)

# Product management on the AI exponential

Claude Code’s Head of Product Cat Wu shares how product management teams are adapting their workflows and roadmaps in the face of rapidly evolving model intelligence.

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  Claude Code
* Date

  March 19, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/product-management-on-the-ai-exponential

Since [Claude Sonnet 3.5 (new)](https://www.anthropic.com/news/3-5-models-and-computer-use) in October 2024, I made a habit of testing every new model by asking Claude Code (an internal tool at the time) to add a table tool to Excalidraw. With each new model, Claude got a little further but still failed.

Then, with the release of [Opus 4](https://www.anthropic.com/news/claude-4) in June 2025, Claude started occasionally succeeding, enough that we turned the exercise into a [pre-recorded demo](https://www.youtube.com/live/EvtPBaaykdo?t=3478s) for the Claude 4 model launch to show what had become possible with our latest model.

Less than a year later, [Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6) can one-shot Excalidraw feature requests reliably enough that we feel comfortable doing it live, in front of thousands of professional developers.

The speed of model progress keeps expanding what's possible. The traditional product management playbook is built on the assumption that what's technologically possible at the start of a project is roughly what's possible at the end. PMs would gather enough information upfront to make confident bets about the future, then execute against a plan over the course of months.

Exponentially improving models break that assumption. The constraints you designed around might disappear mid-project. You're building on ground that's rising underneath you, and teams need to reorganize around that reality. The new product management rhythm is rapid experimentation, consistent shipping, and doubling down on what works.

Not surprisingly, one of the most common questions I get as a product manager at Anthropic is how our role is changing. Here's what I've learned.

## My journey to product management with Claude Code

I started my career as a product engineer at startups like Scale AI and Dagster, and then became a venture capitalist, a role in which I still wrote code to automate the tedious parts of my job, like scanning X for the announcement of new companies or detecting when open source projects were gaining momentum.

I joined Anthropic in August 2024 as a product manager on the Research PM team, which bridges our research team and real-world customers to deliver better models. When Claude Code became available internally that fall, I used it to accelerate the more manual parts of my job, including building Streamlit apps to analyze large-scale user feedback and running evals to help the company find new benchmarks to trust. The low barrier to building also meant I could explore well beyond my usual role, like creating RL environments to better understand training.

These projects took hundreds of hours of prompting Claude Code powered by Sonnet 3.5 (new), but not a single line of code written by hand.

## Designing a new product management workflow

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69bc295c981804a6cc75ded9_fig1-claude-code-pm-playbook-on-the-ai-exponential-v4%402x.png)

Tools like Claude Code and Cowork are blurring the lines between distinct roles in the product development life cycle.

Claude Code isn’t the only tool powering my workflow. Over time, I've settled into a natural division of labor across three products: a chat collaborator ([Claude.ai](http://claude.ai)), agentic coding tool (Claude Code), and a knowledge work tool ([Cowork](https://www.anthropic.com/webinars/future-of-ai-at-work-introducing-cowork)).

**Claude.ai** is where I talk to Claude as a thought partner without needing it to take action. I bounce ideas for strategy docs, how to handle tricky situations, and get quick answers.

**Claude Code** is where I build prototypes, evals, and scripts, many of which call Claude API. I use this when the output is code.

**Cowork** is where I do everything else, from getting to inbox zero, tracking and acting on a todo list, creating slide decks, understanding the history of a decision by searching Slack, and booking my work travel.

I’ve talked with product managers across the industry who've found their own versions of this workflow:

> *“Claude has raised the ceiling on what good product teams can build, and dramatically shortened the distance between idea and prototype. Getting something tangible in front of customers used to take weeks of building. Now I'll start in Claude Cowork, pulling in context from Slack, our codebase, and docs, then move into Claude Code to have something demo-able in a couple of hours. Good product teams have always tested their ideas with real customers, and that instinct hasn't changed. What has is how many more high-quality ideas we can actually put through the loop.” - Bihan Jiang, Director of Product, Decagon*

> *“To me, being a PM in an AI-native world is both creative and academic. Each new model release changes what’s possible, and in building Datadog’s Bits AI SRE agent we study its strengths and failure modes through offline evaluation on real-world production incidents. We also design tight feedback loops, refining the UX to surface where the agent struggles and turning those insights into product improvements. In that sense, a PM’s craft has shifted from defining certainty upfront to accelerating discovery.” - Kai Xin Tai, Senior Product Manager, Datadog*

One of the most exciting parts of being a product manager today is that these workflows are constantly evolving and giving us more leverage.

## Leaning into the AI exponential

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69bc2f892ac8ae5b32d2ac32_Screenshot%202026-03-19%20at%201.16.39%E2%80%AFPM.png)

*METR. (2026, March). Task-Completion Time Horizons of Frontier AI Models.* [*https://metr.org/time-horizons/*](https://metr.org/time-horizons/)

METR [finds](https://metr.org/time-horizons/) that, about half the time, Opus 4.6 can complete software tasks which take humans almost 12 hours. When we first started building Claude Code, Sonnet 3.5 (new) was the frontier model and METR measured that it could do tasks that would take a human around 21 minutes. That's a roughly 41x jump in 16 months.

The Claude Code team has evolved to keep pace with how quickly models improve. Our roles are blending together: designers ship code, engineers make product decisions, product managers build prototypes and evals. This works because clear strategy and goals let everyone prioritize autonomously. The product manager’s job is to create clarity in the ambiguity that rapid model progress creates, push the team to think bigger about what’s possible, and clear the path to shipping faster.

Here are four shifts we’ve embraced:

**Plan in short sprints**

Traditional product manager thinking treats exploration as something that happens before the roadmap gets locked. You do your research, you write the PRD, and you hand it off for the engineering team to build.

Instead of a long-term roadmap, we encourage everyone on the team (engineers, product managers, designers) to take on side quests. A side quest is a short self-directed experiment you run outside your official roadmap—an afternoon spent prototyping an idea, testing a capability you assumed was out of reach, or just seeing what happens when you push the model harder than you expect to.

Some of Anthropic’s most popular features—[Claude Code on Desktop](https://code.claude.com/docs/en/desktop), the [AskUserQuestion tool](https://platform.claude.com/docs/en/agent-sdk/user-input), and [todo lists](https://platform.claude.com/docs/en/agent-sdk/todo-tracking)—emerged this way.

**Encourage demos and evals over docs**

Our team has largely replaced documentation-first thinking with prototype-first thinking. Instead of hosting traditional stand-ups, we share demos of new ideas. Internal users try them, and the ones with real engagement get polished and shared more broadly. Because you can prototype in an afternoon, wrong bets are cheap.

For example, when Noah shared his [plugins](https://code.claude.com/docs/en/plugins) spec with Claude Code, the prototype that came back was close to production ready. That prototype anchored what the team ultimately shipped since it enabled the team to quickly validate the UX.

Pro-tip: after you write a spec, send it to Claude Code and see if it can build it. Even a rough prototype changes the conversation.

In addition to demos, evals can also help make an abstract product feel more concrete. For example, for [agent teams](https://code.claude.com/docs/en/agent-teams) which lets users coordinate multiple Claude Code instances working together, Conner hand-crafted a set of evals to understand when agent teams work well, when they don’t, and what to fix. Measuring whether the feature is working makes it easier to improve it.

**Revisit features with new models**

Now, you ship a feature, then a better model comes out and your feature could be dramatically better. Every model release is an implicit prompt to revisit what you've already built.

The best way to catch these moments is to be a daily active user and deliberately ask it to do things you think might be too hard. Sometimes it works, and that’s a signal that the product needs to catch up.

That’s how [Claude Code with Chrome](https://code.claude.com/docs/en/chrome) happened. We noticed users were building web apps with Claude Code and then manually switching to Claude in Chrome to test it. Users were manually prompting and copying and pasting instructions between these two tools. It worked well enough that we realized this should be a built-in feature. If users are hacking something together, that’s scaffolding you can build into the product.

When prototyping these ideas, always optimize for capability first. Use more tokens than you think you need. It's a common mistake to cut token costs too early and ship something much less capable as a result. You can always bring costs down later as cheaper models catch up, but first you need to know whether the feature is even possible.

**Do the simple thing**

At Anthropic, we have a guiding principle across every team: do the simple thing that works.

If your product cleverly works around a model limitation, that workaround becomes unnecessary complexity when the next model drops. That's why "do the simple thing" matters: the simpler your implementation, the easier it is to swap in new capabilities when they arrive.

When we first launched todo lists in Claude Code, the model wouldn't reliably check off items as it completed them. So we added system reminders every few messages that would periodically nudge the agent to update its own todo list. It worked, but it was a hack. With the next model, the behavior came for free and we removed the reminders entirely. We've seen this pattern repeatedly: our system prompt and tool descriptions used to be heavily engineered to compensate for model limitations, and we've been able to cut the prompting with each model, including a 20% reduction for Opus 4.6.

## Looking forward

Many product managers are used to having tight control over the full product experience, but AI pushes you to let go in order to move quickly. When it comes to building AI products in particular, it feels like surfing a wave where the most important thing is to stay on it. As a perfectionist, this was the hardest shift for me to get comfortable with, but the product manager’s role is now to identify the handful of true non-negotiables and let the rest go.

The net effect of these shifts is that product teams can move significantly faster. When a product manager can go from idea to working prototype in an afternoon, the gap between “what if we tried…” and “here, try this” nearly disappears.

At Anthropic, product managers aren’t the only ones transforming their workflows with Claude. Our data science, [finance](https://www.anthropic.com/webinars/claude-code-financial-services), marketing, [legal](https://www.youtube.com/watch?v=tJP6SKfo49c), and [design teams](https://www.youtube.com/watch?v=vLIDHi-1PVU) picked up these tools on their own. The whole organization moves at the same speed instead of waiting on handoffs.

<!-- yt-inline:tJP6SKfo49c -->
[![How Anthropic uses Claude in Legal](https://img.youtube.com/vi/tJP6SKfo49c/hqdefault.jpg)](https://www.youtube.com/watch?v=tJP6SKfo49c)

<details>
<summary>📺 자막: How Anthropic uses Claude in Legal (3:40)</summary>

[00:00]
This is
a legal lamp. That's what we call it.
And I was working on a project
to learn more about how Claude Code works.
And so I was trying to
think of a fun project that would sort of
make my desk come to life more.
And now I can type a message
and ask this lamp to blink in Morse code.
It says it's thinking it's going to do
four quick blinks and two quick blinks,
which is H. I.
Abracadabra.
It's kind of magical. I'm not an engineer.
I'm non-technical.
I don't know how to code.
But with Claude Code,
you don't have to know how to code.
And you can just kind of talk to it
in plain language. And.
No lawyer
likes doing the same repetitive exercise
over and over and over again.
The work can be dull.
You can make mistakes before Claude.
I had a ton of busywork.
Things I would put off
to the end of the day, because I just knew
it'd take a lot of time,
but not using the best parts of my brain.
So we put our heads together and realized
we might be able to use Claude to help

[00:01]
get our best work done and build
workflows.
It used to be that the marketing team
would reach out to me, maybe a day before
a launch and say, hey, we've got this
really exciting launch happening tomorrow.
We're so sorry.
The blog post just came together.
We need you to quickly read this and flag
anything that might be problematic.
So, I asked,
Claude wants to just build me a workflow.
Here's what I care about.
And to my surprise, Claude
just ran with it and set it up.
If I were a marketer and I needed to get
one of my blog posts reviewed,
I would open up this link
to the Marketing Materials Software
review tool,
which is pinned in my channel.
I would cut and paste.
So let me copy their blog post.
I'm going to go back to the review tool.
I'm going to paste all that content
and then I'm going to click
the Analyze Content button.
And this is going to send Claude off
on its journey reviewing my material.
There we have it.
Review results.
Claude is identified
five issues to address.
So it wants to make
sure I focus on accuracy.

[00:02]
It wants to review the security claims,
wants to make sure we have publicity
rights on third
party content,
as well as partnership considerations.
And it gave me props.
It said what looks good
clear the feature descriptions.
Comprehensive integration
details, specific use cases.
Here are the items that require
legal tickets.
Review.
I'm going to click on Generate
Slack message for legal team.
And Claude has now summarized the issues
here.
I'm going to click on Copy the Clipboard
and I'm going to click
go to Legal Tickets to file on my ticket.
To tee it up for legal review,
it identifies the most important issues.
It helps me prioritize.
Sort of has like a low, medium, high risk
level signal.
That's based on a framework
that I gave it.
So it's kind of acting as my eyes
and ears to that first pass.
As we build these types of automations
and in new workflows, I'm always trying
to ensure that a human remains in the loop
from the legal team.
We know that AI systems
can still hallucinate.
I'm still making sure
I'm reviewing the work.

[00:03]
But this is really helping us move
with more speed and sort
of preemptively flagging things
within the legal department.
We're using Claude
in so many different ways.
So we're using it to do redlining
exercises and commercial, matters.
We're using Claude to help us,
with our conflict of interest
policy and reviewing outside business
activity requests.
When people reach out to me and ask,
how do I get started?
I tell them to think of their most routine
work.
Just open up Claude and give it a shot.
You really don't know what it's capable of
doing until you give it a shot.

</details>


<!-- yt-inline:vLIDHi-1PVU -->
[![Designing Claude Code](https://img.youtube.com/vi/vLIDHi-1PVU/hqdefault.jpg)](https://www.youtube.com/watch?v=vLIDHi-1PVU)

<details>
<summary>📺 자막: Designing Claude Code (12:03)</summary>

[00:00]
- Hi, I'm Alex.
I lead Claude Relations here at Anthropic.
Today we're talking about
design for Claude Code
and I'm joined by my colleague Meaghan.
- Hi, my name is Meaghan
and I'm the design lead for Claude Code.
- Meaghan, I wanna start with
the very unique form factor
that Claude Code has.
So, we built this coding product
and it lives within a terminal.
Can you tell me how we even got to that?
- Yeah, yeah, definitely.
Well, if you've seen some
of our previous videos,
you know that Claude
Code was a brain child
of a few folks here at Anthropic
who are really passionate
about Claude's ability
to solve coding problems
and help developers.
And, part of the initial decision for CLI
was really just the
ease of the form factor
to be able to build really quickly
and to iterate on features
and functionality.
But I think from there, really,
kind of against honestly my expectations
and all our expectations,
it took a life of its own
because it's just so versatile.

[00:01]
Like, a terminal is in
every developer's workflow.
Whether or not you're primarily in IDE
or even if you're just like a Vim user,
you're using terminal as part
of your workflow in one shape or another.
And so, it lets you
really integrate directly
into developer's workflow,
where they are today without needing
to adopt a new tool of any sort.
- I think that's like a really good point
is like the terminal's kind
of been a foundational piece
of software development since,
man, since forever basically,
as long as we've been doing this.
So it's almost natural to kind
of embed the next generation
of a coding product within it.
But Claude Code does some things
that I didn't even know were
possible with a terminal.
So, maybe like, walk me through
what has kind of the history been
of terminal products thus far,
and how is Claude Code
like the next step there?
- Yeah, this is something I'm personally,
very, very passionate about.
I think terminals are like the
first user interface, right?
Like, they're the first
ways that people used
to talk to computers.
They were text-only.
There were like very
specific commands you needed
to know in order to be able to
interface with these devices.
And they're like a super-powered tool.

[00:02]
And then, kind of from there,
we evolved into these
really rich web interfaces.
We had like all these beautiful web UI,
we had like Tailwind, we had
like CSS, we had JavaScript,
everything became very
animated and very polished.
But then when LLMs came out,
we actually went all the way back
to just chatting with a computer again.
Like, you didn't actually
need all these buttons,
you just needed to chat.
And so I think terminal, interestingly,
is actually the perfect
form factor for an LLM.
'Cause you're giving text
in, you're getting text out,
and it just is like so native
to how you think about using
like a command line interface
that it was like a
beautiful marriage, I think,
of like what the technology can do
and what the product can do.
And then it just happened to be
that developers also spend
their time there, so it's great.
- I see.
So we're almost like going
full circle to some degree,
because the model allows
us to do it in some sense
and removes the need
for the UI abstractions
that we've had to develop previously
for different applications.
- Mm hm. Mm hm.
Exactly. Exactly.
I also think big part
of why I think Claude Code
is successful is, you know,

[00:03]
no one likes copying and pasting things,
from like a web UI to
like your local file.
Like, I definitely do this all the time
when I'm using Claude AI.
And so being able to be like
natively in the environment
where everything lives
is just such a rich
part of the experience.
But it does come with some challenges.
You know, CLI is not necessarily
the most rich interaction surface.
- Mm.
Let's talk more on that workflow piece
because I remember very vividly
when I was first using Claude
and using language models
for programming, and I would
be on the website on claude.ai
and type in a prompt and paste in a file,
then all of a sudden I'd get a code output
and I have to copy it, find
my file on my local computer,
paste it in, make the
edits myself manually.
And now, we've kind of
taken out that piece
of the developer workflow
and gone straight
from the prompt to the
direct edits on the file.
- Mm hm.
- Can you tell me a little bit more
about how we're thinking
about future iterations
of this dev workflow and this
dev loop within Claude Code?
- Mm hm. Mm hm.
Absolutely.
I think the way that I've
been thinking about it

[00:04]
within the team, and a lot
of folks will talk about it,
is, you know, the developer
workflow initially started
as writing lines of code.
Like you're at a word level,
you're at a function level
and like that's where you spend time.
And then the first
really big AI development
for coding was tab to auto complete.
But that's still not a line level of code.
When we get to kind of the
first-generation of Claude Code,
we're up-leveling it to
like full file changes
or like full task changes,
almost like a PR level.
And of course, there are some things
that Claude Code can do better or worse,
but we're trying to kind
of move in that direction.
As time goes on, as our
models get more intelligent,
as our capabilities get stronger,
I think we're gonna be moving
not just from a specific task,
but almost to like a project level,
where you're orchestrating
multiple Claudes
from multiple places in order
to be able to accomplish something.
And I think the tasks
will be longer running
and the Claude will be
a lot more autonomous.
And so, you'll just get into a place
where I do believe eventually,
well, we might outgrow the CLI,
but also you're operating at
a higher order of workflow

[00:05]
than you ever were before as a developer.
- Mm, okay.
Related to the agent front,
I know that we just
recently, a few weeks ago,
put out subagent a product.
Can you talk more about that
and how this kind of
paradigm of slash commands
and subagent workflows and
some of the other features
that we've shipped under
the hood of Claude Code,
how do those all tie together?
- Yeah, definitely.
So I think part of the
reason terminal is so great
is because it has a built-in architecture
of how you control the interface, right?
You have your flags that you
put in as you launch Claude,
and then you have your commands
that you have within kind of a terminal.
And we introduced a very new paradigm,
which is prompting in the terminal.
There was so much debate.
I even have a doc that I have with Boris
from like I think November,
December of last year
of like, we can't put outlines in terminal
because when you resize the window
it's gonna break everything.
Every experience I've
ever had with designing
for CLIs before, I like avoid
outlines like the plague
because it breaks everything
when you have that much-
- What is an outline?

[00:06]
- It's like the outline
around the input box-
- Oh, I see, yeah.
- That you have right now.
You tend to avoid those in CLI design
because when you resize,
it's all just characters
and spaces.
- Right.
- And so it doesn't align properly.
But Boris had a vision and I was wrong.
Like, we found a great
library and a great interface
and the team worked really
hard to make it usable.
And so the combination of being able
to separate your prompting,
which is how you're talking to the model,
and then the tools that
you have available,
which is our slash commands,
and the settings and the
way you configure it,
which is in our settings.json
and our CLAUDE.md,
I think that's kind of the architecture
that I think powers Claude Code,
but also is just part
of the regular architecture
of software development.
Like a README file is very similar,
so it just pairs really beautifully.
- Mm.
How do we actually design new things
like the outline box or
just the visual aesthetics?
Do we have design principles we follow?
Is there rules or, just walk
me through that process.
- Yeah, definitely.
I would say everyone is an
inventor here at Anthropic

[00:07]
and at the Claude Code team.
So, for the most part, it's
a small team of like one
or two engineers coming up with ideas
and then prototyping them
and then we rigorously
test 'em internally.
For the most part, they are used
by all of, everyone at Anthropic,
everyone uses Claude Code.
And so, that's where we
get a lot of our feedback.
And then we'll typically
do a cycle of UX polish
towards the end when we feel
like we have the right shape
of what this technology should be.
Subagents was a really fast one,
where it went from like an idea to lend
and there was a little
bit of design polish
on like how we show a subagent
and differentiate from like
a subagent versus Claude,
how you set it up.
Same thing with MCP.
But the big principles I think that I hold
and push for very dearly is, you know,
a CLI is a very limited interface.
We need to keep it clean as possible,
and so we wanna make sure
that we're not flooding it
with a lot of information and
just keeping it really focused
on the task that you're doing.
The second is that we really
want the model to shine
because at the end of the day,
part of the reason CLI is so nice

[00:08]
is that it's the thinnest wrapper possible
around our models.
And so you just get access to
the raw capability of Claude
and that's honestly what
makes Claude Code so powerful.
- Mm.
Do you have any favorite
little design polishes
or things that, touches in Claude Code?
- I definitely do.
I really like the ASCII
reticulating and thinking.
I think those are such a great point
of personality for Claude.
And I also really, really
like the different modes,
how we've like outlined if
you're in thinking mode,
or planning mode, or auto-accept mode,
I think it's just a very rich way
to communicate complex information
in a way that people can understand.
- I agree.
And I love the personality
touches as well.
It feels like, sometimes
programming and the process
of programming can be
like a robotic thing.
You know, you're dealing
with lines of code
and lots of characters, but
when you're using Claude Code,
it's almost like a different experience
and it kind of elicits a different emotion
than just like if I'm in an IDE
and I'm just typing
line after line of code.
- Yeah, definitely, definitely.
I think there's actually a lot
of really rich things
you can do in terminal,
and sometimes it's even
about pulling us back.

[00:09]
It's like, "Oh, actually we
don't need to over design this.
We can just let the
model take care of it."
- I see.
- Because it is really
great at it, honestly.
- That's, that's great.
I'm really curious to
hear some of your tips
and best practices for using Claude Code,
especially as a designer
and not a traditional technical person.
How do you best use
Claude Code day-to-day?
- I love this question.
It's something I'm personally
very passionate about.
I am a product designer.
I will be the first to admit
that I should not be writing any code
and any code I write is
definitely vibe coded
and should be reviewed.
But Claude Code and
all these coding agents
have what I consider
unlocked a new skill set,
or like a new skill tree
for non-technical folks.
Where before, I would
need to maybe request time
for a software engineer, or
kind of let some things go
if it didn't necessarily make it
to the right level of priority.
I now have a new set to
reach into to do it myself.
And so, the two big axes
that you'll hear a lot,
like designers talking about,
the first one is the
cost of an idea is zero.

[00:10]
You can prototype very, very quickly.
And I think that's interesting,
but it's actually not the
most exciting unlock for me.
I think the more exciting unlock
is I can actually push code to production.
I can make the changes that I want.
I'm in the live code base itself.
And so, some of the most common use cases
that I do almost on the daily is
if I'm designing a new feature,
I'll actually brainstorm
with Claude Code at first.
I'll be like, "What are the
most common use cases here?
What are the edge states
that I should think about?
How would you design this, maybe?"
And then I'll do some
iterations from there.
I also ask Claude Code sometimes
to help me scope designs
that I've proposed.
I'll like drag and drop it as an image.
I'll be like, "Hey,
how long do you think
it'll take to make this?"
And Claude will give me
estimates so I can, you know,
friendly debate with the engineers,
how long it'll actually
take to build something
and we get to a good compromise.
And then the last one is, you know,
when you're launching a new product,
you often don't really
get to do the last 2%
of design polish you always want to do.

[00:11]
And, that's no longer true,
because I can just go in there
once the engineers are done
and in the last day before launch,
or even in the few days after launch,
I will go up and clean up all those
things that are P2s-
- Wow. Yeah.
- That I really wanted
to happen in the product.
- Wow, that's amazing.
I love that.
And those are awesome tips.
It's kind of exciting to hear about
this almost convergence
almost of like the designer
and the engineer into
this design engineer,
I guess in some sense,
because of Claude Code and what it allows.
- Yeah, absolutely.
And I think one thing
that it's actually done,
surprisingly for me, is
it's made my partnership
with my engineers a lot
better because there's a lot
of things I honestly can't
do on my own right now.
But, even making a first attempt
and then going and
chatting with the engineer,
it makes our collaboration
a lot stronger as well.
So it's not just like
giving you a new skill set,
it's also helping you collaborate
better with your partners,
which I think is a really important part
of this kinda whole cycle
we're building out right now.
- I agree.
That's great.
Well, Meaghan, this has been awesome.
I really appreciate the conversation.

</details>


The PM role now is to track both things at once: how AI is changing the way you work, and how it's changing what's possible in your product. Do that well, and you stop being surprised when the table tool finally works. You're the one who saw it coming.

*Start building better products with* [*Claude Code*](https://code.claude.com/docs/en/overview)*.*

‍

***Acknowledgments:****This article was written by Cat Wu, the Head of Product for Claude Code at Anthropic. You can find her on* [*X*](https://x.com/_catwu) *and* [*LinkedIn*](https://www.linkedin.com/in/cat-wu/)*. She'd like to thank Bihan Jiang and Kai Xin Tai for their contributions to this piece.*

‍

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225588ad176f7c4aafd_abc884c723daea810d2e986455358281a2f94102-1000x1000.svg)

Jun 24, 2026

### Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

Claude Code

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](#)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](/blog/agent-identity-access-model)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

Jun 3, 2026

### Running an AI-native engineering org

Claude Code

[Running an AI-native engineering org](#)Running an AI-native engineering org

[Running an AI-native engineering org](/blog/running-an-ai-native-engineering-org)Running an AI-native engineering org

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

May 12, 2026

### How Anthropic's cybersecurity team built a threat detection platform with Claude Code

Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](#)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](/blog/how-anthropic-uses-claude-cybersecurity)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2222403b092e0358b0e_cd4fd51deacd067d4e30aee4f4b149f6cba1b97b-1000x1000.svg)

Apr 20, 2026

### Meet the winners of our Built with Opus 4.6 Claude Code hackathon

Claude Code

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](#) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

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
