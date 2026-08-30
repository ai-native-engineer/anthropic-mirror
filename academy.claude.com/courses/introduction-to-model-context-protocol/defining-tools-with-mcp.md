<!-- source: https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-tools-with-mcp -->

Lesson 3 of 10 · Introduction to Model Context ProtocolDefining tools with MCP

3. /[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

# Defining tools with MCP

Lesson 310 min

Building an MCP server becomes much simpler when you use the official Python SDK. Instead of writing complex JSON schemas by hand, you can define tools with decorators and let the SDK handle the heavy lifting.

![](https://academy.claude.com/assets/media/19aefa6bde860d04e6b71bd38de13b4ef638c4bd9aa2bcd4d385cd8281fe0c20.png)

In this example, we're creating a document management server with two core tools: one to read documents and another to update them. All documents exist in memory as a simple dictionary where keys are document IDs and values are the content.

## Setting Up the MCP Server[](#setting-up-the-mcp-server)

The Python MCP SDK makes server creation straightforward. You can initialize a server with just one line:

python

```
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")
```

Your documents can be stored in a simple dictionary structure:

python

```
docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures",
    "outlook.pdf": "This document presents the projected future performance of the system",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment"
}
```

## Tool Definition with Decorators[](#tool-definition-with-decorators)

The SDK uses decorators to define tools. Instead of writing JSON schemas manually, you can use Python type hints and field descriptions. The SDK automatically generates the proper schema that Claude can understand.

## Creating a Document Reader Tool[](#creating-a-document-reader-tool)

The first tool reads document contents by ID. Here's the complete implementation:

python

```
@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")

    return docs[doc_id]
```

The decorator specifies the tool name and description, while the function parameters define the required arguments. The `Field` class from Pydantic provides argument descriptions that help Claude understand what each parameter expects.

## Building a Document Editor Tool[](#building-a-document-editor-tool)

The second tool performs simple find-and-replace operations on documents:

python

```
@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including whitespace."),
    new_str: str = Field(description="The new text to insert in place of the old text.")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")

    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
```

This tool takes three parameters: the document ID, the text to find, and the replacement text. The implementation includes error handling for missing documents and performs a straightforward string replacement.

## Key Benefits of the SDK Approach[](#key-benefits-of-the-sdk-approach)

* No manual JSON schema writing required
* Type hints provide automatic validation
* Clear parameter descriptions help Claude understand tool usage
* Error handling integrates naturally with Python exceptions
* Tool registration happens automatically through decorators

The MCP Python SDK transforms tool creation from a complex schema-writing exercise into simple Python function definitions. This approach makes it much easier to build and maintain MCP servers while ensuring Claude receives properly formatted tool specifications.

[Previous lessonMCP clients](https://academy.claude.com/courses/introduction-to-model-context-protocol/mcp-clients)[Next lessonThe server inspector](https://academy.claude.com/courses/introduction-to-model-context-protocol/the-server-inspector)

Lesson 3 of 10 · Introduction to Model Context ProtocolDefining tools with MCP

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

* [Setting Up the MCP Server](#setting-up-the-mcp-server)
* [Tool Definition with Decorators](#tool-definition-with-decorators)
* [Creating a Document Reader Tool](#creating-a-document-reader-tool)
* [Building a Document Editor Tool](#building-a-document-editor-tool)
* [Key Benefits of the SDK Approach](#key-benefits-of-the-sdk-approach)
