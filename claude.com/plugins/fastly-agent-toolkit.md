<!-- source: https://claude.com/plugins/fastly-agent-toolkit -->

# Fastly Agent Toolkit

Fastly development tools and platform skills

* Install in

  [Claude Code](#)

  [Fastly](https://www.fastly.com)
* Installs

  2636

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

A collection of six specialized skills that give your coding agent deep knowledge of the Fastly edge cloud platform. Covers the full Fastly development lifecycle — from writing and linting VCL, to running Compute applications locally, to managing services, caching, security, and deployment via the Fastly CLI and API.

The toolkit includes skills for: **Fastly platform** knowledge (services, caching, WAF, TLS, DDoS, purging, and API usage), **Fastly CLI** operations, **Falco** (VCL linting, testing, simulation, and formatting), **Viceroy** (local WASM-based Compute execution and testing for Rust projects), **Fastlike** (Go-based local Compute execution), and **XVCL** (a VCL transpiler with metaprogramming features like loops, constants, and macros).

Each skill provides curated reference documentation that the agent consults when working on Fastly projects, helping it avoid common pitfalls like VCL scope violations, incorrect Vary header placement, missing local\_server configuration, and deprecated syntax.

### How to use

Install individual skills based on your workflow — for example, add the `falco` and `viceroy` skills if you're developing Fastly Compute apps in Rust. Once installed, skills activate automatically based on context. Try prompts like: "Lint my VCL files and fix any errors", "Set up a local Viceroy dev server for this Compute app", "Configure a new Fastly service with caching and WAF rules", "Transpile my XVCL files to VCL and test them with Falco", or "Help me set up logging endpoints and purge strategies for this Fastly service".

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
