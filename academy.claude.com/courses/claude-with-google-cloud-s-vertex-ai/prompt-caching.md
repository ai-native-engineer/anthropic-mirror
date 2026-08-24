<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-caching -->

Lesson 46 of 66 · Claude with Google Cloud's Vertex AIPrompt caching

Prompt caching is a feature that speeds up Claude's responses and reduces the cost of text generation by reusing computational work from previous requests. Instead of throwing away all the processing work after each request, Claude can save and reuse it when you send similar content again.

## How Claude Normally Processes Requests

To understand prompt caching, let's first look at what happens during a typical request without caching enabled.

![](https://academy.claude.com/assets/media/f670a1e4bee760fe451429b9cf6ec359de06e991c8be6c3146336e1c6ac5ee2b.png)

When you send a message to Claude, it doesn't immediately start generating a response. Instead, Claude performs extensive preprocessing work on your input:

![](https://academy.claude.com/assets/media/6a0ffdf4274c14682d46d6ad1ed46969113c5d04a593b3d81573b8dd0602a58e.png)

* Tokenizes the prompt (breaks text into smaller units)
* Creates embeddings for each token (mathematical representations)
* Adds context based on surrounding text
* Only then generates the actual output text

![](https://academy.claude.com/assets/media/a9af83a2506539df02c2890f271e24de0692223c7432107bdb4a6dcb073250bc.png)

After sending you the response, Claude discards all this computational work. Everything gets thrown away, and Claude declares itself ready for the next request.

## The Problem with Repeated Content

Here's where things get inefficient. Imagine you're having a conversation with Claude, so your follow-up request includes:

![](https://academy.claude.com/assets/media/119df7860755d40acb3f9deea04b461c748cb93134c6923f209a4deb0de0acec.png)

* The same original user message from before
* Claude's previous response
* Your new follow-up message

![](https://academy.claude.com/assets/media/23a082b372fe8c501eb13986bda1cda0a544625ead4f5fb4fb645353e10fe28c.png)

Claude has to reprocess that original message all over again, even though it just analyzed the exact same content moments earlier. As Claude might think: "I just processed that message and threw away all the work I did. I could have reused it!"

## How Prompt Caching Solves This

Prompt caching changes this wasteful process. Instead of discarding the preprocessing work, Claude saves it in a cache.

![](https://academy.claude.com/assets/media/eaa63fb826afc14522f6f30cfa355e8c1ac1044d11f46af4bb226fb5c2f956cf.png)

Here's how it works:

1. **Initial request:** Claude processes your message and writes the computational work to a cache
2. **Follow-up requests:** When Claude sees the same content again, it reads the previously processed work from the cache instead of starting over

![](https://academy.claude.com/assets/media/cfa29c6ccc3b38c9f15403f6ab5eb2d52b600a9400d4dc7f2d39beeef30a7740.png)

The cache acts like a lookup table: "If I ever see this message again, I'll reuse this work I already did."

## Key Benefits and Limitations

![](https://academy.claude.com/assets/media/5f97d3d94b77e04e07b60802a35f57d2d4743ee22174320bbd4feb24875b68ee.png)

Prompt caching offers several advantages:

* **Faster responses:** Requests using cached content execute more quickly
* **Lower costs:** You pay less for processing that reuses cached work
* **Automatic optimization:** The initial request writes to cache, follow-up requests read from it

However, there are important limitations to keep in mind:

* **Short lifespan:** Cache only lives for 5 minutes
* **Exact matches required:** Only useful when you're repeatedly sending the same content
* **Common use case:** This happens extremely frequently in conversational applications and document analysis workflows

Prompt caching is particularly valuable for applications where users frequently reference the same documents, continue conversations, or iterate on similar prompts within a short timeframe.
