<!-- source: https://claude.com/plugins/goodmem -->

# GoodMem

GoodMem: AI memory infrastructure. Python SDK and MCP tools manage embedders, spaces, memories via natural language.

* Install in

  [Claude Code](#)

  [PAIR Systems](https://docs.goodmem.ai)
* Installs

  3622

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

GoodMem provides memory infrastructure for AI agents, enabling storage, retrieval, and semantic search over vector embeddings. The plugin exposes 41 MCP tools across 10 functional namespaces — covering embedder management, memory spaces, semantic retrieval, LLM and reranker registration, OCR, and administration. A built-in registry of 79 models (29 embedders, 34 LLMs, 16 rerankers) auto-infers provider types, endpoints, and dimensionality from a model identifier, reducing manual setup.

The plugin supports two usage modes. You can perform GoodMem operations directly through natural language — Claude will invoke the underlying MCP tools to create embedders, manage memory spaces, store documents, and run semantic searches. Alternatively, you can ask Claude to generate Python scripts using the GoodMem SDK for building complete RAG pipelines and retrieval applications.

Supported providers include OpenAI, Cohere, Voyage, Google, Jina, Anthropic, and Mistral for embeddings, language models, and rerankers. SaaS provider credentials are validated before API calls, with clear error messages for missing keys. Configuration can be done via environment variables or interactively in chat.

**How to use:** After installing, configure your GoodMem credentials by setting `GOODMEM_BASE_URL` and `GOODMEM_API_KEY` environment variables, or say "configure GoodMem" to set them interactively. Then try prompts like: "Create an embedder using OpenAI text-embedding-3-small", "Create a memory space called 'project-docs' and ingest this file", "Search my memories for authentication error handling", or "Write a Python RAG pipeline using the GoodMem SDK". Use `/goodmem:help` for setup guidance, `/goodmem:mcp` for the full MCP tools reference, and `/goodmem:python` for Python SDK documentation.

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
