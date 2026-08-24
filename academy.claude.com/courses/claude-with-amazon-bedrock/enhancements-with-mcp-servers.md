<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/enhancements-with-mcp-servers -->

Lesson 60 of 65 · Claude with Amazon BedrockEnhancements with MCP servers

Claude Code has an MCP client built right into it, which means you can connect MCP servers to dramatically expand its functionality. This opens up some really powerful possibilities for customizing your development workflow.

## How MCP Integration Works

The Model Context Protocol allows Claude Code to connect to external services through MCP servers. Each server can provide tools, prompts, and resources that extend what Claude can do.

![](https://academy.claude.com/assets/media/f6811880b277ed7bfb1a1d8680a08e31353b3de4f22b0114a964a98fc6582f76.png)

In this example, we'll connect Claude Code to a custom MCP server that provides a document conversion tool. This will let Claude read and convert PDF and Word documents to markdown format.

![](https://academy.claude.com/assets/media/0a249b24a1366e1ff3f1dfe3cb525d14f8453cc7f3f8d822304c53bf060ab5f2.png)

## Adding an MCP Server to Claude Code

Setting up an MCP server is straightforward. First, stop any running Claude Code session, then use the MCP add command:

bash

```
claude mcp add documents uv run main.py
```

This command takes two arguments:

* The server name (can be anything you want - "documents" in this case)
* The command to start your MCP server

After adding the server, restart Claude Code and it will automatically connect to your MCP server.

## Testing the Integration

Once connected, Claude can use the tools provided by your MCP server. In our example, we can ask Claude to convert document files to markdown format, and it will automatically use the document conversion tool we created.

![](https://academy.claude.com/assets/media/84fd59d8fe1fdec90ff03bf48b1f850a449680ad1e7c97b6b2d0716e8343e3b8.png)

The tool successfully converts the document content, showing how MCP servers can add entirely new capabilities to Claude Code.

## Popular MCP Servers for Development

There are many existing MCP servers that can enhance your development workflow:

![](https://academy.claude.com/assets/media/e1fbfe9fdc0157c977156bc860ad86a16a82c1467c3135021efb0b90b9bff540.png)

* **sentry-mcp** - Automatically discover and fix bugs logged in Sentry
* **playwright-mcp** - Gives Claude browser automation capabilities for testing and troubleshooting
* **figma-context-mcp** - Exposes Figma designs to Claude
* **mcp-atlassian** - Allows Claude to access Confluence and Jira
* **firecrawl-mcp-server** - Adds web scraping capabilities to Claude
* **slack-mcp** - Allows Claude to post messages or reply to specific threads

## Building Your Custom Workflow

The real power comes from combining multiple MCP servers that match your specific development needs. For example, you might set up:

* A Sentry server to fetch production error details
* A Jira server to read ticket requirements
* A Slack server to notify your team when work is complete
* Custom servers for your specific tools and processes

This flexibility makes Claude Code incredibly adaptable to different development environments and workflows. Take some time to think about which external services and tools you use regularly - there's likely an MCP server that can integrate them with Claude Code.
