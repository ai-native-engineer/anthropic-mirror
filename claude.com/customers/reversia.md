<!-- source: https://claude.com/customers/reversia -->

Case study | Claude Platform

# Reversia translates e-commerce stores across 110+ languages with Claude

[Try Claude](https://claude.ai)

![Reversia logo](https://assets.claude.com/86b324fdb04166c3b115b1cf48071e52e83d08cf.svg)

Industry:
:   Ecommerce

Company size:
:   Startup

Product:
:   Claude Platform

Location:
:   EMEA

99% translation accuracy

validated by native-speaking translation professionals

2–3 weeks to minutes

to launch a new language on a merchant's store

[Reversia](https://reversia.tech/) is a Paris-based e-commerce translation platform that integrates natively with Shopify app. It translates every piece of a merchant's store: product descriptions, collections, blog posts, navigation, SEO metadata, and the structured data fields that power modern Shopify storefronts. More than 100 brands use Reversia across 110+ supported languages.

## With Claude, Reversia:

* Achieved 99% translation accuracy, validated by independent native-speaking translators across multiple language pairs
* Estimated 70–80% lower cost than traditional per-word pricing, enabled by Claude-powered flat subscription model
* Reduced new language launches from 2 to 3 weeks to minutes
* Translates content updates within 1 to 3 minutes of a change, with no manual intervention
* Supports 110+ languages, including regional variants, with no per-language surcharge

## The challenge

## Machine translation wasn't built for brand copy

For brands running [Shopify stores in multiple countries](https://apps.shopify.com/reversia), localization has been a persistent bottleneck. When Reversia's co-founder Anatole Rozan looked at what was available, the options weren't close to what merchants needed.

"The existing translation apps on Shopify had massive gaps," Rozan said. "The translations themselves were literal and low quality, and most apps capped the number of languages you could add." Key content types like metafields and metaobjects often went untranslated entirely, and internal linking for SEO was broken or ignored. Merchants knew international expansion was a growth lever, but the tools weren't keeping up.

Reversia's first version used a conventional machine translation engine, and the same problems applied: the output was overly literal, and the engine produced significant errors when processing HTML content. Launching a new language still took two to three weeks of manual work, coordinating translations, verifying internal links, and checking that nothing was missed.

Choosing the right Claude model

![Choosing the right Claude model](https://assets.claude.com/7388619b452db0af26c78442a275c86c5ebe3124.jpg?w=2400&q=75&fm=webp&fit=max)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## The solution

## Selecting Claude for contextual understanding

When the team decided to rebuild the translation layer on an LLM, they ran a structured benchmark across multiple providers. They tested each model side-by-side on real merchant content across multiple language pairs. The criteria included translation quality, contextual understanding, tone consistency, and the ability to handle glossary rules and HTML structure. Claude scored highest on all four quality metrics.

"It's overall more expensive than some alternatives, but we haven't found anything better to this day," Rozan said. "For a product where translation quality is the entire value proposition, that's what matters."

Reversia now runs Claude Sonnet 4.6 as its primary translation model, with Claude Haiku 4.5 running a secondary quality-check pass on all translated content to flag inconsistencies before publication. The team plans to upgrade to Opus 4.7.

## How Reversia translates stores with Claude

The core of Reversia's product is a glossary system that injects merchant-defined rules directly into Claude's prompt context at translation time. Rather than simple find-and-replace word matching, merchants can force specific term translations (always render "vestiaire" as "wardrobe" in English), exclude brand and product names from translation so they stay unchanged across every language, and add free-form natural language instructions such as "Adapt shoe size conventions for the German market" or "Translate in a modern, accessible tone for urban 20–40 year-olds." This is where Claude's reasoning matters. A conventional translation engine can swap words, but Reversia needed a model that could apply brand-specific rules around tone, audience, and terminology without breaking the output.

Claude also translates content types that often go unaddressed in localization: metafields and metaobjects, SEO title tags, meta descriptions, hreflang attributes, canonical URLs, and internal cross-language linking. Every URL is preserved so shoppers experience identical navigation in any language.

Reversia monitors each merchant's store in real time. When content is created or updated, the platform detects the change and triggers a new Claude translation within 1 to 3 minutes. The pipeline runs on Google’s Cloud Run with Cloud Tasks managing job priority, and the app is fully native to Shopify, so merchants manage everything from within their existing admin.

"The goal is that after six months on Reversia, the AI translates as if it were an internal team member who knows your brand inside out," Rozan said. "Claude's ability to reason about context, not just words, is what makes that possible."

Introducing Claude Sonnet 4.6

![Introducing Claude Sonnet 4.6 ](https://assets.claude.com/ed4441933d84103efbafec32505ce83cf3b1dcc6.png?w=2400&q=75&fm=webp&fit=max)

Hybrid reasoning model with superior intelligence for agents, featuring a 1M context window

> "Claude's ability to reason about context, not just words, is what makes it possible."

Anatole RozanCo-founder, Reversia

## The outcome

## Native-quality translation in minutes

What used to take two to three weeks per language now takes minutes. A merchant activates a new language, and the entire store is translated automatically: products, collections, metafields, URLs, SEO metadata, internal linking. No manual verification of links or content completeness is required.

Reversia validates the output by having native-speaking translation professionals audit batches of merchant content across multiple language pairs. Across those audits, accuracy has consistently landed at 99%. Reversia charges a flat monthly subscription rather than per-word rates. The company estimates this runs 70–80% less than traditional translation pricing for a typical store.

## What’s next

Reversia's roadmap deepens its use of Claude on two fronts. Automatic quality scoring will have Claude evaluate its own translations before publication and flag segments that fall below a confidence threshold so merchants only review what needs attention. And persistent brand memory will soon let the system learn each merchant's preferences over time, making translations progressively more on-brand without additional glossary configuration.

"Our customers tell us the translations feel like they were written by a native speaker who actually knows their brand," Rozan said. "That's what we were after. Claude makes that possible at scale."

> "The AI translates as if it were an internal team member who knows your brand inside out."

Anatole RozanCo-founder, Reversia

[![Rakuten](https://assets.claude.com/5463fa5a44d12868ceec5ae30bfc8c412cafdeae.svg)

### Inside Rakuten's plan to turn every employee into a builder with Claude Managed Agents](https://claude.com/customers/rakuten-qa)[![Rakuten](https://assets.claude.com/5463fa5a44d12868ceec5ae30bfc8c412cafdeae.svg)

### Rakuten accelerates development with Claude Code](https://claude.com/customers/rakuten)[![Shopify](https://assets.claude.com/33de1bc0b1b2c92e879e513e3c14ec213c311ff1.svg)

### How Shopify uses Anthropic’s Claude on Google Cloud to supercharge Sidekick](https://claude.com/customers/shopify)[![L'Oreal](https://assets.claude.com/206c93e387b69b9a7fe23c7b2d3d33d66bc0fc60.svg)

### L'Oréal advances conversational analytics with Claude](https://claude.com/customers/loreal)
