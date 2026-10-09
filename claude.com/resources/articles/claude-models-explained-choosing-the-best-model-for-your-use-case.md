<!-- source: https://claude.com/resources/articles/claude-models-explained-choosing-the-best-model-for-your-use-case -->

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

Sonnet is our versatile model class for everyday tasks. Sonnet provides a balance of performance, cost, and speed for the widest set of general purpose use cases, including high-volume sub-agents in multi-agent orchestration setups.

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

![](https://assets.claude.com/dfef391930320e0da39548b50d2b1e7b7ddfcd6c.png)

Curves are illustrative and not plotted from benchmark data.

![](https://assets.claude.com/8352a1d61d466c02e601b9d3cb8012cb75a676fb.png)

Curves are illustrative and not plotted from benchmark data.

To learn more read [Choosing a Claude model and effort level in Claude Code](https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code).

## Combining models’ strengths with the advisor strategy

The [advisor strategy](https://claude.com/resources/articles/the-advisor-strategy) allows faster, lower-cost worker models to call more intelligent models to check their plan and evaluate their work, leading to improved performance.

This method, where the executor model is coached only when needed, improves performance by a substantial amount. For example, on SWE-bench Pro Sonnet 5 with a Fable 5 advisor is within 10% of Fable 5’s score at 63% of the price of using Fable 5 for the whole task.

## How evals and benchmarks help with model choice

Two common ways to see if model capabilities are sufficient for your needs are to use standard benchmarks and custom evaluations.

Benchmarks are a set of pre-determined tasks or scenarios, often for a specific domain, with known solutions. These can be helpful directional guides for evaluating capabilities across model classes and providers. The challenge arises when evaluating powerful models, such as Opus and Fable, which can solve almost all of the questions on the test (often referred to as saturation).

In these cases, we recommend organizations use the models on real workloads or test them with their own evaluations to make a decision on which model is the right choice. Typically, evaluations are a curated set of problems drawn from production — including difficult tasks where your current tools fall short, with success criteria your team defines.

![](https://assets.claude.com/322dd4e9db870a1f5b8c8935849bcf1164a90b56.png)

This is where the capability and creativity of frontier models start to separate from the pack and from one another. We’ve written extensively on the best practices for developing [custom agent evaluations](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

## Making the smart choice

There is no one-size-fits-all approach to AI model selection, which is why we make multiple model classes available. Ultimately, the best way to select a model is to understand the basics of each model class and understand your use case in-depth. That means building, maintaining, and deploying strong evaluations.

[ArticleSep 30, 2026

### How Anthropic's sales team rebuilt inbound with Claude Managed Agents

Carl Johnson, a sales development leader at Anthropic, shares how a Claude-powered buying agent now answers most inbound customers, and how that changed the way our sales team works.

Claude Platform](https://claude.com/resources/articles/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents)[ArticleSep 23, 2026

### How to prepare for AI-driven code modernization projects

How to organize AI-driven modernization projects for critical systems and regulated enterprises.

Claude Code](https://claude.com/resources/articles/how-to-prepare-for-ai-driven-code-modernization-projects)[ArticleSep 23, 2026

### How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace

CodeRabbit expanded its Vercel plan through Claude Marketplace, and Power Digital and ThoughtSpot expanded their Snowflake capacity using their existing Anthropic commitment.

Claude Platform](https://claude.com/resources/articles/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace)[ArticleSep 17, 2026

### Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5

Balyasny Asset Management (BAM) Chief AI Officer Charlie Flanagan on why the firm uses Claude Fable 5 and the role of safeguards in deploying frontier intelligence safely and reliably across the organization.
‍

Claude PlatformClaude Code](https://claude.com/resources/articles/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
