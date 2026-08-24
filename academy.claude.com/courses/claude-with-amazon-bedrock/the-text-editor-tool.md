<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/the-text-editor-tool -->

Lesson 32 of 65 · Claude with Amazon BedrockThe text editor tool

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# The text editor tool

Lesson 327 min

**Important Note: Up-to-date tool ID's for the text editor tool can be found in the AWS documentation here:** [**https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-tool-use.html#model-parameters-anthropic-anthropic-defined-tools**(opens in new tab)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-tool-use.html#model-parameters-anthropic-anthropic-defined-tools)

The Text Editor Tool is Claude's built-in capability that gives it file system access and text editing abilities. Unlike other tools where you write both the schema and implementation, Claude already knows how to request text editor operations - you just need to handle those requests.

## What the Text Editor Tool Does

This tool gives Claude the ability to work with files and directories like a software engineer would:

* View file or directory contents
* View specific ranges of lines in a file
* Replace text in files
* Create new files
* Insert text at specific line numbers

## How It Works

The Text Editor Tool is different from custom tools because only the JSON schema is built into Claude. You still need to provide the actual implementation.

![](https://academy.claude.com/assets/media/bdd9c2ad3349a4645fdba1babd3527ea810f72377369720f6ca911b571b7a946.png)

When you create custom tools, you write both sides - the schema that tells Claude about the tool, and the function that actually does the work. With the Text Editor Tool, Claude already has the schema, but you must write functions to handle Claude's requests to view, edit, or create files.

## Setting Up the Tool

To use the Text Editor Tool, you need to provide the tool version that matches your model:

python

```
# For Claude 4 and later models
text_editor = "text_editor_20250728"

# For earlier Claude models
text_editor = "text_editor_20250124"
```

The rest of this lesson uses the Claude 4 and later version; with `text_editor_20250124` the tool name is `str_replace_editor` instead, and an `undo_edit` command also exists.

You'll also need to modify your chat function to accept the text editor parameter and include it in the model configuration.

## Tool Commands

When Claude wants to use the text editor, it sends back tool use requests with specific commands:

![](https://academy.claude.com/assets/media/613a033d723bd2107764f31fbeb9d9f34483a57e89df4624ec31c0bdd1fa5ef2.png)

Your implementation needs to handle all four commands: view, str\_replace, create, and insert. Here's the basic structure for processing these requests:

python

```
def run_tool(tool_name, tool_input):
    if tool_name == "str_replace_based_edit_tool":
        command = tool_input.get("command", "")
        if command == "view":
            path = tool_input.get("path", "")
            return text_editor_tool.view(path)
        elif command == "str_replace":
            path = tool_input.get("path", "")
            old_str = tool_input.get("old_str", "")
            new_str = tool_input.get("new_str", "")
            return text_editor_tool.str_replace(path, old_str, new_str)
        # ... handle other commands
```

## Example: File Analysis

Here's how the tool works in practice. When you ask Claude to "Write a one sentence description of the code in the ./main.py file", this happens:

![](https://academy.claude.com/assets/media/a78ad2fdb4336bd24170a56c9f156b5817000b4ac5f79b5a7fbc0e5059ce8b27.png)

Claude sends a tool use request with `{"command": "view", "path": "./main.py"}`. Your server uses the TextEditorTool class to read the file and returns the contents. Claude then provides its analysis based on the code it read.

## Practical Applications

The Text Editor Tool essentially turns Claude into a code assistant that can:

* Read existing code and provide analysis
* Create new files and functions
* Modify existing code
* Set up test files
* Refactor code across multiple files

For example, you could ask Claude to "write a function to calculate pi to the 5th digit in main.py, then create a test.py file to test it." Claude will read the existing file, add the new function, create the test file, and write comprehensive tests - all automatically using the text editor commands.

This makes it possible to build AI-powered development tools similar to modern code editors with integrated AI features, where you can ask for code changes and have them implemented directly in your file system.

[Previous lessonFlexible tool extraction](https://academy.claude.com/courses/claude-with-amazon-bedrock/flexible-tool-extraction)[Next lessonQuiz on tool use](https://academy.claude.com/courses/claude-with-amazon-bedrock/quiz-on-tool-use)

Lesson 32 of 65 · Claude with Amazon BedrockThe text editor tool

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

* [What the Text Editor Tool Does](#what-the-text-editor-tool-does)
* [How It Works](#how-it-works)
* [Setting Up the Tool](#setting-up-the-tool)
* [Tool Commands](#tool-commands)
* [Example: File Analysis](#example-file-analysis)
* [Practical Applications](#practical-applications)
