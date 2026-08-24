<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/mcp-clients -->

Lesson 50 of 66 · Claude with Google Cloud's Vertex AIMCP clients

The MCP client serves as the communication bridge between your server and MCP servers. Think of it as your access point to all the tools that an MCP server provides. When you need to use external functionality, the client handles all the message passing and protocol details for you.

## Transport Agnostic Communication

One of MCP's key strengths is being transport agnostic - a fancy way of saying the client and server can talk to each other using different communication methods. The most common setup runs both the MCP client and server on the same machine, where they communicate through standard input/output.

![](https://academy.claude.com/assets/media/b393bf3821c37b06d31300b588c291caa460db51353ebbfbc6a56b9c2a2c0160.png)

But you're not limited to that approach. MCP clients and servers can also connect over:

* HTTP
* WebSockets
* Various other network protocols

![](https://academy.claude.com/assets/media/3a63d189484fd713cdaa1932e5b9638da2b20059ce414c288f77d915371b5f5c.png)

## Message Types

Once connected, the client and server exchange specific message types defined in the MCP specification. The main ones you'll work with are:

![](https://academy.claude.com/assets/media/5e3b30e6b2152e48fe623d81d1d8ea7b3108bee6f03b2dd61d482b30892ddbf3.png)

**ListToolsRequest/ListToolsResult:** The client asks the server "what tools do you provide?" and gets back a complete list of available functionality.

![](https://academy.claude.com/assets/media/4dbfe70297791ff32dced94d745d416ec7ec8c5889d3cbd45ef3328bbdb7f755.png)

**CallToolRequest/CallToolResult:** The client tells the server "run this specific tool with these arguments" and receives the execution results.

![](https://academy.claude.com/assets/media/79f55bb4a81644264e083784408b2a6ef48ca9020dfeafbf7af01acd51f0cf15.png)

## Real-World Example Flow

Let's walk through a complete example to see how all these pieces work together. Imagine a user asks "What repositories do I have?" - here's the entire communication chain:

![](https://academy.claude.com/assets/media/a59d7b848aab54c6194c71ee995382030f667a899ec28918872eb1475f94e784.png)

The process starts when a user submits their question to your server. Your server realizes it needs to provide Claude with available tools before making the AI request.

![](https://academy.claude.com/assets/media/1c07f5155e3236d4041a308cff4f852f90b03cc346db6a394943ea81d4cfb73b.png)

Your server asks the MCP client for a tool list, which triggers a `ListToolsRequest` to the MCP server. The server responds with `ListToolsResult` containing all available tools.

![](https://academy.claude.com/assets/media/75b325da2e24c8a501a9a2cee9d77dae6fc89d4c8eed8116b87a57d8446aed53.png)

Now your server has everything needed to make the initial Claude request: the user's question plus the available tools. Claude analyzes the tools and decides it needs to call one to answer the question properly.

![](https://academy.claude.com/assets/media/1518fad3b60e01d67fc4009b0f6c53b3f889f4ee161b2a30fe9a85eecd6a1ff1.png)

Claude responds with a tool use request. Your server recognizes this and asks the MCP client to execute the tool with Claude's specified arguments.

![](https://academy.claude.com/assets/media/1415a4318b5565540c9003623ee7c39dd14d479e89d6493b996045ad670ee6b8.png)

The MCP client sends a `CallToolRequest` to the MCP server, which then makes the actual API call to GitHub to fetch the user's repositories.

![](https://academy.claude.com/assets/media/dd69a4ce1ab6d335d71ee7a44b39bc7444de41fc5d3ba7b064cfdd489bacbd15.png)

GitHub returns the repository data, which the MCP server wraps in a `CallToolResult` and sends back through the chain. Your server receives this data and can now make a follow-up request to Claude.

![](https://academy.claude.com/assets/media/e567d86142d465bc3fd10f03ed3ce64ac0e3d1a66f7681dd62153a4c28774340.png)

The final step sends the tool results to Claude as part of a user message. Claude now has all the information needed to formulate a complete response about the user's repositories.

![](https://academy.claude.com/assets/media/5cf8d2c9004dbbf4da4442e186ff1042e62d508e3e5810a7314832125c701093.png)

Yes, this flow involves many steps, but understanding it prepares you for implementing your own MCP clients and servers. Each component has a specific role, and the standardized message types ensure everything works together smoothly regardless of the underlying transport mechanism.
