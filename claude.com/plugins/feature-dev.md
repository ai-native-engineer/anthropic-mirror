<!-- source: https://claude.com/plugins/feature-dev -->

# Feature Dev

Feature development workflow with agents for exploration, design, and review

* Anthropic Verified
* Install in

  [Claude Code](#)

  [Anthropic](https://anthropic.com)
* Installs

  233860

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

A structured 7-phase workflow for building features systematically. Rather than jumping into code, this plugin guides you through understanding the existing codebase, clarifying requirements, designing architecture thoughtfully, and conducting quality reviews before and after implementation.

The plugin deploys three specialized agents: **code-explorer** traces execution paths and maps architecture layers to understand existing patterns; **code-architect** proposes multiple implementation approaches with clear trade-offs; and **code-reviewer** catches bugs, security issues, and convention violations with confidence-scored findings.

**How to use:** Run `/feature-dev` followed by a description of what you want to build. For example: `/feature-dev Add user authentication with OAuth` or simply `/feature-dev` to start the guided workflow. The plugin will walk you through discovery, codebase exploration, clarifying questions, architecture design, implementation, quality review, and a final summary.

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
