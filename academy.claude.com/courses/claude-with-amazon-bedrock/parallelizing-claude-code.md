<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/parallelizing-claude-code -->

Lesson 61 of 65 · Claude with Amazon BedrockParallelizing Claude Code

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Parallelizing Claude Code

Lesson 613 min

Running multiple instances of Claude Code in parallel is one of the biggest productivity gains you can achieve. Since Claude is lightweight, you can easily spin up several copies, assign each a different task, and have them work simultaneously. This effectively gives you a team of virtual software engineers working on your project.

## The Challenge: File Conflicts[](#the-challenge-file-conflicts)

The main problem with parallel instances is that they might try to modify the same files at the same time. This can lead to conflicting or invalid code since each instance isn't aware of what the others are doing.

![](https://academy.claude.com/assets/media/23c2b65a689b211558ee5f064078042d0535c0d10f4b80bd5f094dfb2c879b7e.png)

The solution is to give each Claude instance its own separate workspace. Each instance works with its own copy of your project, makes changes in isolation, and then merges those changes back into your main project.

![](https://academy.claude.com/assets/media/3a6bb5b1df65e93091dcc1a1787b12d88c05df95497c7e0b46f802eeaeb89095.png)

## Git Worktrees[](#git-worktrees)

Git worktrees are perfect for this workflow. If your project is already managed by Git, you can use worktrees immediately. They're like an extension of Git's branching functionality that lets you create complete copies of your project in separate directories on your machine.

![](https://academy.claude.com/assets/media/950a050ee2b081d9db4b04d04b487afb506d797d846bf494df58912a8c0a2807.png)

Each worktree corresponds to a separate branch. You can have one folder for feature A and another for feature B, each containing a complete copy of your codebase. Then you run separate Claude Code instances in each worktree, working in total isolation.

![](https://academy.claude.com/assets/media/536e6bef11940caea62b1d41d10070eb1e2a220811cb0ff388da1af20b4d2c79.png)

Once each Claude instance finishes its feature, you commit the work and merge it back into your main branch, just like merging any normal Git branch.

![](https://academy.claude.com/assets/media/ad6aa49fddf47e8f7a267db97aaa4913d12c95fea4812cfcabc0514fa5acce73.png)

## Automating Worktree Creation[](#automating-worktree-creation)

This might sound complicated to manage, but you can delegate the entire workflow to Claude Code itself. You can write a prompt that asks Claude to:

1. Create a new git worktree in a specific folder
2. Symlink dependencies that aren't tracked by Git
3. Launch a new VS Code instance in that directory

![](https://academy.claude.com/assets/media/8b857191538aca7ffc5a0a7ba8b5b63ae23497444cdadbf0ede58756341b4218.png)

## Custom Commands[](#custom-commands)

Rather than copying and pasting long prompts every time, you can create custom slash commands in Claude Code. Add a `.md` file to `.claude/commands` to create a custom command.

![](https://academy.claude.com/assets/media/518237ab1b5c747edc756586e07903d4e20e5a84fc967528561f724331affa48.png)

The custom command can reference `$ARGUMENTS`, which gets replaced with whatever arguments you pass to your command. For example:

* `/project:create_worktree feature_a` creates a worktree named "feature\_a"
* `/project:create_worktree develop` creates a worktree named "develop"

## Parallel Development in Action[](#parallel-development-in-action)

Here's how the complete workflow looks in practice. You can create multiple worktrees for different features:

![](https://academy.claude.com/assets/media/fa078fbbc5d07ffea2fdbd7703d792523ff28b6b9f66ad2be679b215e5854d77.png)

Each Claude instance works on its assigned task:

* Update document tests
* Add logging
* Add note-taking tools
* Add a subtract tool

![](https://academy.claude.com/assets/media/7100def75d32908917a6793170501668a72d5131b39e71549ccfb6b06c97e079.png)

## Merging Changes[](#merging-changes)

When the features are complete, you can automate the merge process too. Create another custom command that tells Claude to:

1. Change into the worktree directory
2. Examine the latest commit
3. Change back to the root directory
4. Merge the worktree branch
5. Handle any merge conflicts automatically

![](https://academy.claude.com/assets/media/0cfd5f360ce83f3a7a29a93486a909ab400fcc51b73a9f3701fc7f9ad7cf3959.png)

Claude can even resolve merge conflicts automatically based on its understanding of the changes made in each branch.

## Results[](#results)

This approach scales to as many parallel instances as you can manage. Instead of working on features sequentially, you can have multiple Claude instances developing different parts of your project simultaneously. It's like having your own team of developers, each working in their own isolated environment before bringing their work together.

The productivity gains are substantial - you're essentially multiplying your development capacity by the number of parallel instances you run.

[Previous lessonEnhancements with MCP servers](https://academy.claude.com/courses/claude-with-amazon-bedrock/enhancements-with-mcp-servers)[Next lessonAutomated debugging](https://academy.claude.com/courses/claude-with-amazon-bedrock/automated-debugging)

Lesson 61 of 65 · Claude with Amazon BedrockParallelizing Claude Code

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

* [The Challenge: File Conflicts](#the-challenge-file-conflicts)
* [Git Worktrees](#git-worktrees)
* [Automating Worktree Creation](#automating-worktree-creation)
* [Custom Commands](#custom-commands)
* [Parallel Development in Action](#parallel-development-in-action)
* [Merging Changes](#merging-changes)
* [Results](#results)
