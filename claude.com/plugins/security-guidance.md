<!-- source: https://claude.com/plugins/security-guidance -->

# Security Guidance

Security hook warns about command injection, XSS, and unsafe code patterns when editing files

* Anthropic Verified
* Install in

  [Claude Code](#)

  [Anthropic](https://anthropic.com)
* Installs

  209119

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

A security reminder hook that automatically warns about potential security vulnerabilities when Claude edits files. The plugin intercepts Write, Edit, and MultiEdit operations and scans code for dangerous patterns before changes are applied.

The plugin detects eight major vulnerability categories including command injection in GitHub Actions workflows, unsafe child\_process.exec() calls, eval() and new Function() usage, XSS vectors like dangerouslySetInnerHTML and innerHTML, Python pickle deserialization risks, and os.system() command injection.

**How it works:** The plugin runs automatically as a pre-tool hook - no commands needed. When Claude attempts to write code containing potentially unsafe patterns, you'll see a warning with specific remediation advice before the edit proceeds. Warnings are session-scoped so you only see each one once.

**Example warnings you might see:**

* Suggestions to use execFileNoThrow() instead of child\_process.exec() to prevent shell injection
* Alerts about XSS risks when using innerHTML or dangerouslySetInnerHTML
* Warnings about GitHub Actions injection when editing workflow files

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
