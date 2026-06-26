<!-- source: https://claude.com/plugins/sonatype-guide -->

# Sonatype Guide

Sonatype Guide MCP: supply chain intelligence & dependency security analysis with vulnerability detection and version recommendations.

* Install in

  [Claude Code](#)

  [Sonatype](https://guide.sonatype.com)
* Installs

  6989

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Sonatype Guide connects Claude Code to Sonatype's software supply chain intelligence platform via MCP. It lets you scan your project's dependencies for known vulnerabilities, get secure version recommendations, and evaluate open-source components based on security, licensing, and quality metrics — all without leaving your editor.

The plugin connects to Sonatype's hosted MCP server, providing access to their comprehensive component database. It authenticates using an API token from [guide.sonatype.com](https://guide.sonatype.com/settings/tokens), set via the `SONATYPE_GUIDE_TOKEN` environment variable.

**How to use:** After installing and setting your API token, try prompts like: "What vulnerabilities exist in log4j 2.14.0?", "Scan my package.json for vulnerable dependencies", "What's the most secure version of lodash?", or "Evaluate the quality and licensing of this npm package".

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
