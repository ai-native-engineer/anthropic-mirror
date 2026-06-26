<!-- source: https://claude.com/customers/postman -->

Case study | Claude Platform

# Postman automates the API development lifecycle with Claude for 40 million developers

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b452dbea85f462beabd699_logo_postman-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b452dbea85f462beabd699_logo_postman-light-mode.svg)

Industry:

Software

Company size:

Medium

Product:

Partner:

AWS

Location:

North America

Up to 1,150 hours saved per year

for developers using Agent Mode on average

Hours to production via Amazon Bedrock

Postman moved from model evaluation to a production-ready integration in hours

More than 40 million developers and 500,000 organizations use Postman to build, test, and manage APIs, including 98% of the Fortune 500. As AI agents become primary consumers of APIs alongside human developers, Postman is building AI-native tooling that automates the design, testing, and maintenance of APIs end to end. Claude models power Agent Mode, Postman's AI assistant for automating API workflows, and a growing set of integrations that bring Postman's API context directly into Claude Code and Claude.ai.

## With Claude, Postman:

* Selected Claude Opus 4.6 as the default model choice in Agent Mode after evaluation showed it was the best-performing model for development and coding tasks
* Integratedvia Amazon Bedrock in hours, with no infrastructure rebuild required
* Created an AI assistant that understands APIs and can read, write, and reason across collections, tests, specs, and code
* Built a Claude Code plugin, Claude connector, and Claude skill enabling developers to test APIs, generate client code, and sync workspaces from within Claude
* Adopted Claude Code across Postman’s own engineering teams for daily API collaboration and testing

‍

## The challenge

Developer Platform

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f5266ed232fd1354625a6_68c469d18f61fb5c21c81781_og-claude-api.jpeg)

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

Read more

[Read more](/platform/api)Read more

Developer Platform

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Developer Platform

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

## Fragmented APIs at enterprise scale

APIs sit at the center of modern software, but the lifecycle of building, testing, documenting, and maintaining them remains manual and fragmented. A developer working with an API endpoint typically needs to write tests, generate documentation, update the OpenAPI spec, and keep everything in sync with Git. Each step is a separate task, and any change upstream can ripple through the rest. At enterprise scale, across thousands of endpoints, this manual workflow creates drift: documentation falls out of date, tests don't match, and standards get applied inconsistently.

Postman's 2025 State of the API report found that 69% of developers spend more than 10 hours a week on API-related work, with testing, development and documentation being the most time consuming. Postman wanted to address this not by bolting AI onto individual tasks, but by building an AI-native experience with full context of a developer's workflow that could act across the entire platform.

‍

## The solution

Introducing Claude Opus 4.6

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698529955ffaa6de831ec14e_opus%201%20(4).jpg)

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Introducing Claude Opus 4.6

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

## Selecting Claude for coding performance and enterprise trust

Postman evaluated multiple model providers, measuring output quality on development and coding tasks. Claude consistently delivered the best results, particularly for code generation, a core capability in the latest version of Postman. The team also found that Claude's single-shot performance stood out: developers preferred working with a model that delivered complete, usable outputs rather than one that repeatedly asked for confirmation. “Our customers are developers and engineering leaders who have high standards for coding tools,” said Abhinav Asthana, CEO at Postman. “Claude consistently performs at the top for development tasks."

Beyond raw performance, the decision came down to trust and fit. Anthropic's approach to information usage and organizational governance aligned with what Postman's customers expect. And Postman's products are often introduced by individual developers before expanding to enterprise-wide deployment. "The fact that Claude is available through Amazon Bedrock and that Anthropic has a mature enterprise governance story matters a lot when we're talking to Fortune 500 teams,"Asthana added.

Integrating Claude through Amazon Bedrock was fast. "We were already using Opus 4.6, and Sonnet shares much of the same capability profile, so adding it didn't require rebuilding anything," said Asthana**.** "Once we made the call, getting up and running was a matter of hours, not weeks.”

‍

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## AI with full context of API workflows

Agent Mode is Postman's AI-native assistant, and Claude models power it as the default selection. "Agent Mode is an entirely new way of interfacing with the Postman platform," said Asthana. "Given developers' trust of Claude, it was a natural fit for Claude to be the brains behind this product." What sets Agent Mode apart from a generic chatbot bolted onto a developer tool is that it operates with full context of the developer's workspace: collections, environments, tests, API history, and underlying code in native Git and filesystem workflows.

In practice, a developer can point Agent Mode at an API endpoint and have it generate a complete workflow: creating a Postman collection, writing tests, updating the OpenAPI spec, and keeping everything versioned in Git. Because Agent Mode has full context of a developer's workspace, it can also generate a full-stack CRUD app from a team's APIs, including frontend and backend, without switching tools. When debugging, Agent Mode can identify a failed request, locate the error in backend code, modify and fix the test, and rerun the request to confirm a successful response. “It connects model reasoning to real Postman operations like creating collections, updating tests, modifying specs, and working with Git and the filesystem. By using context from your existing collections, developers reduce manual work while maintaining organizational standards and quality,” explained Asthana**.**

Postman estimates that Agent Mode can save individual developers up to 1,150 hours per year, translating to nearly $1 million in annual cost savings for a 10-person team.

Beyond Agent Mode, Postman released a Claude Code plugin, a Claude connector, and a Claude skill that bring API context into developers' agentic workflows. With these integrations, developers working in Claude Code or Claude.ai can test APIs by running collections, generate idiomatic client code, keep Postman workspaces in sync with their codebase, and more, all without leaving their preferred environment.

## Looking ahead

Postman will continue expanding AI-assisted capabilities for engineers building APIs for internal, external, and agentic use. The team is also eager to see how Claude Sonnet and Opus perform in more complex, hands-on engineering scenarios. Early signals are promising. "Postman sits at the center of how enterprises manage their APIs,” Asthana said. “By bringing Postman directly into Claude, developers and enterprise teams can move faster at every stage of API development, all without switching tools or losing context.”

"The fact that Claude is available through Amazon Bedrock and that Anthropic has a mature enterprise governance story matters a lot when we're talking to Fortune 500 teams."

Abhinav Asthana

CEO, Postman

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
