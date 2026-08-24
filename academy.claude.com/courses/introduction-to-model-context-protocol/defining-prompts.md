<!-- source: https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-prompts -->

Lesson 8 of 10 · Introduction to Model Context ProtocolDefining prompts

Prompts in MCP servers let you define pre-built, high-quality instructions that clients can use instead of writing their own prompts from scratch. Think of them as carefully crafted templates that give better results than what users might come up with on their own.

![Diagram of an MCP client connecting to two MCP servers, each exposing Tools, Resources, and Prompts — with Prompts highlighted — in front of outside services](https://academy.claude.com/assets/media/2dfd2f9fcdfea8424d36b8323f892460291128c6cd96e7953011584e59cf4fb8.png)

## Why Use Prompts?

Here's the key insight: users can already ask Claude to do most tasks directly. For example, a user could type "reformat the report.pdf in markdown" and get decent results. But they'll get much better results if you provide a thoroughly tested, specialized prompt that handles edge cases and follows best practices.

As the MCP server author, you can spend time crafting, testing, and evaluating prompts that work consistently across different scenarios. Users benefit from this expertise without having to become prompt engineering experts themselves.

![Side-by-side comparison of the short prompt a user would write — "Convert report.pdf to markdown" — versus the much longer, thoroughly evaluated prompt an MCP server author can provide instead](https://academy.claude.com/assets/media/6ab55d7162ceb856be527d35317b17f5327a2e76d36ee4590d61c7f7292787a1.png)

## Building a Format Command

Let's implement a practical example: a format command that converts documents to markdown. Users will type `/format doc_id` and get back a professionally formatted markdown version of their document.

The workflow looks like this:

* User types `/` to see available commands
* They select `format` and specify a document ID
* Claude uses your pre-built prompt to read and reformat the document
* The result is clean markdown with proper headers, lists, and formatting

## Defining Prompts

Prompts use a similar decorator pattern to tools and resources:

python

```
@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format."
)
def format_document(
    doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
    prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:
<document_id>
{doc_id}
</document_id>

Add in headers, bullet points, tables, etc as necessary. Feel free to add in structure.
Use the 'edit_document' tool to edit the document. After the document has been reformatted...
"""

    return [
        base.UserMessage(prompt)
    ]
```

The function returns a list of messages that get sent directly to Claude. You can include multiple user and assistant messages to create more complex conversation flows.

## Testing Your Prompts

Use the MCP Inspector to test your prompts before deploying them:

![The MCP Inspector with the format prompt selected, showing the doc_id argument and the interpolated message that will be sent to Claude](https://academy.claude.com/assets/media/fd582104701b532c711ad7cf51c3272fba51b68bf4999e36ea28c2823d4d4576.png)

The inspector shows you exactly what messages will be sent to Claude, including how variables get interpolated into your prompt template. This lets you verify the prompt looks correct before users start relying on it.

## Key Benefits

* **Consistency** - Users get reliable results every time
* **Expertise** - You can encode domain knowledge into prompts
* **Reusability** - Multiple client applications can use the same prompts
* **Maintenance** - Update prompts in one place to improve all clients

Prompts work best when they're specialized for your MCP server's domain. A document management server might have prompts for formatting, summarizing, or analyzing documents. A data analysis server might have prompts for generating reports or visualizations.

The goal is to provide prompts that are so well-crafted and tested that users prefer them over writing their own instructions from scratch.
