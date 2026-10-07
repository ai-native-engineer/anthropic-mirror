<!-- source: https://claude.com/resources/articles/giving-companies-more-control-over-their-ai-agents-with-nvidia -->

NVIDIA today announced the [Open Agent Safety Platform](https://nvidianews.nvidia.com/news/open-agent-safety-platform), an open software platform and reference system design for strengthening AI security. Anthropic has collaborated with NVIDIA to bring additional layers of security and control to the agent stack.

Claude Managed Agents, a suite of composable APIs for building and deploying production-grade agents at scale, holds the credentials an agent needs in a vault so the agent never sees them. Open source NVIDIA OpenShell software is designed to control what the agent can execute and reach while it works. Customers who are using Managed Agents with OpenShell can limit what an agent can do, review what the agent did and confirm that the limits are in place.

Companies are moving from using AI to answer questions to deploying agents that handle complex work across business units, use proprietary data and take actions on behalf of users. As models improve, agents find more uses and get more access. The more access an agent has, the more its company needs to control and check what it does.

## **Protection in layers**

Protection starts with safeguards inside the model. Managed Agents and NVIDIA Open Shell add limits that sit outside the model and apply to what the agent does. Each layer is designed to enforce its limits independently, so protection doesn't depend on any single layer. The layers are modular, so companies can adopt the ones that fit their setup.

## **Claude Managed Agents does the work and holds the credentials**

With Managed Agents, the agent loop runs on a separate server from the sandbox, the isolated environment where the work happens. Credentials, meaning passwords and access keys, are held in a separate vault, so the agent never sees them.

Managed Agents also provides audit trails, which record what each agent did, and integration with a company's existing access controls. Companies can bring their own sandbox setup and choose where and how it runs.

## **NVIDIA OpenShell sets what an agent can reach**

[OpenShell](https://www.nvidia.com/en-us/ai/openshell/) is open source secure runtime software from NVIDIA. It governs and monitors all AI agent behavior and enforces policies for every action. OpenShell blocks everything unless a rule allows it. It checks each tool an agent tries to use and applies rules to the files, network connections and data the agent accesses. The rules are enforced outside the agent, and OpenShell logs every decision it allows or blocks.

Teams can start with narrow permissions, review the log, and use Claude to tighten the rules toward the least access a task needs. OpenShell's policy prover then uses mathematical proof to confirm what the agent can reach under the rules the team wrote.

## **What Claude Managed Agents includes**

* Production-grade agents with secure sandboxing, authentication, and tool execution handled for you.
* Long-running sessions that operate autonomously for hours, with progress and outputs that persist even through disconnections.
* Multi-agent orchestration, where agents can spin up and direct other agents to parallelize complex work.
* Trusted governance, giving agents access to real systems with scoped permissions, identity management, and execution tracing built in.

## **How teams use Managed Agents**

* [Notion](https://claude.com/customers/notion-qa) lets teams hand work to Claude inside their workspace. Engineers use it to ship code, and other employees use it to produce websites and presentations. Dozens of tasks can run in parallel while the team works on the results together.
* [Rakuten](https://claude.com/customers/rakuten-qa) runs specialist agents across engineering, product, sales, marketing, and finance, each deployed within a week.
* [Asana](https://claude.com/customers/asana-qa) built AI Teammates, agents that work alongside people in Asana projects, take on tasks and draft deliverables. Using Managed Agents, the team added advanced features faster than it could have otherwise.

## **Availability**

Managed Agents is available today. It can operate in a sandbox you control either running on your own infrastructure, or with a managed provider. NVIDIA OpenShell is open source under the Apache 2.0 license and available on [GitHub](https://github.com/NVIDIA/OpenShell) and NVIDIA's [developer resources page](https://docs.nvidia.com/openshell/latest/about/overview).

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
