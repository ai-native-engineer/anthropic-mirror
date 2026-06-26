<!-- source: https://claude.com/plugins/jfrog -->

# JFrog

Official JFrog plugin. Connect Claude Code to JFrog to manage, secure and govern your software supply chain. Give agents the context to build secure, compliant software.

* Install in

  [Claude Code](#)

  [JFrog](https://jfrog.com/)
* Installs

  182

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Connect Claude Code to your JFrog Platform to simplify platform administration and bring DevSecOps context directly into agents' development process. This plugin makes it easy for agents to consume artifacts through Artifactory, where they are scanned, verified, and governed by your organization's security and compliance policies.

It also ensures that the MCP tools the agent uses are controlled through the JFrog AI Catalog, enforcing centralized allow and block policies across all agent activity. This gives you a single point of control over both the artifacts flowing through your pipelines and the tools your agent is allowed to use.

Key capabilities include vulnerability scanning, provenance verification, and curation checks on artifacts; governance of MCP tools and AI assets; visibility into build and artifact metadata; and project administration tasks such as repository creation and permission management. The plugin integrates JFrog Platform Skills and MCP tools with simple authentication, while providing reliable, native access to the entire JFrog Platform.

**How to use:** Once installed and authenticated, interact with Claude Code in natural language as usual. Relevant requests are routed through JFrog for action. Try prompts like:

* "Is it safe to upgrade to package-name version X.Y.Z?"
* "Show me curation audit events from the last 7 days"
* "Which build produced artifact-name in repo-name?"
* "Which MCP am I allowed to install?"
* "Provision a new project and create a local NPM repository for it."

You can also orchestrate multi-step workflows, such as:

* "Show me available repositories, download package-name from repo-name, and check it for vulnerabilities."

**Install in Claude Code:** `claude plugin install jfrog@claude-plugins-official`  
**Made by:** [JFrog](https://jfrog.com/)

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

948012

installs](/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

855112

installs](/plugins/superpowers)

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

383892

installs](/plugins/code-review)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

377529

installs](/plugins/context7)
