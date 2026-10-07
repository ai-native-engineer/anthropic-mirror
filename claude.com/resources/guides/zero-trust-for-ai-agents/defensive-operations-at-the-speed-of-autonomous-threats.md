<!-- source: https://claude.com/resources/guides/zero-trust-for-ai-agents/defensive-operations-at-the-speed-of-autonomous-threats -->

Chapter 076 min read

# Defensive operations at the speed of autonomous threats

6 min read

9 min remaining

Securing the agents you deploy is half the work. The other half is running security operations fast enough to contend with attackers who are themselves AI-accelerated. When exploits appear within hours of a patch, response processes that take days are too slow. Agentic adversaries might attack hundreds or thousands of systems in the time required for a human to review a single alert.

## The case for autonomous defense

Traditional security operations assume humans analyze alerts and decide on responses. That methodology struggles when attackers can probe defenses, adapt techniques, and exfiltrate data faster than analysts can respond. The answer is not to remove humans from the loop — it is to move humans off the bookkeeping and onto the decisions. Automate evidence collection, enrichment, correlation, and documentation. Keep humans on containment calls, disclosure calls, and customer-comms calls. Human decision speed during an incident should never be rate-limited on evidence collection or write-ups.

## Put a model at the front of your alert queue

Every inbound alert should get an automated first-pass investigation before a human sees it. A triage agent with read-only access to your SIEM and a well-scoped set of query tools can direct analyst attention to the alerts that most need human judgement.

Practical start: pick one noisy rule with a known-high false positive rate. Wire a frontier model into its alert stream with read-only access to the underlying data, and have it produce a structured disposition for every firing. Measure agreement against a human reviewer for two weeks. If the agreement rate is tolerable, expand to the next rule. Do not try to automate the whole queue at once.

## Agentic security orchestration

Today, Security Orchestration, Automation, and Response (SOAR) platforms enable security teams to integrate and coordinate separate security tools, automate repetitive tasks, and streamline incident and threat response workflows.

The next generation of SOAR is Agentic SOAR, which adds adaptive capabilities that respond to novel situations. This allows flexibility beyond existing playbooks and the adaptability to directly address malicious AI-driven attacks within seconds.

Response actions for suspicious traffic or behavior could include automated quarantine or isolation at the network or system level, dynamic access control adjustments at the user or resource level, session termination, and credential revocation — all executed through the identity-based isolation and short-lived-credential infrastructure built in Part III.

## Map detection coverage against MITRE ATT&CK

[MITRE ATT&CK (opens in new tab)](https://attack.mitre.org/) provides a standard vocabulary of attacker techniques that most detection tools already use. Knowing which techniques you can detect, and which you can't, is more useful than a general goal to "improve detection." Prioritize coverage for lateral movement and credential access. These are where AI-accelerated attackers will get the most leverage from compromised agent identities.

[Atomic Red Team (opens in new tab)](https://atomicredteam.io/) is an open-source library of small, safe tests mapped to ATT&CK techniques; running a handful and checking which ones your existing logging actually detected is a one-afternoon exercise that produces a concrete coverage map.

## Run a tabletop for five simultaneous incidents, not one

The standard tabletop exercise assumes one critical CVE with a working exploit hits on a Monday. Run the version where five hit in the same week. Intake, triage, and remediation tracking should scale accordingly — a workflow built around a spreadsheet and a weekly meeting will not keep up. Plan for an order-of-magnitude increase in finding volume and rehearse it before it happens.

## Establish emergency change procedures in advance

A two-week change-approval cycle for production patches is itself a security risk. The same applies to emergency containment actions: taking a service offline, rotating a credential, blocking a network path. Decide in advance who can authorize these, how fast they can be authorized, and what evidence is required. Practice the authorization path so it is not improvised during an incident.

## Trust through verification for defensive agents

Agentic SOAR capabilities are powerful, and their blast radius can be significant. The same Zero Trust principles outlined earlier need to be applied. Organizations should not blindly trust defensive automation any more than they trust other autonomous systems.

**Verified integrity** ensures agentic SOAR systems have not been compromised. Attackers who compromise defensive agents gain powerful capabilities. Defensive agents should run in hardened environments with strong integrity verification.

**Limited blast radius** constrains what defensive agents can do. Even trusted defensive systems should operate with least privilege. Automated response capabilities should be scoped to specific actions with clear boundaries.

**Clear escalation paths** ensure humans remain informed and in control. Automated responses should generate alerts for human review. High-impact responses should require human approval even when automated systems recommend them.

The monitoring and audit capabilities described earlier apply to defensive agents as well. Defensive agent actions should be logged, traced, and reviewed just like any other agent activity. This ensures accountability and enables improvement of defensive capabilities over time.
