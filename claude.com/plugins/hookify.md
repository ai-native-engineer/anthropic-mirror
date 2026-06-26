<!-- source: https://claude.com/plugins/hookify -->

# Hookify

Create custom hooks via markdown to prevent unwanted behaviors from conversation patterns or explicit instructions.

* Anthropic Verified
* Install in

  [Claude Code](#)

  [Anthropic](https://anthropic.com)
* Installs

  55021

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Hookify lets you create custom behavioral guardrails for Claude using simple markdown files. Define rules to warn about or block unwanted behaviors like dangerous bash commands, debug code in production files, or hardcoded credentials—all without writing any code.

Rules are configured with YAML frontmatter in markdown files, supporting regex pattern matching across different event types: bash commands, file edits, user prompts, and session stops. Changes take effect immediately without restarting Claude.

**How to use:**

Create rules from natural language: `/hookify Warn me when I use rm -rf commands` or `/hookify Don't use console.log in TypeScript files`. Run `/hookify` without arguments to analyze recent conversation and auto-generate rules from behaviors you've corrected. Use `/hookify:list` to see active rules and `/hookify:configure` for interactive management.

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
