<!-- source: https://claude.com/marketplace/plugins/sonatype-guide -->

Sonatype Guide connects Claude Code to Sonatype's software supply chain intelligence platform via MCP. It lets you scan your project's dependencies for known vulnerabilities, get secure version recommendations, and evaluate open-source components based on security, licensing, and quality metrics — all without leaving your editor.

The plugin connects to Sonatype's hosted MCP server, providing access to their comprehensive component database. It authenticates using an API token from [guide.sonatype.com](https://guide.sonatype.com/settings/tokens), set via the `SONATYPE_GUIDE_TOKEN` environment variable.

**How to use:** After installing and setting your API token, try prompts like: "What vulnerabilities exist in log4j 2.14.0?", "Scan my package.json for vulnerable dependencies", "What's the most secure version of lodash?", or "Evaluate the quality and licensing of this npm package".

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
