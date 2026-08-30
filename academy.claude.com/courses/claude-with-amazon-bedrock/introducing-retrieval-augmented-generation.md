<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/introducing-retrieval-augmented-generation -->

Lesson 33 of 65 · Claude with Amazon BedrockIntroducing Retrieval Augmented Generation

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Introducing Retrieval Augmented Generation

Lesson 333 min

Retrieval Augmented Generation (RAG) is a technique that helps you work with large documents by breaking them into smaller pieces and only feeding Claude the most relevant chunks for each question. Instead of overwhelming the model with an entire 800-page financial report, RAG lets you extract just the sections that matter for answering specific queries.

## The Problem with Large Documents[](#the-problem-with-large-documents)

When you have a massive document and want to ask Claude specific questions about it, you face a fundamental challenge: how do you get the right information to Claude without hitting limits or degrading performance?

![](https://academy.claude.com/assets/media/aa2d6dcef1136beb3f94eac3d88c0e58c286f71cf7e6ba9c5711a9d75d987d86.png)

Consider asking "What risk factors does this company have?" about a lengthy financial document. The document contains the answer, but Claude needs access to the relevant content to help you.

## Option 1: Include Everything in the Prompt[](#option-1-include-everything-in-the-prompt)

The straightforward approach is extracting all text from the document and stuffing it into a single prompt:

![](https://academy.claude.com/assets/media/38c79483e6c91a124d55658918a5ab20523aa8089d0e031360e5f45d25078624.png)

This method has serious limitations:

* Hard token limits mean very long documents simply won't fit
* Claude becomes less effective with extremely long prompts
* Larger prompts cost more money and take longer to process
* Performance degrades when there's too much information to sift through

## Option 2: Break Documents into Chunks[](#option-2-break-documents-into-chunks)

RAG takes a smarter approach by preprocessing documents into manageable pieces, then retrieving only the relevant chunks for each question.

![](https://academy.claude.com/assets/media/1a6d91701aed328e1e8a964098476303554d0ee3dbc081f14ea8c0c7184c3142.png)

Here's how it works:

1. Split the document into smaller chunks (Strategy Outlook, Risk Factors, Balance Sheet, etc.)
2. When a user asks a question, analyze what they're looking for
3. Find the chunks most relevant to their question
4. Include only those relevant chunks in the prompt to Claude

![](https://academy.claude.com/assets/media/b28946e9396a7c6f9015727c34b282669ab472c30081b79cb1639c85df4c40e0.png)

For a question about company risks, the system would identify and retrieve the "Risk Factors" chunk, giving Claude focused, relevant context instead of the entire document.

## Benefits of RAG[](#benefits-of-rag)

* Claude can focus on only the most relevant content
* Scales to very large documents and multiple documents
* Works across document collections, not just single files
* Smaller prompts mean faster processing and lower costs

## Challenges with RAG[](#challenges-with-rag)

RAG introduces complexity that you need to manage:

* Requires a preprocessing step to chunk documents
* Need a search mechanism to find relevant chunks
* Retrieved chunks might not contain all necessary context
* Many different ways to chunk text - which approach works best?

You can chunk documents by equal portions, by headers and sections, by semantic meaning, or other strategies. Each approach has tradeoffs you'll need to evaluate for your specific use case.

## When to Use RAG[](#when-to-use-rag)

RAG shines when you're working with large documents or document collections where users ask specific questions that only require portions of the content. The preprocessing complexity pays off when you need to scale beyond what fits in a single prompt, when you want faster responses, or when you're managing costs across many queries.

The key is analyzing whether the technical overhead of implementing chunking, search, and retrieval makes sense for your particular application. Sometimes the simple "dump everything in a prompt" approach works fine - other times, RAG becomes essential for making your system practical and performant.

[Previous lessonQuiz on tool use](https://academy.claude.com/courses/claude-with-amazon-bedrock/quiz-on-tool-use)[Next lessonText chunking strategies](https://academy.claude.com/courses/claude-with-amazon-bedrock/text-chunking-strategies)

Lesson 33 of 65 · Claude with Amazon BedrockIntroducing Retrieval Augmented Generation

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

* [The Problem with Large Documents](#the-problem-with-large-documents)
* [Option 1: Include Everything in the Prompt](#option-1-include-everything-in-the-prompt)
* [Option 2: Break Documents into Chunks](#option-2-break-documents-into-chunks)
* [Benefits of RAG](#benefits-of-rag)
* [Challenges with RAG](#challenges-with-rag)
* [When to Use RAG](#when-to-use-rag)
