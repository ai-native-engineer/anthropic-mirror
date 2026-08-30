<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/making-a-request -->

Lesson 3 of 65 · Claude with Amazon BedrockMaking a request

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Making a request

Lesson 310 min

Making your first API request to AWS Bedrock requires three essential components: a Bedrock Runtime Client to connect to the service, a Model ID to specify which model you want to run, and a User Message containing the text you want to feed into the model.

## Setting Up the Bedrock Client[](#setting-up-the-bedrock-client)

Start by creating a client using boto3 to connect to the Bedrock runtime service:

python

```
import boto3

client = boto3.client("bedrock-runtime", region_name="us-west-2")
```

## Understanding Model IDs and Regional Availability[](#understanding-model-ids-and-regional-availability)

Here's where things get tricky. Not every model is available in every AWS region. If you try to run a model that doesn't exist in your chosen region, you'll get a cryptic error message saying the model doesn't exist.

![](https://academy.claude.com/assets/media/c93ba7b7d44d11d5d029f2709c08988d47141b76038f1d025b299646d8b709a1.png)

For example, if Claude Sonnet is available in us-west-2 but you're making requests from us-east-1, your request will fail.

![](https://academy.claude.com/assets/media/bcba2fe357dd53df9ec27b5edeb98ede867d3615e0e291a9a17469c608bc80e2.png)

## Using Inference Profiles[](#using-inference-profiles)

Inference profiles solve the regional availability problem by automatically routing your requests to a region where your chosen model is actually hosted.

![](https://academy.claude.com/assets/media/d4643acb25d958cd530ce9fe7ff978f7d5008aa65475bb0ca5f007a026115c27.png)

Instead of tracking which models are in which regions, you can use an inference profile that knows the model is available in multiple regions like us-west-2 and us-east-2.

![](https://academy.claude.com/assets/media/4789ffaf0596fa27ae75b1d8b18808aebeb282677f9b7eac625a369f601208ac.png)

When you make a request using an inference profile, AWS automatically routes it to the correct region where your model exists, even if you're connecting from a different region.

To find inference profile IDs, go to the AWS Bedrock console and look under "Cross-region inference" rather than using the model ID from the main model catalog page.

![](https://academy.claude.com/assets/media/8d6a91b2c2190a620782d010aa6f0e5343f8934d1809e2b673aa253d82daa4a8.png)

Copy the inference profile ID for your chosen model. The examples in this course use Claude Haiku 4.5, whose inference profile ID is `us.anthropic.claude-haiku-4-5-20251001-v1:0`.

## Creating User Messages[](#creating-user-messages)

User messages have a specific structure that might look overly complex at first, but there's a good reason for it:

python

```
user_message = {
    "role": "user",
    "content": [
        {"text": "What's 1+1?"}
    ]
}
```

The content is a list because a single message can contain different types of content - text, images, or other media types. This structure allows you to send multimodal requests.

![](https://academy.claude.com/assets/media/224c2c12f355b33dfe64e5b1e5105b54154311b98b229085514f7598e67108bd.png)

## Making the Request[](#making-the-request)

Now you can make your API call using the converse method:

python

```
response = client.converse(
    modelId=model_id,
    messages=[user_message]
)
```

The response contains a lot of metadata, but to get just the generated text, you need to navigate through the response structure:

python

```
response["output"]["message"]["content"][0]["text"]
```

## Understanding Message Types[](#understanding-message-types)

There are two main message types you'll work with:

* **User messages** - Content you want to feed into the model (role: "user")
* **Assistant messages** - Content the model has produced (role: "assistant")

![](https://academy.claude.com/assets/media/059b35dbd386649cbe09f243d35616c1df97af81e9519fbf3aaef5bb9f167d65.png)

Both message types follow the same structure with a role and content list. This consistency makes it easy to build conversations by alternating between user and assistant messages.

The assistant message you get back from Bedrock follows the exact same format as your user message, just with a different role. This standardized structure makes it straightforward to chain multiple requests together for longer conversations.

[Previous lessonAccessing the API](https://academy.claude.com/courses/claude-with-amazon-bedrock/accessing-the-api)[Next lessonMulti-Turn conversations](https://academy.claude.com/courses/claude-with-amazon-bedrock/multi-turn-conversations)

Lesson 3 of 65 · Claude with Amazon BedrockMaking a request

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

* [Setting Up the Bedrock Client](#setting-up-the-bedrock-client)
* [Understanding Model IDs and Regional Availability](#understanding-model-ids-and-regional-availability)
* [Using Inference Profiles](#using-inference-profiles)
* [Creating User Messages](#creating-user-messages)
* [Making the Request](#making-the-request)
* [Understanding Message Types](#understanding-message-types)
