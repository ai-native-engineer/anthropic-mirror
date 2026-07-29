<!-- source: https://claude.com/plugins/claude-security -->

# Claude Security

Vulnerability scanning and patch generation with researcher agents and adversarial validation

* Anthropic Verified
* Install in

  [Claude Code](#)
* Made by

  [Anthropic](https://anthropic.com)
* Installs

  899

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

The vulnerability detection and patching capabilities behind Claude Security, packaged for Claude Code. Scans run inside your session on your machine, against any repository you can clone.

Scan Codebase maps your repository's architecture, threat-models every component, fans research agents across the code, and verifies what they find. Each finding comes back with a severity, a CWE category, potential impact, reproduction steps, and a suggested path to remediation.

**How it works:** Install the plugin, run /claude-security, and choose an option.

* **Scan Codebase** covers the whole repository, including code you didn't write
* **Scan Changes** points the same analysis at a pull request, a single commit, or the changes on a branch. Research agents still read the whole repository for context rather than the diff alone. Run it in CI, or locally before you commit
* **Suggest Patches** turns confirmed findings into patches, with an adversarial panel reviewing each one. Output is a .patch file that Claude can apply and open a pull request with

In beta. Scans use the Claude access you already have. [Learn more here.](https://code.claude.com/docs/en/claude-security)

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

1110438

installs](https://claude.com/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

987572

installs](https://claude.com/plugins/superpowers)

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

430450

installs](https://claude.com/plugins/code-review)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

412076

installs](https://claude.com/plugins/context7)
