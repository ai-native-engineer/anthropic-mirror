<!-- source: https://claude.com/marketplace/plugins/deploy-on-aws -->

Deploy applications to AWS through a guided five-stage workflow: analyze your codebase, receive service recommendations, get monthly cost estimates, generate Infrastructure as Code (CDK/CloudFormation), and execute deployments — all without leaving your editor. The plugin defaults to dev-sized configurations and makes straightforward decisions automatically, only prompting you when choices are genuinely ambiguous.

Three MCP servers power the experience: **awsknowledge** for architecture validation and AWS documentation, **awspricing** for real-time cost calculations, and **awsiac** for infrastructure-as-code best practices. Security defaults are applied during code generation, and a security check runs before every deployment.

**How to use:** Trigger the deploy skill with natural language prompts such as `deploy to AWS`, `host on AWS`, `estimate AWS cost`, or `generate infrastructure`. For production workloads, specify "production-ready" to get multi-AZ, redundant configurations instead of the default minimal setup. Requires AWS CLI with configured credentials.

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
