<!-- source: https://claude.com/marketplace/plugins/elixir-ls-lsp -->

Integrates the [ElixirLS](https://github.com/elixir-lsp/elixir-ls) language server with Claude Code, providing code intelligence and diagnostics for Elixir projects. Supports `.ex` (Elixir source), `.exs` (Elixir script), and `.heex` (Phoenix HEEx template) files.

With this plugin enabled, Claude Code gains access to real-time compiler diagnostics, code navigation, and language-aware analysis powered by ElixirLS — the same language server used by popular editors like VS Code and Neovim. This means more accurate code suggestions, better error detection, and richer understanding of your Elixir and Phoenix codebases.

**Prerequisites:** Elixir and Erlang must be installed. ElixirLS can be installed via Homebrew (`brew install elixir-ls`), Nix, or built from source.

**How to use:** Once installed, the plugin activates automatically when you work with Elixir files. Try prompts like: "Find all compiler warnings in this Phoenix project," "Refactor this GenServer module," or "Explain what this Ecto changeset pipeline does." The language server runs in the background, giving Claude deeper insight into your code structure, types, and potential issues.

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
