<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/a-multi-index-rag-pipeline -->

Lesson 40 of 66 · Claude with Google Cloud's Vertex AIA Multi-index RAG pipeline

3. /[Claude with Google Cloud's Vertex AI](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai)

[Claude with Google Cloud's Vertex AI](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai)

# A Multi-index RAG pipeline

Lesson 408 min

When you have both semantic search (vector embeddings) and lexical search (BM25) working independently, the next step is combining them into a unified search pipeline. This hybrid approach leverages the strengths of both methods to deliver more accurate results.

![](https://academy.claude.com/assets/media/961cd9717345a16435ab45da7572f0b9fa5c4125f4823018c271d8e33c7c9963.png)

## Creating a Unified Interface[](#creating-a-unified-interface)

Both search implementations share nearly identical APIs - they both have `add_document()` and `search()` methods that work the same way. This consistency makes it straightforward to wrap them in a single `Retriever` class.

![](https://academy.claude.com/assets/media/3fbfcb27eda153712dfac8bdf83d4a93171aa4507f63a2df44724e9fbf2de91a.png)

The Retriever acts as a coordinator that forwards user queries to both indexes, collects their results, and merges them into a single ranked list.

![](https://academy.claude.com/assets/media/1aae9ddbb1781429d0c3797b675cc9d0fd9d9e1a8fba70b49aa7bc510c29e6ab.png)

## Reciprocal Rank Fusion[](#reciprocal-rank-fusion)

The challenge is merging results from different search methods that use different scoring systems. Vector search returns cosine similarity scores, while BM25 returns relevance scores - you can't simply combine these numbers directly.

Instead, we use a technique called Reciprocal Rank Fusion (RRF). This method focuses on the rank position of results rather than their raw scores.

![](https://academy.claude.com/assets/media/109886b19d3a59d7d11952d789c8b446ca014e7ccf8cd289eccd58490ba46451.png)

Here's how it works with an example. Say your vector search returns sections 2, 7, and 6 in that order, while BM25 returns sections 6, 2, and 7. To merge these:

![](https://academy.claude.com/assets/media/938a17fa4eccbea3668f59c5a4e7ab822fa05a50e07afc5946a0e1bfecd44d75.png)

First, create a table showing each text chunk and its rank from both search methods:

* Section 2: Rank 1 from vector, rank 2 from BM25
* Section 7: Rank 2 from vector, rank 3 from BM25
* Section 6: Rank 3 from vector, rank 1 from BM25

![](https://academy.claude.com/assets/media/93f690ee13cd14bf23375161fe02601f943f188bf4a73ee4f3510b012b9acf24.png)

Then apply the RRF formula to calculate a combined score for each chunk:

```
RRF_score(d) = Σ(1 / (k + rank_i(d)))
```

Where `k` is a constant (typically 60, but we'll use 1 for clearer results) and `rank_i(d)` is the rank of document `d` in the i-th search result.

![](https://academy.claude.com/assets/media/e032f44934036a65174bc1b0c8242b99abd2a76736db1773f249121e3d192137.png)

For our example:

* Section 2: 1.0/(1+1) + 1.0/(1+2) = 0.833
* Section 7: 1.0/(1+2) + 1.0/(1+3) = 0.583
* Section 6: 1.0/(1+3) + 1.0/(1+1) = 0.75

![](https://academy.claude.com/assets/media/ed4b193934439db2890a4065c7437248a2aa956b1b47fd68e795b0e1161aae70.png)

The final ranking becomes: Section 2 (0.833), Section 6 (0.75), Section 7 (0.583). This makes intuitive sense - Section 2 performed well in both searches, Section 6 had mixed results, and Section 7 ranked lower overall.

![](https://academy.claude.com/assets/media/c17e3349fd61b432b819c67d700780f96f20f8b86ba881907b3fb4e323bd45ea.png)

## Implementation[](#implementation)

The Retriever class implementation is straightforward:

![](https://academy.claude.com/assets/media/67939ad6d66d81afd52852de8afa576344c1e04479b9027686e67703f21eb2c9.png)

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
        all_results = [index.search(query_text, k) for index in self._indexes]

        # Apply reciprocal rank fusion
        # ... merge logic here ...
```

![](https://academy.claude.com/assets/media/4b4b00e88ea9cc48222bf33c52963ba38e5f677028dd06e87bcd5f5c80b8188b.png)

The merge logic tracks document ranks across all search results, calculates RRF scores, and returns the top-k documents sorted by their combined scores.

## Testing the Hybrid Approach[](#testing-the-hybrid-approach)

When testing with the query "what happened with INC-2023-Q4-011?", the hybrid approach delivers much better results than vector search alone:

![](https://academy.claude.com/assets/media/1bf772a4caba54d5029b99c487a5b19f3cfef345ad09acf937d34f081a548c8c.png)

The results now correctly prioritize:

1. Section 10: Cybersecurity Analysis (the actual incident report)
2. Section 2: Software Engineering (relevant context)
3. Section 5: Legal Developments (less relevant but still related)

![](https://academy.claude.com/assets/media/99e48f9eae840a3bddb1d226d4f9f4b0bfb372749ff212509f7b558d12a31dd6.png)

## Benefits of the Hybrid Architecture[](#benefits-of-the-hybrid-architecture)

This design offers several advantages:

* **Modular design**: Each search index is implemented independently with the same API
* **Easy extensibility**: You can add new search methods by implementing the same `search()` and `add_document()` interface
* **Better accuracy**: Combines semantic understanding with exact keyword matching
* **Flexible fusion**: The RRF algorithm works regardless of how many search indexes you combine

![](https://academy.claude.com/assets/media/0732ae059a29273832ad2998053b9bbee80d6a69e22811007a9b03a87a663bb0.png)

The consistent API means you could easily add a third search index - perhaps one that specializes in named entity recognition or handles specific document types - and the Retriever would automatically incorporate its results into the final ranking.

![](https://academy.claude.com/assets/media/1ed3bf11f055466c304302dbcaff88f3a787cadb7d0cdbdd35fbae9714a95f96.png)

This hybrid search foundation provides significantly more robust retrieval than either method alone, setting up your RAG pipeline for better performance across a wider range of query types.

[Previous lessonBM25 lexical search](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/bm25-lexical-search)[Next lessonReranking results](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/reranking-results)

Lesson 40 of 66 · Claude with Google Cloud's Vertex AIA Multi-index RAG pipeline

Accessing Claude with the API

* [Accessing the API](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/accessing-the-api)
* [Vertex AI Setup](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/vertex-ai-setup)
* [Making a request](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/making-a-request)
* [Multi-turn conversations](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/multi-turn-conversations)
* [System prompts](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/system-prompts)
* [Temperature](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/temperature)
* [Response streaming](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/response-streaming)
* [Controlling model output](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/controlling-model-output)
* [Structured data](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/structured-data)
* [Quiz on accessing Claude with the APIQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-accessing-claude-with-the-api)

Prompt evaluation

* [Prompt evaluation](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-evaluation)
* [A typical eval workflow](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/a-typical-eval-workflow)
* [Generating test datasets](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/generating-test-datasets)
* [Running the eval](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/running-the-eval)
* [Model based grading](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/model-based-grading)
* [Code based grading](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/code-based-grading)
* [Quiz on prompt evaluationQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-prompt-evaluation)

Prompt engineering techniques

* [Prompt engineering](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-engineering)
* [Being clear and direct](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/being-clear-and-direct)
* [Being specific](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/being-specific)
* [Structure with XML tags](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/structure-with-xml-tags)
* [Providing examples](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/providing-examples)
* [Quiz on prompt engineering techniquesQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-prompt-engineering-techniques)

Tool use with Claude

* [Introducing tool use](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/introducing-tool-use)
* [Project overview](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/project-overview)
* [Tool functions](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/tool-functions)
* [Tool schemas](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/tool-schemas)
* [Handling message blocks](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/handling-message-blocks)
* [Sending tool results](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/sending-tool-results)
* [Multi-turn conversations with tools](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/multi-turn-conversations-with-tools)
* [Implementing multiple turns](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/implementing-multiple-turns)
* [Using multiple tools](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/using-multiple-tools)
* [The batch tool](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/the-batch-tool)
* [Tools for structured data](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/tools-for-structured-data)
* [The text edit tool](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/the-text-edit-tool)
* [The web search tool](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/the-web-search-tool)
* [Quiz on tool use with ClaudeQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-tool-use-with-claude)

Retrieval Augmented Generation

* [Introducing Retrieval Augmented Generation](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/introducing-retrieval-augmented-generation)
* [Text chunking strategies](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/text-chunking-strategies)
* [Text embeddings](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/text-embeddings)
* [The full RAG flow](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/the-full-rag-flow)
* [Implementing the RAG flow](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/implementing-the-rag-flow)
* [BM25 lexical search](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/bm25-lexical-search)
* [A Multi-index RAG pipeline](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/a-multi-index-rag-pipeline)
* [Reranking results](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/reranking-results)
* [Contextual retrieval](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/contextual-retrieval)
* [Quiz on Retrieval Augmented GenerationQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-retrieval-augmented-generation)

Features of Claude

* [Extended thinking](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/extended-thinking)
* [Image support](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/image-support)
* [Citations](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/citations)
* [Prompt caching](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-caching)
* [Rules of prompt caching](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/rules-of-prompt-caching)
* [Prompt caching in action](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-caching-in-action)
* [Quiz on features of ClaudeQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-features-of-claude)

Model Context Protocol

* [Introducing MCP](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/introducing-mcp)
* [MCP clients](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/mcp-clients)
* [Project setup](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/project-setup)
* [Defining tools with MCP](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/defining-tools-with-mcp)
* [The server inspector](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/the-server-inspector)
* [Implementing a client](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/implementing-a-client)
* [Defining resources](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/defining-resources)
* [Accessing resources](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/accessing-resources)
* [Defining prompts](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/defining-prompts)
* [Prompts in the client](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompts-in-the-client)
* [MCP review](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/mcp-review)
* [Quiz on Model Context ProtocolQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-model-context-protocol)

Agents and workflows

* [Agents and workflows](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/agents-and-workflows)
* [Parallelization workflows](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/parallelization-workflows)
* [Chaining workflows](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/chaining-workflows)
* [Routing workflows](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/routing-workflows)
* [Agents and tools](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/agents-and-tools)
* [Environment inspection](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/environment-inspection)
* [Workflows vs agents](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/workflows-vs-agents)
* [Quiz on agents and workflowsQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-agents-and-workflows)

Final assessment

* [Final assessment quizQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/final-assessment-quiz)

* [Completion badge](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/badge)

* [Creating a Unified Interface](#creating-a-unified-interface)
* [Reciprocal Rank Fusion](#reciprocal-rank-fusion)
* [Implementation](#implementation)
* [Testing the Hybrid Approach](#testing-the-hybrid-approach)
* [Benefits of the Hybrid Architecture](#benefits-of-the-hybrid-architecture)
