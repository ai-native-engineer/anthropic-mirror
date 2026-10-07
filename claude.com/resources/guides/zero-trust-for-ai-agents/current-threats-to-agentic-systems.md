<!-- source: https://claude.com/resources/guides/zero-trust-for-ai-agents/current-threats-to-agentic-systems -->

Chapter 049 min read

# Current threats to agentic systems

9 min read

59 min remaining

Agentic systems face a distinct threat landscape. Current threats identified by [OWASP (opens in new tab)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) include prompt injection, tool and resource hijacking, identity and access privilege abuses, memory and context poisoning, and supply chain risks.

## Prompt injection and instruction manipulation

Prompt injection occurs when an external attacker inserts malicious instructions that cause an agent to follow attacker commands. It takes two forms: direct injection through user input and indirect injection through external sources.

[Direct prompt injection (opens in new tab)](https://atlas.mitre.org/techniques/AML.T0051.000) occurs when attackers craft inputs that override system instructions. Techniques include explicit instruction overrides, encoding schemes like Base64 or hexadecimal to bypass filters, and adversarial suffixes that appear meaningless to humans but influence model outputs. Research shows algorithmic approaches can [achieve 100% attack success rates (opens in new tab)](https://arxiv.org/abs/2307.15043) with prompts that transfer across multiple model families.

[Indirect prompt injection (opens in new tab)](https://atlas.mitre.org/techniques/AML.T0051.001) presents the more insidious threat. Attackers embed malicious instructions in external data sources that agents process, such as web pages or emails. Microsoft Research confirms that [LLMs cannot reliably distinguish between informational context and actionable instructions (opens in new tab)](https://www.microsoft.com/en-us/research/publication/defending-against-indirect-prompt-injection-attacks-with-spotlighting/). The user never sees the malicious payload, and the agent executes it as if it were a legitimate request.

## Tool and resource misuse

Agents with tool access can be manipulated into using those tools maliciously, even within authorized privileges. Traditional access controls can't prevent this attack because the agent operates within its granted permissions.

*Tool poisoning* occurs when attackers compromise tool interfaces such as MCP tool descriptors, schemas, or metadata. The agent invokes a tool based on falsified capabilities, leading to unintended actions. A malicious tool can [hide commands in its metadata (opens in new tab)](https://invariantlabs.ai/blog/mcp-github-vulnerability) that exfiltrate data without user knowledge. In rug pull attacks, a legitimate tool is secretly replaced with a malicious version. The [first documented in-the-wild malicious MCP server (opens in new tab)](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft) impersonated a legitimate email service and secretly copied all sent emails.

*Tool chaining* attacks present a more subtle threat. [Attackers trick agents (opens in new tab)](https://www.crowdstrike.com/en-us/blog/how-agentic-tool-chain-attacks-threaten-ai-agent-security/) into combining legitimate tools in harmful sequences: chaining a secure internal CRM tool with an external email tool to exfiltrate customer data that neither tool would expose alone. Because every command executes through trusted binaries under valid credentials, host-centric monitoring sees no malware and the misuse goes undetected.

*Resource exhaustion* attacks exploit the automated nature of agent operations. Loop amplification causes agents to repeatedly call costly APIs, generating denial-of-service conditions or billing spikes.

## Identity and privilege abuse

Agents often operate with elevated privileges or service accounts, and traditional identity systems designed for human users struggle to accommodate them. This mismatch creates exploitable security gaps.

### Unscoped privilege inheritance

*Unscoped privilege inheritance* occurs when a high-privilege manager agent delegates tasks without applying least-privilege scoping, passing its full access context to a worker agent that should have limited rights. In multi-agent systems, trust relationships are dynamic and often implicit.

Another example is when a compromised low-privilege agent relays valid-looking instructions to a high-privilege agent, which executes them without verifying the original user's intent. This confused deputy problem is amplified when agents routinely coordinate and delegate.

### Memory-based privilege retention

*Memory-based privilege retention* happens when agents cache credentials or keys for context reuse without proper memory segmentation. Without that segmentation, an attacker can prompt the agent to perform actions that the attacker's own credentials would never allow. The agent pulls cached secrets from a prior secure session and executes the request, effectively escalating privileges across session boundaries.

## Supply chain and dependency risks

Unlike static software supply chains, agentic ecosystems often compose capabilities at runtime, loading external tools and agent personas dynamically. This expands the attack surface beyond what traditional software composition analysis can handle — and frontier models are very effective at recognizing the signatures of known, already-patched vulnerabilities in unpatched upstream components.

### Model supply chain risks

*Model supply chain risks* include poisoned weights and compromised fine-tuning data that introduce backdoors that persist through deployment. Anthropic research demonstrates that injecting just 250 malicious documents can successfully [backdoor LLMs ranging from 600 million to 13 billion parameters (opens in new tab)](https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training), and these backdoors persist through safety training including supervised fine-tuning and RLHF.

### Tool and framework supply chain risks

*Tool supply chain risks* affect MCP servers, API integrations, and agent frameworks. The [PyTorch dependency confusion attack (opens in new tab)](https://www.bleepingcomputer.com/news/security/pytorch-discloses-malicious-dependency-chain-compromise-over-holidays/) demonstrated how malicious packages can exfiltrate sensitive data, including SSH keys during installation. Security researchers have [discovered approximately 100 malicious AI models on major platforms (opens in new tab)](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/), including models that initiate reverse shell connections when loaded.

Beyond deliberate attacks, most software supply chains are mostly open source, and most open-source projects have no service-level agreement. Evaluate the security health of every dependency your agent infrastructure loads: [OpenSSF Scorecard (opens in new tab)](https://securityscorecards.dev/) automatically scores each dependency on signals like branch protection, fuzzing coverage, signed releases, and maintainer activity, runs in CI, and helps identify unmaintained packages. Apply the same expectations to your vendors — your third-party risk management process should ask suppliers how they are preparing for accelerated exploit timelines and whether they are scanning their own code.

Most large codebases also accumulate multiple libraries doing the same job (several HTTP clients, several JSON parsers), each adding an attack surface for no functional gain. A one-hour dependency-tree audit — pointing a frontier model at your lockfile and asking which dependencies overlap and what migration would look like — often surfaces consolidation worth doing.

## Memory and context poisoning

Agents that persist context across sessions can have that memory corrupted, causing future reasoning to become biased, unsafe, or actively aiding data exfiltration. [Malicious instructions implanted in assistant memory (opens in new tab)](https://labs.zenity.io/p/agentflayer-chatgpt-connectors-0click-attack-5b41) can compromise current and all future sessions. The agent continues serving attacker goals long after the initial injection.

### RAG poisoning

*RAG poisoning* introduces malicious data into vector databases through poisoned sources, direct uploads, or over-trusted pipelines. The agent retrieves this contaminated context when answering queries, [producing false answers or executing targeted payloads (opens in new tab)](https://arxiv.org/abs/2407.12784).

### Shared context poisoning

*Shared context poisoning* exploits reused or shared contexts in multi-tenant environments. Attackers inject data through normal interactions that influence later sessions. A new user session may inherit poisoned context, leading to misinformation, unsafe code execution, or incorrect tool actions. Long-term memory drift is subtler: summaries or peer-agent feedback gradually shift stored knowledge or goal weighting, producing behavioral deviations over time that are difficult to detect because no single change appears malicious.

Chasing individual threats keeps you reactive. The next section shows how Zero Trust principles provide a more durable foundation.
