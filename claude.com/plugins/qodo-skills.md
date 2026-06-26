<!-- source: https://claude.com/plugins/qodo-skills -->

# Qodo Skills

Qodo Skills: AI agents that integrate code quality, testing, security, and compliance checks into your SDLC.

* Install in

  [Claude Code](#)

  [Qodo.ai](https://github.com/qodo-ai/qodo-skills)
* Installs

  10986

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Qodo Skills brings shift-left code review capabilities into your development workflow. It connects Claude Code to the Qodo platform, letting you fetch and enforce repository-specific coding rules before you commit, and resolve Qodo PR review issues directly from your terminal. Rules are organized by severity—ERROR (mandatory), WARNING (recommended), and RECOMMENDATION (optional)—and are scoped hierarchically across organization, repository, and path levels.

The plugin includes two core skills: **get-qodo-rules** fetches your team's coding standards from the Qodo API and applies them during code generation, refactoring, and review tasks. **qodo-pr-resolver** pulls Qodo review comments from open pull requests and lets you fix issues interactively or in batch mode, with automatic commits and PR summary comments. It supports GitHub, GitLab, Bitbucket, and Azure DevOps.

**How to use:** Say `get qodo rules` or `load coding rules` before writing or modifying code to enforce your team's standards. To resolve PR feedback, say `resolve pr`, `qodo fix`, or `fix qodo issues` while on a branch with an open pull request. The resolver will display outstanding issues and let you choose manual review or auto-fix mode.

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

948012

installs](/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

855112

installs](/plugins/superpowers)

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

383892

installs](/plugins/code-review)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

377529

installs](/plugins/context7)
