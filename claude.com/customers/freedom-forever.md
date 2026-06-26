<!-- source: https://claude.com/customers/freedom-forever -->

Case study | Claude Platform

# Freedom Forever automates permit workflows with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697cff85878a4b10b577a326_logo_freedomforever-light-mode.png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697cff89716ed55051dcaaa0_logo_freedomforever-dark-mode.png)

Industry:

Energy

Company size:

Large

Product:

Location:

North America

97.5% benchmark success

on complex web automation tests (39 of 40 runs passed), compared to 20–60% for alternative frameworks

~19,000 permit emails processed

in the first month of production

Introducing Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

See Claude Code in action—from concept to commit in one seamless workflow.

Read more

[Read more](https://claude.com/product/claude-code)Read more

Introducing Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b862e6ee6520aee5bc0741_vid-placeholder.avif)

[Next](#)Next

See Claude Code in action—from concept to commit in one seamless workflow.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b862e6ee6520aee5bc0741_vid-placeholder.avif)

Introducing Claude Code

See Claude Code in action—from concept to commit in one seamless workflow.

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

[Freedom Forever](https://www.freedomforever.com), the largest residential solar installer in the United States, handles the full lifecycle of solar installation—from sales and permitting through design, installation, and ongoing monitoring. The company has 3,000 employees, primarily field operations and installation crews, and a 50-person software and product team.

## With Claude, Freedom Forever:

* Achieved 97.5% success rate on complex web automation benchmarks where alternative frameworks hit 20–60%
* Processed approximately 19,000 permit emails in the first month of production, handling communications from hundreds of utility companies
* Built a unified agent framework connecting web automation, CRM workflows, file validation, and sales support
* Reduced agent execution costs to $0.20–$0.35 per run while completing most tasks in about two minutes

## The problem

Between a signed contract and solar panels on a roof lies a maze of permits. Every residential solar installation requires submissions to utilities and municipalities—each with their own third-party websites, forms, and approval processes. Freedom Forever processes about 5,000 individual permits per month, but each permit involves multiple touchpoints: inspection communications, receipt confirmations, payment requirements, correction requests, and approval notifications.

The permit team was drowning in email. Hundreds of utility companies send updates throughout the day, and processing this volume manually meant backlogs kept growing. Some emails sat unprocessed for weeks while customers waited in limbo, their projects stalled for reasons they couldn't see. "Installation timelines are our most important metric," said Rob Richardson, VP of Product at Freedom Forever. "We've strengthened our systems and processes so every customer gets consistent updates and support throughout the process.”

The company had experimented with AI coding assistants for a small group of developers, part of a broader push to build faster. But for complex agentic workflows—particularly web automation on third-party permit sites with cookie consent pop-ups, iframes, shadow DOM elements, and multi-step forms—they needed something more robust than existing frameworks could provide.

## Choosing Claude through rigorous benchmarking

Freedom Forever built a formal benchmark around their hardest problem: automating permit submissions on third-party websites. The team created eight internal mock sites replicating real-world challenges—simple single-page forms, multi-step workflows, blocking interfaces like cookie consent and pop-ups, iframes, and shadow DOM elements. They ran five iterations per site, comparing what each framework submitted against expected results, with video recordings to verify accuracy.

"Claude Agent SDK scored 97.5% on our benchmark—we couldn't break it," said Richardson. "The single failure was a rate limit issue from running dozens of parallel agents, not the agent itself. Other frameworks hit 20–60% at higher cost."

The team had explored alternatives, including building applications using other agent frameworks. Each showed promise in limited contexts, but Claude Agent SDK handled the full complexity of their web automation workflows. Beyond performance, the SDK proved to be the easiest to build on—the benchmark development and testing took about three weeks, and they launched their first production agents two weeks later.

## Building the permit automation system

Claude Agent SDK now serves as Freedom Forever's primary agent framework for production workflows. The system handles permit submissions on third-party utility and municipality websites, processes incoming permit emails in real time, and connects to their custom CRM for scheduling, task completion, file analysis, and human handoffs. A single, unified framework powers automation across the business.

The SDK was straightforward to build on—the core agent loop required little custom work, and it handled most underlying complexity out of the box. Freedom Forever built an internal "agent console" on top of it to manage workflows, but the foundation came together quickly. And as the SDK improves, they benefit automatically. "When structured outputs rolled out, we stripped out our custom workarounds and just turned it on," said Richardson. "That kind of speed matters." In addition, much of the internal tooling, benchmarks, and reporting infrastructure was itself built using Claude Code, Anthropic's command-line tool for agentic coding.

## The outcome

The permit email processing agent—their highest-volume deployment—processed approximately 19,000 emails in its first month of production, handling communications from hundreds of utility companies. The system categorizes incoming messages (inspection communications, receipt confirmations, payment requirements, correction requests, and more), extracts relevant data, and takes appropriate action. About 71% of emails are fully processed without human intervention; even cases requiring handoff have the human work dramatically reduced. Each execution costs $0.20–$0.35 and completes in about two minutes—two to five times less than the human equivalent.

But the real discovery came when they ran a backfill. The agent found emails that had been sitting unprocessed for an average of three weeks—a couple dozen customers stuck in limbo, waiting for action on permits that would let their installations proceed. The agent identified these cases and moved the projects forward, clearing a backlog the team hadn't fully grasped. "Installation timelines are our most important metric, and we've never had faster timelines and better quality," said Richardson. "I know Claude and our agent system is affecting that."

"The main limitation now is just opening up more workflows and going deep enough on each to remove substantial load from teams," said Richardson. "The limitations are on us building more tools and capabilities, not the agent's ability to orchestrate and make decisions."

## Expanding across the organization

Freedom Forever continues expanding Claude's role. They recently deployed a file validation agent that processes about 1,500 documents, validating utility bills against internal system requirements. These documents often include meter numbers and past usage data displayed in charts rather than text—information that traditional OCR struggles with. Many uploads are photos of someone holding the document in their hand; Claude handles these without issue.

"We even found cases where our validation rules had gaps," said Richardson. "By enabling web search, the agent was able to fill in missing information for deeper validation—and then commit those learnings to a knowledge base so future runs are even more capable."

The company also recently migrated their sales support agent from another framework to Claude Agent SDK. This system serves as an inbound support line where over 10,000 sales representatives can call or text to understand their pipeline, navigate company processes, and interact with internal systems.

The internal agent console they built on top of the SDK now serves as a platform for the entire team, with only a handful of developers working directly in the SDK layer while many more use the UI to configure skills and workflows. "We're going headfirst with Claude and the Agent SDK," said Richardson. "We see it as the future for a lot of our work and want to be deeply embedded."

"Claude Agent SDK scored 97.5% on our benchmark—we couldn't break it."

Rob Richardson

VP of Product, Freedom Forever

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

## Related stories

No items found.
