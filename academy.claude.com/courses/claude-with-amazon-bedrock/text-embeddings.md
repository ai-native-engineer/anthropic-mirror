<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/text-embeddings -->

Lesson 35 of 65 · Claude with Amazon BedrockText embeddings

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Text embeddings

Lesson 355 min

After breaking a document into chunks, the next step in a RAG pipeline is finding which chunks are most relevant to a user's question. This is fundamentally a search problem - you need to look through all your text chunks and identify the ones that relate to what the user is asking about.

## Finding Relevant Chunks

The challenge is determining which chunks are "related" to a user's question. This isn't as simple as keyword matching - you need to understand the meaning and context of both the question and the chunks.

![](https://academy.claude.com/assets/media/644f01627e92ea5429173cb72c7e1764973b8c9b73821309115253fec0392dec.png)

The most common solution is semantic search, which uses text embeddings to understand what each piece of text is actually about, rather than just looking for exact word matches.

## What Are Text Embeddings?

A text embedding is a numerical representation of the meaning contained in some text. Think of it as converting words and sentences into a format that computers can work with mathematically.

![](https://academy.claude.com/assets/media/a3f8ebf9f863efb16c85fb5da3c81d87ca47d138b06e161a8a4abd9307cb6c66.png)

Here's how it works:

* You feed text into an embedding model
* The model outputs a long list of numbers (typically 1024 numbers)
* Each number represents a "score" for some quality of the input text
* The numbers range from -1 to +1

## Understanding the Numbers

Each number in an embedding is like a score for some aspect of the text. While we don't know exactly what each position represents, it's helpful to think of them as measuring different qualities.

![](https://academy.claude.com/assets/media/12f327b493d6106872ba6ec2ddb56320bc528bf34319c26d0a7ec48aa4a4e4a0.png)

For example, one number might score "how happy the text is" while another might measure "how much the text talks about oceans." The key point is that we don't actually know what each number represents - the embedding model learns these patterns during training, and they're not human-interpretable.

## Generating Embeddings with Code

Creating embeddings is straightforward. Here's the basic process:

python

```
def generate_embedding(
    text,
    embedding_model_id="amazon.titan-embed-text-v2:0",
    dimensions=1024,
    normalize=True,
):
    request_body = {
        "inputText": text,
        "dimensions": dimensions,
        "normalize": normalize,
    }

    request_json = json.dumps(request_body)
    response = client.invoke_model(
        modelId=embedding_model_id,
        body=request_json,
        accept="application/json",
        contentType="application/json",
    )

    response_body = json.loads(response.get("body").read())
    return response_body["embedding"]
```

When you run this function on a text chunk, you get back a list of 1024 numbers that represent the semantic meaning of that text.

Note that you might need to request access to the Titan embedding model in the AWS Bedrock console. If version 2 isn't available, version 1 works just as well for learning purposes.

## Why Embeddings Matter for RAG

The power of embeddings becomes clear when you realize that similar texts will have similar embedding values. This means you can mathematically compare a user's question to your document chunks and find the most semantically similar ones - even if they don't share the exact same words.

This numerical representation is what makes semantic search possible and much more effective than simple keyword matching for finding relevant context in RAG systems.

[Previous lessonText chunking strategies](https://academy.claude.com/courses/claude-with-amazon-bedrock/text-chunking-strategies)[Next lessonThe full RAG flow](https://academy.claude.com/courses/claude-with-amazon-bedrock/the-full-rag-flow)

Lesson 35 of 65 · Claude with Amazon BedrockText embeddings

Course introduction

* [Overview of Claude Models](https://academy.claude.com/courses/claude-with-amazon-bedrock/overview-of-claude-models)

Working with the API

* [Accessing the API](https://academy.claude.com/courses/claude-with-amazon-bedrock/accessing-the-api)
* [Making a request](https://academy.claude.com/courses/claude-with-amazon-bedrock/making-a-request)
* [Multi-Turn conversations](https://academy.claude.com/courses/claude-with-amazon-bedrock/multi-turn-conversations)
* [System prompts](https://academy.claude.com/courses/claude-with-amazon-bedrock/system-prompts)
* [Temperature](https://academy.claude.com/courses/claude-with-amazon-bedrock/temperature)
* [Streaming](https://academy.claude.com/courses/claude-with-amazon-bedrock/streaming)
* [Controlling model output](https://academy.claude.com/courses/claude-with-amazon-bedrock/controlling-model-output)
* [Structured data](https://academy.claude.com/courses/claude-with-amazon-bedrock/structured-data)
* [Quiz on working with the APIQuiz](https://academy.claude.com/courses/claude-with-amazon-bedrock/quiz-on-working-with-the-api)

Prompt evaluations

* [Prompt evaluation](https://academy.claude.com/courses/claude-with-amazon-bedrock/prompt-evaluation)
* [A typical eval workflow](https://academy.claude.com/courses/claude-with-amazon-bedrock/a-typical-eval-workflow)
* [Generating test datasets](https://academy.claude.com/courses/claude-with-amazon-bedrock/generating-test-datasets)
* [Running the eval](https://academy.claude.com/courses/claude-with-amazon-bedrock/running-the-eval)
* [Model based grading](https://academy.claude.com/courses/claude-with-amazon-bedrock/model-based-grading)
* [Code based grading](https://academy.claude.com/courses/claude-with-amazon-bedrock/code-based-grading)
* [Quiz on prompt evaluationsQuiz](https://academy.claude.com/courses/claude-with-amazon-bedrock/quiz-on-prompt-evaluations)

Prompt engineering

* [Prompt engineering](https://academy.claude.com/courses/claude-with-amazon-bedrock/prompt-engineering)
* [Being clear and direct](https://academy.claude.com/courses/claude-with-amazon-bedrock/being-clear-and-direct)
* [Being specific](https://academy.claude.com/courses/claude-with-amazon-bedrock/being-specific)
* [Structure with XML tags](https://academy.claude.com/courses/claude-with-amazon-bedrock/structure-with-xml-tags)
* [Providing examples](https://academy.claude.com/courses/claude-with-amazon-bedrock/providing-examples)
* [Quiz on prompt engineeringQuiz](https://academy.claude.com/courses/claude-with-amazon-bedrock/quiz-on-prompt-engineering)

Tool use

* [Introducing tool use](https://academy.claude.com/courses/claude-with-amazon-bedrock/introducing-tool-use)
* [Tool functions](https://academy.claude.com/courses/claude-with-amazon-bedrock/tool-functions)
* [JSON Schema for tools](https://academy.claude.com/courses/claude-with-amazon-bedrock/json-schema-for-tools)
* [Handling tool use responses](https://academy.claude.com/courses/claude-with-amazon-bedrock/handling-tool-use-responses)
* [Running tool functions](https://academy.claude.com/courses/claude-with-amazon-bedrock/running-tool-functions)
* [Sending tool results](https://academy.claude.com/courses/claude-with-amazon-bedrock/sending-tool-results)
* [Multi-Turn conversations with tools](https://academy.claude.com/courses/claude-with-amazon-bedrock/multi-turn-conversations-with-tools)
* [Adding multiple tools](https://academy.claude.com/courses/claude-with-amazon-bedrock/adding-multiple-tools)
* [Batch tool use](https://academy.claude.com/courses/claude-with-amazon-bedrock/batch-tool-use)
* [Structured data with tools](https://academy.claude.com/courses/claude-with-amazon-bedrock/structured-data-with-tools)
* [Flexible tool extraction](https://academy.claude.com/courses/claude-with-amazon-bedrock/flexible-tool-extraction)
* [The text editor tool](https://academy.claude.com/courses/claude-with-amazon-bedrock/the-text-editor-tool)
* [Quiz on tool useQuiz](https://academy.claude.com/courses/claude-with-amazon-bedrock/quiz-on-tool-use)

Retrieval Augmented Generation

* [Introducing Retrieval Augmented Generation](https://academy.claude.com/courses/claude-with-amazon-bedrock/introducing-retrieval-augmented-generation)
* [Text chunking strategies](https://academy.claude.com/courses/claude-with-amazon-bedrock/text-chunking-strategies)
* [Text embeddings](https://academy.claude.com/courses/claude-with-amazon-bedrock/text-embeddings)
* [The full RAG flow](https://academy.claude.com/courses/claude-with-amazon-bedrock/the-full-rag-flow)
* [Implementing the RAG flow](https://academy.claude.com/courses/claude-with-amazon-bedrock/implementing-the-rag-flow)
* [BM25 lexical search](https://academy.claude.com/courses/claude-with-amazon-bedrock/bm25-lexical-search)
* [A multi-search RAG pipeline](https://academy.claude.com/courses/claude-with-amazon-bedrock/a-multi-search-rag-pipeline)
* [Reranking results](https://academy.claude.com/courses/claude-with-amazon-bedrock/reranking-results)
* [Contextual retrieval](https://academy.claude.com/courses/claude-with-amazon-bedrock/contextual-retrieval)
* [Quiz on Retrieval Augmented GenerationQuiz](https://academy.claude.com/courses/claude-with-amazon-bedrock/quiz-on-retrieval-augmented-generation)

Features of Claude

* [Extended thinking](https://academy.claude.com/courses/claude-with-amazon-bedrock/extended-thinking)
* [Image support](https://academy.claude.com/courses/claude-with-amazon-bedrock/image-support)
* [PDF support](https://academy.claude.com/courses/claude-with-amazon-bedrock/pdf-support)
* [Citations](https://academy.claude.com/courses/claude-with-amazon-bedrock/citations)
* [Prompt caching](https://academy.claude.com/courses/claude-with-amazon-bedrock/prompt-caching)
* [Rules of prompt caching](https://academy.claude.com/courses/claude-with-amazon-bedrock/rules-of-prompt-caching)
* [Quiz on features of ClaudeQuiz](https://academy.claude.com/courses/claude-with-amazon-bedrock/quiz-on-features-of-claude)

Model Context Protocol

* [Introducing MCP](https://academy.claude.com/courses/claude-with-amazon-bedrock/introducing-mcp)
* [MCP clients](https://academy.claude.com/courses/claude-with-amazon-bedrock/mcp-clients)
* [Project setup](https://academy.claude.com/courses/claude-with-amazon-bedrock/project-setup)
* [Defining tools with MCP](https://academy.claude.com/courses/claude-with-amazon-bedrock/defining-tools-with-mcp)
* [The server inspector](https://academy.claude.com/courses/claude-with-amazon-bedrock/the-server-inspector)
* [Implementing a client](https://academy.claude.com/courses/claude-with-amazon-bedrock/implementing-a-client)
* [Defining resources](https://academy.claude.com/courses/claude-with-amazon-bedrock/defining-resources)
* [Accessing resources](https://academy.claude.com/courses/claude-with-amazon-bedrock/accessing-resources)
* [Defining prompts](https://academy.claude.com/courses/claude-with-amazon-bedrock/defining-prompts)
* [Prompts in the client](https://academy.claude.com/courses/claude-with-amazon-bedrock/prompts-in-the-client)
* [MCP review](https://academy.claude.com/courses/claude-with-amazon-bedrock/mcp-review)
* [Quiz on Model Context ProtocolQuiz](https://academy.claude.com/courses/claude-with-amazon-bedrock/quiz-on-model-context-protocol)

Agents

* [Claude Code in action](https://academy.claude.com/courses/claude-with-amazon-bedrock/claude-code-in-action)
* [Enhancements with MCP servers](https://academy.claude.com/courses/claude-with-amazon-bedrock/enhancements-with-mcp-servers)
* [Parallelizing Claude Code](https://academy.claude.com/courses/claude-with-amazon-bedrock/parallelizing-claude-code)
* [Automated debugging](https://academy.claude.com/courses/claude-with-amazon-bedrock/automated-debugging)
* [Computer Use](https://academy.claude.com/courses/claude-with-amazon-bedrock/computer-use)
* [How Computer Use works](https://academy.claude.com/courses/claude-with-amazon-bedrock/how-computer-use-works)
* [Qualities of agents](https://academy.claude.com/courses/claude-with-amazon-bedrock/qualities-of-agents)

Final assessment

* [Final assessment quizQuiz](https://academy.claude.com/courses/claude-with-amazon-bedrock/final-assessment-quiz)

* [Completion badge](https://academy.claude.com/courses/claude-with-amazon-bedrock/badge)

* [Finding Relevant Chunks](#finding-relevant-chunks)
* [What Are Text Embeddings?](#what-are-text-embeddings)
* [Understanding the Numbers](#understanding-the-numbers)
* [Generating Embeddings with Code](#generating-embeddings-with-code)
* [Why Embeddings Matter for RAG](#why-embeddings-matter-for-rag)
