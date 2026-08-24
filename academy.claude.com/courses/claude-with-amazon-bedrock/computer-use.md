<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/computer-use -->

Lesson 63 of 65 · Claude with Amazon BedrockComputer Use

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Computer Use

Lesson 633 min

Computer use is a powerful feature that lets Claude interact directly with desktop environments, essentially giving it the ability to control a computer like a human would. This opens up entirely new possibilities for automation, testing, and complex workflows that go beyond simple text generation.

![](https://academy.claude.com/assets/media/4b5ec9792d6955bb4389f95219aaffbced39e4ee1bff425fc72d7cd1adcc9c13.png)

## What Computer Use Can Do

Instead of just describing what to do or generating code, Claude can actually perform tasks by:

* Taking screenshots to see what's on screen
* Clicking buttons and links
* Typing text into forms and applications
* Navigating between different applications and browser tabs
* Following multi-step processes that require visual feedback

This makes it particularly valuable for tasks like quality assurance testing, where you need to interact with a user interface and verify that everything works as expected.

## Real-World Example: Automated QA Testing

Here's a practical scenario that shows the power of computer use. Imagine you've built a React component with an autocomplete feature - users can type `@` to mention files or resources. The component seems to work fine at first glance, but you want to thoroughly test it for edge cases.

![](https://academy.claude.com/assets/media/c476223dcd1df89d3467a3207760914269daf2f98aad5e61e257dbeec7ce8db4.png)

Rather than manually testing every scenario yourself, you can set up Claude with computer use to handle the QA process. You provide Claude with specific test cases to run:

1. Verify that typing "Did you read @" displays autocomplete options
2. Test that pressing Enter properly adds a mention to the text area
3. Check that pressing backspace after adding mentions shows the autocomplete list in the correct position

![](https://academy.claude.com/assets/media/550676db0431879659b96f5ef02ba8936f8bba9af8ba01fb616c7d66ffe71d3e.png)

Claude will systematically work through each test case, taking screenshots, interacting with the interface, and documenting what happens. In this example, Claude discovered that while the first two tests passed, the third one failed - the autocomplete dropdown was appearing in the wrong location when users pressed backspace.

![](https://academy.claude.com/assets/media/7644029498ffc8e35056380d5ae29ddf68c110a9e3f05bafbc73991ee2629afe.png)

## How the Testing Process Works

When you give Claude a testing task, it follows a structured approach:

* Opens a browser and navigates to your application
* Executes each test case step by step
* Takes screenshots to verify visual behavior
* Refreshes the page between tests to ensure clean state
* Documents results with specific details about what passed or failed
* Provides a summary report with actionable findings

The key advantage is that Claude can catch issues you might miss during manual testing, and it can run the same tests consistently every time you make changes to your code.

## Setting Up Computer Use

Computer use runs in an isolated environment for security. The typical setup involves:

* A Docker container running a desktop environment
* A browser instance that Claude can control
* A chat interface where you give Claude instructions
* Complete isolation from your main system

This isolation is crucial because it means Claude can interact with applications and websites without any risk to your personal data or system security.

## Best Practices for Computer Use

When working with computer use, keep these guidelines in mind:

* Be specific about what you want Claude to test or accomplish
* Provide clear success criteria for each task
* Break complex workflows into smaller, manageable steps
* Always run computer use in isolated environments
* Review Claude's findings and verify important results manually

Computer use represents a significant step forward in AI capabilities, moving from generating text about tasks to actually performing them. Whether you're doing QA testing, automating repetitive workflows, or exploring complex applications, it can save substantial time while providing consistent, documented results.

[Previous lessonAutomated debugging](https://academy.claude.com/courses/claude-with-amazon-bedrock/automated-debugging)[Next lessonHow Computer Use works](https://academy.claude.com/courses/claude-with-amazon-bedrock/how-computer-use-works)

Lesson 63 of 65 · Claude with Amazon BedrockComputer Use

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

* [What Computer Use Can Do](#what-computer-use-can-do)
* [Real-World Example: Automated QA Testing](#real-world-example-automated-qa-testing)
* [How the Testing Process Works](#how-the-testing-process-works)
* [Setting Up Computer Use](#setting-up-computer-use)
* [Best Practices for Computer Use](#best-practices-for-computer-use)
