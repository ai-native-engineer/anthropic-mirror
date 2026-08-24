<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/implementing-a-client -->

Lesson 53 of 65 · Claude with Amazon BedrockImplementing a client

Now that we have our MCP server working, it's time to build the client side. The client is what allows our application to communicate with the MCP server and access its functionality.

## Understanding the Client Architecture

Before diving into the code, let's clarify an important point about MCP projects. Normally, you'd implement either an MCP client or an MCP server - not both. We're building both in this project just so you can see how they work together.

![](https://academy.claude.com/assets/media/e94731a8dca43d340b500f65cfb16000c821fe5e222b2b056639a2b575e7b8f3.png)

The MCP client consists of two main components working together:

![](https://academy.claude.com/assets/media/cc4caa2d061790f9dd25575567a1a1a39f3b7665cce6019103004c86fd7c87e4.png)

* **MCP Client** - A custom class we create to make using the session easier
* **Client Session** - The actual connection to the server (part of the MCP Python SDK)

The client session handles the low-level communication but requires careful resource cleanup when your program shuts down. That's why we wrap it in our own class - to manage that cleanup automatically.

## How the Client Fits Into Our Application

Remember our application flow diagram? The client plays a crucial role in two key moments:

![](https://academy.claude.com/assets/media/a2e0ebe2d4d156022ef0407cd8d9dfcbab01dfdfbec1a87875c82618902af67a.png)

Our CLI code uses the client to:

* Get a list of available tools to send to Claude
* Execute tools when Claude requests them

## Implementing Core Client Functions

Let's implement the two essential functions: `list_tools` and `call_tool`.

For `list_tools`, we need to connect to our session and request the available tools:

python

```
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools
```

For `call_tool`, we pass the tool name and input parameters to the server:

python

```
async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

That's it! The session handles all the complex communication details for us.

## Testing the Client

The client file includes a simple test harness at the bottom. You can run it directly to verify everything works:

bash

```
uv run mcp_client.py
```

This will connect to your MCP server and print out the available tools. You should see output showing your tool definitions, including names, descriptions, and input schemas.

## Important Schema Differences

Here's a gotcha you need to know about: MCP tool definitions don't exactly match what Claude expects. The MCP spec has its own format for tool schemas, which is slightly different from what Bedrock requires.

Don't worry - there's already code in the project that handles this conversion automatically. The `to_bedrock_tools` function in `core/bedrock.py` translates MCP tool definitions into the format Claude understands.

## Testing with Claude

Now that both the server and client are working, you can test the complete flow. Try running your main application and asking Claude to read a document:

bash

```
uv run main.py
```

Then ask: "What is the contents of the report.pdf document?"

Claude will:

1. Receive the list of available tools from your client
2. Decide to use the read\_doc\_contents tool
3. Your client will execute that tool on the MCP server
4. Claude will receive the document contents and respond

The client acts as the bridge between your application code and the MCP server, making it easy to expose server functionality to Claude and other parts of your system.
