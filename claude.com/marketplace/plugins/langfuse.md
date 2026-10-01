<!-- source: https://claude.com/marketplace/plugins/langfuse -->

Integrate with **Langfuse**, the open-source LLM engineering platform, directly from Claude Code. This plugin gives you skills for setting up tracing and observability in your LLM applications, migrating hardcoded prompts into Langfuse's managed prompt system, querying traces and datasets via the Langfuse CLI, configuring CI/CD experiment gates for automated regression checks, and looking up Langfuse documentation, SDK usage, and integration guides.

Key capabilities include a guided instrumentation workflow that assesses your current setup and adds proper span hierarchy, token tracking, and PII masking; a prompt migration skill that inventories your codebase's prompts and moves them to Langfuse with versioning and labeling; error analysis and LLM judge calibration references; and CI/CD gating via the `langfuse/experiment-action` GitHub Action for automated quality checks on pull requests.

**How to use:** Ask Claude to help with Langfuse tasks naturally — for example, `"Set up Langfuse tracing in my project"`, `"Migrate my hardcoded prompts to Langfuse"`, `"Query my recent traces using the Langfuse CLI"`, `"Add a Langfuse experiment gate to my CI pipeline"`, or `"How do I capture user feedback with Langfuse?"`. The plugin automatically fetches the latest Langfuse docs and uses the `langfuse-cli` to interact with your Langfuse instance.

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
