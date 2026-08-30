<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/json-schema-for-tools -->

Lesson 23 of 65 · Claude with Amazon BedrockJSON Schema for tools

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# JSON Schema for tools

Lesson 235 min

After creating your tool function, the next step is writing a JSON schema to describe it. This schema tells Claude what arguments your function expects and how to use it properly. While the configuration might look intimidating at first, it's actually straightforward once you understand the process.

## Understanding JSON Schema[](#understanding-json-schema)

JSON Schema isn't something invented just for AI tools - it's been around for years as a standard way to validate data. The schema has two main parts: the name and description at the top (which help Claude understand when to use the tool), and the actual schema that describes the function's arguments.

![](https://academy.claude.com/assets/media/4f9eb92ac92c4d104bd4188885d3eff8ed7b78c962a75bf4c3b1cc456894aff1.png)

The top section contains the tool's name and description, which helps Claude understand when to use it. The bottom section is the actual schema that describes your function's arguments in detail.

## Creating a JSON Schema: Step-by-Step[](#creating-a-json-schema-step-by-step)

Here's the simplest way to create a JSON schema for any function:

### Step 1: Write a Dictionary with Sample Data[](#step-1-write-a-dictionary-with-sample-data)

Take your function and create a dictionary of all keyword arguments with sample data. For example, if you have a function like this:

python

```
def process_data(ids, profile, primary_id, value):
    pass
```

Create a dictionary with sample values:

![](https://academy.claude.com/assets/media/45dc10d709dd7a8967367cbec8a349090f3613e3ef8dc7c7633e761e30d2cde7.png)

### Step 2: Convert to JSON[](#step-2-convert-to-json)

Convert your Python dictionary to proper JSON format. The main difference is changing Python's `True` to JSON's `true`.

![](https://academy.claude.com/assets/media/d177a699af0fe1303683ea4279df2ea3466ded1f78370ae949e062f3ddf260e0.png)

### Step 3: Use an Online Converter[](#step-3-use-an-online-converter)

Search for "JSON to JSON Schema converter" and use one of the many free online tools. Paste your JSON data and let it generate the schema automatically.

![](https://academy.claude.com/assets/media/fac5eb551cc26408c62aa5e1ea21ffa04b1b4dbeacb7312089a99b84ebad974e.png)

The tool will analyze your sample data and create a proper schema structure. Remove any `$schema` declarations from the output - you don't need them.

### Step 4: Add Descriptions[](#step-4-add-descriptions)

The most important step is adding detailed descriptions to each property. These descriptions help Claude understand exactly what each argument does and how to use it.

![](https://academy.claude.com/assets/media/1e49419e1af6a7f4e9b0ee35e6e2c01c0b85012d6819463b4f87122c3e915a97.png)

## Writing Good Descriptions[](#writing-good-descriptions)

When writing descriptions for your tools and properties, follow these best practices:

* Explain what the tool does, when to use it, and what it returns
* Aim for 3-4 sentences in your tool description
* Provide super detailed descriptions for each property
* If you're stuck, paste your function into Claude and ask it to write descriptions for you

Here's an example of a well-described tool schema:

![](https://academy.claude.com/assets/media/cf9af981071dbfc4414f4402c77be9c86a55a210fd62fb3daf543839d9685f4d.png)

Notice how the description clearly explains what the weather tool does, when to use it, what data it returns, and provides specific examples of valid location formats.

## Putting It All Together[](#putting-it-all-together)

Your final JSON schema should look something like this structure, with the `toolSpec` containing the name, description, and `inputSchema` with the detailed argument specifications:

![](https://academy.claude.com/assets/media/62744d87fb2e71403697f8f18ecf2be24fe1f1ffefff3c8ea39c04cc27652aec.png)

The schema acts as a contract between your code and Claude, ensuring that when Claude decides to use your tool, it knows exactly what information to provide and in what format. This clear communication is what makes tool use reliable and effective.

[Previous lessonTool functions](https://academy.claude.com/courses/claude-with-amazon-bedrock/tool-functions)[Next lessonHandling tool use responses](https://academy.claude.com/courses/claude-with-amazon-bedrock/handling-tool-use-responses)

Lesson 23 of 65 · Claude with Amazon BedrockJSON Schema for tools

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

* [Understanding JSON Schema](#understanding-json-schema)
* [Creating a JSON Schema: Step-by-Step](#creating-a-json-schema-step-by-step)
* [Writing Good Descriptions](#writing-good-descriptions)
* [Putting It All Together](#putting-it-all-together)
