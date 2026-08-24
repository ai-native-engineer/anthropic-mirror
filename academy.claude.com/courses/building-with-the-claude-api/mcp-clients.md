<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/mcp-clients -->

Lesson 48 of 67 · Building with the Claude APIMCP clients

The MCP client serves as the communication bridge between your server and MCP servers. Think of it as your access point to all the tools that an MCP server provides. When you need to use external tools or services, the client handles all the message passing and protocol details for you.

## Transport Agnostic Communication

One of MCP's key strengths is being transport agnostic - a fancy way of saying the client and server can talk to each other using different communication methods. The most common setup runs both the MCP client and server on the same machine, where they communicate through standard input/output.

![](https://academy.claude.com/assets/media/8bdb21c32a46d02cbc360167f39e7fce71d6a04634334136e76ffcaf2daee127.jpg)

But you're not limited to that approach. MCP clients and servers can also connect over:

* HTTP
* WebSockets
* Various other network protocols

![](https://academy.claude.com/assets/media/4508517b29879b546ebbba8597863458129816ce4aad5c0ee3113f3b30a5a6c3.jpg)

## Message Types

Once connected, the client and server exchange specific message types defined in the MCP specification. The main message types you'll work with are:

![](https://academy.claude.com/assets/media/17af17ed9ff3f229f603c3b59250b5d92786e7b63e7e3c1a30ab284addba1ef4.jpg)

**ListToolsRequest/ListToolsResult:** The client asks the server "what tools do you provide?" and gets back a list of available tools.

![](https://academy.claude.com/assets/media/73bd1e2204d018c2acb8cfc31f580727221ad718074048a27ab315306b8c0a8f.jpg)

**CallToolRequest/CallToolResult:** The client asks the server to run a specific tool with certain arguments, then receives the results.

![](https://academy.claude.com/assets/media/44fde20f099c3312553c496d79ed51d3043af6b987109bbbcee429da51776cad.jpg)

## Complete Flow Example

Here's how all the pieces work together in a real scenario. Let's say a user asks "What repositories do I have?" - here's the complete communication flow:

![](https://academy.claude.com/assets/media/61428a53b0f6730592f0e711bb8f24e34176883ce9c39ecaf7c8122f72106cc3.jpg)

The process starts when a user submits a query to your server. Your server realizes it needs to provide Claude with a list of available tools before making the request.

![](https://academy.claude.com/assets/media/e964768453610b1138d6d4217761b5f316fa09816587ee5c2e9aad1b3e3acad7.jpg)

Your server asks the MCP client for tools, which sends a `ListToolsRequest` to the MCP server and receives a `ListToolsResult` back.

![](https://academy.claude.com/assets/media/2e4cdc634443c2846cf601478dd087dbf77df4850b4f4e022f2f7ad48346d148.jpg)

Now your server has everything needed to make the initial request to Claude - both the user's question and the available tools.

![](https://academy.claude.com/assets/media/461d8942bd83d63419cca305408d14865e2256499763134a4978829c61af0d9a.jpg)

Claude examines the tools and decides it needs to call one to answer the question. It responds with a tool use request.

![](https://academy.claude.com/assets/media/d35808ae9031b629b0294f919659fde5a005d0ba3ab72b0dff0a0797431d1a32.jpg)

Your server asks the MCP client to execute the tool Claude requested. The MCP client sends a `CallToolRequest` to the MCP server, which then makes the actual request to GitHub.

![](https://academy.claude.com/assets/media/2acd9bb9a6ece8248270885ef6e1bd7c803b26ebfd17cd795ae1bcd0133e35de.jpg)

GitHub returns the repository data, which flows back through the MCP server as a `CallToolResult`, then to the MCP client, and finally to your server.

![](https://academy.claude.com/assets/media/df5aca29f01605a07abb6642257466546f29268dc9e96b66d3acd3fbc2ab170f.jpg)

Your server sends the tool results back to Claude in a follow-up message. Claude now has all the information it needs to formulate a complete response.

![](https://academy.claude.com/assets/media/0ed2a940cf9df91c07456642de6995d79618e838efb702be7762d8596caf6ec3.jpg)

Finally, Claude responds with the formatted answer, which your server passes back to the user.

Yes, this flow involves many steps, but each component has a clear responsibility. The MCP client abstracts away the complexity of server communication, letting you focus on building your application logic. As we implement our own MCP client and server, you'll see how each piece fits together in practice.
