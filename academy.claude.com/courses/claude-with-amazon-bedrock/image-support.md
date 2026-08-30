<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/image-support -->

Lesson 43 of 65 · Claude with Amazon BedrockImage support

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Image support

Lesson 439 min

Claude's vision capabilities allow you to include images in your messages and ask Claude to analyze, compare, count objects, or perform virtually any visual task you can imagine. This opens up powerful possibilities for applications ranging from document analysis to automated assessments.

## Image Handling Basics[](#image-handling-basics)

When working with images in Claude, you need to understand a few key limitations:

* Up to 20 images across all messages in a single request
* Max size of 3.75MB
* Max height/width of 8000px
* Each image counts as a certain number of tokens: `tokens = (width px × height px) / 750`

![](https://academy.claude.com/assets/media/526d6a757d8d880fe2d248896cf82c9fcab501795d46eed54dc629dcd228399f.png)

To include an image, you add it as another type of message part. For each image you want to send, you include one image part in your user message. The structure looks like this:

python

```
with open("image.png", "rb") as f:
    image_bytes = f.read()

add_user_message(messages, [
    {
        "image": {
            "format": "png",
            "source": {"bytes": image_bytes}
        }
    },
    {"text": "What do you see in this image?"}
])
```

## Multiple Images[](#multiple-images)

You can send multiple images in a single message by adding multiple image parts. Claude can then analyze relationships between images, compare them, or answer questions that require understanding multiple visual inputs.

![](https://academy.claude.com/assets/media/eb3d93da4c6eae9dfbb42c81d9af0310645c111350adb26c2940b3906eb97d9d.png)

## Prompting Techniques[](#prompting-techniques)

The most important thing to understand about Claude's vision capabilities is that all the same prompting engineering techniques apply to images. You can dramatically increase Claude's vision accuracy by providing guidelines, analysis steps, or using one-shot/multi-shot examples.

![](https://academy.claude.com/assets/media/a44d1b913150f04b56211cbb5236f2ea95cae516f182aa779715df8a4512d478.png)

For example, instead of simply asking "How many marbles are in this image?", you can provide a structured approach:

```
Analyze this image of marbles and determine the exact count using this methodology:
1. Begin by identifying each unique marble one at a time. Assign each a number as you identify it.
2. Verify your result by counting with a different method. Start from the bottom-left corner and work row by row, from left to right.
What is the exact, verified number of marbles in this image?
```

![](https://academy.claude.com/assets/media/6f2b0e93d9c939e8aaac277640ff521cfe27d54a8bc87a1b71b8e5dba06c61cf.png)

Another effective technique is one-shot prompting, where you provide an example image with the correct analysis before asking Claude to analyze your target image:

![](https://academy.claude.com/assets/media/2c5f3cf4f134638be4f1040e7c813ec8a27d3fc0e8d68c5b995a8e7c265d32b0.png)

## Real-World Example: Fire Risk Assessments[](#real-world-example-fire-risk-assessments)

A practical application of Claude's vision capabilities is automated fire risk assessment for insurance companies. Instead of sending inspectors to each property, companies can use high-resolution satellite imagery and ask Claude to evaluate fire risks.

![](https://academy.claude.com/assets/media/80ed96dcab575198d37f2de1bf938f5613e751b5f7047e83eca7b57e2e4108dd.png)

The system can analyze several key factors:

* Dense, close-packed trees near the residence
* Difficult access routes for emergency vehicles
* Branches overhanging the residence
* Overall tree density and spacing

Here's how you might structure such an analysis:

python

```
with open('./images/prop7.png', 'rb') as f:
    image_bytes = f.read()

messages = []

add_user_message(messages, [
    {"image": {"format": "png", "source": {"bytes": image_bytes}}},
    {"text": prompt}
])

response = chat(messages)
```

The key to success with this type of complex visual analysis is providing detailed, structured prompts that guide Claude through specific analysis steps rather than asking for a simple assessment.

Remember: when working with images, don't fall into the trap of using simple prompts. Apply the same prompt engineering techniques you've learned for text-based interactions to dramatically improve Claude's visual analysis accuracy.

[Previous lessonExtended thinking](https://academy.claude.com/courses/claude-with-amazon-bedrock/extended-thinking)[Next lessonPDF support](https://academy.claude.com/courses/claude-with-amazon-bedrock/pdf-support)

Lesson 43 of 65 · Claude with Amazon BedrockImage support

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

* [Image Handling Basics](#image-handling-basics)
* [Multiple Images](#multiple-images)
* [Prompting Techniques](#prompting-techniques)
* [Real-World Example: Fire Risk Assessments](#real-world-example-fire-risk-assessments)
