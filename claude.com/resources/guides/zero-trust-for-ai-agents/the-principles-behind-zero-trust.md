<!-- source: https://claude.com/resources/guides/zero-trust-for-ai-agents/the-principles-behind-zero-trust -->

Chapter 023 min read

# The principles behind Zero Trust

3 min read

66 min remaining

Zero Trust has roots stretching back to 1994, when Stephen Paul Marsh first formalized the concept in his doctoral thesis at the University of Stirling. The idea gained real momentum after high-profile breaches exposed the limits of perimeter-based security, pushing the industry to rethink its foundational assumptions.

That shift produced concrete guidance: NIST published [SP 800-207 Zero Trust Architecture in 2020 (opens in new tab)](https://csrc.nist.gov/pubs/sp/800/207/final), and the National Security Agency (NSA) followed with its [Zero Trust Implementation Guides (ZIGs) (opens in new tab)](https://www.nsa.gov/Press-Room/Cybersecurity-Advisories-Guidance/) in 2026. Together, these frameworks codify a set of principles that redefine how organizations approach security.

Zero Trust replaces perimeter-based security with a simple premise: trust nothing, verify everything, assume breach has already occurred.

Three principles define the framework:

**Never trust and always verify** — Every access request undergoes authentication and authorization regardless of origin. A request from inside the corporate network receives the same scrutiny as one from an external IP address.

**Assume breach** — Design systems while expecting that compromise will occur. Rather than focusing on preventing intrusion, limit the damage an attacker can cause. Segment by identity, implement fine-grained access controls, and ensure that compromising one system doesn't grant access to others.

**Least privilege** — Grant only the minimum access necessary for a specific task. A database administrator doesn't need access to the email server. By constraining what each identity can access, organizations contain the blast radius of any single compromise.

## A design test: impossible, not tedious

When you evaluate any control in this document, ask a single question: *does this make the attack impossible, or just tedious?* Mitigations whose value comes from friction rather than a hard barrier—including extra pivot hops, rate limits, non-standard ports, and SMS-based MFA—degrade significantly against an adversary that can grind through tedious steps at scale. Agentic attackers have unlimited patience and near-zero per-attempt cost.

The controls that survive this test share a pattern: hardware-bound credentials, expiring tokens, cryptographic identity, and network paths that do not exist rather than paths that are merely inconvenient. This test informs every tier recommendation in this document. When in doubt, prefer a control that removes a capability over a control that throttles it.
