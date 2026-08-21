<!-- source: https://claude.com/plugins/context7 -->

# Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

* Install in

  [Claude Code](#)

  [Upstash](https://upstash.com)
* Installs

  417801

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Context7 is an MCP server that delivers up-to-date, version-specific documentation and code examples directly into your prompts. It solves a common problem with LLMs: outdated training data leading to hallucinated APIs and deprecated code patterns. Instead of relying on stale information, Context7 pulls current documentation straight from source repositories.

The plugin provides two main tools: **resolve-library-id** for matching library names to Context7-compatible identifiers, and **query-docs** for retrieving documentation for specific libraries. You can even target specific versions by mentioning them in your prompt.

**How to use:** Simply add "use context7" to any prompt where you need current documentation. For example: "Create a Next.js middleware that checks for a valid JWT in cookies. use context7" or "Configure a Cloudflare Worker script to cache JSON API responses. use context7". You can also specify exact libraries with "use library /supabase/supabase for API and docs".

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

1134112

installs](https://claude.com/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

1009371

installs](https://claude.com/plugins/superpowers)

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

438525

installs](https://claude.com/plugins/code-review)

[### Skill Creator

Create, improve, and measure skills. Use for creating, updating, evaluating, and benchmarking performance.

Anthropic verified

385083

installs](https://claude.com/plugins/skill-creator)
