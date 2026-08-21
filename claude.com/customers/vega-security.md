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

Completes investigations up to 44 times faster with 82% lower costs

than legacy SIEMs

Cut triage from 25 minutes to less than 3 minutes

at a Fortune 500 company

[Vega](https://vega.io/) is an agentic cyber defense platform for enterprises, including Fortune 200 companies, global banks, and leading healthcare providers. The Vega platform runs an agentic cyber defense loop of detection, triage, investigation, and optimization directly on security data where it lives, without ingestion or centralization, with Claude as a reasoning engine behind it.

## With Claude, Vega:

* Completes investigations up to 44 times faster with 82% lower costs than legacy SIEMs
* Cuts triage from 25 minutes to <3 minutes for a Fortune 500 company
* Reclaims roughly 67% of cyber defense engineering team’s time

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

AI made the tradeoff sharper. "AI agents are only as effective as the data they can access, and most security architectures are either too fragmented or too slow to support agentic cyber defense at scale," explained Eli Rozen, Co-founder and CTO. A security operations center (SOC) that only sees a sampled slice of the environment inherits every blind spot the sampling created. For one top-four global bank, visibility into Amazon VPC Flow Logs, AWS CloudTrail, and Microsoft 365 telemetry sat out of reach, as ingesting it into a legacy SIEM would have cost an additional $6 million.

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

## One model family, the right depth at every layer

Vega set out to build agentic cyber defense: agents that detect cyberattacks, then triage, investigate and optimize themselves against the whole environment. The team chose Claude to power those agents in production. “As an AI-native company, we built Vega to work with best-in-class frontier models like Claude from day one, establishing that level of reasoning as the baseline for our platform,” Rozen said.

Reasoning a security team will act on has to clear a high bar, and Vega set a baseline of accuracy using the most capable Claude model, then worked backward to optimize for cost and efficiency without losing quality.

The deciding factor is the range. "Claude gives us the ability to work within a single model family and apply the right level of intelligence exactly where it’s needed across Haiku, Sonnet, and Opus," Rozen explained.

Vega matches each layer of the pipeline to the Claude model tier that fits it: the deepest reasoning goes to confirmed alerts, where the stakes are highest, while high-volume work like log analysis and summarization runs on lighter, faster tiers. "Customers feel this as speed and precision at scale; our own team feels it as being able to keep unit economics reasonable, while ensuring cyber defense engineers have frontier-level answers where it counts," Rozen noted.

## Building on Agent Skills

Within the platform, Vega built on Anthropic’s Agent Skills format to introduce [detection skills](https://vega.io/blog/vega-introduces-detection-skills), an open standard that allows cyber defense engineers to codify their expertise as an agentic loop: how to triage, investigate, and optimize a detection, written when it is authored and applied to every alert. Vega released the standard at [detectionskills.io](http://detectionskills.io), enabling security teams across platforms to encode and share their judgment with the community.

When a detection fires, the loop runs on that judgment. Triage skills decide whether the alert escalates to an incident, with the reasoning attached. Investigation skills analyze the incident before a human looks: forming a hypothesis, gathering evidence, and drafting an explainable conclusion with recommended next actions. Optimization skills write approved verdicts back into the detection, so it fires sharper next time. Engineers sign off on every change, so the judgment stays theirs while the repetitive work finishes before they arrive.

## Running it in production: Amazon Bedrock, EU residency, and resilience

Inference reaches customers through Amazon Bedrock, with zero data retention, no training on customer data, VPC endpoints keeping traffic off the public internet, and pass-through pricing; the direct Claude API runs alongside it for internal tooling and Claude Code. As usage has scaled, Amazon Bedrock's cross-region inference has absorbed load spikes without Vega having to build that capacity itself.

As a global company, Vega needs to serve organizations with compliance, privacy, and data sovereignty requirements in every region. When a customer needed EU data residency for GDPR, Vega stood up a dedicated control plane in Frankfurt, running Amazon Bedrock's EU-hosted Claude models, in under three weeks.

"As an AI-native company, we built Vega to work with best-in-class frontier models like Claude from day one, establishing that level of reasoning as the baseline for our platform."

Eli Rozen,

Co-founder & CTO, Vega Security

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## Two-thirds of analyst time back

Across production deployments, customers reclaim roughly 67% of analyst time, complete investigations up to 44 times faster, and pay up to 82% less for data than legacy SIEM ingestion. One Fortune 500 insurer cut mean time to triage from 25 minutes to under 3, and the top-four global bank gained the $6 million worth of telemetry it previously couldn't afford. Underneath those numbers sits the full picture: The Vega platform completes a scan across more than 1 billion CloudTrail logs spanning 17 AWS regions in 41 seconds, against a 30-minute manual baseline, ensuring frontier AI can reason across the entire environment, rather than a sample of it.

"Scaling frontier reasoning to every detection is the ultimate win for our customers,” Rozen explained. "With adversaries using AI to bypass static rules in legacy SIEMs, we’re bringing the judgement of your best cyber defense engineers to every alert, in real time.” At a leading cybersecurity company, Vega uncovered a live malware infection that signature-based tools had missed entirely. An investment banking firm ran a proof of value and decided to replace its legacy SIEM with Vega's platform. A Fortune 500 technology manufacturer brought Vega in to monitor a large-scale Claude Code deployment for AI agent-specific risks such as prompt-based privilege escalation and unauthorized MCP installations.

Next, Vega is shipping agentic search, which lets AI agents execute complete multi-step threat hunts across an organization's entire security environment. “Choose the right model for each task instead of defaulting to the largest model,” Rozen advised. “Rigorously measure quality in production, and build durable platform capabilities that outlast any single foundation model."

"Claude gives us the ability to work within a single model family and apply the right level of intelligence exactly where it’s needed."

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
