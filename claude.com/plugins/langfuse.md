<!-- source: https://claude.com/plugins/langfuse -->

# Langfuse

Skills for Langfuse: open-source LLM platform for tracing, prompts, and evaluation

* Install in

  [Claude Code](#)

  [Langfuse](https://langfuse.com)
* Installs

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Integrate with **Langfuse**, the open-source LLM engineering platform, directly from Claude Code. This plugin gives you skills for setting up tracing and observability in your LLM applications, migrating hardcoded prompts into Langfuse's managed prompt system, querying traces and datasets via the Langfuse CLI, configuring CI/CD experiment gates for automated regression checks, and looking up Langfuse documentation, SDK usage, and integration guides.

Key capabilities include a guided instrumentation workflow that assesses your current setup and adds proper span hierarchy, token tracking, and PII masking; a prompt migration skill that inventories your codebase's prompts and moves them to Langfuse with versioning and labeling; error analysis and LLM judge calibration references; and CI/CD gating via the `langfuse/experiment-action` GitHub Action for automated quality checks on pull requests.

**How to use:** Ask Claude to help with Langfuse tasks naturally — for example, `"Set up Langfuse tracing in my project"`, `"Migrate my hardcoded prompts to Langfuse"`, `"Query my recent traces using the Langfuse CLI"`, `"Add a Langfuse experiment gate to my CI pipeline"`, or `"How do I capture user feedback with Langfuse?"`. The plugin automatically fetches the latest Langfuse docs and uses the `langfuse-cli` to interact with your Langfuse instance.

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
