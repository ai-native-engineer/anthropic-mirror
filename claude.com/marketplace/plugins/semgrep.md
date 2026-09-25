<!-- source: https://claude.com/marketplace/plugins/semgrep -->

Semgrep catches security vulnerabilities in real-time as Claude writes code. The plugin integrates Semgrep's static analysis engine directly into your Claude Code workflow, automatically scanning files after every edit for issues like injection flaws, hardcoded secrets, and insecure patterns — then guiding Claude to produce secure code from the start.

At session start and with each prompt, Semgrep injects secure coding defaults so Claude follows security best practices by default. After every file write or edit, a post-tool hook automatically runs a Semgrep scan on the changed code, catching vulnerabilities before they make it into your codebase. This provides a continuous security feedback loop without any manual intervention.

The plugin connects to Semgrep's MCP server, giving Claude access to Semgrep's full analysis capabilities including SAST (static application security testing), SCA (software composition analysis), and secrets detection — all powered by Semgrep's extensive rule library with minimal false positives.

**How to use:** After installing, run `/semgrep-plugin:setup_semgrep_plugin` to configure Semgrep and authenticate your account. Once set up, the plugin works automatically — security scans run in the background on every code change, and Claude receives secure coding guidance with each prompt. No additional commands needed for day-to-day use.

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
