<!-- https://anthropic-partners.skilljar.com/partner-basecamp/464659 -->
<!-- scorm-content: https://anthropic-partners.skilljar.com/content/wp/4hdejjwplbrm/169e66to5dm2p/module-01-intro-ai-apps.html -->

# Introduction to AI Applications

Module 1 of 6

# Intro to Building *AI Apps*

Three market shifts explain why this moment is different. One framework helps you make sense of it in every client conversation.

Partner Basecamp
~22 min
SET A - DAY 1 PREP
3 practice scenarios

The Pattern

## A pattern worth recognising.

A Fortune 500 exec walks into a meeting and says: "We've got budget. We need AI. Go figure it out." Three months later, the thing the team built isn't being used. Not because the technology failed. Because they built the wrong thing.

What clients describe in almost every discovery conversation

It usually happens because teams skip the map and go straight to building. They have budget, API access, and capable engineers, but no framework for *what* to build or *how* it should work.

This session covers that map. By the end, you'll be able to explain why the opportunity is real right now, place any client scenario into a single framework, and recommend the right path, including when the right answer is to not use AI at all.

What you'll walk away with

## Three things you'll be able to do.

These translate directly into how you run client conversations, not just how you talk about AI in the abstract.

1

**Frame the AI opportunity for any client.** You'll understand the three shifts that explain why building with AI is viable *now*, and how to use them to calibrate expectations in a first meeting, not just in a pitch.

2

**Place any scenario into the right pillar and path, including when the answer is to not use AI at all.** That call is often where the most useful partner conversations happen.

3

**Walk a technical client through the three decisions that define any Claude deployment:** which model, which architecture, which API surface, and the reasoning behind each default.

Context first

## A lot changed in four years.

Three questions tend to come up in early client meetings: why is this the right time to act? Why would this be any different from the pilots that didn’t stick? And why bring in a partner when anyone can call the same APIs? There are good, specific answers to all three. Understanding them gives you a more grounded starting point for discovery conversations.

Three shifts created the opening. Each one maps to something concrete you can say.

Shift 1

Models became accessible

Shift 2

Capabilities crossed the threshold

Shift 3

The bottleneck moved

Shift 1 of 3

## Models became accessible.

For most of AI's history, using a frontier language model required a research team, GPU clusters, and months of training runs. That changed when the first public model APIs launched in 2020. For the first time, any developer could call a world-class model without owning any of the infrastructure that trained it.

hello\_claude.pyCopy

No ML expertise. No proprietary training data. No infrastructure to manage. Nine lines of code. The same model that cost millions to train is doing real work. When a client says they don’t have an AI team, this is what you show them. The barrier isn’t technical access anymore. It’s knowing what to build. That’s where the partner conversation starts.

Quick check

Client conversation

A client's CTO says: "We've looked at building with AI but assumed we'd need to hire a machine learning team first. That's not in the budget."

How do you respond using what Shift 1 gives you?

A

Acknowledge the constraint and suggest starting with off-the-shelf AI tools until budget opens up.


B

You don't need one. Nine lines of code gives you access to the same model that cost millions to train. The infrastructure question is already solved. The real question is what to build with it.


C

That's a common misconception. Most companies start small and grow the team as use cases prove out.


D

The cost of entry has come down significantly. It's much more accessible than it was five years ago.

Why this works

Shift 2 of 3

## Capabilities crossed the threshold.

Accessibility only matters if the models are reliable enough to stake a production system on. This is where most sceptical clients are stuck. They saw demos in 2021 or 2022 that impressed them but broke in real use. The MMLU benchmark tracks what actually changed. 15,908 questions. 57 subjects: law, medicine, coding. The line below is the human expert baseline. When a client says they tried AI and it didn’t work, this is the data to point to.

MMLU: 4 answer choices, knowledge-focused

GPT-3 2020

0%

GPT-3.5 2023

0%

GPT-4 2023

0%

GPT-4o 2024

0%

Human experts ~90%

Benchmark saturated. The field built a harder one. Enter MMLU-Pro: 10 choices, reasoning required.

MMLU-Pro : harder questions, 10 choices, requires reasoning

GPT-4o 2024

0%

Claude Opus 4.5 2025

0%

Claude Opus 4.6 2026

0%

Note: Claude Opus 4.7 (Apr 2026) does not report an official MMLU-Pro score. Anthropic's benchmarks for this release focus on coding and agentic tasks.

Below that line, AI works well enough for controlled demos. Above it, it’s reliable enough for production. Something you build a product around, put in front of customers, and charge for. When a client says they’ve been watching AI but haven’t committed, they’re usually anchored to the pre-threshold world. Show them where the line moved. The pilots they remember were below it. That tends to reframe the conversation quickly.

Quick check

Sceptical stakeholder

A VP of Operations says: "We ran an AI proof of concept two years ago. The demos were genuinely impressive. But it never worked reliably enough to put in front of customers."

What does Shift 2 give you to say here?

A

The models have improved a lot. What you saw then is very different from what's available now.


B

Two years ago is about when most companies started piloting. Timing matters a lot in this space.


C

Two years ago, models were below the human expert performance threshold. Impressive in controlled demos, but not reliable enough for production. That line has moved. What you saw was a demo-grade model. What we're working with now is production-grade.


D

Reliability issues are usually about implementation rather than the model itself. The technology was probably fine.

Why this works

Shift 3 of 3

## The bottleneck moved.

This is the shift that addresses the question clients often don't ask directly but are thinking about: if the models are commodities anyone can access, why bring in a partner? When models were below the threshold, the hard problem was “can the AI do this?” That question is mostly answered now. The hard problem is everything around the model: how you design the product, how you connect it to real data, how you get people to actually change how they work.

Model60%

The Application Layer40%

~0%

Prompts

System prompts, few-shot examples, instruction design

~0%

Context

RAG, tool use, structured outputs, memory

~0%

Evaluation

Measuring quality, catching regressions, building trust

~0%

Guardrails

Safety, monitoring, edge cases, human escalation

Everyone has access to the same APIs: same models, same capabilities, roughly the same cost. The differentiation isn't in the model. It's in how well you build around it: better prompts, tighter data connections, more rigorous evaluation, better adoption design. That's the application layer. And it's where partner expertise compounds in ways that raw API access can't replicate. When clients ask “why do we need a partner?”, this is the honest answer.

The model is a commodity. The application layer is the product. This idea runs through everything else this week.

Scenario: Shifts in practice

Client conversation

A client's Director of Innovation says: "We ran an AI pilot 18 months ago. Some things worked brilliantly in the demos, but nothing stuck after launch. Why would this time be any different?"

Which shift is most relevant to this client's experience, and how you'd frame what's different now?

Shift 1: Accessible

The models they used weren't accessible enough. Better API availability means faster iteration this time.


Shift 2: Threshold

Their model was below the performance threshold. It worked in demos but wasn't reliable enough for real production use.


Shift 3: Bottleneck

They focused on the model but didn't invest in the application layer: the product design, the integrations, the adoption work that makes something stick.


None of the above

This is a change management problem, not a technology one. The shifts aren't the right frame here.

The framing that lands

Before the framework

## Group these before we name them.

Five client situations. Sort them into three groups however makes sense to you. There are no wrong groupings at this stage. The point is to build your own logic before we introduce the categories.

0 of 5 placed

Group A

Group B

Group C

Reveal the framework

These three groups are the three pillars Anthropic uses to categorise every client problem. **Smarter Employees** is about giving individuals a tool. **Faster Processes** is about automating a defined workflow end to end. **Transformational Products** is about embedding Claude in something customers interact with directly. The framework puts a name to the logic you were already applying.

The Framework

## Three ways AI creates business value.

Anthropic organises every customer problem into three patterns. These are diagnostic categories, not marketing ones. They predict what you need to build, how you measure success, and what the change management looks like. When a client comes in, the first useful question is: which pillar? The answer shapes everything downstream, from architecture to timeline to how you frame the business case.

⚡

Smarter  
Employees

Claude for every knowledge worker

Claude Enterprise · Claude Code

25–50%

productivity lift, consulting firm

🔄

Faster  
Processes

Automate high-cost workflows

Claude Developer Platform

40 hrs → 1 hr

pipeline creation, data platform

🚀

Transformational  
Products

Embed Claude in customer experiences

Claude Developer Platform

56% avg

ticket resolution, support platform

Most clients can pursue all three, but each requires a different solution, different success metrics, and different change management. When clients conflate the pillars, it tends to produce the wrong design. Worth catching early.

Pillars in action

## Frameworks are useful. Examples make them stick.

One real case per pillar. Take note of the pattern for each problem's outcome. It explains what the engagement model looks like and where the risk and value typically sit.

Pillar 1A DevOps Platform

Problem

Field teams spent 3–4 hours per deal on RFP responses and competitive analysis: skilled time on repeatable work that scaled linearly with headcount.

Solution

Claude Enterprise across go-to-market teams. Employees use Claude with persistent Projects context to draft, synthesise, and analyse, delivering the same output in a fraction of the time.

Outcome

25–50%

Productivity lift. Time saved reinvested into higher-value customer engagement, not more headcount. **Pattern:** Start with Claude Code for developers, expand to Enterprise for broader teams. Lowest risk, fastest time to value.

See the approach →

Pillar 2A Data Integration Platform

Problem

Data pipeline creation required specialised engineers and took roughly 40 hours per pipeline. Business analysts had the domain knowledge but couldn't translate it into pipeline logic without engineering support.

Solution

A Claude API-powered assistant: users describe what they need in plain language, Claude generates the complete pipeline configuration: schema mapping, transformations, validation.

Outcome

40 hrs → 1 hr

Business users now self-serve. The engineering queue effectively disappeared. **Pattern:** Identify a high-cost manual process with clear success criteria. Build a workflow, not an agent. This is typically the highest-value engineering work in a partner engagement.

See the approach →

Pillar 3A Customer Support Platform

Problem

Traditional chatbots handled only scripted FAQs and could not reason through complex, multi-step issues, forcing human agents to handle the full ticket volume. Resolution rate stuck at ~30%.

Solution

A Claude-powered support agent that ingests a company's entire help centre, reasons through multi-turn conversations, takes actions via tool use, and escalates when its confidence is low.

Outcome

56% avg resolution

Within 30 days. Some customers hit 90%. Anthropic bought it rather than built their own, and hit 50.8% in a month. **Pattern:** AI becomes the product, not a bolt-on. Highest visibility, highest quality bar, most sophisticated engineering.

See the approach →

←→

Decision Framework

## Three paths. In order of complexity.

Before thinking about models, architecture, or APIs, the first question is: which path? Not every client problem needs AI. Not every AI problem needs Anthropic. Being clear about this early, rather than defaulting to a recommendation, tends to build the kind of trust that holds up when things get complicated.

Path 1

🚫

Don't use AI (or use a non-Anthropic model)

Sometimes a rules engine, a database query, or a competitor's model is genuinely the right answer. Saying so when it fits tends to build more durable trust than any demo. It's the kind of call that clients remember when the next, bigger conversation comes around.

Regex · decision trees · other providers

Path 2

⚡

Leverage Claude in our apps

Deploy Anthropic's products directly. Lower barrier, faster time to value, no custom development required. Claude does the heavy lifting. The client deploys and adopts rather than engineers.

Claude.ai · Claude Enterprise · Claude Code

Path 3

🔧

Build Claude into your apps

Custom solutions on the Developer Platform. Most flexibility, most decisions to make, most engineering effort. This is where most partner implementations live. When a client needs custom integrations, bespoke workflows, or a product built around Claude, this is the path.

Messages API · Agent SDK

Your engagement model

## Every engagement follows the same arc.

The frameworks from this session (pillars, paths, levers) all map onto a four-stage engagement lifecycle. Knowing where you are in that lifecycle shapes what questions are useful to ask, what decisions are ready to be made, and where the risk accumulates if you move too fast.

🔍

Discover

Find the real problem. Which pillar? What is actually broken?

Deliver & Engage

→

🔧

Design

Choose the path. Model, architecture, API surface.

Products & Platform

→

⚙️

Build

Implement. Prompts, context, tools, evals.

Build & Implement

→

📊

Iterate

Eval, harden, close the feedback loop. This is where production is earned.

Build & Implement

The most common failure mode in client work isn't technical. It's misaligned discovery. A client says "we need a chatbot." The real problem is "our support team is drowning and we're losing customers." Those two framings require very different solutions. It's worth investing time in the Discover stage. What you learn there shapes every decision that follows.

Scenario: Pillar and path

Client situation

An insurance carrier's head of operations comes to you. They have 400 underwriters, each spending 3–5 hours per deal pulling data from 6 different internal systems and synthesising it into a risk assessment. They want Claude to handle the research and synthesis, with human underwriters reviewing and approving the output before anything is acted on.

1

Which pillar does this problem belong to?

Pillar 1

Smarter Employees: giving underwriters a Claude productivity tool


Pillar 2

Faster Processes: automating a defined multi-step research workflow


Pillar 3

Transformational Products: embedding AI in customer-facing insurance products


Either 1 or 2

Hard to tell: it could go either way

The tell

2

Which solution path fits?

Path 1

Don't use AI: this is better solved with existing tools


Path 2

Leverage Claude in existing apps: deploy Claude.ai or Enterprise


Path 3

Build Claude into their apps: custom integration on the Developer Platform

Why this path

Path 3 deep-dive

## Three decisions define every deployment.

When a client chooses Path 3 (building on the Developer Platform), three architectural decisions shape everything that follows. Think of them as dials rather than checkboxes. Most production systems end up using more than one model and more than one architecture pattern. The question is where to start. Anthropic's consistent guidance: begin with the simplest option at each lever and add complexity only when the task actually demands it.

1

Which model?

Haiku 4.5

High-volume, cost-sensitive tasks

$1 / $5 per M tokens

Sonnet 4.6

Best balance of quality, speed, and cost

$3 / $15 per M tokens

Opus 4.7

Complex reasoning, highest accuracy

$5 / $25 per M tokens

2

What architecture?

💬 Augmented LLM

Single call with retrieval and tools. Start here.

⚙️ Workflow

Predefined code paths orchestrating multiple calls

🤖 Agent

Claude directs its own process. Most power, most complexity.

3

What to build with?

Messages API

Stateless. Direct model access, tool use, extended thinking. You manage the loop.

Agent SDK

Open-source. Self-hosted agent loop and tool orchestration. Powers Claude Code.

Start simple: Sonnet on the Messages API with an augmented LLM architecture. Add complexity only when the task requires it.

Capstone: Cold read

Client brief: read and respond

A healthcare network. 500 physicians. They want AI to transcribe and structure physician-patient conversations into visit notes, freeing up 30–40 minutes per physician per day. No existing AI tooling in place. Protected health information (PHI) is involved.

Your initial read

Before you see the options: what's your instinct on pillar, path, and starting model?

See the options →

Your initial read

Build your recommendation. Three decisions, in sequence.

Decision 1

Which pillar?

Pillar 1  
Smarter Employees
Pillar 2  
Faster Processes
Pillar 3  
Transformational Products

Decision 2

Which path?

Path 1  
Don't use AI
Path 2  
Leverage existing apps
Path 3  
Build into their apps

Decision 3

Starting model?

Haiku  
Fast, low cost
Sonnet  
Balanced
Opus  
Highest capability

Your recommendation

Pillar

Faster Processes

Path

Build (Path 3)

Starting model

Sonnet 4.6

Pillar 2 because the workflow is fully describable from start to finish: audio input, transcription, structured note output, clear success criteria. Pillar 1 would mean giving physicians Claude to work with however they like; this automates a specific task entirely. Path 3 because you need custom audio integrations and PHI-compliant infrastructure that Claude.ai cannot provide. Sonnet because clinical note quality rules out Haiku (accuracy risk is too high), and structured note generation at this scale doesn't require Opus-level reasoning.

Client flag: PHI handling requires a Business Associate Agreement (BAA) with Anthropic before any data processing begins. Raise this in discovery.

Apply it now

## One client. One starting position.

Think of a client or prospect you're meeting with in the next two weeks. A real conversation, not a hypothetical.

Which pillar does their biggest challenge belong to?

Pillar 1

Smarter Employees


Pillar 2

Faster Processes


Pillar 3

Transformational Products


Not sure yet

Need to ask more questions first

Which path would you recommend?

Path 1

Don't use AI


Path 2

Leverage Claude in existing apps


Path 3

Build Claude into their apps

You have a starting position for that conversation. Use the three shifts as context. Lead with the pillar diagnosis. The path follows from there.

Module 1 of 6 Complete

## The model is a commodity. *The application layer is the product.*

You now have the framework: **three shifts** that explain why the window is open, **three pillars** that categorise any client problem, **three paths** that structure how you respond, and **three levers** that define the technical architecture. The rest of Basecamp builds from here.

Next up: Module 2

Understanding Foundation Models

When a client asks "why does Claude sometimes get things wrong?" the useful answer isn't a marketing one. The next module strips back the abstraction and shows you what's actually happening inside the model when it generates a response.

Mark module as complete

Use ← → to navigate

Begin
