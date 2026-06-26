<!-- source: https://claude.com/customers/vapi -->

Case study | Claude Platform

# Vapi turns natural language into production voice agents with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fce9da8250c46378f9920a_logo_vapi-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fce9db997307a8c2ac5cf3_logo_vapi-dark-mode.svg)

Industry:

Software

Company size:

Startup

Product:

Claude Agent SDK

Claude Code

Partner:

AWS

Location:

North America

~3x higher deep activation rate

for users who build voice agents through Vapi's Claude-powered AI agent

3x recovery rate after a failed first call

for users guided by Vapi's AI-powered setup agent

[Vapi](https://vapi.ai/) is an enterprise platform for building, deploying, and managing voice agents. The platform is API-native and deeply configurable, from audio ingestion and endpointing to tool-call structure and fallback logic.

## With Claude, Vapi:

* Shipped Composer, Vapi’s intelligent assistant that helps build and configure voice AI agents through natural conversation, from prototype to general availability in 2.5 months with a team of five engineers
* Made users nearly 3x more likely to reach 100 call minutes, Vapi's milestone for sustained platform usage, when they build voice agents through Vapi's Claude-powered AI agent
* Tripled recovery rate for users who engage Claude-powered guidance after a failed first call
* Doubled initial activation, defined as 10 call minutes, for users onboarded through natural language
* Enabled natural-language debugging of live agents, compressing hours of engineering time into minutes

## The challenge

Building agents with the Claude Agent SDK

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698395d5956e6e0e78f3e486_image-claude-sdk.jpg)

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Read more

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)Read more

Building agents with the Claude Agent SDK

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

## Strong signups, soft activation

Vapi gives teams a platform to build AI-powered voice agents that handle real customer calls without a human on the line. The platform exposes more than a dozen configuration points because the use cases demand it: a healthcare company with strict data residency requirements handling 250,000 monthly patient calls and a labor marketplace screening 50,000 applicants a month have almost nothing in common architecturally, but both run on Vapi. That depth of configurability was also a double-edged sword. Technical users could reach a prototype in a day or two. Everyone else hit a wall.

"If you were technical enough to read our API reference and wire up a call, you could reach a prototype in a day or two," said Jordan Dearsley, CEO and Co-founder. "If you were not, you were either in a support channel, a sales conversation, or you logged out."

New customer activation depended on documentation, example code, and Vapi's field engineering team. That was expensive in both directions: lost self-serve revenue from users who never activated, and engineering time spent on basic setup instead of strategic customer work. The goal was concrete: get a non-technical user from signup to a working voice agent in under 30 minutes through natural language alone.

## The solution

Introducing Agent Skills

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6902681b6935a6f61e64165c_og_introducing-agent-skills.jpg)

Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.

Read more

[Read more](https://claude.com/blog/skills)Read more

Introducing Agent Skills

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Introducing Agent Skills

Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.

## Selecting Claude for function-calling reliability

To close that gap, Vapi built Composer, a Claude-powered AI agent that lets anyone create voice agents through natural language conversation. The team ran production experiments across Claude Opus, Sonnet, and Haiku, alongside models from other providers. They used feature flags to split live traffic between models and measured tool success rate, error classes, and user-level outcomes.

For Composer, the criteria that mattered most were function-calling reliability, output consistency under tool orchestration, and latency. Cost mattered once the first three were satisfied.

"Claude's function-calling behavior under the kinds of agentic workloads Composer runs is meaningfully more reliable than alternatives we have tested," Dearsley explained. "When Composer needs to invoke a tool to update an assistant's prompt, add a new squad member, run a simulation, or pull a call log, Claude gets the schema right on the first try more consistently."

The Claude Agent SDK was the second factor. Dearsley built the original Composer prototype on the SDK, which reduced the amount of agent-loop and context-management code the team had to write. "That let us move faster, and it let us reach a level of agentic reliability earlier than we would have otherwise," he noted.

## Composer turns natural language into working voice agents

Dearsley built the first working Composer prototype in a single evening. From that overnight build to general availability took 2.5 months with a team of five engineers, led by Dev Seth, Manager, Product Engineering. A user types what they want ("build me an outbound agent that qualifies real estate leads, transfers hot ones to my sales team, and logs the call in HubSpot") and Composer takes over. Claude has access to a tool suite that mirrors the full Vapi API, selects and invokes the right tools, and streams results back with an approve/deny flow on any action that mutates state. The loop is multi-turn and persistent across sessions.

Scaling that to production meant solving a real architectural problem. "Our first version was a single giant system prompt with tools bolted on," said Seth. "The system prompt was consuming more than 50 percent of our context window before a single user message came in." The fix was a modular architecture with a runtime router, shared chat kernel, and pluggable UI shell. The result: adding Composer to a new product surface dropped from around 700 lines of frontend code to around 30. Claude provides the intelligence layer; the team built everything else, from the architecture to the observability to the fallback logic between the direct Anthropic API and Amazon Bedrock.

Composer now runs on more than 10 skills and a catalog of 100+ tools that reaches beyond agent setup. In a chat thread, Composer searches the web to fill in missing prompt details, provisions a new phone number, runs a simulation against a proposed change, analyzes a transcript, or computes fleet-wide metrics like p95 latency. Claude reaches the catalog through tool search rather than loading every definition upfront. Only the tools relevant to the current turn flow into context.

"The accuracy gap between Claude and the other models we tested widens with chain length and tool specialization," Seth said. "Composer often picks the right tool, chains a dozen of them in the right order, and tunes an assistant's settings across many interdependent configs. Claude gets the full chain right far more often."

Beyond Composer, customers building voice agents on Vapi can also select Claude Sonnet or Opus, via the direct Anthropic API or Amazon Bedrock, to power the intelligence layer of their agent. Claude is among the most heavily used models across Vapi's enterprise customer base.

"The accuracy gap between Claude and the other models we tested widens with chain length and tool specialization."

Dev Seth

Manager, Product Engineering, Vapi

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## 3x more likely to reach deep activation

Composer users are 2x more likely to reach 10 call minutes and nearly 3x more likely to reach 100 call minutes, compared to users who don't engage Composer. The recovery metric is especially telling: users who engage Composer after a failed first call are 3x more likely to reach deep activation rather than churning.

Vapi's solutions engineers now stand up customer-specific demo agents in real time during prospect calls. Composer can also read call transcripts, diagnose why a call went sideways, and suggest or apply a fix directly, compressing what used to be hours of debugging into minutes.

One moment captures the shift well: a customer flagged a configuration option that was exposed in Vapi's API but didn't yet have a UI surface. A team member asked Composer to make the change, and it worked, updating the configuration through the underlying API without anyone waiting for a UI to ship.

"We knew that if we could compress the time from 'I signed up' to 'I have a working voice agent,' we would materially change the trajectory of the business," Dearsley said.

"Claude's function-calling behavior under the kinds of agentic workloads Composer runs is meaningfully more reliable than alternatives we have tested."

Jordan Dearsley

CEO and Co-founder, Vapi

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
