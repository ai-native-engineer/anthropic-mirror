<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/temperature -->

Lesson 6 of 65 · Claude with Amazon BedrockTemperature

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Temperature

Lesson 65 min

Temperature is a powerful parameter that controls how creative or deterministic Claude's responses will be. Understanding how to use it effectively can dramatically improve your AI applications.

## How Claude Generates Text

Before diving into temperature, it's helpful to understand Claude's text generation process. When you send Claude a prompt like "What do you think?", it goes through three phases:

* **Tokenization:** Breaking your input into smaller chunks
* **Prediction:** Calculating probabilities for possible next tokens
* **Sampling:** Selecting a token based on those probabilities

![](https://academy.claude.com/assets/media/b83b845133d34175d2fa01b5bb5329ef596bb96b65c82bd5415a8bdf29f71d22.png)

In the diagram above, you can see how Claude might assign different probabilities to potential next tokens. The word "about" has a 30% chance, "would" has 20%, and so on. This process repeats for each token until the response is complete.

![](https://academy.claude.com/assets/media/fd8b6aa732eb08b6b96b37f58cdfa4f457ad26b60606200f75490e64edee5bb5.png)

## What Temperature Does

Temperature is a decimal value between 0 and 1 that directly influences these token selection probabilities. Think of it as a creativity dial:

* **Low temperature (near 0):** Makes the highest probability token much more likely to be selected
* **High temperature (near 1):** Distributes probability more evenly across all possible tokens

![](https://academy.claude.com/assets/media/006332a5c3d92fa135d7a4910b5d622c9fc9793ab61f751103494a6f474e6b7d.png)

At temperature 0, Claude becomes deterministic - it will always pick the most probable token. At temperature 1, lower-probability tokens have a much better chance of being selected, leading to more creative and varied outputs.

## Temperature Ranges and Use Cases

Different tasks call for different temperature settings:

![](https://academy.claude.com/assets/media/939a7ade13434b2fa7c8d519d428465b1803736f5ef6432020a4a241aa14360d.png)

### Low Temperature (0.0 - 0.3)

* Factual responses
* Coding assistance
* Data extraction
* Content moderation

### Medium Temperature (0.4 - 0.7)

* Summarization
* Educational content
* Problem-solving
* Creative writing with constraints

### High Temperature (0.8 - 1.0)

* Brainstorming
* Creative writing
* Marketing content
* Joke generation

## Setting Temperature in Code

By default, Claude's temperature is set to 1.0, which means maximum creativity. You can override this by adding temperature to your inference configuration:

python

```
def chat(messages, system=None, temperature=1.0):
    params = {
        "modelId": model_id,
        "messages": messages,
        "inferenceConfig": {"temperature": temperature}
    }

    if system:
        params["system"] = [{"text": system}]

    response = client.converse(**params)
    return response["output"]["message"]["content"][0]["text"]
```

## Temperature in Practice

Here's a practical example using movie idea generation. With temperature set to the default (1.0), you might get creative responses like:

*"A reclusive origami master discovers her intricate paper creations come to life at night, leading her on a magical journey to save their miniature world from a mysterious shadow creature threatening to unfold their existence."*

But when you set temperature to 0.0 for the same prompt, you'll consistently get more predictable responses:

*"A time-traveling archaeologist must prevent ancient artifacts from being stolen by a tech billionaire who's using them to build a doomsday device that harnesses their forgotten power."*

Running the low-temperature version multiple times will produce very similar responses, often with repeated themes like "time-traveling historian" or "time-traveling archaeologist."

## Key Takeaways

Temperature gives you direct control over Claude's creativity level. Use lower temperatures when you need consistent, factual responses, and higher temperatures when you want creative, varied outputs. The default temperature of 1.0 maximizes creativity, so consider lowering it for tasks requiring precision and consistency.

[Previous lessonSystem prompts](https://academy.claude.com/courses/claude-with-amazon-bedrock/system-prompts)[Next lessonStreaming](https://academy.claude.com/courses/claude-with-amazon-bedrock/streaming)

Lesson 6 of 65 · Claude with Amazon BedrockTemperature

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

* [How Claude Generates Text](#how-claude-generates-text)
* [What Temperature Does](#what-temperature-does)
* [Temperature Ranges and Use Cases](#temperature-ranges-and-use-cases)
* [Setting Temperature in Code](#setting-temperature-in-code)
* [Temperature in Practice](#temperature-in-practice)
* [Key Takeaways](#key-takeaways)
