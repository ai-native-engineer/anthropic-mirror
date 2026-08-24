<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/code-execution-and-the-files-api -->

Lesson 46 of 67 · Building with the Claude APICode execution and the Files API

3. /[Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api)

[Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api)

# Code execution and the Files API

Lesson 4610 min

The Anthropic API offers two powerful features that work exceptionally well together: the Files API and Code Execution. While they might seem separate at first, combining them opens up some really interesting possibilities for delegating complex tasks to Claude.

## Files API

The Files API provides an alternative way to handle file uploads. Instead of encoding images or PDFs directly in your messages as base64 data, you can upload files ahead of time and reference them later.

![](https://academy.claude.com/assets/media/ee042cc9aaaaf3d0ce0177dd43d9c26aca27190fbac45d51f37c4318f7b22e07.jpg)

Here's how it works:

* Upload your file (image, PDF, text, etc.) to Claude using a separate API call
* Receive a file metadata object containing a unique file ID
* Reference that file ID in future messages instead of including raw file data

![](https://academy.claude.com/assets/media/96059a1704f4b5ec3f88bcd6519f2bf178558676fcabf3fdd4e5dc2d66912f6b.jpg)

This approach is particularly useful when you want to reference the same file multiple times or when working with larger files that would be cumbersome to include in every request.

## Code Execution Tool

Code execution is a server-based tool that doesn't require you to provide an implementation. You simply include a predefined tool schema in your request, and Claude can optionally execute Python code in an isolated Docker container.

![](https://academy.claude.com/assets/media/1d10a3e11cdf7df719894139c9797e7aaa5d19634fbdf4ff35f36937fd8a1cde.jpg)

Key characteristics of the code execution environment:

* Runs in an isolated Docker container
* No network access (can't make external API calls)
* Claude can execute code multiple times during a single conversation
* Results are captured and interpreted by Claude for the final response

## Combining Files API and Code Execution

The real power comes from using these features together. Since the Docker containers have no network access, the Files API becomes the primary way to get data in and out of the execution environment.

![](https://academy.claude.com/assets/media/f680a4ba00bc0efa3ab86156263d34ed95e0fb7d7181341677e9b386a246ee33.jpg)

Here's a typical workflow:

1. Upload your data file (like a CSV) using the Files API
2. Include a container upload block in your message with the file ID
3. Ask Claude to analyze the data
4. Claude writes and executes code to process your file
5. Claude can generate outputs (like plots) that you can download

## Practical Example

Let's look at a real example using streaming service data. The CSV file contains user information including subscription tiers, viewing habits, and whether they've churned (canceled their subscription).

![](https://academy.claude.com/assets/media/37896049b6036071a0c10181dfa7468260b1c071ebd49e15223861d9918581b0.jpg)

First, upload the file using a helper function:

python

```
file_metadata = upload('streaming.csv')
```

Then create a message that includes both the uploaded file and a request for analysis:

python

```
messages = []
add_user_message(
    messages,
    [
        {
            "type": "text",
            "text": """Run a detailed analysis to determine major drivers of churn.
            Your final output should include at least one detailed plot summarizing your findings."""
        },
        {"type": "container_upload", "file_id": file_metadata.id},
    ],
)

chat(
    messages,
    tools=[{"type": "code_execution_20250522", "name": "code_execution"}]
)
```

## Understanding the Response

When Claude uses code execution, the response contains multiple types of blocks:

* **Text blocks** - Claude's analysis and explanations
* **Server tool use blocks** - The actual code Claude decided to run
* **Code execution tool result blocks** - Output from running the code

![](https://academy.claude.com/assets/media/532b74fcf5245797a3f537305a22a033db55c59faf5995bca4834ad517066a4d.jpg)

Claude might execute code multiple times during a single response, iteratively building up its analysis. Each execution cycle includes the code and its results.

## Downloading Generated Files

One of the most powerful features is Claude's ability to generate files (like plots or reports) and make them available for download. When Claude creates a visualization, it gets stored in the container and you can download it using the Files API.

Look for blocks with `type: "code_execution_output"` in the response - these contain file IDs for generated content:

python

```
download_file("file_id_from_response")
```

![](https://academy.claude.com/assets/media/8c86d9737bcc9bcf07c7a91c64fe2311e8878e713e0c5fab8471de65cc71907b.jpg)

The result is a comprehensive analysis with professional visualizations that would have taken significant manual coding to produce.

## Beyond Data Analysis

While data analysis is a natural fit, the combination of Files API and code execution opens up many possibilities:

* Image processing and manipulation
* Document parsing and transformation
* Mathematical computations and modeling
* Report generation with custom formatting

The key is that you can delegate complex, computational tasks to Claude while maintaining control over the inputs and outputs through the Files API. This creates a powerful workflow where Claude becomes your coding assistant that can actually execute and iterate on solutions.

[Previous lessonPrompt caching in action](https://academy.claude.com/courses/building-with-the-claude-api/prompt-caching-in-action)[Next lessonQuiz on features of Claude](https://academy.claude.com/courses/building-with-the-claude-api/quiz-on-features-of-claude)

Lesson 46 of 67 · Building with the Claude APICode execution and the Files API

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

* [Files API](#files-api)
* [Code Execution Tool](#code-execution-tool)
* [Combining Files API and Code Execution](#combining-files-api-and-code-execution)
* [Practical Example](#practical-example)
* [Understanding the Response](#understanding-the-response)
* [Downloading Generated Files](#downloading-generated-files)
* [Beyond Data Analysis](#beyond-data-analysis)
