<!-- source: https://claude.com/plugins/sourcegraph -->

# Sourcegraph

Search code across codebases, trace references, analyze refactor impact, investigate incidents, run security sweeps.

* Install in

  [Claude Code](#)

  [Sourcegraph Community](https://github.com/sourcegraph-community/sourcegraph-claudecode-plugin)
* Installs

  11452

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Search, navigate, and understand code across all your repositories directly from Claude Code. This plugin connects to your Sourcegraph instance via MCP, giving you access to semantic search, keyword/regex search, commit and diff history, symbol navigation, reference tracing, and Sourcegraph's Deep Search — all without leaving your terminal.

With twelve integrated tools spanning search, code navigation, and analysis, you can explore unfamiliar codebases, trace how symbols are used across repositories, investigate incidents through commit history, audit code for security patterns, and assess the impact of refactors before making changes.

**How to use:** Set your `SOURCEGRAPH_ENDPOINT` and `SOURCEGRAPH_ACCESS_TOKEN` environment variables, then try these commands and prompts:

`/sourcegraph:sg-search` — Run a Sourcegraph search using natural language or keyword syntax (e.g., "find all callers of parseConfig across our Go services").  
`/sourcegraph:sg-file` — Retrieve and summarize a file from any repository, highlighting key symbols and suggesting related files to explore.  
"Search for all uses of the deprecated handleAuth function and show me which repos still depend on it."  
"Find recent commits that modified database migration files across all backend repos."  
"Trace where the UserSession type is defined and list every file that references it."

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
