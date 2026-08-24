<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/defining-tools-with-mcp -->

Lesson 51 of 65 · Claude with Amazon BedrockDefining tools with MCP

Building an MCP server becomes much simpler when you use the official MCP Python SDK. Instead of manually writing complex JSON schemas for tools, you can define them with decorators and let the SDK handle the heavy lifting.

![](https://academy.claude.com/assets/media/dfb5af14ac360361a3e5034af52cffbaab9b7ff1559c84b7274fe8380b804ac7.png)

In this example, we're creating an MCP server that manages document operations. The server will have two main tools: one to read document contents and another to update them. All documents exist in memory as a simple dictionary where keys are document IDs and values are the content strings.

## MCP Python SDK Benefits

The MCP project provides official SDKs for building servers and clients across multiple programming languages. Using the Python SDK offers several advantages:

* Creates MCP servers with minimal boilerplate code
* Automatically generates JSON schemas from Python function signatures
* Simplifies tool definition through decorators
* Handles type validation and error handling

![](https://academy.claude.com/assets/media/6f3f040c71e2fbdc91c66358529c876029cf37b64d4815af9768c7f0192e717f.png)

Here's how easy it is to define a tool with the SDK. The `@mcp.tool` decorator, combined with type hints and field descriptions, automatically creates the proper tool schema that Claude can understand and use.

## Setting Up the Server

The basic server setup requires just a few lines:

python

```
from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures",
    "outlook.pdf": "This document presents the projected future performance of the system",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment"
}
```

## Implementing the Read Tool

The first tool allows Claude to read document contents by providing a document ID:

python

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

The tool definition includes:

* A clear name that describes the action
* A description explaining what the tool does
* Typed parameters with field descriptions
* Error handling for invalid document IDs

## Implementing the Edit Tool

The second tool performs simple find-and-replace operations on document content:

python

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

This tool takes three parameters: the document ID, the text to find, and the replacement text. The implementation uses Python's built-in string `replace()` method for simplicity.

## Key Implementation Details

When defining tools with the MCP SDK, remember these important points:

* Import `Field` from pydantic to add parameter descriptions
* Use type hints to specify parameter types
* Include error handling for edge cases
* Write clear, descriptive tool names and descriptions
* The MCP Python SDK automatically converts your function signature into the proper JSON schema

The MCP Python SDK dramatically reduces the complexity of creating tools compared to manually writing JSON schemas. What used to require dozens of lines of schema definition now takes just a few lines of decorated Python functions.

The `@mcp.tool` decorator and its signature-based schema generation come from the MCP Python SDK. The [Claude Agent SDK provides a separate `@tool` decorator(opens in new tab)](https://code.claude.com/docs/en/agent-sdk/custom-tools) for defining custom tools, and it expects an explicit `input_schema` argument rather than pydantic `Field` annotations on the function signature. In Python that schema is a dict mapping parameter names to types, like `{"latitude": float}`, which the Agent SDK converts to JSON Schema for you, or a full JSON Schema dict when you need enums, ranges, optional fields, or nested objects. When you read tool code elsewhere, check which SDK it imports, since the two decorators are easy to confuse.
