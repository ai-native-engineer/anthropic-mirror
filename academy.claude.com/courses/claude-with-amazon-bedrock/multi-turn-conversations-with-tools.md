<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/multi-turn-conversations-with-tools -->

Lesson 27 of 65 · Claude with Amazon BedrockMulti-Turn conversations with tools

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Multi-Turn conversations with tools

Lesson 279 min

Building multi-turn conversations with tool use requires handling different response types from Claude. When Claude responds, it might need to use a tool, or it might provide a direct answer. Your code needs to handle both scenarios gracefully.

## The Problem with Simple Tool Integration

If you just add tool results to every conversation, you'll run into issues. When Claude answers a simple question like "What is 1+1?", it doesn't need any tools. But if your code always tries to process tool results, you'll end up adding empty messages to your conversation history.

The solution is to check the `stop_reason` that comes back with every Claude response. This tells you why Claude stopped generating - whether it finished naturally or because it wants to use a tool.

## Stop Reasons

![](https://academy.claude.com/assets/media/a461bfa198f998666258b152abc1a277f7804c7d9850a10e70ac5df553fa13f2.png)

Claude can stop for several reasons:

* `"tool_use"` - The model wants to call a tool
* `"end_turn"` - Model finished generating its response
* `"max_tokens"` - Hit the output limit
* `"stop_sequence"` - Encountered a stop sequence you provided

## Improving the Chat Function

First, update your chat function to return more information. Instead of just returning text and parts separately, return a dictionary with everything you need:

python

```
def chat(messages, tools=None, system=None, **kwargs):
    # ... existing code ...

    return {
        "parts": parts,
        "stop_reason": response["stopReason"],
        "text": "\n".join([p["text"] for p in parts if "text" in p])
    }
```

This approach extracts all text content from the response parts, which is more robust than assuming the first part is always text.

## Building a Conversation Loop

Create a function that handles the full conversation flow:

python

```
def run_conversation(messages):
    while True:
        result = chat(messages, tools=[get_current_datetime_schema])

        add_assistant_message(messages, result["parts"])
        print(result["text"])

        if result["stop_reason"] != "tool_use":
            break

        tool_result_parts = run_tools(result["parts"])
        add_user_message(messages, tool_result_parts)

    return messages
```

This loop continues until Claude stops for a reason other than tool use. Each iteration:

1. Sends the current messages to Claude
2. Adds Claude's response to the message history
3. Checks if Claude wants to use a tool
4. If so, runs the tools and adds results back to the conversation
5. If not, exits the loop

## Testing the Implementation

This approach handles both tool-requiring and simple questions:

python

```
# Tool-requiring question
messages = []
add_user_message(messages, "What time is it?")
run_conversation(messages)

# Simple question
messages = []
add_user_message(messages, "What is 1+1?")
run_conversation(messages)
```

For time questions, Claude will use the datetime tool. For math questions, it responds directly without any tool calls. The conversation loop adapts automatically based on Claude's stop reason.

This pattern scales well when you add more tools - the same loop handles any combination of tool use and direct responses, making your conversational AI more robust and natural.

[Previous lessonSending tool results](https://academy.claude.com/courses/claude-with-amazon-bedrock/sending-tool-results)[Next lessonAdding multiple tools](https://academy.claude.com/courses/claude-with-amazon-bedrock/adding-multiple-tools)

Lesson 27 of 65 · Claude with Amazon BedrockMulti-Turn conversations with tools

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

* [The Problem with Simple Tool Integration](#the-problem-with-simple-tool-integration)
* [Stop Reasons](#stop-reasons)
* [Improving the Chat Function](#improving-the-chat-function)
* [Building a Conversation Loop](#building-a-conversation-loop)
* [Testing the Implementation](#testing-the-implementation)
