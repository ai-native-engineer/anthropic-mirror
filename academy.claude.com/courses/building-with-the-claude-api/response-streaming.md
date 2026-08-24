<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/response-streaming -->

Lesson 7 of 67 · Building with the Claude APIResponse streaming

3. /[Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api)

[Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api)

# Response streaming

Lesson 79 min

When building chat applications with Claude, there's a significant user experience challenge: responses can take 10-30 seconds to generate, leaving users staring at a loading spinner. The solution is response streaming, which lets users see text appear chunk by chunk as Claude generates it, creating a much more responsive feel.

![](https://academy.claude.com/assets/media/b677fa9ad3691de38586f695074f86d29f7920d7afdf51b0114cc57707bcbbdb.png)

## The Problem with Standard Responses

In a typical chat setup, your server sends a user message to Claude and waits for the complete response before sending anything back to the client. This creates an awkward delay where users have no feedback that anything is happening.

![](https://academy.claude.com/assets/media/75db72aa31a223044a968e76b43a324eb25c751002be314d3ab94ae137c9ac6c.png)

## How Streaming Works

With streaming enabled, Claude immediately sends back an initial response indicating it has received your request and is starting to generate text. Then you receive a series of events, each containing a small piece of the overall response.

![](https://academy.claude.com/assets/media/383a3ef0267d731d42ae032c4a7946df84a9a0de6d78e5abbdf02db3b606a23f.png)

Your server can forward these text chunks to your client application as they arrive, allowing users to see the response building up word by word. All of these events are part of a single request to Claude.

![](https://academy.claude.com/assets/media/383a3ef0267d731d42ae032c4a7946df84a9a0de6d78e5abbdf02db3b606a23f.png)

## Understanding Stream Events

When you enable streaming, Claude sends back several types of events:

* **MessageStart** - A new message is being sent
* **ContentBlockStart** - Start of a new block containing text, tool use, or other content
* **ContentBlockDelta** - Chunks of the actual generated text
* **ContentBlockStop** - The current content block has been completed
* **MessageDelta** - The current message is complete
* **MessageStop** - End of information about the current message

![](https://academy.claude.com/assets/media/b05e5fa5712d1f4223b7da33e9f3400fe48ce1503eb6001f5fa22963fd4f80e8.png)

The `ContentBlockDelta` events contain the actual generated text that you'll want to display to users.

## Basic Streaming Implementation

To enable streaming, add `stream=True` to your messages.create call:

python

```
messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")

stream = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    stream=True
)

for event in stream:
    print(event)
```

![](https://academy.claude.com/assets/media/f3eb92bf758b0bf8c34fdec38ed54393f1c79ad7f8152fdc3dcfdd1e2bde058d.png)

## Simplified Text Streaming

Rather than manually parsing events, you can use the SDK's simplified streaming interface that extracts just the text content:

python

```
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        print(text, end="")
```

This approach automatically filters out everything except the actual text content, which is usually what you need for displaying responses to users.

## Getting the Complete Message

While streaming individual chunks is great for user experience, you often need the complete message for storage or further processing. After streaming completes, you can get the assembled final message:

python

```
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        # Send each chunk to your client
        pass

    # Get the complete message for database storage
    final_message = stream.get_final_message()
```

This gives you the best of both worlds: real-time streaming for users and a complete message object for your application logic.

[Previous lessonTemperature](https://academy.claude.com/courses/building-with-the-claude-api/temperature)[Next lessonStructured data](https://academy.claude.com/courses/building-with-the-claude-api/structured-data)

Lesson 7 of 67 · Building with the Claude APIResponse streaming

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

* [The Problem with Standard Responses](#the-problem-with-standard-responses)
* [How Streaming Works](#how-streaming-works)
* [Understanding Stream Events](#understanding-stream-events)
* [Basic Streaming Implementation](#basic-streaming-implementation)
* [Simplified Text Streaming](#simplified-text-streaming)
* [Getting the Complete Message](#getting-the-complete-message)
