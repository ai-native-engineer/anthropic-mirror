<!-- source: https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-resources -->

Lesson 6 of 10 · Introduction to Model Context ProtocolDefining resources

3. /[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

# Defining resources

Lesson 68 min

Resources in MCP servers allow you to expose data to clients, similar to GET request handlers in a typical HTTP server. They're perfect for scenarios where you need to fetch information rather than perform actions.

## Understanding Resources Through an Example

Let's say you want to build a document mention feature where users can type `@document_name` to reference files. This requires two operations:

* Getting a list of all available documents (for autocomplete)
* Fetching the contents of a specific document (when mentioned)

![Feature slide: users can mention a document by writing out @doc_name; typing @ shows a list of all available documents in an autocomplete, and a mentioned document's contents are automatically injected into the prompt](https://academy.claude.com/assets/media/23bc7e478d6c6758102ca48f72ed2a8606615e8fc1aaa4920b6b7fa38203ebe7.png)

When a user mentions a document, your system automatically injects the document's contents into the prompt sent to Claude, eliminating the need for Claude to use tools to fetch the information.

![Diagram of a user asking "What's in the @report.pdf file?" — our code wraps the query in a prompt for Claude with the referenced document's contents injected inside a document tag](https://academy.claude.com/assets/media/49dbdb150ca9eba442fd911a0e136afb35a2bab168d8910577c54fdf1bb6e733.png)

## How Resources Work

Resources follow a request-response pattern. When your client needs data, it sends a `ReadResourceRequest` with a URI to identify which resource it wants. The MCP server processes this request and returns the data in a `ReadResourceResult`.

![Sequence diagram: the user types "What's in the @…", our code asks the MCP client for a list of document names for the autocomplete, and the client sends a ReadResourceRequest with the docs://documents URI to the MCP server](https://academy.claude.com/assets/media/8530241c3b0e429b3498df6bc546cf064bb76adf01c965d77e1d68bf687a5ae3.png)

The flow looks like this: your code requests a resource from the MCP client, which forwards the request to the MCP server. The server processes the URI, runs the appropriate function, and returns the result.

![Sequence diagram continued: the MCP server returns a ReadResourceResult containing the list of doc names, which the MCP client passes back to our code to put into the autocomplete](https://academy.claude.com/assets/media/90c43206eae4c5f233e73b2d4de24c46ad2abd7419c0eac31eaad78d37407290.png)

## Types of Resources

There are two types of resources:

### Direct Resources

Direct resources have static URIs that never change. They're perfect for operations that don't need parameters.

python

```
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())
```

### Templated Resources

Templated resources include parameters in their URIs. The Python SDK automatically parses these parameters and passes them as keyword arguments to your function.

python

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

![Side-by-side comparison: a Direct Resource whose URI doesn't contain any params, and a Templated Resource whose URI contains one or more params that the Python SDK parses and passes as args to your function](https://academy.claude.com/assets/media/7fa0c5f6bafc5aec5ed6ff72d121e8b04986bc6379c9c4da1d042b7cca99ce50.png)

## Implementation Details

Resources can return any type of data - strings, JSON, binary data, etc. Use the `mime_type` parameter to give clients a hint about what kind of data you're returning:

* `"application/json"` for structured data
* `"text/plain"` for plain text
* `"application/pdf"` for binary files

The MCP Python SDK automatically serializes your return values. You don't need to manually convert objects to JSON strings - just return the data structure and let the SDK handle serialization.

## Testing Your Resources

You can test resources using the MCP Inspector. Start your server with:

`uv run mcp dev mcp_server.py`

Then connect to the inspector in your browser. You'll see two sections:

* **Resources** - Lists your direct/static resources
* **Resource Templates** - Lists your templated resources

![MCP Inspector with the Resources tab open, showing the docs://documents direct resource under Resources, the fetch_doc template under Resource Templates, and the JSON response for docs://documents with its URI, mimeType, and serialized list of document names](https://academy.claude.com/assets/media/aaba6fbd4b955f7b77e8a806c6ac6bc7c7b6a7406c9094b4bdddc93f146e8dcb.png)

Click on any resource to test it. For templated resources, you'll need to provide values for the parameters. The inspector shows you the exact response structure your client will receive, including the MIME type and serialized data.

Resources provide a clean way to expose read-only data from your MCP server, making it easy for clients to fetch information without the complexity of tool calls.

[Previous lessonImplementing a client](https://academy.claude.com/courses/introduction-to-model-context-protocol/implementing-a-client)[Next lessonAccessing resources](https://academy.claude.com/courses/introduction-to-model-context-protocol/accessing-resources)

Lesson 6 of 10 · Introduction to Model Context ProtocolDefining resources

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

* [Understanding Resources Through an Example](#understanding-resources-through-an-example)
* [How Resources Work](#how-resources-work)
* [Types of Resources](#types-of-resources)
* [Implementation Details](#implementation-details)
* [Testing Your Resources](#testing-your-resources)
