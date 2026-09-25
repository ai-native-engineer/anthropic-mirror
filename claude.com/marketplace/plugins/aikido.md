<!-- source: https://claude.com/marketplace/plugins/aikido -->

Aikido Security scanning for Claude Code detects SAST vulnerabilities, exposed secrets, and Infrastructure-as-Code misconfigurations in code you write or modify. Powered by the Aikido MCP server, it scans your files in real time and guides Claude to fix issues before they ship.

The plugin automatically identifies files generated or changed during your session, runs a full security scan (up to 50 files per request), and when vulnerabilities are found, applies remediation guidance and re-scans — repeating up to three times until the code is clean. Each finding includes its title, severity, location, and line numbers.

**How to use:** After installing, run `/aikido:setup your-api-key` to configure your Aikido API key (get one from app.aikido.dev → Settings → Integrations → IDE Plugins). Then use `/aikido:scan` to scan modified or new files for security issues, apply fixes, and re-scan until clean. You can also ask Claude naturally — for example, "scan my code for security vulnerabilities" or "check for exposed secrets in the files I changed."

Requires Node.js 18 or later and an Aikido API key.

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
