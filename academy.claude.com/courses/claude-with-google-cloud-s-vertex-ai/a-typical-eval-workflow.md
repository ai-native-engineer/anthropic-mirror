<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/a-typical-eval-workflow -->

Lesson 11 of 66 · Claude with Google Cloud's Vertex AIA typical eval workflow

3. /[Claude with Google Cloud's Vertex AI](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai)

[Claude with Google Cloud's Vertex AI](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai)

# A typical eval workflow

Lesson 118 min

A typical prompt evaluation workflow follows five key steps that help you systematically improve your prompts through objective measurement. While there are many different ways to assemble these workflows and various open source and paid tools available, understanding the core process helps you start small and scale up as needed.

![](https://academy.claude.com/assets/media/c7dc99eee2300e25b5e601d4873fb6fc50dd72ef7781e054a2da3139d7087179.png)

## Step 1: Draft a Prompt

Start by writing an initial prompt that you want to improve. For this example, we'll use a simple prompt:

python

```
prompt = f"""
Please answer the user's question:

{question}
"""
```

![](https://academy.claude.com/assets/media/1d125564307d10c1fce46b50e731bd38b8ef51381dd330927f826d17d698f007.png)

This basic prompt will serve as our baseline for testing and improvement.

## Step 2: Create an Evaluation Dataset

Your evaluation dataset contains sample inputs that you'll feed into your prompt. Since our prompt only has one input (the user's question), we need a collection of different questions to test with.

![](https://academy.claude.com/assets/media/204aa70281126d75cbe56bb5b8925018ba22f69d862b09c5d33b05e508dc5620.png)

The dataset contains questions that we will merge with our prompt. You can assemble these datasets by hand or generate them using Claude. In real-world evaluations, you might have tens, hundreds, or even thousands of different records, but we'll start with just three questions for this example:

* What's 2+2?
* How do I make oatmeal?
* How far away is the Moon?

## Step 3: Feed Through Claude

Take each question from your dataset and merge it with your prompt template to create complete prompts. Then send each one to Claude and collect the responses.

![](https://academy.claude.com/assets/media/cbbc8e6ec17e34a40c891f578de10dbe3642a10e0de6a0a863df5db43759bed3.png)

For example, the first question becomes a complete prompt that Claude processes and returns an answer like "2 + 2 = 4". You repeat this process for all questions in your dataset, building a collection of question-answer pairs.

## Step 4: Feed Through a Grader

Now comes the crucial step of objectively measuring the quality of Claude's responses. You take each question-answer pair and feed them into a grader that scores the responses.

![](https://academy.claude.com/assets/media/d78f04e3f2294bee5d220762184603602cb18750c969c3e0c547d017f78a8068.png)

The grader assigns scores (typically 1-10) based on answer quality:

* 10 = Perfect answer with no room for improvement
* 4 = Adequate but definitely room for improvement
* Lower scores indicate poor responses

After scoring all responses, you average the scores together. In our example, scores of 10, 4, and 9 average to 7.66, giving you an objective measurement of your prompt's performance.

![](https://academy.claude.com/assets/media/0e9f812d824c4b31dfaa72e4983983fa9c519b253da93fc2501323e178157ee1.png)

## Step 5: Change Prompt and Repeat

With your baseline score established, you can now modify your prompt and run the entire process again to see if your changes improve performance.

![](https://academy.claude.com/assets/media/8ea9ee875981cf215a529a826e10a560adeede1df88e88a22c4670ffce24845e.png)

For example, you might enhance the original prompt by adding more specific instructions:

python

```
prompt = f"""
Please answer the user's question:

{question}

Answer the question with ample detail
"""
```

## Prompt Scoring

The power of this workflow lies in getting objective measurements of prompt performance. You can compare scores between different prompt versions to determine which performs better.

![](https://academy.claude.com/assets/media/b0a62f4f11b13c7465479f01619c313baac6f88f43b133557f8a3dfd90faccad.png)

In our example:

* Prompt v1 scored 7.66
* Prompt v2 scored 8.7

The higher score for v2 provides objective evidence that adding "Answer the question with ample detail" improved the prompt's performance. You can then use the better-performing version or continue iterating to achieve even higher scores.

This systematic approach removes guesswork from prompt improvement and gives you a reliable framework for optimization. While there's complexity in implementing effective graders, this workflow provides a solid foundation for building your own evaluation system.

[Previous lessonPrompt evaluation](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-evaluation)[Next lessonGenerating test datasets](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/generating-test-datasets)

Lesson 11 of 66 · Claude with Google Cloud's Vertex AIA typical eval workflow

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

* [Step 1: Draft a Prompt](#step-1-draft-a-prompt)
* [Step 2: Create an Evaluation Dataset](#step-2-create-an-evaluation-dataset)
* [Step 3: Feed Through Claude](#step-3-feed-through-claude)
* [Step 4: Feed Through a Grader](#step-4-feed-through-a-grader)
* [Step 5: Change Prompt and Repeat](#step-5-change-prompt-and-repeat)
* [Prompt Scoring](#prompt-scoring)
