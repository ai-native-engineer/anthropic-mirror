<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/defining-prompts -->

Lesson 57 of 66 · Claude with Google Cloud's Vertex AIDefining prompts

Prompts in MCP servers let you define pre-built, high-quality instructions that clients can use instead of writing their own prompts from scratch. Think of them as carefully crafted templates that give better results than what users might come up with on their own.

## Why Use Prompts?

Let's say you want Claude to reformat a document into markdown. A user could just type "convert report.pdf to markdown" and get decent results. But they'd probably get much better output if they used a thoroughly tested, specialized prompt that you've designed specifically for document formatting.

![](https://academy.claude.com/assets/media/6ab55d7162ceb856be527d35317b17f5327a2e76d36ee4590d61c7f7292787a1.png)

The key insight is that while users can accomplish these tasks on their own, they'll get superior results when using prompts that have been carefully engineered and tested by the MCP server authors.

## How Prompts Work

Prompts define a set of user and assistant messages that clients can use directly. When a client requests a prompt, your server returns a list of messages that can be sent straight to Claude.

![](https://academy.claude.com/assets/media/6fbf83bdc5e673db7ea6f43b7fcadb48e29bfe3f48d49112f21693d7925845bb.png)

The basic structure looks like this:

python

```
@mcp.prompt(
    name="format",
    description="Rewrites the contents of a document in Markdown format",
)
def format_document(
    doc_id: str = Field(description="Id of the document to format"),
) -> list[base.Message]:
    # Return a list of messages
```

## Building a Format Command

Here's a practical example. We'll create a format command that lets users type `/format doc_id` to reformat any document into markdown syntax.

The prompt implementation includes detailed instructions for Claude:

python

```
def format_document(
    doc_id: str = Field(description="Id of the document to format"),
) -> list[base.Message]:
    prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:

{doc_id}

Add in headers, bullet points, tables, etc as necessary. Feel free to add in structure.
Use the 'edit_document' tool to edit the document. After the document has been reformatted...
"""

    return [
        base.UserMessage(prompt)
    ]
```

## Testing Your Prompts

You can test prompts using the MCP Inspector. Navigate to the Prompts tab, select your prompt, and provide any required parameters.

![](https://academy.claude.com/assets/media/fd582104701b532c711ad7cf51c3272fba51b68bf4999e36ea28c2823d4d4576.png)

The inspector shows you exactly what messages will be sent to Claude, including how any parameters get interpolated into the prompt text.

## Key Benefits

* **Quality control** - You can test and refine prompts before users see them
* **Consistency** - Users get reliable results every time
* **Specialization** - Prompts can be tailored to your server's specific domain
* **Reusability** - Multiple clients can use the same well-crafted prompts

## Implementation Details

Don't forget to import the base module for message types:

python

```
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
```

Prompts should be high quality, well-tested, and relevant to your MCP server's overall purpose. In our document management example, formatting prompts make perfect sense since the server specializes in document operations.
