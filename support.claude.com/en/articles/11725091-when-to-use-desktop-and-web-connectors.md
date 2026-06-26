<!-- source: https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors -->

# When to use desktop and web connectors

April 15, 2026

Claude can connect to your tools in two ways: through the web (remote connectors) or through the Claude Desktop app (desktop extensions). Most connectors are remote—they're the default choice and work everywhere you use Claude.

# Use a remote connector when

* The tool is a cloud service you sign into (Slack, Notion, Linear, GitHub, your company's SaaS)
* You want the connector available everywhere—web, mobile, Cowork, Desktop, and Claude Code
* You're connecting something from the [Connectors Directory](https://claude.ai/directory)

Remote connectors work across all Claude surfaces. Once connected, they're available everywhere without extra setup.

# Use a desktop extension when

* The tool runs on your computer—local files, a database on localhost, a desktop application
* The tool needs OS-level access (filesystem, clipboard, local processes)
* There's no cloud version to connect to

Desktop extensions run locally and are only available in Claude Desktop and Claude Code—not on web or mobile.

# Plugins work with both

A plugin can bundle either remote or local MCP servers (or both). Installing a plugin that references a remote MCP makes it available everywhere; one that references a local MCP works in Desktop and Claude Code.

# Quick guide

|  |  |  |
| --- | --- | --- |
| Your tool is… | Use | Available on |
| A cloud/SaaS product | Remote connector | All surfaces |
| In the Connectors Directory | Remote connector | All surfaces |
| Running on your machine | Desktop extension | Desktop, Claude Code |
| A local file or folder | Desktop extension | Desktop, Claude Code |
| Something you built with a public URL | Remote connector (add as custom) | All surfaces |
| Something you built that runs locally | Desktop extension | Desktop, Claude Code |

# Get started

* Browse and add remote connectors: [Settings → Connectors](https://claude.ai/settings/connectors) or the [Connectors Directory](https://claude.ai/directory)
* Install a desktop extension: Open Claude Desktop → Settings → Extensions
* Building your own? See the [connector building docs](https://claude.com/docs/connectors/building) for remote connectors or the [MCPB guide](https://claude.com/docs/connectors/building/mcpb) for local ones.

[Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)[Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)[Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)[Deploying enterprise-grade MCP servers with desktop extensions](https://support.claude.com/en/articles/12702546-deploying-enterprise-grade-mcp-servers-with-desktop-extensions)[Use interactive connectors in Claude](https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude)
