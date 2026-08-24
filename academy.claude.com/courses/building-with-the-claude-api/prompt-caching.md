<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/prompt-caching -->

Lesson 43 of 67 · Building with the Claude APIPrompt caching

3. /[Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api)

[Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api)

# Prompt caching

Lesson 432 min

Prompt caching is a feature that speeds up Claude's responses and reduces the cost of text generation by reusing computational work from previous requests. Instead of throwing away all the processing work after each request, Claude can save and reuse it when you send similar content again.

## How Claude Normally Processes Requests

To understand prompt caching, let's first look at what happens during a typical request without caching enabled.

![](https://academy.claude.com/assets/media/f34cfa8bf918544d8a4e65f33ee2a4a05df4b0e28c320fe58209e698fe879d0f.jpg)

When you send a message to Claude, it doesn't immediately start generating a response. Instead, Claude does a tremendous amount of preprocessing work on your input:

![](https://academy.claude.com/assets/media/2c5fc9b8ab8589af3aaf26b0c0665ec1a9e089f9179e38b8f8465d286c104709.jpg)

* Tokenizes the prompt into smaller pieces
* Creates embeddings for each token
* Adds context based on surrounding text
* Only then generates the actual output text

After sending you the response, Claude throws away all this computational work - the tokenization, embeddings, and context analysis all get discarded.

![](https://academy.claude.com/assets/media/c5670ac3a8561da33cfc6e7a1422f0ea6c4b3ff4be41950c6052ae130f608365.jpg)

## The Problem with Discarding Work

This becomes inefficient when you make follow-up requests that include the same content. For example, in a conversation where you're asking Claude to refine a summary of the same long text:

![](https://academy.claude.com/assets/media/162ab5f5fd0caa46c6da9ebc1b3027957dbd1134738199add3b54de2f830b602.jpg)

Claude has to repeat all the same preprocessing work on content it just analyzed moments ago. As Claude might think to itself: "I just processed that message and threw away all the work I did - I could have reused it!"

![](https://academy.claude.com/assets/media/3e5343f6f0943e88aac09a6b77080067181f0f6a66a7248b75c87567b34c5d11.jpg)

## How Prompt Caching Solves This

Prompt caching changes this workflow by saving the preprocessing work instead of discarding it:

![](https://academy.claude.com/assets/media/c53467e87036b0620d17f59efb60a8f2f2901c8b45932d3cbb1a86d9d8385797.jpg)

When you make an initial request, Claude performs all the usual preprocessing but stores the results in a cache instead of throwing them away. The cache acts like a lookup table that says "If I ever see this message again, I'll reuse this work I already did."

![](https://academy.claude.com/assets/media/4bbeab1fdbfa0b11b72db93eb6bf1387decf17ac54318d1a57a341b731914bb9.jpg)

## Key Benefits and Limitations

![](https://academy.claude.com/assets/media/78e580715d88f89b2704b59d9cf39db06990cf031d081efff2b72ba6df0d1603.jpg)

Prompt caching offers several advantages:

* **Faster responses:** Requests using cached content execute more quickly
* **Lower costs:** You pay less for the cached portions of your requests
* **Automatic optimization:** The initial request writes to the cache, follow-up requests read from it

However, there are important limitations to keep in mind:

* **Cache duration:** By default, cached content lives for 5 minutes, and each reuse refreshes that timer at no extra cost. You can optionally extend the lifetime to 1 hour, which carries a higher cache-write price.
* **Limited use cases:** Only beneficial when you're repeatedly sending the same content
* **High frequency requirement:** Most effective when the same content appears extremely frequently in your requests

Prompt caching works best for scenarios like document analysis workflows, where you're asking multiple questions about the same large document, or iterative editing tasks where the base content remains constant while you refine specific aspects.

[Previous lessonCitations](https://academy.claude.com/courses/building-with-the-claude-api/citations)[Next lessonRules of prompt caching](https://academy.claude.com/courses/building-with-the-claude-api/rules-of-prompt-caching)

Lesson 43 of 67 · Building with the Claude APIPrompt caching

Accessing Claude with the API

* [Accessing the API](https://academy.claude.com/courses/building-with-the-claude-api/accessing-the-api)
* [Getting an API key](https://academy.claude.com/courses/building-with-the-claude-api/getting-an-api-key)
* [Making a request](https://academy.claude.com/courses/building-with-the-claude-api/making-a-request)
* [Multi-Turn conversations](https://academy.claude.com/courses/building-with-the-claude-api/multi-turn-conversations)
* [System prompts](https://academy.claude.com/courses/building-with-the-claude-api/system-prompts)
* [Temperature](https://academy.claude.com/courses/building-with-the-claude-api/temperature)
* [Response streaming](https://academy.claude.com/courses/building-with-the-claude-api/response-streaming)
* [Structured data](https://academy.claude.com/courses/building-with-the-claude-api/structured-data)
* [Quiz on accessing Claude with the APIQuiz](https://academy.claude.com/courses/building-with-the-claude-api/quiz-on-accessing-claude-with-the-api)

Prompt evaluation

* [Prompt evaluation](https://academy.claude.com/courses/building-with-the-claude-api/prompt-evaluation)
* [A typical eval workflow](https://academy.claude.com/courses/building-with-the-claude-api/a-typical-eval-workflow)
* [Generating test datasets](https://academy.claude.com/courses/building-with-the-claude-api/generating-test-datasets)
* [Running the eval](https://academy.claude.com/courses/building-with-the-claude-api/running-the-eval)
* [Model based grading](https://academy.claude.com/courses/building-with-the-claude-api/model-based-grading)
* [Code based grading](https://academy.claude.com/courses/building-with-the-claude-api/code-based-grading)
* [Quiz on prompt evaluationQuiz](https://academy.claude.com/courses/building-with-the-claude-api/quiz-on-prompt-evaluation)

Prompt engineering techniques

* [Prompt engineering](https://academy.claude.com/courses/building-with-the-claude-api/prompt-engineering)
* [Being clear and direct](https://academy.claude.com/courses/building-with-the-claude-api/being-clear-and-direct)
* [Being specific](https://academy.claude.com/courses/building-with-the-claude-api/being-specific)
* [Structure with XML tags](https://academy.claude.com/courses/building-with-the-claude-api/structure-with-xml-tags)
* [Providing examples](https://academy.claude.com/courses/building-with-the-claude-api/providing-examples)
* [Quiz on prompt engineering techniquesQuiz](https://academy.claude.com/courses/building-with-the-claude-api/quiz-on-prompt-engineering-techniques)

Tool use with Claude

* [Introducing tool use](https://academy.claude.com/courses/building-with-the-claude-api/introducing-tool-use)
* [Project overview](https://academy.claude.com/courses/building-with-the-claude-api/project-overview)
* [Tool functions](https://academy.claude.com/courses/building-with-the-claude-api/tool-functions)
* [Tool schemas](https://academy.claude.com/courses/building-with-the-claude-api/tool-schemas)
* [Handling message blocks](https://academy.claude.com/courses/building-with-the-claude-api/handling-message-blocks)
* [Sending tool results](https://academy.claude.com/courses/building-with-the-claude-api/sending-tool-results)
* [Multi-turn conversations with tools](https://academy.claude.com/courses/building-with-the-claude-api/multi-turn-conversations-with-tools)
* [Implementing multiple turns](https://academy.claude.com/courses/building-with-the-claude-api/implementing-multiple-turns)
* [Using multiple tools](https://academy.claude.com/courses/building-with-the-claude-api/using-multiple-tools)
* [Fine grained tool calling](https://academy.claude.com/courses/building-with-the-claude-api/fine-grained-tool-calling)
* [The text edit tool](https://academy.claude.com/courses/building-with-the-claude-api/the-text-edit-tool)
* [The web search tool](https://academy.claude.com/courses/building-with-the-claude-api/the-web-search-tool)
* [Quiz on tool use with ClaudeQuiz](https://academy.claude.com/courses/building-with-the-claude-api/quiz-on-tool-use-with-claude)

RAG and Agentic Search

* [Introducing Retrieval Augmented Generation](https://academy.claude.com/courses/building-with-the-claude-api/introducing-retrieval-augmented-generation)
* [Text chunking strategies](https://academy.claude.com/courses/building-with-the-claude-api/text-chunking-strategies)
* [Text embeddings](https://academy.claude.com/courses/building-with-the-claude-api/text-embeddings)
* [The full RAG flow](https://academy.claude.com/courses/building-with-the-claude-api/the-full-rag-flow)
* [Implementing the RAG flow](https://academy.claude.com/courses/building-with-the-claude-api/implementing-the-rag-flow)
* [BM25 lexical search](https://academy.claude.com/courses/building-with-the-claude-api/bm25-lexical-search)
* [A Multi-Index RAG pipeline](https://academy.claude.com/courses/building-with-the-claude-api/a-multi-index-rag-pipeline)

Features of Claude

* [Extended thinking](https://academy.claude.com/courses/building-with-the-claude-api/extended-thinking)
* [Image support](https://academy.claude.com/courses/building-with-the-claude-api/image-support)
* [PDF support](https://academy.claude.com/courses/building-with-the-claude-api/pdf-support)
* [Citations](https://academy.claude.com/courses/building-with-the-claude-api/citations)
* [Prompt caching](https://academy.claude.com/courses/building-with-the-claude-api/prompt-caching)
* [Rules of prompt caching](https://academy.claude.com/courses/building-with-the-claude-api/rules-of-prompt-caching)
* [Prompt caching in action](https://academy.claude.com/courses/building-with-the-claude-api/prompt-caching-in-action)
* [Code execution and the Files API](https://academy.claude.com/courses/building-with-the-claude-api/code-execution-and-the-files-api)
* [Quiz on features of ClaudeQuiz](https://academy.claude.com/courses/building-with-the-claude-api/quiz-on-features-of-claude)

Model Context Protocol

* [Introducing MCP](https://academy.claude.com/courses/building-with-the-claude-api/introducing-mcp)
* [MCP clients](https://academy.claude.com/courses/building-with-the-claude-api/mcp-clients)
* [Project setup](https://academy.claude.com/courses/building-with-the-claude-api/project-setup)
* [Defining tools with MCP](https://academy.claude.com/courses/building-with-the-claude-api/defining-tools-with-mcp)
* [The server inspector](https://academy.claude.com/courses/building-with-the-claude-api/the-server-inspector)
* [Implementing a client](https://academy.claude.com/courses/building-with-the-claude-api/implementing-a-client)
* [Defining resources](https://academy.claude.com/courses/building-with-the-claude-api/defining-resources)
* [Accessing resources](https://academy.claude.com/courses/building-with-the-claude-api/accessing-resources)
* [Defining prompts](https://academy.claude.com/courses/building-with-the-claude-api/defining-prompts)
* [Prompts in the client](https://academy.claude.com/courses/building-with-the-claude-api/prompts-in-the-client)
* [Quiz on Model Context ProtocolQuiz](https://academy.claude.com/courses/building-with-the-claude-api/quiz-on-model-context-protocol)

Anthropic apps - Claude Code and computer use

* [Anthropic apps](https://academy.claude.com/courses/building-with-the-claude-api/anthropic-apps)
* [Claude Code setup](https://academy.claude.com/courses/building-with-the-claude-api/claude-code-setup)
* [Claude Code in action](https://academy.claude.com/courses/building-with-the-claude-api/claude-code-in-action)
* [Enhancements with MCP servers](https://academy.claude.com/courses/building-with-the-claude-api/enhancements-with-mcp-servers)

Agents and workflows

* [Agents and workflows](https://academy.claude.com/courses/building-with-the-claude-api/agents-and-workflows)
* [Parallelization workflows](https://academy.claude.com/courses/building-with-the-claude-api/parallelization-workflows)
* [Chaining workflows](https://academy.claude.com/courses/building-with-the-claude-api/chaining-workflows)
* [Routing workflows](https://academy.claude.com/courses/building-with-the-claude-api/routing-workflows)
* [Agents and tools](https://academy.claude.com/courses/building-with-the-claude-api/agents-and-tools)
* [Environment inspection](https://academy.claude.com/courses/building-with-the-claude-api/environment-inspection)
* [Workflows vs agents](https://academy.claude.com/courses/building-with-the-claude-api/workflows-vs-agents)
* [Quiz on Agents and WorkflowsQuiz](https://academy.claude.com/courses/building-with-the-claude-api/quiz-on-agents-and-workflows)

Final assessment

* [Final AssessmentQuiz](https://academy.claude.com/courses/building-with-the-claude-api/final-assessment)

* [Completion badge](https://academy.claude.com/courses/building-with-the-claude-api/badge)

* [How Claude Normally Processes Requests](#how-claude-normally-processes-requests)
* [The Problem with Discarding Work](#the-problem-with-discarding-work)
* [How Prompt Caching Solves This](#how-prompt-caching-solves-this)
* [Key Benefits and Limitations](#key-benefits-and-limitations)
