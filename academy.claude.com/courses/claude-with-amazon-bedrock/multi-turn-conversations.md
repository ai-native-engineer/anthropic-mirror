<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/multi-turn-conversations -->

Lesson 4 of 65 · Claude with Amazon BedrockMulti-Turn conversations

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Multi-Turn conversations

Lesson 47 min

The code we've written so far simulates a very simple exchange with Claude. But what happens when you want to continue a conversation? When you ask a follow-up question like "And 3 more?" after asking "What's 1+1?", you might expect Claude to understand you're asking about adding 3 to the previous result of 2.

![](https://academy.claude.com/assets/media/f29c60433e17d03d10e044a9c2a3fb707fc872e106269c250c8ff185309321e0.png)

However, there's something critical you need to understand about the Bedrock API and Claude itself.

## No Message Storage

Bedrock and Claude do not store any messages. None of the messages you send get stored, and none of the responses you receive are stored either. Each API call is completely independent.

![](https://academy.claude.com/assets/media/e16ef969c212a7411214c239a1a87ff224f3f84aa71924c586f12a2ccaf56142.png)

To have a conversation with multiple messages that maintain context, you need to:

* Manually maintain a list of all messages in your code
* Provide that entire list of messages with each follow-up request

## Why Context Matters

Let's see what happens without proper context. If you send just "And 3 more?" as a standalone message, Claude has no idea what you're referring to. It will do its best to respond, but the answer won't make sense because it lacks the context of your previous conversation.

![](https://academy.claude.com/assets/media/e8cb9ad98933f418225e8f7219abdc2685cde3583eb4bb26bde655351f7cfdbb.png)

When you send only the follow-up question, Claude sees just that isolated message and tries to respond without knowing about the previous "What's 1+1?" exchange.

![](https://academy.claude.com/assets/media/6e2e0f684037ec9034087e687eab7bb834c6932109a56c5e38807b8d7dd74336.png)

## Building Conversation Context

To maintain context, you need to include the full conversation history in each request. Here's how it works:

![](https://academy.claude.com/assets/media/513d4d190ef8558b64469605d419f7722dc06a898c2151ae6818fb7fa85385d0.png)

Your message list should contain all previous exchanges - both user messages and assistant responses. When you send this complete context, Claude can understand that "And 3 more?" refers to adding 3 to the previous result of 2.

## Helper Functions for Message Management

To make conversation management easier, you can create helper functions:

python

```
def add_user_message(messages, text):
    user_message = {
        "role": "user",
        "content": [
            {"text": text}
        ]
    }
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {
        "role": "assistant",
        "content": [
            {"text": text}
        ]
    }
    messages.append(assistant_message)

def chat(messages):
    response = client.converse(
        modelId=model_id,
        messages=messages
    )
    return response["output"]["message"]["content"][0]["text"]
```

## Implementing Multi-Turn Conversations

Here's how to build a conversation step by step:

python

```
# Make a starting list of messages
messages = []

# Add in the initial user question of "What's 1+1?"
add_user_message(messages, "What's 1+1?")

# Pass the list of messages into chat to get an answer
answer = chat(messages)

# Take the answer and add it as an assistant message into our list
add_assistant_message(messages, answer)

# Add in the user's followup question
add_user_message(messages, "And 3 more added to that?")

# Call chat again with the list of messages to get a final answer
answer = chat(messages)
print(answer)
```

This approach ensures Claude has the full context and can respond appropriately: "Starting with the result of 1+1 = 2, if we add 3 more to that, we get: 2 + 3 = 5"

## Message Role Alternation

When building your message list, always ensure that message roles alternate properly:

![](https://academy.claude.com/assets/media/a6c3f43aa044d65f4faa1456f338e1a7f7832b20d328b42f77683071c20d7575.png)

Your conversation should follow the pattern: user → assistant → user → assistant. Never have two user messages in a row or two assistant messages in a row. This alternating pattern is required by the API and reflects natural conversation flow.

While this manual message management might seem tedious at first, you'll quickly get used to it. This pattern is fundamental to building any application that needs to maintain conversational context with Claude.

[Previous lessonMaking a request](https://academy.claude.com/courses/claude-with-amazon-bedrock/making-a-request)[Next lessonSystem prompts](https://academy.claude.com/courses/claude-with-amazon-bedrock/system-prompts)

Lesson 4 of 65 · Claude with Amazon BedrockMulti-Turn conversations

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

* [No Message Storage](#no-message-storage)
* [Why Context Matters](#why-context-matters)
* [Building Conversation Context](#building-conversation-context)
* [Helper Functions for Message Management](#helper-functions-for-message-management)
* [Implementing Multi-Turn Conversations](#implementing-multi-turn-conversations)
* [Message Role Alternation](#message-role-alternation)
