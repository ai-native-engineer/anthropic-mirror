<!-- source: https://claude.com/customers/mintlify -->

Case study | Claude Platform

# Mintlify ships 3x faster automating developer documentation with Claude

[Try Claude](https://claude.ai)

![Mintlify logo](https://assets.claude.com/17e354acbdb212465bbff93d971f04b1e480b324.svg)

Industry:
:   Software

Company size:
:   Small

Product:
:   Claude Platform

Location:
:   North America

3-4x

Increase in engineering code output per engineer

50% faster

Time-to-market for new features

Introducing Claude Code

![Introducing Claude Code](https://assets.claude.com/56575a2d86ba511e0095b0cb9a92cafe7079c820.jpg)

See Claude Code in action—from concept to commit in one seamless workflow.

Introducing Claude Opus 4.6

![Introducing Claude Opus 4.6](https://assets.claude.com/d7a4c17612163424a76462db8e58b65621bdf903.jpg)

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

[Mintlify](https://www.mintlify.com/), a developer documentation platform serving companies like Coinbase, HubSpot, and Perplexity, uses Claude to power an AI assistant that resolves 67% of documentation queries without human intervention—while an automated agent keeps their customers' docs synchronized with code changes. Internally, their engineering team ships features 3-4x faster using Claude Code. Mintlify documentation sites receive as many requests from AI agents as from human developers.

## With Claude, Mintlify achieved:

* **67%** of documentation queries resolved by AI assistant without human intervention
* **3-4x** increase in engineering code output per engineer
* **40%** reduction in documentation bugs and outdated content
* **50%** faster time-to-market for new features

## The challenge

Mintlify's customers faced two persistent problems: developer relations teams overwhelmed by repetitive documentation questions, and documentation that couldn't keep pace with rapidly evolving codebases. For enterprise customers with thousands of API developers, this meant dedicating significant support resources to answering questions that were already covered in documentation.

Meanwhile, API endpoints would change, code examples would become outdated, and parameter names would drift—often going unnoticed for weeks or months. Technical writers manually reviewing commits couldn't keep pace with the volume of changes, and the resulting documentation gaps eroded developer trust.

Mintlify wanted to solve these problems not just for their customers, but also for their own engineering team. They needed to accelerate feature development while maintaining quality—shipping customer-requested improvements faster.

## Selecting Claude

Mintlify evaluated multiple AI providers, measuring resolution rate for their AI assistant and merge rate for their documentation agent. Claude consistently outperformed alternatives on both metrics. The extended 200k context window in Opus 4.5 proved essential—documentation sites often span hundreds of pages covering APIs, SDKs, tutorials, and reference materials. Being able to process entire documentation codebases in a single request, rather than chunking content and losing context, meant the AI assistant could provide more accurate, contextually relevant answers.

"Everyone on our team is writing far more code using Claude than they are manually," explains Nick Khami, an engineering manager at Mintlify. "Our engineers find Claude the best for programming—everyone prefers it relative to all other models we have tried."

## Implementing Claude

The AI assistant went from prototype to production in two weeks. Most of that time was spent on prompt engineering and designing the context pipeline—the Claude API integration itself was straightforward. Building the documentation maintenance agent took 3-4 weeks, instead of the typical 7-8 weeks, reflecting the complexity of analyzing codebases and handling git operations rather than any friction with Claude. Claude Code required no implementation—engineers installed it and started using it the same day, with minimal learning curve since it integrates directly into existing development workflows.

## Mintlify deploys Claude from customer docs to internal dev

**AI-powered documentation assistant:** Every Mintlify documentation site now includes an assistant built on Opus 4.5 that answers natural language questions using documentation, code examples, and live API schemas. It handles complex, multi-step queries—breaking down compound questions like "How do I set up authentication with SSO and then customize the user profile page?", pulling from multiple documentation sections, and delivering coherent step-by-step answers. The assistant uses tool use to fetch live API schemas, ensuring responses reflect the current state of each customer's product.

**Automated documentation maintenance:** An agentic system monitors code repositories and automatically generates pull requests when it detects drift between code and docs—such as an API endpoint that has changed while documentation still references the old version. One enterprise customer reported 43 outdated code examples identified and fixed in the first month alone, issues that would have otherwise gone unnoticed and potentially generated support tickets.

**Internal engineering with Claude Code:** The team uses Claude Code for daily development—implementing features, refactoring legacy code, debugging complex issues, and writing tests. The tool has proven particularly valuable for framework migrations and helping engineers understand unfamiliar parts of the codebase. A recent authentication system refactor, estimated at 3-4 days of work, was completed in 6 hours.

## The outcome

Developer satisfaction scores at one enterprise customer increased from 3.8 to 4.6 out of 5 after implementing the assistant—developers particularly appreciated getting instant answers during off-hours. For customers with thousands of API developers, the AI assistant translates to hundreds of support hours saved monthly.

Documentation quality improved substantially. Customers report saving 8-12 hours per week on documentation maintenance. Engineering velocity accelerated dramatically—Mintlify's team now ships features at 3-4x their previous rate, and time from feature request to deployment dropped from 3-4 weeks to 1-2 weeks.

Customer retention improved by 15%, with the AI assistant becoming a competitive differentiator that prospects specifically cite when choosing Mintlify. Looking ahead, Mintlify is building multi-repository documentation orchestration to maintain consistency across related codebases, and exploring proactive documentation intelligence to identify gaps before they become support issues.

> "Everyone on our team is writing far more code using Claude than they are manually."

Nick KhamiEngineering Manager, Mintlify

[![Supermetrics](https://assets.claude.com/3ac4171a81008be0340e5c3d8ccb46571c3edfb3.svg)

### Supermetrics lets marketers manage ad campaigns from a conversation with Claude](https://claude.com/customers/supermetrics)[![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

### How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### How Rocket Money built its personal finance agent with Claude](https://claude.com/customers/rocket-money)
