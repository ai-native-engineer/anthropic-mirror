<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/introducing-mcp -->

Lesson 47 of 67 · Building with the Claude APIIntroducing MCP

Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Think of it as a way to shift the burden of tool definitions and execution away from your server to specialized MCP servers.

![](https://academy.claude.com/assets/media/67a3dc4f3b47c72a974af9fb82c5edaeb37bf4c2107cc64e29446f0442c92a17.jpg)

When you first encounter MCP, you'll see diagrams showing the basic architecture: an MCP Client (your server) connecting to MCP Servers that contain tools, prompts, and resources. Each MCP server acts as an interface to some outside service.

## Understanding MCP Through a Real Example

Let's say you're building a chat interface where users can ask Claude about their GitHub data. A user might ask "What open pull requests are there across all my repositories?" To answer this, Claude needs tools to access GitHub's API.

![](https://academy.claude.com/assets/media/ec4cb615cb147904fb138deaf8beb3ddf64f305dafa05a1f636da5871269c076.jpg)

Without MCP, you'd need to create all the GitHub integration tools yourself. This means writing schemas and functions for every piece of GitHub functionality you want to support.

## The Tool Function Problem

GitHub has massive functionality - repositories, pull requests, issues, projects, and much more. To build a complete GitHub chatbot, you'd need to author an incredible number of tools:

![](https://academy.claude.com/assets/media/fb120ae3e674367b0e6fd0c8d7fc730344b9b6e0979537a1312c3ad8d609b7fc.jpg)

Each tool requires both a schema definition and a function implementation. This represents a lot of code that you have to write, test, and maintain as a developer.

## How MCP Solves This

MCP shifts the burden of tool definitions and execution from your server to MCP servers. Instead of you writing all those GitHub tools, they're authored and executed inside a dedicated MCP server.

![](https://academy.claude.com/assets/media/4575f8cefd76631fd1629fa2a56f94fbc052b26c29f9df86e36d2f599a5daf68.jpg)

The MCP server acts as a wrapper around GitHub's functionality, providing pre-built tools that you can use without having to implement them yourself.

![](https://academy.claude.com/assets/media/ed302c0ffd32a43180f012372029b6220ad4563cd36214f3077cc29d45b7a06f.jpg)

MCP servers provide access to data or functionality implemented by outside services. They package up complex integrations into reusable components that any application can connect to.

## Common Questions About MCP

![](https://academy.claude.com/assets/media/8f732f327ed47e73d82dcc2c4056fa8e2b7c923c60a9dab0d1992113af222e5f.jpg)

### Who Authors MCP Servers?

Anyone can create an MCP server implementation. Often, service providers themselves will make their own official MCP implementations. For example, AWS might release an official MCP server with tools for their various services.

### How is MCP Different from Direct API Calls?

MCP servers provide tool schemas and functions already defined for you. If you call an API directly, you're responsible for authoring those tool definitions yourself. MCP saves you that implementation work.

### Isn't MCP Just Tool Use?

This is a common misconception. MCP servers and tool use are complementary but different concepts. MCP is about who does the work of creating and maintaining the tools. With MCP, someone else has already written the tool functions and schemas for you - they're packaged inside the MCP server.

The key insight is that MCP servers provide tool schemas and functions already defined for you, eliminating the need to build and maintain complex integrations yourself.
