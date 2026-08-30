<!-- source: https://academy.claude.com/courses/introduction-to-model-context-protocol/mcp-clients -->

Lesson 2 of 10 · Introduction to Model Context ProtocolMCP clients

3. /[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

# MCP clients

Lesson 22 min

The MCP client serves as the communication bridge between your server and MCP servers. It's your access point to all the tools that an MCP server provides, handling the message exchange and protocol details so your application doesn't have to.

## Transport Agnostic Communication[](#transport-agnostic-communication)

One of MCP's key strengths is being transport agnostic - a fancy way of saying the client and server can communicate over different protocols depending on your setup.

![](https://academy.claude.com/assets/media/b393bf3821c37b06d31300b588c291caa460db51353ebbfbc6a56b9c2a2c0160.png)

The most common setup runs both the MCP client and server on the same machine, communicating through standard input/output. But you can also connect them over:

* HTTP
* WebSockets
* Various other network protocols

![](https://academy.claude.com/assets/media/3a63d189484fd713cdaa1932e5b9638da2b20059ce414c288f77d915371b5f5c.png)

## MCP Message Types[](#mcp-message-types)

Once connected, the client and server exchange specific message types defined in the MCP specification. The main ones you'll work with are:

![](https://academy.claude.com/assets/media/4dbfe70297791ff32dced94d745d416ec7ec8c5889d3cbd45ef3328bbdb7f755.png)

**ListToolsRequest/ListToolsResult:** The client asks the server "what tools do you provide?" and gets back a list of available tools.

![](https://academy.claude.com/assets/media/b94c5c441b196cce093af43405bb70be67728aeee37f7a526f6a022ce53e0ffe.png)

**CallToolRequest/CallToolResult:** The client asks the server to run a specific tool with given arguments, then receives the results.

## How It All Works Together[](#how-it-all-works-together)

Here's a complete example showing how a user query flows through the entire system - from your server, through the MCP client, to external services like GitHub, and back to Claude.

Let's say a user asks "What repositories do I have?" Here's the step-by-step flow:

1. **User Query:** The user submits their question to your server
2. **Tool Discovery:** Your server needs to know what tools are available to send to Claude
3. **List Tools Exchange:** Your server asks the MCP client for available tools
4. **MCP Communication:** The MCP client sends a `ListToolsRequest` to the MCP server and receives a `ListToolsResult`
5. **Claude Request:** Your server sends the user's query plus the available tools to Claude
6. **Tool Use Decision:** Claude decides it needs to call a tool to answer the question
7. **Tool Execution Request:** Your server asks the MCP client to run the tool Claude specified
8. **External API Call:** The MCP client sends a `CallToolRequest` to the MCP server, which makes the actual GitHub API call
9. **Results Flow Back:** GitHub responds with repository data, which flows back through the MCP server as a `CallToolResult`
10. **Tool Result to Claude:** Your server sends the tool results back to Claude
11. **Final Response:** Claude formulates a final answer using the repository data
12. **User Gets Answer:** Your server delivers Claude's response back to the user

![](https://academy.claude.com/assets/media/92b5f03a879df7c7bc870a7b08fe1f93aa1cc9398f4de4128089c213c19df24f.png)

Yes, this flow involves many steps, but each component has a clear responsibility. The MCP client abstracts away the complexity of server communication, letting you focus on your application logic while still getting access to powerful external tools and data sources.

Understanding this flow is crucial because you'll see all these pieces when building your own MCP clients and servers in the upcoming sections.

[Previous lessonIntroducing MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol/introducing-mcp)[Next lessonDefining tools with MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-tools-with-mcp)

Lesson 2 of 10 · Introduction to Model Context ProtocolMCP clients

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

* [Transport Agnostic Communication](#transport-agnostic-communication)
* [MCP Message Types](#mcp-message-types)
* [How It All Works Together](#how-it-all-works-together)
