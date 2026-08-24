<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/the-full-rag-flow -->

Lesson 36 of 65 · Claude with Amazon BedrockThe full RAG flow

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# The full RAG flow

Lesson 364 min

Now that we've covered the basics of RAG, text chunking, and embeddings, let's walk through the complete RAG pipeline step by step. This detailed example will show you exactly how all the pieces fit together in a real implementation.

## Step 1: Chunk Your Source Text

First, we take our source document and break it into manageable chunks. For this example, we'll use two simple text sections:

* Section 1: Medical Research - "This year saw significant strides in our understanding of XDR-47, a 'bug' we have not seen before."
* Section 2: Software Engineering - "This division dedicated significant effort to studying various infection vectors in our distributed systems"

## Step 2: Generate Embeddings

Next, we convert each text chunk into numerical embeddings. To make this concept clear, let's imagine we have a perfect embedding model that always returns exactly two numbers, and we know what each number represents:

![](https://academy.claude.com/assets/media/7167baedf645f8c9620b90bc9246a1c67dc1f258a24e489bf6e2831c6f8da53f.png)

In our imaginary model:

* First number: How much the text talks about the medical field
* Second number: How much the text talks about software engineering

So our medical research section gets an embedding of `[0.97, 0.34]` - very medical, somewhat software-related due to the word "bug". The software engineering section gets `[0.30, 0.97]` - very software-focused, but "infection vectors" has medical connotations.

## Normalization

Before storing these embeddings, they go through a normalization process that scales each vector to have a magnitude of 1.0. This is typically handled automatically by your embedding API, but it's important to understand that it happens.

![](https://academy.claude.com/assets/media/5694ebd1a8d76478dfc3b92ff613a13a37462f7bdb18637c2a50271206952bec.png)

After normalization, our embeddings become `[0.944, 0.331]` and `[0.295, 0.955]`. We can visualize these on a unit circle where each point lies exactly on the circle's edge.

![](https://academy.claude.com/assets/media/f08995bf43ba665000a225838abda4129bece49b3d467a5c36764da9fde4a4ae.png)

## Step 3: Store in Vector Database

The normalized embeddings get stored in a vector database - a specialized database optimized for storing, comparing, and searching through long lists of numbers like our embeddings.

![](https://academy.claude.com/assets/media/c0f5e517c4260f85779a61cd731b5fe815963e0fcc9e4c055d00884a0a67e17c.png)

At this point, we pause. All the work so far has been preprocessing that happens ahead of time. Now we wait for a user to submit a query.

## Step 4: Process User Query

When a user asks a question like "I'm curious about the company. In particular, what did the software engineering dept do this year?", we run their query through the same embedding model.

![](https://academy.claude.com/assets/media/e182b15de5aa36467e88cd371317a10d6e7174780c7925d6e720ef63b0bcc01e.png)

This query gets embedded as `[0.1, 0.89]` - low medical score, high software engineering score. After normalization, it becomes `[0.112, 0.993]`.

## Step 5: Find Similar Embeddings

Now we ask the vector database: "Find the stored embedding that's closest to this user query embedding." The database returns the software engineering section because it's the most similar.

![](https://academy.claude.com/assets/media/02f8d982cfef4c9b7507f4e0ce7c5bcaefeed5907f99b07957e22cd0343e69dd.png)

## How Similarity Works: Cosine Similarity

The vector database uses cosine similarity to determine which embeddings are most similar. This measures the cosine of the angle between two vectors.

![](https://academy.claude.com/assets/media/e9e58d87d3810283a0ecb754f38d5741dbb8c25251cf16c05b5d910b615396c0.png)

Key points about cosine similarity:

* Results range from -1 to 1
* Values close to 1 mean very similar
* Values close to 0 mean perpendicular (unrelated)
* Values close to -1 mean completely opposite

The calculation uses the dot product formula: `cos(a) = (A · B) / (||A|| · ||B||)`

![](https://academy.claude.com/assets/media/1ead50fb7e5ab0b029b6104d96525dfc91aba61ee79bba14f41a9e36ba769900.png)

In our example, the user query has a cosine similarity of 0.983 with the software engineering chunk and only 0.398 with the medical research chunk. The software engineering chunk is clearly the better match.

## Cosine Distance

You'll often see "cosine distance" in vector database documentation. This is simply `1 - cosine similarity`, which gives us an easier-to-interpret number where:

* Values close to 0 mean high similarity
* Larger values mean less similarity

## Step 6: Build the Final Prompt

Finally, we take the user's question and the most relevant text chunk we found, then combine them into a prompt for Claude:

![](https://academy.claude.com/assets/media/0a7e460e7f0bb53f7bc3f0b40cbc9c62257f50dfc9fdae2cc2dcabfa1ea358eb.png)

The prompt includes both the user's question and the relevant context from our document, allowing Claude to provide an informed answer based on the specific information in our knowledge base.

## The Complete Flow

That's the entire RAG pipeline from start to finish:

1. Chunk source documents
2. Generate embeddings for each chunk
3. Store embeddings in a vector database
4. When a user asks a question, embed their query
5. Find the most similar stored embeddings using cosine similarity
6. Add the relevant chunks to a prompt with the user's question
7. Send the enhanced prompt to Claude for a response

Understanding this process and the math behind it will help you work effectively with vector databases and debug issues when your RAG system isn't returning the results you expect.

[Previous lessonText embeddings](https://academy.claude.com/courses/claude-with-amazon-bedrock/text-embeddings)[Next lessonImplementing the RAG flow](https://academy.claude.com/courses/claude-with-amazon-bedrock/implementing-the-rag-flow)

Lesson 36 of 65 · Claude with Amazon BedrockThe full RAG flow

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

* [Step 1: Chunk Your Source Text](#step-1-chunk-your-source-text)
* [Step 2: Generate Embeddings](#step-2-generate-embeddings)
* [Normalization](#normalization)
* [Step 3: Store in Vector Database](#step-3-store-in-vector-database)
* [Step 4: Process User Query](#step-4-process-user-query)
* [Step 5: Find Similar Embeddings](#step-5-find-similar-embeddings)
* [How Similarity Works: Cosine Similarity](#how-similarity-works-cosine-similarity)
* [Cosine Distance](#cosine-distance)
* [Step 6: Build the Final Prompt](#step-6-build-the-final-prompt)
* [The Complete Flow](#the-complete-flow)
