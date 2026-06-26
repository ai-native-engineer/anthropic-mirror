<!-- source: https://claude.com/customers/anything -->

Case study | Claude Platform

# Anything builds coding agent for 1.5 million users with Claude Agent SDK

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c4449cbdd758b4b0b599ec_logo_anything-light-mode%20(1).png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c444a5414f5966382739f3_logo_anything-dark-mode%20(1).png)

Industry:

Software

Company size:

Startup

Product:

Location:

North America

800,000+ apps

created in five months

91-96% agent success rate

with complex product builds from databases to App Store deployment

A non-technical founder built and is already selling a full recruiting platform. A creator with no engineering background published a social app to the App Store. Across [Anything's](https://anything.com) platform, 1.5 million users are turning ideas into working software products without writing code. Anything’s AI agent, powered by Claude and the Agent SDK, handles the full build: databases, backend logic, mobile deployment, App Store submission, and payments.

## With Claude, Anything achieved:

* 800,000+ apps built in the last five months by users, many of whom have never written code
* 91-96% agent success rate—measured by completion rates, agent self-reports, and user feedback—with complex product builds from databases to App Store deployment
* Evolution from simple single-page tools to full-stack, multi-platform applications with backends, mobile apps, API and AI integrations, and product paywalls
* Implementation in days rather than weeks
* Internal adoption of Claude across support, inbound sales, product feedback analysis, and codebase improvement

## The challenge

Choosing the right Claude model

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c2dd485d80024bc14f48c6_choosing%20model.jpeg)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Choosing the right Claude model

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## Closing the gap between idea and working product

The goal of helping non-technical people create software predates Anything's current stack. Before Claude, the models they relied on were prone to outages. The team ended up building multi-stage code generation pipelines—calling separate agents to produce code and manually splicing it in—and relying on RAG pipelines to locate relevant code and package documentation, leaving little room to focus on the actual product. Single-page applications were achievable. But a production-quality product with databases, integrations, and mobile deployment was a different problem entirely.

Serving a non-technical audience raised the bar further. The agent couldn't just produce code: it needed to handle complex workflows reliably, correct its own errors across long building sessions, and maintain quality throughout. "It was unclear how to go from simple tools to something much deeper," says Marcus Lowe, co-founder of Anything. “Once AI models reached the level of reliable instruction following, parallel tool-calling, and consistent tool reliability, it became clear how it could fit into our stack and help us evolve from simple solutions to something that could support more complex product creation.”

## The solution

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

agent success rate

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

agent success rate

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

91-96%

agent success rate

## Why Anything chose Claude

Anything ran structured evaluations across several criteria: compliance with user instructions, ability to build relatively complex applications, performance across many rounds of tool calling and error correction in long conversations, and precision and recall with minimal hallucinations. "Claude models came out on top in those evaluations, so they became the best fit for our agent architecture," Lowe said.

The evaluation went beyond raw generation quality. Anything's architecture gives the agent full visibility into the user's stack, including runtime behavior, not just the codebase. That design requires a model with strong tool calling, reliable reasoning across many steps, and consistent coding quality. “Anthropic's specific focus around coding abilities is what drove Claude to the top for us,” said software engineer Ahmad Jiha. “The warmth and personality of Claude models resonates with our users. That's why we default to Claude in the product.”

Claude's performance in those areas let the team shift their focus from keeping the AI functional to launching a better agent experience. "Reliability at scale was also important, and that allowed us to focus more on building the agent and solving the full user job rather than just making the AI function,” Lowe said. “The warmth and personality of Claude models resonates with our users. That's why we default to Claude in the product.”

Built with the Agent SDK, the team had Claude integrated in a day. Opus 4.6's performance was strong enough from the start that they didn't need the weeks of testing and iteration they'd typically budget for a new model.

Building agents with the Claude Agent SDK

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698395d5956e6e0e78f3e486_image-claude-sdk.jpg)

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Building agents with the Claude Agent SDK

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

## The outcome

## From prompt to a published app

Claude runs throughout Anything's stack: the core product-building agent, subroutines within it, and internal processes that improve development workflows. What distinguishes Anything from simpler code-generation tools is scope. Rather than producing isolated snippets, the agent handles entire product-building workflows end to end.

"There is a baseline level of quality needed to move from simple or single-page applications to multi-page, full-stack apps that integrate many libraries and cover a wide range of use cases," Lowe said. In practice, that meant unlocking full-stack, multi-platform applications with backends, mobile apps, API and AI integrations, and product paywalls. "Claude helped us reach that level of quality, which allowed us to support much more complex applications and deliver a better overall user experience."

The results show up in what users ship: Shane, a non-technical founder, used Anything to build PipelinePro, a recruiting ATS and client-intelligence platform with Zoho Recruit sync, candidate scoring, AI interview bots, and a client portal. He's already demoing and selling to customers. Laurent, a French film director, launched Telefan, a streaming app helping people discover thousands of hard-to-find French TV films, with voice-driven discovery. A user with no engineering background built The Collective, a social app for making friends and meeting people in the Philadelphia area. Another user is creating an AI radio station where listeners can generate music through the ElevenLabs API and earn royalties when their tracks are played, with a discovery marketplace in development.

In the last five months alone, users have built more than 800,000 apps, with the agent maintaining a 91-96% success rate as measured by generation completion rates, agent self-reports, and in-product user feedback. Beyond the customer-facing product, Anything uses Claude internally to power agentic workflows across support, inbound sales, product feedback analysis, and improving parts of the company's own codebase with Claude Code.

## Looking ahead: Long-running agents at scale

Anything is building toward more advanced agents capable of massive parallelization and long-running processes. The team expects user-built apps to increasingly become self-improving as the agents grow sophisticated enough to handle complexity that users previously managed themselves.

"We're building toward agents that can work on multiple parts of a product simultaneously," Lowe said. "We're just seeing the beginning. The apps our users build will start improving themselves."

"The warmth and personality of Claude models resonates with our users. That's why we default to Claude in the product.”

Ahmad Jiha

Software Engineer, Anything

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
