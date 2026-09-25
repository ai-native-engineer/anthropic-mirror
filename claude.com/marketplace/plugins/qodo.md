<!-- source: https://claude.com/marketplace/plugins/qodo -->

Qodo brings shift-left code review directly into your Claude Code workflow. It connects to Qodo's AI-powered code quality platform to retrieve relevant coding rules before you write or refactor code, and to resolve PR review feedback without leaving your agent session. The plugin enforces your organization's coding standards consistently across your entire development lifecycle.

The **qodo-get-rules** skill automatically fetches the most relevant coding rules for your current task using semantic search. When you're about to write, edit, or refactor code, it queries Qodo's rules database and returns applicable standards ranked by relevance, with severity levels (error, warning, recommendation) so you know which rules are strict requirements and which are advisory.

The **qodo-pr-resolver** skill fetches AI-generated review comments from Qodo on your current branch's pull request, then lets you fix issues interactively or in batch mode. It supports GitHub, GitLab, Bitbucket, Azure DevOps, and Gerrit. It includes safety features like oscillation prevention (detecting when a fix would reverse a prior decision) and automatic deduplication of findings across multiple review rounds.

**How to use:** Run `/qodo-get-rules` before starting a coding task to load relevant coding standards — the skill also triggers automatically during code generation and refactoring. Use `/qodo-pr-resolver` to pull in Qodo's review comments on your current branch's PR and fix them one by one or all at once. Requires a Qodo API key configured in `~/.qodo/config.json` (get one at [app.qodo.ai](https://app.qodo.ai/account/api-keys)).

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
