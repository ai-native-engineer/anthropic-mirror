<!-- source: https://claude.com/blog/claude-api-skill -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

# Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp

* Category

  [Agents](https://claude.com/blog/category/agents)

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  [Claude Enterprise](https://claude.com/solutions/enterprise)

  [Claude Code](https://claude.com/product/claude-code)
* Date

  April 29, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-api-skill

Today, CodeRabbit, JetBrains, Resolve AI, and Warp are bundling the [claude-api skill](https://github.com/anthropics/skills/tree/main/skills/claude-api), giving developers production-ready Claude API code wherever they build. First introduced in Claude Code in March, the skill is now in more of the tools developers already use.

## Building with the Claude API skill

The `claude-api` skill captures the details that make Claude API code work well, like which agent pattern fits a given job, what parameters change between model generations, and when to apply prompt caching. The result is fewer errors, better caching, cleaner agent patterns, and smoother model migrations.

It stays current as our SDKs change. When a new model is released or the API gains a feature, Claude already knows.

Anywhere the skill is available, ask Claude to:

* **"Improve my cache hit rate."** The skill applies prompt caching rules many developers miss.
* **"Add context compaction to my agent."** It walks you through the compaction primitives and agent patterns in our docs.
* **"Upgrade me to the latest Claude model."** Claude reviews your code and walks you through updating model names, prompts, and effort settings for a new model like [Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7). In Claude Code, you can also run this directly with `/claude-api migrate.`**‍**
* **"Build a deep research agent for my industry."** Claude walks you through configuring [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), so long-running research is a few prompts, not a custom project. In Claude Code, you can also run this directly with `/claude-api managed-agents-onboard`.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fa025bc189d96f44b5bfc1_Orange_Typemark_43bf516c9d.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fa0261a5b6253465bd45be_White_Typemark_79b9189d19%20(1).svg)

"At CodeRabbit, we review millions of PRs a week and see how often stale API knowledge causes production issues. The Claude API skill keeps Claude current as our SDKs change, so developers building agents run into fewer review-time surprises."

Erik Thorelli, Developer Experience Lead

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e543f9e6c0e1972c338437_logo_%5Bjetbrains%5D-%5Blight%5D.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e54425a3fe2aed4f88910e_logo_jetbrains_dark.svg)

"With the Claude API skill, developers on JetBrains IDEs and Junie can turn a Claude API upgrade into a guided IDE workflow. A good example is migrating to Claude Opus 4.7, where the skill can update model references, move manual thinking settings to adaptive thinking, clean up outdated parameters and beta headers, and suggest the right effort level inline. That gives teams a stronger first pass and helps avoid version-specific mistakes that normally show up in cleanup rounds."

Denis Shiryaev, Head of AI Dev Tools Ecosystem

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31397615d221067e19bda_Resolve%20SVG%20original%20color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31393431c1a52a589e3a9_Resolve%20SVG%20light%20color.svg)

“The Claude API skill helps Resolve AI engineers adopt new model capabilities faster. Instead of manually parsing migration guides and chasing every small API change, our team can move from model release to implementation in a single guided pass."

Mayank Agarwal, Founder & CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692481a076d768db9276c4d9_warp-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692481a493eb0f6f4ca5b90a_warp-white.svg)

"Developers shouldn't have to leave Warp to look up Claude API parameters or caching rules. With the Claude API skill built in, that knowledge is already there, so engineers stay in flow and ship faster."

Zach Lloyd, Founder and CEO

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## For Claude-powered coding agents

Any coding agent can bundle the `claude-api` skill to give their users expertise around the Claude API. If you are building a tool where developers write Claude API code, the skill is open source at [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/claude-api). Our bundling guide walks through the setup in about 20 lines of CI, and the skill stays current automatically.

## Getting started

The skill is already in [Claude Code](https://claude.com/product/claude-code), [CodeRabbit](https://www.coderabbit.ai/), [JetBrains](https://www.jetbrains.com/), [Junie](https://www.jetbrains.com/junie/), [Resolve AI](https://resolve.ai/), and [Warp](https://www.warp.dev/). To learn more, see the [claude-api skill docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill).

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225485fe31f1ed2d9a1_db28a79c9f4492b8471009d4c20e900f234ece48-1000x1000.svg)

Aug 26, 2026

### How Warp builds self-improving agents on Claude

Agents

[How Warp builds self-improving agents on Claude](#)How Warp builds self-improving agents on Claude

[How Warp builds self-improving agents on Claude](https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude)How Warp builds self-improving agents on Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Aug 21, 2026

### The AI-Native SDLC playbook

Enterprise AI

[The AI-Native SDLC playbook](#)The AI-Native SDLC playbook

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)The AI-Native SDLC playbook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d226ca443e2e05990c00_83d7d2fe412ceb4dfe627f0d5f3d64aff1a3f5db-1000x1000.svg)

Aug 24, 2026

### How an Anthropic field marketer uses Claude Code to send weekly personalized updates to every sales rep

Claude Code

[How an Anthropic field marketer uses Claude Code to send weekly personalized updates to every sales rep](#)How an Anthropic field marketer uses Claude Code to send weekly personalized updates to every sales rep

[How an Anthropic field marketer uses Claude Code to send weekly personalized updates to every sales rep](https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep)How an Anthropic field marketer uses Claude Code to send weekly personalized updates to every sales rep

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

Aug 13, 2026

### Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

Agents

[Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions](#)Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

[Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions](https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions)Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Enterprise

Claude Code

Agents

Coding
