<!-- source: https://claude.com/customers/lg-cns -->

Case study | Claude Code

# LG CNS modernizes 20-year-old enterprise systems with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a4fc121f28f7c3e0b3bc1b8_logo_lg2-light-mode.png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a4fc124c395704f7f63d30a_logo_lg2-dark-mode.png)

Industry:

Professional services

Company size:

Large

Product:

[Claude Code](https://claude.com/product/claude-code)

Partner:

AWS

Location:

Asia Pacific

99.1% API conversion completion

2,888 of 2,913 APIs migrated from a 20-year-old legacy system

7-month full migration

delivered at roughly 50% of the cost of a conventional rebuild

LG CNS is the IT services and digital transformation arm of LG Group, with approximately 7,000 employees and $4.2 billion in 2025 revenue. The company has built and operated mission-critical systems for financial institutions, manufacturers, and public-sector organizations for more than 35 years. Claude Code is the engine of its newest offering: LG CNS Build Factory, a turn-key software development service that modernizes decades-old enterprise systems at production scale.

## With Claude, LG CNS:

* Converted 2,888 of 2,913 APIs from a 20-year-old legacy system, a 99.1% completion rate
* Delivered a multi-million dollar system migration in seven months, at roughly 50% of the cost of a conventional rebuild
* Migrated 1,340 screens from a proprietary legacy frontend platform to React, with backend and frontend converted simultaneously on 24/7 parallel tracks
* Adopted Claude Code as the standard development approach across the 200-engineer Build Center
* Made a new category of project viable: modernizations that customers had deferred for years because of cost, risk, and specialist shortages

## The challenge

Claude on Amazon Bedrock

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69eaf379756a2219fdd60403_Screenshot%202026-04-23%20at%209.36.06%E2%80%AFPM.png)

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

Claude on Amazon Bedrock

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

## The modernization projects that never get started

The migration requests landing at LG CNS follow a pattern. Customers need stored procedures over 10,000 lines long moved to a modern database, or Oracle Forms screens rebuilt in React. Many need to retire MiPlatform, proprietary UI platforms that dominated Korean enterprise IT two decades ago and have now reached end of service.

These systems are mission-critical, but the engineers who understand them are scarce and the documentation is thin. "From the customer's perspective, modernization is clearly necessary, but cost, timeline, and quality risks make it difficult to initiate," explained Hyosup Bae, Director and Head of Build Center at LG CNS.

One engagement made the bind concrete. A Korean construction company ran its projects on a 20-year-old project management system covering everything from winning an order through final settlement. The company needed to move onto a modern stack, with a fixed deadline and a tightly constrained budget.

Conventional delivery would have taken at least twice the available time and money, at an estimated cost of several billion Korean won. Offshore development did not change the math: dozens of developers writing in parallel against a poorly documented codebase makes consistency harder, not easier. Without a different approach, the project was not going to start.

## The solution

Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525504b02eec936ac51b_68c469d41149ace562bfd24d_og-claude-product-claude-code.jpeg)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Read more

[Read more](https://claude.com/product/claude-code)Read more

Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

## A software factory built around Claude Code

LG CNS tested multiple models, starting from the position that public benchmarks are useful only as a reference point. The criterion that mattered most was task completion: does the model finish what it was asked to do? The team evaluated planning capability, to-do sequencing, tool-calling behavior, and what happened when a model hit an error. Could it find an alternative path, or did it stall?

Claude stood out for understanding intent, not just instructions. "While other models were able to execute given tasks reasonably well, Claude often interpreted what was not explicitly stated and proposed outputs that were more closely aligned with the underlying objective of the problem," Bae said. The difference was clearest in architecture design for large projects, where Claude behaved "less like a code generator and more like a consultant that could understand the problem and propose a direction for solving it."

Access mattered as much as capability. LG CNS reaches Claude through Amazon Bedrock, which lets the team run Claude inside the AWS security configurations its enterprise customers already have in place. For clients in regulated industries such as financial services, that changed the nature of the adoption discussion. "The conversation shifts from 'Can we trust this model?' to 'How can we use a technology that is already within our security boundary?'" Bae noted.

Selecting the model was only half the equation. [Enterprise customers](https://claude.com/solutions/enterprise) need far more than generated code: they expect security, compliance, testing, and uniform quality across thousands of APIs and screens.

To deliver that, the Build Center, LG CNS's 200-engineer technology delivery organization, built an engineering orchestration layer around Claude Code. The harness connects legacy analysis, business logic extraction, code generation, testing, verification, and quality management.

A typical project runs in pods of five to seven people: a Solution Owner, Architect, Engineers, and DevOps. Work starts with planning, where the team presents the project objective and intent to Claude and asks it to propose an approach.

Once the direction is set, work is decomposed into small, clearly scoped tasks defined in YAML. Context is chained through the local file system, with each stage's output stored as files and passed to the next. The team relies on Claude Opus 4.6 for core work: architecture design, legacy analysis, complex code generation, and multi-step workflow execution.

The file-mediated approach began as a workaround. Before the 1M-token context window and memory features arrived, preventing quality degradation as context accumulated was the team's hardest engineering problem. The patterns LG CNS designed to solve it, persistent file-based memory and multi-agent coordination through file handoffs, anticipated capabilities Anthropic later shipped natively.

The team still treats decomposition and context chaining as core strategy. At enterprise scale, maintaining context taxonomy and output consistency matters more than raw context length.

The design philosophy is deliberately restrained. "Trust the model," Bae advised. "Building an overly thick harness to prevent every possible failure constrains the model's performance and increases token consumption." Instead, LG CNS uses a thin, multi-layered harness, with lightweight layers for validation, context scoping, and quality checks that preserve Claude's ability to reason while providing the stability enterprise projects require.

"The ROI is not simply that we did it faster. The ROI is that we made a previously difficult-to-start project possible."

Hyosup Bae

Director and Head of Build Center, LG CNS

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## Proof on a real customer system

The approach was validated on the construction PMS itself: a multi-billion-won, next-generation rebuild delivered between November 2025 and June 2026, at roughly 50% of the cost of a conventional rebuild. The system is in final testing ahead of its scheduled launch in June 2026.

The project achieved a 99.1% API mapping completion rate, with 2,888 of 2,913 APIs converted. On the frontend, 1,340 screens moved from MiPlatform to React across a main portal and a partner portal. Backend and frontend conversion ran simultaneously through 24/7 parallel-track operations.

"The ROI is not simply that we did it faster," Bae said. "The ROI is that we made a previously difficult-to-start project possible."

The work itself has shifted for senior engineers. Their role now centers on setting direction: defining the tasks a large-scale project requires, decomposing them along the right boundaries, and establishing the work sequence and chaining strategy between them. "Once the strategy and direction are set correctly, the details are then refined to fit the on-site situation and the nature of each individual task," Bae explained.

For customers, the most meaningful change is not speed. Migrations they had deferred for years are now realistic options, discussed not as open-ended risks but as executable transformation roadmaps. "The most memorable customer reaction has been the realization that this is now possible," Bae said.

LG CNS plans to develop LG CNS Build Factory into a rigorous, verifiable modernization discipline, investing in deterministic validation through decision-making, automated quality measurement against golden datasets, and a harness that improves itself over time. As the team sees it, the two layers compound.

"The model gets more capable, the harness becomes more sophisticated, and as the two evolve together, the quality and scale of modernization outcomes we can deliver to customers will continue to improve," Bae said.

"The model gets more capable, the harness becomes more sophisticated, and as the two evolve together, the quality and scale of modernization outcomes we can deliver to customers will continue to improve."

Hyosup Bae

Director and Head of Build Center, LG CNS

## Related stories

[Caylent turns months of migration work into days with Claude Agent SDK](https://claude.com/customers/caylent)Caylent turns months of migration work into days with Claude Agent SDK

Caylent turns months of migration work into days with Claude Agent SDK

Customer story

[Customer story](https://claude.com/customers/caylent)Customer story

[How can a two-person fabrication studio make room for problems it’s never solved before?](https://claude.com/customers/bla-studios)How can a two-person fabrication studio make room for problems it’s never solved before?

How can a two-person fabrication studio make room for problems it’s never solved before?

Customer story

[Customer story](https://claude.com/customers/bla-studios)Customer story

[How Blank Metal, a lean professional services firm, runs on Claude Cowork](https://claude.com/customers/blank-metal-qa)How Blank Metal, a lean professional services firm, runs on Claude Cowork

How Blank Metal, a lean professional services firm, runs on Claude Cowork

Customer story

[Customer story](https://claude.com/customers/blank-metal-qa)Customer story

[Quantium scales Claude across Australia's largest enterprises](https://claude.com/customers/quantium-qa)Quantium scales Claude across Australia's largest enterprises

Quantium scales Claude across Australia's largest enterprises

Customer story

[Customer story](https://claude.com/customers/quantium-qa)Customer story
