<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/defining-resources -->

Lesson 54 of 65 · Claude with Amazon BedrockDefining resources

Resources in MCP servers allow you to expose data to clients, similar to GET request handlers in a typical HTTP server. They're perfect for scenarios where you need to fetch information rather than perform actions.

## Understanding Resources

Think of resources as read-only endpoints that can return any type of data - strings, JSON, binary files, etc. You set a 'mime\_type' to give the client a hint about what kind of data you're returning.

![](https://academy.claude.com/assets/media/bef714547cc3f86a4f566052ca3e2d3b7bba3694a823f2bbebd84e742c766e1b.png)

Resources work by exposing data through URIs (essentially addresses). When a client needs data, it sends a ReadResourceRequest with the specific URI, and your server responds with the requested information.

## Two Types of Resources

There are two main types of resources you can create:

* **Direct Resources** - Have static URIs that don't contain any parameters (like `docs://documents`)
* **Templated Resources** - Include parameters in their URIs (like `docs://documents/{doc_id}`)

![](https://academy.claude.com/assets/media/7fa0c5f6bafc5aec5ed6ff72d121e8b04986bc6379c9c4da1d042b7cca99ce50.png)

For templated resources, the Python SDK automatically parses parameters from the URI and passes them as keyword arguments to your function. The parameter name in the URI becomes the argument name in your function.

## Implementing Resources

Creating resources is straightforward using the `@mcp.resource()` decorator. Here's how to implement both types:

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

The MCP Python SDK automatically serializes whatever you return. You don't need to manually convert data to JSON strings - just return the appropriate Python data structure.

## Testing Your Resources

You can test resources using the MCP Inspector tool. Start your server with `uv run mcp dev mcp_server.py` and navigate to the web interface.

![](https://academy.claude.com/assets/media/aaba6fbd4b955f7b77e8a806c6ac6bc7c7b6a7406c9094b4bdddc93f146e8dcb.png)

The inspector separates direct resources from templated ones. Direct resources appear in the main "Resources" section, while templated resources show up under "Resource Templates". You can click on any resource to test it and see the exact response structure your server returns.

## Practical Use Cases

Resources are ideal for:

* Providing autocomplete data (like document lists)
* Fetching file contents or database records
* Exposing configuration data
* Serving any read-only information your client needs

The key advantage is that resources allow clients to proactively fetch data without relying on tools or complex interactions. This makes them perfect for features like document mentions, where you want to automatically inject content into prompts based on user references.
