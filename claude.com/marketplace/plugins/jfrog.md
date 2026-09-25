<!-- source: https://claude.com/marketplace/plugins/jfrog -->

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

## Other plugins

### [Frontend Design](https://claude.com/marketplace/plugins/frontend-design)

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

### [Superpowers](https://claude.com/marketplace/plugins/superpowers)

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

### [Code Review](https://claude.com/marketplace/plugins/code-review)

AI code review with specialized agents and confidence-based filtering for pull requests

### [Context7](https://claude.com/marketplace/plugins/context7)

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

### [Code Simplifier](https://claude.com/marketplace/plugins/code-simplifier)

Code clarity agent: simplifies and refines recently modified code while preserving functionality and consistency.

### [Playwright](https://claude.com/marketplace/plugins/playwright)

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, and automate testing workflows.
