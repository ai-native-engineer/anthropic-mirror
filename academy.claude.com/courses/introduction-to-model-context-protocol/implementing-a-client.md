<!-- source: https://academy.claude.com/courses/introduction-to-model-context-protocol/implementing-a-client -->

Lesson 5 of 10 · Introduction to Model Context ProtocolImplementing a client

3. /[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

# Implementing a client

Lesson 510 min

Now that we have our MCP server working, it's time to build the client side. The client is what allows our application code to communicate with the MCP server and access its functionality.

## Understanding the Client Architecture

In most real-world projects, you'll either implement an MCP client or an MCP server - not both. We're building both in this project just so you can see how they work together.

![Diagram noting that a project normally implements either an MCP client or an MCP server; our project implements both, showing the MCP client inside our server connected to the MCP server](https://academy.claude.com/assets/media/e05ff8cc824dbd58f3347d6af9f49b018dbd9f71ea5062186a6422b07300571a.png)

The MCP client consists of two main components:

* **MCP Client** - A custom class we create to make using the session easier
* **Client Session** - The actual connection to the server (part of the MCP Python SDK)

![Diagram of mcp_client.py containing the MCP Client, a custom class we author to make using the session easier, and the Client Session, the actual connection to the MCP server](https://academy.claude.com/assets/media/8496bb45df0f912602045b5c8dc2d979174d4e85604a144a595996973b97bbd4.png)

The client session requires careful resource management - we need to properly clean up connections when we're done. That's why we wrap it in our own class that handles all the cleanup automatically.

## How the Client Fits Into Our Application

Remember our application flow diagram? The client is what enables our code to interact with the MCP server at two key points:

![Sequence diagram of the application flow with callouts highlighting where our CLI code uses the client to get a list of tools to pass to Claude and where it uses the client to call a tool](https://academy.claude.com/assets/media/abd2d482edcac888b5dc91716804e873e2f93caeaef3524cd24c0098bb8221e1.png)

Our CLI code uses the client to:

* Get a list of available tools to send to Claude
* Execute tools when Claude requests them

## Implementing Core Client Functions

We need to implement two essential functions: `list_tools()` and `call_tool()`.

### List Tools Function

This function gets all available tools from the MCP server:

python

```
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools
```

It's straightforward - we access our session (the connection to the server), call the built-in `list_tools()` method, and return the tools from the result.

### Call Tool Function

This function executes a specific tool on the server:

python

```
async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

We pass the tool name and input parameters (provided by Claude) to the server and return the result.

## Testing the Client

The client file includes a simple test harness at the bottom. You can run it directly to verify everything works:

`uv run mcp_client.py`

This will connect to your MCP server and print out the available tools. You should see output showing your tool definitions, including descriptions and input schemas.

## Putting It All Together

Once the client functions are implemented, you can test the complete flow by running your main application:

`uv run main.py`

Try asking:

What is the contents of the report.pdf document?

Copy prompt

Here's what happens behind the scenes:

1. Your application uses the client to get available tools
2. These tools are sent to Claude along with your question
3. Claude decides to use the read\_doc\_contents tool
4. Your application uses the client to execute that tool
5. The result is returned to Claude, who then responds to you

The client acts as the bridge between your application logic and the MCP server's functionality, making it easy to integrate powerful tools into your AI workflows.

[Previous lessonThe server inspector](https://academy.claude.com/courses/introduction-to-model-context-protocol/the-server-inspector)[Next lessonDefining resources](https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-resources)

Lesson 5 of 10 · Introduction to Model Context ProtocolImplementing a client

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

* [Understanding the Client Architecture](#understanding-the-client-architecture)
* [How the Client Fits Into Our Application](#how-the-client-fits-into-our-application)
* [Implementing Core Client Functions](#implementing-core-client-functions)
* [Testing the Client](#testing-the-client)
* [Putting It All Together](#putting-it-all-together)
