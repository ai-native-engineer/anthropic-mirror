<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/prompt-caching -->

Lesson 46 of 65 · Claude with Amazon BedrockPrompt caching

Prompt caching is a feature that speeds up Claude's responses and reduces the cost of text generation by reusing computational work from previous requests. To understand how this works, let's first look at what normally happens inside Claude during a typical request.

## How Claude Normally Processes Requests

When you send a message to Claude, a lot happens behind the scenes before you get a response back. Claude doesn't just immediately start generating text - it first does extensive work on your input message.

![](https://academy.claude.com/assets/media/0b475b8de7b1926e78bce51210694ae6bea02844cafe7d4400280cc17fad41f6.png)

Here's what Claude does with your message:

* Tokenize the prompt
* Create embeddings for each token
* Add context based on surrounding text
* Generate output text

![](https://academy.claude.com/assets/media/a89e1005631d685f9aa0e849cd24597b526f027289a88dd9f029146797d3f26c.png)

All of this preprocessing work happens before Claude generates any actual response. Once Claude finishes processing your request and sends back the response, it throws away all the computational work it just did.

![](https://academy.claude.com/assets/media/b31f901cebc4f169484a288f9927964c68dde33d8f0b7277990077bab37dd6ed.png)

## The Problem with Throwing Away Work

This creates an inefficiency when you're having conversations with Claude. Let's say you make a follow-up request that includes the same message from earlier, plus Claude's previous response, plus a new message to continue the conversation.

![](https://academy.claude.com/assets/media/c42f17f540a9d88d191c5c5c78fa86d6c07ca3cf34377f5404aea3a146f80f87.png)

When Claude sees that original message again, it has to redo all the same computational work it just threw away moments earlier. Claude essentially thinks: "I just processed this exact message and did all this work, then threw it away. Now I have to do it all over again."

![](https://academy.claude.com/assets/media/23a082b372fe8c501eb13986bda1cda0a544625ead4f5fb4fb645353e10fe28c.png)

## How Prompt Caching Solves This

Prompt caching addresses this inefficiency by saving the computational work instead of discarding it. Here's how it works:

![](https://academy.claude.com/assets/media/48e26c950efbe0b3261457890466175e9449908d23138ca6e17755388d574bc4.png)

When Claude processes your initial request, instead of throwing away all the preprocessing work, it stores that work in a cache. The cache acts like a lookup table that maps specific input messages to their corresponding computational results.

![](https://academy.claude.com/assets/media/9919962f137b9558ea678da27975afca62ec374e905f294e72ba34252a1d77c6.png)

When you make a follow-up request that includes the same content, Claude can check its cache and reuse the previous work instead of starting from scratch.

## Key Benefits and Limitations

![](https://academy.claude.com/assets/media/c6e44e4688cbd7852e70ea2ee247871eed0bf9a9c0c24cba493f630b87ae5275.png)

Prompt caching offers several advantages:

* Requests that use cached content are cheaper and faster to execute
* Initial request will write to the cache
* Follow up requests can read from the cache
* Cache lives for 5 minutes
* Only useful if you're repeatedly sending the same content (but this happens extremely frequently)

The cache has a 5-minute lifespan, so it's most beneficial for conversations or workflows where you're making multiple requests with overlapping content within a short timeframe. This pattern is actually very common in real applications - think about chatbots, document analysis tools, or any system that maintains conversation context.

Prompt caching is particularly valuable because many AI applications do repeatedly send the same content. Whether it's system prompts, conversation history, or large documents being analyzed, the same text often appears across multiple requests in a session.
