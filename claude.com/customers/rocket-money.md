<!-- source: https://claude.com/customers/rocket-money -->

Case study | Claude

# How Rocket Money built its personal finance agent with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8e170db69adaa238d89c2d_logo_rocketmoney-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8e17136685ddacc4602392_logo_customer-dark-mode.svg)

Industry:

Software

Company size:

Large

Product:

[Claude Platform](https://claude.com/platform/api)

[Claude Code](https://claude.com/product/claude-code)

Partner:

AWS

Location:

North America

11x increase in code commits

from 11 in December to 128 in July, as the team built its financial agent Rowan

Near-zero hallucinations across Rowan's beta,

with apparent errors tracing to data, not the model

[Rocket Money](https://www.rocketmoney.com/) is a personal finance app used by millions of people to track spending, cancel subscriptions, negotiate bills, and automate savings. Its newest innovation, Rowan, is a financial agent built on Claude that users reach by text message: ask a question in plain language, and Rowan does the work.

## With Claude, Rocket Money:

* Ran Rowan's beta with near zero hallucinations, the apparent errors tracing to source data rather than the model
* Grew monthly code commits 11x, from 11 in December to 128 in July
* Saw a Rowan product manager climb to 9th of 76 PR authors across the entire repository within three months of her first commit
* Designed an agent-workflow hybrid that routes each request through a Haiku 4.5 classifier to single-responsibility subagents, with Sonnet 5 running most of them and Opus 5 reserved for financial tasks that need deeper reasoning
* Automated routine tasks as deterministic code, with an agent that repairs the code when a website changes
* Made every failure traceable to the exact classifier or call that went wrong, so a single fix covers every user

## The challenge

Q&A: Rocket Money on building agents that fix their own code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8e470dae58261233b29295_og_Q%26A%20Rocket.jpg)

Anthropic spoke with Rocket Money's engineering team about the architecture behind Rowan and their approach to building agents in consumer AI.

Read more

[Read more](https://claude.com/customers/rocket-money-qa)Read more

Q&A: Rocket Money on building agents that fix their own code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Anthropic spoke with Rocket Money's engineering team about the architecture behind Rowan and their approach to building agents in consumer AI.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Q&A: Rocket Money on building agents that fix their own code

Anthropic spoke with Rocket Money's engineering team about the architecture behind Rowan and their approach to building agents in consumer AI.

## Putting a money manager in everyone's pocket

The people who manage their money best usually have help: someone watching their accounts, flagging what looks off, and weighing in when a decision comes up. That kind of attention has long been reserved for the wealthy, and everyone else has managed on their own, mostly by opening an app and reading dashboards.

Aaron Dignan, Rocket Money's VP of Product & AI, puts it simply: "The most successful people have a financial expert on their team, who is looking after their accounts and taking action to save them time and money," he said. "What would it mean to put that in everyone's pocket?"

Rocket Money had already built the underlying machinery, with millions of users relying on it to stay on top of their finances. But that value still depended on people doing the work themselves, and a large share of those who want to manage money well don't have the time, aptitude, or interest to sit in an app. "I don't want to make anyone open a dashboard or read a graph," said Chase Adams, VP of AI Engineering. The job was to deliver that value without asking for attention.

## The solution

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

## Choosing a model that could be trusted with money

Delivering on that reliably meant choosing the right model, and the two leaders building Rowan had unusual standing to judge. Dignan and Adams arrived at Rocket Money after years building an AI automation platform together, work that meant writing integrations for every major model and developing a feel for how each one behaved. They ran their own internal tests across models for Rowan, and Claude's approach to agentic engineering kept producing the highest quality output and reliability. For Adams, the moment it clicked was Opus 4.5, which could complete complex tasks in a single pass. The pace of improvement, the consistency, and a philosophy that matched their own made it the choice.

The stakes set the stage. "We're in finance," Dignan said. "Our bar for accuracy needs to be 100%." An agent that moves real money has to be right every time, and that shaped how the team built Rowan.

## Agents that fix their own code

Most teams building agents reach for one large agent loaded with tools and hope it works out the sequence. Rowan is built the opposite way. A classifier running on Haiku 4.5 reads each incoming request and routes it to a subagent built to do exactly one thing. Most subagents run on Sonnet 5; for a financial task that needs real reasoning, the system reaches for Opus 5; and a final subagent formats every response so Rowan's voice stays consistent. The design keeps each step small on purpose, because shorter context tends to produce more reliable results than one call carrying everything. All of this runs in production on Claude through Amazon Bedrock.

The deeper idea is what Dignan calls "third way engineering." Most people, in his view, are either “all in” on agents or stuck in a fully programmatic approach, and neither is right. To reason about this, he likes to imagine superintelligence arriving tomorrow: rather than canceling subscriptions as a novel agentic problem over and over, ASI would almost certainly write code to automate the task. "Let's behave as if that intelligence is already here," Dignan said, "and build accordingly."

Adams makes that concrete: "A cancellation should be codified into a procedure a computer runs over and over until it breaks, usually because a website changed," he said. "At that point an agent steps in, figures out where it broke, self-heals the process, and turns it back into code so it can run on autopilot again." The pattern crystallized when the team saw Agent Skills, which let them package executable scripts alongside instructions, not just prose.

Because Rowan handles money, the architecture is also built to be auditable. Structured outputs let the team run evals against deterministic results instead of asking a model to grade itself, and classifier fall-throughs catch off-topic requests early so a conversation never drifts away from money. After Rowan takes an action, Claude classifies whether it actually completed, such as whether a cancellation went through, and surfaces why when it hasn't, so a person can decide what happens next. Opus 5 also runs automated analysis over traces of production data. "We can trace the thread back to exactly where it went wrong—a specific classifier or a specific call—and fix it for everyone," Dignan said.

"We're in finance. Our bar for accuracy needs to be 100%."

Aaron Dignan

VP of Product & AI, Rocket Money

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## An agent reliable enough for personal finance

As Rowan came together, the team's monthly code commits climbed from 11 in December 2025 to 128 in July 2026, an 11x increase in seven months. Much of that came from widening who writes code: Rowan's product manager made her first commit on March 24 and, within three months, ranked ninth out of 76 PR authors across the entire Rocket Money repository. The code itself is written with Claude Code, using primarily Opus, with Fable in the mix as well. That velocity lets a group of about 23 people, 10 of them engineers, own and improve many specialized subagents at once, and it has given the team capacity to expand what Rowan can do.

Expanding what Rowan does depends on it staying reliable. Across Rowan's beta, the team has seen near-zero hallucinations. "We haven't had any meaningful hallucination patterns with our beta users so far," Adams said, "and when someone thinks they've found one, it usually turns out to be a data problem under the hood, not the model making something up." That track record matters for an agent trusted to act on people's finances.

Rowan is now beginning a phased private rollout, starting with its first paying users and expanding through the second half of the year, and the discipline, the team says, is staying focused rather than saying yes to everything. "Our hypothesis is that people will eventually hire a handful of specialized agents for the major roles in their life, not one agent for everything," Dignan said. "Specialization is what delivers a high quality experience, so Rowan will continue to think about one thing: money."

"We haven't had any meaningful hallucination patterns, and when someone thinks they've found one, it usually turns out to be a data problem, not the model making something up."

Chase Adams

VP of AI Engineering, Rocket Money

## Related stories

[How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)How Atlassian builds AI agents teams can trust with Claude and Google Cloud

How Atlassian builds AI agents teams can trust with Claude and Google Cloud

Customer story

[Customer story](https://claude.com/customers/atlassian)Customer story

[Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)Rocket Money on building agents that fix their own code

Rocket Money on building agents that fix their own code

Customer story

[Customer story](https://claude.com/customers/rocket-money-qa)Customer story

[How Notion ships and scales agents with Claude Managed Agents](https://claude.com/customers/notion-qa)How Notion ships and scales agents with Claude Managed Agents

How Notion ships and scales agents with Claude Managed Agents

Customer story

[Customer story](https://claude.com/customers/notion-qa)Customer story

[Deepgram ships 4–10x more durable code with Claude](https://claude.com/customers/deepgram) Deepgram ships 4–10x more durable code with Claude

Deepgram ships 4–10x more durable code with Claude

Customer story

[Customer story](https://claude.com/customers/deepgram)Customer story
