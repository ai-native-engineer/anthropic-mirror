<!-- source: https://claude.com/customers/vega-security -->

Case study | Claude Platform

# Vega's cyber defense platform returns 67% of analysts' time with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7cd9b3a32e0823cc2246db_logo_vega-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7cd9b694804d6ccb090f8f_logo_vega-dark-mode.svg)

Industry:

Cybersecurity

Company size:

Startup

Product:

Claude Agent SDK

[Claude Platform](https://claude.com/platform/api)

Partner:

AWS

Location:

North America

Reclaimed 67% of its cyber defense engineering team’s time

Cut triage from 25 minutes to <3 minutes

at a Fortune 500 company

[Vega](https://vega.io/) is an agentic cyber defense platform for enterprises, including Fortune 200 companies, global banks, and leading healthcare providers. The Vega platform runs an agentic cyber defense loop of detection, triage, investigation, and optimization directly on security data where it lives, without ingestion or centralization, with Claude as a reasoning engine behind it.

## With Claude, Vega:

* Reclaims roughly 67% of cyber defense engineering team’s time
* Cuts triage from 25 minutes to <3 minutes for a Fortune 500 company
* Completes investigations up to 44 times faster at up to 82% lower data cost than legacy SIEM ingestion

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

## Security teams could defend and reason across only what they could afford to ingest

Most large enterprises have security data spread across dozens of tools and cloud environments. In theory they could ingest everything into a security information and event management (SIEM) platform, but this is often too complex and cost-prohibitive at enterprise scale. Security teams typically ingest only the fraction they can afford, and everything outside it becomes a blind spot. That can make it difficult to run queries, detection, or investigation at scale.

AI made the tradeoff sharper. "AI agents are only as effective as the data they can access, and most security architectures are either too fragmented or too slow to support agentic cyber defense at scale," explained Eli Rozen, Co-founder and CTO. A security operations center (SOC) that only sees a sampled slice of the environment inherits every blind spot the sampling created. For one top-four global bank, more than $6 million worth of visibility into Amazon VPC Flow Logs, AWS CloudTrail, and Microsoft 365 telemetry sat out of reach because ingesting it into a SIEM was too expensive.

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

## Build on Claude, route across the model family

Vega set out to build agentic cyber defense: agents that detect cyberattacks, then triage, investigate and optimize themselves against the whole environment. That only works if the reasoning is accurate enough to trust, and the team chose Claude as part of the reasoning layer for Vega to run on. "We built our platform to work with best-in-class frontier AI models like Claude from day one,” Rozen said. Being AI-native meant treating frontier-level reasoning as the baseline rather than something to grow into: the team established its accuracy bar using the most capable model, then worked backward to optimize for cost and efficiency without losing quality.

The high bar is enforced with production evals, measuring hallucination rates against curated datasets, precision and recall on classification, and exact-match and runnable rates on the queries Claude generates. Anthropic's Applied AI team worked alongside Vega to strengthen that framework, expanding the golden datasets, refining grading criteria, and hardening the query and log-analysis pipelines against prompt injection.

The lever is the model family itself. "What Claude gives us that we haven't found anywhere else is range within a single model family, the ability to run Haiku, Sonnet, and Opus against different layers of the same pipeline and get frontier level reasoning exactly where it's needed without paying frontier cost everywhere," Rozen explained.

In practice, Vega matches each layer of the pipeline to the Claude model tier that fits it: the deepest reasoning goes to confirmed alerts, where the stakes are highest, while high-volume work like log analysis and summarization runs on lighter, faster tiers. "Customers feel this as speed and precision at scale; our own team feels it as being able to keep unit economics sane while still giving cyber defense engineers frontier quality answers where it counts," Rozen noted.

## Running it in production: Amazon Bedrock, EU residency, and resilience

All of that inference reaches customers through Amazon Bedrock, with zero data retention, no training on customer data, VPC endpoints keeping traffic off the public internet, and pass-through pricing; the direct Claude API runs alongside it for internal tooling and Claude Code. As usage has scaled, Amazon Bedrock's cross-region inference has absorbed load spikes without Vega having to build that capacity itself.

As a global company, Vega needs to serve organizations with compliance, privacy and data sovereignty requirements in every region. When a customer needed EU data residency for GDPR, Vega stood up a dedicated control plane in Frankfurt, a separate deployment running Amazon Bedrock's EU-hosted Claude models, in under three weeks. "The question isn't really about where a company is headquartered," Rozen said. "It's about whether you can move fast enough to meet the global requirements enterprises actually have."

## Inside the platform

Claude's reasoning powers Vega’s Security Analytics Mesh (SAM), the federated layer that underpins its platform. It queries an enterprise's SIEM, data lakes, and cloud storage as one source without moving it. One Model Context Protocol interface exposes all of it, so Claude, other agents, and engineers working alongside them have the same information.

Above that layer sits a loop an engineer authors as a detection skill, based on Anthropic’s Agent skills format. A detection agent judges incoming signals as malicious or benign and shows its reasoning; a triage agent sets priority, an investigation agent runs the deeper hunt, writing queries, pulling evidence, and drafting a verdict. An independent oversight agent reviews that work before any of it reaches a person. Optimization then closes the loop, writing approved conclusions back into the detection so it fires sharper next time. Engineers sign off on every change, so the judgment stays theirs while the repetitive work finishes before they arrive.Every prompt is grounded in live query results, never free-form text.

Vega has evolved detection skills into an [open standard](https://detectionskills.io/) the broader security industry can build on, and it applies the same build-on-Claude philosophy inward, rebuilding its internal automation on the Claude Agent SDK rather than an off-the-shelf product.

"What Claude gives us that we haven't found anywhere else is range within a single model family, and the ability to get frontier level reasoning exactly where it's needed."

Eli Rozen,

Co-founder & CTO, Vega Security

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## Two-thirds of analyst time back

Across production deployments, customers reclaim roughly 67% of analyst time, complete investigations up to 44 times faster, and pay up to 82% less for data than traditional SIEM ingestion. One Fortune 500 insurer cut mean time to triage from 25 minutes to under 3, and the top-four global bank gained the $6 million worth of telemetry visibility it previously couldn't afford. Underneath those numbers sits the full picture: The Vega platform completes a scan across more than 1 billion CloudTrail logs spanning 17 AWS regions in 41 seconds, against a 30-minute manual baseline, ensuring frontier AI can reason across the entire environment, rather than a sample of it.

"Those numbers aren't three separate wins," Rozen explained. "They're the same architecture showing up three ways: the reasoning catches what narrower tools miss, the platform is what lets that reasoning run at 1B-log scale, and the cost drop is what happens when you stop paying to duplicate data before you can analyze it."

One of those catches came at a leading cybersecurity company, where Vega's threat hunting uncovered a live malware infection that signature-based tools had missed entirely. An investment banking firm ran a proof of value and decided to replace its legacy SIEM with Vega's platform. And a Fortune 500 technology manufacturer brought Vega in to monitor a large-scale Claude Code deployment for AI agent-specific risks such as prompt-based privilege escalation and unauthorized MCP installations.

Next, Vega is shipping agentic search, which lets AI agents execute complete multi-step threat hunts across an organization's entire security environment. “Choose the right model for each task instead of defaulting to the largest model,” Rozen advised. “Rigorously measure quality in production, and build durable platform capabilities that outlast any single foundation model."

"The cost drop is what happens when you stop paying to duplicate data before you can analyze it."

Eli Rozen,

Co-founder & CTO, Vega Security

## Related stories

[Cyera on making Claude Cowork the front door to 40 tools](https://claude.com/customers/cyera-qa)Cyera on making Claude Cowork the front door to 40 tools

Cyera on making Claude Cowork the front door to 40 tools

Customer story

[Customer story](https://claude.com/customers/cyera-qa)Customer story

[Cyera scales agentic AI across 1,500 employees with Claude Enterprise](https://claude.com/customers/cyera) Cyera scales agentic AI across 1,500 employees with Claude Enterprise

Cyera scales agentic AI across 1,500 employees with Claude Enterprise

Customer story

[Customer story](https://claude.com/customers/cyera)Customer story

[Kai delivers preemptive exposure management with Claude](https://claude.com/customers/kai) Kai delivers preemptive exposure management with Claude

Kai delivers preemptive exposure management with Claude

Customer story

[Customer story](https://claude.com/customers/kai)Customer story

[How Artemis helps security teams cut incident resolution time by 96%](https://claude.com/customers/artemis)How Artemis helps security teams cut incident resolution time by 96%

How Artemis helps security teams cut incident resolution time by 96%

Customer story

[Customer story](https://claude.com/customers/artemis)Customer story
