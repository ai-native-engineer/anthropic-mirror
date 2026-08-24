<!-- source: https://academy.claude.com/courses/introduction-to-model-context-protocol/the-server-inspector -->

Lesson 4 of 10 · Introduction to Model Context ProtocolThe server inspector

3. /[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

# The server inspector

Lesson 43 min

When building MCP servers, you need a way to test your functionality without connecting to a full application. The Python MCP SDK includes a built-in browser-based inspector that lets you debug and test your server in real-time.

## Starting the Inspector

First, make sure your Python environment is activated (check your project's README for the exact command). Then run the inspector with:

`mcp dev mcp_server.py`

This starts a development server and gives you a local URL, typically something like `http://127.0.0.1:6274`. Open this URL in your browser to access the MCP Inspector.

## Using the Inspector Interface

The inspector interface is actively being developed, so it may look different when you use it. However, the core functionality remains consistent. Look for these key elements:

* A **Connect** button to start your MCP server
* Navigation tabs for **Resources**, **Tools**, **Prompts**, and other features
* A tools listing and testing panel

Click the Connect button first to initialize your server. You'll see the connection status change from "Disconnected" to "Connected".

## Testing Your Tools

Navigate to the Tools section and click "List Tools" to see all available tools from your server. When you select a tool, the right panel shows its details and input fields.

![MCP Inspector with the Tools tab open, showing the read_doc_contents and edit_document tools listed and the read_doc_contents panel with a doc_id input field and Run Tool button](https://academy.claude.com/assets/media/cb9b3c821130bee229aefb94456017fd04d46e53b1d24a91aef58a83d49b31a4.png)

For example, to test a document reading tool:

1. Select the `read_doc_contents` tool
2. Enter a document ID (like "deposition.md")
3. Click "Run Tool"
4. Check the results for success and expected output

The inspector shows both the success status and the actual returned data, making it easy to verify your tool works correctly.

## Testing Tool Interactions

You can test multiple tools in sequence to verify complex workflows. For instance, after using an edit tool to modify a document, immediately test the read tool to confirm the changes were applied correctly.

The inspector maintains your server state between tool calls, so edits persist and you can verify the complete functionality of your MCP server.

## Development Workflow

The MCP Inspector becomes an essential part of your development process. Instead of writing separate test scripts or connecting to full applications, you can:

* Quickly iterate on tool implementations
* Test edge cases and error conditions
* Verify tool interactions and state management
* Debug issues in real-time

This immediate feedback loop makes MCP server development much more efficient and helps catch issues early in the development process.

[Previous lessonDefining tools with MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-tools-with-mcp)[Next lessonImplementing a client](https://academy.claude.com/courses/introduction-to-model-context-protocol/implementing-a-client)

Lesson 4 of 10 · Introduction to Model Context ProtocolThe server inspector

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

* [Starting the Inspector](#starting-the-inspector)
* [Using the Inspector Interface](#using-the-inspector-interface)
* [Testing Your Tools](#testing-your-tools)
* [Testing Tool Interactions](#testing-tool-interactions)
* [Development Workflow](#development-workflow)
