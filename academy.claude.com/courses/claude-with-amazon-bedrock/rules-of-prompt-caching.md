<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/rules-of-prompt-caching -->

Lesson 47 of 65 · Claude with Amazon BedrockRules of prompt caching

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Rules of prompt caching

Lesson 4710 min

Prompt caching in Claude works by storing the computational work done on messages so it can be reused in follow-up requests. This makes subsequent requests both cheaper and faster to execute, but only when you're repeatedly sending the same content.

![](https://academy.claude.com/assets/media/097732ecdd541098bf4f1bfd3c4ae1b9893223af3b2c07be2f928667986ccfb4.png)

The process follows a two-phase pattern: the initial request writes to the cache, and follow-up requests can read from it. The cache only lives for 5 minutes, so this feature is most useful when you're sending the same content repeatedly within a short timeframe.

## Cache Points

Prompt caching isn't enabled automatically - you need to manually add cache point message parts to control what gets cached. Cache points tell Claude to cache all the work done for everything before that point in your message.

![](https://academy.claude.com/assets/media/a5cae96fc1ad655e0338fda4f6b2d4fd282f5bc8de8e9d7e5bb674df66c50ad8.png)

Here's how you add a cache point to a user message:

python

```
user_message = {
  "role": "user",
  "content": [
    {"text": ""},
    {"cachePoint": {"type": "default"}}
  ]
}
```

The key rule is that work done for everything before the cache point will be cached, but anything after the cache point won't be stored in the cache.

## How Cache Points Work

![](https://academy.claude.com/assets/media/c5fbe6101c5953ab6a8e4a24d28b9ef5fe36a7c26c20d295e14efd498652f31f.png)

When you make an initial request with a cache point, Claude processes all the content and stores the work done up to that cache point. On follow-up requests, if the content before the cache point is identical, Claude reads the previously processed work from cache instead of reprocessing it.

![](https://academy.claude.com/assets/media/6c453da9b6bf10b9907fe5ffdc09058be052f4a7c8da298b337f81a8c663d317.png)

The cache will only be used if the content before the cache point is completely identical. Even small changes like adding "Please" to the beginning of your prompt will prevent cache usage, forcing Claude to process everything from scratch.

![](https://academy.claude.com/assets/media/9a7504d0101bbcb1abbb4079bdd4e3fb01563ace29c74714cdb4fa171978d1e4.png)

## Caching Across Messages

Cache points can span multiple messages and even include assistant messages. This means you can cache entire conversation histories up to a certain point.

![](https://academy.claude.com/assets/media/af18cf98e69870372338b1feceb3fb6b7ee86028f8afc2a85c1b0d94463bdc21.png)

For example, you might have a conversation with a user message, assistant response, and another user message, with a cache point at the end. All the processing work for that entire conversation thread gets cached and can be reused.

## Minimum Content Length

Content must be at least 1024 tokens long to be cached. This is the sum of all messages and parts you're trying to cache before the cache point.

![](https://academy.claude.com/assets/media/d0ef1cc4dc937f9d0324d64e61d382a9c0050d4c2df85857202b1e0741445644.png)

A simple "Hi there!" message won't meet the 1024 token minimum, so nothing gets cached. But if you repeat "Hi there!" 500 times, that would exceed 1024 tokens and qualify for caching.

## Cache Point Locations

Cache points aren't restricted to user messages. You can add them to system prompts and tool definitions, which are actually the most common caching opportunities.

![](https://academy.claude.com/assets/media/b0cbe00c845760ca9af1fcab79e6acadc78530e5eb99ac74a074827b121f4096.png)

For tool definitions:

python

```
tools = [
  {"toolSpec": add_duration_to_datetime_schema},
  {"toolSpec": get_current_datetime_schema},
  {"cachePoint": {"type": "default"}}
]
```

For system prompts:

python

```
system = [
  {"text": "You are a senior software..."},
  {"cachePoint": {"type": "default"}}
]
```

These are the most valuable caching opportunities because system prompts and tool lists rarely change between requests, making them perfect candidates for caching.

[Previous lessonPrompt caching](https://academy.claude.com/courses/claude-with-amazon-bedrock/prompt-caching)[Next lessonQuiz on features of Claude](https://academy.claude.com/courses/claude-with-amazon-bedrock/quiz-on-features-of-claude)

Lesson 47 of 65 · Claude with Amazon BedrockRules of prompt caching

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

* [Cache Points](#cache-points)
* [How Cache Points Work](#how-cache-points-work)
* [Caching Across Messages](#caching-across-messages)
* [Minimum Content Length](#minimum-content-length)
* [Cache Point Locations](#cache-point-locations)
