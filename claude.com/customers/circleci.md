<!-- source: https://claude.com/customers/circleci -->

Case study | Claude Platform

# How CircleCI built a code validation agent with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1f0251ef26c2f437138f1_logo_circleci-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1f02afb707d585ea57da3_logo_circleci-dark-mode.svg)

Industry:

Software

Company size:

Medium

Product:

Location:

North America

90% of the engineering team uses Claude Code

with daily usage jumping 9x since structured adoption began

75% reduction in average test run time

when customers use CircleCI's Smarter Testing feature

Building agents with the Claude Agent SDK

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698395d5956e6e0e78f3e486_image-claude-sdk.jpg)

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Read more

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)Read more

Building agents with the Claude Agent SDK

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Introducing Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

See Claude Code in action—from concept to commit in one seamless workflow.

Read more

[Read more](https://claude.com/product/claude-code)Read more

Introducing Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b862e6ee6520aee5bc0741_vid-placeholder.avif)

[Next](#)Next

See Claude Code in action—from concept to commit in one seamless workflow.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b862e6ee6520aee5bc0741_vid-placeholder.avif)

Introducing Claude Code

See Claude Code in action—from concept to commit in one seamless workflow.

[Prev](#)Prev

[Next](#)Next

[CircleCI](https://circleci.com/), whose CI/CD platform processes billions of jobs annually for teams at Okta, Hinge, and Hugging Face, set out to tackle the growing maintenance burden that slows engineering teams down. The result is CircleCI’s autonomous AI agent [Chunk](https://circleci.com/product/chunk/), built with Claude, which identifies and resolves CI/CD-related maintenance issues with minimal human intervention.

## With Claude, CircleCI achieved:

* 75% reduction in average test run time when customers use CircleCI's Smarter Testing feature
* 90% of the engineering team on Claude Code, with daily usage jumping 9x since structured adoption began
* 90%+ prompt cache efficiency in production, meaning context is reused rather than reprocessed across workflows.
* Multi-quarter internal projects completed in weeks, including an AI-powered PR review system.
* More than 4 in 5 agent tasks now triggered automatically at the point of failure, with the rate of tasks converted into completed pull requests more than doubling since launch

## The challenge: Maintenance backlogs that slow teams

CircleCI's customers are engineering teams where delivery speed directly determines competitive outcomes. Those teams face a persistent tension: test optimization, build fixes, and pipeline improvements all pile up in backlogs while everyone focuses on shipping new features. Technical debt compounds, and the velocity teams are trying to protect gradually erodes.

CircleCI sees this problem intensifying as AI tools accelerate code output across the industry, generating code faster than teams can maintain it. The company needed to solve this internally before they could credibly help their customers solve it too. The goal: build an autonomous agent that could pick up routine maintenance and validate its own fixes before a human ever sees them.

## A decision driven by developer experience

CircleCI's work with Claude started broadly. The company encouraged teams across engineering, operations, and go-to-market to experiment for prototyping, iteration, and analysis. "We encouraged teams to use AI to reimagine the art of what's possible," said JP Leblanc, SVP Engineering. "By providing a single, robust platform for AI exploration, we saw adoption numbers soar."

When the team selected Claude to power Chunk, the deciding factor was the Claude Agent SDK's developer experience: a clean, well-documented interface that made it fast to build. MCP integration meant connecting to existing development tools without coordination overhead. The team found Claude's security posture met their enterprise requirements and rated it the strongest general-purpose model available.

## A closed loop from task to validated pull request

CircleCI’s agent Chunk operates as a closed loop: a natural language task goes in, a validated pull request comes out. Because customers have already described their build environment in their CI configuration, Chunk can spin up those environments as sandboxes with confidence because Claude has access to the right dependencies and tools. For build failures, Claude receives logs as context. For tests, it gets results from previous runs. Claude generates a fix, and CircleCI pipelines validate it. If the pipeline fails, Claude reattempts. The customer receives a PR that is already "green," with the CI pipeline serving as attestation that the change meets testing, linting, and static analysis standards.

"We could not have built Chunk without the Claude Agent SDK," explained Michael Webster, Principal Engineer at CircleCI. "If we had tried to do this three years ago, the amount of work to support all the language variations, framework integrations, and toolchain connections would have been prohibitive. Now we can build really powerful tools very quickly without all the traditional coordination overhead and custom integration work."

A team of 8 engineers built Chunk, moving from working prototypes in days to production-ready capabilities in weeks. Tasks can trigger automatically (periodic runs to fix flaky tests), be user-initiated (fixing a failed build), or come as ad-hoc prompts through Chunk's chat interface. Predictive test selection, which CircleCI calls Smarter Testing, runs only what is new or impacted. This cut time-to-feedback by an average of 75% and up to 97%.

Beyond Chunk, Claude Code has become the daily driver for CircleCI's engineering team, with 90% of engineers engaged. Daily usage has jumped 9x since adoption. One team built an AI-powered PR review system that scans for code issues, analyzes downstream SQL dependencies, flags query optimizations, and generates impact summaries. It deployed in weeks rather than the multiple quarters it would previously have required.

## The results

More than 4 in 5 Chunk tasks now trigger automatically at the point of failure, without a human needing to step in. The rate at which Chunk converts tasks into completed pull requests has more than doubled since launch, meaning Chunk is getting better at knowing when it has enough confidence to propose a fix. For one large enterprise customer, analysis time dropped from 14 hours to 18 minutes. A team that previously waited until the following morning to know whether a change was safe now gets that answer in minutes.

CircleCI's roadmap builds on Claude's advancing reasoning capabilities: automated test management, build optimization, and predictive maintenance that anticipates issues before they affect workflows. As code output accelerates, autonomous validation is what keeps the system from falling behind.

"Claude allowed us to bring Chunk to market faster than we would have otherwise," said Webster. "We've put autonomous maintenance, test optimization, and continuous improvement within reach of every developer by giving them an agent that picks up these tasks automatically. Issues that would sit in backlogs for months are now resolved automatically, and customers can stay in flow and focus on innovation rather than dealing with toil."

‍

"We could not have built Chunk without the Claude Agent SDK."

Michael Webster

Principal Engineer, CircleCI

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
