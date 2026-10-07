<!-- source: https://claude.com/resources/guides/zero-trust-for-ai-agents/security-considerations-for-autonomous-systems -->

Chapter 034 min read

# Security considerations for autonomous systems

4 min read

63 min remaining

Agentic AI introduces capabilities that existing security models were not designed to address.

## What makes agentic systems different

Traditional software executes predefined logic. Agentic AI systems operate differently. They execute multi-step operations with varying degrees of autonomy. This shift introduces several security considerations, including:

* **Agents execute operations without human initiation or approval at each step.** An agent researching a topic might search the web, synthesize information, and produce a report without human review. This efficiency also means a manipulated agent can cause harm at machine speed.
* **Tool access allows agents to interact with APIs, databases, file systems, and external services.** This includes Model Context Protocol (MCP), which standardizes how agents connect to these resources. A compromised MCP stack can lead to data theft, malicious code execution, and sabotage.
* **Making decisions requires agents to interpret instructions and choose how to accomplish goals.** This introduces ambiguity attackers can exploit. An instruction that seems benign to humans might be interpreted by an agent in ways that enable very different outcomes.
* **Context persistence allows agents to maintain memory across sessions.** Remembering previous interactions, learned preferences, and knowledge makes AI assistants more capable. It also creates new data protection needs.
* **Multi-agent coordination enables agents to communicate with other agents.** These trust relationships let attackers compromise one agent and pivot through others, potentially reaching systems the initial target couldn't access directly.

## Agentic security concepts

Extending cybersecurity to agentic systems requires some new terminology.

### Blast radius

Blast radius measures the potential damage if something goes wrong. An agent with read-only access to a single database has a small blast radius; an agent with administrative access to cloud infrastructure has an enormous one. Security investment should match this exposure, and the "design for breach" posture means assuming at some point, every agent's blast radius will be tested.

### Least agency

[Least agency (opens in new tab)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), a new term coined by [OWASP (opens in new tab)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), extends least privilege to agentic applications. Where least privilege constrains what users and systems can access, least agency goes further, restricting what each agent tool can do, how often, and where. In practice: a database tool gets read-only queries, an email summarizer gets no send/delete rights, an API gets minimal CRUD operations.

## Regulated industries and compliance requirements

Healthcare, finance, government, and other regulated sectors face specific requirements that agentic AI deployments must also address. Zero Trust aligns with and enhances existing regulations. The governing bodies that oversee these compliance regulations will likely adopt Zero Trust and integrate it into existing requirements.

The United States, United Kingdom, and Australian governments have already published Zero Trust guidance, with the US requiring all federal agencies to adopt Zero Trust by 2027.

Government Zero Trust guidance by country

| Country | Office / Guidance |
| --- | --- |
| Australia | homeaffairs.gov.au Guiding principles of Zero Trust |
| United Kingdom | NCSC.gov.uk Introduction to Zero Trust |
| United States | CISA.gov Zero Trust Maturity Model, NSA.gov Zero-Trust Implementation Guides (ZIGs), NIST.gov SP 800-207 |
