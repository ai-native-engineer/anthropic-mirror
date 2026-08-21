<!-- source: https://claude.com/blog/introducing-citations-api -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22f70ecef3c9356822a_928166e443bc1b1f19ebadf4fd11b7c45fce4153-1000x1000.svg)

# Introducing Citations on the Anthropic API

Claude can now cite specific passages from your documents, delivering verifiable responses with built-in source tracking.

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude apps
* Date

  June 23, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/introducing-citations-api

***Update:****Now available in Amazon Bedrock. (June 30, 2025)*

Today, we're launching Citations, a new API feature that lets Claude ground its answers in source documents. Claude can now provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs.

Citations is generally available on the Anthropic API and Google Cloud’s Vertex AI.

### Trust by verification

All Claude models are trained to be trustworthy and steerable by design. Citations builds upon this foundation, addressing a specific need in AI applications: verifying the sources behind AI-generated responses.

Previously, developers relied on complex prompts that instruct Claude to include source information, often resulting in inconsistent performance and significant time investment in prompt engineering and testing. With Citations, users can now add source documents to the context window, and when querying the model, Claude automatically cites claims in its output that are inferred from those sources.

**Our internal evaluations show that Claude's built-in citation capabilities outperform most custom implementations, increasing recall accuracy by up to 15%.1**

### Use cases

With Citations, developers can create AI solutions that offer enhanced accountability across use cases like:

* Document summarization: Generate concise summaries of long documents, like case files, with each key point linked back to its original source.
* Complex Q&A: Provide detailed answers to user queries across a large corpus of documents, like financial statements, with each response element traced back to specific sections of relevant texts.
* Customer support: Create support systems that can answer complex queries by referencing multiple product manuals, FAQs, and support tickets, always citing the exact source of information.

### How it works

When Citations is enabled, the API processes user-provided source documents (PDF documents and plain text files) by chunking them into sentences. These chunked sentences, along with user-provided context, are then passed to the model with the user's query. Alternatively, users can provide their own chunks for the source documents.

Claude analyzes the query and generates a response that includes precise citations based on the provided chunks and context for any claims derived from the source material. Cited text will reference source documents to minimize hallucinations.

This approach offers superior flexibility and ease of use, as it doesn't require file storage and seamlessly integrates with the Messages API.

### Pricing

Citations uses our standard token-based pricing model. While it may use additional input tokens to process documents, users will not pay for output tokens that return the quoted text itself.

### Customer spotlight: Thomson Reuters

Thomson Reuters uses Claude to power their AI platform, CoCounsel, helping legal and tax professionals synthesize expert knowledge and deliver comprehensive advice to clients.

“For CoCounsel to be trustworthy and immediately useful for practicing attorneys, it needs to cite its work. We first built this ourselves, but it was really hard to build and maintain. That's why we were excited to test out Anthropic’s Citations functionality. It makes citing and linking to primary sources much easier to build, maintain, and deploy to our users. This capability not only helps minimize hallucination risk but also strengthens trust in AI-generated content. The Citations feature will enable us to build an even more accurate and thorough AI assistant for lawyers,” said Jake Heller, Head of Product, CoCounsel, Thomson Reuters.

### Customer Spotlight: Endex

Endex uses Claude to power an Autonomous Agent for financial firms.

"With Anthropic's Citations, we reduced source hallucinations and formatting issues from 10% to 0% and saw a 20% increase in references per response. This removed the need for elaborate prompt engineering around references and improved our accuracy when conducting complex, multi-stage financial research,” said Tarun Amasa, CEO, Endex.

### Get started

Citations is now available for the new Claude 3.5 Sonnet and Claude 3.5 Haiku. To start using Citations, explore our [documentation](https://docs.anthropic.com/en/docs/build-with-claude/citations).

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

Aug 20, 2026

### Build production agents with computer use, the Skills API, and the Files API

Product announcements

[Build production agents with computer use, the Skills API, and the Files API](#)Build production agents with computer use, the Skills API, and the Files API

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api)Build production agents with computer use, the Skills API, and the Files API

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

Aug 20, 2026

### Anthropic’s approach to teaching and learning AI

Product announcements

[Anthropic’s approach to teaching and learning AI](#)Anthropic’s approach to teaching and learning AI

[Anthropic’s approach to teaching and learning AI](https://claude.com/blog/anthropics-approach-to-teaching-and-learning-ai)Anthropic’s approach to teaching and learning AI

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

May 19, 2026

### New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

Product announcements

[New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](#)New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

[New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](https://claude.com/blog/claude-managed-agents-updates)New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2260bfc90348429f9c3_cd9cf56a7f049285b7c1c8786c0a600cf3d7f317-1000x1000.svg)

Aug 13, 2026

### Claude Tag now reads even more of the room

Product announcements

[Claude Tag now reads even more of the room](#)Claude Tag now reads even more of the room

[Claude Tag now reads even more of the room](https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room)Claude Tag now reads even more of the room

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude apps

Learning

Productivity
