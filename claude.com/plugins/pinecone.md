<!-- source: https://claude.com/plugins/pinecone -->

# Pinecone

Pinecone vector database integration for managing indexes, querying, and rapid prototyping with slash commands and MCP server support.

* Install in

  [Claude Code](#)

  [Pinecone](https://www.pinecone.io)
* Installs

  9588

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Integrate Pinecone vector database directly into your Claude Code workflow. This plugin provides a complete toolkit for managing vector indexes, querying data with natural language, and rapidly prototyping semantic search applications—all without leaving your editor.

The MCP server gives you access to seven powerful tools: list-indexes, describe-index, describe-index-stats, search-records, create-index-for-model, upsert-records, and rerank-documents. Build RAG applications, recommendation systems, and semantic search features with full control over your vector data.

**How to use:** Run `/pinecone:quickstart` to generate AGENTS.md files and walk through a Python tutorial. Use `/pinecone:query` to search your indexes interactively—specify an index name, namespace, and optional reranker. Run `/pinecone:help` for setup guidance and troubleshooting. You can also ask Claude directly to "list my Pinecone indexes" or "create a new index for my embeddings model."

Requires a Pinecone API key set as `PINECONE_API_KEY` environment variable before starting Claude Code. Sign up for a free account at pinecone.io to get started.

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
