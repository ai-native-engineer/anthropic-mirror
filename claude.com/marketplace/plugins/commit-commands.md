<!-- source: https://claude.com/marketplace/plugins/commit-commands -->

Streamline your git workflow with intelligent commands for committing, pushing, and creating pull requests. This plugin automates common git operations with AI-powered commit message generation that matches your repository's existing style conventions.

Key features include automatic analysis of staged and unstaged changes, smart commit message generation based on recent commit history, comprehensive PR descriptions with summaries and test plan checklists, and protection against accidentally committing sensitive files like `.env`.

**How to use:** Type `/commit` to automatically stage changes and create a commit with an AI-generated message. Use `/commit-push-pr` for a complete workflow that commits, pushes to a feature branch, and creates a pull request in one step. Run `/clean_gone` to remove local branches that have been deleted from the remote repository.

**Requirements:** Git must be installed and configured. For PR creation, the GitHub CLI (`gh`) must be authenticated. Your repository needs a remote origin configured.

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
