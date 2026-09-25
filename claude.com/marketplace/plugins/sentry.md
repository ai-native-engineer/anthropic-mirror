<!-- source: https://claude.com/marketplace/plugins/sentry -->

The Sentry plugin brings powerful error monitoring and debugging capabilities directly into Claude Code. Connect to your Sentry environment to analyze production errors, investigate stack traces, and identify patterns across issues—all through natural language queries. The plugin provides real-time access to your error data with severity indicators, user impact metrics, and direct links to Sentry issues.

Key features include the issue-summarizer agent for parallel analysis of multiple issues, automatic pattern detection across error types, and root cause investigation with actionable fix suggestions. The plugin quantifies user impact and prioritizes issues by severity, helping you focus on what matters most.

**How to use:**

Use `/seer` followed by natural language queries like "What are the top errors in the last 24 hours?" or "Show me unresolved issues assigned to me." Run `/getIssues [projectName]` to retrieve recent issues from a specific project. The sentry-code-review skill automatically analyzes and fixes detected bugs in GitHub Pull Requests.

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
