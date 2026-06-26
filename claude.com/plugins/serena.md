<!-- source: https://claude.com/plugins/serena -->

# Serena

Semantic code analysis MCP server for intelligent code understanding, refactoring, and navigation via language server protocol.

* Install in

  [Claude Code](#)

  [Oraios](https://github.com/oraios)
* Installs

  84277

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Serena transforms Claude into a powerful coding agent with IDE-like capabilities. This MCP server provides semantic code retrieval and editing tools that work at the symbol level, enabling intelligent navigation of large codebases without reading entire files. Supporting over 30 programming languages including Python, JavaScript, TypeScript, Java, Rust, Go, and C++, Serena leverages Language Server Protocol integration to deliver precise code understanding.

Key features include symbol-level code extraction with tools like `find_symbol` and `find_referencing_symbols`, precision editing operations such as `insert_after_symbol`, and token-efficient codebase interaction. The toolkit exploits the relational structure of code to help Claude work effectively on complex projects.

**How to use:** Once installed, Claude gains semantic code tools automatically. Ask Claude to find symbol definitions, locate references across your codebase, or make targeted edits. Example prompts: "Find all references to the UserService class", "Show me where the authenticate function is defined", "Insert a logging statement after the validateInput method".

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
