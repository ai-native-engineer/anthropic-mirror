<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/accessing-the-api -->

Lesson 1 of 66 · Claude with Google Cloud's Vertex AIAccessing the API

3. /[Claude with Google Cloud's Vertex AI](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai)

[Claude with Google Cloud's Vertex AI](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai)

# Accessing the API

Lesson 13 min

When building applications with Claude, understanding the complete request lifecycle helps you architect better systems and debug issues more effectively. Let's walk through what happens when a user sends a message to your AI-powered chat application.

![](https://academy.claude.com/assets/media/2a8244ea430c62fdba1dc04c5a8be19c3521ef69da5867972b57cffa5330668a.png)

## The Complete Request Flow

The journey from user input to AI response involves five distinct steps: Request to Server, Request to Vertex, Model Processing, Response to Server, and Response to Client. Each step plays a crucial role in delivering that "magical" response users expect.

![](https://academy.claude.com/assets/media/43789ae1571d4b4e2e9dc427f6e91932024bc7ab14ace57c53e085e1255c21bc.png)

## Why You Need a Server

Never make API requests directly from client-side code. Here's why:

* API requests require secret credentials that must stay secure
* Exposing credentials in client code makes them visible to anyone
* Your server acts as a secure intermediary between your app and Vertex

Always route requests through your own server that you control and secure.

## Making the API Request

Your server communicates with Vertex using either Anthropic's SDKs or Google's official Vertex SDKs. Anthropic provides official SDKs for Python, TypeScript, Go, and Ruby.

![](https://academy.claude.com/assets/media/5093c29c69228f0566456850e9e08e18348e997f3985608544d5838a6ee60693.png)

Every request must include these key fields:

* **API Key** - Identifies your request to Anthropic
* **Model** - Name of the specific model to use
* **Messages** - List containing the user's input text
* **Max Tokens** - Limits how many tokens the model can generate

The user's input gets placed inside a "user" message, which then goes into a list of messages sent to the API.

## Inside Claude: Text Generation Process

Once Vertex receives your request, Claude processes it through four stages: Tokenization, Embedding, Contextualization, and Generation.

![](https://academy.claude.com/assets/media/69ce6a422e611bb0cad6d36aead21b04cc7f0f0c50641c2fecf3e11c441c6a57.png)

### Tokenization

Claude first breaks down the input text into smaller chunks called tokens. These can be whole words, parts of words, spaces, or symbols. For simplicity, think of each word as one token.

### Embedding

Each token gets converted into an embedding - a long list of numbers that represents all possible meanings of that word. Think of embeddings as number-based definitions.

![](https://academy.claude.com/assets/media/29e3767c2c97dccb20530cfa0094321b1b7db82c564fe49176669852bcc58a8d.png)

### Contextualization

Since words can have multiple meanings, Claude uses context to determine the right interpretation. The word "quantum" could refer to physics, computing, or just mean "very small" - context from surrounding words clarifies the intended meaning.

![](https://academy.claude.com/assets/media/071c8391eaa772ac2e40d85f6f4c1f576ef00549da6a56ab93cf5fe87d571d03.png)

During contextualization, each embedding gets adjusted based on its neighbors, highlighting the meaning that makes most sense given the context.

![](https://academy.claude.com/assets/media/4039dc65298ec6f64f6a640528c0c913d214c71cf2c9d058835f49756f788fbe.png)

### Generation

The contextualized embeddings pass through an output layer that produces probabilities for each possible next word. Claude doesn't always pick the highest probability word - it uses a mix of probability and randomness to create more natural, varied responses.

![](https://academy.claude.com/assets/media/0fbdaf6f0b6335656798e98ae0483007af16163aa2c31b42f7bdbe50bfe568ce.png)

After selecting a word, Claude adds it to the sequence and repeats the entire process for the next word.

## When Generation Stops

After generating each token, Claude checks several conditions to decide whether to continue:

![](https://academy.claude.com/assets/media/50b0a7c628d398ab94c2517b42f5f570ab8f0ab2591dc53adfeefca85b2ca1b9.png)

* **Max tokens reached** - Has it hit the limit you specified?
* **Natural ending** - Did it generate an end-of-sequence token?
* **Stop sequence** - Did it encounter a predefined stop phrase?

The end-of-sequence token is a special signal (not visible text) that Claude uses to indicate it has reached a natural conclusion.

## The Response

Once generation completes, Vertex sends a response back to your server containing:

![](https://academy.claude.com/assets/media/69c1e66a21bcdc01892e5180df4b99cc5696b97a64ca7efc9e663d62d2d0b2f1.png)

* **Message** - The generated text
* **Usage** - Count of input and output tokens
* **Stop Reason** - Why the model stopped generating

Your server then forwards the generated text to your client application, where it appears in the chat interface.

![](https://academy.claude.com/assets/media/95913acc6c7e9c4e29a0dfb69d9ae9c40a12668250054e8a9c854cd126e8d09d.png)

## The Complete Picture

This entire process - from user input through tokenization, embedding, contextualization, generation, and back to the user - happens in seconds. Understanding this flow helps you build more robust applications and troubleshoot issues when they arise.

![](https://academy.claude.com/assets/media/bce56c24f2cbadc616690f966a1b374838ccd07307ca311feea4e915319e20e5.png)

The key takeaway: always use a server as an intermediary, understand that text generation is an iterative process, and pay attention to the response metadata to monitor usage and understand model behavior.

[Next lessonVertex AI Setup](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/vertex-ai-setup)

Lesson 1 of 66 · Claude with Google Cloud's Vertex AIAccessing the API

Accessing Claude with the API

* [Accessing the API](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/accessing-the-api)
* [Vertex AI Setup](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/vertex-ai-setup)
* [Making a request](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/making-a-request)
* [Multi-turn conversations](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/multi-turn-conversations)
* [System prompts](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/system-prompts)
* [Temperature](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/temperature)
* [Response streaming](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/response-streaming)
* [Controlling model output](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/controlling-model-output)
* [Structured data](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/structured-data)
* [Quiz on accessing Claude with the APIQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-accessing-claude-with-the-api)

Prompt evaluation

* [Prompt evaluation](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-evaluation)
* [A typical eval workflow](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/a-typical-eval-workflow)
* [Generating test datasets](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/generating-test-datasets)
* [Running the eval](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/running-the-eval)
* [Model based grading](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/model-based-grading)
* [Code based grading](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/code-based-grading)
* [Quiz on prompt evaluationQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-prompt-evaluation)

Prompt engineering techniques

* [Prompt engineering](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-engineering)
* [Being clear and direct](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/being-clear-and-direct)
* [Being specific](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/being-specific)
* [Structure with XML tags](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/structure-with-xml-tags)
* [Providing examples](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/providing-examples)
* [Quiz on prompt engineering techniquesQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-prompt-engineering-techniques)

Tool use with Claude

* [Introducing tool use](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/introducing-tool-use)
* [Project overview](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/project-overview)
* [Tool functions](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/tool-functions)
* [Tool schemas](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/tool-schemas)
* [Handling message blocks](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/handling-message-blocks)
* [Sending tool results](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/sending-tool-results)
* [Multi-turn conversations with tools](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/multi-turn-conversations-with-tools)
* [Implementing multiple turns](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/implementing-multiple-turns)
* [Using multiple tools](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/using-multiple-tools)
* [The batch tool](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/the-batch-tool)
* [Tools for structured data](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/tools-for-structured-data)
* [The text edit tool](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/the-text-edit-tool)
* [The web search tool](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/the-web-search-tool)
* [Quiz on tool use with ClaudeQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-tool-use-with-claude)

Retrieval Augmented Generation

* [Introducing Retrieval Augmented Generation](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/introducing-retrieval-augmented-generation)
* [Text chunking strategies](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/text-chunking-strategies)
* [Text embeddings](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/text-embeddings)
* [The full RAG flow](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/the-full-rag-flow)
* [Implementing the RAG flow](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/implementing-the-rag-flow)
* [BM25 lexical search](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/bm25-lexical-search)
* [A Multi-index RAG pipeline](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/a-multi-index-rag-pipeline)
* [Reranking results](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/reranking-results)
* [Contextual retrieval](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/contextual-retrieval)
* [Quiz on Retrieval Augmented GenerationQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-retrieval-augmented-generation)

Features of Claude

* [Extended thinking](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/extended-thinking)
* [Image support](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/image-support)
* [Citations](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/citations)
* [Prompt caching](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-caching)
* [Rules of prompt caching](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/rules-of-prompt-caching)
* [Prompt caching in action](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-caching-in-action)
* [Quiz on features of ClaudeQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-features-of-claude)

Model Context Protocol

* [Introducing MCP](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/introducing-mcp)
* [MCP clients](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/mcp-clients)
* [Project setup](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/project-setup)
* [Defining tools with MCP](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/defining-tools-with-mcp)
* [The server inspector](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/the-server-inspector)
* [Implementing a client](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/implementing-a-client)
* [Defining resources](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/defining-resources)
* [Accessing resources](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/accessing-resources)
* [Defining prompts](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/defining-prompts)
* [Prompts in the client](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompts-in-the-client)
* [MCP review](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/mcp-review)
* [Quiz on Model Context ProtocolQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-model-context-protocol)

Agents and workflows

* [Agents and workflows](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/agents-and-workflows)
* [Parallelization workflows](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/parallelization-workflows)
* [Chaining workflows](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/chaining-workflows)
* [Routing workflows](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/routing-workflows)
* [Agents and tools](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/agents-and-tools)
* [Environment inspection](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/environment-inspection)
* [Workflows vs agents](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/workflows-vs-agents)
* [Quiz on agents and workflowsQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/quiz-on-agents-and-workflows)

Final assessment

* [Final assessment quizQuiz](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/final-assessment-quiz)

* [Completion badge](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/badge)

* [The Complete Request Flow](#the-complete-request-flow)
* [Why You Need a Server](#why-you-need-a-server)
* [Making the API Request](#making-the-api-request)
* [Inside Claude: Text Generation Process](#inside-claude-text-generation-process)
* [When Generation Stops](#when-generation-stops)
* [The Response](#the-response)
* [The Complete Picture](#the-complete-picture)
