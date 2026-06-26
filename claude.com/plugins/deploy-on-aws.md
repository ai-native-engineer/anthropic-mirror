<!-- source: https://claude.com/plugins/deploy-on-aws -->

# Deploy on AWS

Deploy applications to AWS with architecture recommendations, cost estimates, and IaC deployment.

* Install in

  [Claude Code](#)

  [Amazon Web Services](https://github.com/awslabs/agent-plugins)
* Installs

  8801

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Deploy applications to AWS through a guided five-stage workflow: analyze your codebase, receive service recommendations, get monthly cost estimates, generate Infrastructure as Code (CDK/CloudFormation), and execute deployments — all without leaving your editor. The plugin defaults to dev-sized configurations and makes straightforward decisions automatically, only prompting you when choices are genuinely ambiguous.

Three MCP servers power the experience: **awsknowledge** for architecture validation and AWS documentation, **awspricing** for real-time cost calculations, and **awsiac** for infrastructure-as-code best practices. Security defaults are applied during code generation, and a security check runs before every deployment.

**How to use:** Trigger the deploy skill with natural language prompts such as `deploy to AWS`, `host on AWS`, `estimate AWS cost`, or `generate infrastructure`. For production workloads, specify "production-ready" to get multi-AZ, redundant configurations instead of the default minimal setup. Requires AWS CLI with configured credentials.

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
