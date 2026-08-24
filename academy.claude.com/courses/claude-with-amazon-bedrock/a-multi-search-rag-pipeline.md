<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/a-multi-search-rag-pipeline -->

Lesson 39 of 65 · Claude with Amazon BedrockA multi-search RAG pipeline

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# A multi-search RAG pipeline

Lesson 397 min

When you have both semantic search (vector embeddings) and lexical search (BM25) working independently, the next step is combining them into a unified search pipeline. This hybrid approach leverages the strengths of both methods to deliver more accurate results.

![](https://academy.claude.com/assets/media/961cd9717345a16435ab45da7572f0b9fa5c4125f4823018c271d8e33c7c9963.png)

## Building a Unified Interface

Both search implementations share nearly identical APIs - they both have `add_document()` and `search()` methods. This consistency makes it straightforward to wrap them in a single `Retriever` class that coordinates between the two approaches.

![](https://academy.claude.com/assets/media/3fbfcb27eda153712dfac8bdf83d4a93171aa4507f63a2df44724e9fbf2de91a.png)

The Retriever acts as a coordinator that:

* Receives a user's question
* Forwards it to both the VectorIndex and BM25Index
* Collects results from both systems
* Merges the results using a ranking algorithm

![](https://academy.claude.com/assets/media/1aae9ddbb1781429d0c3797b675cc9d0fd9d9e1a8fba70b49aa7bc510c29e6ab.png)

## Reciprocal Rank Fusion

The challenge lies in merging results from different search methods. Each system returns results with different scoring mechanisms, so you can't simply combine scores directly. Instead, we use a technique called Reciprocal Rank Fusion (RRF).

![](https://academy.claude.com/assets/media/109886b19d3a59d7d11952d789c8b446ca014e7ccf8cd289eccd58490ba46451.png)

Here's how RRF works with a practical example. Suppose your VectorIndex returns results ranked as: Section 2, Section 7, Section 6. Meanwhile, your BM25Index returns: Section 6, Section 2, Section 7.

![](https://academy.claude.com/assets/media/938a17fa4eccbea3668f59c5a4e7ab822fa05a50e07afc5946a0e1bfecd44d75.png)

To merge these results, you create a combined table showing each text chunk's rank from both systems:

![](https://academy.claude.com/assets/media/93f690ee13cd14bf23375161fe02601f943f188bf4a73ee4f3510b012b9acf24.png)

The RRF formula calculates a score for each document:

```
RRF_score(d) = Σ(1 / (k + rank_i(d)))
```

Where `k` is a constant (typically 60, though 1 works well for clearer results) and `rank_i(d)` is the rank of document `d` in the i-th ranking system.

![](https://academy.claude.com/assets/media/e032f44934036a65174bc1b0c8242b99abd2a76736db1773f249121e3d192137.png)

For each text chunk, you calculate:

* Section 2: 1.0/(1+1) + 1.0/(1+2) = 0.833
* Section 7: 1.0/(1+2) + 1.0/(1+3) = 0.583
* Section 6: 1.0/(1+3) + 1.0/(1+1) = 0.75

After sorting by score, the final ranking becomes: Section 2 (first), Section 6 (second), Section 7 (third).

![](https://academy.claude.com/assets/media/ed4b193934439db2890a4065c7437248a2aa956b1b47fd68e795b0e1161aae70.png)

## Implementation

The Retriever class implementation is straightforward:

python

```
class Retriever:
    def __init__(self, *indexes):
        self._indexes = list(indexes)

    def add_document(self, document):
        for index in self._indexes:
            index.add_document(document)

    def search(self, query_text, k=1, k_rrf=60):
        # Get results from all indexes
        all_results = []
        for idx, results in enumerate(all_results):
            for rank, (doc, _) in enumerate(results):
                # Track document ranks across systems
                # Apply RRF formula
                # Return merged, sorted results
```

![](https://academy.claude.com/assets/media/67939ad6d66d81afd52852de8afa576344c1e04479b9027686e67703f21eb2c9.png)

The key insight is that the RRF algorithm creates a unified ranking by considering how well each document performs across all search systems, rather than relying on any single scoring method.

## Testing the Hybrid Approach

When testing with a query like "what happened with INC-2023-Q4-011?", the hybrid approach delivers significantly better results than either method alone. Instead of getting unexpected results from pure vector search, you now get the most relevant cybersecurity incident report first, followed by related software engineering content.

![](https://academy.claude.com/assets/media/99e48f9eae840a3bddb1d226d4f9f4b0bfb372749ff212509f7b558d12a31dd6.png)

## Extensibility

The beauty of this design is its modularity. Since each search index implements the same interface (`add_document()` and `search()`), you can easily add new search methodologies to the system. Whether it's a different embedding model, a specialized domain search, or any other retrieval technique, as long as it follows the established API, it integrates seamlessly into the hybrid pipeline.

![](https://academy.claude.com/assets/media/0732ae059a29273832ad2998053b9bbee80d6a69e22811007a9b03a87a663bb0.png)

This hybrid search approach represents a significant improvement in retrieval accuracy by combining the semantic understanding of vector search with the precise keyword matching of lexical search, all unified through the mathematically sound RRF ranking algorithm.

[Previous lessonBM25 lexical search](https://academy.claude.com/courses/claude-with-amazon-bedrock/bm25-lexical-search)[Next lessonReranking results](https://academy.claude.com/courses/claude-with-amazon-bedrock/reranking-results)

Lesson 39 of 65 · Claude with Amazon BedrockA multi-search RAG pipeline

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

* [Building a Unified Interface](#building-a-unified-interface)
* [Reciprocal Rank Fusion](#reciprocal-rank-fusion)
* [Implementation](#implementation)
* [Testing the Hybrid Approach](#testing-the-hybrid-approach)
* [Extensibility](#extensibility)
