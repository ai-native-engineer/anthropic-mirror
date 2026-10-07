<!-- source: https://claude.com/resources/articles/claude-managed-agents -->

## Claude Managed Agents explained

Claude Managed Agents is a suite of composable APIs for building and deploying cloud-hosted agents at scale. It pairs an Anthropic-managed harness with production infrastructure for state, memory, permissions, and scheduled execution.

Prior to today's launch, building agents meant spending development cycles on secure infrastructure, state management, permissioning, and reworking your agent loops for every model upgrade. Managed Agents combines an agent harness tuned for performance with production infrastructure to go from prototype to launch in days rather than months.

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

![](https://assets.claude.com/08b6a06365ef3624bef93f9cdcff4b29e80ad7f2.png)

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
* [**Asana**](https://claude.com/customers/asana-qa) built AI Teammates, collaborative AI agents that work alongside humans inside Asana projects, taking on tasks and drafting deliverables. The team used Managed Agents to add advanced features dramatically faster than they would have been able to otherwise.
* [**Vibecode**](https://claude.com/customers/vibecode) helps their customers go from prompt to deployed app using Managed Agents as the default integration, powering a new generation of AI-native apps. Users can now spin up that same infrastructure at least 10x quicker than before.[**‍**](https://claude.com/customers/sentry)
* [**Sentry**](https://claude.com/customers/sentry) paired Seer, their debugging agent, with a Claude-powered agent that writes the patch and opens the PR, so developers go from a flagged bug to a reviewable fix in one flow. The integration shipped in weeks instead of months on Managed Agents.

![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

> “Atlassian helps enterprises orchestrate work across humans and agents. With Claude Managed Agents, we can build agents for developers directly into the workflows teams already rely on in weeks instead of months, so customers can assign tasks right from Jira. Managed Agents handles the hard parts like sandboxing, sessions, and scoped permissions, which means our engineers can spend less time on infrastructure and more time building great features for our end users.”

Sanchan Saxena, SVP, Head of Product, Teamwork Collection

![General Legal](https://assets.claude.com/cdec3718a68a04655d28ce94cd0118bbe12d7f02.svg)

> “Using Claude Managed Agents, we've built a system that can pull information from our users' documents and correspondence to answer any query they ask, even when we haven't built a specific tool to retrieve the data. Before Managed Agents, we would've had to anticipate every question our users might want to ask and build tools or prompt workflows for each one. Now, with Managed Agents it can code up any tool it needs on the fly, allowing it to handle virtually any user query. This cut development time by 10x, letting us focus on UX and integrating more data sources instead.”

Javed Qadrud-Din, CTO

![Blockit](https://assets.claude.com/3cae7291e5befcd2bc2ef5f1281ce3daf4cf6e38.svg)

> “Claude Managed Agents made it 3x faster to build a production-ready meeting prep agent. We went from idea to shipping in a matter of days. Our agent researches every participant ahead of a meeting to surface what matters for moving the conversation forward. Custom tools let us feed in our own calendar and contacts data, MCP made it simple to connect external systems like meeting notetakers, CRMs, etc., and the managed harness handled the heavy lifting, including sandboxed execution and built-in web search. Letting us focus on building the product, not the infrastructure.”

John Han, Co-founder

![Notion](https://assets.claude.com/19e0cdfaef9d2980bddd19cd993076d62b46c0c7.svg)

> “We want Notion to be the best place for teams to work with agents and get things done. We integrated Claude Managed Agents, which can handle long-running sessions, manage memory, and deliver high-quality outputs over time, to make that possible. Our users can now delegate open-ended, complex tasks, everything from coding to generating slides and spreadsheets, without ever leaving Notion.”

Eric Liu, Product Manager

![Rakuten](https://assets.claude.com/5463fa5a44d12868ceec5ae30bfc8c412cafdeae.svg)

> “With Claude Managed Agents, our power users become like Galileo, contributing across domains far beyond a single specialty or discipline. We deploy each specialist agent within a week, managing long-running tasks across engineering, product, sales, marketing, and finance, generating apps, proposal decks, and spreadsheets in sandboxed environments. As agents become more capable, Managed Agents lets us scale safely without building agentic infrastructure ourselves, so we can focus entirely on democratizing innovation across the company.”

Yusuke Kaji, General Manager of AI for Business

![Asana](https://assets.claude.com/b8ffecd4a133f2860151d51156002816a54772e7.svg)

> “Claude Managed Agents dramatically accelerated our development of Asana AI Teammates — helping us ship advanced capabilities faster — and freeing us to focus on creating an enterprise-grade multiplayer user experience.”

Amritansh Raghav, CTO

![Vibecode](https://assets.claude.com/5f87469e4a2c00123682d8b35785892ff55bd4f4.svg)

> “Before Claude Managed Agents, users would have to manually run LLMs in sandboxes, manage their lifecycle, equip them with appropriate tools, and oversee their execution, a process that could take weeks or months to set up. Now, with a few lines of code, users can spin up that same infrastructure at least 10x quicker than before. This opens up what's possible to be built by developers and vibe coders alike. We're going to see a surge of AI-native applications on web and mobile.”

Ansh Nanda, Co-founder

![Sentry](https://assets.claude.com/410f375f04040180bb6545e287b4ad178b0d7767.svg)

> “Turns out telling developers what's wrong with their code isn't enough: they want you to fix it too. Customers can now go from Seer's root cause analysis straight to a Claude-powered agent that writes the fix and opens a PR. We chose Claude Managed Agents because it gives us a secure, fully managed agent runtime, allowing us to focus our efforts on building a seamless developer experience around the handoff. Managed Agents not only allowed us to build the initial integration in weeks instead of months, but has also eliminated the ongoing operational overhead of maintaining bespoke agent infrastructure.”

Indragie Karunaratne, Senior Director of Engineering, AI/ML

![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

> “Atlassian helps enterprises orchestrate work across humans and agents. With Claude Managed Agents, we can build agents for developers directly into the workflows teams already rely on in weeks instead of months, so customers can assign tasks right from Jira. Managed Agents handles the hard parts like sandboxing, sessions, and scoped permissions, which means our engineers can spend less time on infrastructure and more time building great features for our end users.”

Sanchan Saxena, SVP, Head of Product, Teamwork Collection

![General Legal](https://assets.claude.com/cdec3718a68a04655d28ce94cd0118bbe12d7f02.svg)

> “Using Claude Managed Agents, we've built a system that can pull information from our users' documents and correspondence to answer any query they ask, even when we haven't built a specific tool to retrieve the data. Before Managed Agents, we would've had to anticipate every question our users might want to ask and build tools or prompt workflows for each one. Now, with Managed Agents it can code up any tool it needs on the fly, allowing it to handle virtually any user query. This cut development time by 10x, letting us focus on UX and integrating more data sources instead.”

Javed Qadrud-Din, CTO

![Blockit](https://assets.claude.com/3cae7291e5befcd2bc2ef5f1281ce3daf4cf6e38.svg)

> “Claude Managed Agents made it 3x faster to build a production-ready meeting prep agent. We went from idea to shipping in a matter of days. Our agent researches every participant ahead of a meeting to surface what matters for moving the conversation forward. Custom tools let us feed in our own calendar and contacts data, MCP made it simple to connect external systems like meeting notetakers, CRMs, etc., and the managed harness handled the heavy lifting, including sandboxed execution and built-in web search. Letting us focus on building the product, not the infrastructure.”

John Han, Co-founder

![Notion](https://assets.claude.com/19e0cdfaef9d2980bddd19cd993076d62b46c0c7.svg)

> “We want Notion to be the best place for teams to work with agents and get things done. We integrated Claude Managed Agents, which can handle long-running sessions, manage memory, and deliver high-quality outputs over time, to make that possible. Our users can now delegate open-ended, complex tasks, everything from coding to generating slides and spreadsheets, without ever leaving Notion.”

Eric Liu, Product Manager

![Rakuten](https://assets.claude.com/5463fa5a44d12868ceec5ae30bfc8c412cafdeae.svg)

> “With Claude Managed Agents, our power users become like Galileo, contributing across domains far beyond a single specialty or discipline. We deploy each specialist agent within a week, managing long-running tasks across engineering, product, sales, marketing, and finance, generating apps, proposal decks, and spreadsheets in sandboxed environments. As agents become more capable, Managed Agents lets us scale safely without building agentic infrastructure ourselves, so we can focus entirely on democratizing innovation across the company.”

Yusuke Kaji, General Manager of AI for Business

![Asana](https://assets.claude.com/b8ffecd4a133f2860151d51156002816a54772e7.svg)

> “Claude Managed Agents dramatically accelerated our development of Asana AI Teammates — helping us ship advanced capabilities faster — and freeing us to focus on creating an enterprise-grade multiplayer user experience.”

Amritansh Raghav, CTO

1/8

## What's new in Claude Managed Agents

New capabilities regularly. Agents can now learn across sessions with [built-in memory](https://claude.com/resources/articles/claude-managed-agents-memory) and improve themselves through [dreaming, outcomes, and multiagent orchestration](https://claude.com/resources/articles/new-in-claude-managed-agents). They can run unattended on [scheduled deployments with credentials stored in vaults](https://claude.com/resources/articles/whats-new-in-claude-managed-agents), and operate inside your own perimeter with [self-hosted sandboxes and MCP tunnels](https://claude.com/resources/articles/claude-managed-agents-updates).

## Getting started

Managed Agents is priced on consumption. Standard Claude Platform token rates apply, plus $0.08 per session-hour for active runtime. See the [docs](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing) for full pricing details.

Managed Agents is available now on the Claude Platform. Read our [docs](https://platform.claude.com/docs/en/managed-agents/overview) to learn more, head to the [Claude Console](https://platform.claude.com/workspaces/default/agent-quickstart), or use our new CLI to deploy your first agent.

Developers can also use the latest version of Claude Code and built-in claude-api Skill to build with Managed Agents. Just ask “start onboarding for managed agents in Claude API” to get started.

[ArticleOct 1, 2026

### Customize Claude Code with mods

Change how Claude Code behaves and looks with a few lines of TypeScript.

Claude Code](https://claude.com/resources/articles/claude-code-mods)[ArticleSep 30, 2026

### Claude for Government is now generally available

Claude Code CLI and Claude for Microsoft 365 also now available in early access.](https://claude.com/resources/articles/claude-for-government-is-now-generally-available)[ArticleSep 25, 2026

### Build plugins for Claude

You can now submit plugins to the Claude directory through a new developer portal, track them through review, and see usage analytics once they’re live.

Claude apps](https://claude.com/resources/articles/build-plugins-for-claude)[ArticleSep 24, 2026

### Claude Tag now supports personal connectors in channels

Claude Tag can now use your connectors for requests you make in a channel. Nobody else can use them, and you're in control of how to present the output.

Claude Tag](https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Claude Managed Agents: get to production 10x faster | Claude by Anthropic
