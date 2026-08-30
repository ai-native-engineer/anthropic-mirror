<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/extended-thinking -->

Lesson 42 of 65 · Claude with Amazon BedrockExtended thinking

3. /[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

[Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)

# Extended thinking

Lesson 427 min

Extended thinking is Claude's advanced feature that gives the model time to reason through complex problems before generating a final response. Think of it as Claude's internal monologue - you can see how it approaches your problem step by step.

![](https://academy.claude.com/assets/media/0bd1c482a9cdf3617fbf43e2386eea9cd78fe67c3ad91b25908844201784558c.png)

## How Extended Thinking Works[](#how-extended-thinking-works)

When you enable extended thinking, Claude's response includes two parts instead of one:

* **Reasoning Content Part** - Claude's internal thinking process
* **Text Part** - The final response you actually wanted

![](https://academy.claude.com/assets/media/7737b60029d867e83be1ad7abaea1c521cfb6cedbbad66a74b5560b6aed71a0e.png)

The reasoning content shows you exactly how Claude breaks down your problem, what it considers, and how it arrives at its final answer. This transparency can be incredibly valuable for understanding and debugging complex tasks.

## Trade-offs to Consider[](#trade-offs-to-consider)

Extended thinking comes with clear benefits and costs:

* **Better accuracy** on complex tasks
* **Higher cost** - you pay for all thinking tokens
* **Increased latency** - thinking takes time

The key decision point is simple: use your evaluations. If you've already optimized your prompt but still aren't getting the accuracy you need, that's when extended thinking becomes worth considering.

## The Signature System[](#the-signature-system)

One important detail you'll notice immediately is the cryptographic signature attached to reasoning content:

![](https://academy.claude.com/assets/media/fd50c9e46194b656ccf7369d31035d2a5459e0e1adf556a39ed535c1e2b91ced.png)

This signature ensures you can't modify the thinking text. If you want to include Claude's previous reasoning in a follow-up conversation, the signature verifies the content hasn't been tampered with. This prevents potential safety issues from modified reasoning text.

## Redacted Content[](#redacted-content)

Sometimes Claude's thinking gets flagged by safety systems. When this happens, you'll receive a `redactedContent` field instead of readable thinking text:

![](https://academy.claude.com/assets/media/78c6e80cb4759302f2168576aca51757419eaf3970c816d3e0c2775ffed8dfac.png)

The redacted content is encrypted but still functional - you can pass it back to Claude in future conversations without losing context. It's just not readable to you as a developer.

## Implementation[](#implementation)

On current Claude models, such as Claude Opus 5 and Claude Sonnet 5, thinking runs as **adaptive thinking** and is on by default: Claude decides how much reasoning each request needs, with no token budget to manage. These models omit the reasoning text unless you ask for it, so set `display` to `summarized` to see it:

python

```
additional_model_fields["thinking"] = {
    "type": "adaptive",
    "display": "summarized"
}
```

With adaptive thinking on, simple questions often come back quickly while harder ones get more reasoning time. To guide how much Claude thinks, you can combine adaptive thinking with the `effort` parameter. The effort level acts as soft guidance for Claude's thinking allocation, and it takes the place of the manual token budget you would otherwise manage.

If you've used extended thinking before, note that the manual configuration is being phased out: `thinking.type: "enabled"` with `budget_tokens` is deprecated on Claude Opus 4.6 and Claude Sonnet 4.6, and Claude Opus 4.7 and later models, including Claude Opus 5 and Claude Sonnet 5, do not support it and reject such requests with a 400 error. Use `thinking.type: "adaptive"` with the `effort` parameter instead.

### Models without adaptive thinking[](#models-without-adaptive-thinking)

The Claude 4.5 models (Claude Haiku 4.5, Claude Sonnet 4.5, and Claude Opus 4.5) and earlier models do not support adaptive thinking. On those models you enable extended thinking with a manual token budget:

python

```
additional_model_fields["thinking"] = {
    "type": "enabled",
    "budget_tokens": thinking_budget
}
```

The `thinking_budget` controls how many tokens Claude can spend on reasoning. The minimum is 1024 tokens, but you might need more for complex problems. Like everything else with Claude, use your evaluations to find the right budget for your use case.

Here's how the updated chat function looks:

python

```
def chat(
    messages,
    system=None,
    temperature=1.0,
    stop_sequences=[],
    tools=None,
    tool_choice="auto",
    text_editor=None,
    thinking=False,
    thinking_budget=1024
):
```

## Testing Your Implementation[](#testing-your-implementation)

When building applications that handle extended thinking, you'll want to test both normal reasoning content and redacted content scenarios. There's actually a special test string that forces Claude to return redacted content - useful for making sure your code handles both cases properly.

The most important takeaway about extended thinking is that the decision to use it should always be data-driven. Run your evaluations first, optimize your prompts, and only then consider extended thinking if you need that extra boost in accuracy for complex tasks. That discipline rests on a simple habit: decide what good looks like before you reach for more capability. When you know the accuracy your task needs, you can tell whether extended thinking earns its cost instead of guessing.

## Practice: run adaptive thinking yourself[](#practice-run-adaptive-thinking-yourself)

Adaptive thinking is easiest to understand by watching it make decisions. In the code where you have been building the chat function, turn it on:

python

```
additional_model_fields["thinking"] = {
    "type": "adaptive",
    "display": "summarized"
}
```

Now send two requests through this same configuration. First ask a quick factual question you already know the answer to. Then ask a genuinely hard one, like a multi-step analysis problem from your own work. If you are working on a model that does not support adaptive thinking, enable thinking with the manual `budget_tokens` configuration from the section above and run the same two requests.

### Check what the thinking did[](#check-what-the-thinking-did)

Setting the flag only proves the request was accepted. These checks tell you what the thinking did:

1. **Confirm thinking engaged.** Each response should now contain two parts, the reasoning content and the final text, instead of text alone. The one exception is redacted content, which you saw earlier: a `redactedContent` field means thinking ran but the text is encrypted.
2. **Read the reasoning content.** Check that it genuinely reasons about the question you asked rather than restating it. This is the same transparency you will rely on when debugging complex tasks later.
3. **Compare the two requests.** The simple question will usually come back quickly with little reasoning, while the hard one gets noticeably more. That difference is adaptive thinking making the allocation decision for you.
4. **Weigh the cost.** You pay for every thinking token, so check whether the harder answer is better than what you get without thinking. Your evaluations are the judge of that, and seeing reasoning text appear is no substitute for them.

The behavior worth keeping from this lesson: whenever you enable extended thinking on a new task, read the reasoning content on a few representative requests and re-run your evaluations before deciding the setting stays.

[Previous lessonQuiz on Retrieval Augmented Generation](https://academy.claude.com/courses/claude-with-amazon-bedrock/quiz-on-retrieval-augmented-generation)[Next lessonImage support](https://academy.claude.com/courses/claude-with-amazon-bedrock/image-support)

Lesson 42 of 65 · Claude with Amazon BedrockExtended thinking

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

* [How Extended Thinking Works](#how-extended-thinking-works)
* [Trade-offs to Consider](#trade-offs-to-consider)
* [The Signature System](#the-signature-system)
* [Redacted Content](#redacted-content)
* [Implementation](#implementation)
* [Testing Your Implementation](#testing-your-implementation)
* [Practice: run adaptive thinking yourself](#practice-run-adaptive-thinking-yourself)
