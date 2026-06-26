<!-- source: https://claude.com/customers/tasklet -->

Case study | Claude Platform

# How Tasklet built 24/7 business automation with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b97eb6b3c9cdc4593e7763_logo_tasklet-light-mode%20(1).svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b97ebac828c496b73459cd_logo_tasklet-dark-mode%20(1).svg)

Industry:

Software

Company size:

Startup

Product:

Location:

North America

450,000 agent actions per day

executed across thousands of customer agents

160% revenue growth

month-over-month

Most workflow automation tools require users to think like programmers: map every branch, handle every edge case, start over when something unexpected happens. Productivity startup Tasklet takes a different approach. Users describe what they want an agent to do and the agent reasons through how to get it done. And because everything runs in the cloud, the agents keep working 24x7 even when you close your laptop.

## With Claude, Tasklet achieved:

* 160% month-over-month revenue growth, reaching over $2.5M ARR within five months of launch
* 450,000 agent actions executed per day across all customer agents
* 2,000 new agents created daily by users automating everything from email triage to revenue reconciliation
* The ability to connect to any SaaS product or API via 3,000+ pre-built integrations, MCP, browser use, and an AI-powered feature that dynamically creates API connectors to new services
* A five-engineer team shipping production code 4+ times per day, supported by Claude Code

## The challenge

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

agent actions executed per day

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

agent actions executed per day

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

450,000

agent actions executed per day

## From email triggers to a general-purpose agent

[Tasklet](https://tasklet.ai/) grew out of Shortwave, an AI-powered email client the same team started building in 2022. Shortwave users kept asking for one thing: "Can the AI just run automatically?" They wanted their inbox to trigger a HubSpot update, a Notion edit, or a Slack message, without having to open a chat window every time.

The team started building that, then realized the idea was bigger than email. If an agent could trigger on inbox events, it could trigger on anything: webhooks, schedules, RSS feeds, form submissions. And if it was running unattended in the cloud, it didn't need to live inside an email client at all. In June 2025 the team started writing Tasklet from scratch. By July they had their first paying customers, and by October they launched publicly.

By the time the team started on Tasklet, they had years of production experience with every major model family. What they found was that most models handle single-turn questions well. The gap shows up when the task requires iteration.

## The solution

Introducing Claude Opus 4.6

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698529955ffaa6de831ec14e_opus%201%20(4).jpg)

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Introducing Claude Opus 4.6

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

## Selecting Claude for multi-step reasoning

When the team started building Tasklet, they made a deliberate architectural choice: let the model reason through the workflow rather than constraining it with predefined logic. "What if the workflow goes away and you just let the agent reason about what to do?" said Andrew Lee, Tasklet's CEO and a co-founder of Firebase. "The argument in the past was that this approach isn’t reliable enough because the models aren't smart enough. But the models are smart enough now.”

"For tasks where it's not just one question and one response, but where you need to call a tool, think, and iterate, the other models get off track after a few iterations," Lee said. "Claude can just iterate a lot longer at a high quality level."

That difference compounds in practice. A Tasklet agent might make dozens or hundreds of tool calls to complete a single task: reading an email, looking up a contact in a CRM, drafting a reply, checking a calendar, updating a spreadsheet. A small reliability gap at each step becomes a large success-rate gap over a full workflow.

Every LLM call in Tasklet's product goes to a Claude model. Users working on standard business workflows use Claude Sonnet 4.6; those tackling complex, multi-step reasoning can step up to Claude Opus 4.6 with extended thinking. The team found Claude particularly reliable in unattended operation: taking careful, considered actions when uncertain. "Safety and reliability matter a lot when agents are running autonomously without human oversight," Lee noted.

Developer Platform

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f5266ed232fd1354625a6_68c469d18f61fb5c21c81781_og-claude-api.jpeg)

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

Developer Platform

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Developer Platform

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

## The outcome

## The outcome: Connected agents that run overnight

Every Tasklet agent is a long-lived Claude conversation built around three core capabilities. Connections give it reach: 3,000+ pre-built integrations, plus the ability to have Claude read API documentation on the fly and construct a working connector for any HTTP service. Triggers give it autonomy: the agent fires automatically on a schedule or in response to events like a new email, a webhook, or a calendar entry. And computer use gives it a fallback: when no API exists, Claude spins up a browser in a cloud VM and navigates the web interface directly.

That last capability, along with the recently launched Instant Apps feature, is where Lee sees Claude's latest models pulling furthest ahead. Instant Apps lets agents generate live, interactive web applications on the fly, connected to the user's real data. A user can ask for a marketing dashboard and get one built in minutes, wired directly to their real accounts. The feature relies on Claude's code generation capabilities to produce functional UI rather than static output, something Lee says wasn't possible with earlier models.

The Tasklet team also uses Claude Code for all internal development. With five engineers, the team has shipped major architectural releases roughly every three weeks since launch. "It's amazing what we can do with five engineers and Claude Code," Lee said.

Five months in, Tasklet is growing revenue 160% month over month. Customer agents are executing 450,000 tool calls per day, and users are creating roughly 2,000 new agents daily. Use cases include intelligent email triage, revenue reconciliation across tools like Stripe and Ramp, multi-source research, deal desk pipelines, and competitor monitoring. One customer built an entire multi-agent venture capital firm back-office system in under a week.

What stands out in customer feedback is speed to value. Users report working automations in minutes, not the days or weeks a traditional workflow build would take.

Tasklet's roadmap is shaped by the same bet that started the company: every model improvement from Anthropic makes the product better without a rewrite. Near-term work includes team workspaces, shared agents, and faster & cheaper computer use. The longer-term vision is what Lee calls the "Cloud Agent OS": a primary workspace where business users consume other software through agents rather than switching between interfaces.

“2025 was the year of coding agents,” Lee said. “We think 2026 will be the year of general purpose knowledge work agents.”

"Claude can just iterate a lot longer at a high quality level."

Andrew Lee

CEO, Tasklet

## Related stories

[How Vercel built an ecosystem on the open skills standard](/customers/vercel-qa)How Vercel built an ecosystem on the open skills standard

How Vercel built an ecosystem on the open skills standard

Customer story

[Customer story](/customers/vercel-qa)Customer story

[Box builds document creation into its AI agent with Claude](/customers/box)Box builds document creation into its AI agent with Claude

Box builds document creation into its AI agent with Claude

Customer story

[Customer story](/customers/box)Customer story

[Juno helps people with chronic illness find patterns in their symptoms with Claude](/customers/juno)Juno helps people with chronic illness find patterns in their symptoms with Claude

Juno helps people with chronic illness find patterns in their symptoms with Claude

Customer story

[Customer story](/customers/juno)Customer story

[A conversation with Cursor on building coding agents for professional developers](/customers/cursor-qa)A conversation with Cursor on building coding agents for professional developers

A conversation with Cursor on building coding agents for professional developers

Customer story

[Customer story](/customers/cursor-qa)Customer story
