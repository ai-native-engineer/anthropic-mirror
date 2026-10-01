<!-- source: https://claude.com/marketplace/plugins/qodo-skills -->

Qodo Skills brings shift-left code review capabilities into your development workflow. It connects Claude Code to the Qodo platform, letting you fetch and enforce repository-specific coding rules before you commit, and resolve Qodo PR review issues directly from your terminal. Rules are organized by severity—ERROR (mandatory), WARNING (recommended), and RECOMMENDATION (optional)—and are scoped hierarchically across organization, repository, and path levels.

The plugin includes two core skills: **get-qodo-rules** fetches your team's coding standards from the Qodo API and applies them during code generation, refactoring, and review tasks. **qodo-pr-resolver** pulls Qodo review comments from open pull requests and lets you fix issues interactively or in batch mode, with automatic commits and PR summary comments. It supports GitHub, GitLab, Bitbucket, and Azure DevOps.

**How to use:** Say get qodo rules or load coding rules before writing or modifying code to enforce your team's standards. To resolve PR feedback, say resolve pr, qodo fix, or fix qodo issues while on a branch with an open pull request. The resolver will display outstanding issues and let you choose manual review or auto-fix mode.

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
