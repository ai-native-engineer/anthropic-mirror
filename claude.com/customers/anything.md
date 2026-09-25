<!-- source: https://claude.com/customers/anything -->

Case study | Claude Platform

# Anything builds coding agent for 1.5 million users with Claude Agent SDK

[Try Claude](https://claude.ai)

![Anything logo](https://assets.claude.com/87b34a52251db9e74ee09ff0989c7ac3265f2a49.png)

Industry:
:   Software

Company size:
:   Startup

Product:
:   Claude Platform

Location:
:   North America

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

## Closing the gap between idea and working product

The goal of helping non-technical people create software predates Anything's current stack. Before Claude, the models they relied on were prone to outages. The team ended up building multi-stage code generation pipelines—calling separate agents to produce code and manually splicing it in—and relying on RAG pipelines to locate relevant code and package documentation, leaving little room to focus on the actual product. Single-page applications were achievable. But a production-quality product with databases, integrations, and mobile deployment was a different problem entirely.

Serving a non-technical audience raised the bar further. The agent couldn't just produce code: it needed to handle complex workflows reliably, correct its own errors across long building sessions, and maintain quality throughout. "It was unclear how to go from simple tools to something much deeper," says Marcus Lowe, co-founder of Anything. “Once AI models reached the level of reliable instruction following, parallel tool-calling, and consistent tool reliability, it became clear how it could fit into our stack and help us evolve from simple solutions to something that could support more complex product creation.”

Choosing the right Claude model

![Choosing the right Claude model](https://assets.claude.com/7388619b452db0af26c78442a275c86c5ebe3124.jpg)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## The solution

## Why Anything chose Claude

Anything ran structured evaluations across several criteria: compliance with user instructions, ability to build relatively complex applications, performance across many rounds of tool calling and error correction in long conversations, and precision and recall with minimal hallucinations. "Claude models came out on top in those evaluations, so they became the best fit for our agent architecture," Lowe said.

The evaluation went beyond raw generation quality. Anything's architecture gives the agent full visibility into the user's stack, including runtime behavior, not just the codebase. That design requires a model with strong tool calling, reliable reasoning across many steps, and consistent coding quality. “Anthropic's specific focus around coding abilities is what drove Claude to the top for us,” said software engineer Ahmad Jiha. “The warmth and personality of Claude models resonates with our users. That's why we default to Claude in the product.”

Claude's performance in those areas let the team shift their focus from keeping the AI functional to launching a better agent experience. "Reliability at scale was also important, and that allowed us to focus more on building the agent and solving the full user job rather than just making the AI function,” Lowe said. “The warmth and personality of Claude models resonates with our users. That's why we default to Claude in the product.”

Built with the Agent SDK, the team had Claude integrated in a day. Opus 4.6's performance was strong enough from the start that they didn't need the weeks of testing and iteration they'd typically budget for a new model.

91-96%

agent success rate

## The outcome

## From prompt to a published app

Claude runs throughout Anything's stack: the core product-building agent, subroutines within it, and internal processes that improve development workflows. What distinguishes Anything from simpler code-generation tools is scope. Rather than producing isolated snippets, the agent handles entire product-building workflows end to end.

"There is a baseline level of quality needed to move from simple or single-page applications to multi-page, full-stack apps that integrate many libraries and cover a wide range of use cases," Lowe said. In practice, that meant unlocking full-stack, multi-platform applications with backends, mobile apps, API and AI integrations, and product paywalls. "Claude helped us reach that level of quality, which allowed us to support much more complex applications and deliver a better overall user experience."

The results show up in what users ship: Shane, a non-technical founder, used Anything to build PipelinePro, a recruiting ATS and client-intelligence platform with Zoho Recruit sync, candidate scoring, AI interview bots, and a client portal. He's already demoing and selling to customers. Laurent, a French film director, launched Telefan, a streaming app helping people discover thousands of hard-to-find French TV films, with voice-driven discovery. A user with no engineering background built The Collective, a social app for making friends and meeting people in the Philadelphia area. Another user is creating an AI radio station where listeners can generate music through the ElevenLabs API and earn royalties when their tracks are played, with a discovery marketplace in development.

In the last five months alone, users have built more than 800,000 apps, with the agent maintaining a 91-96% success rate as measured by generation completion rates, agent self-reports, and in-product user feedback. Beyond the customer-facing product, Anything uses Claude internally to power agentic workflows across support, inbound sales, product feedback analysis, and improving parts of the company's own codebase with Claude Code.

## Looking ahead: Long-running agents at scale

Anything is building toward more advanced agents capable of massive parallelization and long-running processes. The team expects user-built apps to increasingly become self-improving as the agents grow sophisticated enough to handle complexity that users previously managed themselves.

"We're building toward agents that can work on multiple parts of a product simultaneously," Lowe said. "We're just seeing the beginning. The apps our users build will start improving themselves."

Building agents with the Claude Agent SDK

![Building agents with the Claude Agent SDK ](https://assets.claude.com/8a8df6660b8f39d6a0a88896d12215466857b588.jpg)

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

> "The warmth and personality of Claude models resonates with our users. That's why we default to Claude in the product.”

Ahmad JihaSoftware Engineer, Anything

[![Supermetrics](https://assets.claude.com/3ac4171a81008be0340e5c3d8ccb46571c3edfb3.svg)

### Supermetrics lets marketers manage ad campaigns from a conversation with Claude](https://claude.com/customers/supermetrics)[![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

### How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### How Rocket Money built its personal finance agent with Claude](https://claude.com/customers/rocket-money)
