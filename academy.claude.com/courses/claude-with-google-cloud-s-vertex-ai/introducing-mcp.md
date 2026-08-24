<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/introducing-mcp -->

Lesson 49 of 66 · Claude with Google Cloud's Vertex AIIntroducing MCP

Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Instead of building every tool function yourself, MCP shifts that burden to specialized servers that handle the heavy lifting.

![](https://academy.claude.com/assets/media/756f4e95014aed5979d5f87c2da8ea56b75c516a1e6879becbf224de8c1c4803.png)

When you first encounter MCP, you'll see diagrams showing the basic architecture: an MCP Client (your server) connects to MCP Servers that contain tools, prompts, and resources. Each MCP Server acts as an interface to outside services like GitHub, AWS, or databases.

## The Problem MCP Solves

Let's say you're building a chat interface where users can ask Claude about their GitHub data. A user might ask "What open pull requests are there across all my repositories?" To answer this, Claude needs tools that can access GitHub's API.

![](https://academy.claude.com/assets/media/5148da8be952ac4f34dff0ecef9640cadcb7f14a249ac7890445fcda84dd6a81.png)

GitHub has massive functionality - repositories, pull requests, issues, projects, and much more. To handle all of GitHub's features, you'd need to create an incredible number of tool schemas and functions:

![](https://academy.claude.com/assets/media/8a56e2bfc0864037ea772066e4ebe028a9b70455fcf69753f162234bc0791b30.png)

This means writing, testing, and maintaining a lot of code for functions like:

* `get_repos()`
* `list_repos()`
* `create_repos()`
* `search_issues()`
* `update_issue()`
* `create_issue()`
* `get_issue()`
* `create_file()`

## How MCP Changes This

MCP shifts the burden of tool definitions and execution from your server to MCP Servers. Instead of you writing all those GitHub integration tools, someone else creates an MCP Server for GitHub that contains all the necessary tools and functions.

![](https://academy.claude.com/assets/media/4ae6049ccbd84c2451d768fc2bda25d2352d406e28e01124efe63d1339f26b62.png)

The MCP Server acts as a wrapper around the outside service, providing pre-built tools that you can use immediately. Your server becomes an MCP Client that connects to these specialized servers.

![](https://academy.claude.com/assets/media/6007c0bb43df548f5718d979f8f3edf520d95cd5d9cd10924de5c1d115d0a274.png)

## Who Creates MCP Servers

Anyone can create an MCP Server implementation. Often, service providers themselves will create official MCP implementations. For example, AWS might release their own official MCP Server with tools for their various services.

You can also create your own MCP Server to wrap access to any service you need to integrate with.

## Common Questions

![](https://academy.claude.com/assets/media/69d10ad78e4bc7d024d6956b7dd7ddab90e68b004434f998c62d4e5a5fbc3da9.png)

**How is using an MCP Server different from calling a service's API directly?**

MCP Servers provide tool schemas and functions already defined for you. If you call an API directly, you'll be writing those tool definitions yourself. MCP saves you that implementation work.

**Aren't MCP Servers and tool use the same thing?**

This is a common misconception. MCP Servers and tool use are complementary but different concepts. MCP Servers provide pre-built tool schemas and functions, while tool use is about how Claude actually calls those tools. MCP is really about who does the work of creating and maintaining the tool implementations.

The key benefit is that MCP Servers give you access to sophisticated integrations without having to build and maintain all that code yourself. You get the power of tool use with much less development overhead.
