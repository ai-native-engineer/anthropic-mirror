<!-- source: https://claude.com/plugins/explanatory-output-style -->

# Explanatory Output Style

Adds educational insights on implementation choices and codebase patterns (mimics deprecated Explanatory style)

* Anthropic Verified
* Install in

  [Claude Code](#)

  [Anthropic](https://anthropic.com)
* Installs

  59521

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

This plugin adds educational insights about implementation choices and codebase patterns to Claude's responses. It recreates the functionality of the deprecated "Explanatory" output style as a session hook that activates automatically when you start a new session.

When enabled, Claude will provide 2-3 key educational points about your codebase as you work, formatted in a distinctive insight box. These insights focus on implementation choices specific to your codebase, pattern conventions, and design trade-offs — not generic programming concepts.

**How to use:** Simply install the plugin and it activates automatically on each new session. Claude will include educational insights as it writes code, helping you learn about the codebase while completing tasks. Note that this plugin increases token usage due to the additional instructional output.

**Example output format:**  
`★ Insight ─────────────────────────────────────`  
[2-3 key educational points about the code]  
`─────────────────────────────────────────────────`

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
