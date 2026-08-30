<!-- source: https://academy.claude.com/courses/model-context-protocol-advanced-topics/streamablehttp-in-depth -->

Lesson 10 of 11 · Model Context Protocol: Advanced TopicsStreamableHTTP in depth

3. /[Model Context Protocol: Advanced Topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics)

[Model Context Protocol: Advanced Topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics)

# StreamableHTTP in depth

Lesson 102 min

StreamableHTTP is MCP's solution to a fundamental problem: some MCP functionality requires the server to make requests to the client, but HTTP makes this challenging. Let's explore how StreamableHTTP works around this limitation and when you might need to break that workaround.

## The Core Problem[](#the-core-problem)

Some MCP features like sampling, notifications, and logging rely on the server initiating requests to the client. However, HTTP is designed for clients to make requests to servers, not the other way around. StreamableHTTP solves this with a clever workaround using Server-Sent Events (SSE).

## How StreamableHTTP Works[](#how-streamablehttp-works)

The magic happens through a multi-step process that establishes persistent connections between client and server.

![](https://academy.claude.com/assets/media/672d7ee890f7d2e488ee062732d8008b8078bff2b894368a541d09a88be1cdbf.png)

### Initial Connection Setup[](#initial-connection-setup)

The process starts like any MCP connection:

* Client sends an `Initialize Request` to the server
* Server responds with an `Initialize Result` that includes a special `mcp-session-id` header
* Client sends an `Initialized Notification` with the session ID

This session ID is crucial - it uniquely identifies the client and must be included in all future requests.

### The SSE Workaround[](#the-sse-workaround)

After initialization, the client can make a GET request to establish a Server-Sent Events connection. This creates a long-lived HTTP response that the server can use to stream messages back to the client at any time.

![](https://academy.claude.com/assets/media/1de391510a4e8d81ff4ffe1c2d5c6fb6fec62feb30774c185761940f89fa40bd.png)

This SSE connection is the key to allowing server-to-client communication. The server can now send requests, notifications, and other messages through this persistent channel.

## Tool Calls and Dual SSE Connections[](#tool-calls-and-dual-sse-connections)

When the client makes a tool call, things get more complex. The system creates two separate SSE connections:

![](https://academy.claude.com/assets/media/bc825054ffd31454af897765d4cb2449c4470ad2353473fb03a5e2939734f32c.png)

* **Primary SSE Connection:** Used for server-initiated requests and stays open indefinitely
* **Tool-Specific SSE Connection:** Created for each tool call and closes automatically when the tool result is sent

### Message Routing[](#message-routing)

Different types of messages get routed through different connections:

* **Progress notifications:** Sent through the primary SSE connection
* **Logging messages and tool results:** Sent through the tool-specific SSE connection

![](https://academy.claude.com/assets/media/857a3d847a1d27824d158e7c882db0524ea37819fe699d6c252317a92b9f57fb.png)

## Configuration Flags That Break the Workaround[](#configuration-flags-that-break-the-workaround)

StreamableHTTP includes two important configuration options:

* `stateless_http`
* `json_response`

Setting these to `True` can break the SSE workaround mechanism. You might want to enable these flags in certain scenarios, but doing so limits the full MCP functionality that depends on server-to-client communication.

## Key Takeaways[](#key-takeaways)

StreamableHTTP is more complex than other MCP transports because it has to work around HTTP's limitations. The SSE-based workaround enables full MCP functionality over HTTP, but understanding the dual-connection model is crucial for debugging and optimization.

When building MCP applications with StreamableHTTP, remember that session IDs are required for all requests after initialization, and the system automatically manages multiple SSE connections to handle different types of server-to-client communication.

[Previous lessonThe StreamableHTTP transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-streamablehttp-transport)[Next lessonState and the StreamableHTTP transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/state-and-the-streamablehttp-transport)

Lesson 10 of 11 · Model Context Protocol: Advanced TopicsStreamableHTTP in depth

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

* [The Core Problem](#the-core-problem)
* [How StreamableHTTP Works](#how-streamablehttp-works)
* [Tool Calls and Dual SSE Connections](#tool-calls-and-dual-sse-connections)
* [Configuration Flags That Break the Workaround](#configuration-flags-that-break-the-workaround)
* [Key Takeaways](#key-takeaways)
