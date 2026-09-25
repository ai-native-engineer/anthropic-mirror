<!-- source: https://claude.com/marketplace/plugins/hookify -->

Hookify lets you create custom behavioral guardrails for Claude using simple markdown files. Define rules to warn about or block unwanted behaviors like dangerous bash commands, debug code in production files, or hardcoded credentials—all without writing any code.

Rules are configured with YAML frontmatter in markdown files, supporting regex pattern matching across different event types: bash commands, file edits, user prompts, and session stops. Changes take effect immediately without restarting Claude.

**How to use:**

Create rules from natural language: `/hookify Warn me when I use rm -rf commands` or `/hookify Don't use console.log in TypeScript files`. Run `/hookify` without arguments to analyze recent conversation and auto-generate rules from behaviors you've corrected. Use `/hookify:list` to see active rules and `/hookify:configure` for interactive management.

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
