<!-- source: https://claude.com/plugins/claude-security -->

# Claude Security

Vulnerability scanning and patch generation with researcher agents and adversarial validation

* Anthropic Verified

  [Anthropic](https://anthropic.com)

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
