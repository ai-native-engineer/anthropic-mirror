<!-- source: https://claude.com/customers/delivery-hero -->

Case study | Claude Platform

# How Delivery Hero's agent merges 100+ pull requests a day with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69e938f0afd05059654ce111_logo_deliveryhero-light-mode.png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69e938f30394182e7b0b306e_logo_deliveryhero-dark-mode.png)

Industry:

Software

Company size:

Large

Product:

Claude Code

Partner:

Google

Location:

EMEA

>100 merged pull requests per day

From Herogen, Delivery Hero's autonomous software delivery agent

85% success rate

Most tasks completed with zero to one developer interactions

[Delivery Hero](https://www.deliveryhero.com/) operates in about 65 countries, connecting customers with restaurants, grocery stores, and shops through local brands. The company's tech teams are spread across dozens of these regional operations, many of which were independent startups before being acquired, each with its own cloud providers, programming languages, and engineering culture. When Delivery Hero centralized its developer platform, it needed a way to give thousands of engineers access to the best AI models without months of procurement delays. Google Cloud provided that path, and Claude quickly became the model of choice.

## With Claude, Delivery Hero achieved:

* >100 merged pull requests per day from Herogen, Delivery Hero's autonomous software delivery agent, about 9% of all PRs
* 85% success rate on assigned tickets, with most requiring zero to one developer interactions
* 18x the original quarterly goal for merged pull requests in Q1 2026
* Cross-repository changes across hundreds of codebases, previously a multi-day effort, completed in minutes
* 95% Claude model usage across central engineering teams
* A 9-to-2 preference for Claude over the next closest option in a survey of the company's CTO group

## The challenge

Claude on Google Cloud

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69eaf379756a2219fdd60403_Screenshot%202026-04-23%20at%209.36.06%E2%80%AFPM.png)

Build advanced AI agents with Claude on Google Cloud.

Read more

[Read more](https://claude.com/partners/google-cloud)Read more

Claude on Google Cloud

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Build advanced AI agents with Claude on Google Cloud.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude on Google Cloud

Build advanced AI agents with Claude on Google Cloud.

## Centralizing engineering across a global network of teams

Since its founding in 2011, Delivery Hero has brought local delivery leaders into a global group of brands that now processes over 11 million orders daily. For years, each of these local brands ran with near-total autonomy over technical decisions. That approach worked during hypergrowth, but as the company began centralizing around 2021, it created a problem: every team had different build systems, different infrastructure setups, and deeply held preferences about all of it. Some teams still had traditional structures with strict distinctions between developers, testers, and system administrators. Others had adopted cross-functional teams that owned, tested, and operated everything they built.

"There's always a certain history and attachment to whatever engineers have at the moment," said Rodrigue Schäfer, Vice President of Platform at Delivery Hero. "Convincing everybody that a global developer platform might be a good idea took around a year and a half."

The challenge extended to AI tooling. Starting in mid-2024, Delivery Hero entered an experimentation phase, allowing different teams to pilot different solutions. The results were promising across the board, but the decentralized approach made it hard to measure success consistently or push for adoption at scale. Many engineers within the platform organization remained skeptical about the competitive edge of agentic engineering until late 2025, when a new generation of models changed what was possible.

## The solution

Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525504b02eec936ac51b_68c469d41149ace562bfd24d_og-claude-product-claude-code.jpeg)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Read more

[Read more](/product/claude-code)Read more

Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

## Selecting Claude on Google Cloud

Delivery Hero centralized its approach using Google Cloud, which hosts Claude and other AI models as a managed service. The company needed a way to give engineers across the entire organization access to the same models without locking them into a single tool, and without months of procurement delays for each new integration. "The tooling itself wasn't the main driver of the success of agentic engineering," Schäfer said. "The main driver was the new models that were substantially better in terms of quality."

Google Cloud solved the access problem. By placing a proxy called LiteLLM in front of the platform, Delivery Hero could route engineers to the best available models regardless of which coding tools they preferred. "Google Cloud allowed us to set up a proxy and give our engineers choice by offering all Google Cloud models, hooked up with whatever tools they use," Schäfer said. "This combination lets us move forward with the newest models. Otherwise, we might need to wait several months."

Once the infrastructure was in place, the preference became clear. A survey of Delivery Hero's CTO group showed nine votes for the Claude setup versus two for the next closest alternative. Usage data confirmed the pattern: across the company's central engineering teams, Claude models account for roughly 95% of all LiteLLM requests.

"Google Cloud allowed us to set up a proxy and give our engineers choice by offering all Google Cloud models, hooked up with whatever tools they use."

Rodrigue Schäfer

Vice President of Platform, Delivery Hero

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## Herogen: an autonomous agent for software delivery

The biggest product to emerge from this infrastructure is Herogen, an autonomous software delivery agent built on Claude Opus 4.5 as its primary coding model. The origin was scrappy, reflecting Delivery Hero’s approach to intrapreneurship. "We had a strong belief in this product and the technology," Schäfer said. "We pulled in a principal engineer and two staff engineers and put them on this as a virtual team, self-funded within my organization.”

Herogen picks up tasks assigned through Jira, writes the code, runs and iterates on tests, then submits the result as a pull request, a proposed code change for review. A "council of agents" that includes both Claude and Gemini reviews the code from different perspectives before a human does a final check. Using multiple models for review is intentional: it reduces the chance that blind spots in any single model's training data slip through.

The team shipped an MVP with a single merged pull request in Q4 2025. From there, the trajectory was steep. "Our goal for Q1 was 100 merged pull requests," Schäfer said. "We met that before we went GA in February. Then we set 500, met that, doubled to 1,000, met that. We ended the quarter at 18 times the original goal."

Herogen now processes more than 100 merged pull requests per day, a volume that Schäfer noted is what a typical engineer produces in an entire year. Only about 15% of the company's engineers are using it so far. The agent is particularly effective at tasks that span large numbers of code repositories: infrastructure configuration updates and refactoring work that would otherwise require an engineer to open each repo individually. Schäfer's team has seen pull requests that refactored over 50 files in a single repository.

"Agentic engineering replaces rigid programming syntax with the fluidity of natural language,” Schäfer explained. “By embedding this technology into the heart of our software delivery via Herogen, we have moved the primary interface to the change request itself. This allows our engineers to lead with intent rather than code, liberating them to focus on high-level innovation and complex problem-solving. It's about achieving quality as high as possible and going toward zero interactions with developers.”

Claude Code fills a different role alongside Herogen. Where Herogen is designed for autonomous task completion on existing code, Claude Code supports engineers in more exploratory work: building new projects from scratch, experimenting with design approaches, and features that benefit from back-and-forth between the developer and the model. Schäfer described the relationship as one of "symbiosis between the engineer and the agent." One team used Claude Code to overhaul a design system across 100 UI components, a task that would have taken an engineer at least a week. Claude Code finished it in minutes.

## Looking ahead

Schäfer is set to expand Delivery Hero’s Herogen team and raise its year-end ambitions significantly. The roadmap includes coordinating changes across multiple connected services, Slack integration for human handoffs, and the ability for engineers to call Herogen into existing pull requests. Beyond Herogen, Schäfer is building a dedicated team that will provide a Claude-based tool stack tailored to Delivery Hero's internal infrastructure, with built-in context for connecting to the company's payment APIs, order APIs, and proprietary infrastructure definitions. The goal is to deploy Claude to approximately 50% of its over 4,000 engineers.

Schäfer is also candid about what comes next. As agentic engineering accelerates the development phase, the constraint shifts downstream. "If you churn out five times more changes to your production environment, you will have five times more incidents if the change failure rate remains at the same level," he noted. The team is investing in agent-driven operations and safer rollouts alongside expanding what Herogen can build.

"Every fifth pull request that's merged, we want that to be done by Herogen in 2026," Schäfer said. "It's a very ambitious target, but we're betting on the improvement in LLMs, especially in Claude, to help us with that."

"This allows our engineers to lead with intent rather than code, liberating them to focus on high-level innovation and complex problem-solving."

Rodrigue Schäfer

Vice President of Platform, Delivery Hero

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
