<!-- source: https://claude.com/resources/articles/claude-for-commerce-agents -->

Many of the world’s largest retailers, marketplaces, e-commerce platforms, and travel companies use Claude to build agents that make shopping easier. Enterprise customers like Shopify, Priceline, and others have agents that let consumers use AI to search for what they want in plain language, find it, compare it, and buy it.

Today, we're launching a blueprint to help build commerce agents on Claude. It contains the harnesses, patterns, and guardrails an engineering team needs to get a commerce agent running in days, with reference implementations of a shopping agent and a merchant agent for retail, travel, telecom, and ticketing platforms. It also includes a Claude Code plugin to get you started.

The code deploys where you already build with Claude, including the Claude API, Amazon Bedrock, Microsoft Foundry, or Google Cloud Vertex AI. You can also work with our solutions and ecosystem partners such as Accenture, Mastercard, and Visa, who are working with us to enable clients and merchant communities to leverage the blueprints.

It’s [available today](https://github.com/anthropics/commerce-agents), with [live demos](https://claude.com/solutions/commerce) for each vertical and an [engineering deep-dive](https://claude.com/resources/articles/the-anatomy-of-effective-commerce-agents) on how it was built, just in time for holiday season planning.

![](https://assets.claude.com/b9ec1abf25aff70e3ad5f91895c78ad550cf92e3.jpg)

The shopping agent running in the ACME retail example.

## What's in the blueprint

The repository contains complete, working implementations of a shopping agent and merchant agent that can be built using the [Messages API](https://platform.claude.com/docs/en/intro), [Agent SDK](https://code.claude.com/docs/en/agent-sdk), or [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) (beta). You can see them running in a self-guided demo before writing any code, and then work with Claude Code to customize them to your catalogs, policies, brand, and more.

### The shopping agent

The shopping agent lives inside your app or website. The blueprint includes the integration points for catalog, cart, checkout, customer preferences, and order history, and leaves payment to you, whether that is your existing checkout or an agentic payments provider.

A customer can say “I need a tent, sleeping bag, and stove for a weekend trip with two kids,” and the agent can take it from there. Here’s what it can do:

* Search the catalog and assemble the right set of items, including multi-item requests.
* Remember the customer's preferences and tailor what it suggests.
* Show products, comparisons, and the cart right in the conversation, not just as text.
* Build the cart and hand it to checkout.
* Answer customer service questions in the same conversation, like where an order is, how to return or exchange an item, and what the refund policy says, instead of sending the customer to a support page.

The agent features guardrails designed to constrain prices and products to actual catalog data, and avoids manipulative upsell patterns. In the repository, these are skills and tools for catalog search, multi-item planning, deep research, personalization, customer care, and in-conversation UI.

### The merchant agent

The merchant agent supports the people running the store. A user can ask “what should we discount to clear last season’s inventory?” and get an answer based on their own data. Here’s what it can do:

* Answer questions about sales performance like what's selling and what isn't.
* Track inventory and proactively flag problems, like an item about to sell out before a promotion starts.
* Recommend pricing and promotions based on the store's own sales history.
* Draft marketing campaigns to move the products that need moving.

When the agent proactively suggests a change, a person approves it before anything goes live, meaning users get the final say while their agent watches the store. In the repository, these capabilities ship as skills for sales analytics, catalog and inventory management, marketing and promotions, and in-portal UI such as charts and dashboards.

![](https://assets.claude.com/045755d6e355214e83ca27b6378b2fb4dde6d3cf.png)

## Trusted across the industry

Companies that serve shoppers, travelers, subscribers, and merchants build and run agents on Claude. Here's what they have to say about building commerce agents with Claude:

![Zomato](https://assets.claude.com/7b06fdb76b1b2e350bd19549c430d46d8a147631.svg)

> “Our engineers had the blueprint running with no blockers; the setup worked exactly as documented. The practices it bakes in, from tool iteration limits to prompt caching, are the ones we recognized from building Zomato's own agent. Teams standing up their first agent on Claude will skip weeks of trial and error.”

Akhil Bansal, Senior Engineering Manager

![Fetch](https://assets.claude.com/baf2ceeaaabf6636e392fb03b3796544fa67966a.svg)

> “Our engineers had both commerce agents from Anthropic's blueprint running locally in well under an hour, with live conversations working on the first attempt. We ran the Claude Code workflow twice and got two different architectures back, each designed to what we'd asked for. For a team starting from scratch, that turns days of agent scaffolding into hours.”

Ashley Nader, Staff Product Manager

![Square](https://assets.claude.com/8054b096faa0b59ca686be2f59ac108fa0a98638.svg)

> “Much of what we build at Square is about giving sellers time back, and agents are a big leap in our ability to do that. We're building agentic tools that watch sales, labor, and inventory and come back with real next steps, not just an answer, while keeping sellers in control. Trust is the hardest part of that work, and Claude helps us meet a high standard.””

Willem Avé, Head of Product

![Visa](https://assets.claude.com/0e2431b0f4c10fb7cdaa4c5a08d3048cf0320583.svg)

> “AI will fundamentally reshape commerce, but trust must remain at the center of every transaction. Merchants are telling us they want more control over how AI engages their customers. Our collaboration with Anthropic on their commerce blueprint helps bring together the intelligence of Claude with the trust, security, and global reach of the Visa network, empowering merchants to deliver better customer experiences while maintaining the relationships that drive their businesses forward.”

Jack Forestell, Chief Product and Strategy Officer

![Mastercard](https://assets.claude.com/fe3fc522db9dc6e27e569e2275c67babeb168ff9.svg)

> “Trust is the currency of commerce, and it is even more critical in the agentic era. With Anthropic's commerce blueprint, we're helping merchants build their own agents with Claude to drive their growth. By combining AI innovation with trusted payments and commerce infrastructure, we're helping connect consumers, merchants and AI agents securely, seamlessly and at scale.”

Sherri Haymond, Executive Vice President, Global Head of Digital Commercialization

![Accenture](https://assets.claude.com/eef8a51d4b99d31d65fa28d41f247f85bc363b45.svg)

> “Commerce agents are quickly becoming a critical capability for organizations seeking to deliver the personalized, intelligent customer experiences that today’s consumers expect. Our latest research revealed that 85% are now open to collaboration with an AI agent and nearly three in four would trust a personal AI agent more than their best friend to make a purchase on their behalf. This is more than a shift in how people shop. Agentic commerce is rewriting the rules of brand value – fundamentally shaping what gets purchased, when, where and by whom. Anthropic’s commerce agent blueprint provides a proven starting point that can help organizations accelerate deployment and build differentiated experiences that increase customer satisfaction, loyalty, and growth. Combined with Accenture's deep retail and consumer goods expertise, we can help clients move from concept to production and realize value from agentic AI faster.”

Kath Gramling, Global Consumer Goods, Retail and Travel lead

![Priceline](https://assets.claude.com/8ddfae0a9bf7f1b17537d760f26449eac334f4cc.svg)

> “A trip is one of the most complex things a person buys: flights, hotels, cars, and dozens of options to weigh against each other. Penny, our AI assistant, navigates all of that in one conversation and surfaces the best options and best value. We built the latest generation of Penny on Claude because that kind of reasoning is exactly what Claude models are good at.”

Cobus Kok, Vice President, AI Experiences

![Intuit](https://assets.claude.com/b730fa6588d08aef3d1c1e12fbe768211c465c24.svg)

> “Millions of consumers, businesses and accountants run their finances on Intuit. Working with partners like Anthropic, we're building highly personalized experiences that provide customers with a clear understanding of what's shifting in their business and why, so they can take action with complete confidence. We are creating a financial system of intelligence by combining frontier AI reasoning, including Claude, with our proprietary data, capabilities, intelligence, and human expertise that powers the next level of prosperity for our customers.”

Chris Kasten, Intuit’s Chief Architect and SVP of Engineering, Platform and Development Xceleration Group

![Shopify](https://assets.claude.com/33de1bc0b1b2c92e879e513e3c14ec213c311ff1.svg)

> “We want our merchants to be everywhere customers are shopping, and increasingly that means a conversation with an agent. We're building on Anthropic's blueprints with a reference storefront implementation that connects them to a merchant's store through Catalog, UCP and Shop Sign-in. Merchants can use Claude to build agents that help customers find products, check out, and answer questions about their orders.”

Vanessa Lee, VP Product

![Klaviyo](https://assets.claude.com/6187fcdd66b66e7fc77047e18645f766fb5e2182.svg)

> “Commerce and stunning customer experiences require personalization, and every brand on Klaviyo sits on more customer data and decisions than any team could act on by hand. Claude closes that gap, turning consumer preferences and performance data into the insights, campaigns and personalization that drive revenue. That's why we keep building with Anthropic: agents do complex analysis, design and decision making, and businesses can focus on delighting customers.”

Andrew Bialecki, Founder and Co-CEO

![Wix](https://assets.claude.com/31f3d282988b62d2920e9374b2e0571f60d5c3f9.svg)

> “Wix’s mission has always been to make complex technology simple and accessible for our users. For merchants, that means providing powerful commerce capabilities without adding operational complexity, and agents are a natural next step. Our engineers had a working commerce agent taking prompts within fifteen minutes, and the pilot showed the potential of combining Anthropic’s AI capabilities with Wix’s commerce platform and deep expertise in commerce for SMB.”

Dror Zalika, Head of Commerce at Wix

![Zomato](https://assets.claude.com/7b06fdb76b1b2e350bd19549c430d46d8a147631.svg)

> “Our engineers had the blueprint running with no blockers; the setup worked exactly as documented. The practices it bakes in, from tool iteration limits to prompt caching, are the ones we recognized from building Zomato's own agent. Teams standing up their first agent on Claude will skip weeks of trial and error.”

Akhil Bansal, Senior Engineering Manager

![Fetch](https://assets.claude.com/baf2ceeaaabf6636e392fb03b3796544fa67966a.svg)

> “Our engineers had both commerce agents from Anthropic's blueprint running locally in well under an hour, with live conversations working on the first attempt. We ran the Claude Code workflow twice and got two different architectures back, each designed to what we'd asked for. For a team starting from scratch, that turns days of agent scaffolding into hours.”

Ashley Nader, Staff Product Manager

![Square](https://assets.claude.com/8054b096faa0b59ca686be2f59ac108fa0a98638.svg)

> “Much of what we build at Square is about giving sellers time back, and agents are a big leap in our ability to do that. We're building agentic tools that watch sales, labor, and inventory and come back with real next steps, not just an answer, while keeping sellers in control. Trust is the hardest part of that work, and Claude helps us meet a high standard.””

Willem Avé, Head of Product

![Visa](https://assets.claude.com/0e2431b0f4c10fb7cdaa4c5a08d3048cf0320583.svg)

> “AI will fundamentally reshape commerce, but trust must remain at the center of every transaction. Merchants are telling us they want more control over how AI engages their customers. Our collaboration with Anthropic on their commerce blueprint helps bring together the intelligence of Claude with the trust, security, and global reach of the Visa network, empowering merchants to deliver better customer experiences while maintaining the relationships that drive their businesses forward.”

Jack Forestell, Chief Product and Strategy Officer

![Mastercard](https://assets.claude.com/fe3fc522db9dc6e27e569e2275c67babeb168ff9.svg)

> “Trust is the currency of commerce, and it is even more critical in the agentic era. With Anthropic's commerce blueprint, we're helping merchants build their own agents with Claude to drive their growth. By combining AI innovation with trusted payments and commerce infrastructure, we're helping connect consumers, merchants and AI agents securely, seamlessly and at scale.”

Sherri Haymond, Executive Vice President, Global Head of Digital Commercialization

![Accenture](https://assets.claude.com/eef8a51d4b99d31d65fa28d41f247f85bc363b45.svg)

> “Commerce agents are quickly becoming a critical capability for organizations seeking to deliver the personalized, intelligent customer experiences that today’s consumers expect. Our latest research revealed that 85% are now open to collaboration with an AI agent and nearly three in four would trust a personal AI agent more than their best friend to make a purchase on their behalf. This is more than a shift in how people shop. Agentic commerce is rewriting the rules of brand value – fundamentally shaping what gets purchased, when, where and by whom. Anthropic’s commerce agent blueprint provides a proven starting point that can help organizations accelerate deployment and build differentiated experiences that increase customer satisfaction, loyalty, and growth. Combined with Accenture's deep retail and consumer goods expertise, we can help clients move from concept to production and realize value from agentic AI faster.”

Kath Gramling, Global Consumer Goods, Retail and Travel lead

1/11

## Getting started

The blueprint is available today. [Contact our sales team](https://claude.com/contact-sales) to learn more, schedule a demonstration, or discuss how to implement for your organization.

1. Fork the repository at [github.com/anthropics/commerce-agents](https://github.com/anthropics/commerce-agents).
2. Read the engineering deep-dive at [claude.com/blog/the-anatomy-of-effective-commerce-agents.](https://claude.com/resources/articles/the-anatomy-of-effective-commerce-agents)
3. See the vertical demos and request a working session at [claude.com/solutions/commerce](https://claude.com/solutions/commerce).

Register for our [webinar](https://claude.com/resources/webinars/building-claude-commerce-agents) to see the deep dive where we'll share live walkthroughs, demos, and cover how commerce builders can get the most out of Claude.

[ArticleOct 1, 2026

### Customize Claude Code with mods

Change how Claude Code behaves and looks with a few lines of TypeScript.

Claude Code](https://claude.com/resources/articles/claude-code-mods)[ArticleSep 30, 2026

### Claude for Government is now generally available

Claude Code CLI and Claude for Microsoft 365 also now available in early access.](https://claude.com/resources/articles/claude-for-government-is-now-generally-available)[ArticleSep 25, 2026

### Build plugins for Claude

You can now submit plugins to the Claude directory through a new developer portal, track them through review, and see usage analytics once they’re live.

Claude apps](https://claude.com/resources/articles/build-plugins-for-claude)[ArticleSep 24, 2026

### Claude Tag now supports personal connectors in channels

Claude Tag can now use your connectors for requests you make in a channel. Nobody else can use them, and you're in control of how to present the output.

Claude Tag](https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
