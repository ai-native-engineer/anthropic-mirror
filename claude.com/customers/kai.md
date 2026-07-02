<!-- source: https://claude.com/customers/kai -->

Case study | Claude Platform

# Kai delivers preemptive exposure management with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3d58f7d668ee0558dc6fec_Kai%20Logo_Horizontal_Dark_Transparent%20BG.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3d590a9fa9b75011957e73_Kai%20Logo_Horizontal_All%20White_Transparent%20BG.svg)

Industry:

Cybersecurity

Company size:

Startup

Product:

Partner:

AWS

Location:

North America

99.5% of 2.5 million software composition analysis findings eliminated

as false positives, with true findings auto-remediated

Investigated and triaged 250 million vulnerabilities

surfaced by enterprise scanners in 20 hours, eliminating 83% as benign and triggering auto-remediation for the exploitable findings

AI has made attackers fast: the window between a vulnerability's discovery and its exploitation has shrunk from weeks to hours, and sometimes minutes. Defenders, meanwhile, face more findings than any human team can investigate.  [Kai](https://www.kai.security/) is a cybersecurity company with an AI-native platform for autonomous defense. Using Claude as the analysis layer, the platform autonomously investigates, triages, and remediates security findings across application security, enterprise and infrastructure.

## With Claude, Kai:

* Investigated and triaged 250 million vulnerabilities surfaced by enterprise scanners in 20 hours, eliminating 83% as benign and triggering auto-remediation for the exploitable findings
* Eliminated 99.5% of false positives across 2.5 million findings from Software Composition Analysis (SCA) of 5,000 container images within one hour, saving 3 million hours annually
* Reduced zero-day and supply-chain attack response from days or weeks to a few minutes, with all affected assets identified, mitigation steps generated, and threat hunting launched autonomously

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

## A human-led process built for a threat environment that no longer exists

Inside a large enterprise, security scanners never stop producing findings, and every finding waits on a human security team to investigate it. "A skilled security analyst can thoroughly investigate 10 to 20 vulnerabilities per day," said Damiano Bolzoni, Kai's co-founder and CTO. "Our customers were sitting on millions of findings." AI-enabled attackers are moving faster than human defenders can resolve their backlog, creating an exploitable time gap that is structurally impossible to close with human-led workflows alone.

The industry's answer to that backlog is Continuous Threat Exposure Management, or CTEM, a process of identifying, prioritizing, validating, and remediating exposures. The process was designed to close the gap, but was also designed to be executed by humans. Every phase that depends on human investigation or coordination becomes a bottleneck. The vulnerability stays exploitable for as long as the cycle is stalled, and a process measured in weeks never catches up to attackers who move in hours.

Kai's goal was to run every phase of that cycle autonomously, as fast as attackers move and as accurately as a senior analyst. The obstacle was distilling intelligence from unstructured data at scale. That intelligence informs how inputs are selected and enriched, how context is gathered and applied across millions of findings, and how outputs translate directly into remediation plans and mitigating detection rules. Kai needed a model that could produce analyst-grade intelligence from that data, across millions of signals, without sacrificing the accuracy that makes the output actionable.

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

## Selecting Claude as the analysis layer

Kai's founding bet was that defending against AI-enabled attacks required collapsing and replacing the fragmented stack of security tools rather than adding AI on top of it. "When the foundation is fragmented, AI makes fragments faster," Bolzoni explained. "It does not close the gaps between them."

Many security platforms carry the weight of architecture decisions made before the AI era. "For us, there was no before," Bolzoni said. "Kai was conceived and built at a moment when Claude and frontier models already existed."

That put the weight on model selection. At Kai's scale a single model error does not stay contained; it propagates through the pipeline, leaving a real vulnerability unremediated or an asset misattributed. The bar, Bolzoni added, was commercial as much as technical: “The CISOs we spoke with were not going to act autonomously on findings from a system that could not function at the level of their best analysts,” Bolzoni said.

To find the right model, the team ran side-by-side tests against representative CTEM tasks, measuring extraction accuracy, schema compliance, hallucination rate, latency, cost, and how much human cleanup each result required. “What stood out about Claude was its consistency,” Bolzoni said. "The combination of analysis, depth, and instruction-following held up across the volume and variety of inputs our customers bring to the platform every day."

Trust shaped the access path as much as the model choice. Kai builds for Fortune 500 and Global 2000 enterprises, and the vulnerability data, asset metadata, and environment context those customers put into the platform come with hard requirements about where it goes and who can access it. "For a security platform handling sensitive data at the scale Kai handles it, the access path to the model is not an implementation detail," Bolzoni noted. "It is a security decision in its own right." Kai's decision was Amazon Bedrock.

"Bedrock gave us the access controls, monitoring, and compliance framework that made autonomous execution at enterprise scale something our customers could approve, not just evaluate," Bolzoni said. The setup paid off in the evaluation itself: with identity, access control, and logging patterns already in place, the team spent its time testing model quality against real workflows rather than on procurement and security setup. Consolidation mattered too. "Using fewer vendors means leaner infrastructure and tighter control over how customer data is handled," he added.

## An AI-native platform for autonomous defense

Kai built an AI-native platform to run the entire exposure management cycle. The platform autonomously pulls from scanners, logs, asset inventories, and threat feeds, and multiple investigative agents correlate that data, separating true exposures from noise. Kai then scores severity in the context of the environment, assessing network reachability, vulnerability chaining, and real-world exploitability so the issues that matter surface first. Validated exposures get remediation plans routed to the responsible owner, with ticketing and verification built into the pipeline.

At the core of the architecture is a harness: a layer of deterministic algorithms that ingests, cleanses, deduplicates, validates, and chunks raw security data before any of it reaches the model. Claude then analyzes inconsistent findings and extracts insights from unstructured data. Kai routes that work across Claude Sonnet and Opus models, applying the one best suited to each task. "We implemented Claude, and LLMs in general, as a fully autonomous system rather than as a chatbot," Bolzoni said. "That allowed us to use LLMs in sensitive and complex workflows while keeping control, auditability, and reliability."

"Amazon Bedrock gave us the access controls, monitoring, and compliance framework."

Damiano Bolzoni

Co-founder and CTO, Kai

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## Preemptive exposure management

For one Global 1000 company, the numbers were straightforward: Kai processed 2.5 million Software Composition Analysis (SCA) findings from 5,000 images in under an hour with 99.5% eliminated as false positives. The triage work Kai absorbed saved roughly 3 million engineering and security hours annually. When threat intelligence identified a new supply chain attack, Kai delivered a remediation solution within minutes.

The remediation side is where Kai’s ability to preempt attacks becomes concrete for engineers. For validated findings, Kai generates least-invasive auto-remediation, resolving dependencies upstream and downstream so a fix would not introduce a breaking change. "Engineers do not receive a vulnerability report and a problem to solve," Bolzoni said. "For AppSec findings, they receive commit-ready fixes with the dependency analysis already done. What remained was the work that actually requires human judgment."

## Looking ahead

Kai's architecture is designed so that as frontier models advance, its capabilities advance with them. “Kai's roadmap expands autonomous defense beyond the CTEM cycle, into domains where the intelligence Kai has already built creates a direct path to deeper, more specialized coverage,” said Galina Antova, co-founder and CEO. "Frontier model advances are accelerating what is possible faster than we anticipated when we started building."

"What stood out about Claude was its consistency. The combination of analysis, depth, and instruction-following held up."

Damiano Bolzoni

Co-founder and CTO, Kai

## Related stories

[How Artemis helps security teams cut incident resolution time by 96%](/customers/artemis)How Artemis helps security teams cut incident resolution time by 96%

How Artemis helps security teams cut incident resolution time by 96%

Customer story

[Customer story](/customers/artemis)Customer story

[Cogent resolves security threats 97% faster with Claude](/customers/cogent)Cogent resolves security threats 97% faster with Claude

Cogent resolves security threats 97% faster with Claude

Customer story

[Customer story](/customers/cogent)Customer story

[How eSentire runs expert-level threat investigations at scale with Claude](/customers/esentire)How eSentire runs expert-level threat investigations at scale with Claude

How eSentire runs expert-level threat investigations at scale with Claude

Customer story

[Customer story](/customers/esentire)Customer story

[Vanta streamlines compliance remediation with Claude](/customers/vanta)Vanta streamlines compliance remediation with Claude

Vanta streamlines compliance remediation with Claude

Customer story

[Customer story](/customers/vanta)Customer story
