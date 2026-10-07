<!-- source: https://claude.com/resources/guides/claude-science-product-guide/frequently-asked-questions-for-cios-and-it-leaders -->

Chapter 079 min read

# Frequently asked questions for CIOs and IT leaders

9 min read

9 min remaining

*Note: The questions below cover Claude Science primarily, with Claude.ai and Claude Cowork addressed where the answer differs. Custom applications built on the Claude Platform have additional configuration options handled directly with the account team.*

### Where does Claude Science run, and where does our data go?

Claude Science is a local application for macOS and Linux. It runs a daemon on the machine where you install it — a scientist's laptop, a lab Linux box, an HPC login node, or a cloud VM in your tenancy — with its UI in the browser. Files remain on the host and are read in place; content the agent reads as part of an analysis is sent to Anthropic's API as context, subject to your plan's data-use and retention commitments. An OS-level sandbox with deny-by-default network egress controls all other traffic leaving the host. Claude Science is not currently available through Amazon Bedrock, Google Vertex AI, or Microsoft Foundry.

### What does Claude Science install on user endpoints?

A signed binary that runs as a user-space daemon plus a browser-based UI. No kernel-level components. On Linux it can run headless and be reached over an SSH tunnel from the scientist's laptop. Windows is not currently supported.

### How is code execution and file access controlled?

A human-approval broker gates thirteen action kinds, including code execution, network grants, host file access, deletions, MCP tool calls, remote compute dispatch, and skill persistence. Every request surfaces as a single approval card—allow once, for this project, or always—and every decision can be reviewed or revoked from one permission screen. An OS-level sandbox with allowlist-proxy network egress, SSRF and DNS-rebind defenses, and seccomp hardening sits underneath. Plan mode is on by default, so the agent drafts a step-by-step plan and waits for approval before executing.

### How does Claude Science reach our HPC cluster or GPU hosts?

From inside a session the agent can dispatch jobs to an SSH host, a SLURM cluster (batch directives are written automatically), or a serverless GPU account the user supplies. Dispatch targets are gated by the same approval broker, so Research IT can restrict which hosts a group's install is permitted to reach.

### Can Claude Science be used with NIH controlled-access or patient-level data?

Claude Science installs next to the data so files do not have to leave the lab's machines, which is the design that makes it deployable in environments where uploading is not an option. That said, NIH controlled-access datasets (for example, dbGaP) typically require the analysis environment itself to meet NIST SP 800-171 controls, and Claude Science has not yet been assessed against that standard—formal NIH controlled-access data compliance is on the roadmap. Organizations working with controlled-access or patient-level data should pair the local-daemon model with their own data-governance review of the network allowlist and dispatch targets, and with internal policy on which datasets may be analyzed on which hosts. Claude Science is not a validated system; analyses that feed a regulated record go through the organization's existing qualified review.

### Is Claude Science HIPAA-ready?

Not at launch. HIPAA readiness is on the post-launch roadmap. Until then, Claude Science should not be used to process protected health information. Your Anthropic account team can share current timing.

### How is Claude Science priced, and how heavy is usage?

Claude Science draws down from the usage limits of the user's existing Claude plan—Pro, Max, Team, or Enterprise—with no separate license and no free tier. It is token-intensive: scientists routinely run several long agentic analyses in parallel, and heavy users consume at a rate comparable to heavy Claude Code use, so organizations should plan usage limits accordingly and expect heavy individual users to need Max-tier limits. Users can monitor consumption from inside the application under Settings → Usage. A subsidized Team plan is available for academic and nonprofit research labs; contact your Anthropic account team or visit the life sciences solutions page for eligibility.

### What biosecurity controls are in place?

Biosecurity rules ship unconditionally in every agent's system prompt, a per-turn bio trajectory classifier runs in the binary and cannot be disabled by the user or admin, and authentication is OAuth-only with no anonymous or API-key access against the product. Claude Science completed external red-teaming and Anthropic Safeguards review against CBRNE risk before public release. These bio-specific controls sit on top of the OS-level sandbox, deny-by-default network egress, and human-approval broker described above.

### What retention controls are available?

Team and Enterprise plans support custom data retention. Claude Science is a stateful product—sessions, artifacts, and provenance bundles require storage to function — so Zero Data Retention does not apply. ZDR is available on the Claude Platform (API) and Claude Code for approved customers.

### What identity and access controls do you support?

Team and Enterprise plans include SSO via SAML, SCIM for user provisioning, role-based access controls, and admin-managed plugin and skill marketplaces. Claude Science is governed from the same admin console: a Team admin enables it under capabilities settings, and an Enterprise admin scopes it to specific groups via a role with the Claude Science permission before enabling the capability.

### How does Claude Science integrate with our ELN or internal services?

Claude Science is MCP-native. Any MCP server — Benchling, an internal LIMS, a data warehouse, a ticketing system — connects, and skills can wrap internal APIs so the lab's own tools become first-class. Connectors authenticate as the end user and respect entitlements at the project and folder level, so the agent only sees what the scientist already has access to.

### Can Claude Science be used in GxP-regulated workflows?

Claude Science is not a validated system. Organizations typically deploy it in research, analysis, and draft-support roles, with a qualified scientist or reviewer approving every output before it enters a validated record, a regulatory submission, or a publication. The four-layer provenance on every artifact—description, code, conversation, and environment snapshot—gives the reviewer a complete record of how each result was produced. Pair the deployment with your own CSV/CSA assessment of the surrounding process; your Anthropic account team can share how other sponsors and research organizations have approached this.

### Where are Claude.ai and Claude Cowork hosted?

Both are SaaS products hosted by Anthropic. Organizations that need workloads to run inside their own cloud perimeter typically build on the Claude Platform via Amazon Bedrock, Google Vertex AI, or Microsoft Foundry. Cowork is a signed desktop application for macOS and Windows that reads only the local folders the user explicitly grants access to.

### Who are the subprocessors?

A current list of Anthropic subprocessors is published at [trust.anthropic.com (opens in new tab)](http://trust.anthropic.com) and updated as the list changes.

Learn more in our [getting started guide (opens in new tab)](https://claude.com/resources/tutorials/getting-started-with-claude-science).

## Resources

* **[Claude for life sciences solutions page (opens in new tab)](https://claude.com/solutions/life-sciences):** how Claude helps research, clinical, regulatory, and medical affairs teams across the development lifecycle.
* **[Life sciences tutorials on Claude.com (opens in new tab)](https://claude.com/resources/tutorials-category/life-sciences):** step-by-step guides covering literature review, single-cell analysis, protocol drafting, and connector setup.
* **[Claude skills catalog (opens in new tab)](https://skillsmp.com/):** Anthropic's public catalog of community-contributed skills, useful for finding pre-built scientific skills before authoring your own.
* **[The Enterprise AI Guide for Life Sciences (opens in new tab)](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6a39b907335186777dc02c93_Claude-eBook-The-Enterprise-AI-Transformation-Guide-for-Life-Sciences-06172026.pdf):** Anthropic's enterprise transformation guide for life sciences IT and digital leaders.

## Enjoyed the guide?

Take it with you or get in touch with us.

[Download now (opens in new tab)](https://assets.claude.com/b3b5bed92304446a922204a173a864d75a04f2a4.pdf?dl=)[Contact sales](https://claude.com/contact-sales)
