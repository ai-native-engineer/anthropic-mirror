<!-- source: https://claude.com/plugins/qodo -->

# Qodo

Qodo Skills: AI agent capabilities for code quality, testing, security, and compliance across your SDLC.

* Install in

  [Claude Code](#)
* Made by

  [Qodo.ai](https://www.qodo.ai)
* Installs

  11807

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Qodo Skills brings shift-left code review directly into your Claude Code workflow. It connects to Qodo's AI-powered code quality platform to retrieve relevant coding rules before you write or refactor code, and to resolve PR review feedback without leaving your agent session. The plugin enforces your organization's coding standards consistently across your entire development lifecycle.

The **qodo-get-rules** skill automatically fetches the most relevant coding rules for your current task using semantic search. When you're about to write, edit, or refactor code, it queries Qodo's rules database and returns applicable standards ranked by relevance, with severity levels (error, warning, recommendation) so you know which rules are strict requirements and which are advisory.

The **qodo-pr-resolver** skill fetches AI-generated review comments from Qodo on your current branch's pull request, then lets you fix issues interactively or in batch mode. It supports GitHub, GitLab, Bitbucket, Azure DevOps, and Gerrit. It includes safety features like oscillation prevention (detecting when a fix would reverse a prior decision) and automatic deduplication of findings across multiple review rounds.

**How to use:** Run `/qodo-get-rules` before starting a coding task to load relevant coding standards — the skill also triggers automatically during code generation and refactoring. Use `/qodo-pr-resolver` to pull in Qodo's review comments on your current branch's PR and fix them one by one or all at once. Requires a Qodo API key configured in `~/.qodo/config.json` (get one at [app.qodo.ai](https://app.qodo.ai/account/api-keys)).

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

1134112

installs](https://claude.com/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

1009371

installs](https://claude.com/plugins/superpowers)

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

438525

installs](https://claude.com/plugins/code-review)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

417801

installs](https://claude.com/plugins/context7)
