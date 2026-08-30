<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/mcp-clients -->

Lesson 49 of 65 · Claude with Amazon BedrockMCP clients

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# MCP clients

Lesson 492 min

The MCP client serves as the communication bridge between your server and MCP servers. Think of it as your access point to all the tools that an MCP server provides. When you need to use external functionality, the client handles all the message passing and protocol details for you.

## Transport Agnostic Communication[](#transport-agnostic-communication)

One of MCP's key strengths is being transport agnostic - a fancy way of saying the client and server can talk to each other using different communication methods. The most common setup runs both the MCP client and server on the same machine, where they communicate through standard input/output.

![](https://academy.claude.com/assets/media/b393bf3821c37b06d31300b588c291caa460db51353ebbfbc6a56b9c2a2c0160.png)

But you're not limited to that approach. MCP clients and servers can also connect over:

* HTTP
* WebSockets
* Various other network protocols

![](https://academy.claude.com/assets/media/3a63d189484fd713cdaa1932e5b9638da2b20059ce414c288f77d915371b5f5c.png)

## Message Types[](#message-types)

Once connected, the client and server exchange specific message types defined in the MCP specification. The main ones you'll work with are:

![](https://academy.claude.com/assets/media/4dbfe70297791ff32dced94d745d416ec7ec8c5889d3cbd45ef3328bbdb7f755.png)

**ListToolsRequest/ListToolsResult:** The client asks the server "what tools do you provide?" and gets back a complete list of available functionality.

![](https://academy.claude.com/assets/media/b94c5c441b196cce093af43405bb70be67728aeee37f7a526f6a022ce53e0ffe.png)

**CallToolRequest/CallToolResult:** The client tells the server "run this specific tool with these arguments" and receives the execution results.

## Complete Flow Example[](#complete-flow-example)

Here's how all the pieces work together in a real scenario. Let's say a user asks "What repositories do I have?" - here's the complete communication flow:

![](https://academy.claude.com/assets/media/1c07f5155e3236d4041a308cff4f852f90b03cc346db6a394943ea81d4cfb73b.png)

The process starts when a user submits their question to your server. But before your server can ask Claude for help, it needs to know what tools are available.

![](https://academy.claude.com/assets/media/75b325da2e24c8a501a9a2cee9d77dae6fc89d4c8eed8116b87a57d8446aed53.png)

Your server asks the MCP client for a list of tools. The client sends a `ListToolsRequest` to the MCP server and gets back a `ListToolsResult` with all available tools.

![](https://academy.claude.com/assets/media/1518fad3b60e01d67fc4009b0f6c53b3f889f4ee161b2a30fe9a85eecd6a1ff1.png)

Now your server has everything needed to make the initial request to Claude: the user's question plus the list of available tools.

![](https://academy.claude.com/assets/media/1415a4318b5565540c9003623ee7c39dd14d479e89d6493b996045ad670ee6b8.png)

Claude analyzes the tools and decides it needs to call one to answer the question. It responds with a tool use request.

![](https://academy.claude.com/assets/media/59781bd96669e5c72052e5490ad036f4d56da79c1f740817ca0e41f1f1ea9791.png)

Your server recognizes that Claude wants to run a tool, but your server doesn't execute tools directly anymore - that's the MCP server's job. So it asks the MCP client to run the tool with Claude's specified arguments.

![](https://academy.claude.com/assets/media/dd69a4ce1ab6d335d71ee7a44b39bc7444de41fc5d3ba7b064cfdd489bacbd15.png)

The MCP client sends a `CallToolRequest` to the MCP server, which then makes the actual request to GitHub to fetch the user's repositories.

![](https://academy.claude.com/assets/media/e567d86142d465bc3fd10f03ed3ce64ac0e3d1a66f7681dd62153a4c28774340.png)

GitHub responds with the repository data, which the MCP server wraps in a `CallToolResult` and sends back to the MCP client.

![](https://academy.claude.com/assets/media/97d8b2efc898885b26329b2ac8f8d539f2ac1e36c9220b7c30def11831af6b87.png)

The MCP client passes the tool result back to your server, which then sends it to Claude as part of a follow-up message.

![](https://academy.claude.com/assets/media/5cf8d2c9004dbbf4da4442e186ff1042e62d508e3e5810a7314832125c701093.png)

Finally, Claude has all the information it needs and formulates a response like "Your repositories are..." which gets sent back through your server to the user.

![](https://academy.claude.com/assets/media/92b5f03a879df7c7bc870a7b08fe1f93aa1cc9398f4de4128089c213c19df24f.png)

Yes, this flow involves many steps, but each component has a clear responsibility. The MCP client abstracts away the complexity of server communication, letting you focus on building your application logic while still having access to powerful external tools and services.

[Previous lessonIntroducing MCP](https://academy.claude.com/courses/claude-with-amazon-bedrock/introducing-mcp)[Next lessonProject setup](https://academy.claude.com/courses/claude-with-amazon-bedrock/project-setup)

Lesson 49 of 65 · Claude with Amazon BedrockMCP clients

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

* [Transport Agnostic Communication](#transport-agnostic-communication)
* [Message Types](#message-types)
* [Complete Flow Example](#complete-flow-example)
