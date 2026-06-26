<!-- source: https://claude.com/plugins/elixir-ls-lsp -->

# Elixir LS

ElixirLS for Claude Code — code intelligence and diagnostics for .ex, .exs, .heex files.

* Install in

  [Claude Code](#)

  [mikaelfangel](https://github.com/MikaelFangel)
* Installs

  2006

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Integrates the [ElixirLS](https://github.com/elixir-lsp/elixir-ls) language server with Claude Code, providing code intelligence and diagnostics for Elixir projects. Supports `.ex` (Elixir source), `.exs` (Elixir script), and `.heex` (Phoenix HEEx template) files.

With this plugin enabled, Claude Code gains access to real-time compiler diagnostics, code navigation, and language-aware analysis powered by ElixirLS — the same language server used by popular editors like VS Code and Neovim. This means more accurate code suggestions, better error detection, and richer understanding of your Elixir and Phoenix codebases.

**Prerequisites:** Elixir and Erlang must be installed. ElixirLS can be installed via Homebrew (`brew install elixir-ls`), Nix, or built from source.

**How to use:** Once installed, the plugin activates automatically when you work with Elixir files. Try prompts like: "Find all compiler warnings in this Phoenix project," "Refactor this GenServer module," or "Explain what this Ecto changeset pipeline does." The language server runs in the background, giving Claude deeper insight into your code structure, types, and potential issues.

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
