<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/defining-resources -->

Lesson 55 of 66 · Claude with Google Cloud's Vertex AIDefining resources

Resources in MCP servers allow you to expose data to clients, similar to GET request handlers in a typical HTTP server. They're perfect for scenarios where you need to fetch information rather than perform actions.

## Understanding Resources

Think of resources as read-only endpoints that can return any type of data - strings, JSON, binary files, etc. You set a 'mime\_type' to give the client a hint about what kind of data you're returning.

![](https://academy.claude.com/assets/media/bef714547cc3f86a4f566052ca3e2d3b7bba3694a823f2bbebd84e742c766e1b.png)

Resources work by defining a URI (like a URL) that clients can request. When a client needs data, it sends a ReadResourceRequest with the specific URI, and your server responds with a ReadResourceResult containing the data.

## Two Types of Resources

There are two main types of resources you can create:

* **Direct Resources** - Have static URIs that don't contain any parameters (like "docs://documents")
* **Templated Resources** - Include parameters in their URIs that get parsed and passed to your function (like "docs://documents/{doc\_id}")

![](https://academy.claude.com/assets/media/7fa0c5f6bafc5aec5ed6ff72d121e8b04986bc6379c9c4da1d042b7cca99ce50.png)

For templated resources, the Python SDK automatically parses parameters from the URI and passes them as keyword arguments to your function. The parameter names in the URI must match your function's parameter names exactly.

## Creating Resources

Here's how to implement both types of resources:

python

```
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())

@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

The MCP Python SDK automatically serializes whatever you return. You don't need to manually convert data to JSON strings - just return Python objects and the SDK handles the conversion.

## Testing Your Resources

You can test resources using the MCP Inspector. Start your server with:

`uv run mcp dev mcp_server.py`

Then connect to the inspector in your browser. You'll see two sections:

* **Resources** - Lists your direct/static resources
* **Resource Templates** - Shows your templated resources

![](https://academy.claude.com/assets/media/aaba6fbd4b955f7b77e8a806c6ac6bc7c7b6a7406c9094b4bdddc93f146e8dcb.png)

Click on any resource to test it. For templated resources, you'll need to provide values for the parameters. The inspector shows you the exact response structure your client will receive, including the mime type and serialized data.

## Practical Use Cases

Resources are ideal for implementing features like document mentions in chat applications. For example, when a user types "@" to mention a document, you could:

1. Use a direct resource to fetch a list of all available documents for autocomplete
2. Use a templated resource to fetch the contents of a specific document when mentioned

This approach lets you preemptively inject document content into prompts without requiring the AI to use tools to fetch the information.
