<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/the-server-inspector -->

Lesson 52 of 65 · Claude with Amazon BedrockThe server inspector

When building MCP servers, you need a way to test your functionality without connecting to a full application. The Python MCP SDK includes a built-in browser-based inspector that lets you debug and test your server in real-time.

## Starting the Inspector

First, make sure your Python environment is activated (check your project's README for the exact command). Then run the inspector with:

bash

```
mcp dev mcp_server.py
```

This starts a development server and gives you a local URL (typically on port 6277) to access the inspector in your browser.

## Using the Inspector Interface

The MCP inspector is actively being developed, so the interface may look different by the time you use it. However, the core functionality remains consistent.

![](https://academy.claude.com/assets/media/b71855041936bb82ba63e92710c498b45c405ca4965b1df73317262d3882ce88.png)

When you first open the inspector, you'll see a "Connect" button on the left side. Click this to start your MCP server and load your tools.

## Testing Your Tools

Once connected, look for a navigation bar with sections like Resources, Prompts, and Tools. Click on the Tools section to see your available tools.

Click "List Tools" to see all the tools your server provides. When you select a specific tool, the right panel updates to show a form where you can test that tool.

## Running Tool Tests

For example, to test a document reading tool:

* Select the `read_doc_contents` tool
* Enter a document ID (like "deposition.md")
* Click "Run Tool"

The inspector will execute your tool and show the results, including success status and any returned data.

![](https://academy.claude.com/assets/media/14cce52c52772af7b18d1a65cd32117d8883c297c738859ddf7b2aff22663d00.png)

## Testing Document Editing

You can also test more complex tools like document editing:

* Switch to the `edit_document` tool
* Fill in the document ID, old text to replace, and new text
* Run the tool to see if it succeeds
* Use the read tool again to verify the changes were applied

![](https://academy.claude.com/assets/media/768ecb1a50bbf0db37a9ba8dcc98e3147cac24f121fd043a0e530ee5d41dc96d.png)

## Development Workflow

The inspector shows a history of your tool calls on the left side, making it easy to track what you've tested and repeat previous operations. This creates an efficient development loop where you can:

* Make changes to your server code
* Restart the inspector
* Test your tools immediately
* Verify the results

This inspector tool becomes essential as you build more complex MCP servers. It eliminates the need to wire up your server to a full application just to test basic functionality, making development much faster and more reliable.
