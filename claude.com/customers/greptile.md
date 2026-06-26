<!-- source: https://claude.com/customers/greptile -->

Case study | Claude Agent SDK

# Greptile builds truly agentic code review with Claude Agent SDK

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

Get started

[Get started](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)Get started

![Greptile logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c0232414369115421c1f65_6863e9434f1286f887473e7b_logo-Greptile.svg)![Greptile logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c0232414369115421c1f65_6863e9434f1286f887473e7b_logo-Greptile.svg)

Industry:

Software

Company size:

Small

Product:

Claude Agent SDK

Claude Code

Location:

North America

~90% cache hit rates

Prompt caching through the Agent SDK dramatically reduces costs and increases compute efficiency

1 million

Issues caught per month

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Read more

[Read more](#)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Read more

[Read more](#)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

[**Greptile**](https://greptile.com) builds AI agents that review pull requests with full codebase context. The company serves more than 2,000 organizations, from startups to enterprises like NVIDIA, Brex, and Coinbase, helping engineering teams catch bugs and anti-patterns before they ship to production.

## With Claude Agent SDK, Greptile:

* Achieves ~90% cache hit rates, dramatically reducing costs for both Greptile and self-hosting customers
* Enables multi-hop code investigation that follows leads across git history, similar functions, and pull request context
* Ships new capabilities faster by focusing engineering time on specialized tooling rather than harness infrastructure
* Powers autonomous code review that iteratively investigates issues rather than following rigid workflows
* Provides enterprise customers with cost-effective self-hosting options through efficient compute usage

## The problem

In the AI code review space, most tools follow predetermined paths. They scan a pull request, run through a fixed checklist, and surface findings in a predictable sequence. But Greptile sees code review as an investigation, not a checklist. When a skilled engineer spots something unusual, they don't follow a script. They dig deeper, examine context, trace history, and connect dots across the codebase.

Greptile's team recognized this gap. They had built specialized tools for the investigative work: utilities for grabbing codebase context, finding semantically similar functions, retrieving git history, and more. But their orchestration layer forced these tools into a rigid flowchart. Each step revealed new information, but the system couldn't act on those discoveries because it was locked into a predetermined sequence.

"We wanted to build a system where Greptile could be truly multi-hop and autonomous—where every step reveals new information, and the next step can be based on that information instead of following a rigid flowchart," says Daksh Gupta, Co-founder and CEO, at Greptile.

The team needed an orchestration layer as intelligent as their tooling—one that would let their code review agent think like a skilled engineer.

## Building an agentic code review system with the Agent SDK

The Greptile team considered building their own agent harness but quickly realized where their time would be better spent. "It became clear to us that the value was to spend all of our time building better tools for code review," Gupta says. For a team of 10 engineers, that focus matters.

The Claude Agent SDK offered a powerful orchestration layer that would let them focus on their domain expertise rather than infrastructure. The decision also reflected a technical intuition: agent harnesses and models are tightly coupled. "It was clear to us that models and harnesses would be coupled, and the models were the best," Gupta explains. "That was a really big advantage for the Anthropic SDK."

## Greptile uses Claude for multi-hop code investigation

Claude now powers Greptile's investigative approach to code review. When the agent spots a calculation that looks unusual or a function that differs from similar ones across the codebase, it can autonomously decide what to investigate next. It might examine git history to understand why something changed, trace a commit back to its original pull request to read the context, or compare the code against patterns elsewhere in the repository. "It's acting like an investigative reporter or detective," Gupta explains. "We have all the tooling for the detective, and what we wanted was a really powerful orchestrator for it."

Greptile runs on Opus 4.5. “We believe it to be the best coding model for everything we're trying to achieve with detecting bugs and anti-patterns in code,” Gupta said. “The prompt caching works well for our use case, and the integration with MCP has been valuable."

Greptile also makes heavy use of the SDK's sub-agent capabilities. One sub-agent handles memory retrieval, pulling from a bank of information that includes coding standards the team has expressed, idiosyncrasies Greptile has learned about the codebase, and context from documentation, claude.md files, and cursor rules. This accumulated knowledge informs every review.

The team also uses hooks to inject determinism where it matters. For code review, this means ensuring that every file in a pull request gets examined—a guarantee that's essential for enterprise customers who need thorough, consistent coverage.

## The outcome

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/696a9788da0a2879bd4e7abb_03707559.png)

[Greptile](https://www.greptile.com/examples) catches a precision calculation bug in [NVIDIA's PhysicsNeMo](https://github.com/NVIDIA/physicsnemo/pull/1174), then backs it up with evidence when the author pushes back.

‍

The shift to the Agent SDK delivered immediate efficiency gains. Greptile now achieves cache hit rates close to 90%, which translates to meaningful cost savings across their operation. For customers who self-host Greptile using their own Anthropic instances, this efficiency means they can roll out AI code review at larger scale without proportional cost increases. "Now with the Agent SDK, we have true autonomy—every step creates new information, and the next step can be based on that information," Gupta says. "This has fundamentally changed how our code review agent operates."

The deeper impact is in what Greptile can now build. "The Agent SDK has allowed us to ship faster with far more cost effectiveness and allows us to focus deeply on building specialized tooling," Gupta says."We can focus all our energy on building highly specialized tools for the specific types of things we want to achieve."

Rather than maintaining harness infrastructure, the team invests that engineering time in the tools that make code review genuinely useful: better codebase understanding, smarter similarity detection, richer git history analysis.

The results show up in production. In one example from an NVIDIA open-source repository, Greptile flagged an issue that the reviewing engineer initially disputed. The agent responded with additional evidence—comparisons to similar functions across the codebase, relevant git history—and the engineer acknowledged the catch was correct. That kind of multi-step investigation, where the agent can defend its findings with evidence, is exactly what the agentic architecture enables.  
  
Customers have noticed the difference. "Despite having a tech stack that has repeatedly proven difficult for AI to grasp, Greptile has delivered consistent review insights with a good signal-to-noise ratio that has won over even our most discerning engineers," says Jarrod Ruhdland, Principal Engineer at Brex.

Greptile continues to expand what's possible with the Agent SDK, building new capabilities that would have been far more difficult to develop and maintain without it. For a company reviewing over a billion lines of code each month, the ability to focus on domain expertise rather than infrastructure has become a strategic advantage.

"The Agent SDK has allowed us to ship faster with far more cost effectiveness and allows us to focus deeply on building specialized tooling."

Daksh Gupta

Co-founder and CEO, Greptile

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

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
