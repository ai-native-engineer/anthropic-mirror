<!-- source: https://claude.com/resources/articles/1m-context -->

***Update:**Now available on Google Cloud's Vertex AI (Aug 26, 2025)*

Claude Sonnet 4 now supports up to 1 million tokens of context on the Anthropic API—a 5x increase that lets you process entire codebases with over 75,000 lines of code or dozens of research papers in a single request.

Long context support for Sonnet 4 is now in public beta on the Claude Developer Platform natively, and in Amazon Bedrock and Google Cloud’s Vertex AI.

### Longer context, more use cases

With longer context, developers can run more comprehensive and data-intensive use cases with Claude, including:

* **Large-scale code analysis:** Load entire codebases including source files, tests, and documentation. Claude can understand project architecture, identify cross-file dependencies, and suggest improvements that account for the complete system design.
* **Document synthesis:** Process extensive document sets like legal contracts, research papers, or technical specifications. Analyze relationships across hundreds of documents while maintaining full context.
* **Context-aware agents:** Build agents that maintain context across hundreds of tool calls and multi-step workflows. Include complete API documentation, tool definitions, and interaction histories without losing coherence.

### API pricing

To account for increased computational requirements, [pricing](https://www.anthropic.com/pricing#api) adjusts for prompts over 200K tokens:

Claude Sonnet 4 pricing on the Anthropic API

|  | Input | Output |
| --- | --- | --- |
| Prompts ≤ 200K | $3 / MTok | $15 / MTok |
| Prompts > 200K | $6 / MTok | $22.50 / MTok |

When combined with [prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching), users can reduce latency and costs for Claude Sonnet 4 with long context. The 1M context window can also be used with [batch processing](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing) for an additional 50% cost savings.

### Customer spotlight: Bolt.new

Bolt.new transforms web development by integrating Claude into their browser-based development platform.

“Claude Sonnet 4 remains our go-to model for code generation workflows, consistently outperforming other leading models in production. With the 1M context window, developers can now work on significantly larger projects while maintaining the high accuracy we need for real-world coding," said Eric Simons, CEO and Co-founder of Bolt.new.

### Customer spotlight: iGent AI

London-based iGent AI is advancing the field of software development with Maestro, an AI partner that transforms conversations into executable code.

"What was once impossible is now reality: Claude Sonnet 4 with 1M token context has supercharged autonomous capabilities in Maestro, our software engineering agent at iGent AI. This leap unlocks true production-scale engineering—multi-day sessions on real-world codebases—establishing a new paradigm in agentic software engineering," said Sean Ward, CEO and Co-founder of iGent AI.

### Get started

Long context support for Sonnet 4 is now in public beta on the Claude Developer Platform for customers with Tier 4 and custom rate limits, with broader availability rolling out over the coming weeks. Long context is also available in Amazon Bedrock and on Google Cloud's Vertex AI. We’re also exploring how to bring long context to other Claude products.

To learn more about Sonnet 4 and the 1M context window, see our [documentation](https://docs.anthropic.com/en/docs/build-with-claude/context-windows#1m-token-context-window) and [pricing page](https://www.anthropic.com/pricing#api).

[ArticleNov 5, 2026

### Introducing Personal Finance in Claude

Ask Claude about your money and get straight answers from the accounts you connect.](https://claude.com/resources/articles/introducing-personal-finance-in-claude)[ArticleNov 5, 2026

### More visibility and control over Claude Enterprise for security teams

Claude EnterpriseClaude apps](https://claude.com/resources/articles/claude-enterprise-security-updates)[ArticleNov 4, 2026

### New agents and products for security, productivity, and creative work on Claude Marketplace](https://claude.com/resources/articles/new-agents-and-products-claude-marketplace)[ArticleNov 2, 2026

### Make long-running agents faster with message threads

New in the Messages API, send your conversation once, and the API receives only what’s new with every turn.

Claude Platform](https://claude.com/resources/articles/message-threads)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
