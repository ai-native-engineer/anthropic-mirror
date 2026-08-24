<!-- source: https://academy.claude.com/courses/introduction-to-model-context-protocol/introducing-mcp -->

Lesson 1 of 10 · Introduction to Model Context ProtocolIntroducing MCP

3. /[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

# Introducing MCP

Lesson 12 min

Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Think of it as a way to shift the burden of tool definitions and execution away from your server to specialized MCP servers.

![](https://academy.claude.com/assets/media/756f4e95014aed5979d5f87c2da8ea56b75c516a1e6879becbf224de8c1c4803.png)

When you first encounter MCP, you'll see diagrams showing the basic architecture: an MCP Client (your server) connecting to MCP Servers that contain tools, prompts, and resources. Each MCP Server acts as an interface to some outside service.

## The Problem MCP Solves

Let's say you're building a chat interface where users can ask Claude about their GitHub data. A user might ask "What open pull requests are there across all my repositories?" To handle this, Claude needs tools to access GitHub's API.

![](https://academy.claude.com/assets/media/5148da8be952ac4f34dff0ecef9640cadcb7f14a249ac7890445fcda84dd6a81.png)

GitHub has massive functionality - repositories, pull requests, issues, projects, and tons more. Without MCP, you'd need to create an incredible number of tool schemas and functions to handle all of GitHub's features.

![](https://academy.claude.com/assets/media/8a56e2bfc0864037ea772066e4ebe028a9b70455fcf69753f162234bc0791b30.png)

This means writing, testing, and maintaining all that integration code yourself. That's a lot of effort and ongoing maintenance burden.

## How MCP Works

MCP shifts this burden by moving tool definitions and execution from your server to dedicated MCP servers. Instead of you authoring all those GitHub tools, an MCP Server for GitHub handles it.

![](https://academy.claude.com/assets/media/4ae6049ccbd84c2451d768fc2bda25d2352d406e28e01124efe63d1339f26b62.png)

The MCP Server wraps up tons of functionality around GitHub and exposes it as a standardized set of tools. Your application connects to this MCP server instead of implementing everything from scratch.

## MCP Servers Explained

MCP Servers provide access to data or functionality implemented by outside services. They act as specialized interfaces that expose tools, prompts, and resources in a standardized way.

![](https://academy.claude.com/assets/media/6007c0bb43df548f5718d979f8f3edf520d95cd5d9cd10924de5c1d115d0a274.png)

In our GitHub example, the MCP Server for GitHub contains tools like `get_repos()` and connects directly to GitHub's API. Your server communicates with the MCP server, which handles all the GitHub-specific implementation details.

## Common Questions

### Who authors MCP Servers?

Anyone can create an MCP server implementation. Often, service providers themselves will make their own official MCP implementations. For example, AWS might release an official MCP server with tools for their various services.

### How is this different from calling APIs directly?

MCP servers provide tool schemas and functions already defined for you. If you want to call an API directly, you'll be authoring those tool definitions on your own. MCP saves you that implementation work.

### Isn't MCP just the same as tool use?

This is a common misconception. MCP servers and tool use are complementary but different concepts. MCP servers provide tool schemas and functions already defined for you, while tool use is about how Claude actually calls those tools. The key difference is who does the work - with MCP, someone else has already implemented the tools for you.

The benefit is clear: instead of maintaining a complex set of integrations yourself, you can leverage MCP servers that handle the heavy lifting of connecting to external services.

[Next lessonMCP clients](https://academy.claude.com/courses/introduction-to-model-context-protocol/mcp-clients)

Lesson 1 of 10 · Introduction to Model Context ProtocolIntroducing MCP

Introduction

* [Introducing MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol/introducing-mcp)
* [MCP clients](https://academy.claude.com/courses/introduction-to-model-context-protocol/mcp-clients)

Hands-on with MCP servers

* [Defining tools with MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-tools-with-mcp)
* [The server inspector](https://academy.claude.com/courses/introduction-to-model-context-protocol/the-server-inspector)

Connecting with MCP clients

* [Implementing a client](https://academy.claude.com/courses/introduction-to-model-context-protocol/implementing-a-client)
* [Defining resources](https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-resources)
* [Accessing resources](https://academy.claude.com/courses/introduction-to-model-context-protocol/accessing-resources)
* [Defining prompts](https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-prompts)
* [Prompts in the client](https://academy.claude.com/courses/introduction-to-model-context-protocol/prompts-in-the-client)

Assessment and wrap Up

* [Final assessment on MCPQuiz](https://academy.claude.com/courses/introduction-to-model-context-protocol/final-assessment-on-mcp)
* [MCP review](https://academy.claude.com/courses/introduction-to-model-context-protocol/mcp-review)

* [Completion badge](https://academy.claude.com/courses/introduction-to-model-context-protocol/badge)

* [The Problem MCP Solves](#the-problem-mcp-solves)
* [How MCP Works](#how-mcp-works)
* [MCP Servers Explained](#mcp-servers-explained)
* [Common Questions](#common-questions)
