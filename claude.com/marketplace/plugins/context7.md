<!-- source: https://claude.com/marketplace/plugins/context7 -->

Context7 is an MCP server that delivers up-to-date, version-specific documentation and code examples directly into your prompts. It solves a common problem with LLMs: outdated training data leading to hallucinated APIs and deprecated code patterns. Instead of relying on stale information, Context7 pulls current documentation straight from source repositories.

The plugin provides two main tools: **resolve-library-id** for matching library names to Context7-compatible identifiers, and **query-docs** for retrieving documentation for specific libraries. You can even target specific versions by mentioning them in your prompt.

**How to use:** Simply add "use context7" to any prompt where you need current documentation. For example: "Create a Next.js middleware that checks for a valid JWT in cookies. use context7" or "Configure a Cloudflare Worker script to cache JSON API responses. use context7". You can also specify exact libraries with "use library /supabase/supabase for API and docs".

## Other plugins

### [Frontend Design](https://claude.com/marketplace/plugins/frontend-design)

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

### [Superpowers](https://claude.com/marketplace/plugins/superpowers)

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

### [Code Review](https://claude.com/marketplace/plugins/code-review)

AI code review with specialized agents and confidence-based filtering for pull requests

### [Code Simplifier](https://claude.com/marketplace/plugins/code-simplifier)

Code clarity agent: simplifies and refines recently modified code while preserving functionality and consistency.

### [Playwright](https://claude.com/marketplace/plugins/playwright)

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, and automate testing workflows.

### [GitHub](https://claude.com/marketplace/plugins/github)

Official GitHub MCP server for repo management. Create issues, manage PRs, review code, search repos, and access GitHub's API from Claude Code.
