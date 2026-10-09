<!-- source: https://claude.com/solutions/cybersecurity -->

# Defense at the pace threats now demand

Frontier AI models have surpassed all but the most skilled humans at finding and exploiting software vulnerabilities. Within months, we expect these capabilities will proliferate across AI models and become widely accessible to everyone, including attackers.

Defenders across industries, research, open source, and government must act to find and fix what’s exposed today, and build a durable advantage that drives vulnerabilities ever closer to zero in the future.

01

### State of cybersecurity

Insights on model capabilities today, including Claude Mythos.

[Skip to](#state-of-cybersecurity)

02

### Products and technology

Security-tuned models and tools you can deploy today.

[Skip to](#products-and-technology)

03

### Commitments

Open-source support, critical-systems defense, and policy advocacy.

[Skip to](#commitments)

04

### Resources

Cybersecurity resources, including research, guides, and field insights.

[Skip to](#resources)

The state of cybersecurity

## Where frontier capability stands today

Models can build working exploits, defeat security walls, or help defenders ship fixes at scale. The outcome depends on how they’re used.

CapabilityRemediation

![From finding flaws to full system control — interactive demo](https://assets.claude.com/83edef0822acab8bc90e7127be77c0dcf890fc82.jpg)Interactive demo — open this page on a larger screen to try it

### From finding flaws to full system control

A year ago, the most capable AI models could spot security flaws but couldn't reliably exploit them. Today, in the wrong hands, they can — and not just in simple software. Mythos Preview is the first model to consistently break through the sandbox protections modern browsers and operating systems rely on; other frontier models still stop at the wall. Defenses built on last year's assumptions are already behind.

[Read Red Team research (opens in new tab)](https://red.anthropic.com/2026/exploit-evals/)

Reading the chart

Capability trends downward as tasks get harder. T5 is "the model reaches vulnerable code." Only Mythos Preview passed T1: "the model fully controls the system."

### Tipping the scales to defenders

In March 2026, Mozilla shipped fixes for vulnerabilities found by Claude Opus 4.6, the model that found hundreds of bugs in open source software that survived decades of human review. With Mythos Preview, Mozilla shipped an additional 271 fixes in the April release, more than 20 times their monthly average. Says Bobby Holley, CTO of Firefox, “Defenders finally have a chance to win, decisively.”

[Read Mozilla research (opens in new tab)](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)

Inside Mozilla's review process

The model expands what gets reviewed, and humans decide what gets patched.

Safeguards

### Our approach to dual-use frontier capabilities

Claude Opus and Mythos-class models have significantly stronger cybersecurity capabilities than previous generations, especially in exploit reasoning. As capabilities across all model classes continue to advance, we make our frontier models available under responsible safeguards that give defenders an advantage while limiting the potential for misuse.

* ### Securing critical software

  We’re partnering with organizations that maintain critical infrastructure and widely used software, so the systems the world depends on are hardened first.
* ### Verification program

  Cybersecurity practitioners whose legitimate work overlaps with dual use categories can apply for the Cyber Verification Program for adjusted safeguards.

  [Apply now](https://portal.anthropic.com/programs)
* ### Mythos-powered defense

  Security teams can put frontier reasoning to work on their defense today through Claude Security alongside products and services delivered through trusted partners.

  [Learn more](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)

Project Glasswing

## Our approach to dual-use with Claude Mythos models

Claude Mythos Preview, and now Claude Mythos 5, are models with significantly stronger cybersecurity capabilities, especially in exploit reasoning. As this capability carries the greatest potential for misuse in security, we are limiting initial access to a small number of partners through Project Glasswing. Claude Fable 5 is our Mythos-class model safe for general use through additional safeguards. [Read the latest (opens in new tab)](https://www.anthropic.com/news/claude-fable-5-mythos-5)

## Securing critical software

Glasswing partners maintain critical infrastructure or software the world depends on, where a successful attack would be catastrophic.

## Expanding through trusted access

We are working toward steadily expanding access to Claude Mythos 5 through a trusted access program, and will share more soon.

## Providing tools for defenders today

[Claude Security (opens in new tab)](https://claude.com/product/claude-security), the open-source reference tools, and the practices emerging from Project Glasswing are available to all security teams.

## Backing defenders with resources

## 50+

12 founding members and 40+ organizations joined us in stewarding open-source infrastructure

## $100M

In usage credits from Anthropic to Glasswing partners defending critical infrastructure

## $4M

In direct donations to OpenSSF, Alpha-Omega, and the Apache Software Foundation

## Organizations defending critical software with Claude Mythos

## How security teams put Claude to work for defense

Across enterprise security programs and inside Anthropic, teams use Claude to improve risk posture.

[Learn more](https://claude.com/product/claude-security)

Claude SecurityClaude CodeClaude Developer Platform

![](https://assets.claude.com/db5b0eb52879bafd5325601021c5431e874ba9f3.png)

### Find and fix vulnerabilities with Claude Security

Claude Security reasons about your code like a security researcher: scanning for vulnerabilities, validating findings, and proposing targeted patches.

[Start defending](https://claude.com/product/claude-security)

### Ship secure code in your CI/CD workflow

Use the Code Review skill to set up automated PR reviews to catch logic errors, security vulnerabilities, and regressions across your full codebase.

[Start reviewing](https://claude.com/product/claude-code)

### Deploy security agents with the Claude Developer Platform

Ship defender tools and custom security agents with sandboxed execution, credential isolation, and audit logging built in via the Agent SDK, MCP, and Claude API.

[Start building](https://claude.com/platform/api)

![Palo Alto Networks](https://assets.claude.com/f60d9d14dae95a9824f6bd1592a591e94f2a1c12.svg)

"Anthropic prioritized safety and security a lot more than other LLMs... As the largest cybersecurity company, that's a big deal for us."
- Gunjan Patel, Director of Engineering

![Cogent](https://assets.claude.com/766698d5659097dc0ff541e1d7b77c991a4e9cae.svg)

“Claude consistently performed best on complex, agentic workflows, especially multi-step investigations requiring policy adherence and sustained reasoning across multiple tools.”
- Anirudh Ravula, Head of AI

![Trellix](https://assets.claude.com/1023b604e778c1c5d5646feb4817094ae1865bb6.svg)

“The industry has always moved too slowly compared to attackers. AI is like giving defenders a jetpack when they've been limited to walking.”
- Martin Holste, CTO of Cloud & AI

1 of 3

### Build threat context

Give scanning and response a map to work from. Claude derives a threat model from your codebase and past vulnerabilities, then enriches raw indicators with infrastructure links, attribution, and ATT&CK mapping, so analysts start with context.

* [Open source: Threat Intel Enrichment agent (opens in new tab)](https://platform.claude.com/cookbook/tool-use-threat-intel-enrichment-agent)
* [Open source: Threat Model skill (opens in new tab)](https://github.com/anthropics/defending-code-reference-harness/tree/main/.claude/skills/threat-model#threat-model)

### Vulnerability detection

Claude reads source code the way a researcher does, reasoning about reachability and exploitability, catching vulnerabilities that static tools often miss. A separate triage pass re-verifies every finding to help reduce false positives.

* [In Claude Security (opens in new tab)](https://claude.com/product/claude-security)
* [Open source: Vulnerability detection agent (opens in new tab)](https://platform.claude.com/cookbook/claude-agent-sdk-06-the-vulnerability-detection-agent)

### Patching

Findings now arrive faster than teams can fix them. Claude traces each one to its root cause, locates sibling call sites with the same flaw, and writes a minimal diff with a regression test for your team to review.

* [In Claude Security (opens in new tab)](https://claude.com/product/claude-security)
* [Open source: Patching skill (opens in new tab)](https://github.com/anthropics/defending-code-reference-harness/blob/main/.claude/skills/patch/SKILL.md#patch)

### Triage and verify findings

Hand Claude raw findings from any scanner and get back insights. Claude reads the surrounding code to confirm exploitability, deduplicates by root cause, and ranks by precondition and impact, so engineers can focus and work on real issues first.

* [In Claude Security (opens in new tab)](https://claude.com/product/claude-security)
* [Open source: Triage skill (opens in new tab)](https://github.com/anthropics/defending-code-reference-harness/tree/main/.claude/skills/triage)

### Security review across the dev loop

Review code for security at every stage of development. Claude checks its own edits as it writes and fixes issues in the same session, then specialized agents re-examine pull requests against your codebase, posting verified findings inline without blocking your review gates.

* [Security guidance in Claude Code (opens in new tab)](https://code.claude.com/docs/en/security-guidance)
* [Code Review in Claude Code (opens in new tab)](https://code.claude.com/docs/en/code-review)

### Secure source code, end to end

As offensive capability accelerates, the find-and-fix loop has to close faster. Claude runs threat modeling, discovery, verification, triage, and patching as one continuous loop on your codebase, carrying context across every stage so each finding arrives at the fix with its full history.

* [Using LLMs to secure source code (opens in new tab)](https://claude.com/resources/articles/using-llms-to-secure-source-code)

Customer story

![Cogent](https://assets.claude.com/766698d5659097dc0ff541e1d7b77c991a4e9cae.svg)

Cogent resolves security threats 97% faster with Claude

[Read story (opens in new tab)](https://claude.com/customers/cogent)

Claude Opus

500+

high-severity vulnerabilities found that survived decades of scrutiny and automated analysis

## Cyber defense powered by Claude, available through our partners

* ![Accenture](https://assets.claude.com/eef8a51d4b99d31d65fa28d41f247f85bc363b45.svg)
* ![BCG](https://assets.claude.com/17bafc27b70209e8188ac3e3a45156fb963e8d0e.svg)
* ![Crowdstrike](https://assets.claude.com/291e9ff14319c1efb026b912170a146a475897da.svg)
* ![Deloitte](https://assets.claude.com/d799180e9a468d82dc23a32c1ddfe94dcee116d0.svg)
* ![Infosys](https://assets.claude.com/fd9c7b6b421b5cd59ef7f1737f67175d7c29eaf8.svg)
* ![Microsoft Security](https://assets.claude.com/a854ae20e6357487c253c498b85ed5508eb551ae.svg)
* ![Palo Alto Networks](https://assets.claude.com/f60d9d14dae95a9824f6bd1592a591e94f2a1c12.svg)
* ![PWC](https://assets.claude.com/99f71ec3e626032e4da0ddfce4dc448b0ba18737.svg)
* ![SentinelOne](https://assets.claude.com/a5c2db3e380a063e4c91652932422e0d84ec8dd6.svg)
* ![TrendAI](https://assets.claude.com/da1a36ba4fd9d362ff787fe294ae1d88e20287e1.svg)
* ![Wiz](https://assets.claude.com/3aedf47d07a1ac4d6159c791c631ce40911fc110.svg)

Frontier capabilities

### Leverage powerful models for defense

Claude reads code carefully, understands real risks, and sustains the long workflows that continuous defense requires. Verified practitioners can request [adjusted safeguards](https://support.claude.com/en/articles/14604842) for dual-use work.

[Learn more (opens in new tab)](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)

## Anthropic’s commitment to cyberdefense

Frontier AI capabilities are advancing faster than any single team can respond to, and developers, vendors, researchers, open-source maintainers, and public-sector defenders all have a role to play.

### Supporting open-source security

The internet runs on critical software maintained by people with limited resources. We extend access to capable models, fund the foundations behind them, and disclose vulnerabilities responsibly when Claude finds them.

* [Apply through Claude for Open Source (opens in new tab)](https://claude.com/contact-sales/claude-for-oss)
* [Read our CVD policy (opens in new tab)](https://www.anthropic.com/coordinated-vulnerability-disclosure)
* [See our work with the Linux Foundation (opens in new tab)](http://linuxfoundation.org/blog/project-glasswing-gives-maintainers-advanced-ai-to-secure-open-source)

### Defending mission-critical systems

We partner with the organizations responsible for the world's most critical software and infrastructure — from Project Glasswing's work hardening systemically important code, to our research with Pacific Northwest National Laboratory (PNNL**)** on defending cyber-physical systems.

* [Read the latest on Project Glasswing (opens in new tab)](https://www.anthropic.com/news/expanding-project-glasswing)
* [Read about Anthropic and PNNL](https://red.anthropic.com/2026/critical-infrastructure-defense/)

### Advocating for policy that backs defenders

Our Advanced AI Framework proposes policies for binding obligations on frontier labs, Anthropic included, and government authority to block dangerous deployments, alongside investment in open-source hardening and the safeguards that would let frontier cyber capability reach more defenders safely.

* [Read the Advanced AI Framework (opens in new tab)](https://www.anthropic.com/policy-on-the-ai-exponential/aaif)

## Go deeper on cyberdefense

Everything you need to strengthen your defense posture, from research to implementation guides.

ResearchGuidesIn the field

TitleDate

* [Measuring LLMs’ impact on N-day exploitsDateJune 8, 2026](https://red.anthropic.com/2026/n-days/)
* [Expanding Project GlasswingDateJune 2, 2026](https://www.anthropic.com/news/expanding-project-glasswing)
* [Project Glasswing: An initial updateDateMay 22, 2026](https://www.anthropic.com/research/glasswing-initial-update)
* [Measuring LLMs’ ability to develop exploitsDateMay 22, 2026](https://red.anthropic.com/2026/exploit-evals/)
* [Anthropic's coordinated vulnerabilty disclosure dashboardDateMay 22, 2026](https://red.anthropic.com/2026/cvd/)
* [Assessing Claude Mythos Preview’s cybersecurity capabilitiesDateApril 7, 2026](https://red.anthropic.com/2026/mythos-preview/)
* [Reverse engineering Claude's CVE-2026-2796 exploitDateMarch 6, 2026](https://red.anthropic.com/2026/exploit/)
* [LLM-discovered 0-daysDateFebruary 5, 2026](https://red.anthropic.com/2026/zero-days/)
* [AI models on realistic cyber rangesDateJanuary 16, 2026](https://red.anthropic.com/2026/cyber-toolkits-update/)
* [Finding Bugs with Claude and Property-based TestingDateJanuary 14, 2026](https://red.anthropic.com/2026/property-based-testing/)
* [Experimenting with AI to Defend Critical InfrastructureDateJanuary 8, 2026](https://red.anthropic.com/2026/critical-infrastructure-defense/)

Titlecontent typeDate

* [Using LLMs to secure source codecontent typeBlogDateMay 27, 2026](https://claude.com/resources/articles/using-llms-to-secure-source-code)
* [Zero Trust for AI Agentscontent typeeBookDateMay 27, 2026](https://claude.com/resources/articles/zero-trust-for-ai-agents)
* [Secure the Advantage: A CISO's Guide to Agentic AIcontent typeBlogDateMay 12, 2026](https://claude.com/resources/webinars/secure-the-advantage-a-cisos-guide-to-agentic-ai)
* [Vulnerability Detection Agentcontent typeCookbookDateApril 22, 2026](https://platform.claude.com/cookbook/claude-agent-sdk-06-the-vulnerability-detection-agent)
* [Preparing Your Security Program for AI-Accelerated Offensecontent typeBlogDateApril 10, 2026](https://claude.com/resources/articles/preparing-your-security-program-for-ai-accelerated-offense)
* [Threat Intelligence Enrichment Agentcontent typeCookbookDateApril 7, 2026](https://platform.claude.com/cookbook/tool-use-threat-intel-enrichment-agent)

Titlecontent typeDate

* [Claude Security: Putting Claude to Work for Defenderscontent typeWebinarDateMay 28, 2026](https://claude.com/resources/webinars/claude-security-putting-claude-to-work-for-defenders)
* [How our partners are putting Opus to work for cybersecuritycontent typeBlogDateMay 21, 2026](https://claude.com/resources/articles/how-our-partners-are-putting-opus-to-work-for-cybersecurity)
* [How Anthropic's cybersecurity team built a threat detection platform with Claude Codecontent typeBlogDateMay 12, 2026](https://claude.com/resources/articles/how-anthropic-uses-claude-cybersecurity)
* [Long Running Agents: How Outtake built a Cyber investigator on Claudecontent typeWebinarDateApril 28, 2026](https://claude.com/resources/webinars/outtake-built-cyber-investigator-claude)
* [Partnering with Mozilla to improve Firefox's securitycontent typeBlogDateMarch 6, 2026](https://red.anthropic.com/2026/firefox/)

## Give defenders an edge with Claude

[Contact sales](https://claude.com/contact-sales)[Start building](https://platform.claude.com/)
