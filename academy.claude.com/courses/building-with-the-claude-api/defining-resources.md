<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/defining-resources -->

Lesson 53 of 67 · Building with the Claude APIDefining resources

Resources in MCP servers allow you to expose data to clients, similar to GET request handlers in a typical HTTP server. They're perfect for scenarios where you need to fetch information rather than perform actions.

## Understanding Resources Through an Example

Let's say you want to build a document mention feature where users can type `@document_name` to reference files. This requires two operations:

* Getting a list of all available documents (for autocomplete)
* Fetching the contents of a specific document (when mentioned)

![](https://academy.claude.com/assets/media/cd7019a12385a54b4089f63b6e975d484577eeb9af1ca129e405eec83744bf05.jpg)

When a user types `@`, you need to show available documents. When they submit a message with a mention, you automatically inject that document's content into the prompt sent to Claude.

![](https://academy.claude.com/assets/media/a170bf8f94380bcc029a6daead85c463cdc8e23ec71b8b2916d277a6408ced76.jpg)

## How Resources Work

Resources follow a request-response pattern. Your client sends a `ReadResourceRequest` with a URI, and the MCP server responds with the data. The URI acts like an address for the resource you want to access.

![](https://academy.claude.com/assets/media/8bfda681993ad051a7e85469a51a31a92a3a9978db28b8ffcedf64bd1af0f8ea.jpg)

## Types of Resources

There are two types of resources:

![](https://academy.claude.com/assets/media/74cf80a71ba587ae82fa642f86a4d79b074d82eefd1428f88a74e51cfddc435d.jpg)

* **Direct Resources:** Static URIs that don't change, like `docs://documents`
* **Templated Resources:** URIs with parameters, like `docs://documents/{doc_id}`

For templated resources, the Python SDK automatically parses parameters from the URI and passes them as keyword arguments to your function.

## Implementing Resources

Resources are defined using the `@mcp.resource()` decorator. Here's how to create both types:

### Direct Resource (List Documents)

python

```
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())
```

### Templated Resource (Fetch Document)

python

```
@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

## MIME Types

Resources can return any type of data - strings, JSON, binary, etc. The `mime_type` parameter gives clients a hint about what kind of data you're returning:

* `application/json` - Structured JSON data
* `text/plain` - Plain text content
* Any other valid MIME type for different data formats

The MCP Python SDK automatically serializes your return values. You don't need to manually convert to JSON strings.

## Testing Resources

You can test your resources using the MCP Inspector. Run your server with:

bash

```
uv run mcp dev mcp_server.py
```

Then connect to the inspector in your browser. You'll see:

![](https://academy.claude.com/assets/media/b26f1ed0bfbe7f7c66d1cdd739b81c0255fbdf1fececc14917f410bc1a9fc24c.jpg)

* **Resources:** Lists your direct/static resources
* **Resource Templates:** Shows templated resources that accept parameters

Click on any resource to test it and see the exact response structure your client will receive.

![](https://academy.claude.com/assets/media/d0d0f67385c33ac2744acab67a33e84d2c464bc3794ce05313c7e903ed281bce.jpg)

## Key Points

* Resources expose data, tools perform actions
* Use direct resources for static data, templated resources for parameterized queries
* MIME types help clients understand response format
* The SDK handles serialization automatically
* Parameter names in templated URIs become function arguments

Resources provide a clean way to make data available to MCP clients, enabling features like document mentions, file browsing, or any scenario where you need to fetch information from your server.
