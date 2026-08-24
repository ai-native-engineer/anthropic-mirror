<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/contextual-retrieval -->

Lesson 42 of 66 · Claude with Google Cloud's Vertex AIContextual retrieval

Contextual retrieval is a technique that improves RAG pipeline accuracy by solving a fundamental problem: when you split a document into chunks, each chunk loses its connection to the broader document context.

## The Problem with Standard Chunking

When you take a source document and break it into chunks for your vector database, each individual piece no longer knows where it came from or how it relates to the rest of the document. This can hurt retrieval accuracy because the chunks lack important contextual information.

![](https://academy.claude.com/assets/media/e3b6f9ccb54e4c38966ff1e694675a8d2227d273053cbaaffa2810417dd87faa.png)

## How Contextual Retrieval Works

Contextual retrieval adds a preprocessing step before inserting chunks into your retriever database. Here's the process:

* Take each individual chunk and the original source document
* Send both to Claude with a specific prompt asking it to add context
* Claude generates a short snippet that "situates" the chunk within the larger document
* Combine this context with the original chunk to create a "contextualized chunk"
* Use the contextualized chunk in your vector and BM25 indexes

![](https://academy.claude.com/assets/media/7f95046530589905e2e8e53619707a534e4b0c553c1712984a966f50018ac0e7.png)

For example, if you have a section about software engineering that mentions a 2023 incident, Claude might generate context like: "This section is from a larger report about a cross-discipline group. It includes mention of INC-2023-04-011, which is also mentioned in the Cybersecurity Analysis section."

![](https://academy.claude.com/assets/media/49504d077fb3bf4824aeb3fcf10c76b838304ff4263ded2458a2244cc7603973.png)

## Handling Large Documents

A common problem is when your source document is too large to fit into Claude's context window. You can still use contextual retrieval by providing a reduced set of context:

![](https://academy.claude.com/assets/media/ef029b4478a742b0a689cd2c43ea1309adbef8d78c7a5a83e25784dc2c6dba24.png)

Instead of including the entire document, provide:

* A few chunks from the start of the document (often containing summaries or abstracts)
* Chunks immediately before the chunk you're contextualizing

This approach gives Claude enough information to understand the document structure and immediate context without overwhelming the prompt.

## Implementation Example

Here's a basic function for adding context to chunks:

python

```
def add_context(text_chunk, source_text):
    prompt = """
Write a short and succinct snippet of text to situate this chunk within the
overall source document for the purposes of improving search retrieval of the chunk.

Here is the original source document:
<document>
{source_text}
</document>

Here is the chunk we want to situate within the whole document:
<chunk>
{text_chunk}
</chunk>

Answer only with the succinct context and nothing else.
"""

    messages = []
    add_user_message(messages, prompt)
    result = chat(messages)

    return result["text"] + "\n" + text_chunk
```

For large documents, you can implement a strategy that selects relevant context chunks:

python

```
# Add context to each chunk, then add to the retriever
num_start_chunks = 2
num_prev_chunks = 2

for i, chunk in enumerate(chunks):
    context_parts = []

    # Initial set of chunks from the start of the doc
    context_parts.extend(chunks[: min(num_start_chunks, len(chunks))])

    # Additional chunks ahead of the current chunk we're contextualizing
    start_idx = max(0, i - num_prev_chunks)
    context_parts.extend(chunks[start_idx:i])

    context = "\n".join(context_parts)

    contextualized_chunk = add_context(chunk, context)
    retriever.add_document({"content": contextualized_chunk})
```

## When to Use Contextual Retrieval

This technique is most valuable when:

* Your documents have complex internal relationships between sections
* Chunks reference concepts defined elsewhere in the document
* Understanding the document structure is important for accurate retrieval
* You're working with technical documents, reports, or academic papers

While contextual retrieval adds processing time and cost (since you're making additional API calls), it can significantly improve retrieval accuracy for complex documents where context matters.
