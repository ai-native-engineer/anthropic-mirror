<!-- source: https://claude.com/blog/building-agents-with-the-claude-agent-sdk -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d7d4c10df6024f7bc_ee580919acaba2ddc07425f7a7390c8962cadc94-1000x1000.svg)

# Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code. In this article, we walk through how to get started and share our best practices.

‍

  [Claude Code](https://claude.com/blog/category/claude-code)

  [Agents](https://claude.com/blog/category/agents)
* Product

  Claude Code

* Date

  September 29, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/building-agents-with-the-claude-agent-sdk

Last year, we shared lessons in [building effective agents](https://www.anthropic.com/engineering/building-effective-agents) alongside our customers. Since then, we've released [Claude Code](https://claude.com/product/claude-code), an agentic coding solution that we originally built to support developer productivity at Anthropic.

Over the past several months, Claude Code has become far more than a coding tool. At Anthropic, we’ve been [using it](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code) for deep research, video creation, and note-taking, among countless other non-coding applications. In fact, it has begun to power almost all of our major agent loops.

In other words, the agent harness that powers Claude Code (the Claude Code SDK) can power many other types of agents, too. To reflect this broader vision, we're renaming the Claude Code SDK to the Claude Agent SDK.

In this post, we'll highlight why we built the Claude Agent SDK, how to build your own agents with it, and share the best practices that have emerged from our team’s own deployments.

## Giving Claude a computer

[The key design principle](https://www.youtube.com/watch?v=vLIDHi-1PVU) behind Claude Code is that Claude needs the same tools that programmers use every day. It needs to be able to find appropriate files in a codebase, write and edit files, lint the code, run it, debug, edit, and sometimes take these actions iteratively until the code succeeds.

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


We found that by giving Claude access to the user’s computer (via the terminal), it had what it needed to write code like programmers do.

But this has also made Claude in Claude Code effective at *non*-coding tasks. By giving it tools to run bash commands, edit files, create files and search files, Claude can read CSV files, search the web, build visualizations, interpret metrics, and do all sorts of other digital work – in short, create general-purpose agents with a computer. The key design principle behind the Claude Agent SDK is to give your agents a computer, allowing them to work like humans do.

## Creating new types of agents

We believe giving Claude a computer unlocks the ability to build agents that are more effective than before. For example, with our SDK, developers can build:

* **Finance agents**:Build agents that can understand your portfolio and goals, as well as help you evaluate investments by accessing external APIs, storing data and running code to make calculations.
* **Personal assistant agents**. Build agents that can help you book travel and manage your calendar, as well as schedule appointments, put together briefs, and more by connecting to your internal data sources and tracking context across applications.
* **Customer support agents:** Build agents that can handle high ambiguity user requests, like customer service tickets, by collecting and reviewing user data, connecting to external APIs, messaging users back and escalating to humans when needed.
* **Deep research agents**: Build agents that can conduct comprehensive research across large document collections by searching through file systems, analyzing and synthesizing information from multiple sources, cross-referencing data across files, and generating detailed reports.

And much more. At its core, the SDK gives you the primitives to build agents for whatever workflow you're trying to automate.

## Building your agent loop

In Claude Code, Claude often operates in a specific feedback loop: gather context -> take action -> verify work -> repeat.

![Agent feedback loop](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4b28db0e40fd93e63875_image.png)

Agents often operate in a specific feedback loop: gather context -> take action -> verify work -> repeat.

This offers a useful way to think about other agents, and the capabilities they should be given. To illustrate this, we’ll walk through the example of how we might build an email agent in the Claude Agent SDK.

## Gather context

When developing an agent, you want to give it more than just a prompt: it needs to be able to fetch and update its own context. Here’s how features in the SDK can help.

### **Agentic search and the file system**

The file system represents information that *could* be pulled into the model's context.

When Claude encounters large files, like logs or user-uploaded files, it will decide which way to load these into its context by using bash scripts like `grep` and `tail`. In essence, the folder and file structure of an agent becomes a form of [context engineering](http://anthropic.com/news/context-management).

Our email agent might store previous conversations in a folder called ‘Conversations’. This would allow it to search previous these for its context when asked about them.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4b28db0e40fd93e6387e_image.webp)

### **Semantic search**

[Semantic search](https://www.anthropic.com/news/contextual-retrieval) is usually faster than agentic search, but less accurate, more difficult to maintain, and less transparent. It involves ‘chunking’ the relevant context, embedding these chunks as vectors, and then searching for concepts by querying those vectors. Given its limitations, we suggest starting with agentic search, and only adding semantic search if you need faster results or more variations.

### **Subagents**

Claude Agent SDK supports subagents by default. [Subagents](https://docs.claude.com/en/api/agent-sdk/subagents) are useful for two main reasons. First, they enable parallelization: you can spin up multiple subagents to work on different tasks simultaneously. Second, they help manage context: subagents use their own isolated context windows, and only send relevant information back to the orchestrator, rather than their full context. This makes them ideal for tasks that require sifting through large amounts of information where most of it won't be useful.

When designing our email agent, we might give it a 'search subagent' capability. The email agent could then spin off multiple search subagents in parallel—each running different queries against your email history—and have them return only the relevant excerpts rather than full email threads.

### **Compaction**

When agents are running for long periods of time, context maintenance becomes critical. The Claude Agent SDK’s compact feature automatically summarizes previous messages when the context limit approaches, so your agent won’t run out of context. This is built on Claude Code’s [compact slash command](https://docs.claude.com/en/docs/claude-code/sdk/sdk-slash-commands#%2Fcompact-compact-conversation-history).

## Take action

Once you’ve gathered context, you’ll want to give your agent flexible ways of taking action.

### **Tools**

[Tools](https://www.anthropic.com/engineering/writing-tools-for-agents) are the primary building blocks of execution for your agent. Tools are prominent in Claude's context window, making them the primary actions Claude will consider when deciding how to complete a task. This means you should be conscious about how you design your tools to maximize context efficiency. You can see more best practices in our blog post, [Writing effective tools for agents – with agents](https://www.anthropic.com/engineering/writing-tools-for-agents) .

As such, your tools should be primary actions you want your agent to take. Learn how to make [custom tools](https://docs.claude.com/en/api/agent-sdk/custom-tools) in the Claude Agent SDK.

For our email agent, we might define tools like “`fetchInbox`” or “`searchEmails`” as the agent’s primary, most frequent actions.

### **Bash & scripts**

Bash is useful as a general-purpose tool to allow the agent to do flexible work using a computer.

In our email agent, the user might have important information stored in their attachments. Claude could write code to download the PDF, convert it to text, and search across it to find useful information by calling, as depicted below:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4b28db0e40fd93e6387b_image.webp)

### **Code generation**

The Claude Agent SDK excels at code generation—and for good reason. Code is precise, composable, and infinitely reusable, making it an ideal output for agents that need to perform complex operations reliably.

When building agents, consider: which tasks would benefit from being expressed as code? Often, the answer unlocks significant capabilities.

For example, our recent launch of [file creation in](https://www.anthropic.com/news/create-files) [Claude.AI](http://claude.ai/redirect/website.v1.bdb29daa-1a07-41ec-87f6-579dc33634bd) relies entirely on code generation. Claude writes Python scripts to create Excel spreadsheets, PowerPoint presentations, and Word documents, ensuring consistent formatting and complex functionality that would be difficult to achieve any other way.

In our email agent, we might want to allow users to create rules for inbound emails. To achieve this, we could write code to run on that event:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4b28db0e40fd93e63878_image.webp)

### **MCPs**

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) provides standardized integrations to external services, handling authentication and API calls automatically. This means you can connect your agent to tools like Slack, GitHub, Google Drive, or Asana without writing custom integration code or managing OAuth flows yourself.

For our email agent, we might want to `search Slack messages` to understand team context, or `check Asana tasks` to see if someone has already been assigned to handle a customer request. With MCP servers, these integrations work out of the box—your agent can simply call tools like search\_slack\_messages or get\_asana\_tasks and the MCP handles the rest.

The growing [MCP ecosystem](https://github.com/modelcontextprotocol/servers) means you can quickly add new capabilities to your agents as pre-built integrations become available, letting you focus on agent behavior.

## Verify your work

The Claude Code SDK finishes the agentic loop by evaluating its work. Agents that can check and improve their own output are fundamentally more reliable—they catch mistakes before they compound, self-correct when they drift, and get better as they iterate.

The key is giving Claude concrete ways to evaluate its work. Here are three approaches we've found effective:

### **Defining rules**

The best form of feedback is providing clearly defined rules for an output, then explaining which rules failed and why.

[Code linting](https://stackoverflow.com/questions/8503559/what-is-linting) is an excellent form of rules-based feedback. The more in-depth in feedback the better. For instance, it is usually better to generate TypeScript and lint it than it is to generate pure JavaScript because it provides you with multiple additional layers of feedback.

When generating an email, you may want Claude to check that the email address is valid (if not, throw an error) and that the user has sent an email to them before (if so, throw a warning).

### **Visual feedback**

When using an agent to complete visual tasks, like UI generation or testing, visual feedback (in the form of screenshots or renders) can be helpful. For example, if sending an email with HTML formatting, you could screenshot the generated email and provide it back to the model for visual verification and iterative refinement. The model would then check whether the visual output matches what was requested.

For instance:

* **Layout** - Are elements positioned correctly? Is spacing appropriate?
* **Styling** - Do colors, fonts, and formatting appear as intended?
* **Content hierarchy** - Is information presented in the right order with proper emphasis?
* **Responsiveness** - Does it look broken or cramped? (though a single screenshot has limited viewport info)

Using an MCP server like Playwright, you can automate this visual feedback loop—taking screenshots of rendered HTML, capturing different viewport sizes, and even testing interactive elements—all within your agent's workflow.

![Claude provides visual feedback on the body of an email generated by an agent.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4b28db0e40fd93e63881_image.webp)

Visual feedback from a large-language model (LLM) can provide helpful guidance to your agent.

### **LLM as a judge**

You can also have another language model “judge" the output of your agent based on fuzzy rules. This is generally not a very robust method, and can have heavy latency tradeoffs, but for applications where any boost in performance is worth the cost, it can be helpful.

Our email agent might have a separate subagent judge the tone of its drafts, to see if they fit well with the user’s previous messages.

## Testing and improving your agent

After you’ve gone through the agent loop a few times, we recommend testing your agent, and ensuring that it’s well-equipped for its tasks. The best way to improve an agent is to look carefully at its output, especially the cases where it fails, and to put yourself in its shoes: does it have the [right tools](https://www.anthropic.com/engineering/writing-tools-for-agents) for the job?

Here are some other questions to ask as you’re evaluating whether or not your agent is well-equipped to do its job:

* If your agent misunderstands the task, it might be missing key information. Can you alter the structure of your search APIs to make it easier to find what it needs to know?
* If your agent fails at a task repeatedly, can you add a formal rule in your tool calls to identify and fix the failure?
* If your agent can’t fix its errors, can you give it more useful or creative tools to approach the problem differently?
* If your agent’s performance varies as you add features, build a representative test set for programmatic evaluations (or evals) based on customer usage.

## Getting started

The Claude Agent SDK makes it easier to build autonomous agents by giving Claude access to a computer where it can write files, run commands, and iterate on its work.

With the agent loop in mind (gathering context, taking action, and your verifying work), you can build reliable agents that are easy to deploy and iterate on.

You can [get started](https://docs.claude.com/en/api/agent-sdk/overview) with the Claude Agent SDK today. For developers who are already building on the SDK, we recommend migrating to the latest version by following [this guide](https://docs.claude.com/en/docs/claude-code/sdk/migration-guide).

## Acknowledgements

Written by Thariq Shihipar with notes and editing from Molly Vorwerck, Suzanne Wang, Alex Isken, Cat Wu, Keir Bradwell, Alexander Bricken & Ashwin Bhat.

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

Get Claude Code

curl -fsSL https://claude.ai/install.sh | bash

Copy command to clipboard

irm https://claude.ai/install.ps1 | iex

Copy command to clipboard

Or read the [documentation](https://code.claude.com/docs/en/overview)

Try Claude Code

[Try Claude Code](https://claude.ai/code)Try Claude Code

Developer docs

[Developer docs](https://code.claude.com/docs/en/overview)Developer docs

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

Agents

Coding
