<!-- source: https://claude.com/blog/improved-web-search-with-dynamic-filtering -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

# Increase web search accuracy and efficiency with dynamic filtering

*Dynamic filtering makes Claude more accurate and efficient on complex web search tasks. Here’s how it works, and how to enable it on the API.*

  [Product announcements](https://claude.com/blog/category/announcements)

  [Claude Platform](https://claude.com/platform/api)

  February 17, 2026

  https://claude.com/blog/improved-web-search-with-dynamic-filtering

Alongside Claude [Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6) and [Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6), we’re releasing new versions of our [web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) and [web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool) tools. Claude can now natively write and execute code during web searches to filter results before they reach the context window, improving its accuracy and token efficiency.

## **Web search with dynamic filtering**

Web search is a highly token-intensive task. Agents using basic web search tools need to make a query, pull search results into context, fetch full HTML files from multiple websites, and reason over it all before responding. But the context being pulled in from search is often irrelevant, which degrades the quality of the response.

To improve Claude’s performance on web searches, our web search and web fetch tools now automatically write and execute code to post-process query results. Instead of reasoning over full HTML files, Claude can dynamically filter the search results before loading them into context, keeping only what’s relevant and discarding the rest.

We’ve [previously found](https://www.anthropic.com/engineering/advanced-tool-use) this technique to be effective across other agentic workflows, and we’ve added tools such as [code execution](http://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool) and [programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) for native support on our API. We’re now bringing these same techniques to web search and web fetch.

## **Evaluating Claude’s ability to search the web**‍

We evaluated web search on Sonnet 4.6 and Opus 4.6 with and without dynamic filtering and no other tools enabled. Across two benchmarks, [BrowseComp](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf) and [DeepsearchQA](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf), dynamic filtering improved performance by an average of 11% while using 24% fewer input tokens.

**BrowseComp: Searching the web to find one answer**‍

BrowseComp tests whether an agent can navigate many websites to find a specific piece of information that is deliberately hard to find online. Dynamic filtering improved Claude’s accuracy significantly, bringing Sonnet 4.6 from 33.3% to 46.6% and Opus 4.6 from 45.3% to 61.6%.
‍

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69937fbbb7eec8e454d86c9d_Dynamic-filtering-on-browsecomp.png)

**DeepsearchQA: Searching the web to find many answers**‍

DeepsearchQA presents agents with research queries that have many correct answers, all of which must be found via web search. It tests whether an agent can systematically plan and execute multi-step searches without missing any answers. It’s measured by an “F1 score,” which balances precision and recall—capturing both the accuracy of returned answers and the completeness of the search.

Dynamic filtering improved Claude’s F1 score from 52.6% to 59.4% for Sonnet 4.6 and from 69.8% to 77.3% for Opus 4.6.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69937fcede000ba1d5aab33d_Dynamic-filtering-on-DeepsearchQA.png)

Token costs will vary depending on how much code the model needs to write to filter context. Price-weighted tokens decreased for Sonnet 4.6 on both benchmarks but increased for Opus 4.6. To better understand your own costs, we recommend evaluating this tool against a representative set of web search queries your agent is likely to encounter in production.

## Customer spotlight: Quora

[Poe](https://poe.com) by [Quora](https://quora.com) is one of the largest multi-model AI platforms, giving millions of users access to over 200 models through a single interface. Internal teams at Quora found that Opus 4.6 with dynamic filtering “achieved the highest accuracy on our internal evals when tested against other frontier models,” said Gareth Jones, Product and Research Lead. “The model behaves like an actual researcher, writing Python to parse, filter, and cross-reference results rather than reasoning over raw HTML in context.*”*

## Dynamic filtering in the web search and fetch tools

Dynamic filtering will be turned on by default when using our new web search and web fetch tools with Sonnet 4.6and Opus 4.6 on the Claude API. For complex web search queries, such as sifting through technical documentation or verifying citations, you can expect similar performance improvements to those shown above.

Here’s how to use it in the API:

```
{
  "model": "claude-opus-4-6",
  "max_tokens": 4096,
  "tools": [
    {
      "type": "web_search_20260209",
      "name": "web_search"
    },
    {
      "type": "web_fetch_20260209",
      "name": "web_fetch"
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio."
    }
  ]
}
```

## Code execution, memory, and more tools are now generally available

We’re also graduating several tools to general availability to help agents perform better across token-intensive tasks:

* [Code execution](http://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool)**:** Provides a sandbox for agents to run code during a conversation to filter context, analyze data, or perform calculations.
* [Memory](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool): Store and retrieve information across conversations through a persistent file directory, so agents can retain context without keeping everything in the context window.
* [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)**:** Execute complex multi-tool workflows in code, keeping intermediate results out of the context window.
* [Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool):Dynamically discover tools from large libraries without loading all definitions into the context window.[‍](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#providing-tool-use-examples)
* [Tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#providing-tool-use-examples)**:** Provide sample tool calls directly in your tool definitions to demonstrate usage patterns and reduce parameter errors.

### **Getting started**

Improved web search and web fetch—as well as code execution, memory, programmatic tool calling, tool search, and tool use examples—are available now on the Claude Platform. Read our [API documentation](https://platform.claude.com/docs/en/build-with-claude/overview) to get started.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22753311132c8c37b39_d3dd09ad16c68461dc3fb01df5e84cf7ccafda6c-1000x1000.svg)

Aug 5, 2026

### Inference hooks: inline data loss prevention for Claude Enterprise

[Inference hooks: inline data loss prevention for Claude Enterprise](#)Inference hooks: inline data loss prevention for Claude Enterprise

[Inference hooks: inline data loss prevention for Claude Enterprise](https://claude.com/blog/claude-enterprise-inference-hooks)Inference hooks: inline data loss prevention for Claude Enterprise

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22651dd05046d0fdb0b_39c40393e610cc0a5e65f50ad12ff5ada273f792-1000x1000.svg)

### Run Claude Code sessions on your own compute

Product announcements

[Run Claude Code sessions on your own compute](#)Run Claude Code sessions on your own compute

[Run Claude Code sessions on your own compute](https://claude.com/blog/run-claude-code-sessions-on-your-own-compute)Run Claude Code sessions on your own compute

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

Jul 28, 2026

### Bringing MCP 2026-07-28 to Claude

Product announcements

[Bringing MCP 2026-07-28 to Claude](#)Bringing MCP 2026-07-28 to Claude

[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)Bringing MCP 2026-07-28 to Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

Jul 2, 2026

### Giving admins more visibility and control over Claude spend

Product announcements

[Giving admins more visibility and control over Claude spend](#)Giving admins more visibility and control over Claude spend

[Giving admins more visibility and control over Claude spend](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)Giving admins more visibility and control over Claude spend

Claude Platform

Agents
