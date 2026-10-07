<!-- source: https://claude.com/resources/guides/zero-trust-for-ai-agents/agent-implementation-workflow -->

Chapter 0622 min read

# Agent implementation workflow

22 min read

31 min remaining

Successful agent implementation requires a defined, repeatable process built on the security architecture above. Each phase addresses specific security controls while mitigating the identified threats.

## Phase 1: Identify requirements

Define what regulatory requirements you need to meet, what operational goals you're trying to accomplish, and what constraints you're working within. Get security, legal, compliance, and business stakeholders aligned before you build.

## Phase 2: Manage supply chain risks

Supply chain integrity is a challenge across all forms of IT. When devices, services, and applications can be tampered with between source and consumer, threats can be introduced at any time. To mitigate this, component integrity must be verified and validated to be tamper-free.

### AI Bill of Material (AI-BOM)

The AI-BOM concept extends software composition analysis to AI components, tracking model provenance, training dataset lineage, and fine-tuning parameters. OWASP's AI-BOM extends their CycloneDX ML-BOM and is available as a [web tool (opens in new tab)](https://genai.owasp.org/resource/owasp-aibom-generator/). Integrate an AI-BOM into existing supply chain security processes, treating model components with the same rigor applied to code dependencies.

If you're not running local LLMs, consider where you are getting your services. Anthropic was one of the first AI companies to achieve the [ISO 42001 (opens in new tab)](https://www.anthropic.com/news/anthropic-achieves-iso-42001-certification-for-responsible-ai) certification for responsible AI.

### Evaluate dependency health automatically

Most software supply chains are mostly open source, and most open-source projects have no service-level agreement. [OpenSSF Scorecard (opens in new tab)](https://securityscorecards.dev/) automatically scores every dependency on signals like branch protection, fuzzing coverage, signed releases, and maintainer activity. It runs in CI and helps identify unmaintained packages. Wire it in alongside your AI-BOM so model components and code dependencies carry the same risk signals.

### Audit your dependency tree for redundancy

Most large codebases accumulate multiple libraries doing the same job (several HTTP clients, several JSON parsers), each adding attack surface for no functional gain. Point a frontier model at your lockfile and ask which dependencies overlap and what migration would look like — this is typically a one-hour exercise that surfaces consolidation worth doing.

### Narrow remediation with reachability analysis

Evaluate the reachability of vulnerable code so you remediate the smallest set that actually matters. Combine this with continuous delivery pipelines that run regression tests on updates, so you can deploy patches quickly with confidence you haven't broken anything.

### AI vendoring for small unmaintained dependencies

For small dependencies that score poorly on Scorecards and are not actively maintained, having a frontier model reimplement the subset of functionality you actually use is often safer than continuing to depend on them. Treat this as a standard response to an unhealthy dependency, not an exotic workaround.

### Cryptographic signing

Sign models and software at every stage through production deployment. Signatures verified only at deployment might not catch subsequent tampering. Runtime verification confirms ongoing integrity.

### Vendor assessments

Review security practices of tool providers before adoption. Assess update mechanisms for supply chain risk and consider provider incident history and vulnerability response capabilities. Validate components at runtime to detect post-deployment tampering. Your third-party risk management process should explicitly ask suppliers how they are preparing for AI-accelerated exploit timelines and whether they are scanning their own code.

This includes free and open source software (FOSS). Download the software, assess the code directly, and evaluate the provider. Does the provider have a large community, do they have a long history of support, etc.? While this doesn't mean that another submitter couldn't insert malware, it would indicate that the original author isn't directly an adversarial actor.

Pro-tip

Run/host the MCP server yourself, on an immutable platform, after you have verified the code. Cryptographically sign it yourself, and perform the same actions on updates before introducing them to production.

## Phase 3: Define agent boundaries

Define exactly what each agent is allowed to do, when it should escalate to a human for approval, and the resulting blast radius should anything go wrong.

### Assign a unique identity

Every agent instance needs a unique, cryptographically rooted identifier that persists across its actions. Without a distinct identity, correlating logs during an incident becomes guesswork. You can't determine which agent accessed a resource, triggered an error, or made a specific decision. Unique identifiers enable the traceability discussed earlier, allowing you to filter audit logs by agent, reconstruct action sequences, and attribute outcomes to specific instances when investigating anomalies or breaches.

Pro-tip

Claude Code assigns a unique `session.id` to each session, with `user.account_uuid` and `organization.id` attribution on all telemetry events, enabling precise incident investigation without shared identity ambiguity.

### Approved/prohibited actions

Document what actions are permitted or denied. Rather than leaving this implicit, write it down. An agent permitted to read customer records, summarize information, and draft responses has clear boundaries. An agent with vague permission to "help with customer service" does not.

You need to be able to implement this at a granular enforcement level. It's one thing to tell an agent "Don't do this", it's another to prohibit that action through permissions.

Pro-tip

Claude Code natively supports this level of granular access control in [settings.json (opens in new tab)](https://code.claude.com/docs/en/settings), which can be configured with global and project-level settings, and environment variables.

### Escalation triggers

Escalation triggers identify what requires human review before proceeding. High-value transactions, access to sensitive data categories, or communications with external parties might all require approval. Define thresholds that balance security against operational efficiency.

Claude Code natively supports this with both [settings.json (opens in new tab)](https://code.claude.com/docs/en/settings), via the "ask" parameter, as well as [hooks (opens in new tab)](https://claude.com/resources/articles/how-to-configure-hooks).

### Scope limits / Least Agency

Scope limits constrain which systems, data, and resources the agent can access. Even within permitted actions, agents should access only the systems necessary for their function. A customer service agent doesn't need access to HR systems, even if the underlying service account technically permits it.

The best way to tackle this is to limit the access of accounts provided to agents. For example, if you are providing access to a database system via API using certificate-based authentication you would limit the access to read, unless the agent needed write access, and the read access would be limited to only the data necessary to perform its duties. Simply put, Least Agency and deny by default, at all times. If the agent were compromised or the credentials stolen, the blast radius would be severely limited.

Pro-tip

Sometimes you may just want to break up some of the functions/goals of an agent into multiple agents. This compartmentalization of capabilities and access to resources means that attackers are required to compromise more agents in order to gain access to more system resources.

Very important: each agent should have a unique ID and its own access credentials. If you break it into multiple agents and provide them all the same credentials, you have failed to compartmentalize the risk.

### Identify the blast radius

With the approved actions, prohibited actions, escalation triggers, and scope limits in place, identify the effective blast radius. What could go wrong if the agent or system were compromised?

Apply the "impossible vs. tedious" test here. If your containment plan relies on friction — the attacker would have to make a lot of requests, or would have to bypass several rate limits — assume it will fail. If the current risk level is still unacceptable, adjust the previous settings to further restrict what the agent is capable of doing.

## Phase 4: Defend against prompt injection

Just as it's necessary to implement input sanitization on traditional technologies like databases, we need to ensure that we control and clean information that is presented to our agents. Defenses must address both direct attacks through user input and indirect attacks through external data sources.

In addition to escalation triggers and scope limitations, input isolation, constitutional classifiers, and limiting attack surfaces greatly reduce the risks of prompt injections.

### Input isolation

Input isolation treats all natural-language inputs as untrusted. User-provided text, uploaded documents, and retrieved content pass through validation before influencing agent behavior. Microsoft's Spotlighting technique reduces indirect injection attack success from over [50% to under 2% (opens in new tab)](https://arxiv.org/pdf/2403.14720) by clearly delimiting untrusted content.

### Constitutional classifiers

Constitutional classifiers provide an additional detection layer. These AI-based systems scan prompts and responses for manipulation attempts. Anthropic's approach [blocked 95% of jailbreak attempts (opens in new tab)](https://www.anthropic.com/research/constitutional-classifiers) in testing with minimal increase in over-refusal rates.

### Limit attack surfaces

While a traditional security technique, reducing the attack surface is one of the most effective ways to mitigate prompt injection. Limit who or what can interact with the agentic system. If the system can be limited to trusted personnel and resources, the ability for a malicious actor to hijack your system will be severely limited.

## Phase 5: Secure tool access

Tool access is one of the highest-risk surfaces in agentic deployments. When tool capabilities lack proper controls, a single compromised agent can cause widespread damage.

### Tool allow-listing

Tool allow-listing restricts agents to approved tools. Rather than permitting any tool that becomes available, maintain explicit lists of permitted tools per agent function. Further, using our deny-by-default approach, reject invocations of unlisted tools.

This will take different forms depending on the agentic framework you are using — some require you to explicitly provide them to the agent in the first place, others will have them as a resource pool. Regardless of the method, you want to control this on two fronts. The first will be directly at the agent level, with implicit allow/deny permissions. The second will be outside the agent level, in case the agent or the agent environment is compromised. The easiest way to do this is to require authentication for tools: certificate-based authentication on an API interface, or short-lived tokens bound to the calling agent's identity. Static API keys are not acceptable for tool authentication, even at Foundation.

Pro-tip

Claude Code supports explicit tool based permission control at the agent level via [settings.json (opens in new tab)](https://code.claude.com/docs/en/settings), which can be configured with global and project-level settings, and environment variables.

### Capability restrictions

Limit what permitted tools can do. An email tool might be restricted to reading, with send capability requiring separate authorization. A database tool might permit queries but prohibit schema changes. In larger enterprise services, such as Active Directory, this typically takes the form of role-based access controls (RBAC) on the provisioned account.

### Parameter validation

Validate tool call arguments before execution. Input validation applies to tool parameters just as it does to user input. Reject parameters that exceed expected ranges or contain suspicious content.

Parameter validation can, and should, happen on both the agent side and the tool side.

Pro-tip

Claude Code natively supports this capability on the agent side through [hooks (opens in new tab)](https://claude.com/resources/articles/how-to-configure-hooks). Using a `PreToolUse` hook, you can create a hook to validate the parameters before they are sent.

### Sandbox execution

Sandboxed execution provides containment when tools behave unexpectedly. Container sandboxes and/or microVMs with restricted network access, limited file system mounts, and syscall filtering contain the impact of compromised tools.

Another consideration is rate limiting and spending controls to prevent resource exhaustion attacks. Where possible, implement circuit breakers that halt tool execution when usage exceeds defined thresholds, or if you have implemented Attribute-based Access Control (ABAC), where usage behavior deviates from approved baselines. Remember that rate limits are friction, not barriers: they buy time but do not stop a determined agentic attacker.

Pro-tip

Claude Code now supports [sandboxing (opens in new tab)](https://www.anthropic.com/engineering/claude-code-sandboxing), with file system isolation, network isolation, and OS-level enforcement. You can delve deeper in the official [documentation (opens in new tab)](https://code.claude.com/docs/en/sandboxing).

### Approval escalation

Just like the escalation triggers discussed earlier, we apply the same controls to high-risk tool invocations, requiring them to pause for human review. Ensure you display clear descriptions of intended actions and log approval decisions. For later explainability and justification, you need to perform forensics.

Pro-tip

Claude Code supports this natively — by default all tool calls require human approval, and further granularity can be configured via [settings.json (opens in new tab)](https://code.claude.com/docs/en/settings). In addition, pre- and post-tool calling actions can be configured using [hooks (opens in new tab)](https://claude.com/resources/articles/how-to-configure-hooks).

## Phase 6: Protect agent credentials

Credential protection prevents attackers from stealing or misusing agent authentication material. When agents share credentials or operate under generic service accounts, a single compromised credential grants attackers access to every system those agents can reach. A distinct identity for each agent, backed by cryptographic authentication and hardware-rooted wherever possible, contains the blast radius of credential theft while enabling granular access control and accurate audit trails.

Static API keys, embedded credentials, and shared service-account passwords are among the first things an attacker with model-assisted code analysis will find. Treat them as already-compromised.

### Short-lived, identity-provider-issued credentials as baseline

Short-lived credentials limit the window of opportunity for credential theft. Tokens that expire in minutes rather than days reduce the value of stolen credentials. Automated refresh maintains operational continuity without long-lived secrets.

Where resources permit, implement certificate-based identity with a Certificate Authority that enrolls agents, issues short-lived certificates, and maintains Certificate Revocation Lists or OCSP responders for real-time validation. For organizations without PKI expertise, cloud-native managed identity services and secret management platforms like HashiCorp Vault provide automated credential rotation and centralized revocation without the operational overhead of running a certificate authority.

Pro-tip

Claude Code natively supports [OAuth 2.0 authentication (opens in new tab)](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers) with automatic token refresh for MCP server connections, avoiding long-lived secrets. Additionally, permissions granted during a session for tools configured as "ask" are [session-scoped (opens in new tab)](https://code.claude.com/docs/en/iam#access-control-and-permissions) and expire when the session ends.

### Hardware-bound credentials for production and sensitive workloads

For production systems and sensitive internal tools, credentials should be bound to attested hardware so that stolen credential material cannot be exported from a compromised host. This applies to calls between production services as well as to human-to-service calls. Phishing-resistant 2FA (FIDO2 or passkeys) should be the default wherever human authentication is in the loop; SMS-based codes do not meet the Foundation bar.

### Credential isolation

Credential isolation ensures each agent instance has unique credentials. When agents share credentials, a single theft grants attackers the combined access of every agent using that secret, and revoking that credential disrupts all of them. Per-agent credentials contain this blast radius while enabling granular access control and accurate incident investigation. Credentials should never appear in code or configuration files; inject them at runtime from secrets management systems that log access and support emergency revocation.

Pro-tip

Claude Code stores API credentials in the OS credential store rather than configuration files. The `apiKeyHelper` setting can execute a script at runtime to retrieve secrets from external vaults, supporting integration with secrets management systems.

### Explicit trust boundaries

Multi-agent systems require explicit trust boundaries. Agents should verify the identity and authorization of other agents before accepting delegated tasks. Implement authorization checks at each step of multi-agent workflows, rather than trusting that the initiating agent had appropriate permissions. Where possible, log all inter-agent communications and flag unusual delegation patterns for review.

Pro-tip

Claude Code spawns ephemeral sub-agents by design, which act like an extension of the original agent and can have up to the same permissions levels as it has been originally assigned. From an external observability and access standpoint, essentially there is no difference between the original agent and its sub-agents. However, the distinction is captured by Claude Code, and would be visible via OpenTelemetry or in the JSONL transcripts located in the Claude Code projects folder.

### Just-in-time (JIT) access

Just-in-time access grants permissions only when needed and revokes them immediately after use. Rather than maintaining standing access, agents request credentials for specific operations, scoped to specific resources for defined durations. This approach limits exposure even if agent infrastructure is compromised: an attacker finds no cached credentials to steal. Token lifetimes should be measured in minutes rather than hours or days.

Pro-tip

JIT access is very powerful, and not easily implemented. If you can implement it within your environment, even partially, you should do so. This is considered an advanced Zero Trust implementation and a very strong threat mitigation.

### Attribute-based Access Control (ABAC)

Attribute-based access control (ABAC) evaluates multiple factors before granting access, such as: agent identity, resource sensitivity, requested action, time of day, source location, and current risk score. This context-aware approach enables policies like allowing read access to low-sensitivity data while requiring step-up authentication for sensitive records, or permitting routine queries while blocking bulk exports. ABAC policies adapt to circumstances without requiring new roles for every access pattern.

Pro-tip

ABAC, like JIT, is another advanced implementation. The factors used for evaluation, and what is appropriate for each agent in its particular use case, are determined by you. When properly configured, detection and prevention of misuse is immediate.

## Phase 7: Safeguard agent memory

Memory protection prevents attackers from corrupting agent context or extracting sensitive information from memory stores. Unlike attacks targeting a single session, memory poisoning persists across interactions, influencing agent behavior long after the initial compromise. Effective protection requires isolation between users and sessions, integrity verification of stored content, and policies governing how long sensitive context persists.

### Memory isolation

Memory isolation enforces strict boundaries between sessions and users. Without these boundaries, poisoned context from one conversation can influence future interactions, and a compromised session can access data from previous ones. Session isolation ensures that information from one conversation cannot affect another, limiting the persistence of any successful poisoning attempt.

Pro-tip

Claude Code enforces session isolation by default. Each session starts with fresh context, and sub-agents operate in their own isolated context windows without access to the parent conversation history.

### Context integrity validation

Integrity checking validates persisted context before use. Cryptographic hashes detect unauthorized modification, while source attribution tracks where each memory element originated. Together, these enable organizations to identify tampering and quarantine memories derived from untrusted sources.

Implement integrity validation at every retrieval, not just at storage time. Tag each memory element with its source and the conditions under which it was added. Store hashes in tamper-resistant logs separate from the memory content itself. When validation fails, reject the suspect context and alert security teams rather than allowing potentially poisoned memories to proceed.

### Context retention policies

Retention policies limit how long sensitive context persists. By applying time-to-live values and automatically expiring unverified memory, you'll prevent poisoned content from remaining active indefinitely. Shorter retention periods for high-risk context such as external inputs or unverified tool outputs reduce exposure without disrupting core operational data.

When poisoning is detected, recovery depends on preparation. Versioned memory stores enable rollback to known-good states, while quarantine procedures isolate suspected content for forensic analysis before deletion. Test rollback procedures before incidents occur, and define clear criteria for when full memory purging is warranted versus targeted remediation.

Pro-tip

Claude Code supports configurable retention policies. The `cleanupPeriodDays` setting controls how long local transcripts persist before automatic deletion.

Additionally, checkpoints capture the state before each edit, enabling rollback to known-good states via the rewind feature (Esc+Esc or /rewind). You can restore code changes, conversation state, or both independently. For enterprise deployments, server-side retention defaults to 30 days. More information can be found at [data usage (opens in new tab)](https://code.claude.com/docs/en/data-usage) and [checkpointing (opens in new tab)](https://code.claude.com/docs/en/checkpointing).

## Phase 8: Measure what matters

When agentic systems operate as black boxes, you cannot determine whether they are delivering intended outcomes or have been compromised and are serving attacker objectives. Visibility is critical — not just seeing what agents do, but understanding why, and receiving that information quickly enough to act. These factors determine whether teams catch divergent behavior early or face catastrophic failure.

### Dwell time and coverage

Instrument dwell time (anomaly occurrence to human awareness) and coverage (fraction of alerts investigated) before anything else. These are the two metrics AI automation has the greatest leverage to move, and they matter most when exploit windows shorten.

### Explainability

Decision explainability asks whether you can trace any agent action back to its triggering input and explain why the agent chose that response. For regulated industries handling financial, health, or personal data, this explainability is not optional. It enables compliance demonstration, incident investigation, and customer trust.

Security teams should be able to answer: would we know within an hour if an agent went rogue? Can the team take time off without worrying about undetected agent misbehavior? If the answers are uncertain, the foundational controls need more work.

### Behavior

Behavioral conformance tracks whether agent actions align with intended policies and expected patterns. Establish behavioral baselines during controlled deployment and measure drift over time. Key indicators include tool usage patterns, output characteristics, and decision distributions. An agent that suddenly favors different tools or produces outputs with changed characteristics warrants investigation, even if no single action triggers an alert.

Define acceptable variance thresholds and flag deviations for review. Continuous behavioral monitoring catches subtle compromises that evade rule-based detection, such as gradual drift from memory poisoning or slow-acting supply chain attacks.

### Detection speed

Detection speed measures how quickly your team becomes aware when an agent behaves unexpectedly. The difference between minutes and days translates directly to damage contained. Target detection within an hour for critical systems. Measure from anomaly occurrence to human awareness.
