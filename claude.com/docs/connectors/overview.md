<!-- source: https://claude.com/docs/connectors/overview -->

Connectors extend Claude’s capabilities by connecting it to external tools and data sources. They are powered by the [Model Context Protocol (MCP)](/docs/connectors/building/mcp), an open standard created by Anthropic that provides a unified way for AI applications to interact with the outside world.

##  How connectors work

Connectors can do two things:

* **Provide tools and information** — Give Claude access to external data and the ability to take actions (search files, read emails, create issues, etc.)
* **Surface UI components** — Render interactive visual elements directly in the conversation through [MCP Apps](/docs/connectors/building/mcp-apps/getting-started)

**Building for Claude?** Most partners ship both a remote MCP server and a plugin that wraps it with skills. See [what to build](/docs/connectors/building/what-to-build) for the decision guide.

##  Types of connectors

###  Prebuilt integrations

Anthropic provides first-party integrations with popular services like Google Drive, Gmail, Google Calendar, GitHub, Slack, and Microsoft 365. These are ready to use with no setup beyond authentication. See [Getting started](/docs/connectors/getting-started) for setup instructions.

###  Remote MCP servers

[Remote MCP servers](/docs/connectors/custom/remote-mcp) communicate with Claude over the internet, giving it access to cloud-hosted tools and data. You can connect to existing remote MCP servers or build your own for any tool or service.

###  MCP Apps

[MCP Apps](/docs/connectors/building/mcp-apps/getting-started) allow MCP servers to display interactive UI elements in conversational MCP clients. Rather than only returning text, an MCP App can render charts, maps, forms, and other visual components directly in the chat. See the [design guidelines](/docs/connectors/building/mcp-apps/design-guidelines) and [cross-platform compatibility](/docs/connectors/building/mcp-apps/cross-compatibility) docs for building MCP Apps.

###  MCP Bundles

[MCP Bundles (MCPB)](/docs/connectors/custom/desktop-extensions) package MCP servers with their dependencies for distribution as desktop extensions. MCPB handles cross-platform compatibility, dependency management, code signing, and centralized version updates — making it suitable for enterprise deployment of local MCP servers to Claude Desktop.

###  Self-serve local MCP

Local MCP servers distributed through third-party package registries like npm or PyPI cannot be listed directly in the Connectors Directory. To distribute a local server, package it as an [MCPB](/docs/connectors/building/mcpb) for the Desktop Extensions gallery, or bundle it in a [plugin](/docs/plugins/overview) using `.mcp.json` and submit it to the [plugin directory](/docs/plugins/submit).

##  Ways to connect

###  Connectors directory

The [Connectors Directory](/docs/connectors/directory) is an open catalog of verified and reviewed MCP servers from third-party developers. These integrations are vetted by Anthropic and available across all Claude products.

###  Third-party connectors

You can build and connect your own MCP servers for proprietary tools or workflows. See [Third-party Connectors](/docs/connectors/custom/remote-mcp) for remote MCP and [Desktop Extensions](/docs/connectors/custom/desktop-extensions) for local integrations.

##  Related concepts

###  Plugins

[Plugins](/docs/plugins/overview) combine MCP connectors, [Skills](/docs/skills/overview), slash commands, and sub-agents into shareable capability packages. They are available in Claude Code and Cowork. You can also [submit your plugin](/docs/plugins/submit) to the plugin directory.

##  Platform availability

Prebuilt integrations and directory connectors work across all Claude products:

* **Claude.ai** — Full remote MCP support & MCP Apps
* **Claude Desktop** — Full MCP support and local desktop extensions
* **Claude Mobile** — Remote MCP access
* **Claude Code** — Remote MCP access and plugins
* **Claude Cowork** — Full MCP and plugin support

##  Next steps

## Getting started

Set up your first connector.

## Connectors directory

Browse verified integrations.

## Build a connector

Create your own MCP server.

## MCP Apps

Build UI components for Claude.

## MCP in Claude Code

Add an MCP server to Claude Code from the command line.

## Claude Code documentation

Install, configure, and use the Claude Code CLI.

[Getting started](/docs/connectors/getting-started)
