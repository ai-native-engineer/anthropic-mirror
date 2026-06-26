<!-- source: https://claude.com/customers/rocket -->

Case study | Claude Platform

# Rocket generates agency-grade websites from a single prompt with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69926a920a7a522d58ea87e1_logo_rocket-light-mode.png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69926a95da6530911795f1b9_logo_rocket-dark-mode.png)

Industry:

Software

Company size:

Small

Product:

Location:

India

$200 vs. ~$20,000

for a comparable website that would take a traditional agency a month to deliver

1M+ users

Building websites on the platform

Introducing Claude Opus 4.6

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698529955ffaa6de831ec14e_opus%201%20(4).jpg)

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Read more

[Read more](#)Read more

Introducing Claude Opus 4.6

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525504b02eec936ac51b_68c469d41149ace562bfd24d_og-claude-product-claude-code.jpeg)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Read more

[Read more](/product/claude-code)Read more

Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Prev](#)Prev

[Next](#)Next

[Rocket.new](http://rocket.new) generates websites and web applications from a single natural language prompt—multi-page sites with working forms, navigation, and design decisions built in, rather than requiring users to iterate their way to a finished product.

## The challenge: Delivering beautiful designs without sacrificing depth

From the start, Rocket's team of 35 engineers focused on depth: generating complete, multi-page website experiences from a single prompt rather than requiring users to refine their way to a finished product.

Early user feedback validated that approach, but pointed to a gap. "The constant feedback was that our solutioning is good, but the designs look outdated," said Vishal Virani, CEO and co-founder of Rocket. Users wanted both: the comprehensive output Rocket was known for, and a design quality that felt current and intuitive.

The team considered switching to a different model for design generation, but found that doing so meant losing the code quality and comprehensiveness they had spent months optimizing with Claude. Rocket had built its platform on Claude Sonnet 4 from the beginning, and rather than accept that tradeoff, the engineers committed to achieving both depth and design quality by investing deeper in Claude's capabilities.

## Hundreds of experiments to unlock design on Sonnet 4.5

Rocket’s conviction came from what the team had already seen in Claude’s output. “The code quality is up to the mark, very low hallucination—we didn’t want to compromise on our solutioning depth by switching to another model,” Virani said. Instead, the engineering team ran hundreds of experiments, adjusting system prompts, context layers, and research inputs to get high-quality visual output from Sonnet 4.5. Within weeks, Rocket was generating creative, animated, and media-rich website designs with zero iterations required.

## How Rocket routes prompts across Claude's model family

Rocket’s implementation of Claude goes beyond a single API call. The platform uses a seven-layer decision-making architecture that processes every user prompt through a series of steps before generating any code.

The process started on Claude’s chat interface. “I ran the same basic prompt across models to see what the output looked like,” Virani said. “I started to understand which model to use for which kind of query, when to use deep thinking mode, and when to turn it off.” From there, the team moved to the API and built an internal evaluation tool where engineers run permutation combinations of model settings, score results side by side, and vet code quality.

Today, when a user enters a prompt—even a single sentence—Rocket’s system makes decisions at each layer: which model to use, whether to enable extended thinking, what design context to feed, what content decisions to make, and how to structure the final code generation. The platform strategically routes tasks across Claude’s model family:

* **Opus 4.6** handles deep research and strategic decisions about site architecture and user flows
* **Sonnet 4.5** powers code generation, producing clean, production-ready HTML, CSS, and JavaScript
* **Haiku 4.5** is used for speed- and cost-optimized tasks where lighter processing is sufficient.

This hybrid approach lets Rocket optimize for both quality and cost. “Instead of giving a choice of model to the user and increasing the cost, we decided to use a combination of multiple models for different purposes to optimize cost and speed,” Virani said.

“Not every model is good at everything," added co-founder and COO Deepak Dhanak. "After thousands of experiments, we decided to be a deterministic platform and have an opinion about which model to use and when."

## From engineering bet to measurable results

The engineering investment paid off in concrete terms. A comparable website project that might cost around $20,000 through a traditional agency and take a month to deliver can be generated on Rocket in roughly 15 minutes for about $200. Users who had spent 10 or more hours iterating with other AI tools to get a passable result found they could get there in a single prompt. More than a million users have now built on the platform.

The shift in design quality is visible in what the system produces. A single-sentence prompt requesting a landing page for an indie electronic artist returns a complete site with animations, embedded audio tracks, and a visual language that matches the genre, requiring very few follow-up prompts. For more complex requests, the platform generates multi-page websites with booking flows, forms, and navigation, making design decisions about fonts, color schemes, and layout based on the context it infers from the prompt.  “Even if a user puts in a one-liner, we’re able to generate an intuitive result,” Virani said.

The response to the design improvements has shaped Rocket’s roadmap. Users who saw what the system could create from scratch started asking whether it could also revamp their existing websites. The team is now building a feature where users input a URL and specify constraints—like keeping the SEO intact but redesigning the visuals, or preserving the copy but updating the layout—and the system rebuilds the site accordingly.

Virani’s team is also experimenting with Anthropic’s Agent SDK for future capabilities, though those plans are still in early stages.

"We are using almost everything in the Anthropic system,” Virani said. "We don't want our users to have the cognitive load of putting more and more prompts to get the result. We want them to feel the magic.”

‍

"We are using almost everything in the Anthropic system."

Vishal Virani

CEO and Co-founder, Rocket

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

## Related stories

[How Vercel built an ecosystem on the open skills standard](/customers/vercel-qa)How Vercel built an ecosystem on the open skills standard

How Vercel built an ecosystem on the open skills standard

Customer story

[Customer story](/customers/vercel-qa)Customer story

[Box builds document creation into its AI agent with Claude](/customers/box)Box builds document creation into its AI agent with Claude

Box builds document creation into its AI agent with Claude

Customer story

[Customer story](/customers/box)Customer story

[Juno helps people with chronic illness find patterns in their symptoms with Claude](/customers/juno)Juno helps people with chronic illness find patterns in their symptoms with Claude

Juno helps people with chronic illness find patterns in their symptoms with Claude

Customer story

[Customer story](/customers/juno)Customer story

[A conversation with Cursor on building coding agents for professional developers](/customers/cursor-qa)A conversation with Cursor on building coding agents for professional developers

A conversation with Cursor on building coding agents for professional developers

Customer story

[Customer story](/customers/cursor-qa)Customer story
