<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/implementing-a-client -->

Lesson 54 of 66 · Claude with Google Cloud's Vertex AIImplementing a client

Now that we have our MCP server working, it's time to build the client side. The client is what allows our application to communicate with the MCP server and access its functionality.

## Understanding the Client Architecture

Before diving into the code, let's clarify an important point about MCP projects. Normally, you'd implement either an MCP client or an MCP server - not both. We're building both in this project just so you can see how they work together.

![](https://academy.claude.com/assets/media/e05ff8cc824dbd58f3347d6af9f49b018dbd9f71ea5062186a6422b07300571a.png)

The MCP client consists of two main components:

* **MCP Client** - A custom class we create to make using the session easier
* **Client Session** - The actual connection to the server (part of the MCP Python SDK)

![](https://academy.claude.com/assets/media/8496bb45df0f912602045b5c8dc2d979174d4e85604a144a595996973b97bbd4.png)

The client session requires resource cleanup when we're done with it, which is why we wrap it in our custom class. This handles connection management and cleanup automatically.

## How the Client Fits Into Our Application

Remember our application flow? Our CLI code needs to interact with Claude in two key ways:

![](https://academy.claude.com/assets/media/abd2d482edcac888b5dc91716804e873e2f93caeaef3524cd24c0098bb8221e1.png)

The client enables both of these interactions by exposing the server's functionality to our codebase.

## Implementing Core Client Functions

We need to implement two essential functions: `list_tools` and `call_tool`.

### List Tools Function

This function gets all available tools from the server:

python

```
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools
```

It's straightforward - we access our session (the connection to the MCP server), call the built-in `list_tools` function, and return the tools from the result.

### Call Tool Function

This function executes a specific tool on the server:

python

```
async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

We pass the tool name and input parameters (provided by Claude) to the server and return the result.

## Testing the Client

To verify our implementation works, we can test it directly. The client file includes a testing harness that connects to the MCP server and runs commands against it.

Running `uv run mcp_client.py` should return a list of available tools with their descriptions and input schemas. You should see tools like `read_doc_contents` and `edit_document` that we defined in our server.

## End-to-End Testing

Now that both the client and server are working, we can test the complete flow. Running our main application and asking Claude "What is the contents of the report.pdf document?" should:

1. Send the list of available tools to Claude
2. Claude decides to use the `read_doc_contents` tool
3. Our client calls the tool on the server
4. The server returns the document contents
5. Claude responds with the information

The client acts as the bridge between your application code and the MCP server, making it easy to access server functionality without dealing with the low-level connection details directly.
