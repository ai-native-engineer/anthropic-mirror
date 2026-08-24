<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/enhancements-with-mcp-servers -->

Lesson 60 of 67 · Building with the Claude APIEnhancements with MCP servers

Claude Code has an MCP client built right into it, which means you can connect MCP servers to dramatically expand what Claude can do. This opens up some really powerful possibilities for customizing your development workflow.

## How MCP Extends Claude

The Model Context Protocol allows Claude Code to connect to external services and tools through MCP servers. Instead of being limited to Claude's built-in capabilities, you can add custom functionality by connecting servers that provide specific tools, resources, or integrations.

![](https://academy.claude.com/assets/media/c7d903c092a62340a1e9c36abc2c3f5f317356fbb499f42dd3958547285b9ab3.jpg)

Each MCP server can expose different types of functionality to Claude through three main components: Tools (for taking actions), Prompts (for templates), and Resources (for accessing data).

## Setting Up an MCP Server

Adding an MCP server to Claude Code is straightforward. You use the command line to register your server:

bash

```
claude mcp add [server-name] [command-to-start-server]
```

For example, if you have a document processing server that starts with `uv run main.py`, you'd run:

bash

```
claude mcp add documents uv run main.py
```

Once registered, Claude Code will automatically connect to your server when it starts up.

## Example: Document Processing

A practical example is creating a tool that lets Claude read PDF and Word documents. By building an MCP server with a "document\_path\_to\_markdown" tool, you can ask Claude to convert document contents to markdown format.

![](https://academy.claude.com/assets/media/5d7db0b4cc0fa80349a1beb409118e8f25f26dd3b00c205dd4b7aa7efc365570.jpg)

When you ask Claude to "Convert the tests/fixtures/mcp\_docs.docx file to markdown", it will automatically use your custom tool to read the document and return the converted content.

![](https://academy.claude.com/assets/media/e24f0d96487a127d94ed519aea57e010b3ba629cf9c85e3d305bcc7160e36646.jpg)

## Popular MCP Integrations

The MCP ecosystem includes servers for many common development tools and services:

![](https://academy.claude.com/assets/media/2f33a85e6b8751b88d028085e29ede0a0894cb36a5d02e7e0175e55477336f02.jpg)

* **sentry-mcp** - Automatically discover and fix bugs logged in Sentry
* **playwright-mcp** - Gives Claude browser automation capabilities for testing and troubleshooting
* **figma-context-mcp** - Exposes Figma designs to Claude
* **mcp-atlassian** - Allows Claude to access Confluence and Jira
* **firecrawl-mcp-server** - Adds web scraping capabilities to Claude
* **slack-mcp** - Allows Claude to post messages or reply to specific threads

## Building Your Development Workflow

The real power comes from combining multiple MCP servers that match your specific development process. You might set up:

* A Sentry server to fetch production error details
* A Jira server to read ticket requirements
* A Slack server to notify your team when work is complete
* Custom servers for your internal tools and APIs

This creates a development environment where Claude can seamlessly work with all the tools and services you already use, making it a much more powerful coding assistant tailored to your specific workflow.
