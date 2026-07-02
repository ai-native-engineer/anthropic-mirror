<!-- source: https://claude.com/plugins/pixeltable -->

# Pixeltable

Build multimodal AI apps with Pixeltable -- tables, computed columns, embeddings, UDFs, agents, 25+ AI integrations.

  [Pixeltable](https://pixeltable.com)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Pixeltable is a plugin that helps you build multimodal AI applications using Pixeltable's declarative table framework. It provides expert guidance on tables, computed columns, embedding indexes, user-defined functions (UDFs), tool-calling agents, and integrations with 25+ AI providers including OpenAI, Anthropic, Gemini, Groq, Bedrock, Together, Fireworks, and Ollama. Instead of stitching together LangChain, pandas, and vector databases, you work with a single unified system where inserting a row automatically triggers the entire computed-column pipeline.

The plugin includes two specialist agents: a **Pipeline Architect** that designs Pixeltable schemas for multimodal ML pipelines — mapping out tables, views, computed columns, indexes, and UDFs — and a **Debugger** that diagnoses failing or stale pipelines using CLI inspection and SDK validation. Both agents encode Pixeltable-specific best practices and anti-patterns so you avoid common pitfalls.

Two slash commands round out the plugin: `/scaffold` generates new Pixeltable projects from templates (knowledge bases, chat agents, audio transcription, video search, and more) and `/add-provider` walks you through wiring up any supported AI provider as a computed column in your tables.

**How to use:** Type `/scaffold` to create a new Pixeltable project from a template. Use `/add-provider` to integrate an AI provider like OpenAI or Anthropic into your pipeline. Ask questions like "design a RAG pipeline for PDF documents", "debug why my computed column returns empty results", or "set up a video search table with embedding indexes" to get expert Pixeltable guidance from the built-in agents.
