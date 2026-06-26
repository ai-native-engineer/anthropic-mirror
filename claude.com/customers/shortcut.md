<!-- source: https://claude.com/customers/shortcut -->

Case study | Claude Platform

# How Shortcut uses Opus 4.6 to tackle complex spreadsheet work for enterprises

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69aecadda48c863501e56369_shortcut-logo.png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69aecadda48c863501e56369_shortcut-logo.png)

Industry:

Software

Company size:

Small

Product:

Location:

North America

100,000+ users

Shortcut scaled from a consumer app to supporting more than 1,000 companies

Benchmark accuracy from 7.29 to 8.08

out of 10 after swapping to Opus 4.6 with no prompt changes

Introducing Claude Opus 4.6

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698529955ffaa6de831ec14e_opus%201%20(4).jpg)

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Read more

[Read more](#)Read more

Introducing Claude Opus 4.6

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Read more

[Read more](#)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

[Fundamental Research Labs](https://fundamentalresearchlabs.com/) is a two-year-old research lab focused on building more human-like AI. Their first commercial product, Shortcut, is an AI-powered spreadsheet tool that works across Excel, Google Sheets, and a standalone web and desktop app.

## With Claude, Fundamental Research Labs achieved:

* Benchmark accuracy from 7.29 to 8.08 out of 10 after swapping to Opus 4.6 with no prompt changes
* Almost half a trillion tokens processed through the platform in January 2026
* 100,000+ users at 1,000+ companies, spanning consumers, ad agencies, hedge funds, and management consulting firms
* Users report saving multiple hours per day on tasks like financial model buildouts, data extraction, and formula auditing
* Multi-agent architecture running 10+ Claude sub-agents simultaneously to analyze complex multi-sheet workbooks

## The challenge: Making AI work for spreadsheets

Spreadsheet tasks are deceptively complex for AI agents. A single financial model can contain hundreds of thousands of related cells across multiple sheets, and lacks the typical scaffolding afforded to coding agents to do the job. Nico Christie, who leads Shortcut at Fundamental Research Labs, previously worked in financial consulting where a team could spend weeks iterating on a single model before getting client sign-off. “AI is coming for spreadsheets now the same way it did for coding,” Christie said.

The work involves data extraction from documents, formula creation across interconnected cells, error detection, and model auditing. Tasks that involve finishing or auditing these models require both accuracy and an understanding of how sheets relate to each other.

Fundamental Research Labs built a benchmarking infrastructure to measure AI performance on these tasks: realistic, difficult Excel problems with verifiably correct answers. When they first launched their product Shortcut, the best models they tested scored in the 4-to-5.5 range out of 10. With other model providers, Christie reported that tasks failed roughly 70% of the time.

## Selecting Claude for spreadsheet complexity

After testing multiple model providers against its benchmark pipeline, Claude became the only model in production for Shortcut.

A key factor in the selection was how little adaptation Claude required. Other models required rounds of prompt engineering and benchmarking to work around model-specific behavior. Swapping in Opus required none. “There's very little Claude-specific prompting we have to do," Christie said.

Each subsequent Claude release has reinforced that decision. When Anthropic released Opus 4.6 in February, the score went from 7.29 to 8.08 out of 10.

“It was a step change in improvement,” Christie said. “Hard tasks that were impossible became doable. Medium tasks became easy. Easy tasks were just completely saturated. It was a total change, in the same way it was for coding."

## The results: Multi-agent architecture for complex tasks

Shortcut's architecture uses Claude in a multi-agent pattern. When a user asks Shortcut to audit a complex workbook, the system spins off multiple Claude sub-agents to explore each sheet in parallel, similar to how Claude Code operates. For a ten-sheet financial model, that might mean six to ten agents running simultaneously, each analyzing a different tab for errors, structural issues, and missing data. These agents gather context and feed findings back to a main agent.

Before executing changes, the system enters planning mode where Claude reviews the workbook, identifies issues, and asks clarifying questions. Once the plan is approved, Shortcut hands execution to a fresh Claude agent, which keeps the execution context clean and focused.

## Looking to the future

Each Claude model upgrade has delivered measurable gains for Shortcut without requiring engineering work. For Christie, that pattern shapes how the team thinks about its roadmap: as Claude's capabilities improve, so does what Shortcut can offer its users.

“Excel is used by a billion or so people, spreadsheets by two billion,” Christie said. “Shortcut’s mission is to give the feeling we get when using Claude to a billion Spreadsheet users around the world."

‍

"Shortcut’s mission is to give the feeling we get when using Claude to a billion spreadsheet users around the world."

Nico Christie

Co-founder, Fundamental Research Labs

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

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
