<!-- source: https://claude.com/marketplace/plugins/claude-security -->

The vulnerability detection and patching capabilities behind Claude Security, packaged for Claude Code. Scans run inside your session on your machine, against any repository you can clone.

Scan Codebase maps your repository's architecture, threat-models every component, fans research agents across the code, and verifies what they find. Each finding comes back with a severity, a CWE category, potential impact, reproduction steps, and a suggested path to remediation.

**How it works:** Install the plugin, run /claude-security, and choose an option.

* **Scan Codebase** covers the whole repository, including code you didn't write
* **Scan Changes** points the same analysis at a pull request, a single commit, or the changes on a branch. Research agents still read the whole repository for context rather than the diff alone. Run it in CI, or locally before you commit
* **Suggest Patches** turns confirmed findings into patches, with an adversarial panel reviewing each one. Output is a .patch file that Claude can apply and open a pull request with

In beta. Scans use the Claude access you already have. [Learn more here.](https://code.claude.com/docs/en/claude-security)

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
