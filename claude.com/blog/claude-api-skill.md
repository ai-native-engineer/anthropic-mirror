<!-- source: https://claude.com/blog/claude-api-skill -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

# Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp

  [Agents](https://claude.com/blog/category/agents)

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  Claude Enterprise

  Claude Code
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

The skill is already in [Claude Code](https://code.claude.com/docs/en/overview), [CodeRabbit](https://www.coderabbit.ai/), [JetBrains](https://www.jetbrains.com/), [Junie](https://www.jetbrains.com/junie/), [Resolve AI](https://resolve.ai/), and [Warp](https://www.warp.dev/). To learn more, see the [claude-api skill docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill).

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225588ad176f7c4aafd_abc884c723daea810d2e986455358281a2f94102-1000x1000.svg)

Jun 24, 2026

### Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

Claude Code

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](#)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](/blog/agent-identity-access-model)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

Jun 3, 2026

### Running an AI-native engineering org

Claude Code

[Running an AI-native engineering org](#)Running an AI-native engineering org

[Running an AI-native engineering org](/blog/running-an-ai-native-engineering-org)Running an AI-native engineering org

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

May 12, 2026

### How Anthropic's cybersecurity team built a threat detection platform with Claude Code

Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](#)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](/blog/how-anthropic-uses-claude-cybersecurity)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2222403b092e0358b0e_cd4fd51deacd067d4e30aee4f4b149f6cba1b97b-1000x1000.svg)

Apr 20, 2026

### Meet the winners of our Built with Opus 4.6 Claude Code hackathon

Claude Code

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](#) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

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
