<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/introducing-mcp -->

Lesson 48 of 65 · Claude with Amazon BedrockIntroducing MCP

Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Instead of building every tool function yourself, MCP shifts that burden to specialized servers that handle the heavy lifting.

![](https://academy.claude.com/assets/media/756f4e95014aed5979d5f87c2da8ea56b75c516a1e6879becbf224de8c1c4803.png)

When you first encounter MCP, you'll see diagrams showing the basic architecture: an MCP Client (your server) connects to MCP Servers that contain tools, prompts, and resources. Each MCP Server acts as an interface to outside services like GitHub, AWS, or databases.

## The Problem MCP Solves

Let's say you're building a chat interface where users can ask Claude about their GitHub data - questions like "What open pull requests are there across all my repositories?" To handle this without MCP, you'd need to create tools for every GitHub operation you want to support.

![](https://academy.claude.com/assets/media/5148da8be952ac4f34dff0ecef9640cadcb7f14a249ac7890445fcda84dd6a81.png)

GitHub has massive functionality - repositories, pull requests, issues, projects, and much more. Building a complete GitHub integration means authoring an incredible number of tool schemas and functions:

![](https://academy.claude.com/assets/media/8a56e2bfc0864037ea772066e4ebe028a9b70455fcf69753f162234bc0791b30.png)

This creates a lot of code that you have to write, test, and maintain. That's where MCP comes in.

## How MCP Works

MCP shifts the burden of tool definitions and execution from your server to dedicated MCP Servers. Instead of writing all those GitHub tools yourself, you connect to a GitHub MCP Server that already has them implemented.

![](https://academy.claude.com/assets/media/4ae6049ccbd84c2451d768fc2bda25d2352d406e28e01124efe63d1339f26b62.png)

The MCP Server acts as a wrapper around the outside service, providing pre-built tools that Claude can use. You get access to all that GitHub functionality without writing any of the integration code yourself.

![](https://academy.claude.com/assets/media/6007c0bb43df548f5718d979f8f3edf520d95cd5d9cd10924de5c1d115d0a274.png)

## Common Questions

### Who authors MCP Servers?

Anyone can create an MCP Server implementation. Often, service providers themselves will make their own official implementations. For example, AWS might release an official MCP Server with tools for their various services.

### How is this different from calling APIs directly?

When you call a service's API directly, you still have to write the tool schemas and function implementations yourself. MCP Servers provide those tool schemas and functions already defined for you, saving you development time.

![](https://academy.claude.com/assets/media/69d10ad78e4bc7d024d6956b7dd7ddab90e68b004434f998c62d4e5a5fbc3da9.png)

### Isn't MCP just the same as tool use?

This is a common misconception. MCP Servers and tool use are complementary but different concepts. Tool use is about Claude calling functions to accomplish tasks. MCP is about who provides those functions - instead of you writing them, someone else has already implemented them in an MCP Server.

The key insight is that MCP Servers provide tool schemas and functions already defined for you, while direct tool use requires you to author everything yourself. Both involve Claude using tools, but MCP dramatically reduces the development work required on your end.
