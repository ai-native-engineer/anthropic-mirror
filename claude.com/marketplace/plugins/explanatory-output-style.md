<!-- source: https://claude.com/marketplace/plugins/explanatory-output-style -->

This plugin adds educational insights about implementation choices and codebase patterns to Claude's responses. It recreates the functionality of the deprecated "Explanatory" output style as a session hook that activates automatically when you start a new session.

When enabled, Claude will provide 2-3 key educational points about your codebase as you work, formatted in a distinctive insight box. These insights focus on implementation choices specific to your codebase, pattern conventions, and design trade-offs — not generic programming concepts.

**How to use:** Simply install the plugin and it activates automatically on each new session. Claude will include educational insights as it writes code, helping you learn about the codebase while completing tasks. Note that this plugin increases token usage due to the additional instructional output.

**Example output format:**
`★ Insight ─────────────────────────────────────`
[2-3 key educational points about the code]
`─────────────────────────────────────────────────`

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
