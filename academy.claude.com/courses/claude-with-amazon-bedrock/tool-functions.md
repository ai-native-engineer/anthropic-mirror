<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/tool-functions -->

Lesson 22 of 65 · Claude with Amazon BedrockTool functions

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Tool functions

Lesson 225 min

Building tools for Claude requires solving several challenges that aren't immediately obvious. When you want Claude to set reminders for future dates, you quickly discover that while Claude knows the current date, it doesn't always know the exact time, struggles with complex date arithmetic, and has no built-in way to actually set reminders.

![](https://academy.claude.com/assets/media/59f1421b35b91a9e12d77fe6fc39b9aa25f631d512952ff9d558642a0644650e.png)

The solution is to create custom tools that handle these specific tasks. For a reminder system, you'll need three separate tools: one to get the current date and time, another to add durations to dates, and a third to actually set the reminder.

## Why This Is Challenging[](#why-this-is-challenging)

Claude has some limitations when it comes to time-based tasks:

* Claude might know the current date, but not the exact time
* Claude doesn't always handle time-based addition well, especially when looking many days into the future
* Claude doesn't know how to set a reminder

![](https://academy.claude.com/assets/media/a7c479969f35c554cc2bbba8f8e3908cabc2f621e13b4068267e5c971b20692b.png)

## The Tools You Need[](#the-tools-you-need)

To solve these problems, you'll create three dedicated tools:

* **Get the current date time** - Claude needs to know the current date and time
* **Add duration to date time** - Claude isn't perfect with date time addition
* **Set a reminder** - Need a way to set a reminder

![](https://academy.claude.com/assets/media/ab568fe7efa0dc2e7418393d5d926dbca2ccc2840fa0ea0e396b4c786d2699c6.png)

## How Tool Functions Work[](#how-tool-functions-work)

The tool system follows a specific flow between your server and Claude. You write functions that Claude can call when it needs additional information, and Claude receives the results to help formulate its response.

![](https://academy.claude.com/assets/media/5b0bb0502e2b58bf4e767efced7d0f7f7c385c57501d457c61769d5ede05a2a1.png)

The process involves several steps: writing the tool function, creating a JSON schema specification, calling Claude with that schema, running the tool when Claude requests it, and providing the results back to Claude.

![](https://academy.claude.com/assets/media/493213de9630b90abce40533716123bee8656cde00774668558a6aedcf045085.png)

## Writing Tool Functions[](#writing-tool-functions)

Tool functions are plain Python functions that get executed when Claude decides it needs additional information to help the user. Here's how to write them effectively:

### Best Practices[](#best-practices)

* Use well-named, descriptive arguments (this becomes important later)
* Validate the inputs, raising an error if they fail validation
* Return meaningful errors - Claude will try to call your function a second time if it gets an error

![](https://academy.claude.com/assets/media/ab8e2ed3a5d133c180b9fb859d6d53a4c122fea7cef28570e948c20faa8dcd33.png)

## Creating Your First Tool[](#creating-your-first-tool)

Let's start with the simplest tool - getting the current date and time. This function takes a date format parameter and returns the current timestamp:

python

```
from datetime import datetime, timedelta

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    return datetime.now().strftime(date_format)
```

This function is straightforward but follows the key principles: it has a descriptive name, takes a well-named parameter with a sensible default, and returns exactly what it promises.

## JSON Schema Specification[](#json-schema-specification)

Once you have your function, you need to write a JSON Schema that describes it to Claude. This schema tells Claude what arguments the function requires and helps it understand when and how to use the tool.

![](https://academy.claude.com/assets/media/6ea349aba9b64c132b3081158284d2e6eecfc9fcba6b1b8a88aaec781d262097.png)

The JSON Schema serves two purposes: it helps Claude understand what arguments your function requires, and it's not just an LLM concept - JSON Schema is commonly used for data validation across many programming contexts. There are plenty of online tools to help you generate schemas.

### Schema Best Practices[](#schema-best-practices)

* Explain what the tool does, when to use it, and what it returns
* Aim for 3 to 4 sentences in your descriptions
* Provide detailed descriptions for parameters

With your tool function written and schema defined, you're ready to integrate it with Claude and start building more sophisticated AI interactions that can handle real-world tasks like setting reminders.

[Previous lessonIntroducing tool use](https://academy.claude.com/courses/claude-with-amazon-bedrock/introducing-tool-use)[Next lessonJSON Schema for tools](https://academy.claude.com/courses/claude-with-amazon-bedrock/json-schema-for-tools)

Lesson 22 of 65 · Claude with Amazon BedrockTool functions

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

* [Why This Is Challenging](#why-this-is-challenging)
* [The Tools You Need](#the-tools-you-need)
* [How Tool Functions Work](#how-tool-functions-work)
* [Writing Tool Functions](#writing-tool-functions)
* [Creating Your First Tool](#creating-your-first-tool)
* [JSON Schema Specification](#json-schema-specification)
