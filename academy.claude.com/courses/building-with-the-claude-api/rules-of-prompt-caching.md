<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/rules-of-prompt-caching -->

Lesson 44 of 67 · Building with the Claude APIRules of prompt caching

Prompt caching in Claude works by storing the computational work done on your messages so it can be reused in follow-up requests. This makes subsequent requests both faster and cheaper to execute, but only when you're repeatedly sending identical content.

![](https://academy.claude.com/assets/media/5f73b85b403282f7f9ffd86dcf5d3861079d984f1e7021f9731288ded9139696.jpg)

The process is straightforward: your initial request writes processing work to the cache, and follow-up requests can read from that cache instead of reprocessing the same content. By default, the cache lives for 5 minutes, so this feature is only useful if you're repeatedly sending the same content within that timeframe. If you need longer, a 1-hour cache duration is also available at a higher cache-write price.

## Cache Breakpoints

Caching isn't enabled automatically - you need to manually add cache breakpoints to specific blocks in your messages. Here's how it works:

* Work done on messages is **not cached automatically**
* You must manually add a 'cache breakpoint' to a block
* Work done for everything **before** the breakpoint will be cached
* Cache will only be used on follow-up requests if the content up to and including the breakpoint is identical

![](https://academy.claude.com/assets/media/2779a78a7771a84318b4f9c0eccb40a8caf7e63ff9784cd61a439a54c5fd6f19.jpg)

To add a cache breakpoint, you need to use the longhand form for writing text blocks instead of the shorthand:

![](https://academy.claude.com/assets/media/97c071649fbc50222c537c4b2d0124d2f9f1e1ab86877001cbab0e7b73eeb2cb.jpg)

The shorthand form doesn't provide a place to add the cache control field, so you must use the expanded format with the `cache_control` field set to `{"type": "ephemeral"}`.

## How Cache Breakpoints Work

When you place a cache breakpoint in a message, Claude caches all the processing work up to and including that breakpoint. Content after the breakpoint is processed normally without caching.

![](https://academy.claude.com/assets/media/9d5e67fff198809f45cd5ffef1514639de7a3c14fa37f917d599e7560c8838e3.jpg)

For the cache to be useful in follow-up requests, the content must be identical up to the breakpoint. Even small changes like adding the word "please" will invalidate the cache and force Claude to reprocess everything.

![](https://academy.claude.com/assets/media/bfeefd9e40743a7d88cacfde361f1042185b2699c3f6d66fa75887d9a7ef1aff.jpg)

## Cross-Message Caching

Cache breakpoints can span across multiple messages and message types. If you place a breakpoint in a later message, all previous messages (user, assistant, etc.) will be included in the cached content.

![](https://academy.claude.com/assets/media/a93fd8ec510e4c23603eda04dac8c56ff87d74e1e6c31d379bbd4c6b60e0ed2d.jpg)

This is particularly useful for conversations where you want to cache the entire context up to a certain point.

## System Prompts and Tools

You're not limited to text blocks - cache breakpoints can be added to:

* System prompts
* Tool definitions
* Image blocks
* Tool use and tool result blocks

![](https://academy.claude.com/assets/media/cd81704d36d86dcbfd2d346b4bf71fb3766760c36f39d5bc31e7aad50e27effa.jpg)

System prompts and tool definitions are excellent candidates for caching since they rarely change between requests. This is often where you'll get the most benefit from prompt caching.

## Cache Ordering

Behind the scenes, Claude processes your request components in a specific order: tools first, then system prompt, then messages. Understanding this order helps you place breakpoints effectively.

![](https://academy.claude.com/assets/media/28440d7825fc506d017c5d37035b95eae9cf58b3e9f9c5817c235ea77f275c0c.jpg)

You can add up to four cache breakpoints total. For example, you might cache your tools, then add another breakpoint partway through your conversation history. This gives you flexibility in what gets cached when different parts of your request change.

![](https://academy.claude.com/assets/media/800aa4c461a1938ee496487f3c291e6d196e6a13251c6b1fac261aa34ce3b8e6.jpg)

## Minimum Content Length

There's a minimum threshold for caching: content must be at least 1024 tokens long to be cached. This is the sum of all messages and blocks you're trying to cache, not individual blocks.

![](https://academy.claude.com/assets/media/b76bb4d709ad0dd84747578292abb55f440e249148d9702363eae445d8fab796.jpg)

A simple "Hi there!" message won't meet this threshold, but if you duplicate that content 500 times (or have a genuinely long prompt), it will exceed 1024 tokens and be eligible for caching.

The key to effective prompt caching is identifying which parts of your requests stay consistent across multiple calls and placing breakpoints strategically to maximize reuse while minimizing cache invalidation.
