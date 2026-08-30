<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/system-prompts -->

Lesson 5 of 65 · Claude with Amazon BedrockSystem prompts

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# System prompts

Lesson 58 min

When building AI chatbots for specific use cases, you need a way to control how the AI responds. System prompts are the key to transforming a general-purpose AI into a specialized assistant that follows specific guidelines and stays on topic.

![](https://academy.claude.com/assets/media/a8883fbe515bc8ea7e369f29e866caa10ed49af599dd529a3143bed87c9cd346.png)

## The Problem with User-Level Instructions[](#the-problem-with-user-level-instructions)

You might think the solution is to include all your requirements in the user message itself. For example, telling the AI in each conversation to "mention AWS services" and "don't mention competitors." This approach has serious limitations:

* You'd need to anticipate every possible question and edge case
* The instruction list becomes unwieldy and repetitive
* Users see all the internal instructions, making conversations cluttered
* Requirements change based on the specific question being asked

![](https://academy.claude.com/assets/media/0d5cb99bb7a6fcab168500308b061b008367df300bbd299edff265dbebf3805e.png)

## System Prompts: A Better Approach[](#system-prompts-a-better-approach)

System prompts solve this problem by giving Claude a role to play. Instead of listing specific do's and don'ts, you tell Claude to act like a particular type of professional. The AI then responds as that person would naturally respond.

![](https://academy.claude.com/assets/media/e8f3cc5bc734943a959be45a79ed9f50cd24eeee7976474ed9b1dbc33fd47b4c.png)

System prompts provide several key benefits:

* Claude gets guidance on how to respond consistently
* The AI adopts the mindset and constraints of the specified role
* Responses stay focused and on-brand automatically
* You don't need to anticipate every possible scenario

## Implementing System Prompts[](#implementing-system-prompts)

To add a system prompt to your Claude conversation, you pass it as a parameter to the `converse` function:

python

```
system_prompt = """
You are an AWS cloud support specialist. Your job is to answer user queries related
to cloud hosting services on AWS.
"""

response = client.converse(
    modelId=model_id,
    messages=messages,
    system=[{"text": system_prompt}]
)
```

The system prompt gets passed as a list containing a dictionary with a "text" key. This tells Claude what role to adopt before it sees any user messages.

## Building a Flexible Chat Function[](#building-a-flexible-chat-function)

Here's a reusable chat function that handles system prompts elegantly:

python

```
def chat(messages, system=None):
    params = {"modelId": model_id, "messages": messages}

    if system:
        params["system"] = [{"text": system}]

    response = client.converse(**params)

    return response["output"]["message"]["content"][0]["text"]
```

This approach lets you optionally include a system prompt. When no system prompt is provided, Claude responds as its default self. When you include one, Claude adopts that specific role.

## System Prompts in Action[](#system-prompts-in-action)

The difference is immediately apparent when you test the same question with and without a system prompt. Ask "How do I host a Postgres database?" without a system prompt, and you'll get a comprehensive answer covering multiple cloud providers and self-hosting options.

![](https://academy.claude.com/assets/media/3068fd0afb53cb298b442ddf08066d861887d2ae5ec6cd1f965e801e9932c039.png)

With an AWS support specialist system prompt, the response focuses exclusively on AWS solutions like RDS, Aurora, and EC2-based deployments. No competitors mentioned, and the answer includes AWS-specific setup steps.

Even more impressive is how system prompts handle off-topic questions. Ask for a bread recipe with the AWS specialist prompt active, and Claude politely declines while staying in character:

![](https://academy.claude.com/assets/media/23098f708f02781a4dd30a7c21b4d0d96413f6a22840b791a63d919a0aa22832.png)

## Important Technical Details[](#important-technical-details)

When working with system prompts, keep these requirements in mind:

* System prompts cannot be empty strings - they must contain at least one character
* The system parameter expects a list of dictionaries with "text" keys
* System prompts are processed before any user messages in the conversation
* You can change the top-level `system` value between requests, but not partway through a single `messages` list

If you've worked with Anthropic's Claude API directly, you might know that some Claude models support mid-conversation system messages — adding a message with the `system` role to the `messages` array instead of changing the top-level field. That feature isn't available on Amazon Bedrock. In this course, you'll always set system instructions through the top-level `system` parameter on each `converse` call.

System prompts give you powerful control over AI behavior without complex rule systems. By assigning Claude a specific professional role, you get consistent, appropriate responses that naturally follow the constraints and expertise of that role.

[Previous lessonMulti-Turn conversations](https://academy.claude.com/courses/claude-with-amazon-bedrock/multi-turn-conversations)[Next lessonTemperature](https://academy.claude.com/courses/claude-with-amazon-bedrock/temperature)

Lesson 5 of 65 · Claude with Amazon BedrockSystem prompts

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

* [The Problem with User-Level Instructions](#the-problem-with-user-level-instructions)
* [System Prompts: A Better Approach](#system-prompts-a-better-approach)
* [Implementing System Prompts](#implementing-system-prompts)
* [Building a Flexible Chat Function](#building-a-flexible-chat-function)
* [System Prompts in Action](#system-prompts-in-action)
* [Important Technical Details](#important-technical-details)
