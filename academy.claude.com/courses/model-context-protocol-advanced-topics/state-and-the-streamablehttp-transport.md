<!-- source: https://academy.claude.com/courses/model-context-protocol-advanced-topics/state-and-the-streamablehttp-transport -->

Lesson 11 of 11 · Model Context Protocol: Advanced TopicsState and the StreamableHTTP transport

3. /[Model Context Protocol: Advanced Topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics)

[Model Context Protocol: Advanced Topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics)

# State and the StreamableHTTP transport

Lesson 112 min

The `stateless_http` and `json_response` flags in MCP servers control fundamental aspects of how your server behaves. Understanding when and why to use them is crucial, especially if you're planning to scale your server or deploy it in production.

## When You Need Stateless HTTP

Imagine you build an MCP server that becomes popular. Initially, you might have just a few clients connecting to a single server instance:

![](https://academy.claude.com/assets/media/d376b529089d3d3e0886cd907fcb7b7087fe871a9d3edcc6f962f1f0d8be9592.png)

As your server grows, you might have thousands of clients trying to connect. Running a single server instance won't scale to handle all that traffic:

![](https://academy.claude.com/assets/media/88f8b947de6b9cb531701bbac11cd8906fd3ad50bb66a094323ab0682439fa3b.png)

The typical solution is horizontal scaling - running multiple server instances behind a load balancer:

![](https://academy.claude.com/assets/media/036078bb89586b9d4de699ed6fceda9ce3c80aab728cc167db0e9c7958ebaf05.png)

But here's where things get complicated. Remember that MCP clients need two separate connections:

* A GET SSE connection for receiving server-to-client requests
* POST requests for calling tools and receiving responses

![](https://academy.claude.com/assets/media/8a2bab206daccb2d03c12a16e4a9e5ac6dc27c72a46c7d7cd4385ac8738f5f0e.png)

With a load balancer, these requests might get routed to different server instances. If your tool needs to use Claude (through sampling), the server handling the POST request would need to coordinate with the server handling the GET SSE connection. This creates a complex coordination problem between servers.

![](https://academy.claude.com/assets/media/b92d21851ccfc52b59ec99b9d493a82beb562369a934a9ae78b8643d73bb9325.png)

## How Stateless HTTP Solves This

Setting `stateless_http=True` eliminates this coordination problem, but with significant trade-offs:

![](https://academy.claude.com/assets/media/602d481b3eb2cd00ffe8969ef1d88e489e6714d2ca814b8dbcc7f4303d0dc008.png)

When stateless HTTP is enabled:

* **Clients don't get session IDs** - the server can't track individual clients
* **No server-to-client requests** - the GET SSE pathway becomes unavailable
* **No sampling** - can't use Claude or other AI models
* **No progress reports** - can't send progress updates during long operations
* **No subscriptions** - can't notify clients about resource updates

However, there's one benefit: **client initialization is no longer required**. Clients can make requests directly without the initial handshake process.

![](https://academy.claude.com/assets/media/685167d8dee5bd3aa4196febf9063335586d8d0b5c72bb8745d8f5d24ff09971.png)

## Understanding JSON Response

The `json_response=True` flag is simpler - it just disables streaming for POST request responses. Instead of getting multiple SSE messages as a tool executes, you get only the final result as plain JSON.

With streaming disabled:

* No intermediate progress messages
* No log statements during execution
* Just the final tool result

## When to Use These Flags

**Use stateless HTTP when:**

* You need horizontal scaling with load balancers
* You don't need server-to-client communication
* Your tools don't require AI model sampling
* You want to minimize connection overhead

**Use JSON response when:**

* You don't need streaming responses
* You prefer simpler, non-streaming HTTP responses
* You're integrating with systems that expect plain JSON

## Development vs Production

If you're developing locally with standard I/O transport but planning to deploy with HTTP transport, test with the same transport you'll use in production. The behavior differences between stateful and stateless modes can be significant, and it's better to catch any issues during development rather than after deployment.

These flags fundamentally change how your MCP server operates, so choose them based on your specific scaling and functionality requirements.

[Previous lessonStreamableHTTP in depth](https://academy.claude.com/courses/model-context-protocol-advanced-topics/streamablehttp-in-depth)[Next lessonAssessment on MCP concepts](https://academy.claude.com/courses/model-context-protocol-advanced-topics/assessment-on-mcp-concepts)

Lesson 11 of 11 · Model Context Protocol: Advanced TopicsState and the StreamableHTTP transport

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

* [When You Need Stateless HTTP](#when-you-need-stateless-http)
* [How Stateless HTTP Solves This](#how-stateless-http-solves-this)
* [Understanding JSON Response](#understanding-json-response)
* [When to Use These Flags](#when-to-use-these-flags)
* [Development vs Production](#development-vs-production)
