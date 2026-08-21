<!-- source: https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

# Claude models explained: choosing the best model for your use case

* Category

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)

  [Agents](https://claude.com/blog/category/agents)

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  [Claude Code](https://claude.com/product/claude-code)

  [Claude Cowork](https://claude.com/product/cowork)

  [Claude Design](https://claude.com/product/design)

  [Claude Enterprise](https://claude.com/solutions/enterprise)

  [Claude Platform](https://claude.com/platform/api)
* Date

  July 24, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case
* Author(s)

  Michael Segner

## Our advice: start smart

One of the most frequent questions we hear is “what model should I choose for this workload?” As we have released more model classes and versions, the answer has become more nuanced.

This article covers those details including a description of each model class, the top questions to ask when selecting a model, and other best practices.

But to put aside the nuance for a moment, our default recommendation is to start with the most intelligent generally available model and use effort level to dial in performance and cost.

Cost-per-task is often lower for more intelligent models, especially at lower effort levels, even if the price-per-token is higher. This is because more capable models often take fewer turns and less thinking time to get most tasks right. Starting with a smaller model can also make it harder to distinguish between model failures and setup failures.

Of course, as use cases arise that are more latency or cost-sensitive, you can test lower tier models until you find your ideal fit.

Some organizations may also choose to start with the most cost effective model and move up classes until the quality bar is met. We include both [directional approaches](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) in our documentation on model selection.

## The Claude model family

The Claude model family is Anthropic's lineup of AI models — Fable, Opus, Sonnet, and Haiku — each balancing intelligence, speed, and cost differently. Choosing well means matching the model to the job.

### Mythos / Fable

Mythos is Anthropic’s most capable model class, with frontier capabilities across domains. This model class is especially capable at coding, long-running agent tasks, and solving problems AI has not reliably handled before.

The Mythos class ships in two packages of the same underlying model. Claude **Mythos** is for [trusted organizations](https://www.anthropic.com/glasswing) handling dual-use cybersecurity and biology work while Claude **Fable** is packaged with additional safeguards that make the model safe for use by the general public. Both require [limited data retention so they can be used safely](https://privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models).

### Opus

Opus is our powerful model class for reasoning-intensive enterprise tasks. Opus models consistently rank among leading models on key industry benchmarks such as GDPval-AA for knowledge work and Terminal-Bench 2.1 for agentic coding.

The choice between Opus and Fable may not seem clear on the surface, as both excel at coding, long-running agents, and knowledge work. In real-world situations, larger models such as Fable tend to have more wisdom, creativity, and writing skills despite having similar benchmark scores to models such as Opus.

The general rule of thumb is if your evals or internal testing show Opus struggling on some tasks, then Fable is the answer. If Opus already clears the quality bar, then its speed and price profile may make it the better choice.

### Sonnet

Sonnetis our versatile model class for everyday tasks. Sonnet provides a balance of performance, cost, and speed for the widest set of general purpose use cases, including high-volume sub-agents in multi-agent orchestration setups.

### Haiku

Haiku is our lowest cost and fastest model class. Haiku models are designed for high-frequency workloads where latency and cost matter.

## How to choose which Claude model is best for your workload

Our model classes don’t specialize in one type of work. We don’t recommend one model class for finance and another for science. Every Claude model is trained to excel in areas like coding, agentic tasks, and knowledge work.

The main difference across model classes is in *how* *hard* *a problem* they can reliably carry, and what that capability costs in price and speed. When choosing a model, ask:

**How hard is this task?** If it typically takes a lot of time, involves multiple steps, or is previously unsolved then a more capable model class is appropriate.

**What are the latency needs?** If the model is involved in high-frequency customer facing workloads, then Sonnet is often the best choice.

**What are the access constraints?** Mythos is only available to organizations under [Project Glasswing](https://www.anthropic.com/glasswing). Not all organizations make all model classes available to all roles.

**What are the unit economics**? Higher volumes of production may be more appropriate for lower classes of models, particularly if evaluations show those tasks are completed satisfactorily. [Models are priced differently per token](https://platform.claude.com/docs/en/about-claude/models/overview) and will have different price-per-task costs based on their capabilities and effort level.

Effort level also impacts the balance of quality, speed, and cost. Higher-class models at higher efforts offer the best possible performance, and higher-class models at lower efforts can sometimes be more efficient than smaller models.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a4d058625e4fe8fe674686e_80670a42.png)

Curves are illustrative and not plotted from benchmark data.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a4d058625e4fe8fe674686b_dc7b4801.png)

Curves are illustrative and not plotted from benchmark data.

To learn more read [Choosing a Claude model and effort level in Claude Code](https://claude.com/blog/claude-model-and-effort-level-in-claude-code).

## Combining models’ strengths with the advisor strategy

The [advisor strategy](https://claude.com/blog/the-advisor-strategy) allows faster, lower-cost worker models to call more intelligent models to check their plan and evaluate their work, leading to improved performance.

This method, where the executor model is coached only when needed, improves performance by a substantial amount. For example, on SWE-bench Pro Sonnet 5 with a Fable 5 advisor is within 10% of Fable 5’s score at 63% of the price of using Fable 5 for the whole task.

## How evals and benchmarks help with model choice

Two common ways to see if model capabilities are sufficient for your needs are to use standard benchmarks and custom evaluations.

Benchmarks are a set of pre-determined tasks or scenarios, often for a specific domain, with known solutions. These can be helpful directional guides for evaluating capabilities across model classes and providers. The challenge arises when evaluating powerful models, such as Opus and Fable, which can solve almost all of the questions on the test (often referred to as saturation).

In these cases, we recommend organizations use the models on real workloads or test them with their own evaluations to make a decision on which model is the right choice. Typically, evaluations are a curated set of problems drawn from production — including difficult tasks where your current tools fall short, with success criteria your team defines.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a60fb98a987acd56295833a_10089945.png)

This is where the capability and creativity of frontier models start to separate from the pack and from one another. We’ve written extensively on the best practices for developing [custom agent evaluations](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

## Making the smart choice

There is no one-size-fits-all approach to AI model selection, which is why we make multiple model classes available. Ultimately, the best way to select a model is to understand the basics of each model class and understand your use case in-depth. That means building, maintaining, and deploying strong evaluations.

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

Aug 20, 2026

### How monday.com transformed its platform into an agent-first product where humans and agents collaborate

Agents

[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](#)How monday.com transformed its platform into an agent-first product where humans and agents collaborate

[How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate)How monday.com transformed its platform into an agent-first product where humans and agents collaborate

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Aug 20, 2026

### The Claude Code guide for startups

Claude Code

[The Claude Code guide for startups](#)The Claude Code guide for startups

[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups)The Claude Code guide for startups

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

Aug 20, 2026

### Build production agents with computer use, the Skills API, and the Files API

Product announcements

[Build production agents with computer use, the Skills API, and the Files API](#)Build production agents with computer use, the Skills API, and the Files API

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api)Build production agents with computer use, the Skills API, and the Files API

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

Aug 20, 2026

### Anthropic’s approach to teaching and learning AI

Product announcements

[Anthropic’s approach to teaching and learning AI](#)Anthropic’s approach to teaching and learning AI

[Anthropic’s approach to teaching and learning AI](https://claude.com/blog/anthropics-approach-to-teaching-and-learning-ai)Anthropic’s approach to teaching and learning AI

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Code

Claude Cowork

Claude Design

Claude Enterprise

Claude Platform
