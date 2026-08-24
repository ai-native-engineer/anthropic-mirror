<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock -->

[Courses](https://academy.claude.com/courses)

# Claude with Amazon Bedrock

Integrating and deploying Claude through Amazon Bedrock: API implementation, tool use, RAG pipelines, agents, and production-ready applications on AWS.

65 lessons8 hr8 quizzesCompletion badge

[Start course](https://academy.claude.com/courses/claude-with-amazon-bedrock/overview-of-claude-models)[Sign in to save progress](https://academy.claude.com/login?returnTo=https%3A%2F%2Facademy.claude.com%2Fcourses%2Fclaude-with-amazon-bedrock)

![](https://academy.claude.com/assets/v1/thumbnail.light-h9uvcfp3.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-bq1s458m.png)

65 lessons · 8 quizzesClaude with Amazon Bedrock

What you’ll learnBy the end of this course, you’ll be able to

* Utilize Anthropic models on Amazon Bedrock for multi-turn conversations and system prompt configuration
* Build and evaluate prompts using structured approaches
* Design and integrate custom tools using JSON Schema for function calling and batch processing
* Develop RAG pipelines with text chunking, embeddings, BM25 search, and contextual retrieval techniques
* Configure and optimize Claude's advanced features including extended thinking, vision capabilities, and prompt caching
* Leverage Claude Code for automated debugging and task execution
* Implement Model Context Protocol (MCP) for defining tools, resources, and prompts in client applications
* Optimize inference through streaming, temperature control, and structured data extraction
* Build evaluation frameworks for prompts using model-based and code-based grading approaches

Who it’s for

Devs who want to add AI features to their apps

Before you start

* Proficiency in Python programming
* Basic knowledge of handling JSON data
* AWS account with Bedrock access

This course covers using Claude models through AWS Bedrock API, from basic requests through advanced agent implementations. You'll learn to make API calls, implement tool use, build RAG pipelines, work with MCP servers, and leverage features like Claude Code and computer use for automation.

## Inside the course

### Course introduction

1 lesson

Start here for the fundamentals.

### Working with the API

9 lessons

Covers API authentication, basic requests, conversation management, system prompts, and structured output generation.

![](https://academy.claude.com/assets/media/65d9c77d19069e0a25025a1bac897649f7dcab8d514282d725436041b1032e1a.webp)![](https://academy.claude.com/assets/media/3b6f54695aca003b8556b47e30dc3f2eda967104dfb769b889af232e94485a12.webp)![](https://academy.claude.com/assets/media/69f49d7a6908d7d0bdb2ce3fb248859cf79e407c358e91f09ae04d7df00f7748.webp)

### Prompt engineering

6 lessons

Learn to write prompts that actually work. Focuses on prompting strategies, evaluation frameworks, and systematic testing approaches.

![](https://academy.claude.com/assets/media/d698fb2758b8ed953ec2cfc8e7934e389082145a2fb60a4bb10de21011d637a8.webp)![](https://academy.claude.com/assets/media/1157fd1c808773ec1f720ca71df8f148add31efa70af71075514b13d30a9d33d.webp)![](https://academy.claude.com/assets/media/3faf1b34d9377396ec512bb0eef3232556c30cf8c59bc77a196e9a06de9e4958.webp)

### Tool use

13 lessons

Extend Claude with custom tools and functions. Build apps with function calling, multi-turn tool interactions, batch tool calling, and leverage built-in utilities.

![](https://academy.claude.com/assets/media/26a857680b2257cd55080cf5b802b91f3fe31fea574c2305ce8d1f28e97b84cc.webp)![](https://academy.claude.com/assets/media/e210dc5f246e65c6403a4deb279d716cb063692a98b7908decc3e77639299db9.webp)![](https://academy.claude.com/assets/media/21f493533eb94b561db9153d92ec5b8cd12de2b043f2755c2637f2422ccf3975.webp)

### Retrieval Augmented Generation

10 lessons

Implementation guide for production RAG systems. Covers text chunking, embeddings, hybrid search with BM25, multi-index architectures, reranking, and contextual retrieval.

![](https://academy.claude.com/assets/media/a5455a0f1df401818be5b948b2f9786e2f33b83e19824f8a61d89ec1a8a01e6f.webp)![](https://academy.claude.com/assets/media/acc3f04cdfda2ce579d78c264ba0bb765e3c9141b4954e847382f45f87dea9dd.webp)![](https://academy.claude.com/assets/media/6fc4994e21018a93d1fa0fa9a31e50a1777ed8993a9c113e43e10db4912ec7d3.webp)

### Model Context Protocol

12 lessons

The protocol for building modular AI applications. Define custom tools and resources, implement MCP servers and clients, handle the full integration lifecycle.

![](https://academy.claude.com/assets/media/0685a333a949af8f486bb2fe0b1197e16226f0772059eaef4695cf4b76aaa724.webp)![](https://academy.claude.com/assets/media/56a99dc9e075adf0f948eac55e468a1dbfb9d7c9dcb2ec07ca28df80fa2d7fab.webp)![](https://academy.claude.com/assets/media/82cc1d661480e5a93a155e970acf22d664e1d4ed95cc366dced134e947eb74dd.webp)

### Agents

7 lessons

Two powerful Anthropic tools in action. Claude Code accelerates development workflows, Computer Use automates UI interactions. Includes MCP integration patterns.

![](https://academy.claude.com/assets/media/25c938bf7dcb31204d07112d94b882d5e5f0a69d935b23ada35ab80922e95ed8.webp)![](https://academy.claude.com/assets/media/b02c642dc6885de790925dc4fd7206f1b2ba032d9c25f81a9d4a4ce8cc5b2e53.webp)![](https://academy.claude.com/assets/media/56c699640bbe391d01a890e098a030b6997637c8788d5d8d3938f66e0d117941.webp)

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
