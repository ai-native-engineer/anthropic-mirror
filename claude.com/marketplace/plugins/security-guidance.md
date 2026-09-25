<!-- source: https://claude.com/marketplace/plugins/security-guidance -->

A security reminder hook that automatically warns about potential security vulnerabilities when Claude edits files. The plugin intercepts Write, Edit, and MultiEdit operations and scans code for dangerous patterns before changes are applied.

The plugin detects eight major vulnerability categories including command injection in GitHub Actions workflows, unsafe child\_process.exec() calls, eval() and new Function() usage, XSS vectors like dangerouslySetInnerHTML and innerHTML, Python pickle deserialization risks, and os.system() command injection.

**How it works:** The plugin runs automatically as a pre-tool hook - no commands needed. When Claude attempts to write code containing potentially unsafe patterns, you'll see a warning with specific remediation advice before the edit proceeds. Warnings are session-scoped so you only see each one once.

**Example warnings you might see:**

* Suggestions to use execFileNoThrow() instead of child\_process.exec() to prevent shell injection
* Alerts about XSS risks when using innerHTML or dangerouslySetInnerHTML
* Warnings about GitHub Actions injection when editing workflow files

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
