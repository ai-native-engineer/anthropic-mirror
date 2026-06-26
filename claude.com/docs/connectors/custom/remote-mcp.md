<!-- source: https://claude.com/docs/connectors/custom/remote-mcp -->

Custom connectors enable you to link Claude directly to your essential tools and data sources using the Model Context Protocol (MCP).

##  What are third party connectors?

Custom connectors allow Claude to operate within your preferred software and leverage comprehensive context from your external tools.
You can:

* Connect Claude to existing remote MCP servers
* Build your own remote MCP servers for any tool

###  Finding connectors

Browse the [Connectors Directory](/docs/connectors/directory) to discover verified and reviewed third-party MCP servers that are ready to use across all Claude products.

##  Adding custom connectors

You can manually add any third-party connector to Claude as long as you have the URL of that remote MCP server.

**Security Notice**: Custom connectors allow connections to unverified services. Claude can access and perform actions within these services, so review security considerations carefully.

###  For Team and Enterprise plans

**Owners must:**

1. Navigate to **Admin settings > Connectors**
2. Click “Add custom connector”
3. Enter the remote MCP server URL
4. Optionally configure OAuth Client ID/Secret in Advanced settings
5. Click “Add”

**Members then:**

1. Go to **Settings > Connectors**
2. Find the connector with “Custom” label
3. Click “Connect” to authenticate

###  For Free, Pro, and Max plans

1. Navigate to **Settings > Connectors**
2. Click “Add custom connector”
3. Enter the remote MCP server URL
4. Optionally configure OAuth credentials
5. Click “Add”

###  Enabling connectors in chat

Use the ”+” button in your chat interface to access “Connectors,” where you can enable/disable connectors per conversation.

##  Managing connectors

To remove or edit connectors:

1. Go to **Settings > Connectors**
2. Click “Remove” or select the three-dot menu
3. Follow prompts to edit or remove

##  Security and privacy

###  Best practices

* Only connect to servers from trusted organizations
* Carefully review requested permission scopes during authentication
* Be aware of prompt injection risks; Claude has built-in protections
* Monitor for unexpected changes in tool behavior

###  Tool actions

Remote MCP servers enable Claude to invoke tools that can:

* Read data from applications
* Create, modify, or delete data
* Take actions on your behalf

**Usage guidelines:**

* Monitor Claude’s actions for unintended effects
* Review tool approval requests carefully
* Only click “Allow always” for trusted servers
* Disable irrelevant tools via the “Search and tools” menu

##  Reporting issues

Report malicious MCP servers to [Anthropic’s Bug Bounty Program](https://www.anthropic.com/responsible-disclosure-policy).

##  Related topics

## Building Connectors

Learn to build your own MCP servers.

## Connectors Directory

Browse pre-built connectors.

## MCP Overview

Understand the Model Context Protocol.

## Desktop Extensions

Deploy enterprise-grade MCP servers.

## MCP in Claude Code

Add the same server to Claude Code from the command line.

[Connectors directory](/docs/connectors/directory)[Desktop extensions](/docs/connectors/custom/desktop-extensions)
