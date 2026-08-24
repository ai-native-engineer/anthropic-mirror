<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/agents-and-tools -->

Lesson 64 of 66 · Claude with Google Cloud's Vertex AIAgents and tools

3. /[Claude with Google Cloud's Vertex AI](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai)

[Claude with Google Cloud's Vertex AI](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai)

# Agents and tools

Lesson 643 min

Agents represent a shift from the structured workflows we've explored earlier. While workflows excel when you know the exact steps needed to complete a task, agents shine when the path forward isn't clear. Instead of defining a rigid sequence, you give Claude a goal and a set of tools, then let it figure out how to combine those tools to achieve the objective.

![](https://academy.claude.com/assets/media/16fa498153525b728dcd64b59a13b14a0ed9675789cbef298959ad647a25cd00.png)

This flexibility makes agents attractive for developers. You can build an agent once, ensure it works reasonably well, and then deploy it to handle a wide variety of tasks. However, this approach comes with significant drawbacks around reliability and cost that we'll explore later.

## How Tools Make the Agent

The real power of agents lies in their ability to combine simple tools in unexpected ways. Consider a basic set of datetime tools we covered earlier in the course:

![](https://academy.claude.com/assets/media/7fd7b08522e76b8b19ae619ca26738f461c036eb5a3d728765e44549c5ed0be5.png)

* `get_current_datetime` - Returns the current date and time
* `add_duration_to_datetime` - Adds time to a given date
* `set_reminder` - Creates a reminder for a specific time

Each tool is simple on its own, but Claude can combine them to handle diverse requests:

![](https://academy.claude.com/assets/media/984ba3cc574af7e55b1590c9eec8ea81c87573a6af147f17fdd616f0d13bc2be.png)

For "What's the time?", Claude simply calls `get_current_datetime`. For "What day of the week is it in 11 days?", it chains `get_current_datetime` followed by `add_duration_to_datetime`. More complex requests like "Set a reminder to go to the gym next Wednesday" require all three tools in sequence.

Claude can even recognize when it needs additional information. When asked "When does my 90-day warranty expire?", it first asks the user when they obtained the warranty, then uses that information with `add_duration_to_datetime` to calculate the expiration date.

## Tools Should Be Abstract

The key insight for building effective agents is providing reasonably abstract tools rather than hyper-specialized ones. Claude Code demonstrates this principle perfectly.

![](https://academy.claude.com/assets/media/0870204ddda3d7af4bff0897edb5083e87a93a90b976697e1124eeedbbcf1ef1.png)

Claude Code has access to generic, flexible tools:

* `bash` - Run commands
* `glob` - Find files
* `grep` - Search file contents
* `read` - Read a file
* `write` - Create a file
* `edit` - Edit a file
* `webfetch` - Fetch a URL

Notice what Claude Code doesn't have - specialized tools like "Refactor" or "Run Tests" or "Install Dependencies". Instead, it figures out how to accomplish these tasks by combining the basic tools available. To install dependencies, it reads project files to understand the configuration, then uses bash to run the appropriate installation commands.

## Best Practice: Provide Reasonably Abstract Tools

When building agents, focus on tools that Claude can combine creatively rather than tools that solve one specific problem. Consider a social media video creation agent:

![](https://academy.claude.com/assets/media/315b4d5b327f0a3944c6dec53533b0216e0f0da0e989db4276e58bc46a71befe.png)

Effective tools for this agent might include:

* `bash` - Provides access to FFMPEG for video processing
* `generate_image` - Creates images from text prompts
* `text_to_speech` - Converts text to audio
* `post_media` - Publishes content to social media

This tool set enables both simple and complex interactions. A user might request "Create and post a video on Python programming," and the agent handles everything automatically. Alternatively, the interaction could be more collaborative:

![](https://academy.claude.com/assets/media/246eea9097e99cc6b00ca5178b06762fb06d486175088bf68f353cd556e9431a.png)

The user might say "I want you to make a video on Python, but first I want to pick out an initial image for the video." The agent can generate a sample image, show it to the user for approval, then proceed with video creation once confirmed.

This flexibility emerges naturally from providing the right level of abstraction in your tools. Each tool should be general enough to be useful in multiple contexts, but specific enough to accomplish meaningful work when combined with others.

[Previous lessonRouting workflows](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/routing-workflows)[Next lessonEnvironment inspection](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/environment-inspection)

Lesson 64 of 66 · Claude with Google Cloud's Vertex AIAgents and tools

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

* [How Tools Make the Agent](#how-tools-make-the-agent)
* [Tools Should Be Abstract](#tools-should-be-abstract)
* [Best Practice: Provide Reasonably Abstract Tools](#best-practice-provide-reasonably-abstract-tools)
