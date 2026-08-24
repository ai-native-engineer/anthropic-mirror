<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/routing-workflows -->

Lesson 64 of 67 · Building with the Claude APIRouting workflows

3. /[Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api)

[Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api)

# Routing workflows

Lesson 645 min

Routing workflows solve a common problem in AI applications: different types of user requests need different handling approaches. Instead of using a one-size-fits-all prompt, you can categorize incoming requests and route them to specialized processing pipelines.

## The Problem with Generic Prompts

Consider a social media marketing tool that generates video scripts from user topics. A user might enter "programming" or "surfing" as their topic, but these should produce very different types of content:

![](https://academy.claude.com/assets/media/c861b4e4c23f03be11fcb1abcf4d0a28ed345c73c3f06c91864f68b4ae94dbd1.jpg)

Programming topics call for educational content with clear explanations and definitions. Surfing topics work better with entertainment-focused scripts that emphasize excitement and visual appeal. A single generic prompt can't handle both effectively.

## Setting Up Content Categories

The first step is defining the different types of content your application might need to generate. You might categorize requests into genres like:

* Entertainment - High-energy, culturally relevant content with trendy language
* Educational - Clear, engaging explanations with relatable examples
* Comedy - Sharp, unexpected content with clever observations and timing
* Personal vlog - Authentic, intimate content with conversational storytelling
* Reviews - Decisive, experience-based content highlighting strengths and weaknesses
* Storytelling - Immersive content using vivid details and emotional connection

![](https://academy.claude.com/assets/media/b0c1eaf72ed561f17973769422d9e1eed68e38492e9cafe0bfe6a9253c0bc9a8.jpg)

Each category gets its own specialized prompt template. For example, the educational prompt might ask Claude to "develop a clear, engaging script that transforms complex information into digestible insights using relatable examples and thought-provoking questions."

## How Routing Works in Practice

The routing process happens in two steps:

1. **Categorization** - Send the user's topic to Claude with a request to categorize it into one of your predefined genres
2. **Specialized Processing** - Use the category result to select the appropriate prompt template and generate content

![](https://academy.claude.com/assets/media/9e2cd80ddfae6fab473f7f31ffac7e9eba1e9fdfc1636fe521c73e7319b8c9dc.jpg)

For example, if a user enters "Python functions" as their topic, you'd first ask Claude to categorize it:

```
Categorize the topic of a video into one of the listed categories:
<topic>Python functions</topic>

<categories>
- Educational
- Entertainment
- Comedy
- Personal vlog
- Reviews
- Storytelling
</categories>
```

Claude responds with "Educational", so you then use the educational prompt template to generate the actual script content.

![](https://academy.claude.com/assets/media/d59a1066f0963fcd4a835cf9e8336aa30399554712455e1b8d9f006b99490f8f.jpg)

## Routing Workflow Architecture

A routing workflow follows this pattern:

![](https://academy.claude.com/assets/media/0b78f406652dc020251e48927c0156d40edc591b8cd47d13e56a1246e233f4fb.jpg)

* User input goes to a router component first
* The router categorizes the request using an initial Claude call
* Based on the category, the input gets forwarded to one specific processing pipeline
* Each pipeline can have its own workflow, prompts, or tools optimized for that category

The key insight is that user input only goes to one specialized pipeline, not all of them. This allows each pipeline to be highly optimized for its specific use case.

## When to Use Routing

Routing workflows work well when:

* Your application handles diverse types of requests that need different approaches
* You can clearly define categories that cover your use cases
* The categorization step can be handled reliably by Claude
* The performance benefit of specialized processing outweighs the overhead of the routing step

This pattern is especially valuable for customer service bots, content generation tools, and any application where the "right" response depends heavily on understanding the type of request being made.

[Previous lessonChaining workflows](https://academy.claude.com/courses/building-with-the-claude-api/chaining-workflows)[Next lessonAgents and tools](https://academy.claude.com/courses/building-with-the-claude-api/agents-and-tools)

Lesson 64 of 67 · Building with the Claude APIRouting workflows

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

* [The Problem with Generic Prompts](#the-problem-with-generic-prompts)
* [Setting Up Content Categories](#setting-up-content-categories)
* [How Routing Works in Practice](#how-routing-works-in-practice)
* [Routing Workflow Architecture](#routing-workflow-architecture)
* [When to Use Routing](#when-to-use-routing)
