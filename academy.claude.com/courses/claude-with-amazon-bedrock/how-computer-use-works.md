<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/how-computer-use-works -->

Lesson 64 of 65 · Claude with Amazon BedrockHow Computer Use works

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# How Computer Use works

Lesson 643 min

Computer use in Claude works exactly like regular tool use - it's built on the same foundation you're already familiar with. The key difference is that instead of calling a weather API or database function, Claude is making requests to control a computer interface.

## Tool Use Refresher

Before diving into computer use, let's quickly review how standard tool use works. When you want Claude to use a tool, you send a request that includes both a user message and a tool schema. The tool schema describes the additional functionality you want to expose to Claude.

![](https://academy.claude.com/assets/media/f4d077c8292d0a37e95c2ddca623e45dbac42d8ef11e281a3d89e7b135059873.png)

Here's the typical flow:

1. You send Claude a question along with available tool schemas
2. Claude analyzes the request and decides it needs to use a tool
3. Claude responds with a tool use request containing the tool name and required inputs
4. Your server executes the tool function and returns the result
5. You send the tool result back to Claude

![](https://academy.claude.com/assets/media/d9d83a6056318aa99872c9bb70b721797ba4223cbf93c0144b7509b761317648.png)

For example, if you ask about weather in San Francisco, Claude might call a `get_weather` function with the location parameter, your server fetches the weather data, and you return the result to Claude.

![](https://academy.claude.com/assets/media/b58e95288655e5f2490b8be8b68ad763c8cbc0964b650cf39c9c78851ab87581.png)

## Computer Use: Same Flow, Different Tool

Computer use follows this exact same pattern. The difference is in what the "tool" actually does - instead of fetching weather data, it simulates computer interactions like mouse clicks and keyboard input.

![](https://academy.claude.com/assets/media/7c359ef8d7714fbf80176d332343ccebb580752c41150025ac825314669c02ee.png)

When you enable computer use, you send Claude a special tool schema that gets automatically expanded behind the scenes. What starts as a simple schema on your end becomes a comprehensive interface that tells Claude it can perform actions like:

* Mouse movements and clicks
* Keyboard input and key combinations
* Taking screenshots
* Scrolling and other interface interactions

![](https://academy.claude.com/assets/media/3cb7af73c4a24c1861183ce69a0372cbf06e92950c492e522512c7c9fccb8d07.png)

The tool schema you send is minimal, but it automatically converts into a detailed specification that includes all the computer interaction capabilities Claude needs.

![](https://academy.claude.com/assets/media/106668c3e02cf97566f702349a7ac220bacc904b69c30f81009bc7ded4e5c8a0.png)

## The Technical Implementation

To make computer use work, you need a computing environment that can programmatically execute the actions Claude requests. The reference implementation uses a Docker container running Firefox, along with code that can simulate keypresses and mouse movements.

When Claude decides to interact with the computer, it sends a tool use request just like any other tool. Your server receives this request and executes the corresponding action in the containerized environment - whether that's clicking a button, typing text, or taking a screenshot.

The important thing to understand is that Claude isn't directly controlling a computer. It's making tool requests, and your infrastructure translates those requests into actual computer interactions.

## Getting Started

You don't need to build this infrastructure from scratch. Anthropic provides a reference implementation that handles all the complex parts for you.

![](https://academy.claude.com/assets/media/e8bf080606418b4207fb62709feecd446df055a93b12908794314c52df123bfc.png)

To set up computer use, you need:

1. A Docker runtime installed on your system
2. An AWS profile configured locally (usually "default")
3. The reference implementation from the Anthropic quickstarts repository

Once you have these prerequisites, you can start the Docker container with a single command. This gives you access to the same interface shown in the demonstrations - a chat interface on the left where you can talk to Claude, and a browser environment on the right where Claude can interact with web pages and applications.

![](https://academy.claude.com/assets/media/95ea027141baec80d881a0cae3713ede1ad920c6a2dd8bdc65e1421b3f8e675c.png)

The setup process is straightforward, and the full setup guide is available in the Anthropic quickstarts repository on GitHub. This reference implementation provides everything you need to start experimenting with Claude's computer use capabilities in a safe, contained environment.

[Previous lessonComputer Use](https://academy.claude.com/courses/claude-with-amazon-bedrock/computer-use)[Next lessonQualities of agents](https://academy.claude.com/courses/claude-with-amazon-bedrock/qualities-of-agents)

Lesson 64 of 65 · Claude with Amazon BedrockHow Computer Use works

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

* [Tool Use Refresher](#tool-use-refresher)
* [Computer Use: Same Flow, Different Tool](#computer-use-same-flow-different-tool)
* [The Technical Implementation](#the-technical-implementation)
* [Getting Started](#getting-started)
