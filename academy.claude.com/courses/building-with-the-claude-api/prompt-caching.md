<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/prompt-caching -->

Lesson 43 of 67 · Building with the Claude APIPrompt caching

Prompt caching is a feature that speeds up Claude's responses and reduces the cost of text generation by reusing computational work from previous requests. Instead of throwing away all the processing work after each request, Claude can save and reuse it when you send similar content again.

## How Claude Normally Processes Requests

To understand prompt caching, let's first look at what happens during a typical request without caching enabled.

![](https://academy.claude.com/assets/media/f34cfa8bf918544d8a4e65f33ee2a4a05df4b0e28c320fe58209e698fe879d0f.jpg)

When you send a message to Claude, it doesn't immediately start generating a response. Instead, Claude does a tremendous amount of preprocessing work on your input:

![](https://academy.claude.com/assets/media/2c5fc9b8ab8589af3aaf26b0c0665ec1a9e089f9179e38b8f8465d286c104709.jpg)

* Tokenizes the prompt into smaller pieces
* Creates embeddings for each token
* Adds context based on surrounding text
* Only then generates the actual output text

After sending you the response, Claude throws away all this computational work - the tokenization, embeddings, and context analysis all get discarded.

![](https://academy.claude.com/assets/media/c5670ac3a8561da33cfc6e7a1422f0ea6c4b3ff4be41950c6052ae130f608365.jpg)

## The Problem with Discarding Work

This becomes inefficient when you make follow-up requests that include the same content. For example, in a conversation where you're asking Claude to refine a summary of the same long text:

![](https://academy.claude.com/assets/media/162ab5f5fd0caa46c6da9ebc1b3027957dbd1134738199add3b54de2f830b602.jpg)

Claude has to repeat all the same preprocessing work on content it just analyzed moments ago. As Claude might think to itself: "I just processed that message and threw away all the work I did - I could have reused it!"

![](https://academy.claude.com/assets/media/3e5343f6f0943e88aac09a6b77080067181f0f6a66a7248b75c87567b34c5d11.jpg)

## How Prompt Caching Solves This

Prompt caching changes this workflow by saving the preprocessing work instead of discarding it:

![](https://academy.claude.com/assets/media/c53467e87036b0620d17f59efb60a8f2f2901c8b45932d3cbb1a86d9d8385797.jpg)

When you make an initial request, Claude performs all the usual preprocessing but stores the results in a cache instead of throwing them away. The cache acts like a lookup table that says "If I ever see this message again, I'll reuse this work I already did."

![](https://academy.claude.com/assets/media/4bbeab1fdbfa0b11b72db93eb6bf1387decf17ac54318d1a57a341b731914bb9.jpg)

## Key Benefits and Limitations

![](https://academy.claude.com/assets/media/78e580715d88f89b2704b59d9cf39db06990cf031d081efff2b72ba6df0d1603.jpg)

Prompt caching offers several advantages:

* **Faster responses:** Requests using cached content execute more quickly
* **Lower costs:** You pay less for the cached portions of your requests
* **Automatic optimization:** The initial request writes to the cache, follow-up requests read from it

However, there are important limitations to keep in mind:

* **Cache duration:** By default, cached content lives for 5 minutes, and each reuse refreshes that timer at no extra cost. You can optionally extend the lifetime to 1 hour, which carries a higher cache-write price.
* **Limited use cases:** Only beneficial when you're repeatedly sending the same content
* **High frequency requirement:** Most effective when the same content appears extremely frequently in your requests

Prompt caching works best for scenarios like document analysis workflows, where you're asking multiple questions about the same large document, or iterative editing tasks where the base content remains constant while you refine specific aspects.
