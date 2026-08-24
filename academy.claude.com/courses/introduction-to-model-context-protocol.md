<!-- source: https://academy.claude.com/courses/introduction-to-model-context-protocol -->

10 lessons · 1 quizIntroduction to Model Context Protocol

What you’ll learnBy the end of this course, you’ll be able to

* Understand MCP architecture and how it shifts tool definition and execution burden from your server to specialized MCP servers
* Learn about MCP's transport-agnostic communication system and the message types used between clients and servers
* Explore the complete request-response flow from user queries through MCP clients to external services and back to Claude
* Build MCP servers using the Python SDK with decorators to define tools instead of writing JSON schemas manually
* Implement document management functionality with tools for reading and editing documents using Field descriptions and type hints
* Use the built-in MCP Server Inspector to test and debug your server functionality in a browser-based interface
* Define resources for exposing read-only data, including both direct resources with static URIs and templated resources with parameters
* Implement resource reading functionality in clients with proper MIME type handling for JSON and text content
* Build prompts that provide pre-crafted, high-quality instructions for common workflows like document formatting
* Understand when to use each MCP primitive: tools (model-controlled), resources (app-controlled), and prompts (user-controlled)
* Examine practical integration patterns including autocomplete functionality and context injection for AI conversations

Who it’s for

Engineers who want to integrate Claude with external tools and services without writing tons of boilerplate integration code

Before you start

* Basic Python programming experience
* Understanding of async/await patterns
* Familiarity with API concepts

This course covers MCP, a protocol for connecting Claude to external services and data sources without manually writing tool schemas. You'll learn to build both MCP servers that expose tools, resources, and prompts, and MCP clients that consume them. The course includes a hands-on project where you implement a document management system using MCP.

## Inside the course

### Introduction

2 lessons

Start with understanding MCP's architecture and why it exists.

![](https://academy.claude.com/assets/media/0685a333a949af8f486bb2fe0b1197e16226f0772059eaef4695cf4b76aaa724.webp)

### Hands-on with MCP servers

2 lessons

Build your first MCP server with tools using the Python SDK, then test it with the built-in inspector.

![](https://academy.claude.com/assets/media/080b011e78264adec3df18f48c30e0ebccf08df3a08e5f05b6e0984a96870828.webp)![](https://academy.claude.com/assets/media/56a99dc9e075adf0f948eac55e468a1dbfb9d7c9dcb2ec07ca28df80fa2d7fab.webp)

### Connecting with MCP clients

5 lessons

Build the client side to communicate with MCP servers. Implement resources for direct data access and prompts for pre-built instructions. See how everything connects in a complete application flow.

![](https://academy.claude.com/assets/media/dab6beb4f3d7107d4d58fad7377b71181f59f06b9963f24298e091de0970ef29.webp)![](https://academy.claude.com/assets/media/7f2c3edbff419b6eb06234f765fe32dfd78cd43658f0acc1774181d4a177925b.webp)![](https://academy.claude.com/assets/media/9df2e6209c2c2dd711504b031f5897027fc88d7c682160cc5fe85221cd85792c.webp)
