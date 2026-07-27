<!-- source: https://claude.com/blog/web-search-api -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

# Introducing web search on the Anthropic API

Claude can now search the web through the API, giving users access to real-time information with citations for building up-to-date AI applications.

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

* Date

  May 7, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/web-search-api

***Update:****You can now add the web fetch tool to your requests and Claude will fetch and analyze content from any webpage URL. September 10, 2025*

Today, we're introducing web search on the Anthropic API—a new tool that gives Claude access to current information from across the web. With web search enabled, developers can build Claude-powered applications and agents that deliver up-to-date insights.

### Power AI agents with the latest information from the web

Developers can now augment Claude’s comprehensive knowledge with current, real-world data by enabling the web search tool when making requests to the Messages API.

When Claude receives a request that would benefit from up-to-date information or specialized knowledge, it uses its reasoning capabilities to determine whether the web search tool would help provide a more accurate response. If searching the web would be beneficial, Claude generates a targeted search query, retrieves relevant results, analyzes them for key information, and provides a comprehensive answer with citations back to the source material.

Claude can also operate agentically and conduct multiple progressive searches, using earlier results to inform subsequent queries in order to do light research and generate a more comprehensive answer. Developers can control this by adjusting the *max\_uses* parameter*.* Behind the scenes, Claude may also refine its queries to deliver a more accurate response.

With web search, developers can now build AI solutions that tap into current information without needing to manage their own web search infrastructure.

### Use cases

Web search enables Claude to power a wide range of use cases that benefit from real-time data and specialized knowledge across various industries. Use cases include:

* **Financial services:** Build AI agents that analyze real-time stock prices, market trends, and regulatory updates.
* **Legal research:** Create tools that access recent court decisions, regulatory changes, and legal news.
* **Developer tools:** Enable Claude to reference the latest API documentation, GitHub releases, and technology updates.
* **Productivity:** Build agents that incorporate the latest company reports, competitive intelligence, or industry research.

### Build with trust and control

Every web-sourced response includes citations to source materials, enabling users to verify information directly. This is particularly valuable for sensitive use cases that require accuracy and accountability.

![A screenshot of the UX showing blocked domains.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d93039df37d2c2df52e_b57f878e8735a67a64c1463c8248f0f4b0797952-3840x2160.png)

Organizations can maintain additional control through the following admin settings:

* **Domain allow lists**: Specify which domains Claude can search and retrieve information from, ensuring that results only come from approved sources.
* **Domain block lists**: Prevent Claude from accessing certain domains that may contain sensitive, competitive, or inappropriate content for your organization.
* **Organization-level management**: Administrators can allow or prohibit web search use at the organization level.

### Enhance Claude Code with web search

Web search is also now available in Claude Code, adding the latest information from the web to development workflows.

With web search enabled, Claude Code can access current API documentation, technical articles, and other information on development tools and libraries. This is particularly valuable when working with new or rapidly evolving frameworks, troubleshooting obscure errors, or implementing features that require version-specific API references.

### Customer Spotlight: Poe

Quora is bringing web search to its AI platform, Poe.

“Anthropic's web search tool is a welcome addition to the Poe platform. It is cost effective and delivers search results with impressive speed, which will benefit people who need access to real-time information while using Claude models on Poe,” said Spencer Chan, Head of Poe Product, Quora.

### Customer Spotlight: Adaptive.ai

Adaptive is an AI tool for consumers to create end-to-end apps.

“Anthropic’s web search delivers consistently thorough results that have outperformed other tools we’ve tested. The depth and accuracy of Claude’s responses and its ability to function as a research agent will make a significant difference in how effectively we enable our customers to build web-enabled products,” said Dennis Xu, Co-founder, Adaptive.

### Getting started

Web search is now available on the Anthropic API for Claude 3.7 Sonnet, the upgraded Claude 3.5 Sonnet, and Claude 3.5 Haiku at $10 per 1,000 searches plus standard token costs.

To get started, enable the web search tool in your API requests. Explore our [documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/web-search-tool) and [pricing](https://www.anthropic.com/pricing#api) to learn more.

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d231b45c2193efbb0f02_1869137c9d7f2a38b50e804d707e10e85de05ddb-1000x1000.svg)

Jul 23, 2026

### Think through hard problems in voice mode

Product announcements

[Think through hard problems in voice mode](#)Think through hard problems in voice mode

[Think through hard problems in voice mode](https://claude.com/blog/think-through-hard-problems-in-voice-mode)Think through hard problems in voice mode

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

May 12, 2026

### Claude for the legal industry

Product announcements

[Claude for the legal industry](#)Claude for the legal industry

[Claude for the legal industry](https://claude.com/blog/claude-for-the-legal-industry)Claude for the legal industry

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3f14a08cb97bf1b16d40ef_ObjectClouds.svg)

Jul 7, 2026

### Claude Cowork is coming to mobile and web

Product announcements

[Claude Cowork is coming to mobile and web](#)Claude Cowork is coming to mobile and web

[Claude Cowork is coming to mobile and web](https://claude.com/blog/cowork-web-mobile)Claude Cowork is coming to mobile and web

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

Apr 9, 2026

### Making Claude Cowork ready for enterprise

Product announcements

[Making Claude Cowork ready for enterprise](#)Making Claude Cowork ready for enterprise

[Making Claude Cowork ready for enterprise](https://claude.com/blog/cowork-for-enterprise)Making Claude Cowork ready for enterprise

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Coding
