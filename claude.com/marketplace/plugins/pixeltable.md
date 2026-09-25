<!-- source: https://claude.com/marketplace/plugins/pixeltable -->

Pixeltable is a plugin that helps you build multimodal AI applications using Pixeltable's declarative table framework. It provides expert guidance on tables, computed columns, embedding indexes, user-defined functions (UDFs), tool-calling agents, and integrations with 25+ AI providers including OpenAI, Anthropic, Gemini, Groq, Bedrock, Together, Fireworks, and Ollama. Instead of stitching together LangChain, pandas, and vector databases, you work with a single unified system where inserting a row automatically triggers the entire computed-column pipeline.

The plugin includes two specialist agents: a **Pipeline Architect** that designs Pixeltable schemas for multimodal ML pipelines — mapping out tables, views, computed columns, indexes, and UDFs — and a **Debugger** that diagnoses failing or stale pipelines using CLI inspection and SDK validation. Both agents encode Pixeltable-specific best practices and anti-patterns so you avoid common pitfalls.

Two slash commands round out the plugin: `/scaffold` generates new Pixeltable projects from templates (knowledge bases, chat agents, audio transcription, video search, and more) and `/add-provider` walks you through wiring up any supported AI provider as a computed column in your tables.

**How to use:** Type `/scaffold` to create a new Pixeltable project from a template. Use `/add-provider` to integrate an AI provider like OpenAI or Anthropic into your pipeline. Ask questions like "design a RAG pipeline for PDF documents", "debug why my computed column returns empty results", or "set up a video search table with embedding indexes" to get expert Pixeltable guidance from the built-in agents.

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
