<!-- source: https://claude.com/marketplace/plugins/goodmem -->

GoodMem provides memory infrastructure for AI agents, enabling storage, retrieval, and semantic search over vector embeddings. The plugin exposes 41 MCP tools across 10 functional namespaces — covering embedder management, memory spaces, semantic retrieval, LLM and reranker registration, OCR, and administration. A built-in registry of 79 models (29 embedders, 34 LLMs, 16 rerankers) auto-infers provider types, endpoints, and dimensionality from a model identifier, reducing manual setup.

The plugin supports two usage modes. You can perform GoodMem operations directly through natural language — Claude will invoke the underlying MCP tools to create embedders, manage memory spaces, store documents, and run semantic searches. Alternatively, you can ask Claude to generate Python scripts using the GoodMem SDK for building complete RAG pipelines and retrieval applications.

Supported providers include OpenAI, Cohere, Voyage, Google, Jina, Anthropic, and Mistral for embeddings, language models, and rerankers. SaaS provider credentials are validated before API calls, with clear error messages for missing keys. Configuration can be done via environment variables or interactively in chat.

**How to use:** After installing, configure your GoodMem credentials by setting `GOODMEM_BASE_URL` and `GOODMEM_API_KEY` environment variables, or say "configure GoodMem" to set them interactively. Then try prompts like: "Create an embedder using OpenAI text-embedding-3-small", "Create a memory space called 'project-docs' and ingest this file", "Search my memories for authentication error handling", or "Write a Python RAG pipeline using the GoodMem SDK". Use `/goodmem:help` for setup guidance, `/goodmem:mcp` for the full MCP tools reference, and `/goodmem:python` for Python SDK documentation.

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
