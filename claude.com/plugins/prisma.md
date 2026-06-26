<!-- source: https://claude.com/plugins/prisma -->

# Prisma

Prisma MCP for Postgres: database management, migrations, SQL queries, and data interaction.

* Install in

  [Claude Code](#)

  [Prisma](https://www.prisma.io)
* Installs

  6443

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Prisma MCP integration brings natural language database management to Claude Code. Connect to Prisma Postgres databases to provision new instances, run schema migrations, execute SQL queries, analyze data, and manage connection strings — all through conversational prompts. The plugin configures both a local MCP server (via `npx prisma mcp`) and a remote hosted server at `mcp.prisma.io`, giving you flexibility for local development and cloud workflows.

Key capabilities include creating and configuring databases, executing queries and analyzing results, managing schema migrations, handling backups and connection strings, and opening Prisma Studio to browse your data. The integration supports enterprise-grade security with OAuth, and is compliant with GDPR, HIPAA, ISO 27001, and SOC 2.

**How to use:** Once installed, interact with your Postgres databases using natural language prompts like:

* `"Set up this project with a new database in us-east-1"`
* `"Show me all users who signed up this week and their activity levels"`
* `"Check my migration status and create a new user preferences table"`
* `"Create a new database from the most recent backup"`
* `"Open Prisma Studio and show me the data in my users table"`

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
