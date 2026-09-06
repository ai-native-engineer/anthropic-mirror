<!-- source: https://claude.com/blog/claude-for-commerce-agents -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d228c83775fcc75f4e6d_74409af25137110ac04cc39e4d5ea0a2fbcea421-1000x1000.svg)

# Building commerce agents with Claude

Retailers running shopping agents on Claude have seen carts up to 35% larger and shoppers 60% more likely to complete a purchase.

* Category

  [Product announcements](https://claude.com/blog/category/announcements)

  [Agents](https://claude.com/blog/category/agents)
* Product

  [Claude Platform](https://claude.com/platform/api)
* Date

  September 2, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-for-commerce-agents

Many of the world’s largest retailers, marketplaces, e-commerce platforms, and travel companies use Claude to build agents that make shopping easier. Enterprise customers like Shopify, Priceline, and others have agents that let consumers use AI to search for what they want in plain language, find it, compare it, and buy it.

Today, we're launching a blueprint to help build commerce agents on Claude. It contains the harnesses, patterns, and guardrails an engineering team needs to get a commerce agent running in days, with reference implementations of a shopping agent and a merchant agent for retail, travel, telecom, and ticketing platforms. It also includes a Claude Code plugin to get you started.

The code deploys where you already build with Claude, including the Claude API, Amazon Bedrock, Microsoft Foundry, or Google Cloud Vertex AI. You can also work with our solutions and ecosystem partners such as Accenture, Mastercard, and Visa, who are working with us to enable clients and merchant communities to leverage the blueprints.

It’s [available today](https://github.com/anthropics/commerce-agents), with [live demos](https://claude.com/solutions/commerce) for each vertical and an [engineering deep-dive](http://claude.com/blog/the-anatomy-of-effective-commerce-agents) on how it was built, just in time for holiday season planning.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a95f44f1757be75a0616bd0_demo-retail.webp)

*The shopping agent running in the ACME* [*retail example*.](https://claude.com/solutions/commerce)

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a972d45795f7bbae7ce272f_Retail%20%E2%80%94%20Merchant%20workspace.png)

## Trusted across the industry

Companies that serve shoppers, travelers, subscribers, and merchants build and run agents on Claude. Here's what they have to say about building commerce agents with Claude:

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ae674813a930db5dcaf7_Visa_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ae6d39727b14adbf7631_Visa_dark.svg)

“AI will fundamentally reshape commerce, but trust must remain at the center of every transaction. Merchants are telling us they want more control over how AI engages their customers. Our collaboration with Anthropic on their commerce blueprint helps bring together the intelligence of Claude with the trust, security, and global reach of the Visa network, empowering merchants to deliver better customer experiences while maintaining the relationships that drive their businesses forward.”

Jack Forestell, Chief Product and Strategy Officer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a96d51f43f5c41132ff29ed_mastercard-logo.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a96d51f43f5c41132ff29ed_mastercard-logo.svg)

“Trust is the currency of commerce, and it is even more critical in the agentic era. With Anthropic's commerce blueprint, we're helping merchants build their own agents with Claude to drive their growth. By combining AI innovation with trusted payments and commerce infrastructure, we're helping connect consumers, merchants and AI agents securely, seamlessly and at scale.”

Sherri Haymond, Executive Vice President, Global Head of Digital Commercialization

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68f679a0b07cb25d6830bc76_accenture_logo.svg.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68f679a262980d8650836fd9_accenture_logo.svg-1.svg)

“Commerce agents are quickly becoming a critical capability for organizations seeking to deliver the personalized, intelligent customer experiences that today’s consumers expect. Our latest research revealed that 85% are now open to collaboration with an AI agent and nearly three in four would trust a personal AI agent more than their best friend to make a purchase on their behalf. This is more than a shift in how people shop. Agentic commerce is rewriting the rules of brand value – fundamentally shaping what gets purchased, when, where and by whom. Anthropic’s commerce agent blueprint provides a proven starting point that can help organizations accelerate deployment and build differentiated experiences that increase customer satisfaction, loyalty, and growth. Combined with Accenture's deep retail and consumer goods expertise, we can help clients move from concept to production and realize value from agentic AI faster.”

Kath Gramling, Global Consumer Goods, Retail and Travel lead

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a95a7dc912b141697da7a0c_priceline-color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a95a7de9410fba39a2cfc8d_priceline-white.svg)

“A trip is one of the most complex things a person buys: flights, hotels, cars, and dozens of options to weigh against each other. Penny, our AI assistant, navigates all of that in one conversation and surfaces the best options and best value. We built the latest generation of Penny on Claude because that kind of reasoning is exactly what Claude models are good at.”

Cobus Kok, Vice President, AI Experiences

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a9771254c4225f0bc16623e_intuit-color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a9771288cd6fb2332ebeabe_intuit-white.svg)

“Millions of consumers, businesses and accountants run their finances on Intuit. Working with partners like Anthropic, we're building highly personalized experiences that provide customers with a clear understanding of what's shifting in their business and why, so they can take action with complete confidence. We are creating a financial system of intelligence by combining frontier AI reasoning, including Claude, with our proprietary data, capabilities, intelligence, and human expertise that powers the next level of prosperity for our customers.”

Chris Kasten, Intuit’s Chief Architect and SVP of Engineering, Platform and Development Xceleration Group

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68da9368f2bd228e7080695d_logo_shopify-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68da936caa7913237c0589f4_logo_shopify-dark.svg)

“We want our merchants to be everywhere customers are shopping, and increasingly that means a conversation with an agent. We're building on Anthropic's blueprints with a reference storefront implementation that connects them to a merchant's store through Catalog, UCP and Shop Sign-in. Merchants can use Claude to build agents that help customers find products, check out, and answer questions about their orders.”

Vanessa Lee, VP Product

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a906156d04a91e09ce93cb7_klaviyo-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a90615393673a5ea036d6b2_klaviyo-white.svg)

“Commerce and stunning customer experiences require personalization, and every brand on Klaviyo sits on more customer data and decisions than any team could act on by hand. Claude closes that gap, turning consumer preferences and performance data into the insights, campaigns and personalization that drive revenue. That's why we keep building with Anthropic: agents do complex analysis, design and decision making, and businesses can focus on delighting customers.”

Andrew Bialecki, Founder and Co-CEO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a97717810bbbdeb232b1861_wix-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a97717a1ece7880de88876a_wix-white.svg)

“Wix’s mission has always been to make complex technology simple and accessible for our users. For merchants, that means providing powerful commerce capabilities without adding operational complexity, and agents are a natural next step. Our engineers had a working commerce agent taking prompts within fifteen minutes, and the pilot showed the potential of combining Anthropic’s AI capabilities with Wix’s commerce platform and deep expertise in commerce for SMB.”

Dror Zalika, Head of Commerce at Wix

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a95a7436f6227c5015996a7_zomato-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a95a74649d16140f5e9939f_zomato-white.svg)

“Our engineers had the blueprint running with no blockers; the setup worked exactly as documented. The practices it bakes in, from tool iteration limits to prompt caching, are the ones we recognized from building Zomato's own agent. Teams standing up their first agent on Claude will skip weeks of trial and error.”

Akhil Bansal, Senior Engineering Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a90644256c9ac773063e8e6_fetch-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a906441c42656e199477abf_fetch-white.svg)

“Our engineers had both commerce agents from Anthropic's blueprint running locally in well under an hour, with live conversations working on the first attempt. We ran the Claude Code workflow twice and got two different architectures back, each designed to what we'd asked for. For a team starting from scratch, that turns days of agent scaffolding into hours.”

Ashley Nader, Staff Product Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aded6c2824c6159c1795_Square_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ade71ac3dc1f534d924d_Square_dark.svg)

“Much of what we build at Square is about giving sellers time back, and agents are a big leap in our ability to do that. We're building agentic tools that watch sales, labor, and inventory and come back with real next steps, not just an answer, while keeping sellers in control. Trust is the hardest part of that work, and Claude helps us meet a high standard.”

Willem Avé, Head of Product

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Getting started

The blueprint is available today. [Contact our sales team](https://claude.com/contact-sales) to learn more, schedule a demonstration, or discuss how to implement for your organization.

1. Fork the repository at [github.com/anthropics/commerce-agents](https://github.com/anthropics/commerce-agents).
2. Read the engineering deep-dive at [claude.com/blog/the-anatomy-of-effective-commerce-agents.](http://claude.com/blog/the-anatomy-of-effective-commerce-agents)
3. See the vertical demos and request a working session at [claude.com/solutions/commerce](https://claude.com/solutions/commerce).

Register for our [webinar](http://anthropic.com/webinars/building-claude-commerce-agents) to see the deep dive where we'll share live walkthroughs, demos, and cover how commerce builders can get the most out of Claude.

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Sep 2, 2026

### A guide to the anatomy of effective commerce agents

Agents

[A guide to the anatomy of effective commerce agents](#)A guide to the anatomy of effective commerce agents

[A guide to the anatomy of effective commerce agents](https://claude.com/blog/the-anatomy-of-effective-commerce-agents)A guide to the anatomy of effective commerce agents

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a90479f5433ec75978f1e8a_Object-Apple.svg)

Aug 28, 2026

### Claude for Teachers, now available for U.S. K-12 schools and districts

Product announcements

[Claude for Teachers, now available for U.S. K-12 schools and districts](#)Claude for Teachers, now available for U.S. K-12 schools and districts

[Claude for Teachers, now available for U.S. K-12 schools and districts](https://claude.com/blog/claude-for-teachers-now-available-for-schools-and-districts)Claude for Teachers, now available for U.S. K-12 schools and districts

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22b8840b2f6f9a40fe0_8925ac952fa2cb8eb5e845b2e44f3e71b33fd695-1000x1000.svg)

Aug 26, 2026

### Claude gets its own browser in Cowork

Product announcements

[Claude gets its own browser in Cowork](#)Claude gets its own browser in Cowork

[Claude gets its own browser in Cowork](https://claude.com/blog/cowork-built-in-browser)Claude gets its own browser in Cowork

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225485fe31f1ed2d9a1_db28a79c9f4492b8471009d4c20e900f234ece48-1000x1000.svg)

Aug 26, 2026

### How Warp builds self-improving agents on Claude

Agents

[How Warp builds self-improving agents on Claude](#)How Warp builds self-improving agents on Claude

[How Warp builds self-improving agents on Claude](https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude)How Warp builds self-improving agents on Claude

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

Agents
