<!-- source: https://academy.claude.com/courses/model-context-protocol-advanced-topics/json-message-types -->

Lesson 7 of 11 · Model Context Protocol: Advanced TopicsJSON message types

3. /[Model Context Protocol: Advanced Topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics)

[Model Context Protocol: Advanced Topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics)

# JSON message types

Lesson 72 min

MCP (Model Context Protocol) uses JSON messages to handle communication between clients and servers. Understanding these message types is crucial for working with MCP, especially when dealing with different transport methods like the streamable HTTP transport.

## Message Format

All MCP communication happens through JSON messages. Each message type serves a specific purpose - whether it's calling a tool, listing available resources, or sending notifications about system events.

![](https://academy.claude.com/assets/media/ebaf35d65cc22155c2737dcd9eda65cf974aacd5ec5ba2ce0f00dd50c28ca8e0.png)

Here's a typical example: when Claude needs to call a tool provided by an MCP server, the client sends a "Call Tool Request" message. The server processes this request, runs the tool, and responds with a "Call Tool Result" message containing the output.

![](https://academy.claude.com/assets/media/3e75ce9b60eb0c890a6cd94cf6a2d26e8fb616344d16fdac0a83d8bd7d74ab52.png)

## MCP Specification

The complete list of message types is defined in the official MCP specification repository on GitHub. This specification is separate from the various SDK repositories (like Python or TypeScript SDKs) and serves as the authoritative source for how MCP should work.

The message types are written in TypeScript for convenience - not because they're executed as TypeScript code, but because TypeScript provides a clear way to describe data structures and types.

## Message Categories

MCP messages fall into two main categories:

![](https://academy.claude.com/assets/media/7cc6ab727a5d1a61841a0018791df5aa4f6c6e87467fc1010b0585b3ac696483.png)

### Request-Result Messages

These messages always come in pairs. You send a request and expect to get a result back:

* **Call Tool Request** → **Call Tool Result**
* **List Prompts Request → List Prompts Result**
* **Read Resource Request → Read Resource Result**
* **Initialize Request → Initialize Result**

### Notification Messages

These are one-way messages that inform about events but don't require a response:

* **Progress Notification** - Updates on long-running operations
* **Logging Message Notification** - System log messages
* **Tool List Changed Notification** - When available tools change
* **Resource Updated Notification** - When resources are modified

## Client vs Server Messages

The MCP specification organizes messages by who sends them:

**Client messages** include requests that clients send to servers (like tool calls) and notifications that clients might send.

**Server messages** include requests that servers send to clients and notifications that servers broadcast.

## Why This Matters

Understanding that servers can send messages to clients is particularly important when working with different transport methods. Some transports, like the streamable HTTP transport, have limitations on which types of messages can flow in which directions.

The key insight is that MCP is designed as a bidirectional protocol - both clients and servers can initiate communication. This becomes crucial when you need to choose the right transport method for your specific use case.

[Previous lessonRoots walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/roots-walkthrough)[Next lessonThe STDIO transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-stdio-transport)

Lesson 7 of 11 · Model Context Protocol: Advanced TopicsJSON message types

Core MCP features

* [Sampling](https://academy.claude.com/courses/model-context-protocol-advanced-topics/sampling)
* [Sampling walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/sampling-walkthrough)
* [Log and progress notifications](https://academy.claude.com/courses/model-context-protocol-advanced-topics/log-and-progress-notifications)
* [Notifications walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/notifications-walkthrough)
* [Roots](https://academy.claude.com/courses/model-context-protocol-advanced-topics/roots)
* [Roots walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/roots-walkthrough)

Transports and communication

* [JSON message types](https://academy.claude.com/courses/model-context-protocol-advanced-topics/json-message-types)
* [The STDIO transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-stdio-transport)
* [The StreamableHTTP transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-streamablehttp-transport)
* [StreamableHTTP in depth](https://academy.claude.com/courses/model-context-protocol-advanced-topics/streamablehttp-in-depth)
* [State and the StreamableHTTP transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/state-and-the-streamablehttp-transport)

Assessment and next steps

* [Assessment on MCP conceptsQuiz](https://academy.claude.com/courses/model-context-protocol-advanced-topics/assessment-on-mcp-concepts)

* [Completion badge](https://academy.claude.com/courses/model-context-protocol-advanced-topics/badge)

* [Message Format](#message-format)
* [MCP Specification](#mcp-specification)
* [Message Categories](#message-categories)
* [Client vs Server Messages](#client-vs-server-messages)
* [Why This Matters](#why-this-matters)
