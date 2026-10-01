<!-- source: https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia -->

Explore here

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a42c9bc20d2072552ef256a_Node-EnterpriseAgents.svg)

# Giving companies more control over their AI agents, with NVIDIA

* Category

  [Agents](https://claude.com/blog/category/agents)
* Product

  [Claude Platform](https://claude.com/platform/api)
* Date

  September 28, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia

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

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225485fe31f1ed2d9a1_db28a79c9f4492b8471009d4c20e900f234ece48-1000x1000.svg)

Aug 26, 2026

### How Warp builds self-improving agents on Claude

Agents

[How Warp builds self-improving agents on Claude](#)How Warp builds self-improving agents on Claude

[How Warp builds self-improving agents on Claude](https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude)How Warp builds self-improving agents on Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a42c9bc20d2072552ef256a_Node-EnterpriseAgents.svg)

Sep 29, 2026

### Agents you can coach: how Asana builds human-agent teams with Claude

Agents

[Agents you can coach: how Asana builds human-agent teams with Claude](#)Agents you can coach: how Asana builds human-agent teams with Claude

[Agents you can coach: how Asana builds human-agent teams with Claude](https://claude.com/blog/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude)Agents you can coach: how Asana builds human-agent teams with Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

Sep 8, 2026

### Reducing cost and improving performance with Claude Platform

Agents

[Reducing cost and improving performance with Claude Platform](#)Reducing cost and improving performance with Claude Platform

[Reducing cost and improving performance with Claude Platform](https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform)Reducing cost and improving performance with Claude Platform

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d228c83775fcc75f4e6d_74409af25137110ac04cc39e4d5ea0a2fbcea421-1000x1000.svg)

Sep 2, 2026

### Building commerce agents with Claude

Product announcements

[Building commerce agents with Claude](#)Building commerce agents with Claude

[Building commerce agents with Claude](https://claude.com/blog/claude-for-commerce-agents)Building commerce agents with Claude

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Platform
