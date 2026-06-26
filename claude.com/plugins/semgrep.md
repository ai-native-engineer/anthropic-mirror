<!-- source: https://claude.com/plugins/semgrep -->

# Semgrep

Semgrep catches security vulnerabilities in real-time and guides Claude to write secure code from the start.

* Install in

  [Claude Code](#)

  [Semgrep](https://semgrep.dev)
* Installs

  17255

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Semgrep catches security vulnerabilities in real-time as Claude writes code. The plugin integrates Semgrep's static analysis engine directly into your Claude Code workflow, automatically scanning files after every edit for issues like injection flaws, hardcoded secrets, and insecure patterns — then guiding Claude to produce secure code from the start.

At session start and with each prompt, Semgrep injects secure coding defaults so Claude follows security best practices by default. After every file write or edit, a post-tool hook automatically runs a Semgrep scan on the changed code, catching vulnerabilities before they make it into your codebase. This provides a continuous security feedback loop without any manual intervention.

The plugin connects to Semgrep's MCP server, giving Claude access to Semgrep's full analysis capabilities including SAST (static application security testing), SCA (software composition analysis), and secrets detection — all powered by Semgrep's extensive rule library with minimal false positives.

**How to use:** After installing, run `/semgrep-plugin:setup_semgrep_plugin` to configure Semgrep and authenticate your account. Once set up, the plugin works automatically — security scans run in the background on every code change, and Claude receives secure coding guidance with each prompt. No additional commands needed for day-to-day use.

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
