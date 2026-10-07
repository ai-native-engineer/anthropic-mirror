<!-- source: https://claude.com/resources/articles/claude-api-skill -->

Today, CodeRabbit, JetBrains, Resolve AI, and Warp are bundling the [claude-api skill](https://github.com/anthropics/skills/tree/main/skills/claude-api), giving developers production-ready Claude API code wherever they build. First introduced in Claude Code in March, the skill is now in more of the tools developers already use.

## Building with the Claude API skill

The `claude-api` skill captures the details that make Claude API code work well, like which agent pattern fits a given job, what parameters change between model generations, and when to apply prompt caching. The result is fewer errors, better caching, cleaner agent patterns, and smoother model migrations.

It stays current as our SDKs change. When a new model is released or the API gains a feature, Claude already knows.

Anywhere the skill is available, ask Claude to:

* **"Improve my cache hit rate."** The skill applies prompt caching rules many developers miss.
* **"Add context compaction to my agent."** It walks you through the compaction primitives and agent patterns in our docs.
* **"Upgrade me to the latest Claude model."** Claude reviews your code and walks you through updating model names, prompts, and effort settings for a new model like [Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7). In Claude Code, you can also run this directly with `/claude-api migrate.`**‍**
* **"Build a deep research agent for my industry."** Claude walks you through configuring [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), so long-running research is a few prompts, not a custom project. In Claude Code, you can also run this directly with `/claude-api managed-agents-onboard`.

![Jetbrains New](https://assets.claude.com/5886ece0979c014f7e1fb5119f62efdb9aba5b96.svg)

> “With the Claude API skill, developers on JetBrains IDEs and Junie can turn a Claude API upgrade into a guided IDE workflow. A good example is migrating to Claude Opus 4.7, where the skill can update model references, move manual thinking settings to adaptive thinking, clean up outdated parameters and beta headers, and suggest the right effort level inline. That gives teams a stronger first pass and helps avoid version-specific mistakes that normally show up in cleanup rounds.”

Denis Shiryaev, Head of AI Dev Tools Ecosystem

![Resolve AI](https://assets.claude.com/8b9254c4648042482204412c545e441fe728c810.svg)

> “The Claude API skill helps Resolve AI engineers adopt new model capabilities faster. Instead of manually parsing migration guides and chasing every small API change, our team can move from model release to implementation in a single guided pass.”

Mayank Agarwal, Founder & CTO

![Warp](https://assets.claude.com/399915ee2f0b3513a52ff63e61b1da17ed7eb078.svg)

> “Developers shouldn't have to leave Warp to look up Claude API parameters or caching rules. With the Claude API skill built in, that knowledge is already there, so engineers stay in flow and ship faster.”

Zach Lloyd, Founder and CEO

![CodeRabbit New](https://assets.claude.com/739777711f80e97a1e98612b6d55f9f8498c55a1.svg)

> “At CodeRabbit, we review millions of PRs a week and see how often stale API knowledge causes production issues. The Claude API skill keeps Claude current as our SDKs change, so developers building agents run into fewer review-time surprises.”

Erik Thorelli, Developer Experience Lead

![Jetbrains New](https://assets.claude.com/5886ece0979c014f7e1fb5119f62efdb9aba5b96.svg)

> “With the Claude API skill, developers on JetBrains IDEs and Junie can turn a Claude API upgrade into a guided IDE workflow. A good example is migrating to Claude Opus 4.7, where the skill can update model references, move manual thinking settings to adaptive thinking, clean up outdated parameters and beta headers, and suggest the right effort level inline. That gives teams a stronger first pass and helps avoid version-specific mistakes that normally show up in cleanup rounds.”

Denis Shiryaev, Head of AI Dev Tools Ecosystem

![Resolve AI](https://assets.claude.com/8b9254c4648042482204412c545e441fe728c810.svg)

> “The Claude API skill helps Resolve AI engineers adopt new model capabilities faster. Instead of manually parsing migration guides and chasing every small API change, our team can move from model release to implementation in a single guided pass.”

Mayank Agarwal, Founder & CTO

![Warp](https://assets.claude.com/399915ee2f0b3513a52ff63e61b1da17ed7eb078.svg)

> “Developers shouldn't have to leave Warp to look up Claude API parameters or caching rules. With the Claude API skill built in, that knowledge is already there, so engineers stay in flow and ship faster.”

Zach Lloyd, Founder and CEO

![CodeRabbit New](https://assets.claude.com/739777711f80e97a1e98612b6d55f9f8498c55a1.svg)

> “At CodeRabbit, we review millions of PRs a week and see how often stale API knowledge causes production issues. The Claude API skill keeps Claude current as our SDKs change, so developers building agents run into fewer review-time surprises.”

Erik Thorelli, Developer Experience Lead

![Jetbrains New](https://assets.claude.com/5886ece0979c014f7e1fb5119f62efdb9aba5b96.svg)

> “With the Claude API skill, developers on JetBrains IDEs and Junie can turn a Claude API upgrade into a guided IDE workflow. A good example is migrating to Claude Opus 4.7, where the skill can update model references, move manual thinking settings to adaptive thinking, clean up outdated parameters and beta headers, and suggest the right effort level inline. That gives teams a stronger first pass and helps avoid version-specific mistakes that normally show up in cleanup rounds.”

Denis Shiryaev, Head of AI Dev Tools Ecosystem

![Resolve AI](https://assets.claude.com/8b9254c4648042482204412c545e441fe728c810.svg)

> “The Claude API skill helps Resolve AI engineers adopt new model capabilities faster. Instead of manually parsing migration guides and chasing every small API change, our team can move from model release to implementation in a single guided pass.”

Mayank Agarwal, Founder & CTO

1/4

## For Claude-powered coding agents

Any coding agent can bundle the `claude-api` skill to give their users expertise around the Claude API. If you are building a tool where developers write Claude API code, the skill is open source at [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/claude-api). Our bundling guide walks through the setup in about 20 lines of CI, and the skill stays current automatically.

## Getting started

The skill is already in [Claude Code](https://claude.com/product/claude-code), [CodeRabbit](https://www.coderabbit.ai/), [JetBrains](https://www.jetbrains.com/), [Junie](https://www.jetbrains.com/junie/), [Resolve AI](https://resolve.ai/), and [Warp](https://www.warp.dev/). To learn more, see the [claude-api skill docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill).

[ArticleSep 29, 2026

### Agents you can coach: how Asana builds human-agent teams with Claude

Arnab Bose, Chief Product Officer at Asana, on how Asana runs AI agents as teammates with scoped roles, shared memory, and work that everyone can see.
‍

Claude Platform](https://claude.com/resources/articles/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude)[ArticleSep 28, 2026

### Giving companies more control over their AI agents, with NVIDIA

Claude Platform](https://claude.com/resources/articles/giving-companies-more-control-over-their-ai-agents-with-nvidia)[ArticleSep 8, 2026

### Reducing cost and improving performance with Claude Platform

Tuning prompt caching, instructions, and effort can reduce Claude's cost without sacrificing application performance.

Claude Platform](https://claude.com/resources/articles/reducing-cost-and-improving-performance-with-claude-platform)[ArticleSep 2, 2026

### A guide to the anatomy of effective commerce agents

The architecture, latency & cost techniques, and eval practices for agents that make it easier to buy and sell online.

Claude Platform](https://claude.com/resources/articles/the-anatomy-of-effective-commerce-agents)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
