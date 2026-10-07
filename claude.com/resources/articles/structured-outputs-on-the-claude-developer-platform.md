<!-- source: https://claude.com/resources/articles/structured-outputs-on-the-claude-developer-platform -->

***Update:** Now generally available (GA) natively on the Claude Developer Platform and in Amazon Bedrock for Claude Sonnet 4.5, Opus 4.5, and Haiku 4.5. GA adds support for more complex schemas. (Feb 4, 2026)*

***Update:** Now available on Claude Haiku 4.5—supported on the Claude Developer Platform, natively and in Microsoft Foundry. (Dec 4, 2025)*

The Claude Developer Platform now supports structured outputs for Claude Sonnet 4.5 and Opus 4.1. Available in public beta, this feature ensures API responses always match your specified JSON schemas or tool definitions.

With structured outputs, developers can eliminate schema-related parsing errors and failed tool calls by ensuring that Claude's responses conform to a defined schema—whether you're extracting data from images, orchestrating agents, or integrating with external APIs.

### Building reliable applications

For developers building applications and agents in production, a single error in data formatting can cause cascading failures. Structured outputs solves this by guaranteeing your response matches the exact structure you define, without any impact to model performance. This makes Claude dependable for applications and agents where accuracy is critical, including:

* **Data extraction** when downstream systems rely on error-free, consistent formats.
* **Multi-agent architectures** where consistent communication between agents is critical for a performant, stable experience.
* **Complex search tools** where multiple search fields must be filled in accurately and conform to specific patterns.

Structured outputs can be used two ways: with JSON or tools. When used with JSON, you provide your schema definition in the API request. For tools, you define your tool specifications, and Claude's output conforms to those tool definitions automatically.

The end result is a reliable output, reduced retries, and a simplified codebase that no longer needs failover logic or complex error handling.

### Customer Spotlight: OpenRouter

OpenRouter provides 4M+ developers access to all major AI models through a single, unified interface.

"Structured outputs have become a really valuable part of the agentic AI stack. Agents constantly ingest and produce structured data, so Anthropic’s structured outputs close a real gap for developers. Agent workflows run reliably, every time, and teams can focus on their customers rather than debugging tool calls,” said Chris Clark, COO, OpenRouter.

### Getting started

Structured outputs is now available in public beta for Sonnet 4.5 and Opus 4.1 on the Claude Developer Platform, with support for Haiku 4.5 coming soon. Explore our [documentation](https://docs.claude.com/en/docs/build-with-claude/structured-outputs) for supported JSON schema types, implementation examples, and best practices.

[ArticleOct 1, 2026

### Customize Claude Code with mods

Change how Claude Code behaves and looks with a few lines of TypeScript.

Claude Code](https://claude.com/resources/articles/claude-code-mods)[ArticleSep 30, 2026

### Claude for Government is now generally available

Claude Code CLI and Claude for Microsoft 365 also now available in early access.](https://claude.com/resources/articles/claude-for-government-is-now-generally-available)[ArticleSep 25, 2026

### Build plugins for Claude

You can now submit plugins to the Claude directory through a new developer portal, track them through review, and see usage analytics once they’re live.

Claude apps](https://claude.com/resources/articles/build-plugins-for-claude)[ArticleSep 24, 2026

### Claude Tag now supports personal connectors in channels

Claude Tag can now use your connectors for requests you make in a channel. Nobody else can use them, and you're in control of how to present the output.

Claude Tag](https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Structured outputs on the Claude Developer Platform | Claude by Anthropic
