<!-- source: https://www.anthropic.com/news/claude-sonnet-4-5 -->

# Introducing Claude Sonnet 4.5

Sep 29, 2025

![Introducing Claude Sonnet 4.5](https://www-cdn.anthropic.com/images/4zrzovbb/website/a683fdcfe3e2c7c6532342a0fa4ff789c3fd4852-1000x1000.svg)

Claude Sonnet 4.5 is the best coding model in the world. It's the strongest model for building complex agents. It’s the best model at using computers. And it shows substantial gains in reasoning and math.

Code is everywhere. It runs every application, spreadsheet, and software tool you use. Being able to use those tools and reason through hard problems is how modern work gets done.

Claude Sonnet 4.5 makes this possible. We're releasing it along with a set of major upgrades to our products. In [Claude Code](https://anthropic.com/news/enabling-claude-code-to-work-more-autonomously), we've added checkpoints—one of our most requested features—that save your progress and allow you to roll back instantly to a previous state. We've refreshed the terminal interface and shipped a [native VS Code extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code). We've added a new [context editing feature and memory tool](https://anthropic.com/news/context-management) to the Claude API that lets agents run even longer and handle even greater complexity. In the Claude [apps](https://claude.ai/redirect/website.v1.27bda13e-87f6-45cc-b8d2-4d85ad734b61/download), we've brought code execution and [file creation](https://www.anthropic.com/news/create-files) (spreadsheets, slides, and documents) directly into the conversation. And we've made the [Claude for Chrome](https://www.anthropic.com/news/claude-for-chrome) extension available to Max users who joined the waitlist last month.

We're also giving developers the building blocks we use ourselves to make Claude Code. We're calling this the [Claude Agent SDK](https://anthropic.com/engineering/building-agents-with-the-claude-agent-sdk). The infrastructure that powers our frontier products—and allows them to reach their full potential—is now yours to build with.

This is the [most aligned frontier model](https://www.anthropic.com/claude-sonnet-4-5-system-card) we’ve ever released, showing large improvements across several areas of alignment compared to previous Claude models.

Claude Sonnet 4.5 is available everywhere today. If you’re a developer, simply use `claude-sonnet-4-5` via [the Claude API](https://docs.claude.com/en/docs/about-claude/models/overview). Pricing remains the same as Claude Sonnet 4, at $3/$15 per million tokens.

## Frontier intelligence

Claude Sonnet 4.5 is state-of-the-art on the SWE-bench Verified evaluation, which measures real-world software coding abilities. Practically speaking, we’ve observed it maintaining focus for more than 30 hours on complex, multi-step tasks.

![Chart showing frontier model performance on SWE-bench Verified with Claude Sonnet 4.5 leading](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6421e7049ff8b2c4591497ec92dc4157b2ac1b30-3840x2160.png&w=3840&q=75)

Claude Sonnet 4.5 represents a significant leap forward on computer use. On OSWorld, a benchmark that tests AI models on real-world computer tasks, Sonnet 4.5 now leads at 61.4%. Just four months ago, Sonnet 4 held the lead at 42.2%. Our [Claude for Chrome](https://www.anthropic.com/news/claude-for-chrome) extension puts these upgraded capabilities to use. In the demo below, we show Claude working directly in a browser, navigating sites, filling spreadsheets, and completing tasks.

The model also shows improved capabilities on a broad range of evaluations including reasoning and math:

![Benchmark table comparing frontier models across popular public evals](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F67081be1ea2752e2a554e49a6aab2731b265d11b-2600x2288.png&w=3840&q=75)

Claude Sonnet 4.5 is our most powerful model to date. See footnotes for methodology.

Experts in finance, law, medicine, and STEM found Sonnet 4.5 shows dramatically better domain-specific knowledge and reasoning compared to older models, including Opus 4.1.

FinanceLawMedicineSTEM

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7175bc18c46562f1228280a7abda751219a2aae1-3840x2160.png&w=3840&q=75)

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffd313a5edb996d98b9fc73ee5b3e6a34fbbcbb83-3840x2160.png&w=3840&q=75)

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F442f96fd96de39e3ff3a05b288e2647dd7ec2f58-3840x2160.png&w=3840&q=75)

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F711e6e1178f0ed7ca9aa85a5e0e9940a807c436a-3840x2160.png&w=3840&q=75)

The model’s capabilities are also reflected in the experiences of early customers:

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/464cf83cd04ad624fee1730a71914b18e89cdf9b-150x48.svg)

> **We're seeing state-of-the-art coding performance from Claude Sonnet 4.5**, with significant improvements on longer horizon tasks. It reinforces why many developers using Cursor choose Claude for solving their most complex problems.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/7715b118c5eb0ff2a85f1f7914bce8c634ecacbd-150x48.svg)

> **Claude Sonnet 4.5 amplifies GitHub Copilot's core strengths**. Our initial evals show significant improvements in multi-step reasoning and code comprehension—enabling Copilot's agentic experiences to handle complex, codebase-spanning tasks better.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/daef759120b29e4db8ba4a5664d7574750964ab9-150x48.svg)

> **Claude Sonnet 4.5 is excellent at software development tasks**, learning our codebase patterns to deliver precise implementations. It handles everything from debugging to architecture with deep contextual understanding, transforming our development velocity.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/eb96f772e9ae5e340de41e6b07f3c6d50b3fff22-150x48.svg)

> Claude Sonnet 4.5 **reduced average vulnerability intake time for our Hai security agents by 44% while improving accuracy by 25%**, helping us reduce risk for businesses with confidence.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/8cbf56e184dd5174705a0f55cb91b0af545982ff-150x48.svg)

> **Claude Sonnet 4.5 is state of the art on the most complex litigation tasks.** For example, analyzing full briefing cycles and conducting research to synthesize excellent first drafts of an opinion for judges, or interrogating entire litigation records to create detailed summary judgment analysis.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/431e098a503851789fa4508b88a0418853f513eb-150x48.svg)

> Claude Sonnet 4.5's edit capabilities are exceptional — **we went from 9% error rate on Sonnet 4 to 0% on our internal code editing benchmark**. Higher tool success at lower cost is a major leap for agentic coding. Claude Sonnet 4.5 balances creativity and control perfectly.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/66e0000e396aea64ea31ed3fea7b2b20ac329312-150x48.svg)

> Claude Sonnet 4.5 delivers impressive gains on our most complex, long-context tasks—from engineering in our codebase to in-product features and research. **It's noticeably more intelligent and a big leap forward**, helping us push what 240M+ users can design with Canva.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/cdec0ff1244295571db38838e90f61c47681d63d-150x48.svg)

> **Claude Sonnet 4.5 has noticeably improved Figma Make in early testing**, making it easier to prompt and iterate. Teams can explore and validate their ideas with more functional prototypes and smoother interactions, while still getting the design quality Figma is known for.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/094b76abf3e64453c224e12ae388b8008b02660e-150x48.svg)

> **Sonnet 4.5 represents a new generation of coding models**. It's surprisingly efficient at maximizing actions per context window through parallel tool execution, for example running multiple bash commands at once.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/6e418ccebe0a1d6fd13f21094852b080a0c93ae5-150x48.svg)

> For Devin, Claude Sonnet 4.5 increased planning performance by 18% and end-to-end eval scores by 12%—**the biggest jump we've seen since the release of Claude Sonnet 3.6**. It excels at testing its own code, enabling Devin to run longer, handle harder tasks, and deliver production-ready code.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/5a7dfab326b449aedc0d11053f9d42f48951ae7e-150x48.svg)

> **Claude Sonnet 4.5 shows strong promise for red teaming**, generating creative attack scenarios that accelerate how we study attacker tradecraft. These insights strengthen our defenses across endpoints, identity, cloud, data, SaaS, and AI workloads.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/b0b6b40b55f3aa73e8a32ce81f9bb927134fd3da-150x48.svg)

> Claude Sonnet 4.5 resets our expectations—**it handles 30+ hours of autonomous coding**, freeing our engineers to tackle months of complex architectural work in dramatically less time while maintaining coherence across massive codebases.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/4fcce1a2389ddafa9f3302c51960e1ff4bfbd3d7-150x48.svg)

> For complex financial analysis—risk, structured products, portfolio screening—Claude Sonnet 4.5 with thinking **delivers investment-grade insights that require less human review**. When depth matters more than speed, it's a meaningful step forward for institutional finance.

01 / 13

## Our most aligned model yet

As well as being our most capable model, Claude Sonnet 4.5 is our most aligned frontier model yet. Claude’s improved capabilities and our extensive safety training have allowed us to substantially improve the model’s behavior, reducing concerning behaviors like sycophancy, deception, power-seeking, and the tendency to encourage delusional thinking. For the model’s agentic and computer use capabilities, we’ve also made considerable progress on defending against prompt injection attacks, one of the most serious risks for users of these capabilities.

You can read a detailed set of safety and alignment evaluations, which for the first time includes tests using techniques from mechanistic interpretability, in the Claude Sonnet 4.5 [system card](https://www.anthropic.com/claude-sonnet-4-5-system-card).

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F33efc283321feeff94dd80973dbcd38409806cf5-3840x2160.png&w=3840&q=75)

Overall misaligned behavior scores from an automated behavioral auditor (lower is better). Misaligned behaviors include (but are not limited to) deception, sycophancy, power-seeking, encouragement of delusions, and compliance with harmful system prompts. More details can be found in the Claude Sonnet 4.5 [system card](https://www.anthropic.com/claude-sonnet-4-5-system-card).

Claude Sonnet 4.5 is being released under our AI Safety Level 3 (ASL-3) protections, as per [our framework](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy) that matches model capabilities with appropriate safeguards. These safeguards include filters called classifiers that aim to detect potentially dangerous inputs and outputs—in particular those related to chemical, biological, radiological, and nuclear (CBRN) weapons.

These classifiers might sometimes inadvertently flag normal content. We’ve made it easy for users to continue any interrupted conversations with Sonnet 4, a model that poses a lower CBRN risk. We've already made significant progress in reducing these false positives, reducing them by a factor of ten since [we originally described them](https://www.anthropic.com/news/constitutional-classifiers), and a factor of two since Claude Opus 4 was released in May. We’re continuing to make progress in making the classifiers more discerning1.

## The Claude Agent SDK

We've spent more than six months shipping updates to Claude Code, so we know what it takes to [build](https://www.youtube.com/watch?v=DAQJvGjlgVM) and [design](https://www.youtube.com/watch?v=vLIDHi-1PVU) AI agents. We've solved hard problems: how agents should manage memory across long-running tasks, how to handle permission systems that balance autonomy with user control, and how to coordinate subagents working toward a shared goal.

<!-- yt-inline:DAQJvGjlgVM -->
[![Building and prototyping with Claude Code](https://img.youtube.com/vi/DAQJvGjlgVM/hqdefault.jpg)](https://www.youtube.com/watch?v=DAQJvGjlgVM)

<details>
<summary>자막: Building and prototyping with Claude Code (14:03)</summary>

[00:00]
- These developers tend to like to run
multiple Claude sessions at once,
and they've started calling
this multi-Clauding.
So you might see sessions
where people have like six Claudes open
on their computer at the same time.
- Hey, I'm Alex.
I lead Claude Relations here at Anthropic.
Today we're gonna be
talking about Claude Code,
and I'm joined by my colleague Cat.
- Hey, I'm Cat.
I'm the product manager for Claude Code.
- Cat, I wanna kick this
off just talking about
the insane rate of
shipping in Claude Code.
It feels like literally every time
I open it up in my terminal,
there's a new product or a new feature,
something for me to use.
Can you walk me through
what the process looks like
of the team going from an idea
to actually shipping
something to end users?
- Yeah, so the Claude Code team is full
of very product-minded engineers
and a lot of these features
are just built bottom-up.
It's like you're a developer
and you really wish you had this thing,
and then you build it for yourself.
And the way that our process works
is instead of writing a doc,
it's so fast to use Claude Code

[00:01]
to prototype a feature
that most of the time people
just prototype the feature
and then they ship it
internally to "Ants".
And if the reception is really positive,
then that's a very strong signal
that the external world will like it too.
And that's actually our bar
for shipping it externally.
And then of course there's always features
that like aren't exactly right
that need some tweaking.
And if we feel like, okay,
"Ants" aren't really using it
that much, then we just go
back to the drawing board
and we say like, okay,
what else could we change about this?
- And when we say "Ants," do
we mean Anthropic employees?
- Yes, yes.
- Yeah.
That's really fascinating.
I've never seen a product have as strong
of like a "dogfooding"
loop as Claude Code.
Do you think that's
something we purposely did
or that just kind of naturally arise
from the product itself?
- It is quite intentional,
and it's also a really important reason
why Claude Code works so well.
Because it's so easy to prototype
features on Claude Code,
we do push people to
prototype as much as possible,

[00:02]
but it's hard to reason about
like exactly how a
developer will use a tool
because developers are so heterogeneous
in their workflows.
So oftentimes, even if
you theoretically know
you wanna do something,
like even if you theoretically know
that you wanna build an IDE integration,
there's still a range
of like potential ways
you could go about it.
And often prototyping is the only way
that you can really feel how the product
will actually be in your workflow.
So yeah, it's through the
process of "dogfooding"
that we decide what version of
a feature we decide to ship.
- I see.
And there's something about the,
almost like the flexibility
but also the constraints
of the terminal too
that allows for easy addition
of like new features,
which I've kind of
noticed where it's like,
because we have the primitives built out
of like slash commands and things,
it's easy to add another
one on top of that.
- Yeah, it's totally
designed to be customizable.
And because so many developers
are familiar with the terminal,

[00:03]
it makes like new feature
onboarding super straightforward,
because for example, for
a feature like hooks,
which lets you add a bit of determinism
around Claude Code events,
because every developer
knows how to write a script,
and really at the end of the day,
all a hook is, is a script.
And so you don't need to
learn a new technology
to customize Claude Code.
You write this script that
you already know how to do
and then you add it to one
of the Claude Code events
and now you have some determinism.
- We're really trying to meet customers
or developers where they are
with this tool.
- Definitely.
- Switching gears slightly,
so alongside this insane rate of shipping
is also the insane growth
rate of Claude Code
with developers everywhere.
Can you walk me through
what that's been like
to kind of be on this rocket ship
and how are we seeing various developers,
whether it's at startups or individuals
or at even large enterprises, use Claude?

[00:04]
- So one of the magical
things about Claude Code
is that the onboarding is so smooth.
After you do the NPM install,
Claude Code kind of just
like works out of the box
without any configuration.
And this is true whether
you are an indie developer
through to if you're an
engineer at a Fortune 500.
I think this is the
magic behind Claude Code.
Because it has access to
all of the local tools
and files that you have,
you have this like very clear mental model
for what Claude Code is capable of.
We do see different use
case patterns though
between smaller companies and larger ones.
We find that engineers
at smaller companies
tend to run Claude more autonomously
using things like "auto-accept mode,"
which lets Claude make edits by itself
without approval of each one.
We also find that these developers
tend to like to run multiple
Claude sessions at once,
and they've started calling
this multi-Clauding.
So you might see sessions

[00:05]
where people have like six Claudes open
on their computer at the same time.
Maybe each of them are in
a different Git workspace
or in a different copy of the Git repo,
and they're just like
managing each of them.
Whenever anyone stops
and asks for feedback,
they'll jump in there and then send it off
and let it continue running.
And on the other end of the spectrum
for larger companies,
we find that engineers really
like to use "plan mode."
So "plan mode" is a way for developers
to tell Claude Code to take a second,
explore the code base,
understand the architecture,
and create an engineering plan
before actually jumping
into the code itself.
And so we find that this is really useful
for harder tasks and more complex changes.
- So going back to multi-Clauding
just 'cause I think that's
a fascinating concept.
I'm sure we kind of imagined folks
wanting to do things like that,
but it was like somewhat surprising.
Is there other things
in that domain of like,

[00:06]
oh wow, this is a usage pattern
that we really did not expect
that have kind of popped up organically
and we've shifted our
roadmap around a little bit?
- Yeah, I think multi-Clauding
is the biggest one
because this is something that we thought
was just a power user feature
that like a few people would wanna do.
But in fact this is
actually a really common way
in which people use Claude.
And so for example,
they might have one Claude instance
where they only ask questions
and this one doesn't edit code.
That way they can have
another Claude instance
in the same repo that does edit code
and these two don't
interfere with each other.
Other things that we've seen
are people really like
to customize Claude Code
to handle specialized tasks.
So we've seen people build
like SRE agents on Claude Code,
security agents, incident response agents.
And what that made us realize
is that integrations are so important
for making sure Claude Code works well.
And so we've been encouraging people

[00:07]
to spend more time to
tell Claude Code about,
hey, these are the CLI
tools we commonly use
or to set up remote MCP servers
to get access to logs and
ticket management software.
- When these engineers are
customizing Claude Code,
does that mean they're creating sub-agents
or are they creating markdown files
like CLAUDE.md files?
How exactly are they creating these
different types of agents?
- Yeah, I think the most common ways
that we've seen people customize
is by investing a lot
into the CLAUDE.md file.
So the CLAUDE.md file is
our concept of memory.
And so it's the best place for you
to tell Claude Code about
what your team's goals are,
how the code is architected,
any gotchas in the code base,
any best practices.
And investing in CLAUDE.md
we've heard dramatically improves
the quality of the output.
The other way that people
customize Claude Code
is by adding custom slash commands.

[00:08]
So if there's a prompt
that you're always typing,
you can add that into
the custom slash commands
and you could also check these in
so that you share them
with the rest of your team.
And then you can also add custom hooks.
So if for example,
you want Claude Code to run lints
before it makes a commit,
this is something that's great for a hook.
If you want Claude Code to
send you a Slack notification
every time it's done working,
this is actually the original inspiration
for making hooks.
And so these are all customizations
that people are building today.
- Tell me more about,
what is the Claude Code SDK?
- The Claude Code SDK is a great way
to build general agents.
The Claude Code SDK gives you access
to all of the core building
blocks of an agent,
including you can bring
your own system prompt,
you can bring your own custom tools,
and what you get from the
SDK is a core agentic loop
where we handle the user turns
and we handle executing
the tool calls for you.

[00:09]
You get to use our
existing permission system
so that you don't need to
build one from scratch.
And we also handle interacting
with the underlying API.
So we make sure that we have backoff
if there's any API errors.
We very aggressively prompt cache
to make sure that your
requests are token-efficient.
If you are prototyping
building an agent from scratch,
if you use the Claude Code SDK,
you can get up and running with something
pretty powerful within
like 30 minutes or so.
We've been seeing people build
really cool things with it.
We open-sourced our Claude
Code on GitHub integration,
which is completely built on the SDK,
and we've seen people build
security agents on it,
SRE agents, incident response agents.
And these are just
within the coding domain.
Outside of coding, we've seen people
prototype legal agents, compliance agents.
This is very much intended
to be a general SDK
for all your agent needs.
- The SDK is pretty amazing to me.
I feel like we've lived in
the single request API world

[00:10]
for so long.
And now we're moving to like
a next level abstraction
almost where we're gonna handle
all the nitty-gritty of
the things you mentioned.
Where is the SDK headed?
What's next there?
- We're really excited about the SDK
as the next way to unlock
another generation of agents.
We're investing very heavily
in making sure the SDK is best-in-class
for building agents.
So all of the nice features
that you have in Claude Code
will be available out
of the box in the SDK,
and you can pick and choose
which ones you wanna keep.
So for example, if you want your agent
to be able to have a to-do list, great.
You have the to-do list
tool out of the box.
If you don't want that,
it's really easy to just delete that tool.
If your agent needs to
edit files, for example,
to update its memory, you
get that out of the box.
And if you decide, okay,
mine won't edit files

[00:11]
or it'll edit files in a different way,
you can just bring your
own implementation.
- Okay, so it's extremely customizable,
basically general purpose in the sense
that you could swap out the system prompt
or the tools for your own implementations.
And they just nicely slot in
to whatever thing you're building for,
whether it's in an entirely
different domain than code.
Right?
- Yeah, totally.
I'm really excited to see what
people hack on top of this.
I think like especially for people
who are just trying to prototype an agent,
this is like, I think
by far the fastest way
to get started.
Like we really spent almost a year
perfecting this harness,
and this is the same harness
that Claude Code runs on.
And so if you want to just jump
right into the specific
integrations that your agent needs
and you wanna jump right into like
just working on the system prompt
to share context about the
problems faced with the agent,
and you don't wanna deal
with the agent loop,
this is like the best way to circumvent

[00:12]
all the general purpose harness
and just add your like
special sauce to it.
- Hmm, all right.
Well, you heard it here.
You gotta go build on the SDK.
Before we wrap up here,
I'm really curious to hear your own tips
for how you use Claude Code,
and what are some best practices
we can share with developers?
- When you work with Claude
Code or any agentic tool,
I think the most important thing
is to clearly communicate what
your goals are to the tool.
I think a lot of people
think that prompting
is this like magical
thing, but it really isn't.
It's very much about, okay,
did I clearly articulate
what my purpose is?
Like what my purpose with this task is,
how I'm evaluating the output of the task,
any constraints in the design system.
And I think usually
when you can clearly
communicate these things,
Claude Code will either be able to do them
or just tell you that
like, "Okay, this thing,

[00:13]
like I'm not able to do because A, B, C
and do you wanna try
like D, E, F instead?"
- So it's all about the communication
just as if you're working
with another engineer.
- Yeah, totally.
And another thing is if you notice
that Claude Code did something weird,
you could actually just ask
it why it wanted to do that.
And it might tell you something like,
oh, okay, there was something
in CLAUDE.md that said this,
or I read something in this file
that like gave me this like impression.
And then that way you can actually use
like talking to Claude as a way to debug.
It doesn't always work,
but I think it's definitely worth trying.
And it's like a common
technique that we use.
- You use Claude Code
to debug Claude Code.
I love it.
- Yeah, yeah.
Like the same way that
when working with a human,
if they say something
that you didn't expect,
you might feel like, "Oh, interesting.
Like, what gave you that impression?
Or why did you think this?"
And I think you can do
the same with agents too.
- That's fascinating.
Well, Cat, this has been great.
Really, we appreciate the time.
Thank you.
- Thanks for having me.

</details>


<!-- yt-inline:vLIDHi-1PVU -->
[![Designing Claude Code](https://img.youtube.com/vi/vLIDHi-1PVU/hqdefault.jpg)](https://www.youtube.com/watch?v=vLIDHi-1PVU)

<details>
<summary>자막: Designing Claude Code (12:03)</summary>

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


Now we’re making all of this available to you. The [Claude Agent SDK](https://anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) is the same infrastructure that powers Claude Code, but it shows impressive benefits for a very wide variety of tasks, not just coding. As of today, you can use it to build your own agents.

We built Claude Code because the tool we wanted didn’t exist yet. The Agent SDK gives you the same foundation to build something just as capable for whatever problem you're solving.

## Bonus research preview

We’re releasing a temporary research preview alongside Claude Sonnet 4.5, called "[Imagine with Claude](https://claude.ai/redirect/website.v1.27bda13e-87f6-45cc-b8d2-4d85ad734b61/imagine)".

In this experiment, Claude generates software on the fly. No functionality is predetermined; no code is prewritten. What you see is Claude creating in real time, responding and adapting to your requests as you interact.

It's a fun demonstration showing what Claude Sonnet 4.5 can do—a way to see what's possible when you combine a capable model with the right infrastructure.

"Imagine with Claude" is available to Max subscribers for the next five days. We encourage you to try it out on [claude.ai/imagine](https://claude.ai/redirect/website.v1.27bda13e-87f6-45cc-b8d2-4d85ad734b61/imagine).

## Further information

We recommend upgrading to Claude Sonnet 4.5 for all uses. Whether you’re using Claude through our apps, our API, or Claude Code, Sonnet 4.5 is a drop-in replacement that provides much improved performance for the same price. Claude Code updates are available to all users. [Claude Developer Platform](https://claude.com/platform/api) updates, including the Claude Agent SDK, are available to all developers. Code execution and file creation are available on all paid plans in the Claude apps.

For complete technical details and evaluation results, see our [system card](https://www.anthropic.com/claude-sonnet-4-5-system-card), [model page](https://www.anthropic.com/claude/sonnet), and [documentation](https://docs.claude.com/en/docs/about-claude/models/overview). For more information, explore our [engineering](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) [posts](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) and research post on [cybersecurity](https://red.anthropic.com/2025/ai-for-cyber-defenders).

#### Footnotes

*1**:** Customers in the cybersecurity and biological research industries can work with their account teams to join our allowlist in the meantime.*  
  
**Methodology**

* **SWE-bench Verified**: All Claude results were reported using a simple scaffold with two tools—bash and file editing via string replacements. We report 77.2%, which was averaged over 10 trials, no test-time compute, and 200K thinking budget on the full 500-problem SWE-bench Verified dataset.
  + The score reported uses a minor prompt addition: "You should use tools as much as possible, ideally more than 100 times. You should also implement your own tests first before attempting the problem."
  + A 1M context configuration achieves 78.2%, but we report the 200K result as our primary score as the 1M configuration was implicated in our recent [inference issues](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues).
  + For our "high compute" numbers we adopt additional complexity and parallel test-time compute as follows:
    - We sample multiple parallel attempts.
    - We discard patches that break the visible regression tests in the repository, similar to the rejection sampling approach adopted by [Agentless](https://arxiv.org/abs/2407.01489) (Xia et al. 2024); note no hidden test information is used.
    - We then use an internal scoring model to select the best candidate from the remaining attempts.
    - This results in a score of 82.0% for Sonnet 4.5.
* **Terminal-Bench**: All scores reported use the default agent framework (Terminus 2), with XML parser, averaging multiple runs during different days to smooth the eval sensitivity to inference infrastructure.
* **τ2-bench:** Scores were achieved using extended thinking with tool use and a prompt addendum to the Airline and Telecom Agent Policy instructing Claude to better target its known failure modes when using the vanilla prompt. A prompt addendum was also added to the Telecom User prompt to avoid failure modes from the user ending the interaction incorrectly.
* **AIME**: Sonnet 4.5 score reported using sampling at temperature 1.0. The model used 64K reasoning tokens for the Python configuration.
* **OSWorld:** All scores reported use the official OSWorld-Verified framework with 100 max steps, averaged across 4 runs.
* **MMMLU**: All scores reported are the average of 5 runs over 14 non-English languages with extended thinking (up to 128K).
* **Finance Agent**: All scores reported were run and published by [Vals AI](https://vals.ai) on their public leaderboard. All Claude model results reported are with extended thinking (up to 64K) and Sonnet 4.5 is reported with interleaved thinking on.
* All OpenAI scores reported from their [GPT-5 post](https://openai.com/index/introducing-gpt-5/), [GPT-5 for developers post](https://openai.com/index/introducing-gpt-5-for-developers/), [GPT-5 system card](https://cdn.openai.com/gpt-5-system-card.pdf) (SWE-bench Verified reported using n=500), [Terminal Bench leaderboard](https://www.tbench.ai/) (using Terminus 2), and public [Vals AI](http://vals.ai) leaderboard. All Gemini scores reported from their [model web page](https://deepmind.google/models/gemini/pro/), [Terminal Bench leaderboard](https://www.tbench.ai/) (using Terminus 1), and public [Vals AI](https://vals.ai) leaderboard.
