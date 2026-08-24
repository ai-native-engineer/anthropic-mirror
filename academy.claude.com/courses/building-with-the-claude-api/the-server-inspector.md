<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/the-server-inspector -->

Lesson 51 of 67 · Building with the Claude APIThe server inspector

When building MCP servers, you need a way to test your functionality without connecting to a full application. The Python MCP SDK includes a built-in browser-based inspector that lets you debug and test your server in real-time.

## Starting the Inspector

First, make sure your Python environment is activated (check your project's README for the exact command). Then run the inspector with:

bash

```
mcp dev mcp_server.py
```

This starts a development server on port 6277 and gives you a local URL to open in your browser. The inspector interface will load, showing the MCP Inspector dashboard.

![](https://academy.claude.com/assets/media/d5c53f9c21554c0e600c169c110b95a83b0a13d9859957eca93b5eff2ad2cb37.jpg)

## Important Note About the Interface

The MCP inspector is actively being developed, so the interface you see might look different from current screenshots. However, the core functionality for testing tools, resources, and prompts should remain similar.

## Connecting and Testing Tools

Click the "Connect" button on the left side to start your MCP server. Once connected, you'll see a navigation bar with sections for Resources, Prompts, Tools, and other features.

![](https://academy.claude.com/assets/media/2bd396b5d7555ecf2b9b0717b004d5839ec0f1b48da39cfed4db5b6774fa0d77.jpg)

To test your tools:

* Navigate to the Tools section
* Click "List Tools" to see all available tools
* Select a tool to open its testing interface
* Fill in the required parameters
* Click "Run Tool" to execute and see results

![](https://academy.claude.com/assets/media/48c68f10cf289038f2174feb95524d83e867c2473cbe1b4858dd36a108978b64.jpg)

## Testing Document Operations

For example, to test a document reading tool, you'd enter a document ID (like "deposition.md") and run the tool. The inspector shows the result, including any returned content or success messages.

![](https://academy.claude.com/assets/media/a0a63118f39b5f6feffdbd45ea60891c378b7bd7b969718684b89c983c538d14.jpg)

You can chain operations to verify functionality. For instance, after editing a document by replacing text, you can immediately run the read tool again to confirm the changes were applied correctly.

## Development Workflow

The inspector creates an efficient development loop:

* Make changes to your MCP server code
* Test individual tools through the inspector
* Verify results without needing a full application setup
* Debug issues in isolation

This tool becomes essential as you build more complex MCP servers. It eliminates the need to wire up your server to Claude or another application just to test basic functionality, making development much faster and more focused.
