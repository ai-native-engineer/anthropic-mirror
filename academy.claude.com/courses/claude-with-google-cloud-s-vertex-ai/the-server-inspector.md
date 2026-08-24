<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/the-server-inspector -->

Lesson 53 of 66 · Claude with Google Cloud's Vertex AIThe server inspector

When building MCP servers, you need a way to test your functionality without connecting to a full application. The Python MCP SDK includes a built-in browser-based inspector that lets you debug and test your server in real-time.

## Starting the Inspector

First, make sure your Python environment is activated (check your project's README for the exact command). Then run the inspector with:

bash

```
mcp dev mcp_server.py
```

This starts a development server and gives you a local URL (typically on port 6277) to access the inspector in your browser.

![](https://academy.claude.com/assets/media/19b987b5529baeb03bed9b07e03fd0d0c56298a716b439dc896de8898f1d2b3f.png)

## Using the Inspector Interface

The MCP inspector is actively being developed, so the interface may look different when you use it. However, the core functionality remains consistent.

![](https://academy.claude.com/assets/media/b71855041936bb82ba63e92710c498b45c405ca4965b1df73317262d3882ce88.png)

After clicking "Connect" to start your MCP server, you'll see a navigation bar with sections for:

* Resources
* Prompts
* Tools
* Other server capabilities

## Testing Your Tools

The Tools section is where you'll spend most of your debugging time. Click "List Tools" to see all the tools your server provides.

![](https://academy.claude.com/assets/media/f52575beb9b624156b5d72a5be3235a039335927125dcbefe10d99eef767f749.png)

When you select a tool, the right panel shows its details and provides input fields for testing. For example, to test the `read_doc_contents` tool:

1. Select the tool from the list
2. Enter a document ID (like "deposition.md")
3. Click "Run Tool"
4. Check the results for success and expected output

![](https://academy.claude.com/assets/media/cb9b3c821130bee229aefb94456017fd04d46e53b1d24a91aef58a83d49b31a4.png)

## Testing Tool Interactions

You can test multiple tools in sequence to verify they work together correctly. For instance, after using the `edit_document` tool to modify content:

![](https://academy.claude.com/assets/media/768ecb1a50bbf0db37a9ba8dcc98e3147cac24f121fd043a0e530ee5d41dc96d.png)

Run the `read_doc_contents` tool again with the same document ID to confirm your changes were applied:

![](https://academy.claude.com/assets/media/14cce52c52772af7b18d1a65cd32117d8883c297c738859ddf7b2aff22663d00.png)

## Development Workflow

The inspector creates an efficient development loop:

* Make changes to your MCP server code
* Test individual tools with various inputs
* Verify tool interactions work as expected
* Debug issues without needing a full application setup

This browser-based testing environment is essential for MCP server development. It saves time by letting you catch issues early and verify functionality before integrating with Claude or other applications.
