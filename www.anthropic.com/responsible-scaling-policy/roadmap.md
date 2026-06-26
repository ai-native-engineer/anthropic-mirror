<!-- source: https://www.anthropic.com/responsible-scaling-policy/roadmap -->

# Anthropic's Frontier Safety Roadmap

We believe that AI capabilities will improve rapidly in the coming years. We will need to quickly and dramatically improve our state of preparedness in a number of areas, especially:

### Security

Preventing theft, sabotage and/or manipulation of our AI models.

### Safeguards

Preventing dangerous use of our models via product surfaces and within Anthropic itself.

### Alignment

Ensuring that our models themselves do not autonomously cause harm, and instead consistently behave in line with our Constitution.

### Policy

Laying out and advocating for a tangible path for policymakers to effectively manage AI risks across the industry, worldwide.

Our Frontier Safety Roadmap aims to chart a course in public for some of our highest-priority goals. Our hopes are twofold.

First, many (though not all) of these goals will need large company-wide efforts. Many people, across many different departments, will need to coordinate with each other across reporting lines. By clearly and publicly articulating these goals, we are aiming for a "forcing function" that helps us pull off this kind of coordination and prioritization. We believe our Responsible Scaling Policy has served this function effectively in the past, as with our [ASL-3 protections](https://www.anthropic.com/news/activating-asl3-protections).

Second, we want to share how we're thinking about the future of safety, at the level of tangible practices. We hope that other AI developers will take inspiration from these goals, and publish their own that we can learn from in turn. And we think policymakers and customers should be aware of where AI safety practices are headed.

These roadmaps are subject to change. Some changes may simply reflect our evolving understanding of how best to mitigate key risks. However, we will strive to avoid situations where we revise the goals in a less ambitious direction because we simply can't execute.

We will provide updates on whether we achieve the goals, and set new goals whenever we do.

> Note: we have made redactions from our public Frontier Safety Roadmap for reasons including protecting sensitive IP and not giving too much information about our current protections to threat actors. The unredacted version is shared with all full-time employees as well as our board and Long-Term Benefit Trust (LTBT).

### Updates

*You can find an archive of all our previous Frontier Safety Roadmap goals [here](https://www.anthropic.com/responsible-scaling-policy/updates).*

1. **April 2, 2026: Launching “moonshot R&D” projects.** We completed this goal by selecting and beginning work on two projects, detailed [below](https://www.anthropic.com/responsible-scaling-policy/roadmap#moonshot-r-d-projects).
2. **April 2, 2026: Principles for data retention.** We completed our goal of writing a “comprehensive internal report to identify how our Safeguards could be improved by updating our data retention policies.” The report was completed and sent to leadership on March 29, 2026. As stated [below](https://www.anthropic.com/responsible-scaling-policy/roadmap#principles-for-data-retention), within 6 weeks of that date, we will publish a new goal related to this or announce that we are not doing so.
3. **May 5, 2026: Principles for data retention.** We removed this content from the page after deciding not to set a new goal on this front. Based in part on the analysis we completed as a prior roadmap goal, we are undertaking a major project to improve our data retention practices for certain future models from a safety point of view, and we will be putting out public content explaining our thinking. We don’t feel that setting a separate date-bound goal in this context would be helpful as a forcing function for the goal—we feel that other internal processes will provide adequate forcing functions.
4. **May 5, 2026: “Moonshot R&D” projects.** We changed our target date for Phase 1 from May 15, 2026 to September 30, 2026 because we decided to focus the relevant resources on accelerating our “Leveling up across the board” goal for the time being. While we still don’t expect to *fully complete* the latter goal in the next few months, we believe we will make significant progress on it, and that the safety benefits of doing so are greater than what we’d realize with our original prioritization. As for the latter goal, our initial discussions have left us skeptical that isolated networks are a feasible path forward inside the next 1-2 years, when [powerful AI may be developed](https://www.darioamodei.com/essay/the-adolescence-of-technology). We still plan to complete Phase 1, which will hopefully leave us with a more confident and grounded view.

## Our goals as of May 5th, 2026

Collaborations to rapidly and responsibly develop AI alongside measures to mitigate the potential for our systems to cause undue harm.

AllSecuritySafeguardsAlignmentPolicyCross-cutting

SecurityTarget: September 15, 2026 and September 30, 2026

### "Moonshot R&D" projects

Security is an ongoing and immediate priority for us, but it is also a long-term challenge where we’ll need to be creative and explore promising and incomplete ideas. This is because we may, at some point in the future, be targets of the world’s best-resourced attackers. Our moonshot R&D projects are exploring ambitious, possibly unconventional ways to achieve unprecedented levels of security.

Current ongoing projects:

* We are exploring a potential prototype of what our key workflows and infrastructure would look like (and what the productivity impact would be) if they were subject to extreme security practices. This would include simulating (at very small scale) isolated networks, “green lines” for limited remote connections, as well as commensurate physical security controls. We will complete Phase 1 - an inventory of needed components and preliminary analysis of costs and timelines - by September 15, 2026 and decide on next steps within 2 weeks of doing so. (It’s possible that we will de-prioritize this project in favor of other work, depending on what we determine in Phase 1.)
* We will develop a prototype by September 30, 2026 of *provable inference*, a technique for reliably, provably “signing” AI model outputs in a way that makes them attributable to a specific set of model weights. In the future, it’s possible that very sophisticated attackers will seek to infiltrate our systems and modify our models after we’ve trained them - whether to sabotage our work or co-opt our models into serving their own goals. If we could reliably and systematically verify that model outputs were coming from a specific set of model weights, we believe this threat would be significantly reduced.

Read more

SecurityTarget: July 1, 2027

### Leveling up across the board

While innovation and creativity are important to security, it’s also the case that security is fundamentally about the strength of the weakest link. That means we need to get a large number of small things right. We have a list of key security improvements that would represent a significant leveling up across many areas of security, and we will aim to achieve a strong majority of them (details below). This will be a large, wide-reaching effort to achieve major hardening of our internal systems against attempts to compromise our model weights, model training, etc.

To assess whether we have reached this goal, we will prepare a report for the Responsible Scaling Officer to mark each invariant as "Not in place," "Mostly in place" or "Fully or near-fully in place." The report's conclusions (though not all details of our security posture) will be circulated to the full company and there will be at least a 7-day comment period for people to remark on observations they've made that may not be consistent with the conclusions. We will consider this goal reached if both of the following are true: we have achieved "Fully or near-fully in place" for at least 60% of invariants, and we have achieved "Mostly in place" for at least 80% of invariants.

We're in a unique position to contribute meaningfully to AI security practices across the industry. We aim to systematically share what we’ve learned from all of our security commitments—through blog posts, conference talks, and open source contributions—to help raise the security bar across the AI industry

|  |  |
| --- | --- |
| Area of improvement | Desired State1 |
| Identity, Secrets Management, and Framework | * Systems, employees, and automated processes in sensitive environments use cryptographically verified short-lived identities, reducing the window of opportunity if credentials are compromised. * Sensitive credentials are managed through a central system that supports automated rotation. * We systematically review and reduce access entitlements through periodic reviews, targeting permissions that are stale, excessive, or no longer business-justified. * Internal services in sensitive environments require authentication and authorization using approved methods (e.g. mTLS) and encrypt communications in transit |
| Infrastructure Security | * Workload configurations that deviate from hardened security defaults in frontier clusters require explicit security team approval and ongoing tracking. * Kubernetes access controls are understandable and auditable, and deployed consistently and automatically across frontier clusters. * Sensitive environments use allowlist-based network controls for Internet egress, connecting only to pre-approved destinations * Technical controls prevent accidental exposure of internal systems to the internet, with continuous monitoring of all systems accessible from the internet. * Cloud identity and access management (IAM) permissions are continuously scanned for misconfigurations, with critical issues resolved within SLA. |
| Supply Chain Security | * Software builds that power sensitive environments have integrity guarantees for their sources and dependencies come from verified sources * Deployments to sensitive environments are logged and inventoried. * Integrated Development Environments (IDEs) used for frontier model development are centrally managed, with third-party components subject to security evaluation and ongoing monitoring. * Frontier models are tamper resistant for production inference deployment, with verification that the model running in production matches the intended version. |
| Application Security | * Critical systems undergo formal threat modeling and security review. Fast-moving projects have dedicated security partners. * Research systems are regularly tested by penetration testers with a focus on lateral movement * Automated security testing continuously probes services in sensitive environments * Vulnerability management is proactive: we systematically detect known vulnerabilities, prioritize based on exploitability and reachability in our environment, and enforce remediation timelines for issues that pose genuine risk. |
| Corporate Security | * Employee devices are configured so that only approved software can run. * Corporate applications require authentication from managed devices as part of context aware access (CAA). Unmanaged devices cannot access company systems. |
| Detection and Response | * We maintain validated detection capabilities for the critical attack scenarios in our threat models, including protection of model weights, training integrity, insider threats, and AI system misuse. Detection coverage is measured against priority attack techniques with defined targets. * We use AI-assisted tools to accelerate security investigations, enabling faster triage of alerts and reduced investigation times through automated analysis and playbook execution. * Detection effectiveness is continuously measured including coverage of attack techniques, time to detect threats, and accuracy. Regular adversarial exercises validate our detection capabilities and drive improvements. * Security alerts maintain high precision to minimize false positives. High-priority scenarios have documented response procedures, adequate on-call staffing, and incident response capabilities, which are regularly validated. |
| Physical Security | * Core office facilities meet security standards with consistent physical security controls. * Automated detection and alerting exists for anomalous behaviors that may indicate insider risks. * A global security operations center provides continuous monitoring with AI-enhanced analysis and response capabilities. |

We have moderate confidence that we can achieve this goal. The list of invariants is long and has many dependencies, and we will need substantially more security capacity staffing than we currently have, but we’ve made a substantial effort to determine what is realistic.

Read more

SafeguardsTarget: January 1, 2027

### World-class internal red-teaming

Today, we continually test our safeguards against AI misuse by red-teaming them in a variety of ways, including via a [bug bounty](https://www.anthropic.com/news/testing-our-safety-defenses-with-a-new-bug-bounty-program) program that offers rewards to anyone who can identify jailbreak techniques of concern. In the future, we may need to prevent misuse from actors more sophisticated than what we can simulate with these methods. We believe we can develop a method for red-teaming our systems (likely involving significant automation) that outperforms the collective contributions from the hundreds of participants in our bug bounty. This could put us in position to continue leveling up over time and stay ahead of even state-sponsored threat actors with large teams devoted to bypassing our safeguards.

We will establish an internal jailbreak-finding method for classifier guards (focused on chemical and biological weapons) that matches or exceeds the current collective abilities of all of our [bug bounty](https://www.anthropic.com/news/testing-our-safety-defenses-with-a-new-bug-bounty-program) participants to find jailbreaks. We will assess this via a report that evaluates whether our internal findings are more substantial in aggregate than our bug bounty findings.

We have moderate confidence that we can achieve this goal. We have a technical path in mind that we believe should succeed if we can execute on it well, but this is a research problem and progress may be hard to predict.

Read more

SafeguardsTarget: January 1, 2027

### Fully automated attack investigations

We have already seen [coordinated, sophisticated efforts to misuse our systems for espionage](https://www.anthropic.com/news/disrupting-AI-espionage). Stopping these efforts requires more than blocking individual AI outputs - it can involve dedicated investigation of patterns across many users and interactions. We believe we can build a system that conducts effective investigations with minimal or no human involvement, a major step forward for our ability to detect misuse at scale. Our initial efforts will focus on investigating potential cyber attacks on a subset of product surfaces.

We will develop an automated system intended to detect a large majority of sophisticated cyber attacks that use Claude, with minimal or no human involvement, along with a plan to assess precision and recall (likely based on red teaming).

This system will not necessarily be usable for all of our product surfaces and environments at the outset. It will be a proof-of-concept that we assess in the environments most conducive to it, which will include major production environments.

We have moderate confidence that we can achieve this goal. We already have some preliminary systems that provide a starting point.

Read more

AlignmentTarget: October 1, 2026

### Upholding Claude’s Constitution

We recently published [Claude’s Constitution](https://www.anthropic.com/constitution), which explains the kind of entity we want Claude to be and what principles we hope its behavior will follow. We already have a number of measures in place to ensure that the way we train Claude is in line with the Constitution, but we aim to make these measures more complete and systematic:

* We will keep our public Constitution up to date and run a systematic oversight process over our training data to evaluate alignment with it.
* We will perform systematic “alignment assessments” to examine Claude’s behavioral patterns and propensities, and evaluate whether they are in line with the spirit of the Constitution. These alignment assessments will incorporate findings from our interpretability research, and will validate the effectiveness of our methods using testing exercises with intentionally misaligned models. We will publish our findings in our system cards or Risk Reports.

**Keeping the Constitution up to date and running a systematic oversight process.** We will ensure that the public [Claude’s Constitution](https://www.anthropic.com/constitution) stays in sync with what we use internally (updating it within 90 days of relevant internal updates). We may also use additional guidelines and other training data (such as human preference labels) that are in line with Claude’s Constitution without publishing those.

We will run an oversight process over a representative sample of our production-relevant post-training data and rewards to evaluate alignment with the Constitution, aiming to ensure that we review for any egregious inconsistencies with the Constitution in ways that Claude itself can detect and will describe this oversight process in our Risk Reports.

In the future, we will work to extend the above to all models used in high-stakes usage, including, e.g., internal-only models used for evaluation purposes. But our immediate goal is to establish the above for our mainline models.

Our long-term goal, which may require further progress after we achieve the goal listed here, is that cases where production releases of Claude egregiously violate the Constitution on real-world traffic in ways that Claude itself could detect are rare or require explicit jailbreaks.

We have moderate confidence that we can achieve this goal. We already take measures along the lines of the above, but will work to make them more consistent and systematic.

**Alignment assessments.** We will continue developing and maintaining our alignment assessment pipeline (see past alignment assessments in our [system cards](https://www.anthropic.com/system-cards)) and will ensure that it makes use of both interpretability and non-interpretability techniques. We will aim to use interpretability in particular in such a way that it produces meaningful signal beyond behavioral methods alone. We will thoroughly red-team our alignment arguments, which will likely include testing our assessment pipeline by assessing adversarially-designed misaligned model-organisms, though we may take other approaches if the analysis in our Risk Reports depends primarily on something other than auditing. We will continue to apply this auditing pipeline (a) prior to publicly deploying any model that is significantly more capable than any of the models described in our previous Risk Report; (b) within a reasonable period of time following the deployment of an internal or other non-public model that we determine could pose notable risks (in line with the threat models emphasized in our most recent Risk Report) distinct from those of public models. The latter will—at a minimum—include any internal models that we are deploying for large-scale, fully autonomous research and that are significantly more capable than our most capable such models as of the publication of our previous Risk Report.

We will be open about what we find, as feasible while protecting our IP around the development of model capabilities. For new internal deployments, the Responsible Scaling Officer can (and usually will) allow a temporary internal deployment before the audit is complete. This will be allowed as long as we complete our audit and seek another approval within a reasonable period of time. Our Risk Reports will examine these decisions.

We have high confidence we can achieve the non-interpretability parts of this goal and moderate confidence that we can achieve the interpretability parts of this goal. Our current practices are already fairly similar to the above, but it will require ongoing effort to maintain and improve their adequacy in the face of improving capabilities and to fully expand their coverage to internal deployments. We have done several limited red-teaming exercises to date, but think more would be needed in order to qualify as thoroughly red-teaming our alignment arguments, and using interpretability techniques on new frontier models are at risk of taking longer than initial release dates.

Read more

Cross-cuttingTarget: January 1, 2027

### Moving toward an “eyes on everything” state for our internal AI development activities

For many reasons - preventing theft or sabotage of our models, ensuring adherence to [Claude’s Constitution](https://www.anthropic.com/constitution), and ensuring that our model training hasn’t been manipulated by insiders or attackers (or [AI models themselves](https://alignment.anthropic.com/2025/sabotage-risk-report/)) - we want our internal environment to be intensively monitored and comprehensively understood. We aim to establish comprehensive, centralized records of all our critical AI development activities, and to use AI to analyze these records for issues including concerning behavior by insiders (both human and AI) and security threats.

**Security team subgoal**

**We will improve our observability across the board to the point of relative maturity - involving centralized, searchable logs with the most important relevant information for all of our critical security systems, and robust processes for keeping these logs available.** We believe that if we can establish comprehensive logging of crucial internal activity, we’ll put ourselves in a much better position to leverage current and future advanced AI capabilities for security (since AI systems can be used to analyze our logs). We also believe that some key threat models - including the possibility of both human and AI attackers corrupting our training runs - could be significantly ameliorated if we simply have high odds of detecting when they happen (even if response to those detections lags considerably).

To assess whether we have reached this goal, we will prepare a report for the Responsible Scaling Officer to mark each invariant as "Not in place," "Mostly in place" or "Fully or near-fully in place." The report's conclusions (though not all details of our security posture) will be circulated to the full company and there will be at least a 7-day comment period for people to remark on observations they've made that may not be consistent with the conclusions. We will consider this goal reached if both of the following are true: we have achieved "Fully or near-fully in place" for at least 60% of invariants, and we have achieved "Mostly in place" for at least 80% of invariants.

| Area of improvement | Desired State4 |
| --- | --- |
| Log coverage | * A catalog of log sources exists, labeled by priority and criticality to security * A standardized ingestion process enables logging at deployment time with limited friction |
| Instrumentation | * Libraries and frameworks exist to streamline log onboarding and prevent inadvertent logging of sensitive information |
| Log completeness | * A standardized process evaluates log completeness and identifies gaps * A feedback loop between completeness assessments and instrumentation deployments systematically detects gaps when new systems or environments are created, with systematic remediation or flagging for review |
| Log accessibility | * AI-enabled search exists via a centralized platform with consistent query patterns across all log sources * The system maintains high availability and reliability sufficient for operational use |
| Log pipeline health | * Systematic monitoring continuously tracks pipeline health with alerting on failures, throughput degradation, and data quality problems |

We have moderate confidence that we can achieve this goal (somewhat more so than for our security maturity goal). The list of sub-goals is fairly long and has many dependencies, and we will need to prioritize and resource this work more than in the past, but we’ve made a substantial effort to determine what is realistic.

**Alignment team subgoal**

We will ensure that we are cataloging all high-stakes internal usage of Claude, such as situations where we use Claude internally for fully autonomous research or other situations where it might have an opportunity to engage in catastrophic sabotage, in line with our [current threat models](https://alignment.anthropic.com/2025/sabotage-risk-report/2025_pilot_risk_report.pdf).

We will implement monitoring that we believe is sufficient to produce evidence of egregious sabotage-oriented activities in high-stakes use cases with high probability, under the assumption that Claude has general capabilities broadly comparable to those of a full-time entry level Research Engineer. In cases where we have high confidence that models are sufficiently aligned such that risks are low, we will not consider this monitoring to be necessary.

We will evaluate the effectiveness of our monitoring tools, likely using a combination of human and automated red teaming and adversarially-designed model organisms, and will discuss our findings in our Risk Reports.

We have moderate confidence that we can make Claude aligned enough that monitoring will not be strictly necessary, at least in the medium term. We have moderate-to-high confidence we can put our monitoring goal in position to achieve the goal, as needed. We already do a fair amount of internal monitoring, but need to make it more comprehensive and accurate.

Read more

PolicyTarget: July 1, 2026

### A roadmap for policymakers

We will develop and share a set of ambitious policy proposals to effectively manage industry AI risks globally without unnecessarily limiting the benefits from AI development or slowing the AI development of democracies relative to that of autocracies.

We believe the right framework is a **regulatory ladder**: requirements that scale with risk. Today's frontier models require transparency and basic oversight. Yet as capabilities increase, we are moving towards a need for more rigorous external testing, stronger incident reporting, and deeper government oversight. At the most advanced capability levels and risks, the appropriate governance analogy may be closer to nuclear energy or financial regulation than to today's approach to software.

As with our advocacy for transparency [frameworks](https://www.anthropic.com/news/the-need-for-transparency-in-frontier-ai) as a starting point, we will develop and advocate for more advanced and risk-appropriate proposals in collaboration with a wide array of stakeholders.

## Expectations as AI capabilities advance

With the above goals in mind, this section outlines the risk mitigations we believe we’ll be in position to implement as AI capabilities advance, focused on the threat models we emphasize in our Responsible Scaling Policy.

### Today’s capabilities and mitigations February 22nd, 2026

Our most powerful models today—those with the ability to significantly help individuals or groups with basic technical backgrounds create/obtain and deploy chemical and/or biological weapons with serious potential for catastrophic damages—are safeguarded with [ASL-3 protections](https://www.anthropic.com/news/activating-asl3-protections).

We plan to maintain or improve these protections for relevant models. The key elements of these protections are: safeguards at least as robust as our initial [Constitutional Classifiers](https://www.anthropic.com/research/constitutional-classifiers); access controls for trusted users with exemptions to classifier guards; and methods such as red-teaming, bug bounties, and threat intelligence for continually assessing the threat of jailbreaks; and a number of noteworthy [security controls](https://www-cdn.anthropic.com/807c59454757214bfd37592d6e048079cd7a7728.pdf). The specific tools and methods we use may evolve, but our protections will be at least as rigorous as those we have in place today.

We hope and expect that these measures will remain sufficient to meet our goal of being both (a) robust to persistent attempts to misuse a potentially dangerous capability, and (b) highly protected against most attackers’ attempts at stealing model weights. We will continue to adapt our defenses as attack methods evolve. However, while we can and will maintain the rigor of our protections, we cannot assure a specific level of effectiveness against future attackers, given attackers’ continuous adaptability and the evolving risk landscape.

Additionally, [today’s models](https://www.anthropic.com/system-cards) show strong and improving capabilities for extended, autonomous technical work, and are increasingly relied on for writing high-stakes code. In our Risk Reports, we now regularly analyze the possibility that these models might execute high-stakes sabotage. We believe that our current alignment assessment methods and monitoring practices are sufficient to make the case that the risk of catastrophic sabotage is very low (though not negligible).

### Potential advances in the next few months

As capabilities improve, we are monitoring for significant advances in our models' chemical and biological weapons capabilities, focusing on the point where the models could significantly help threat actors (for example, moderately resourced expert-backed teams) create or obtain and deploy chemical and/or biological weapons with potential for catastrophic damages far beyond those of past catastrophes in this category such as COVID-19.

If and when we determine that this is the case, we will apply protections at least as strong as our current ASL-3 protections (see above) to an expanded set of potential use cases for AI, covering the most likely vectors for this threat. Additionally, we will identify the most concerning specific threat pathways, create policy recommendations for early detection and response for such threats, and share this content with policy leaders.

### Automated R&D

We believe it is plausible, as soon as early 2027, that our AI systems could fully automate, or otherwise dramatically accelerate, the work of large, top-tier teams of human researchers in domains where fast progress could cause threats to international security and/or rapid disruptions to the global balance of power—for example, energy, robotics, weapons development and AI itself.

By that point, we expect to have accomplished most of the goals listed above, including:

* Resourcing and completing significant “[moonshot R&D security](#launching-moonshot-r-d-projects)” projects, currently focused on provable inference and a mock secure research environment.
* Developing [world-class internal red-teaming](#world-class-internal-red-teaming) and [automated attack investigations](#fully-automated-attack-investigations).
* Publishing and advocating for a roadmap for policymakers to achieve industry-wide safety without unnecessarily limiting the benefits from AI development or slowing the AI development of democracies relative to that of autocracies.
* Achieving an [“eyes on everything”](#moving-toward-an-eyes-on-everything-state-for-our-internal-ai-development-activities) state for our internal AI development.
* Consistently implementing systematic alignment audits and other measures for upholding Claude’s Constitution.

We hope and expect to meet these targets on time or ahead of schedule, set new ones, and continually raise the bar for our risk mitigations.
