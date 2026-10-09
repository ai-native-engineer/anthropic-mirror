<!-- source: https://claude.com/resources/articles/giving-companies-more-control-over-their-ai-agents-with-nvidia -->

On September 28, NVIDIA announced the [Open Agent Safety Platform (opens in new tab)](https://nvidianews.nvidia.com/news/open-agent-safety-platform), an open software platform and reference system design for strengthening AI security. Anthropic and NVIDIA collaborated to bring additional layers of security and control to the agent stack.

Agents built with Managed Agents already do their work in secure sandboxes, and NVIDIA OpenShell adds extra protection inside that execution environment, controlling what the agent can access and do.

## Secure agents: architecture and sandboxing

### Split the brain from the hands

One risk with agents is that untrusted content can end up in the sandbox alongside the agent. Agents clone repos, read websites, parse tool output, and even install packages, and any of that can include text a model might follow as instructions (prompt injection) or code that runs. The architectural fix the industry is largely converging on is to [split the ‘brain’ from the ‘hands’ (opens in new tab)](https://www.anthropic.com/engineering/managed-agents).

That means the harness, session state, and credentials live outside the sandbox on durable infrastructure, and the sandbox becomes just a tool the agent uses for execution. For anyone building secure agents, this architecture choice is the easy first step. Claude Managed Agents follows these principles, with core capabilities built for secure agent development, and self-hosted sandboxes let you run that execution on infrastructure you control.

### Self-hosted sandboxes with Claude Managed Agents

Managed Agents is built to run in enterprise environments, with self-hosted sandboxes. With a self-hosted sandbox, the agent loop that handles orchestration, context management, and error recovery stays on Anthropic's infrastructure, while each session's tool calls run in an environment you control, either on your own infrastructure or with a managed sandbox provider. Code execution, sensitive files, packages, services, and data stay within your enterprise perimeter, under your own security and runtime controls.

![Image of Claude Managed Agents self-hosted sandboxes](https://assets.claude.com/10402619d2fe571f9ab4e44846896d667e7a6734.png)

Figure 1: Claude Managed Agents self-hosted sandboxes

### NVIDIA OpenShell sets what an agent can reach

NVIDIA [OpenShell (opens in new tab)](https://www.nvidia.com/en-us/ai/openshell/), open source software from NVIDIA, can serve as the runtime for that sandbox. It governs and monitors all AI agent behavior and enforces policies for every action. OpenShell blocks everything unless a rule allows it. It checks each tool an agent tries to use and applies rules to the files, network connections and data the agent accesses. The rules are enforced outside the agent, and OpenShell logs every decision it allows or blocks.

Teams can start with narrow permissions, review the log, and use Claude to tighten the rules toward the least access a task needs. OpenShell's policy prover then uses mathematical proof to confirm what the agent can reach under the rules the team wrote.

![Image of Claude Managed Agents + NVIDIA OpenShell](https://assets.claude.com/5fed8f359097a21aa893263a4b26d9a2ae908b41.png)

Figure 2: Claude Managed Agents + NVIDIA OpenShell

### What teams are building

Companies are already using Managed Agents with self-hosted sandboxes to enhance agent security. [Clay (opens in new tab)](https://claude.com/blog/claude-managed-agents-updates) runs Sculptor, its GTM engineering agent, in a sandbox that lets it mount external file stores and install packages on the fly. [Rogo (opens in new tab)](https://claude.com/blog/claude-managed-agents-updates) serves customers in highly regulated industries, so it runs its agents’ code in isolated microVMs and keeps code and data inside its own perimeter.

**Availability**

Claude Managed Agents is available today in public beta. NVIDIA OpenShell is open source under the Apache 2.0 license and available on [GitHub (opens in new tab)](https://github.com/NVIDIA/OpenShell) and NVIDIA's [developer resources page (opens in new tab)](https://docs.nvidia.com/openshell/latest/about/overview).

Explore our [docs (opens in new tab)](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) to learn more and follow our [cookbooks (opens in new tab)](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/self-hosted-sandboxes/openshell) to set up your sandbox provider.

[ArticleSep 29, 2026

### Agents you can coach: how Asana builds human-agent teams with Claude

Arnab Bose, Chief Product Officer at Asana, on how Asana runs AI agents as teammates with scoped roles, shared memory, and work that everyone can see.
‍

Claude Platform](https://claude.com/resources/articles/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude)[ArticleSep 8, 2026

### Reducing cost and improving performance with Claude Platform

Tuning prompt caching, instructions, and effort can reduce Claude's cost without sacrificing application performance.

Claude Platform](https://claude.com/resources/articles/reducing-cost-and-improving-performance-with-claude-platform)[ArticleSep 2, 2026

### A guide to the anatomy of effective commerce agents

The architecture, latency & cost techniques, and eval practices for agents that make it easier to buy and sell online.

Claude Platform](https://claude.com/resources/articles/the-anatomy-of-effective-commerce-agents)[ArticleAug 26, 2026

### How Warp builds self-improving agents on Claude

Learn how Warp devised a simple development pattern that anyone can use to create self-improving agents.

Claude Platform](https://claude.com/resources/articles/how-warp-builds-self-improving-agents-on-claude)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
