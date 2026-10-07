<!-- source: https://claude.com/resources/articles/1m-context-ga -->

Claude Opus 4.6 and Sonnet 4.6 now include the full 1M context window at standard pricing on the Claude Platform. Standard pricing applies across the full window — $5/$25 per million tokens for Opus 4.6 and $3/$15 for Sonnet 4.6. There's no multiplier: a 900K-token request is billed at the same per-token rate as a 9K one.

**What's new with general availability:**

* **One price, full context window.** No long-context premium.
* **Full rate limits at every context length.** Your standard account throughput applies across the entire window.
* **6x more media per request**. Up to 600 images or PDF pages, up from 100. Available today on Claude Platform natively, Microsoft Foundry, and Google Cloud’s Vertex AI.
* ​​**No beta header required.** Requests over 200K tokens work automatically. If you're already sending the beta header, it's ignored so no code changes are required.

**1M context is now included in Claude Code for Max, Team, and Enterprise users with Opus 4.6.** Opus 4.6 sessions can use the full 1M context window automatically, meaning fewer compactions and more of the conversation kept intact. 1M context previously required extra usage.

### **Long context that holds up**

A million tokens of context only matters if the model can recall the right details and reason across them. Opus 4.6 scores 78.3% on MRCR v2, the highest among frontier models at that context length.

![](https://assets.claude.com/20962572d16ec5031b2100795c58a3974ab7a304.png)

Claude Opus 4.6 and Sonnet 4.6 maintain accuracy across the full 1M window. Long context retrieval has improved with each model generation.

That means you can load an entire codebase, thousands of pages of contracts, or the full trace of a long-running agent — tool calls, observations, intermediate reasoning — and use it directly. The engineering work, lossy summarization, and context clearing that long-context work previously required are no longer needed. The full conversation stays intact.

![Resolve AI](https://assets.claude.com/8b9254c4648042482204412c545e441fe728c810.svg)

> “Large-scale production systems have endless context, and production incidents can get very complex. With Claude's 1M context window, we are able to keep every entity, signal, and working theory in view from first alert to remediation without having to repeatedly compact or compromise the nuances of these systems.”

Mayank Agarwal, Founder & CTO

![Hex](https://assets.claude.com/9968e969a67c49206d34fe9b4f8ec0a6836fd0e1.svg)

> “We raised our Opus context window from 200k to 500k and the agent runs more efficiently — it actually uses fewer tokens overall. Less overhead, more focus on the goal at hand.”

Izzy Miller, AI Research Lead

![Endex](https://assets.claude.com/f8e632d4750a94b94d2b18e0c0b2aebf222b200c.svg)

> “Real-world spreadsheet tasks require deep research and complex multi-step plans. Claude's 1M context window let’s us maintain task adherence and attention to detail.”

Tarun Amasa, CEO

![Ramp](https://assets.claude.com/6db782273272dd89f11df7b54089328994fe718e.svg)

> “Claude Code can burn 100K+ tokens searching Datadog, Braintrust, databases, and source code. Then compaction kicks in. Details vanish. You're debugging in circles. With 1M context, I search, re-search, aggregate edge cases, and propose fixes — all in one window.”

Anton Biryukov, Software Engineer

![Obvious](https://assets.claude.com/03a84628482ec01a2162a29491d51e5328863180.svg)

> “Before Opus 4.6's 1M context window, we had to compact context as soon as users loaded large PDFs, datasets, or images — losing fidelity on exactly the work that mattered most. We've seen a 15% decrease in compaction events. Now our agents hold it all and run for hours without forgetting what they read on page one.”

Jon Bell, CPO

![Cognition](https://assets.claude.com/668e21fde8e649dceecf16e585196cbf01f4f916.svg)

> “Opus 4.6 with 1M context window made our Devin Review agent significantly more effective. Large diffs didn't fit in a 200K context window so the agent had to chunk context, leading to more passes and loss of cross-file dependencies. With 1M context, we feed the full diff and get higher-quality reviews out of a simpler, more token-efficient harness.”

Adhyyan Sekhsaria, Founding Engineer

![Eve Legal](https://assets.claude.com/f1efc487a08ab700dd2f0a0d09e717745da3e2d0.svg)

> “Eve defaults to 1M context because plaintiff attorneys' hardest problems demand it. Whether it's cross-referencing a 400-page deposition transcript or surfacing key connections across an entire case file, the expanded context window lets us deliver materially higher-quality answers than before.”

Mauricio Wulfovich, ML Engineer

![PSI PBC](https://assets.claude.com/ef5563027673564aadc866ae7032f38298b93137.svg)

> “Scientific discovery requires reasoning across research literature, mathematical frameworks, databases, and simulation code simultaneously. Claude Opus 4.6’s 1M context and expanded media limits let our agentic systems synthesize hundreds of papers, proofs, and codebases in a single pass, helping us dramatically accelerate fundamental and applied physics research.”

Dr. Alex Wissner-Gross, Co-Founder

![General Counsel](https://assets.claude.com/bb452391c42bbffa172911e7671d9d7c088551f8.png)

> “With Claude's 1M context, an in-house lawyer can bring five turns of a 100-page partnership agreement into one session and finally see the full arc of a negotiation. No more toggling between versions or losing track of what changed three rounds ago.”

Bardia Pourvakil, Co-founder and CTO

![Resolve AI](https://assets.claude.com/8b9254c4648042482204412c545e441fe728c810.svg)

> “Large-scale production systems have endless context, and production incidents can get very complex. With Claude's 1M context window, we are able to keep every entity, signal, and working theory in view from first alert to remediation without having to repeatedly compact or compromise the nuances of these systems.”

Mayank Agarwal, Founder & CTO

![Hex](https://assets.claude.com/9968e969a67c49206d34fe9b4f8ec0a6836fd0e1.svg)

> “We raised our Opus context window from 200k to 500k and the agent runs more efficiently — it actually uses fewer tokens overall. Less overhead, more focus on the goal at hand.”

Izzy Miller, AI Research Lead

![Endex](https://assets.claude.com/f8e632d4750a94b94d2b18e0c0b2aebf222b200c.svg)

> “Real-world spreadsheet tasks require deep research and complex multi-step plans. Claude's 1M context window let’s us maintain task adherence and attention to detail.”

Tarun Amasa, CEO

![Ramp](https://assets.claude.com/6db782273272dd89f11df7b54089328994fe718e.svg)

> “Claude Code can burn 100K+ tokens searching Datadog, Braintrust, databases, and source code. Then compaction kicks in. Details vanish. You're debugging in circles. With 1M context, I search, re-search, aggregate edge cases, and propose fixes — all in one window.”

Anton Biryukov, Software Engineer

![Obvious](https://assets.claude.com/03a84628482ec01a2162a29491d51e5328863180.svg)

> “Before Opus 4.6's 1M context window, we had to compact context as soon as users loaded large PDFs, datasets, or images — losing fidelity on exactly the work that mattered most. We've seen a 15% decrease in compaction events. Now our agents hold it all and run for hours without forgetting what they read on page one.”

Jon Bell, CPO

![Cognition](https://assets.claude.com/668e21fde8e649dceecf16e585196cbf01f4f916.svg)

> “Opus 4.6 with 1M context window made our Devin Review agent significantly more effective. Large diffs didn't fit in a 200K context window so the agent had to chunk context, leading to more passes and loss of cross-file dependencies. With 1M context, we feed the full diff and get higher-quality reviews out of a simpler, more token-efficient harness.”

Adhyyan Sekhsaria, Founding Engineer

1/9

### **Getting started**

1M context is available today on the Claude Platform natively and through Amazon Bedrock, Google Cloud’s Vertex AI, and Microsoft Foundry. Claude Code Max, Team, and Enterprise users on Opus 4.6 will default to 1M context automatically.

See our [documentation](https://platform.claude.com/docs/en/build-with-claude/context-windows) and [pricing](https://platform.claude.com/docs/en/about-claude/pricing) for details.

‍

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
