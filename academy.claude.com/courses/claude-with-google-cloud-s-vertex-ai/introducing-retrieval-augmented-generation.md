<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/introducing-retrieval-augmented-generation -->

Lesson 34 of 66 · Claude with Google Cloud's Vertex AIIntroducing Retrieval Augmented Generation

Retrieval Augmented Generation (RAG) is a technique that helps you work with large documents when using Claude. Instead of cramming an entire 800-page financial report into a single prompt, RAG lets you intelligently find and include only the most relevant sections for each question.

## The Problem with Large Documents

Imagine you have a massive financial document and want to ask Claude specific questions about it, like "What risk factors does this company have?" You face a fundamental challenge: how do you get the right information from the document into Claude so it can answer your question effectively?

![](https://academy.claude.com/assets/media/aa2d6dcef1136beb3f94eac3d88c0e58c286f71cf7e6ba9c5711a9d75d987d86.png)

## Option 1: Include Everything in the Prompt

The first approach seems straightforward - extract all the text from the document and stuff it directly into your prompt along with the user's question.

![](https://academy.claude.com/assets/media/38c79483e6c91a124d55658918a5ab20523aa8089d0e031360e5f45d25078624.png)

This approach has several problems:

* There's a hard limit on how much text Claude can process - your document might be too long
* Claude becomes less effective with very long prompts
* Larger prompts cost more money and take longer to process

## Option 2: Break Documents into Chunks

The second approach is more sophisticated. You break the document into smaller chunks during a preprocessing step, then find and include only the chunks relevant to each user question.

![](https://academy.claude.com/assets/media/1a6d91701aed328e1e8a964098476303554d0ee3dbc081f14ea8c0c7184c3142.png)

Here's how it works: when a user asks "What risks does this company face?", you search through your chunks to find the one about "Risk Factors" and include only that section in your prompt to Claude.

![](https://academy.claude.com/assets/media/b28946e9396a7c6f9015727c34b282669ab472c30081b79cb1639c85df4c40e0.png)

## Benefits of the Chunking Approach

* Claude can focus on only the most relevant content
* Scales up to very large documents
* Works with multiple documents
* Smaller prompts cost less and run faster

## Challenges with Chunking

* Requires a preprocessing step to split documents
* Need a searching mechanism to find "relevant" chunks
* Included chunks might not contain all the context Claude needs
* Many ways to chunk text - which approach is best?

For example, if you only include the "Risk Factors" section, you might miss important context from the "Strategy Outlook" section that addresses how the company plans to handle those risks.

## This is RAG

Option 2 is Retrieval Augmented Generation. Despite its complexity, RAG offers significant advantages for working with large documents, but it comes with technical challenges that require careful consideration.

The key components of RAG are:

* Document preprocessing and chunking
* A search mechanism to find relevant chunks
* Intelligent selection of which chunks to include in prompts

When considering RAG for your application, you need to evaluate whether the benefits outweigh the additional complexity for your specific use case. The technique shines when working with large document collections where you need precise, contextual answers, but it requires more upfront engineering work than simply including entire documents in prompts.
