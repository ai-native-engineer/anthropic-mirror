<!-- source: https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-stdio-transport -->

Lesson 8 of 11 · Model Context Protocol: Advanced TopicsThe STDIO transport

MCP clients and servers communicate by exchanging JSON messages, but how do these messages actually get transmitted? The communication channel used is called a **transport**, and there are several ways to implement this - from HTTP requests to WebSockets to even writing JSON on a postcard (though that last one isn't recommended for production use).

## The Stdio Transport

When you're first developing an MCP server or client, the most commonly used transport is the **stdio transport**. This approach is straightforward: the client launches the MCP server as a subprocess and communicates through standard input and output streams.

![Diagram of the stdio transport: an MCP client sends messages to an MCP server through the server's stdin, and the server sends messages back through stdout; either side can send a message at any time, and it only works when both run on the same machine](https://academy.claude.com/assets/media/e5533b780e5ccba1af64a28d58d79c8d7a88dd1a580e901dc743a7dd079eb683.png)

Here's how it works:

* Client sends messages to the server using the server's `stdin`
* Server responds by writing to `stdout`
* Either the server or client can send a message at any time
* Only works when client and server run on the same machine

## Seeing Stdio in Action

You can actually test an MCP server directly from your terminal without writing a separate client. When you run a server with `uv run server.py`, it listens to stdin and writes responses to stdout. This means you can paste JSON messages directly into your terminal and see the server's responses immediately.

The terminal output shows the complete message exchange, including example messages for initialization and tool calls.

## MCP Connection Sequence

Every MCP connection must start with a specific three-message handshake:

![Sequence diagram of the MCP handshake: the client sends an Initialize Request to the server, the server replies with an Initialize Result, then the client sends an Initialized Notification for which no result comes back](https://academy.claude.com/assets/media/784e9ecbcbd5acd3a10550ae854375721ece9fabec09c5222d7ebe3cf062ad8c.png)

1. **Initialize Request** - Client sends this first
2. **Initialize Result** - Server responds with capabilities
3. **Initialized Notification** - Client confirms (no response expected)

Only after this handshake can you send other requests like tool calls or prompt listings.

## Message Types and Flow

MCP supports various message types that flow in both directions:

![Chart of MCP message types between client and server: client-initiated request/result pairs like Call Tool Request → Call Tool Result, server-initiated pairs like Create Message Request and List Roots Request, plus one-way notifications from each side that don't require a response](https://academy.claude.com/assets/media/ec6d64526e67257959ecb4f3322f076fd761db1a8487a63b4f24cce6bbc9c05a.png)

The key insight is that some messages require responses (requests → results) while others don't (notifications). Both client and server can initiate communication at any time.

## Four Communication Scenarios

With any transport, you need to handle four different communication patterns:

![Diagram titled "How can we implement each of these with stdio?" listing four patterns - initial request from client to server, response from server to client, initial request from server to client, and response from client to server - next to an MCP client connected to an MCP server's stdin and stdout](https://academy.claude.com/assets/media/d6a31cbd16c8c478c000b93a0f2e89f20eb88a48d779f5214fa8c7fc28bdfd0d.png)

* **Client → Server request**: Client writes to stdin
* **Server → Client response**: Server writes to stdout
* **Server → Client request**: Server writes to stdout
* **Client → Server response**: Client writes to stdin

The beauty of stdio transport is its simplicity - either party can initiate communication at any time using these two channels.

## Why This Matters

Understanding stdio transport is crucial because it represents the "ideal" case where bidirectional communication is seamless. When we move to other transports like HTTP, we'll encounter limitations where the server cannot always initiate requests to the client. The stdio transport serves as our baseline for understanding what full MCP communication looks like before we tackle the constraints of other transport methods.

For development and testing, stdio transport is perfect. For production deployments where client and server need to run on different machines, you'll need to consider other transport options with their own trade-offs.
