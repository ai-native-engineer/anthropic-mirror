<!-- source: https://claude.com/resources/articles/how-our-partners-are-putting-opus-to-work-for-cybersecurity -->

AI is changing how quickly security vulnerabilities are found and exploited, and the clearest response is for security teams to put highly capable models to work on their own defenses.

When we launched [Claude Security in public beta](https://claude.com/resources/articles/claude-security-public-beta), we also shared a set of technology and services partners building on Claude Opus, because the fastest path to adoption looks different for every team: some may use Claude directly, others through a platform they already run, others through a services partner who knows their environment.

Several of those offerings are now live, and the early results show what frontier-model defense looks like in practice.

## Early results

Partners are reporting significant improvements in defense capabilities powered by Opus, both internally and in customer environments:

* Continuous pentesting across more than 150,000 production assets a week, surfacing thousands of validated high- and critical-severity findings weekly with zero false positives (Wiz, in customer production).
* The equivalent of a year's worth of penetration testing effort completed in under three weeks (Palo Alto Networks, internal testing).
* Security testing coverage taken from roughly 10% to over 80%, across 1,600 applications and 500,000+ APIs, with scan turnaround cut from 3–5 days to under an hour (Accenture, on its own infrastructure).

The work falls into three areas: testing offensively at scale, closing the gap between finding and fixing vulnerabilities, and deploying governed AI into production.

## Continuous offensive testing at production scale

Offensive testing means attacking your own systems the way an adversary would, so you find the exploitable paths first.

Wiz [Red Agent](https://www.wiz.io/blog/red-agent-claude-opus) is an AI-powered attacker that uses Opus to reason like a human pentester across production web applications and APIs. It analyzes application logic, chains steps, and adapts to real-time server responses to surface the logic-driven flaws traditional scanners miss. Running continuously across more than 150,000 production assets a week, it's surfacing thousands of high- and critical-severity findings, each validated with proof of exploitability and business context from the Wiz Security Graph. "Security teams are no longer limited by a lack of data, but by the ability to act on it," said Alon Schindel, VP AI & Threat Research, Wiz. "By embedding frontier models into Wiz Agents, we're enabling organizations to defend at the speed of AI."

[Unit 42 Frontier AI Defense](https://www.paloaltonetworks.com/unit42/ai-advantage) is Palo Alto Networks' expert-led service that uses Opus to find hidden vulnerabilities, map how they chain into critical attack paths, and build a roadmap for hardening against AI-enabled attacks. The service pairs that exposure analysis with a benchmarked blueprint for machine-speed defense and hands-on transformation work. "As attackers weaponize frontier models to automate cyberattacks, the defense must move faster," said Sam Rubin, SVP of Unit 42, Palo Alto Networks.

CrowdStrike’s [Frontier AI Readiness and Resilience Service](https://www.crowdstrike.com/en-us/services/ai-security-services/frontier-ai-readiness-and-resilience/) brings the same class of capability to a platform trusted by more than 60% of the Fortune 500, pairing Opus with CrowdStrike's AI Red Team Services and proprietary agent frameworks to continuously hunt for latent zero-days in customer applications, validate findings, and accelerate remediation before new code reaches production.

> “"Frontier models like Anthropic's Claude Opus are giving defenders a capability advantage that didn't exist a year ago, pushing vulnerability management all the way to the left." - Mark Manglicmot, Global VP of Consulting Services, CrowdStrike”

## Closing the gap between finding and fixing

The gap between finding a vulnerability and fixing it is where much of vulnerability exposure lives, because triage, prioritization, patch testing, and cross-team handoffs all take time.

Accenture's [Cyber.AI](https://newsroom.accenture.com/news/2026/accenture-and-anthropic-team-to-help-organizations-secure-scale-ai-driven-cybersecurity-operations) is an agentic platform that connects assets, identities, threats, and controls into a single operational model that Opus reasons across, running detection, prioritization, and remediation as a continuous loop. Accenture validated at scale internally first: taking security testing coverage from roughly 10% to over 80% across 1,600 applications and 500,000+ APIs, and cutting scan turnaround from 3–5 days to under an hour in their own global IT infrastructure – results that underpin what Cyber.AI now delivers to clients.

> “"Business leaders are navigating the fastest moving and most complex cyber threat landscape in history. We’re partnering with Anthropic to deliver the tools clients need to stay ahead." - Harpreet Sidhu, Global Lead, Accenture Cybersecurity”

TrendAI™ [Vision One](https://www.trendmicro.com/en_us/business/products/one-platform.html) uses Opus-assisted vulnerability research to help enterprises across 185 countries identify exposure and mitigate risk through virtual patching. Validated findings also flow into the TrendAI Zero Day Initiative for coordinated disclosure, helping protect at-risk systems up to 96 days before a vendor patch is available. “As AI accelerates vulnerability discovery, the real challenge for defenders becomes remediation at scale,” said Rachel Jin, Chief Platform and Business Officer, Head of TrendAI. “Together with Anthropic, we’re helping customers reduce risk through mitigation and virtual patching before attackers can exploit the gap.”

Deloitte's [Continuous Threat Exposure Management (CTEM)](https://www.deloitte.com/global/en/services/consulting-risk/services/deloitte-cyber-attack-surface-management.html) built on Deloitte Ascend™ runs discovery, validation, prioritization, and remediation as one workflow, including countermeasure design when no patch exists. Opus's code reasoning and automated stability testing gives teams the confidence to remediate in hours rather than days or weeks. "CTEM built on Ascend exists to help reduce decision latency in vulnerability remediation," said Adnan Amjad, partner and US Cyber leader, Deloitte, "the gap helps determine whether attackers or defenders win the window."

## Getting AI into production, governed

The new world of agentic AI use cases has presented a new challenge for many teams. Without clear frameworks, setting up the controls, audit evidence, and autonomy boundaries for deployment can often leave AI adoption for security in pilot purgatory.

PwC's [Claude Native Cybersecurity offering](https://www.pwc.com/us/en/technology/alliances/anthropic.html) addresses the two problems CISOs raise together: getting AI safely into production, and modernizing the cyber function itself. Secure AI Adoption moves enterprises from sandbox to production in weeks rather than quarters, with the deployment, governance, and audit evidence that helps the CISO and CRO bring innovation to their teams with confidence. Scaled Frontier Defense integrates Opus-powered agentic reasoning into existing vulnerability management, detection, security engineering, and GRC workflows, enabling autonomous execution within defined guardrails and auditability.

> ““This is a defining moment for cybersecurity, where AI-driven transformation becomes essential to staying resilient and competitive,” - Morgan Adamski, U.S. Cyber, Data & Tech Leader, PwC”

## The growing ecosystem

BCG, Infosys, and SentinelOne are also building defensive cyber offerings on Opus, and we'll share more on each as they become available.

Every offering above runs on the same underlying Opus capability: reasoning about code, understanding which exposures translate into real-word risk, and sustaining long agentic workflows. We're excited to be working with these partners to bring frontier defense to more security teams through the access points that fits them best.

*Learn more about [Claude for security use cases](https://claude.com/solutions/security).*

‍

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
