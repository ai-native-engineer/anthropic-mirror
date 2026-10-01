<!-- source: https://claude.com/customers/vega -->

Case study | Claude Platform

# Vega's cyber defense platform returns 67% of analysts' time with Claude

[Try Claude](https://claude.ai)

![Vega Security logo](https://assets.claude.com/4e1839348313fbe4c8f3c96d6c7cbc95f53e13c6.svg)

Industry:
:   Cybersecurity

Company size:
:   Startup

Product:
:   Claude Agent SDK[Claude Platform](https://claude.com/platform/api)

Partner:
:   AWS

Location:
:   North America

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

## Security teams could defend and reason across only what they could afford to ingest

Most large enterprises have security data spread across dozens of tools and cloud environments. In theory they could ingest everything into a security information and event management (SIEM) platform, but this is often too complex and cost-prohibitive at enterprise scale. Security teams typically ingest only the fraction they can afford, and everything outside it becomes a blind spot. That can make it difficult to run queries, detection, or investigation at scale.

AI made the tradeoff sharper. "AI agents are only as effective as the data they can access, and most security architectures are either too fragmented or too slow to support agentic cyber defense at scale," explained Eli Rozen, Co-founder and CTO. A security operations center (SOC) that only sees a sampled slice of the environment inherits every blind spot the sampling created. For one top-four global bank, visibility into Amazon VPC Flow Logs, AWS CloudTrail, and Microsoft 365 telemetry sat out of reach, as ingesting it into a legacy SIEM would have cost an additional $6 million.

Claude on Amazon Bedrock

![Claude on Amazon Bedrock](https://assets.claude.com/3bf99530eb5387631c2eb5a95f92a81c5020c4ef.png?w=2400&q=75&fm=webp&fit=max)

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

## The solution

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

Choosing the right Claude model

![Choosing the right Claude model](https://assets.claude.com/7388619b452db0af26c78442a275c86c5ebe3124.jpg?w=2400&q=75&fm=webp&fit=max)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

> "As an AI-native company, we built Vega to work with best-in-class frontier models like Claude from day one, establishing that level of reasoning as the baseline for our platform."

Eli Rozen, Co-founder & CTO, Vega

## The outcome

## Two-thirds of analyst time back

Across production deployments, customers reclaim roughly 67% of analyst time, complete investigations up to 44 times faster, and pay up to 82% less for data than legacy SIEM ingestion. One Fortune 500 insurer cut mean time to triage from 25 minutes to under 3, and the top-four global bank gained the $6 million worth of telemetry it previously couldn't afford. Underneath those numbers sits the full picture: The Vega platform completes a scan across more than 1 billion CloudTrail logs spanning 17 AWS regions in 41 seconds, against a 30-minute manual baseline, ensuring frontier AI can reason across the entire environment, rather than a sample of it.

"Scaling frontier reasoning to every detection is the ultimate win for our customers,” Rozen explained. "With adversaries using AI to bypass static rules in legacy SIEMs, we’re bringing the judgement of your best cyber defense engineers to every alert, in real time.” At a leading cybersecurity company, Vega uncovered a live malware infection that signature-based tools had missed entirely. An investment banking firm ran a proof of value and decided to replace its legacy SIEM with Vega's platform. A Fortune 500 technology manufacturer brought Vega in to monitor a large-scale Claude Code deployment for AI agent-specific risks such as prompt-based privilege escalation and unauthorized MCP installations.

Next, Vega is shipping agentic search, which lets AI agents execute complete multi-step threat hunts across an organization's entire security environment. “Choose the right model for each task instead of defaulting to the largest model,” Rozen advised. “Rigorously measure quality in production, and build durable platform capabilities that outlast any single foundation model."

> "Claude gives us the ability to work within a single model family and apply the right level of intelligence exactly where it’s needed."

Eli Rozen, Co-founder & CTO, Vega

[![Cyera](https://assets.claude.com/b8c564095d75d596cb49afa2791ea7b0909e958c.svg)

### Cyera on making Claude Cowork the front door to 40 tools](https://claude.com/customers/cyera-qa)[![Cyera](https://assets.claude.com/b8c564095d75d596cb49afa2791ea7b0909e958c.svg)

### Cyera scales agentic AI across 1,500 employees with Claude Enterprise](https://claude.com/customers/cyera)[![Kai](https://assets.claude.com/aff2397c0fd3708b6d0b23554c2ce5f81a3f7c56.svg)

### Kai delivers preemptive exposure management with Claude](https://claude.com/customers/kai)[![Artemis](https://assets.claude.com/48f27f7275d9b4de4be5bb1911d5ad1a92ec95e0.svg)

### How Artemis helps security teams cut incident resolution time by 96%](https://claude.com/customers/artemis)
