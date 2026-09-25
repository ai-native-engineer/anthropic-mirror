<!-- source: https://claude.com/marketplace/plugins/coderabbit -->

CodeRabbit brings AI-powered code review directly into Claude Code. It provides external validation using a specialized AI architecture and 40+ integrated static analyzers, offering a different perspective that catches bugs, security vulnerabilities, logic errors, and edge cases. The plugin performs context-aware analysis via AST parsing and codegraph relationships, and automatically incorporates your CLAUDE.md and project coding guidelines into reviews.

Reviews are organized by severity level: Critical findings (security issues and bugs), Suggestions (code improvements), and Positive feedback (code strengths). The plugin can automatically apply recommended fixes when code generation instructions are available.

**How to use:** Run `/coderabbit:review` to review your code changes. You can also ask naturally: "Review my code", "Check for security issues", or "What's wrong with my changes?" The review command supports different scopes—review all changes, only committed changes, only uncommitted changes, or compare against a specific branch like main.

**Prerequisites:** Requires installing and authenticating the CodeRabbit CLI before use. The plugin is free to use and works within any Git repository.

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
