<!-- source: https://claude.com/blog/agent-capabilities-api -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22c10cdf166eebe4c84_d4b15045df86e43e5b5dc7b25784321ce8b5dd88-1000x1000.svg)

# New capabilities for building agents on the Anthropic API

Claude now offers code execution, MCP server connections, file storage, and extended prompt caching through the API—giving developers powerful tools to build agents that analyze data, connect to external systems, and maintain context for longer periods of time.

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

* Date

  May 22, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/agent-capabilities-api

Today, we're announcing four new capabilities on the Anthropic API that enable developers to build more powerful AI agents: the code execution tool, MCP connector, Files API, and the ability to cache prompts for up to one hour.

### Building better AI agents

Together with [Claude Opus 4 and Sonnet 4](https://www.anthropic.com/news/claude-4), these beta features enable developers to build agents that execute code for advanced data analysis, connect to external systems through MCP servers, store and access files efficiently across sessions, and maintain context for up to 60 minutes with cost-effective caching—without building custom infrastructure.

For example, a project management AI agent can use the MCP connector with Asana to reference tasks and assign work, upload relevant reports via the Files API, analyze progress and risks with the code execution tool, and maintain full context throughout—all while keeping costs down through extended prompt caching.

These capabilities join existing features like [web search](https://www.anthropic.com/news/web-search-api) and [citations](https://www.anthropic.com/news/introducing-citations-api) as part of a comprehensive toolkit for building AI agents. Read on to explore each new capability in detail.

### Code execution tool

We're introducing a [code execution tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool) on the Anthropic API, giving Claude the ability to run Python code in a sandboxed environment to produce computational results and data visualizations. This transforms Claude from a code-writing assistant into a data analyst that can iterate on visualizations, clean datasets, and derive insights directly within API calls.

With the code execution tool, Claude can load datasets, generate exploratory charts, identify patterns, and iteratively refine outputs based on execution results—all within a single interaction. This means that Claude can handle complex analytical tasks end-to-end, rather than just suggesting code for you to run separately.

Key use cases include:

* **Financial modeling**: Generate financial projections, analyze investment portfolios, and calculate complex financial metrics.
* **Scientific computing**: Execute simulations, process experimental data, and analyze research datasets.
* **Business intelligence**: Create automated reports, analyze sales data, and generate performance dashboards.
* **Document processing**: Extract and transform data across formats, generate formatted reports, and automate document workflows.
* **Statistical analysis**: Perform regression analysis, hypothesis testing, and predictive modeling on datasets.

Organizations receive 50 free hours of usage with the code execution tool per day, then pay $0.05 per hour per container for additional usage. Explore the [documentation](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool) to learn more about pricing.

### MCP connector

The [MCP connector](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector) on the Anthropic API enables developers to connect Claude to any remote Model Context Protocol (MCP) server without writing client code.

Previously, connecting to MCP servers required building your own client harness to handle MCP connections. Now, the Anthropic API handles all connection management, tool discovery, and error handling automatically. Simply add a remote MCP server URL to your API request and you can immediately access powerful third-party tools, dramatically reducing the complexity of building tool-enabled agents.

When Claude receives a request with MCP servers configured, it automatically:

* Connects to the specified MCP servers
* Retrieves available tools
* Reasons about what tool to call and what arguments to pass
* Executes tool calls agentically until a sufficient result is achieved
* Manages authentication and error handling
* Returns the enhanced response with integrated data

The growing ecosystem of remote MCP servers means you can easily add capabilities to your AI applications without building one-off integrations. You can integrate with any remote MCP server, including those from [Zapier](https://zapier.com/mcp) and [Asana](https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server). See more remote MCP servers in our [documentation](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers).

### Files API

The [Files API](https://docs.anthropic.com/en/docs/build-with-claude/files) simplifies how developers store and access documents when building with Claude. Instead of managing file uploads in every request, you can now upload documents once and reference them repeatedly across conversations.

This streamlines development workflows, particularly for applications that need to work with large document sets such as knowledge bases, technical documentation, or datasets.

The Files API will integrate with the code execution tool, enabling Claude to access and process uploaded files directly during code execution and produce files such as charts and graphs as part of the response. This means developers can upload a dataset through the Files API once, then have Claude analyze it across multiple sessions without re-uploading.

### Extended prompt caching

Developers can now choose between our standard 5-minute time to live (TTL) for [prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) or opt for an [extended 1-hour TTL](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration-beta) at an [additional cost](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#pricing)—a 12x improvement that can reduce expenses for long-running agent workflows. With extended caching, customers can provide Claude with extensive background knowledge and examples while reducing costs by up to 90% and latency by up to 85% for long prompts.

This makes it practical to build agents that maintain context over extended periods, whether they're handling multi-step workflows, analyzing complex documents, or coordinating with other systems. Long-running agent applications that previously faced prohibitive costs can now operate efficiently at scale.

### Getting started

All of these features are now available in public beta on the Anthropic API. [Visit our documentation](https://docs.anthropic.com/en/docs/overview) to learn more or [watch the keynote](https://www.youtube.com/live/EvtPBaaykdo) from our developer conference to see these capabilities in action.

<!-- yt-inline:EvtPBaaykdo -->
[![Code with Claude Opening Keynote](https://img.youtube.com/vi/EvtPBaaykdo/hqdefault.jpg)](https://www.youtube.com/watch?v=EvtPBaaykdo)

<details>
<summary>자막: Code with Claude Opening Keynote (1:40:20)</summary>

[00:00]
hey hey hey
[Music]
welcome

[00:02]
[Music]

[00:03]
hey
hey hey
[Music]
[Music] hey hey hey [Music]

[00:04]
[Music]
[Music] hey
hey hey
[Music]
heat heat
[Music]
happy

[00:05]
[Music] birthday heat heat
[Music]
doo doo doo doo doo doo
doo doo doo doo doo [Music]

[00:06]
let me do it

[00:07]
[Music]
hey come on

[00:08]
[Music]
heat
[Music]
heat heat heat [Music]

[00:09]
[Music]
happy
[Music]

[00:10]
hey hey hey
[Music]
oh hey hey
you are

[00:11]
[Music]
I'm [Music]
[Music]
Hey over beh

[00:12]
[Music] what
[Music]
hey hey hey one one 1 [Music]

[00:13]
[Music]
1.11
[Music]
here come

[00:14]
[Music]
one one one one one one one

[00:17]
[Music]

[00:18]
hey hey hey
[Music]
hey hey hey [Music]
[Music]
[Music] i [Music]
love me
[Music]
come
on hey
[Music]
[Music] hey hey hey
[Music]
hey hey hey hey hey hey hey hey hey hey hey hey

[00:19]
[Music]
party don't get Get yourself
[Music]
hey down Down down

[00:20]
down down down down [Music]
come on come on [Music]

[00:21]
[Music]
down down down down down down gabbit jump
[Music]
dick dick

[00:22]
[Music]
d [Music] down [Music] d Get [Music]
down
[Music]
hey hey hey

[00:23]
[Music]
down hey [Music]
Black yeah

[00:24]
[Music]
yeah yeah [Music]

[00:25]
yeah
yeah heat heat
[Music]

[00:27]
okay okay [Music]
please welcome to the stage chief
product officer of Anthropic Mike
[Applause] [Music] Kger good morning everyone
and welcome to Code with Claude Anthropic's
first developer conference i'm really happy
to see you all here i'm Mike Kger i am chief
product officer here at Anthropic i just hit my
one-year mark which in AI years is about like
three years um but I'm having a blast um and
before this I co-founded Instagram um and also
an AI powered news app called Artifact which is
where I first started getting exposed to a lot of
these AI technologies i joined Anthropic because
of its founders vision building AI systems that

[00:28]
are powerful as well as helpful and trustworthy
today that vision includes something immediate
and concrete a commitment to empower developers
like yourselves to transform how work gets done
and how companies get built this transformation is
about augmenting not replacing human creativity ai
agents are changing the way we work and the way
we innovate they're expanding what we can build
by removing bottlenecks that have limited human
productivity today you'll hear from our product
and engineering leaders as well as some of our
customers about how they're pushing the frontier
to give you a sense of what you can expect today
at Code with Claude you can attend three technical
deep dives to transform how you build with
Claude and five sessions from leading players
already using Anthropics platform to reshape
their industries and dedicated office hours and
workshops for hands-on experience but before we
talk about some exciting new API API capabilities

[00:29]
I have for you I want to invite a guest on stage
please welcome our CEO and co-founder Daario Amade
hey everyone uh I'm going to be back in 20
minutes for a fireside so uh I'll be I'll be
really really brief with uh with this appearance
um I'm not one to uh hype things up so I'll just
say this without any further fanfare i'm
happy to announce that as of exactly this
moment we're releasing Claude 4 Opus and Claude
4 Sonnet on all of our relevant product services
now I know that we haven't had an opus model
in a while so just as a reminder opus is the
most capable and intelligent model and sonnet is
the mid-level model that you all know and love

[00:30]
and have been using for the last uh approximately
year that's a a good balance between intelligence
and efficiency um we tried to design both
of them so that there are there are use
cases and times when it's optimal to use each
one so I will talk very briefly about the two
of them and then and then turn it back over to
Mike and then I'll be back for the fireside um
uh first let's talk about Opus so it is especially
designed for coding and agentic tasks um it gets
state-of-the-art on Sweetbench Terminal Bench some
other things like like that um uh but I think in
many ways uh as we're often finding with large
models the benchmarks don't fully do justice to it
um customers who we've previewed it to have found
that it can do tasks that take humans up to six or
seven hours autonomously um uh within Enthropic
I've seen some of our most senior engineers be
surprised at how much more productive it has made
them and for the first time actually when I've

[00:31]
um you know looked and and seen clawude
written internal summaries documents and
uh and and ideas you know in the past the quality
was often good but you could never really quite
mistake it for a human because it always had
that that specific style this was the first
time I actually got fooled where I actually get
got back and then you know I just read by the
name really fast and I thought it referred
to someone on the team and I'm like no the
name was Claude um uh uh so I you know I think I
think there's a there's a there's a lot in opus
um on sonnet um I think this will be for
many people a strict update for uh a a strict
improvement from sonnet 3.7 um at the same cost
and better intelligence many customers are simply
uh uh switching directly from one to the other it
actually does just as well as Opus on some of the
uh coding benchmarks but I think it's leaner and
more narrowly focused um I think in particular it

[00:32]
addresses some of the uh feedback we got on sonnet
3.7 around overeagerness the tendency to do more
than you asked for which is sort of the opposite
of laziness which was which was an earlier problem
and and some of the some of the reward hacking
issues so many of our customers have been trying
it out and view it as a strong upgrade from
3.7 for example um you know cursor cursor here
has been uh one of our well-known customers
has been trying it and says saying this is
uh this is a state-of-the-art uh this is this is
this is a state-of-the-art coding model um it's a
leapuh forward and complex codebase understanding
and we expect developers will experience uh across
the board capability improvements um someone who
was playing with the model in person one customer
said "What the f is this model?" Um it's really
it's really amazing so um uh I'll I'll leave the
details to others but um the last thing I'll say
is we are going to continue to improve the Clawude

[00:33]
4 series of models we expect to periodically
release perhaps minor version updates ideally
even more frequently than we than we have for um
for uh for for Sonnet so it should be out there
you should be able to try it on basically all
all the surfaces as of now except I think free
tier has has sonnet uh has sonnet only but all
the other surfaces uh all the API surfaces have
both um so uh really hope you enjoy the
model and I'll turn it back over to Mike
thank you Dario two new models and you heard it
here first um we'll be seeing Dario again as you
mentioned at the end of our agenda for a Q&A where
I'll get to ask him the questions that are likely
on your mind uh right now as well i'm personally
very excited for our customers to try both Cloud
Opus 4 and Sonet 4 our teams have loved working
with them and we think you will too uh now that
Dario has shared our big model news I'll talk
more about our detailed API roadmap our goals

[00:34]
for building Cloud 4 were clear from the start
wanted to build powerful AI that safely introduces
new model capabilities continue to advance the
frontier for coding and AI agents and ensure
that cloud becomes your virtual collaborator and
that's exactly what we've delivered with Opus 4
and Sonnet 4 like uh Sonnet 37 both Cloud 4 models
are what we call hybrid models that have two modes
near instant responses and extended thinking for
when you need deeper reasoning i've been surprised
at how many customers use the deeper reasoning
even for non-coding and non-math use cases
opus 4 is great at understanding your codebase
and planning additions it's extremely effective
uh and accurate with everything from migrations
to code refactorings and it's also the right
choice for your most complex agentic workflows if
you found you've hit a wall with other models on
your use case I think you'll be really pleasantly
surprised with what you can do with Opus 4 sonnet
4 meanwhile excels at everyday coding tasks
app development uh and pair programming it's

[00:35]
also ideal for high volume use cases it perfectly
balances efficiency with performance think of it
as your always on coding partner both models
are live today as Daria mentioned in Cloud
and Claude Code as well as the Enthropic API
Amazon Bedrock and Google Cloud's Vert.ex AI
these models bring critical new capabilities for
building AI agents they can use tools like web
search during their reasoning process which is new
handle multiple tools in parallel and when given
access to local files it can actually maintain
memory across sessions to build knowledge over
time and I'll talk with Dario a little bit about
that memory feature too later these aren't just
incremental improvements they fundamentally change
what's possible for AI agents now I know the term
agents gets thrown around a lot these days i have
a personal uh joke which is how many minutes into
a meeting can we make at Anthropic without
saying the word agents i think I made it 17
minutes or something uh but today what we're
going to focus on is agents beyond the hype
um I think what's really key is with the right
underlying models and the right underlying

[00:36]
platform tools AI agents can actually turn human
imagination into tangible reality at unprecedented
scale and that's especially important for startups
and developers like yourselves i've been a founder
myself when I think back to Instagram's early
days our famously small team had to make a
bunch of very painful eitheror decisions we either
explore uh adding video to the product or focus on
our core creativity either focus on our mobile
app and at first our single mobile app or uh
expand into the web it was all very single track
with AI agents startups now can run experiments
in parallel learn from users and build products
faster than ever before which is something I've
heard from many of you all and AI agents can give
you the the founders of startups uh access to the
kind of strategic thinking that you might get from
a high-powered C CFO i see our CFO in the front
row here or head of product uh while they're still
building towards those key positions yourselves
you're not ready for the make those hires but you
can hire uh Claude for some of those roles for now

[00:37]
this transformation is no longer theoretical
i see it in my role and my work every single
day i personally spend a lot of time with Claude
maybe more time with Claude than my significant
other it's fine uh in fact uh soon after I
joined Anthropic um I uh sat down with Amazon's
Alexa team and they were eager to see how Claude
might become part of their vision for the future
of voice assistants at first my team planned
on presenting some slides talking points kind
of the plan we'd make for any other customer but
in the days leading up to the meeting I had this
like persistent thought why not use Claude itself
to build a hands-on demo i thought it'd make the
conversation more interesting and bring to life
the potential of Claude and Alexa functionality
together the challenge was building this demo
without any access to Alexa's actual codebase we
needed to create a prototype of the core Alexa
functionality while also integrating Claude's
capabilities all within a tight oneweek timeline
really a tight one weekend timeline claude was
the only reason we were able to pull this off uh
in such a limited time frame our threeperson team

[00:38]
split between San Francisco and London built a
functional prototype that showed the potential
and thanks to Claude the effort was a success i
even got to write some of the code you can take
the engineer out of the engineering CT overall
but you can't take it out of me uh and do a lot
of the front end development uh for the project
itself and of course a lot more work went into the
partnership after that first meeting um but Claude
is now one of the models that Amazon is using for
Alexa plus uh which launched earlier this year
and is now rolling out and we were able I think
to really show the potential thanks to Claude
i've been watching this evolution towards ai
for years now uh when I first got a demo early
access of GitHub Copilot back in 2021 I called
it the single most mind-blowing application of
machine learning I've ever seen back in those days
2020 we called it machine learning instead of AI
that was generations ago but it was really clear
the potential for this early glimpse of Agentic
AI i had an even stronger feeling last summer
when we launched Artifacts i could describe what
I wanted for a mini app or visualization hit send

[00:39]
go grab coffee and come back to Claude having
built what I'd imagined and over the following
year it's become clear we're not just building
better tools we're creating genuine collaborators
and Anthropic's economic research uh confirms
what I've seen firsthand for the majority of
use cases AI is augmenting people's work instead
of replacing it it's much more about tasks than
entire roles and this is similar to the influence
that your best colleagues have the most talented
people you work with don't just execute they
understand your context they learn from experience
and they know when to take the initiative versus
when to just check in great AI agents like the
ones you can build on our platform should
excel at three capabilities they should have
contextual intelligence understanding you and your
organization's unique context and continuously
learning from experience not just following
instructions but comprehending the why and the
how that means models that learn and personalize
over time acquiring not just contextual but also
episodic and organizational memory the way
I always put this to the team is your hundth

[00:40]
task with an agent should be much better than your
first just like your hundth day with an employee
should be much better than your first if you're
doing the right things around training second
longunning execution handling complex multi-hour
tasks without constant management coordinating
with other agents and humans as needed so you
have the context and then you can execute it
over a longer period of time and third genuine
collaboration engaging in meaningful dialogue
adapting to your working style and providing
transparent reasoning for their actions the key
insight here is that true agency doesn't mean
uncontrolled action and autonomy doesn't mean
uh just yoloing it it means intelligent autonomy
balanced with clear checkpoints maintaining human
oversight for critical decisions while delegating
the smaller decisions that usually consume so much
of our time now let's talk about those
capabilities we're announcing to serve
those three needs we'll start with our new code
execution tool which is available on the anthropic
API today the code execution tool gives Claude
an environment where it can run code enabling

[00:41]
it to act as a data analyst that can transform
raw data into visual insights claude doesn't
just write code anymore now it can execute it it
sees the results and it can iteratively refine the
results and the code to better highlight patterns
in your data here uh we'll show Claude analyzing
sales data to see how a specific type of product
is performing claude can load your data set clean
it generate exploratory charts and drill down into
anomalies all in real time as someone who started
their career as a data visualization analyst this
resonates a bunch with me and the code execution
tool is even more powerful when combined with
the intelligence of the cloud for models this
is what we mean by agency the ability to take
a complex task and see it through to completion
these are the first models capable of handling
hours of tasks saving you half maybe even full
days when you work alongside them and not just
writing code snippets but refactoring entire
code bases or implementing complex features
from scratch to give you a sense of the kind

[00:42]
of progress that we're seeing back in the day when
I started you could delegate maybe minutes of work
to Cloud3 cloud3 meanwhile could work autonomously
for about 45 minutes without losing its thread
and now we're breaking into hours of work that
Claude can take on autonomously as you saw
earlier Rocketin mentioned that they ran Claude
independently for an incredible seven hours with
sustained performance it can do it without losing
the thread especially as it's able to manage its
memory and its own to-do list we've already
integrated this power where you work hopefully
you're all familiar with Cloud Code our agentic
coding tool that we launched in research preview a
few months ago we're moving cloud code to general
access today this actually started as an internal
exploratory project by Boris one of our tech leads
this is his announcement post who wanted Claude to
help them code directly in the terminal um very
early we still called it Claude CLI internally i
think some of our best innovations like artifacts
and cloud code have really come from this kind
of bottoms up experimentation it's part of the
culture we try to foster at anthropic within just

[00:43]
two days of launching it internally our usage
chart went vertical people talk about product
market fit we really often talk about product
anthropic fit like are people internally dog
fooding are they using it today most anthropic
employees rely on it for everything from routine
coding to large-scale migrations i've watched some
of our most advanced coders run multiple copies
of cloud code across multiple terminal windows
they're moving from just being engineers to being
managers of several autonomous agents tackling
everything from simple coding tasks to complex
full stack development projects across multiple
code bases i realized I was using cloud code and
I would run one in our front-end repo and one
in our backend repo and one of our cloud code
engineers is like you're doing it wrong just run
it in the root cloud can figure out where it's
going to be able to do it across all of them and
it does it beautifully and that's that's changed
how I've used it already the vast majority of
of anthropic developers use cloud code daily
to give you a sense of the impact it's had on our
team it's shortened our technical onboarding time
uh to get engineers up to speed from two to three
weeks to two to three days i've really seen it how

[00:44]
it can help you build an understanding of the
codebase especially a large monolith like ours
very rapidly as it's fantastic at navigating code
and today we're bringing cloud code capabilities
directly into VS Code and Jet Brains with full
diff views and agentic workflow management built
into the editors and we're also introducing
the Cloud Code SDK so you can build your own
applications on top of the same core agent as
Cloud Code as an example of the possibilities
of the SDK you can now run Claude code in GitHub
you can tag Claude in a GitHub pull request or an
issue and it will respond to reviewer uh feedback
modified code or implement test coverage we're
also focused on what we call closing the loop
so Cloud Code is now helping build itself and it
demonstrates the power of self-improvement as it
speeds up its own development it's incredible how
Cloud Code empowers developers like yourselves to
get more done i think back to when I was building
Instagram our team was between two and six
engineers you know before we got acquired

[00:45]
and we were supporting two mobile platforms we
would have been able to produce prototypes in
days and not weeks if we had agentic coding
products like this we've talked a lot about
building performant reliable agents now agency
without responsibility is dangerous especially
when you're talking about something that's
self-improving like our cloud code uh product
and even more so in enterprise settings with
stringent security and compliance requirements
i think widespread adoption of agents will require
improving model discernment and judgment around
confidentiality decision-making and coordination
so our models are already good at this but we'll
continue to improve making sure that they know
what's confidential they know what to reveal
um and that you can trust them in a production
setting that's why every feature that we build
around our models incorporates what we call
architectural safety checkpoints and controls
not just cart blanch agents pausing on major
decisions while users can define which actions
need human approvals which we've also built into
the model context protocol they're robust against

[00:46]
exploitation we test them we battle test them you
know uh a lot around things like prompt injection
and they're also transparent by design with
clear feedback loops and observable behavior
when you trust your agents to act autonomously
you're free to focus on in innovation instead of
mitigation another area we've invested heavily in
is interpretability the science of understanding
exactly what's going on inside the minds of AI
models dario recently wrote about the urgency of
understanding how our AI systems actually work if
you read his essay the urgency of interpretability
what he calls the race between model intelligence
and interpretability effectively we want to be
able to give our AI an MRI to see what what
it's thinking about and spot any potential
problems like deception so we can steer it in
the right direction when I joined Enthropic I
was excited about how our research pipeline could
directly fuel our products take Golden Gate Claude
i pushed the ship that's in our second my second
week at Enthropic because it didn't feel like it
was just a good research paper it would make a
fantastic demo a visceral demonstration of how

[00:47]
interpretability works in action when we amplified
the golden gate bridge feature inside the
uh uh clawed neural network we saw that suddenly
we could see what it means to manipulate the
inner workings of AI and in this case make
it deeply obsessed with our favorite bridge
uh the techniques that we used to create Golden
Gate Claude could in the future help us reduce
uh model harmful model behaviors or improve model
performance for specific domains and as we start
employing virtual collaborators around companies
my hope is that we can lean on techniques like
interpretability and auditability to be a
cornerstone of their work so we can figure
out what they're doing at scale these are the
kinds of breakthroughs that that are going to
help us transform abstract research into tangible
product capabilities as you saw earlier we're now
at the point where AI models can handle hours of
autonomous work and that's a capability that's
doubling every several months but raw model
capability alone isn't enough to unlock these
multi-hour workflows in practice agents also need
access to real world information a connection to

[00:48]
your existing systems and costefficient scaling
that's why we're launching four interconnected
capabilities to help power agents with context
and help them scale so first off starting today
you can now connect the model context protocol
directly through our API mcp is already being used
by Microsoft Google OpenAI Block Atlassian Zapier
Linear and many more this was the dream list when
we started creating the MCP protocol and we open
sourced it this was the dream list like maybe one
day we'll get these companies to adopt it it's
less than a year and they they've all um come
on board mcp acts as the universal translator
and connector for AI agents enabling seamless
connection to your existing system without needing
to write a custom bespoke integration every single
time this lays the foundation of what could
become the agent economy where specialized
agents have access to the data and tools they
need to tackle complex challenges second web
search gives Claude real-time access to current
information this is intelligent data augmentation

[00:49]
that allows Claude to reason about current events
market trends and emerging emerging technologies
it's really powerful in combination with the MCP
feature as well you can imagine searching across
an internal knowledge source making some uh new
uh insights and then going off and searching the
web to contextualize them third the files API
is available today in the API to streamline how
developers access and store documents simplifying
development workflows we're also releasing a
cookbook to help developers build that memory
functionality that I mentioned directly into
their applications these new cloud for models
have shown significant improvement in what we
call self-managed memory so you'll find that this
works surprisingly well and it can be achieved
with very little additional overhead by using
the files API as we demonstrate in that cookbook
you'll see claude both read and write to these
memory files and maintain contact context over
time last power needs to be practical and scalable
we want to ensure that we can grow with you from
prototype to production to millions of users
so that you're able to control cost and improve

[00:50]
efficiency we want cloud to work for you as you
succeed and reach massive scale that's why prompt
caching was our most requested feature one of
our most popular API features with prompt caching
customers can provide Claude with more context
uh and background knowledge and example outputs
reducing costs by up to 90% and latency by up to
85% for long prompts now every customer I talked
to had one very clear request on prompt caching
that we're delivering today which is a longer time
deliver TTL so in addition to the five minute TTL
we had out of the box with prompt caching today
we're launching a premium 1hour TTL which is a
12x improvement that dramatically reduces cost for
longrunning agent workflows this infrastructure
makes agent applications viable at scale so these
capabilities all compound when we think about
building features into the API we don't think
about them as one-off we think about how do they
complement each other how do they form a cohesive
story claude can now execute code understand your
systems access current information on the web

[00:51]
creating the foundation for agents that operate
with full context even for longunning tasks and
it can use the files API to maintain memory and
context during that entire execution everything
you've seen this morning is just the beginning
our road map continues to build on three pillars
the first is industry-leading agentic tools and
applications so you can use cloud autonomously to
handle hours of work knowing it can use the code
environment uh code execution tool to execute code
in its own environment cloud code is now generally
available integrating with VS Code and Jetrain so
you can use the extensive SDKs to build your own
custom workflows including inside GitHub we'll
continue to push on integrating more context in
the API our updates today allow you to bring the
bring this context via the model context protocol
as well as build on real real-time updates from
the web and execute uh complex workflows across
any data source and across anything in the API via
MCP and finally efficient scaling as of today you
can use expanded 1hour prompt caching to optimize

[00:52]
performance and cost at scale each advancement
builds on what we've discussed today with Cloud
4 as the foundation Opus 4 for your most complex
uh agentic workflows Sonnet 4 as your daily driver
for everyday intelligence we're enabling a new
class of applications code execution expands the
hours of work that cloud can do mcp expands the
comprehensive information that cloud can retrieve
and our platform updates ensure our models become
increasingly efficient for every dollar spent
we're actively learning from developers like
yourselves uh to how you use these tools so please
keep the feedback coming i love API feedback if
you don't know this about me like absolutely like
ping me uh I love hearing the feedback and how we
can continue to improve the API for developers or
yourselves and MCP is a perfect example of this
it started as an internal idea and then began and
graduated to community experimentation and now
it's a core platform feature if you watch the
Microsoft Build keynote they're building MCP into
so much of their uh of their real infrastructure
as well we want to create an ecosystem of AI
agents where we have the feedback loops to make

[00:53]
them actually useful for you today we stand at a
major threshold our latest models combined with
all the latest tools that we've released are
giving the seeds of a new era the future isn't
about AI doing human work it's about AI helping
humans do superhuman work and I'm really excited
to build this vision together with you and I
can't wait to see the kinds of applications it
powers for all of your companies and to show you
what's possible I'm next going to hand the mic
to Catwoo from our product team to demonstrate
how accessing our new models inside Cloud Code
transforms your development workflows helping
you ship complex multi-day tasks in a single
conversation welcome again to Code with Claude and
thanks again hope you enjoy the rest of your day
hi everyone I'm Cat Woo product manager for
Cloud Code as Mike mentioned we recently

[00:54]
launched Cloud Code our agent coding
tool in research preview claude Code
gives developers direct access to the
raw power of Enthropics models right
where they work in their terminals
as of today quad code is generally
available throughout computing history
we've continually moved to higher levels
of abstraction from machine code to assembly
to highlevel languages with cloud code and
increasingly agentic models we're
witnessing another step forward
developers are shifting from asking for
specific functions to describing entire
features guiding AI and changing how software
is built today we're bringing the new Claude 4

[00:55]
models to Claude Code making it an even
more powerful and capable coding agent
and on top of new models we're releasing several
new features in Cloud Code focused on making it
a more versatile coding agent across your whole
dev life cycle first Quad Code now integrates with
VS Code and Jet Brains bringing it to familiar
interfaces for millions of developers as Cloud
Code works you can now see its proposed changes
in line in your editor we're also releasing the
Quad Code SDK which allows developers to use Quad
Code as a building block in your applications
and workflows the possibilities are endless
with the SDK to showcase these possibilities

[00:56]
we're releasing an open-source example of the
SDK in action with Claude Code in GitHub you
can tag Claude directly on poll requests and
issues in GitHub and Cloud Code will respond
to reviewer feedback fix CI errors and add new
functionality with these additions Cloud Code
now works everywhere you do acting as a virtual
teammate across all surfaces in the terminal for
deep development work in remote environments
like GitHub for automated workflows built on
the SDK and in the IDE for seamless review
all in Quad Code is a versatile coding agent
for accelerating development wherever you are
whether you're working directly with cloud code
interactively or using it asynchronously great
my favorite part let's see what these updates

[00:57]
look like in a demo i'm going to show Quad Code
tackling a real dev task in a product that many
of you are familiar with we'll use Excaladrol an
open- source whiteboarding tool and ask Quad Code
to implement one of their most requested features
adding a table component how many of you have
gotten that feature request that's been on your
backlog for ages that you know your users would
love but you just haven't had the time to build
this is the kind of task that we can handle much
faster with cloud code normally for a task like
this I would set call to work make some coffee
catch up on email and Slack and come back when
the outputs are ready but I only have 10 minutes
with you all today so let's show a sped up but
real workflow here's the Excal repo open in VS

[00:58]
Code let's write a prompt to tell Cloud Code
our requirements we'll ask Quad Code to add a
table component that supports custom dimensions
drag to resize and all of Excal's other styling
options here's where it gets exciting quad
Code will first create a to-do list for how
it'll approach the entire problem then we can see
that Quad Code will start to explore the codebase
starting with the file that we already have open
for context the best part of the ID integration
is the ability to see diffs in line in the
editor this way you can see the surrounding
code for more context so you can accept changes
with confidence or give quad code feedback
we can approve each edit as Cloud Code works or
we can let Quad Code continue making edits with

[00:59]
auto accept mode letting us balance visibility and
control in this demo we gave Quad Code the ability
to make edits run lint and tests and make PRs so
Quad Code worked for 90 minutes on this task i
wish I could show you the whole thing but we need
to speed things up what you're seeing is actual
unedited output from quad code an hour and a half
later and it's done it added table functionality
wrote tests to validate the change and iterated
until lint and test passed this normally required
us to understand the codebase architecture and
how every single other tool was implemented
in this case cloud code is literally doing
hours of work for us pretty impressive right
now now let's run Excal locally and
just make sure the feature works as

[01:00]
we expect let's check that we have a fully
functional table component by making a three
row by three column table great we can
reposition the table we can drag to
resize we can change the border pattern and
color and we can add text to cells this also
integrates with Excal's existing UI all of
this was done with one prompt in Cloud Code
[Applause]
next we'll ask Cloud Code to use the GitHub
CLI to create a pull request for this branch
cool let's click in now we have our pull
request this is where the Quad Code SDK shines

[01:01]
it lets us build custom workflows on top of cloud
code including through GitHub actions for this PR
I'd like to update the docs instead of going back
to the IDE we can just tag at Claude and ask it to
update our documentation for us behind the scenes
this triggers a GitHub action that runs Cloud Code
claude comments on the PR as it works and it'll
it'll make a commit for us when it's done you can
also tag at Quad on a GitHub issue and I'll also
make a PR for you there with this feature Quad
Code meets users on even more surfaces where
they're already working devs no longer need
to context switch in their local environment and
you can even kick off runs on the go this is all
built on the Cloud Code SDK beyond powering GitHub
actions we've seen customers do incredible things

[01:02]
with the SDK including running many Quad codes in
parallel to fix flaky tests increase test coverage
and even do on call triage cool it looks like
the action is done running and we can see Quad
Code updating its comments to let us know what it
did let's click into the commit and see cloud's
changes it updated the documentation for us in
our PR and committed it without us having to do a
thing in just 10 minutes you've seen quad code
tackle a complex tasks that would have taken
days to implement manually writing hundreds of
lines of code integrating seamlessly with Excal's
existing features and doing hours of work for us
all of this is available to you today quad code

[01:03]
in GitHub actions powered by our SDK is available
in beta and you can install it by running a simple
command on the screen within quad the VS code
and Jetrains IDE extensions are also live in beta
just run quad from your IDE to install
last but not least our latest models
Quad Opus 4 and Claude Sonnet 4
are available to Cloud Code users
today quad code shows what's possible when
AI can truly understand and work with code
to build powerful agents whether coding
assistants or applications in any domain
you need more than just intelligent models
you need the right platform please welcome

[01:04]
Michael Gersonenhober who will show
you exactly how we're making that
possible thanks so much Cat and good morning
everybody thank you so much for being here
i'm Michael Gersonenhopper head
of product for the API platform at
Enthropic how many people here use AI generated
code already to write their applications yeah
and how many of those are using AI at their core
feature delivery like everybody here that's what
I thought most applications in the world will
be built by people already trying to solve the
world's problems whether you pass Ble Code
whiteboard interviews or getting started
with Vibes we're all software engineers now but
writing code is just the start you need to more
quickly build stable secure and maintainable
AI applications and that's why we built the

[01:05]
anthropic platform a complete toolkit designed
for building state-of-the-art AI applications
and agents our platform is already powering
most of the world's AI delivery in every
domain in finance Turboax helps millions of
customers confidently file taxes with federal
tax explainers in healthcare Novo Nordisk is
using Claude to draft clinical study reports in
less than 10 minutes instead of 15 weeks and the
world's best coding assistants run on our platform
each of these companies took Claude's intelligence
and turned it into something uniquely valuable for
their users at its foundation our platform
provides reliable access to Claude through
our model inference service which includes
the messages API and essential tools like
prompt caching to optimize performance
and costs over 50% of all input tokens

[01:06]
are cached on the platform doubling the
effective context window for our models
notion can put vast amounts of your documents in
the context window but maintain snappy real-time
execution this lets them adopt your voice
for creative writing and virtually eliminate
hallucination starting today we're extending
the cash time to live from 5 minutes to 1 hour
your agents can now maintain complex context
across the entire user session without breaking
the bank but that's just a foundation to build
powerful agents our platform provides powerful
building blocks as Mike shared we're releasing
two new capabilities the files API and a code
execution tool just like you and me there are some
problems that are easier to solve by writing a
script our platform lets your agents write their
own code in production just like you would these

[01:07]
new features join existing components like web
search for real-time information and citations
for grounding responses in source documents when
Thompson Reuters provides analysis to attorneys
in co-consel it's critical that they ground this
in their legal research in case law not in the
models training data our platform also connects
your agents and your data and businesses business
systems through model context protocol mcp has
taken off within our developer ecosystem with
over 3,000 integrations built by the community
whether your agent is accessing application
errors with Sentry triggering Zapier workflows
or creating Asana tasks the MCP connector enables
the model to interact with any tool data or app
your task requires and today the platform makes

[01:08]
it even easier by handling all the technical
complexity of tool and API calling for you
one thing that I want to emphasize about the
platform is the composability of the APIs they're
building blocks that work together as well as they
work apart helping to solve unique problems that
can't be coerced into a cookie cutter shape think
of Cloud as the architect and general contractor
for your agent it doesn't execute predefined
sequences or stack components randomly instead it
intelligently determines which materials you need
in what order and how they fit together to create
something far more powerful than any individual
element let me show you what I mean when you build
an agent for complex financial analysis Claude
intelligently assesses the task and orchestrates
the right tools using MCP to access financial
data spinning up code execution for statistical
analysis searching the web for real-time market
data and grounding insights with citations for

[01:09]
accuracy and compliance iterating and refining
based on results no hard-coded workflow no
brittle scripts just intelligent orchestration
that allows you to build powerful agent and is
seamless and seamlessly adopt new capabilities
as our researcher research brings them to life
we understand that prompt quality can make or
break an AI application which is why we created
dev tools like the prompt improver and evaluations
along with new observability features that help
you get to production and scale faster today
we're already helping developers build faster
with resources like cookbooks and guides that show
you how to implement features like memory into
your applications in the future we'll adapt these
for programmatic access and host them directly on
the platform so you can build even more powerful
agents that can research and remember on their own
in production everything we've built centers
on one goal helping you ship better AI faster

[01:10]
the anthropic platform isn't just tools it's
your path to building industryleading agents so
thank you all for being here today with me at at
Code with Claude i'll be on the floor the rest of
the conference but it's my privilege to welcome
Mario Rodriguez from GitHub to show you exactly
what this looks like in production [Applause]
[Music] thank you thank you Michael and I am here
um thrilled to be with you all we at GitHub are
incredibly excited to be part of this energy and
innovation and to share more about our deepening
partnership with Anthropic um this amazing team
everything GitHub does is anchor on two core
beliefs right number one is giving developers
choice and number two is giving them the best
developer experience at GitHub Universe last
year we kicked off the relationship with Anthropic
we announced Cloud Sonet 3.5 support in VS Code

[01:11]
and also in our conversational experiences and we
did this because we share fundamental belief with
Anthropic that AI can be a powerful force and a
force multiplier for developers augmenting their
capabilities not replacing augmenting their
capabilities and freeing them up to focus on
what they do best which is imagination and
creativity are of being a software developer
is being a whizzer since we haven't expanded
since then we have expanded the partnership
and experiences across VS Code Github.com and
our mobile app just to mention a few and today
I am delighted to announce that GitHub copilot
supports Cloud Sonet 4 and Opus 4 available right
now we just pulled the trigger right when Dario
announced it and every one of those services

[01:12]
That is what SIM shipping is all about let
me tell you it's really hard to do i don't
know if you've done it with every application
that you have done but it's incredibly hard to
do so thanks to all of the teams that make
that happen now as you all surely know the
future of code is what agent an agent mode
in VS Code is our autonomous perprogrammer
that can perform multi-step coding tasks based
on your natural language commands we've seen
firsthand how having cloud's intelligence
directly within the editor truly helps
developers understand complex code bases um
get faster code to production and increase
their productivity without ever leaving the
environment they already know love and trust
but even that right even that is singlethreaded
and in my opinion the future is multi-threaded you

[01:13]
think about it you're in your editor it becomes a
waiting room you're you're going faster but it's
still a waiting room and that's why on Monday
we took one step further and announces GitHub's
copilot coding agent now our coding agents this
are autonomous asynchronous peer programmer not
pair anymore now it's your peer programmer
embedded directly into GitHub copilo's coding
agent is currently powered by you probably guessed
it cloud sonnet uh and you know the reason we
chose that was very clear to me so let me just
walk you through three things that made that
decision possible number one our evaluation showed
that cloud demonstrated three main strengths right
strong software engineering and coding knowledge
powerful problem solving and that's very important
because sometimes you have to go and look at
the code and find the right place to make that
edit and then number three excellent instruction
following and specifically when thinking about

[01:14]
tools and MCP so when you're building for ejected
coding dealing with these things and large code
bases and system prompts you also need something
else which is caching right and that prom caching
bless you that prom caching support we get from
the anthropic API let us build these experiences
in a most cost effective way every token counts
and every token counts also on the price side so
the more we save those the better experience we
could provide our customers now on top of that
cloud was already the most frequently selected
model in agent mode so once we put all of those
things together it was very clear to us that
cloud set was the right model choice for agent
coding in GitHub scenarios now with cloud set
4 we seen improvement in all of these areas not
just aggregate benchmarks like sweet benchmarks
but more importantly on our real world evaluation
suites as well now our collaboration goes deeper
than this right it's not just about integrating

[01:15]
models directly we've been working closely with
Anthropic to officially adopt and scale MCP we're
combining intelligence if you think about this
like these models are incredibly intelligent you
stack like three PhDs on them with knowledge so
how do you get knowledge into that intelligent
model well the answer to us is MCP and tools
and that really unlocks the next acceleration
of developer tools recently Kevin Scott that's
Microsoft CTO made the analogy that MCP is like
the HTD protocol of the web and I completely
agree with him so if you have not adopted MCP
do it today right after this keynote go and play
with it it's that important it's the way you get
knowledge into these intelligent models now as
we step into this new era of software development
we're transforming GitHub's platform from an AI
infuse into AI native from creation to deployment

[01:16]
we envision this SDLC powered by an agentic
layer at the top of it that spans that inner
where you are coding and that outer loop those
asynchronous experiences and you are going to be
an active collaborator every single step of the
way the reason why we say co-pilot is the human
is at the center and then there's agents helping
you that is why we're announcing a new partnership
that integrates what Kai just showed you cloud
code and the extensible cloud code SDA directly
into GitHub's agent platform this opens up new
possibilities to customize cloud code remotely
invoke it from new surfaces that are embedded into
GitHub and our workflows again all on the GitHub
platform now we're already done a lot uh but the
journey with anthropic is still just beginning in

[01:17]
our opinion we believe that by bringing together
GitHub's deep deep understanding of developers
and Anthropic's AI capabilities through cloud
and the platform APIs we will and we can unlock
a future that is more intuitive more efficient
more ultimately more human that human power is
important so I'm excited to see what we continue
to build together and also what each of you
builds with us so thank you so much and please
welcome back to the stage Mike Kriger thank you
sir hello again and thanks again to Mario
to Michael and to Cat um I love the GitHub
integration the last project I did I actually was
like "Oh I can actually just install cloud code
into a GitHub code space." And all of a sudden
I have Cloud Code against the repo that I've

[01:18]
already been building it was really great to hear
from each of them and hear all about the exciting
work being done with Cloud so to close out the
show I'd like to dive a little bit deeper into
Cloud 4 our research direction uh and what
developers can expect next from Enthropic um
so please help me welcome back to the stage Dario
for our one-on-one conversation welcome back Dario
hello again this is great this is like our
one-on-one in front of the whole audience this is
great um so Cloud 4 uh uh is out cloud Sonet 4 and
Cloud Cloud Opus 4 are available um what excites
you the most about the Cloud 4 models and how does
it change your thinking about what's possible in
the next 12 months yeah so um I I think abstractly
the thing I'm most excited about is you know every
time you have a new class of models there's like
more you can do with it right so uh uh you know
we're we're we're going to be releasing uh models
after Claude 4 there'll probably be a Claude 4.1
at some point just like we did with uh with Sonnet
uh uh 3.5 and I think we're just at the beginning

[01:19]
of of of of you know what what what we can do
with the new the new generation of model in
terms of tasks i think the autonomy is going to
go uh uh is going to go much further than it has
already just the ability to give you know set
your model free and and give it the ability to
you know do something for for a long period of
time i think we're I think we're very much very
much still still at the beginning of that um uh
I'm I'm actually increasingly excited about the
models for cyber security tasks i mean you can
think of cyber security as like a a subset of of
of of coding tasks but they tend to be higherend
coding tasks and so I think we're maybe finally
hitting the threshold for that and then as a
as a former biologist I'm I'm always excited
about use of the models for uh for you know
biomedical and kind of kind of kind of detailed
uh scientific research work which I think opus
and opus in particular is going to be good opus

[01:20]
in particular I think is going to be particularly
particularly strong at that um it really connects
I think to machines of loving grace so how does
cloud 4 fit into that trajectory overall i like
to joke that people think of Machines of Loving
Grace as an essay and I think of it as a product
road map for the next few years and curious how
Cloud 4 fits into that journey yeah it was sort
of a product road map that I wrote without knowing
how to how to actually get to it and and kind of
said all right guys then this is your work this
is your job um uh yeah uh you know we're I think
we're increasingly thinking about on the biology
side of things and and software is part of that
right where and you know increasing amount because
biology increasingly involves data even involved
data 10 years ago when when I uh when I was
a biologist uh uh I I think I think I think
more and more of it is is is going to be okay we
have these models that know a lot about biology
and they can help write code and so if you're a
computational biologist I think these models will
will really accelerate what what you can do and
you know we have a number of customers who are
who are who are trying out the models for for
these tasks i guess we'll we'll get to that in

[01:21]
a bit yeah I think uh one of the first hackathons
we did after we uh released MCP somebody hooked
up MCP to one of those like plotters that so to do
drawing and so cloud could draw for it's actually
really fun to like see what cloud draws for itself
but it was like the first one was like MCPs don't
just have to be connecting to digital systems they
could also be connecting to the real world so like
when you'll be able to drive lab equipment VMCP I
think is an interesting uh question for the soon
we'll be able to test Claude by connecting it to
a polygraph yeah I love that idea are you lying
who needs interpretability
when we have the polygraph um
uh you mentioned that moment where you were
you know convinced that Claude the claude
written content was was human written um any other
breakthrough moments in watching us all you know
uh dog food uh Cloud 4 or even try it yourself
that made you realize this model felt different
um you know I I didn't actually understand I
didn't actually understand the details but like
there were several people in our side there was
a moment a few weeks before the model launched

[01:22]
where someone said "Oh my god this model just
like oneshotted this like incredibly difficult
performance engineering task." And and no model
had ever had ever done anything like that before
i I I will say that there there's there's this
almost almost like superstitious process in the
model development where like it it it it somehow
all comes together at the last moment even if the
training plot process is all planned out like just
some of the models abilities maybe it's something
about their interaction with people maybe it's
something about like just making it the last bit
better matters maybe it's people getting used
to the model and prompting it but but you you
always find the the early versions of the model
um you know people are struggling to figure out
how to use them and then and then you finally get
to a point and people are like this works for me
all the time and there's that there's that alchemy
that happens somehow always the last moment if you
read uh the Creativity Inc by Ed Catmol he talks
about the same process with all the Pixar movies
like they're really bad until like two days before
they're supposed to go out and I feel the same

[01:23]
way about our models not that they're really bad
but they're like there's like they're not quite
there and then suddenly they click and we're
like I can't wait to get this out to people it
it doesn't make it doesn't make any sense because
like the training process is uniform and you know
you know you you would think that that it doesn't
work that way that it's all a rational process
but it's absolutely not there's no point on the
RL curve at all that that they come together it
comes together at the last minute i don't know why
it's a real moment um many people in the audience
are developers here and a question that I know has
come up internally as people you know think about
uh how AI is developing is which parts of the
software engineering job will AI take over um
and what becomes more important in a world where
we have autonomous agents being able to do do a
lot of software engineering yeah um so probably
like many people here I I read with great interest
uh Steve Jay's blog post a couple months ago uh
revenge of the junior developer uh he had some
uh he had some similar blog posts uh he had some
similar blog posts around that actually uh came in
to visit us even um uh um uh uh and and that laid
out I think the vision of where things are going

[01:24]
maybe maybe even better than I could which is that
we're gradually go we're gradually going to more
and more autonomy of the models right we had this
phase where you would do basically autocomplete
now there's this thing that I guess people have
called vibe coding um uh uh uh and and you know
then then we're going more to kind of like you can
dispatch the agents to to do things and I think
with with claude code we're going to go go more
in the direction of you know you can dispatch the
agents to do things and I'm sure we'll have other
product surfaces that that that allow you to do
that as well and I think we're we're heading to a
world where a human developer can kind of manage a
fleet of agents and say you go off and do this you
go off and do this you go off and do that but but
I think continued human involvement is going to
be going to be important for the quality control
to make sure they do the right things to get the
details right and so you know working together
on both the models and the product surface around
it to get the details right is going to be really
important i think it's also highlighted to me it
makes the stuff that is inefficient in your work

[01:25]
way more painful because it's taking you away
from like this flow of building and so at least
it's made me realize like where we're spending
too much time on crossunctional alignment and
you know road mapping when like we just should
be trying to get more building so it's I've I've
it's become more painful as the engineering part
has has been sped up as well um so there's endless
debate uh you know around the industry around you
know uh bigger models or smaller architectures
which will win in the long run um you're famous
for you know popularizing and and pioneering the
scaling laws paper what's your current take on
you know the extreme being is pre-training dead
is pre-training all that matter still and its
role you know relative to to post-training i
mean without getting too specific I would say that
you know the Clawed 4 models embody advances in
both pre-training and post-training um so we're
continuing to see the pre-training scaling laws
work the way that they've worked before um uh and
we're also continuing to see continued advances in
uh post-training and and they kind of they kind of
complement each other uh and I I think we're going

[01:26]
to continue seeing advances in both of those i
think we're also going to continue to scale up so
we have these these multiple trends these multiple
sources of exponential growth and they're they're
all going to compound with each other right that's
that's why I think all of this is going to go very
fast one of the reasons I liked Jiega's blog post
is that it was someone who was not me repeating
the mantra of like it's only going to be a year
or two until until these things are like you know
are basically peers to us it's insane that 37
was just in February right it's it feels like
a year ago but it was just three months ago i I I
know it i know it feels like it's like oh this is
this feels like an obsolete model or something
and you know it was it's less is like two and
a half months or something it's like the the time
scales are the time scales are compressing and I
often say that uh being in the AI field I will go
on a very brief digress be being in the AI field
it feels like you're getting on a a spaceship
from leaving Earth at relativistic speeds and
uh you know one day you wake up and you know it's
like you know one day on your spaceship two days

[01:27]
on Earth so you have to take in the news of two
days it accelerates one day on your spaceship
three days on Earth and and and you know that
that's that's just what it feels like being
being on this ride that resonates i've heard the
metaphor before but it absolutely does um maybe on
the post- training front one of the things that I
got really excited about seeing developed in Cloud
4 has been this concept of memory and having
the the model being able to manage it memory
maybe talk a sec about why that's important
and what that kind of enables uh sorry repeat
the question like for uh the model to be able to
manage its own memory and be able to handle those
long horizon tasks as well yes yes we have found
that to be uh very useful i think one one place
we found it to be useful is Pokemon right um uh
where the model's able to like remember its state
but you know presumably it's it's useful for many
things other than just Pokemon um uh uh but uh um
no I think I think it's great that you know the
model you know just as a human would like when I'm
thinking I'll write a bunch of notes and uh you
know then I'll like recall those notes at a later

[01:28]
time or you know that there's just a lot of lot
of intermediate work that I have to do that that
you know and models do that to some extent when
they when they reason when they have you know like
our our reasoning traces but uh you know not not
everything I do can be incorporated in one scratch
pad right there's like presentations there's um
you know individual documents that I that I write
and so models are the same right the the idea for
them to kind of you know be able to create files
to do things with those files to load data and to
kind of seamlessly interle those things right the
the one of the new features that we have is this
this kind of interled re interled reasoning and
taking actions and some of those actions can be
storing data recalling data again the affordances
that the models have are gradually converging
towards the affordances that a human has which
I think is is the way that it should be one of
my mind-blowing moments in Cloud 4 so far was
we added like basically a to-do list scratch pad
to cloud code and just watching it turn through

[01:29]
the to-do list and then as it thought of more
things to do add to the to-do list check things
off strike out what was no longer relevant it
really mimicked I think how people managed their
own work and how they think about uh completion
along the way and then the interled reasoning uh
and tool use as well i saw a write up this morning
on Mac stories where it was using a tool it was an
MCP and it hit a rate limit with the backend MCP
server and because it was doing the reasoning it
was long I was like hm I probably hit a rate limit
let me try this other approach to do this as well
and so like that ability to reason and remediate
as part of tool use I think is is really powerful
um I'd love to touch on race at the top so um uh
safety and and capabilities are often you know
uh thought of as being at odds with each other and
your thesis is exactly the opposite and that these
two things can move in tandem i found that very
inspiring and one of the reasons I joined here
but maybe touch on how you think of of race to the
top yeah so you know I think I think it it it uh
applies to things you know from the from the uh
from the very mundane and simple and commercial
to kind of you know the grand directions that
that that that that that that AI is going in

[01:30]
the future um so you know I you know I think
I think when we when we talk to customers we
have a number of customers who you know care a
lot about making sure that the behavior of their
AI models is predictable that it's trustworthy
um uh and I think that's aligned with what some
of we're what what we're trying to do in the long
term for uh you know making sure that models in
a more grand sense stay in line with human intent
um so there's there's this nice there's this nice
synergy here and you know I think whenever
we're able to do so whenever we think it's
reasonable or responsible to do so we do want to
provide tools for the community so M MC MCP MCP
is an example of that um I I myself was actually
surprised at the the pace at which everyone seems
to have standardized around around MCP i mean it
was it was very strange we released it in November
i wouldn't say there was like a huge reaction
immediately but then but then within 3 or 4 months
you know it kind of become it kind of become the
standard again there's again this this feeling

[01:31]
of like being on the spaceship accelerating from
Earth and and and you know experiencing you know
larger and larger time time dilation constants
yeah um where it's you know like you know think
of like USB and other standards you know think
of like standards in the '9s or the two like you
know this would take it would take years for
people to converge on something yeah and even
in talking to other participants in the industry
around MCP they're like we don't want to slow down
whatever is working on MCP like we do want like
some you know help on steering but like this is
you've captured lightning in a bottle let's make
sure it becomes the new protocol and the standard
by which we interoperate agents as well um uh
maybe tied together the race to the top i loved
your urgency of interpretability essay you have a
background in neuroscience as well can you talk a
little bit about how you see the co-development of
interpretability and um machine intelligence yeah
so um you know I think 10 years ago uh many people
thought that neuroscience would tell us about how
to do AI um uh and indeed there you know are a
number of former neuroscientists in the field i'm

[01:32]
not I'm not the only one there you know there are
other lab leaders some who have that uh who have
that background um and you know I found at a high
level there's some inspiration but I wouldn't say
I've said oh you know this is how the you know
this thing we know from the hypothalamus we can
use for you know for for for making these models
it's it's all been pretty much from scratch but
interestingly things have gone the other way more
which is that using interpretability we're able
to see inside models and although of course
they're not ex made in exactly the same way
the human brain is at at a you know the a kind
of superficial level there's there's a lot of
differences a lot of the conceptual patterns we
have found inside models sometimes they then get
replicated in replicated in neuroscience research
there was something about like high low frequency
detectors in vision um that uh was found via
interpretability via via one of one of the

[01:33]
people on Chris Ola's team and then a couple years
later a neuroscientist actually replicated it in
in animal brains um the idea that for example
vision models separate out you know they have
one path that that tends to correspond to color
and you know another path that corresponds to
uh you know uh h a brightness or to the boundaries
between objects these seem to be natural
distinctions in the world right that are that are
kind of there to be discovered and anytime you
have any kind of abstract learning system whether
it's artificial or biological you kind of discover
the same thing so it's very interesting i'm really
curious how the circuits paper ends up affecting
neuroscience research as well um let's move into
the 5 to 10 year time horizon um to the extent
that that is even possible in AI as as we move
relativistically maybe relativistically that's
probably one year in real time um when do you
think there'll be the first billion dollar company
with one human employee 2026 yeah I absolutely
buy that um do you have any advice for people

[01:34]
building with Claude um for the next year how to
think about building at that frontier as well yeah
um I you know I think there's like a lot of very
specific things you could say about like how about
how to use the models but I feel like because of
this whole like relativistic time dilation thing
this like speeding things up like almost all the
advice is drowned out by like one sentence which
is or maybe two words which is just be ambitious
um like build something that's greater than you
think is is possible and even if it doesn't
quite work yet another model will come out
in the next generation which right now is three
months but like probably it's going to go down
to two months then one month and you know then
then if I want to come up this year maybe I'll
be giving advice that's like oh you know don't
build anything today you know we're releasing
something today but by tonight it'll be you know
you won't want to be building with this tonight

[01:35]
i talked to a founder who started a company two
years ago in the sort of autonomous AI coding
agent space and he basically tried every single
model and his startup wasn't working and then it
was actually 37 where he's like my startup works
now and it was the same thing of like this thing
that I was trying that was really hard all of a
sudden is now um possible but hitting your head
against the wall actually sometimes can be useful
because you put all the other pieces in place and
and everything works except the model and then
when the model works it's almost like you've
built something that's like more robust than it
needs to And that can be like a positive property
um so so you know as much as I joke about like
oh you should you know you can just wait for the
next model actually hitting your head against the
wall as long as it's something that's like almost
possible if it's not like you know like three
years out from from what's possible um I think it
can actually be productive we saw that even with
advanced research internally like our our research
and cloud skills team had built a prototype of
this the model kind of lost its way it wasn't
good at using tools and then with 37 especially
with cloud 4 I think you'll find that it does
advanced research really really well as well and
it's because we were trying and kind of failing

[01:36]
along the way as well yeah it's it's almost as if
you want to run your you want to run your startup
as like speculative execution against the next
model right there's some kind of like I don't know
I love that yeah I think that's exactly right um
all right so last question to wrap up um for many
of us today um who aren't Dario we couldn't have
imagined the progress that AI has made and the
rapid pace of change what are you most excited
about for the coming year and in the next five
years um yeah so uh I think for in the next coming
year uh we are going to see incredible things in
in in code i would refer again to kind of the you
know taking where we are with cloud code and where
we are with the coding models and going from there
to kind of to kind of the agent fleets um I think
this will have an interesting effect in the world
which is I don't know that we've thought carefully
like from an economic or business perspective
about what happens when the cost of producing
software goes down it's kind of an assumption
an article of faith that you only make software

[01:37]
if it's only worth it to make it if millions of
people use it or at least hundreds of thousands
or maybe tens of thousands like you wouldn't make
you you know you you you you like wouldn't make a
whole piece of software for this event right like
you might throw together something but like when
it just becomes really cheap when it costs you
20 cents to like oh let's just let's just throw
let's just throw together something that you
know you know changes you know ch changes my
vision for this particular event or something
like that um uh I think the world is going to
be very different when these things can be made ad
hoc on a on a one one one oneoff basis in like a
few seconds for for less than a for for for less
than a dollar what are what is the role of the
developer there what is the role of businesses
what is the role of startups um and what is what
is the experience of the of the you know of the
of the people using it i think we don't know the
answer to any of those questions so that's
very interesting on the on the fiveyear time
scale I will return again to biology i think the
biomedical stuff will not be revolutionized in the

[01:38]
next year because it's it's kind of you know slow
to slow to happen but uh yeah yeah I hope that uh
five years from now we will have uh vanquished uh
many of the diseases that now uh that now exist i
love we'll leave it at that unfortunately we do
have to wrap up i feel like we could talk for
another 40 minutes so first I want to thank Daario
for spending time with us today thank you Dario
i also want to thank all of you who are here
in person and those watching via liveream uh
but before we close I almost forgot one thing um
as a special thank you to everyone who joined us
today at Code with Cloud in person i'm excited
to announce that each of you will receive free
access to Max 20X our highest tier plan
for three months so look out for that
i especially love using Macs with cloud
code so you'll be able to do that as well
so we can't wait to see what you build have
a great rest of your day with the different
um sessions and welcome again to Code with Claude
thanks for coming thanks for coming everyone

[01:39]
[Music]
[Music] oh yeah oh
[Music]
oh
hey hey

[01:40]
[Music]
hey hey hey

</details>


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

    

    

    

    

    

    

    

    

    

    

Agents
