<!-- source: https://claude.com/plugins/aikido -->

# Aikido Security

Aikido Security scanning for Claude Code — SAST, secrets, and IaC vulnerability detection by Aikido MCP server.

* Install in

  [Claude Code](#)

  [Aikido Security](https://aikido.dev)
* Installs

  5403

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Aikido Security scanning for Claude Code detects SAST vulnerabilities, exposed secrets, and Infrastructure-as-Code misconfigurations in code you write or modify. Powered by the Aikido MCP server, it scans your files in real time and guides Claude to fix issues before they ship.

The plugin automatically identifies files generated or changed during your session, runs a full security scan (up to 50 files per request), and when vulnerabilities are found, applies remediation guidance and re-scans — repeating up to three times until the code is clean. Each finding includes its title, severity, location, and line numbers.

**How to use:** After installing, run `/aikido:setup your-api-key` to configure your Aikido API key (get one from app.aikido.dev → Settings → Integrations → IDE Plugins). Then use `/aikido:scan` to scan modified or new files for security issues, apply fixes, and re-scan until clean. You can also ask Claude naturally — for example, "scan my code for security vulnerabilities" or "check for exposed secrets in the files I changed."

Requires Node.js 18 or later and an Aikido API key.

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
