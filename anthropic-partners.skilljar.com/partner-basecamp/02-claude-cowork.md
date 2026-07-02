<!-- https://anthropic-partners.skilljar.com/partner-basecamp/464538 -->
<!-- scorm-content: https://anthropic-partners.skilljar.com/content/wp/4hdejjwplbrm/1ss2o4pk0y01f/module-05-cowork.html -->

# Claude Cowork

Module 5 of 6

# Claude Cowork: *Execution* at the Knowledge Layer

Most AI tools assist knowledge workers. Cowork is built to act for them. This module covers what that distinction means in practice: architecturally, commercially, and in a client conversation.

Partner Basecamp
~22 min
SET B - DAY 2 PREP
2 practice scenarios

What you'll walk away with

## Three things you can do after this module

01

Explain what Cowork is and how it works architecturally, in language a CFO and an enterprise IT lead can both follow.

02

Describe the four building blocks (plugins, skills, connectors, scheduled tasks) that make Cowork configurable and scalable across a client organization.

03

Judge what makes a Cowork demo land with a client, and what kills one, so you walk in with something that actually moves the conversation.

The definition

## Claude Cowork: *agentic AI* for knowledge work

Start here. "Agentic" means it doesn't just respond. It plans, executes, verifies, and delivers. The output isn't a response you then have to action. It's finished work. That single distinction changes the relationship between a knowledge worker and AI from collaboration to delegation.

The technical foundation is the same Agent SDK that powers Claude Code. The difference is the delivery surface: Claude Code runs in a terminal. Cowork runs inside the Claude Desktop application, with no command line required. That design decision opens agentic execution to an entirely different user population.

Step 01

Understand

Cowork reads the task, asks clarifying questions if it needs to, and confirms scope before starting.

Step 02

Plan

It breaks complex work into discrete steps and decides which tools, files, or systems it needs to involve.

Step 03

Execute

Cowork works on multiple steps simultaneously using tools, files, and the web, including sub-agents for parallel tasks.

Step 04

Verify and deliver

It checks its own work, flags uncertainty where it exists, and delivers a finished output. Not a draft. Not a starting point.

Positioning context

## The arc from *response* to execution

Now that you understand what Cowork does, let's see how we got here. The Cowork positioning only makes sense against this backdrop. Understanding the arc helps you orient clients who are still in "chat mode" and don't yet see why agentic matters.

2023

AI as reference

Chat interface. Ask a question, get an answer, go do the work yourself. Valuable, but limited: the AI amplifies you only as far as you can act on its outputs.

All users

2025

AI as executor (for developers)

Claude Code brought agentic capability to the terminal. A developer could hand off a complex task and get it done. A qualitative leap. But still behind a command line.

Technical users

2026

AI as executor for everyone

Cowork extends that same class of execution power to analysts, strategists, ops managers, and finance leads. No terminal. No technical skill requirement.

Knowledge workers

The core shift

## From *assistance* to delegation

This is the framing that lands with business buyers. The "AI assistant" model keeps the human in the loop for every step. The AI produces, you evaluate, you revise, you act. That loop has real value. But it has a ceiling: the AI can only amplify your throughput so much if you're still the bottleneck.

The AI assistant model

You're always in the loop

The AI produces outputs. You evaluate, revise, and act on them. Throughput is amplified, but bounded by your capacity to process and execute.

Typical tasks

Drafting an email you'll edit and send

Getting a quick summary before a call

Brainstorming options you'll then evaluate

The Cowork model

You brief it. It delivers.

Cowork is designed to remove you from the loop for tasks that are well-defined enough to delegate, complex enough to be time-consuming, and important enough to need to be done well.

The right use cases

30-page synthesis pulling from multiple sources

Weekly operational report assembled from five systems

Competitive analysis due before a client meeting

The "coworker" metaphor is useful here: you give a coworker a brief, they do the work, they bring you something you can actually use. **The quality of what you get back depends on how well you briefed them.**

Competitive positioning

## Three differentiators worth knowing for client conversations

These come up in competitive discussions, especially against Copilot and other enterprise AI tools. Understand each one well enough to use them without slides.

Agentic architecture

Cowork plans, executes, verifies, and delivers. For complex tasks, it spins up sub-agents: specialized mini-instances running in parallel, each handling a focused piece of the work. This is architecturally different from a chat model with tool use bolted on.

Built-in planning and orchestration layer

Local file access

Cowork reads, writes, and creates files directly on the user's machine. Real .xlsx files. Real .pptx files. Real .docx deliverables that open in the native application. Not a formatted response. An actual file in the folder you pointed it at.

This distinction matters enormously to business users

Browser control

Through the Chrome extension, Cowork can navigate web portals, fill forms, and extract data from browser-based applications. If a client's data lives in a system without an API, Cowork can still reach it. This is often the thing that surprises technical buyers most.

Covers systems where no API exists

Technical depth

## How it works *under the hood*

Enterprise architects and security teams will ask about this. Know it well enough to answer with confidence. The office building analogy works for mixed rooms with both technical and business buyers.

The architecture layer by layer

CD

Claude Desktop

Runs on the user's macOS or Windows machine. The delivery surface. No command line required.

HV

Hypervisor

Creates and manages a virtual machine inside the app. Assigns a separate, locked environment to each user.

VM

Ubuntu Linux VM

The secured execution environment. Own kernel, own network stack. Where the actual work happens.

AI

Agent SDK + Sub-agents

The Claude Code binary runs inside the VM. Sub-agents handle parallel task execution, each with a clean context window.

The office building analogy (for mixed rooms)

Claude Desktop is the office building. The hypervisor is the building manager: it assigns separate, locked offices to each tenant but they share the building infrastructure. The VM is your secured office floor, with its own locks and air system. Nothing inside reaches outside without permission. The Agent SDK is your coworker: reads the brief, makes the plan, does the work. Sub-agents are the team members they delegate to. Mounted folders are the specific filing cabinets they've been given a key to. Not the whole archive.

Security model (three things for enterprise)

01

Local execution

Code runs on the user's hardware. Only API calls to Anthropic's models leave the machine.

02

Hardware isolation

The VM has a separate kernel. An exploit inside the VM cannot reach the host OS. Same model used by AWS, Azure, and GCP.

03

Admin egress control

Domain allowlists govern web access. OTLP telemetry exports to existing SIEM tools like Datadog.

Key concepts  ·  1 of 2

## Plugins and Skills: *scalability* and process encoding

Cowork's power comes from four building blocks. Plugins and skills let you standardize and scale. Connectors and scheduled tasks let you automate at scale. Together, they answer every enterprise question: how do we deploy this, how do we ensure consistency, and how do we measure impact?

These are the two building blocks that answer the question every enterprise client asks: "If this works for one person, how do I roll it out to five hundred?" They're also where consulting firms start seeing this as a platform play, not a personal productivity tool.

Concept 01

Plugins

Plugins are bundles of capabilities installed in one click. A plugin packages skills, connectors, and slash commands into a domain-specific unit deployable across an organization. Think of it as the enterprise distribution mechanism. A legal ops plugin might bundle a contract review skill, a Salesforce connector, and a set of predefined outputs, all pre-configured, installed once, available to every user with no individual setup. No variation in how it's configured.

**Selling angle:** This shifts the conversation from personal productivity to functional capability. You're not pitching a tool. You're pitching a standardized capability deployed across a practice or a team.

Concept 02

Skills

Skills are detailed instruction sets that encode a specific workflow. Write once, deploy across the organization. Every user gets the same quality, every time. A meeting prep skill, for example, pulls calendar events for the next 48 hours, searches email for related threads, checks Drive for shared docs, and generates a briefing document with attendee backgrounds and recommended talking points. A 30-minute manual task that runs automatically when invoked. Skills encode a process, not just a prompt. If your best analyst approaches competitive research in a particular way, you can encode that workflow and give it to every analyst in the organization.

**Selling angle:** For your organization, skills are also how you productize capabilities. A firm that builds a strong library of vertical-specific skills has a differentiated offering that competitors cannot easily replicate.

Key concepts  ·  2 of 2

## Connectors and Scheduled Tasks: *live data* and operational infrastructure

These two concepts shift the conversation from "what Cowork can do" to "what Cowork becomes" inside an organization. Connectors are the integration layer. Scheduled tasks are where Cowork crosses from powerful tool into infrastructure.

Concept 03

Connectors

Connectors are live integrations with external systems: Google Drive, Slack, Salesforce, Jira, and more. Built on MCP (Model Context Protocol), Anthropic's open standard for giving AI models access to external tools and data. The key word is live. Connectors don't pull a static snapshot. When Cowork pulls a Salesforce opportunity for a briefing doc, it's getting current data. When it posts a summary to Slack, it's actually sending the message. Connectors run with the permissions of the user who authorized them. Cowork doesn't escalate privileges or access systems the user doesn't already have access to.

**Selling angle:** For partners with existing integration practices, MCP is an opportunity to build proprietary connectors that extend Cowork's reach into client-specific systems. Recurring implementation value: the connector becomes infrastructure the client depends on.

Concept 04

Scheduled Tasks

Scheduled tasks let you set Cowork to run workflows on a schedule: daily briefings, weekly reports, monitoring dashboards. Configure once, runs on autopilot. This is where Cowork crosses from "powerful tool" into operational infrastructure. A weekly competitive intelligence report that used to take a junior analyst half a day runs automatically every Friday morning and lands in the right inbox. A daily operations brief assembled from five different systems is ready when the team arrives. That's not assistance. That's automation at a level that used to require bespoke engineering.

**Selling angle:** For operational leaders who are skeptical about AI, this is the most compelling entry point. The value is obvious and measurable: hours saved per week, consistent reports delivered on time. Clear ROI story with low adoption risk.

Practice scenario  ·  1 of 2

## Claude.ai or Cowork? Put the distinction to work

This question comes up constantly with clients. The short version: Claude.ai is for collaboration. Cowork is for delegation. Both have a place in a client's AI stack. For each scenario below, decide which tool you'd recommend and why.

Scenario A

A consultant at a partner firm wants to brainstorm messaging angles for a new practice area launch. She'll write the final copy herself but wants raw material and a sounding board.

Claude.ai
Cowork

Scenario B

A finance team needs a 40-page synthesis report pulling from internal SharePoint documents, three analyst databases, and last quarter's Salesforce pipeline data, delivered by end of day.

Claude.ai
Cowork

Scenario C

An account exec wants a quick summary of a 12-page client proposal before jumping on a call in 10 minutes. He'll read it himself and take notes as he goes.

Claude.ai
Cowork

Scenario D

An operations lead wants a competitive intelligence report assembled from six sources every Monday morning, ready in his inbox before the weekly leadership standup.

Claude.ai
Cowork

The rule of thumb

Claude.ai is for collaboration: quick questions, brainstorming, drafting where you're actively in the loop. Cowork is for delegation: complex, multi-step work where you want to brief it and get a finished output. Both belong in a client's AI stack. Help clients think about which work belongs where. That framing builds more durable adoption than trying to do everything with one product.

Answer all four scenarios to continue

Customer spotlight

## What Cowork looks like when it's *working*

Before we get to demos, here's a real example. The Jamf story matters because the problem is universal: every large organization has clunky internal processes built around tools that were never designed for the work being done on them.

"

You're interacting with it creating UI elements on the fly. I've been at companies where a team of 40 people builds a React portal that's less inventive and less helpful.

Nick, Engineer  ·  Jamf

The problem

Jamf uses a seven-facet performance review spreadsheet for engineering self-evaluations. Engineers found it overwhelming. Not because they couldn't answer the questions, but because the flat format created cognitive overload. Completion rates were low. Response quality was inconsistent.

The Cowork solution

A skill that turned the spreadsheet into an interactive guided experience with branching logic. Engineers walk through each facet with context, examples, and conditional follow-up questions. The output still populates the same spreadsheet. No change to the downstream process. Just a completely different experience of doing it.

45 min

to build what Nick compared favorably to a full React portal built by a team of 40 engineers

Question to bring to your clients

What's your version of the performance review spreadsheet?

Practice scenario  ·  2 of 2

## What makes a Cowork demo *land* with a client

A bad demo loses a customer faster than anything. The bar has risen significantly: clients have seen a lot of AI tools look impressive in a controlled setting and disappoint in practice. For each demo approach below, judge whether it's strong or weak.

Demo approach A

You ask Cowork to summarize a one-page brief you hand it. It produces a clean three-paragraph summary. You show it to the client to demonstrate how fast it works.

Strong demo
Weak demo

Demo approach B

You give Cowork a competitive analysis task that would take a senior analyst three hours to complete. You brief it with real context. While it runs, you show the client the parallel execution in progress, then walk through the finished output together and iterate on one section live.

Strong demo
Weak demo

Demo approach C

You write a one-shot prompt, hand it off to Cowork, and wait for the output without any interaction. The output looks good. You send it to the client as an attachment after the call.

Strong demo
Weak demo

Demo approach D

You pick a task the client has specifically mentioned as a pain point: a report that pulls from five systems and takes two days to compile manually. You build the demo around their actual problem, using their language, scoped so Cowork moves into execution in the first 60 seconds.

Strong demo
Weak demo

The four principles of a great Cowork demo

Show real work

Aggregating, synthesizing, creating actual artifacts. The output should feel like watching a skilled colleague work.

Use ambitious problems

A task that takes an analyst three hours is a better demo than a task that takes three minutes. The contrast is where the value lives.

Show iteration, not one-shot

Back-and-forth shows the AI-as-coworker model. One-shot makes it look like fancy autocomplete.

Make it theirs

Generic demos close fewer deals than specific ones. Build the demo around a problem the client has actually named.

Judge all four approaches to continue

Module 5 of 6 Complete

## Cowork isn't a better AI assistant. *It's a different category of tool.*

You now have the architecture, the four building blocks, and a framework for **when to position Cowork and when not to**. The partners who win the early Cowork conversations are the ones who can explain the distinction clearly and show it doing work that a client recognizes as genuinely hard to do any other way. That's the bar. You're close to it.

Next up: Module 6

The Agent SDK

Cowork runs on the Agent SDK. But what is it, and what does it mean that partners can build directly on top of it? Module 6 covers the layer underneath Cowork and why it matters for the most ambitious client engagements.

Mark module as complete



Begin
