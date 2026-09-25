<!-- source: https://claude.com/marketplace/plugins/code-review -->

Automates pull request code review using multiple specialized agents working in parallel. Five independent reviewers analyze your changes from different angles: CLAUDE.md compliance checking, bug detection, git history context analysis, previous PR comment review, and code comment verification. Each finding is scored on a 0-100 confidence scale, and only high-confidence issues (default threshold: 80) are posted as comments, dramatically reducing false positives and review noise.

The plugin intelligently filters out PRs that don't need review—closed, draft, automated, or already-reviewed pull requests are automatically skipped. Comments include direct GitHub links with full SHA hashes and line number ranges for easy navigation to the exact code in question.

**How to use:** Run `/code-review` on any PR branch to launch the full automated review. The system will analyze your changes, score potential issues, and post actionable feedback directly to GitHub. You can customize the confidence threshold or focus areas (security, performance, accessibility) by editing the command configuration.

## Other plugins

### [Frontend Design](https://claude.com/marketplace/plugins/frontend-design)

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

### [Superpowers](https://claude.com/marketplace/plugins/superpowers)

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

### [Context7](https://claude.com/marketplace/plugins/context7)

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

### [Code Simplifier](https://claude.com/marketplace/plugins/code-simplifier)

Code clarity agent: simplifies and refines recently modified code while preserving functionality and consistency.

### [Playwright](https://claude.com/marketplace/plugins/playwright)

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, and automate testing workflows.

### [GitHub](https://claude.com/marketplace/plugins/github)

Official GitHub MCP server for repo management. Create issues, manage PRs, review code, search repos, and access GitHub's API from Claude Code.
