<!-- source: https://claude.com/blog/claude-managed-agents -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d227246bc2b5a3cc3626_9f6a378a1e3592cf8d27447457409ba12284faef-1000x1000.svg)

# Claude Managed Agents: get to production 10x faster

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

* Date

  April 8, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-managed-agents

Today, we're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

Until now, building agents meant spending development cycles on secure infrastructure, state management, permissioning, and reworking your agent loops for every model upgrade. Managed Agents pairs an agent harness tuned for performance with production infrastructure to go from prototype to launch in days rather than months.

Whether you're building single-task runners or complex multi-agent pipelines, you can focus on the user experience, not the operational overhead.

Managed Agents is available today in public beta on the Claude Platform.

## **Build and deploy agents 10x faster**

Shipping a production agent requires sandboxed code execution, checkpointing, credential management, scoped permissions, and end-to-end tracing. That's months of infrastructure work before you ship anything users see.

Managed Agents handles the complexity. You define your agent's tasks, tools, and guardrails and we run it on our infrastructure. A built-in orchestration harness decides when to call tools, how to manage context, and how to recover from errors.

Managed Agents includes:

* **Production-grade agents** with secure sandboxing, authentication, and tool execution handled for you.
* **Long-running sessions** that operate autonomously for hours, with progress and outputs that persist even through disconnections.
* **Multi-agent coordination** so agents can spin up and direct other agents to parallelize complex work (available in *research preview*, request access [here](http://claude.com/form/claude-managed-agents)).**‍**
* **Trusted governance,** giving agents access to real systems with scoped permissions, identity management, and execution tracing built in.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d53a1b570fa207204f0111_Claude-Blog-Managed-Agents-Diagram-NoBorder.png)

Claude Managed Agents architecture

## **Designed to make the most of Claude**

Claude models are built for agentic work. Managed Agents is purpose-built for Claude, enabling you to get better agent outcomes with less effort.

With Managed Agents, you define outcomes and success criteria, and Claude self-evaluates and iterates until it gets there (available in *research preview*, request access [here](http://claude.com/form/claude-managed-agents)). It also supports traditional prompt-and-response workflows when you want tighter control.

In internal testing around structured file generation, Managed Agents improved outcome task success by up to 10 points over a standard prompting loop, with the largest gains on the hardest problems.

Session tracing, integration analytics, and troubleshooting guidance are built directly into the Claude Console, so you can inspect every tool call, decision, and failure mode.

## **What teams are building**

Teams are already shipping 10x faster with Managed Agents across a range of production use cases. Coding agents that read a codebase, plan a fix, and open a PR. Productivity agents that join a project, pick up tasks, and deliver work alongside the rest of the team. Finance and legal agents that process documents and extract what matters. In each case, shipping in days meant providing value to users faster.

* [**Notion**](https://claude.com/customers/notion-qa) lets teams delegate work to Claude directly inside their workspace (available now in private alpha inside Notion Custom Agents). Engineers use it to ship code, while knowledge workers use it to produce websites and presentations. Dozens of tasks can run in parallel while the whole team collaborates on the output.
* [**Rakuten**](https://claude.com/customers/rakuten-qa) shipped enterprise agents across product, sales, marketing and finance that plug into Slack and Teams, letting employees assign tasks and get back deliverables like spreadsheets, slides, and apps. Each specialist agent was deployed within a week.
* [**Asana**](https://claude.com/customers/asana-qa)built AI Teammates, collaborative AI agents that work alongside humans inside Asana projects, taking on tasks and drafting deliverables. The team used Managed Agents to add advanced features dramatically faster than they would have been able to otherwise.
* [**Vibecode**](https://claude.com/customers/vibecode) helps their customers go from prompt to deployed app using Managed Agents as the default integration, powering a new generation of AI-native apps. Users can now spin up that same infrastructure at least 10x quicker than before.[**‍**](https://claude.com/customers/sentry)
* [**Sentry**](https://claude.com/customers/sentry) paired Seer, their debugging agent, with a Claude-powered agent that writes the patch and opens the PR, so developers go from a flagged bug to a reviewable fix in one flow. The integration shipped in weeks instead of months on Managed Agents.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba17a186e44af7d97dae57_Frame.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba179c1c4432fa78b2f126_Frame-1.svg)

“We want Notion to be the best place for teams to work with agents and get things done. We integrated Claude Managed Agents, which can handle long-running sessions, manage memory, and deliver high-quality outputs over time, to make that possible. Our users can now delegate open-ended, complex tasks, everything from coding to generating slides and spreadsheets, without ever leaving Notion.”

Eric Liu, Product Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

“With Claude Managed Agents, our power users become like Galileo, contributing across domains far beyond a single specialty or discipline. We deploy each specialist agent within a week, managing long-running tasks across engineering, product, sales, marketing, and finance, generating apps, proposal decks, and spreadsheets in sandboxed environments. As agents become more capable, Managed Agents lets us scale safely without building agentic infrastructure ourselves, so we can focus entirely on democratizing innovation across the company.”

Yusuke Kaji, General Manager of AI for Business

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3414e70a75001b66e8d27f_asana-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3414e7f48cd2308583c215_asana-light.svg)

“Claude Managed Agents dramatically accelerated our development of Asana AI Teammates — helping us ship advanced capabilities faster — and freeing us to focus on creating an enterprise-grade multiplayer user experience.”

Amritansh Raghav, CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69813caf8d50645af3af864f_logo_vibecode-light-mode.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69813cb3c3d5ccc7214e1b85_logo_vibecode-dark-mode.svg)

“Before Claude Managed Agents, users would have to manually run LLMs in sandboxes, manage their lifecycle, equip them with appropriate tools, and oversee their execution, a process that could take weeks or months to set up. Now, with a few lines of code, users can spin up that same infrastructure at least 10x quicker than before. This opens up what's possible to be built by developers and vibe coders alike. We're going to see a surge of AI-native applications on web and mobile.”

Ansh Nanda, Co-founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bf57518a91cc645d08ae1a_sentry-light-mode.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bf57579ec56ad383059291_sentry-dark-mode.svg)

“Turns out telling developers what's wrong with their code isn't enough: they want you to fix it too. Customers can now go from Seer's root cause analysis straight to a Claude-powered agent that writes the fix and opens a PR. We chose Claude Managed Agents because it gives us a secure, fully managed agent runtime, allowing us to focus our efforts on building a seamless developer experience around the handoff. Managed Agents not only allowed us to build the initial integration in weeks instead of months, but has also eliminated the ongoing operational overhead of maintaining bespoke agent infrastructure.”

Indragie Karunaratne, Senior Director of Engineering, AI/ML

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a84a22074cc407a84848_Atlassian_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a84a22074cc407a84848_Atlassian_light.svg)

“Atlassian helps enterprises orchestrate work across humans and agents. With Claude Managed Agents, we can build agents for developers directly into the workflows teams already rely on in weeks instead of months, so customers can assign tasks right from Jira. Managed Agents handles the hard parts like sandboxing, sessions, and scoped permissions, which means our engineers can spend less time on infrastructure and more time building great features for our end users.”

Sanchan Saxena, SVP, Head of Product, Teamwork Collection

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d54700357e01220a808b6e_general-legal-light-mode.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d54702528137b79ea59cbd_general-legal-dark-mode.svg)

“Using Claude Managed Agents, we've built a system that can pull information from our users' documents and correspondence to answer any query they ask, even when we haven't built a specific tool to retrieve the data. Before Managed Agents, we would've had to anticipate every question our users might want to ask and build tools or prompt workflows for each one. Now, with Managed Agents it can code up any tool it needs on the fly, allowing it to handle virtually any user query. This cut development time by 10x, letting us focus on UX and integrating more data sources instead.”

Javed Qadrud-Din, CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d546e8750a5d04702cf69a_blockit-light-mode.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d546ea465a73571724d917_blockit-dark-mode.svg)

“Claude Managed Agents made it 3x faster to build a production-ready meeting prep agent. We went from idea to shipping in a matter of days. Our agent researches every participant ahead of a meeting to surface what matters for moving the conversation forward. Custom tools let us feed in our own calendar and contacts data, MCP made it simple to connect external systems like meeting notetakers, CRMs, etc., and the managed harness handled the heavy lifting, including sandboxed execution and built-in web search. Letting us focus on building the product, not the infrastructure.”

John Han, Co-founder

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Getting started

Managed Agents is priced on consumption. Standard Claude Platform token rates apply, plus $0.08 per session-hour for active runtime. See the [docs](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing) for full pricing details.

Managed Agents is available now on the Claude Platform. Read our [docs](https://platform.claude.com/docs/en/managed-agents/overview) to learn more, head to the [Claude Console](https://platform.claude.com/workspaces/default/agent-quickstart), or use our new CLI to deploy your first agent.

Developers can also use the latest version of Claude Code and built-in claude-api Skill to build with Managed Agents. Just ask “start onboarding for managed agents in Claude API” to get started.

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Jun 17, 2026

### Secure access to the Claude Platform with Workload Identity Federation

Product announcements

[Secure access to the Claude Platform with Workload Identity Federation](#)Secure access to the Claude Platform with Workload Identity Federation

[Secure access to the Claude Platform with Workload Identity Federation](/blog/workload-identity-federation)Secure access to the Claude Platform with Workload Identity Federation

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

May 7, 2026

### Collaborate with Claude across Excel, PowerPoint, Word and Outlook

Product announcements

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](#) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224ef32980bc807847d_a683fdcfe3e2c7c6532342a0fa4ff789c3fd4852-1000x1000.svg)

May 19, 2026

### New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

Product announcements

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](#)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](/blog/new-in-claude-managed-agents)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Apr 30, 2026

### Claude Security is now in public beta

Product announcements

[Claude Security is now in public beta](#)Claude Security is now in public beta

[Claude Security is now in public beta](/blog/claude-security-public-beta)Claude Security is now in public beta

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Agents
