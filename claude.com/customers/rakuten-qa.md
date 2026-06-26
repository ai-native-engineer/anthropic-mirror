<!-- source: https://claude.com/customers/rakuten-qa -->

Q&A | Claude Managed Agents

# Inside Rakuten's plan to turn every employee into a builder with Claude Managed Agents

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![Rakuten logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)![Rakuten logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

Industry:

Ecommerce

Company size:

Large

Product:

Claude Managed Agents

Location:

Asia Pacific

Major releases every two weeks

down from once a quarter

97% reduction

in initial critical errors

Claude Managed Agents: Get to production 10x faster

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d6874d9013e4890f253b80_managed-agents-og.jpg)

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

Read more

[Read more](https://claude.com/blog/claude-managed-agents)Read more

Claude Managed Agents: Get to production 10x faster

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Managed Agents: Get to production 10x faster

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

[Prev](#)Prev

[Next](#)Next

[Rakuten](https://www.rakuten.com/) is a global technology company with over 70 businesses spanning e-commerce, travel, fintech, digital content, and communications. As part of its company-wide "AI-nization" strategy, the company moved from using Claude Code to accelerate software development to building AI agents that work alongside employees in every business function. Yusuke Kaji, General Manager of AI for Business at Rakuten, spoke with Anthropic about why the team adopted Claude Managed Agents, what it took to go from experiment to production, and what changes when employees start delegating outcomes to agents instead of tasks. The following conversation has been edited for length and clarity.

## Your team invested early in building agentic infrastructure from scratch. What changed when you started using Claude Managed Agents?

**Yusuke Kaji, Rakuten:** When you are at the frontier, you are often solving problems that have no prior art. We had a strong hunch early on that agents would need persistent compute, memory, and storage to move beyond chat-based AI interaction. That turned out to be exactly the right bet. Our engineers invested significant effort into the infrastructure needed to make our agents reliable and scalable. That was the right call at the time, because no one else had done it before.

Now managing the agent execution layer is not our core objective. With Managed Agents now handling scalability and reliability, that same engineering talent can be redirected toward what actually differentiates us: the agentic experience itself, and the safe, governed integration of agents with corporate systems. We see value in accomplishing things in a week rather than a year. The world will not wait for us.

## Rakuten's company-wide AI strategy accelerated with Claude Code. What made agents across the whole company the next step?

**Kaji:** From day one, we clearly saw the potential of Claude Code as a new way to work beyond engineering. We understand that technical innovation starts with a small group of users and then quickly scales to change the world. We see the agent as the next wave of that pattern.

With Managed Agents, our power users become like Galileo, contributing across domains far beyond a single specialty or discipline. We deploy each specialist agent within a week, managing long-running tasks across engineering, product, sales, marketing, and finance, generating apps, proposal decks, and spreadsheets in sandboxed environments. As agents become more capable, Managed Agents lets us scale safely without building agentic infrastructure ourselves, so we can focus entirely on democratizing innovation across the company.

In practice, we integrate agents with Slack, Microsoft Teams, and our own Kanban-style task system, where users create and assign tasks to agents. The workspace and artifacts are shared with colleagues. Managed Agents' support for multiple environments lets us create separate workspaces for each of these use cases.

We learned we can get things done anywhere, particularly from our mobile devices. Information density tends to be sparse in written communication. By natively supporting mobile, we use voice to communicate with agents, capturing more detail about the problem we want to solve while assigning tasks on the go. We see this as especially encouraging because we have Rakuten Mobile as a mobile communications business. We democratized the telecom industry, and now, using this mobile network, we can democratize innovation with AI agents.

“Technical innovation starts with a small group of users and then quickly scales to change the world. We see the agent as the next wave of that pattern.”

Yusuke Kaji

General Manager of AI for Business at Rakuten

## Walk us through how the task system works in practice. What does a typical workflow look like?

**Kaji:** In one of our products, we collect user feedback through an agent. The agent chats with users to understand their needs and pain points, then creates tickets. Another agent or our human colleagues triage the tickets. If we decide to take it, we work with agents to finalize the PRD, wireframe, or prototype. We run the iteration quickly until we meet our success criteria.

Our colleagues showcased their leadership skills, managing teams of agents the way a strong leader guides a team. One of our colleagues regularly spawns multiple agents in parallel: one for market research, another for analyzing data, while reviewing outputs generated overnight by long-running agents, sharing concrete feedback in real time, and coordinating the results into a final deck.

## You've called these power users "Galileo": people who contribute across domains beyond a single specialty. Can you give a specific example?

**Kaji:** We have a product manager, Shoko Sakamoto, who now operates far beyond her primary role. She uses agents to build FinOps pipelines across multiple public clouds, fetching data from their APIs, building dashboards from scratch to monitor trends, and implementing customized views for various stakeholders. All by herself. She also sets up ambient agents with observability skills to track anomalies in products she manages. The agents notify her when something comes up.

Engineers like Tanapat Ratana made this possible. Leading the Applied AI Group, Tanapat designed an agent that investigates production exceptions, delivers root cause analysis to Slack, and self-improves from feedback. He distributed it across teams so that non-engineers like Shoko can set it up on their own products without depending on the engineering team.

Shoko now scales the products she manages at a speed we have never seen, overseeing major releases every two weeks when it used to take a quarter, while ensuring that growth is financially sustainable. We see her as our "Galileo."

## Some of your agents work for hours at a time. What becomes possible at that timescale, and how does it change what you delegate?

**Kaji:** Before, we had to break work into well-defined chunks for the agent to execute. Now that an agent can work for hours, we share the objective or end state we want to achieve, and the agent decides what tasks should be done. That's the biggest change: we delegate goals, not tasks. This allows us to validate more hypotheses without investing as much cost and time.

## Your agents also use memory to self-improve after each session. What have you observed about quality over time?

**Kaji:** Our agents with memory remember what went wrong in past sessions and avoid repeating those mistakes. In our pilot, initial critical errors dropped by 97%, with cost and latency down more than 30%, without any loss in output quality. Agents adapt, avoiding mistakes they have already seen.

When agents retain memory at scale, the organization itself learns. Today, institutional knowledge is fragmented across people, documents, and systems. With agent memory, every insight one agent gains becomes available to the entire system. Individual learning becomes organizational learning instantly. That is when we stop thinking about agents as tools that remember and start thinking about Rakuten as an entity that continuously evolves its own intelligence. The new categories of work that open up are not just harder tasks, they are tasks that require the full breadth of what the organization knows.

## What's the biggest lesson from this journey?

**Kaji:** Our biggest learning is this hypothesis we validated through our journey: you need to completely transform the way you work to maximize the "marginal returns to intelligence." AI-nization is tough, but it is a required step to fully realize the potential of agentic systems.

## What's the end state you're building towards?

**Kaji:** We do not see AI agents as future colleagues or competitors. They are systems around us. The modern corporation was invented to reduce the cost of coordination. We believe AI agents will do the same for innovation. Our end state is simple: Rakuten becomes an entity that lowers the cost of innovation so we can accelerate our contribution to society.

Case Study: Rakuten

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d68a29adf244215ac55985_og_case-study-rakuten.jpg)

Rakuten uses Claude Code to accelerate software development, achieving 7 hours of autonomous coding and reducing feature delivery time from 24 days to 5 with 99.9% accuracy.

Read more

[Read more](https://claude.com/customers/rakuten)Read more

Case Study: Rakuten

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Rakuten uses Claude Code to accelerate software development, achieving 7 hours of autonomous coding and reducing feature delivery time from 24 days to 5 with 99.9% accuracy.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Case Study: Rakuten

Rakuten uses Claude Code to accelerate software development, achieving 7 hours of autonomous coding and reducing feature delivery time from 24 days to 5 with 99.9% accuracy.

“With Managed Agents, our power users become like Galileo, contributing across domains far beyond a single specialty or discipline. We deploy each specialist agent within a week”

Yusuke Kaji

General Manager of AI for Business at Rakuten

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

## Related stories

[Reversia translates e-commerce stores across 110+ languages with Claude](/customers/reversia)Reversia translates e-commerce stores across 110+ languages with Claude

Reversia translates e-commerce stores across 110+ languages with Claude

Customer story

[Customer story](/customers/reversia)Customer story

[Rakuten accelerates development with Claude Code](/customers/rakuten)Rakuten accelerates development with Claude Code

Rakuten accelerates development with Claude Code

Customer story

[Customer story](/customers/rakuten)Customer story

[How Shopify uses Anthropic’s Claude on Google Cloud to supercharge Sidekick](/customers/shopify)How Shopify uses Anthropic’s Claude on Google Cloud to supercharge Sidekick

How Shopify uses Anthropic’s Claude on Google Cloud to supercharge Sidekick

Customer story

[Customer story](/customers/shopify)Customer story

[L'Oréal advances conversational analytics with Claude](/customers/loreal)L'Oréal advances conversational analytics with Claude

L'Oréal advances conversational analytics with Claude

Customer story

[Customer story](/customers/loreal)Customer story
