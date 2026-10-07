<!-- source: https://claude.com/resources/guides/zero-trust-for-ai-agents/applying-zero-trust-to-agentic-ai-services -->

Chapter 0519 min read

# Applying Zero Trust to agentic AI services

19 min read

50 min remaining

**The remainder of this document is implementation guidance. Security architects and engineers should work through the tier tables and workflow sections; security leaders can use the executive summary and Part II as a briefing document.**

Identifying and mitigating current threats keeps you reactive, always chasing the next exploit. Building your agentic solutions on Zero Trust principles puts you on firmer ground.

The principles are presented across three capability tiers:

* **Foundation** represents the minimum viable security appropriate for smaller deployments or initial implementations. Because AI-accelerated offense has compressed exploitation timelines, the Foundation floor has been raised: friction-only controls no longer qualify.
* **Enterprise** reflects enterprise standard practices that most organizations with significant deployments should target.
* **Advanced** describes aspirational capabilities for most organizations, or baseline for organizations with high-risk deployments/stringent regulatory requirements.

The *Foundation* tier serves as your entry into solid Zero Trust agentic practices. It lays the groundwork for future risk mitigation and, depending on the size and needs of your organization, might meet your risk tolerance on its own. For most, though, Foundation will only satisfy risk requirements for small businesses and teams.

*Enterprise* is where most organizations should aim. This tier takes the Foundation controls and adds the depth needed to handle real-world complexity: larger teams, multiple agentic deployments, and environments where a single compromise carries meaningful business impact. If your organization operates at any significant scale, Enterprise represents your target maturity level.

*Advanced* capabilities go beyond what most organizations need day to day. This tier applies to environments where the stakes demand it, such as highly regulated industries, national security applications, or deployments where a breach carries severe operational or financial consequences. Most organizations will find that **Enterprise** controls satisfy their risk tolerance, but if your threat model includes sophisticated adversaries or your regulatory environment leaves little room for error, **Advanced** is your baseline.

Each tier builds on the one before it, so advancing from **Foundation** to **Enterprise** means strengthening existing controls rather than replacing them. Keep in mind that the countermeasures outlined below depend on supporting infrastructure and services surrounding your agentic deployments. This is a fast-moving space. Every capability described here exists today but the tooling and adoption are still maturing. Expect the **Advanced** tier to become **Enterprise** standard as the space evolves, and **Enterprise** to become **Foundation**.

## Agent identity and authentication

Identity and authentication form the foundation for every other security capability. Without verifiable identity, you cannot enforce access controls, maintain audit trails, or attribute actions to specific agents.

### Agent identity verification

Verifiable identity enables you to attribute actions, enforce access controls, and conduct meaningful audits. Without distinct identities, agents operate in an attribution gap where enforcing Least Agency becomes impossible.

Agent identity verification capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Unique cryptographic identifiers for each agent instance | Assign persistent agent IDs backed by cryptographic material (not just labels). Track agent lifecycle from creation through retirement. IDs appear in all logs and access requests. |
| Enterprise | Certificate-based authentication with full lifecycle management | Issue X.509 certificates to each agent. Require certificate presentation for all service connections. Implement certificate lifecycle management, including rotation and revocation. |
| Advanced | Hardware-backed identity with attestation | Store agent credentials in hardware security modules (HSMs) or trusted platform modules (TPMs). Implement remote attestation to verify agent integrity before granting access. Use confidential computing enclaves for sensitive operations. |

Unique identifiers alone are a labeling exercise; the Foundation tier now requires those identifiers to be cryptographically rooted so that identity forgery is actually hard. Cryptographic identity is what makes non-repudiation possible. Hardware-backed identity makes this stronger still, and for any production system reachable from the internet we increasingly recommend it as the target state.

### Service authentication

Establishing agent identity solves half the problem, but agents must also prove that identity when accessing databases, APIs, and other services. Static API keys and shared service-account passwords are among the first things an attacker with model-assisted code analysis will find; they are no longer a legitimate entry point, not even at Foundation. Short-lived, narrowly-scoped tokens issued by an identity provider are the new baseline.

Service authentication capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Short-lived tokens issued by an identity provider, with automatic refresh | Implement OAuth 2.0 or similar token-based authentication. Issue tokens with expiration measured in minutes. Automate token refresh without human intervention. Never embed credentials in code or configuration files. |
| Enterprise | Mutual TLS with certificate pinning | Require both client and server certificate validation. Pin expected certificates to prevent man-in-the-middle attacks. Implement certificate transparency monitoring. |
| Advanced | Hardware-bound credentials with attested issuance | Bind authentication material to hardware identity so credentials cannot be exfiltrated from a compromised host. Root every service-to-service call in attested hardware, including calls between production services. |

If you are running API keys with rotation policies today, treat it as a known gap rather than a legitimate Foundation posture. Rotating a credential that can be grepped out of a lockfile does not raise the cost to an AI-assisted attacker meaningfully. Move to short-lived tokens first, and bind credentials to hardware wherever you can.

## Access control and privilege management

Even perfectly authenticated agents cause damage when granted excessive permissions. The authorization layer enforces Least Agency, ensuring agents receive only the access required for their specific function.

### Permission models

Permission models determine what actions agents can perform. More sophisticated models enable finer-grained control and context-aware decisions aligned with Zero Trust principles.

Permission model capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Role-based access control (RBAC) with deny-by-default | Define roles matching agent functions. Assign minimum permissions required for each role. Block all access not explicitly granted. Treat this as a starting posture, not a destination. |
| Enterprise | Attribute-based access control (ABAC) with context-aware policies | Incorporate request attributes including time, location, data sensitivity, and risk score into authorization decisions. Adjust permissions dynamically based on context. |
| Advanced | Continuous authorization with real-time policy evaluation | Evaluate authorization at each action rather than session start. Integrate threat intelligence and behavioral analytics into authorization decisions. Revoke access immediately when risk indicators change. |

At a minimum, agents should only have permissions related to their role. An email-drafting agent needs email permissions, not access to the finance department file share. Attribute-based controls add context, such as restricting an agent to operating hours so it cannot be exploited outside of them. Continuous authorization goes further by periodically re-evaluating access, allowing compromised agents to have credentials revoked the moment they fail a challenge.

### Privilege scoping

While permission models define what agents can do, privilege scoping determines when those permissions apply and how long they last.

Static permissions granted at deployment remain active indefinitely, creating persistent exposure. Dynamic privilege scoping grants access only when needed and revokes it automatically, limiting blast radius and exposure windows.

Privilege scoping capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Static least-privilege roles per agent function | Define role boundaries during agent deployment. Review and certify permissions periodically. Remove unused permissions during reviews. |
| Enterprise | Dynamic privilege adjustment based on task requirements | Elevate permissions only when specific tasks require them. Return to baseline permissions after task completion. Log all privilege changes. |
| Advanced | Just-In-Time (JIT) and Just-Enough-Administration (JEA) with automatic expiration | Grant permissions only at moment of need. Scope access to specific resources for specific durations. Automatically revoke permissions after task completion or timeout. |

Privilege scoping is the practical application of least agency. At the Foundation level, agents receive only the static permissions their tasks require, aligning closely with RBAC. Dynamic privilege elevates access only when necessary, similar to an operating system prompting for an administrator password, then returning to standard permissions afterward. JIT/JEA takes this further by automatically revoking elevated permissions the moment the task completes, ensuring no standing access persists beyond what is actively needed.

### Resource boundaries

Even with perfect access controls, a compromised agent can exploit its granted permissions to attack adjacent systems. Isolation mechanisms contain the blast radius by preventing lateral movement between agents and limiting what compromised agents can reach.

Identity-based isolation is the primary control. Network segmentation can still reduce blast radius and noise, but it is a backstop: an attacker who can reach a segment boundary will pivot through it if the services on the other side accept any caller from that network. Enforce isolation at the receiving end — every workload carries its own cryptographic identity, and each service accepts connections only from the specific callers its policy names.

Resource boundary capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Identity-based isolation of agent workloads, backed by network segmentation | Give every agent workload a cryptographic identity; have services accept connections only from explicitly named callers. Use network segmentation as a backstop, not the primary boundary. Block unnecessary east-west traffic. |
| Enterprise | Sandboxed execution environments per agent | Run agents in containers with restricted capabilities. Use container runtimes like gVisor that provide additional syscall filtering. Limit mounted volumes and network access. Treat sandboxing as table stakes for any agent handling untrusted input. |
| Advanced | Hardware isolation with confidential computing | Deploy agents in hardware-isolated environments using technologies like AMD SEV or Intel TDX. Implement microVM architectures using lightweight hypervisors. Verify execution environment integrity through attestation. |

Sandboxed execution constrains what a compromised agent can reach, even within its own identity boundary, and should be considered mandatory rather than aspirational for agents that process web content, documents, or any other untrusted input. Hardware isolation takes this further by ensuring that not even the host operating system can inspect or tamper with agent workloads.

Pro-tip

Claude Code supports this by providing [deny-by-default permissions (opens in new tab)](https://code.claude.com/docs/en/permissions#permission-system) that require explicit approval for every write and execute operation, [sandboxed execution (opens in new tab)](https://code.claude.com/docs/en/sandboxing) with OS-level filesystem and network isolation, [write access restrictions (opens in new tab)](https://code.claude.com/docs/en/security#built-in-protections) that confine modifications to the project directory, and [managed settings (opens in new tab)](https://code.claude.com/docs/en/permissions#managed-settings) that let administrators enforce organization-wide permission policies that users cannot override.

## Observability and auditing

Access controls prevent unauthorized actions. Observability reveals what actually happened. Without comprehensive logging and audit trails, you cannot verify that access controls worked as intended, investigate incidents, or demonstrate compliance. Effective observability captures not just what agents did, but why they did it and who authorized it.

Before investing anywhere else in detection, instrument two things: **dwell time** (how long between an anomaly occurring and a human becoming aware of it) and **coverage** (the fraction of alerts that actually get investigated). These are the two metrics AI-assisted automation has the greatest leverage to move, and they matter most when exploit windows shorten.

### Action logging

Comprehensive logging captures what agents do, when they do it, and under what authority. This creates the foundation for incident investigation, compliance demonstration, and behavioral analysis.

Action logging capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Comprehensive logs of agent actions with timestamps and context | Log all tool invocations, data access, and external communications. Include agent identity, action details, and request context. Retain logs according to regulatory requirements. |
| Enterprise | Immutable audit trails with integrity verification | Write logs to append-only storage. Implement cryptographic verification of log integrity. Replicate logs to prevent single-point tampering. |
| Advanced | Real-time streaming to SIEM with correlation capabilities | Stream logs to centralized security monitoring. Correlate agent activity with other security events. Enable real-time alerting on suspicious patterns. |

Auditing is fundamental to understanding what is going on within your environment, and agents are no different. The difference between the implementations here is the integrity of the logs and the comprehensive real-time visibility you have at any given time. Immutability is implemented at the Enterprise level, preventing unauthorized changes. Visibility and correlation are available at Advanced, allowing you to understand not only what has happened, but what is happening currently and to identify trends.

### Traceability

Logs capture individual actions. Traceability connects those actions into complete sequences, linking each agent decision back to the original triggering event. This enables root cause analysis and accountability when investigating incidents.

Traceability capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Request IDs linking agent actions to triggering events | Generate unique identifiers for each user request. Propagate IDs through all resulting agent actions. Enable filtering logs by request chain. |
| Enterprise | Distributed tracing across multi-agent workflows | Implement OpenTelemetry or similar standards for cross-agent tracing. Capture timing and dependency information. Visualize request flows across agent boundaries. |
| Advanced | Full provenance chains from input to output with intermediate steps | Record complete decision history including retrieved context, tool outputs, and reasoning steps. Enable replay of agent decisions for audit. Support regulatory requirements for algorithmic explainability. |

Unlike auditing which captures events on systems and services that agents interact with, traceability provides insight into the agent actions themselves. This includes internal actions, tool calls, sub-agent spawns, etc. The progression through the tiers here is the extent to which traceability is required within your organization.

Pro-tip

Claude Code supports this by providing [OpenTelemetry metrics (opens in new tab)](https://code.claude.com/docs/en/monitoring-usage) for tracking and auditing agent activity, [audit logging (opens in new tab)](https://code.claude.com/docs/en/security#cloud-execution-security) for all operations in cloud environments, [natural language descriptions (opens in new tab)](https://code.claude.com/docs/en/security#built-in-protections) of complex commands for human-readable traceability, and [ConfigChange hooks (opens in new tab)](https://code.claude.com/docs/en/hooks) that audit or block settings changes during sessions.

## Behavioral monitoring and response

Observability captures what agents do. Behavioral monitoring determines whether those actions are normal or suspicious. Logs and traces provide the data, but detecting compromise requires understanding baseline behavior and identifying deviations. Effective monitoring moves from reactive investigation to proactive threat detection.

### Baseline establishment

Establishing baseline agent behavior enables detection of anomalies that may indicate compromise or malfunction.

Baseline establishment capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Manual definition of expected agent behavior patterns | Document intended agent capabilities and access patterns. Define boundaries that should trigger alerts. Review and update definitions as agent functions evolve. |
| Enterprise | Automated baseline learning from normal operations | Deploy monitoring that observes agent behavior and establishes statistical baselines. Identify typical tool usage patterns, access frequencies, and data volumes. |
| Advanced | Continuous baseline refinement with drift detection | Update baselines as agent behavior legitimately evolves. Detect gradual drift that might indicate slow poisoning attacks. Alert on both sudden anomalies and gradual divergence. |

Knowing what "normal" looks like for an agent serves two purposes. First, it gives you a behavioral attribute for ABAC-based access control, letting you flag or restrict requests that fall outside established patterns. Second, it gives you a recovery point. If a configuration change degrades performance or a malicious actor compromises your agentic service, a captured baseline lets you restore the agent to a known good state rather than rebuilding from scratch.

### Anomaly detection

Detecting anomalies early limits damage. Identifying deviations from expected behavior provides warning before compromised agents cause significant harm, enabling response at detection speed rather than discovery.

Anomaly detection capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Threshold-based alerts for obvious deviations, backed by an automated first-pass triage | Define thresholds for metrics like API call rates, data access volumes, and error frequencies. Alert when thresholds are exceeded. Route every alert through an automated first-pass investigation before a human sees it. |
| Enterprise | Statistical anomaly detection with tunable sensitivity | Apply statistical methods to identify unusual patterns. Adjust sensitivity to balance detection rate against false positives. Correlate anomalies across multiple metrics. |
| Advanced | Machine learning-based behavioral analysis with contextual awareness | Deploy ML models trained on normal agent behavior. Incorporate context including time of day, user activity, and business cycles. Detect subtle anomalies that threshold-based approaches miss. |

Anomaly detection depends directly on the baselines you established in the previous section. Without a clear picture of normal behavior, you have no reference point for identifying what qualifies as abnormal. The stronger your baselines, the more effectively your detection can distinguish genuine threats from routine variation.

### Automated response

Detecting anomalies matters only if you respond quickly enough to contain damage. Manual response creates delays where compromised agents continue operating. Automated response limits exposure by taking immediate action, from terminating sessions to revoking credentials at machine speed. A clear rule applies here: **automate the bookkeeping around incidents, not the decisions.** Models should take notes, capture artifacts, pursue parallel investigation tracks, and draft the postmortem. Humans should make the containment calls, the disclosure calls, and the customer-comms calls.

Automated response capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Alerting to security teams for investigation, with model-drafted triage context | Route anomaly alerts to security operations. A triage agent produces a structured disposition (query, think, report) before the human sees the alert. Establish response procedures for common alert types. |
| Enterprise | Automatic containment actions, including session termination and access revocation | Implement automated responses for high-confidence threats. Terminate suspicious agent sessions. Revoke credentials pending investigation. |
| Advanced | Orchestrated response playbooks with graduated escalation | Deploy SOAR capabilities for automated investigation and response. Implement graduated responses based on threat severity. Coordinate containment across multiple systems. |

Combining behavior baselines and anomaly detection with automated response, an agent that deviates from established behavior patterns can trigger automatic privilege reduction or full shutdown before it causes damage. The automated response should be defined by your organization, appropriate for the risk, and designed for minimal operational impact.

Pro-tip

Claude Code supports this by providing [command injection detection (opens in new tab)](https://code.claude.com/docs/en/security#protect-against-prompt-injection) that flags suspicious commands even when they match allowlisted patterns, [fail-closed matching (opens in new tab)](https://code.claude.com/docs/en/security#protect-against-prompt-injection) that defaults unrecognized commands to requiring manual approval, and [context-aware analysis (opens in new tab)](https://code.claude.com/docs/en/security#core-protections) that detects potentially harmful instructions by analyzing the full request.

## Input validation and output controls

Monitoring and response catch threats after they emerge. Prevention stops them before they start. Input validation blocks manipulation attempts at the boundary, rejecting malicious instructions before agents process them. Output controls constrain what agents can produce, limiting data leakage and harmful actions, even when attackers succeed in compromising agent behavior.

### Input sanitization

Agents cannot reliably distinguish between legitimate instructions and malicious payloads embedded in user input. Input validation provides an external filter, rejecting suspicious content before agents process it.

Input sanitization capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Basic input validation and length limits | Validate input formats against expected schemas. Enforce maximum lengths. Reject obviously malformed inputs. |
| Enterprise | Content filtering with known attack pattern detection | Deploy pattern matching for known injection techniques. Filter encoded payloads. Block inputs containing suspicious instruction patterns. |
| Advanced | Multi-layer validation with constitutional classifiers and spotlighting | Implement multiple detection methods in sequence. Use AI-based classifiers trained on adversarial examples. Apply spotlighting techniques that clearly delimit untrusted content. |

Input sanitization does not translate directly from traditional technologies to agents. SQL injection has well-defined patterns and constrained input fields, but agent inputs are freeform and unpredictable, making simple enforcement rules insufficient.

You can still define expected schemas, enforce maximum lengths, and reject known bad patterns before they reach the agent. At the Enterprise level, pattern matching for known threats and payload filtering before the data is passed to the agent will catch more sophisticated injection techniques. The Advanced tier adds [spotlighting (opens in new tab)](https://arxiv.org/pdf/2403.14720), a technique that uses the known schema established earlier to help the LLM distinguish between system instructions and user input, treating the latter as less trustworthy.

If you are developing your own models, mitigation techniques like constitutional classifiers can also be applied during training to develop specifically trained LLM guards that monitor both input and output. You can read more about our research, and the effectiveness of constitutional classifiers, at our [website (opens in new tab)](https://www.anthropic.com/research/constitutional-classifiers).

Pro-tip

Claude Code supports this by providing [input sanitization (opens in new tab)](https://code.claude.com/docs/en/security#core-protections) that prevents command injection, a [command blocklist (opens in new tab)](https://code.claude.com/docs/en/security#core-protections) that blocks risky commands like curl and wget by default, [isolated context windows (opens in new tab)](https://code.claude.com/docs/en/security#additional-safeguards) that process web content in a separate context to prevent prompt injection, and [network request approval (opens in new tab)](https://code.claude.com/docs/en/security#additional-safeguards) that gates all outbound connections.

### Output filtering

Output filtering prevents agents from leaking sensitive data or producing harmful content. Even well-secured agents can be manipulated into generating outputs that can potentially expose credentials, reveal confidential information, or enable social engineering attacks.

Output filtering capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Output filtering for sensitive data patterns | Scan outputs for patterns matching PII, credentials, and sensitive business data. Block or redact detected sensitive content. Log filtering events. |
| Enterprise | Semantic analysis of outputs before delivery | Analyze output meaning rather than just pattern matching. Detect attempts to encode sensitive data. Identify outputs that might enable social engineering. |
| Advanced | Human-in-the-loop approval for high-risk actions | Require human review before executing actions with significant consequences. Present clear descriptions of intended actions. Log approval decisions for audit. |

The techniques from input sanitization apply to output filtering as well, but the objectives differ. Input sanitization protects agents from malicious actors, while output filtering is typically used to prevent data loss. The advantage at this stage is that you know the data you own and process, putting you in the best position to develop patterns that match it. Human-in-the-loop review is valuable at any tier and absolutely necessary for high-risk actions.

## Integrity and recovery

Prevention and detection assume agents operate correctly. When compromise occurs despite these controls, you need verified configurations and rapid recovery. Attackers who cannot manipulate inputs directly target agent configurations instead, modifying behavior at the source. Integrity protections ensure configurations remain trustworthy. Recovery capabilities restore known-good states when attacks succeed.

### Configuration integrity

Configuration files control agent behavior, making them attractive targets. Attackers who gain file system access can modify configurations to disable security controls, grant excessive permissions, or alter agent instructions. Integrity protections detect and prevent unauthorized configuration changes.

Configuration integrity capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Version-controlled agent configurations | Store configurations in version control systems. Require review for configuration changes. Maintain history of all changes. |
| Enterprise | Signed configurations with deployment verification | Cryptographically sign approved configurations. Verify signatures before deployment. Reject unsigned or invalidly signed configurations. |
| Advanced | Immutable infrastructure with attestation | Deploy agents as immutable images. Verify image integrity through attestation before execution. Replace rather than modify running agents. |

Configuration integrity is one of the more straightforward controls to implement because most organizations already have the building blocks in place. Version control, code review, and CI/CD pipelines apply to agent configurations the same way they apply to application code. The key is treating agent configurations with the same rigor, since a modified configuration can be just as damaging as a code vulnerability, but is often easier to exploit.

At the infrastructure layer, the same rigor argues for a different reflex: enable automatic updates on any component where the risk of an automated update causing an outage is acceptable. Manual approval steps add delay, and delay is now the primary risk. Treat "auto-update on" and "verify signatures before deployment" as complementary, not contradictory — signed updates from a trusted supplier should flow through automatically; unsigned changes should be rejected outright.

### Recovery capabilities

When compromise occurs, speed determines damage. Recovery capabilities enable rapid restoration to known-good states, minimizing the window where compromised agents operate and limiting blast radius.

Recovery capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Documented rollback procedures | Document steps to restore previous agent versions. Test rollback procedures periodically. Maintain previous versions for rapid restoration. |
| Enterprise | Automated rollback with health checks | Implement automated deployment that verifies agent health. Roll back automatically when health checks fail. Maintain deployment history, enabling rapid reversion. |
| Advanced | Self-healing systems with automatic remediation | Deploy agents with automatic restart on failure. Implement circuit breakers that isolate failing components. Automatically provision replacement agents when recovery fails. |

Documented rollback procedures provide a starting point, but untested procedures fail when you need them most. Automating rollback with health checks removes human reaction time from the equation, catching compromised or failing agents before operators even notice. At the Advanced tier, self-healing systems take this further by removing the need for intervention entirely, but the fundamentals still matter. If you cannot reliably roll back to a known-good state, no amount of automation will save you.

Pro-tip

Claude Code supports this by providing [version-controlled settings (opens in new tab)](https://code.claude.com/docs/en/settings) where permission configurations and MCP server allowlists are checked into source control for review and rollback, [managed settings (opens in new tab)](https://code.claude.com/docs/en/permissions#managed-settings) that enforce organization-wide policies users cannot override, and [isolated cloud VMs (opens in new tab)](https://code.claude.com/docs/en/security#cloud-execution-security) with automatic cleanup that implement immutable execution environments.

## AI governance policies

Technical controls enforce security. Governance policies determine when and how your organization uses AI. Many organizations discover during incidents that existing policies provide inadequate guidance for agentic systems.

AI governance policy capabilities by tier

| Tier | Capability | Implementation |
| --- | --- | --- |
| Foundation | Documented acceptable use and incident response policies | Define acceptable AI use cases and prohibited activities. Establish incident response procedures that address agent compromise. Document who approves agent deployments. Address Shadow AI where employees use LLMs without IT approval. |
| Enterprise | Formal governance framework with stakeholder oversight | Establish a cross-functional AI governance committee including security, legal, compliance, and business stakeholders. Implement approval processes for new agent deployments. Create risk assessment procedures specific to agentic systems. Conduct regular policy reviews. |
| Advanced | Continuous policy enforcement with automated compliance checking | Integrate policy checks into deployment pipelines. Implement automated detection of policy violations. Establish metrics for policy compliance and effectiveness. Maintain audit trails of governance decisions. Update policies based on incident learnings. |

Technical controls only enforce what governance defines. Without clear policies, teams make inconsistent decisions about what agents can do, what data they can access, and who is accountable when something goes wrong. Shadow AI is a particular risk at this stage, where employees adopt LLM tools without IT awareness, bypassing every control in this framework. Starting with documented policies and incident response procedures gives your organization a baseline to build on. As governance matures, the goal is to move policy enforcement from periodic reviews into automated checks embedded directly in your deployment pipelines.

Pro-tip

Claude Code addresses policy management by providing [managed settings (opens in new tab)](https://code.claude.com/docs/en/permissions#managed-settings) that let administrators enforce security policies organization-wide, [managed-only restrictions (opens in new tab)](https://code.claude.com/docs/en/permissions#managed-only-settings) like allowManagedPermissionRulesOnly that prevent users from defining their own permission rules, and [server-managed settings (opens in new tab)](https://code.claude.com/docs/en/settings) that deliver centralized configuration through MDM or OS-level policies.
