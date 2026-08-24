<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/agents-and-tools -->

Lesson 65 of 67 · Building with the Claude APIAgents and tools

3. /[Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api)

[Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api)

# Agents and tools

Lesson 653 min

Agents represent a shift from the structured workflows we've been working with. While workflows are perfect when you know the exact steps needed to complete a task, agents shine when you're not sure what those steps should be. Instead of defining a rigid sequence, you give Claude a goal and a set of tools, then let it figure out how to combine those tools to achieve the objective.

![](https://academy.claude.com/assets/media/8478d80427e9081aa66a7084783dfb337ac19806a7d4a29e7c2705ac54474fc3.jpg)

This flexibility makes agents attractive for building applications that need to handle varied, unpredictable tasks. You can create an agent once, ensure it works reasonably well, and then deploy it to solve a wide range of problems. However, this flexibility comes with trade-offs in reliability and cost that we'll explore later.

## How Tools Make the Agent

The real power of agents lies in their ability to combine simple tools in unexpected ways. Consider a basic set of datetime tools:

![](https://academy.claude.com/assets/media/7d814984b14a8cf9d543c3f61882d8abac783e7ce893730b5fc78f059839182c.jpg)

* `get_current_datetime` - Gets the current date and time
* `add_duration_to_datetime` - Adds time to a given date
* `set_reminder` - Creates a reminder for a specific time

These tools seem simple individually, but Claude can chain them together to handle surprisingly complex requests:

![](https://academy.claude.com/assets/media/7c1d89fa8e71f13aa3a2e6f097bdf0c47ce192d6e716044928dd3b3012a67209.jpg)

For "What's the time?", Claude simply calls `get_current_datetime`. But for "What day of the week is it in 11 days?", it chains `get_current_datetime` followed by `add_duration_to_datetime`. For setting a gym reminder next Wednesday, it might use all three tools in sequence.

Claude can even recognize when it needs more information. If you ask "When does my 90-day warranty expire?", it knows to ask when you purchased the item before calculating the expiration date.

## Tools Should Be Abstract

The key insight for building effective agents is providing reasonably abstract tools rather than hyper-specialized ones. Claude Code demonstrates this principle perfectly.

![](https://academy.claude.com/assets/media/4f6caa40d08beb99072be1d57118d7d346bd5d52c2307242d249cf1819ba7de0.jpg)

Claude Code has access to generic, flexible tools like:

* `bash` - Run any command
* `read` - Read any file
* `write` - Create any file
* `edit` - Modify files
* `glob` - Find files
* `grep` - Search file contents

It notably doesn't have specialized tools like "refactor code" or "install dependencies." Instead, Claude figures out how to use the basic tools to accomplish these complex tasks. This abstraction allows it to handle countless programming scenarios that the developers never explicitly planned for.

## Best Practice: Combinable Tools

When designing agents, provide tools that Claude can combine in creative ways. For example, a social media video agent might include:

![](https://academy.claude.com/assets/media/39ba419929e69d84456f4ad31a7c3296b292eb15d7a64a5a158efc0e65291fc0.jpg)

* `bash` - Access to FFMPEG for video processing
* `generate_image` - Create images from prompts
* `text_to_speech` - Convert text to audio
* `post_media` - Upload content to social platforms

This tool set enables both simple workflows (create and post a video) and more interactive experiences where the agent might generate a sample image first, get user approval, then proceed with video creation.

![](https://academy.claude.com/assets/media/0980bf9ff221f46f8d110f9a53eeea730ca1d487090685740bec60708bac5497.jpg)

The agent can adapt its approach based on user feedback and preferences, something that would be difficult to achieve with a rigid workflow. This flexibility is what makes agents powerful for building dynamic, user-responsive applications.

[Previous lessonRouting workflows](https://academy.claude.com/courses/building-with-the-claude-api/routing-workflows)[Next lessonEnvironment inspection](https://academy.claude.com/courses/building-with-the-claude-api/environment-inspection)

Lesson 65 of 67 · Building with the Claude APIAgents and tools

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

* [How Tools Make the Agent](#how-tools-make-the-agent)
* [Tools Should Be Abstract](#tools-should-be-abstract)
* [Best Practice: Combinable Tools](#best-practice-combinable-tools)
