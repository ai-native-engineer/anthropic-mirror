<!-- source: https://claude.com/blog/prompt-caching -->

Explore here

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22606367ec36d6a7179_6380b3c2dc9e4011a3cd96fec382bd9197511e31-1000x1000.svg)

# Prompt caching with Claude

Claude caches frequently used context between API calls, reducing costs and latency for long prompts.

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Platform](https://claude.com/platform/api)
* Date

  August 14, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/prompt-caching

***Update****: Prompt caching is Generally Available on the Anthropic API. Prompt caching is also available in preview in Amazon Bedrock and on Google Cloud’s Vertex AI. (December 17, 2024)*Prompt caching, which enables developers to cache frequently used context between API calls, is now available on the Anthropic API. With prompt caching, customers can provide Claude with more background knowledge and example outputs—all while reducing costs by up to 90% and latency by up to 85% for long prompts. Prompt caching is available today in public beta for Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku.

## When to use prompt caching

Prompt caching can be effective in situations where you want to send a large amount of prompt context once and then refer to that information repeatedly in subsequent requests, including:

* **Conversational agents:** Reduce cost and latency for extended conversations, especially those with long instructions or uploaded documents.
* **Coding assistants:** Improve autocomplete and codebase Q&A by keeping a summarized version of the codebase in the prompt.
* **Large document processing:** Incorporate complete long-form material including images in your prompt without increasing response latency.
* **Detailed instruction sets:** Share extensive lists of instructions, procedures, and examples to fine-tune Claude's responses. Developers often include a few examples in their prompt, but with prompt caching you can get even better performance by including dozens of diverse examples of high quality outputs.
* **Agentic search and tool use:** Enhance performance for scenarios involving multiple rounds of tool calls and iterative changes, where each step typically requires a new API call.
* **Talk to books, papers, documentation, podcast transcripts, and other long-form content:** Bring any knowledge base alive by embedding the entire document(s) into the prompt, and letting users ask it questions.

Early customers have seen substantial speed and cost improvements with prompt caching for a variety of use cases—from including a full knowledge base to 100-shot examples to including each turn of a conversation in their prompt.

| **Use case** | **Latency w/o caching (time to first token)** | **Latency w/ caching (time to first token)** | **Cost reduction** |
| --- | --- | --- | --- |
| Chat with a book (100,000 token cached prompt) [1] | 11.5s | 2.4s (-79%) | -90% |
| Many-shot prompting (10,000 token prompt) [1] | 1.6s | 1.1s (-31%) | -86% |
| Multi-turn conversation (10-turn convo with a long system prompt) [2] | ~10s | ~2.5s (-75%) | -53% |

Prompt caching

### How we price cached prompts

Cached prompts are priced based on the number of input tokens you cache and how frequently you use that content. Writing to the cache costs 25% more than our base input token price for any given model, while using cached content is significantly cheaper, costing only 10% of the base input token price.

|  |  |  |  |
| --- | --- | --- | --- |
| **Claude 3.5 Sonnet**  * Our most intelligent model to date * 200K context window | **Input**  * $3 / MTok | **Prompt caching**  * $3.75 / MTok -   Cache write * $0.30 / MTok - Cache read | **Output**   * $15 / MTok |
| **Claude 3 Opus**  * Powerful model for complex tasks * 200K context window | **Input**  * $15 / MTok | **Prompt caching**  * $18.75 / MTok -   Cache write * $1.50 / MTok - Cache read | **Output**  * $75 / MTok |
| **Claude 3 Haiku**  * Fastest, most cost-effective model * 200K context window | **Input**  * $0.25 / MTok | **Prompt caching**  * $0.30 / MTok   -   Cache write * $0.03 / MTok - Cache read | **Output**  * $1.25 / MTok |

Pricing

### Customer spotlight: Notion

[Notion](https://www.notion.so/product/ai) is adding prompt caching to Claude-powered features for its AI assistant, Notion AI. With reduced costs and increased speed, Notion is able to optimize internal operations and create a more elevated and responsive user experience for their customers.

> We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality.

— Simon Last, Co-founder at Notion

### Get started

To start using the prompt caching public beta on the Anthropic API, explore our [documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) and [pricing page](https://www.anthropic.com/pricing#anthropic-api).

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

Sep 25, 2026

### Build plugins for Claude

Product announcements

[Build plugins for Claude](#)Build plugins for Claude

[Build plugins for Claude](https://claude.com/blog/build-plugins-for-claude)Build plugins for Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22deea97e4a5b5e5739_8d339ae8ecedecc1409db8f5bbb99c958db56946-1000x1000.svg)

Sep 24, 2026

### Claude Tag now supports personal connectors in channels

Product announcements

[Claude Tag now supports personal connectors in channels](#)Claude Tag now supports personal connectors in channels

[Claude Tag now supports personal connectors in channels](https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels)Claude Tag now supports personal connectors in channels

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

Sep 23, 2026

### Claude Marketplace: one place to discover plugins, agents, and services from our partners

Product announcements

[Claude Marketplace: one place to discover plugins, agents, and services from our partners](#)Claude Marketplace: one place to discover plugins, agents, and services from our partners

[Claude Marketplace: one place to discover plugins, agents, and services from our partners](https://claude.com/blog/claude-marketplace)Claude Marketplace: one place to discover plugins, agents, and services from our partners

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

Oct 20, 2025

### Claude Code on the web

Product announcements

[Claude Code on the web](#)Claude Code on the web

[Claude Code on the web](https://claude.com/blog/claude-code-on-the-web)Claude Code on the web

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Platform

Coding
