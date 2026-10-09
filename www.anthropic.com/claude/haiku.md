<!-- source: https://www.anthropic.com/claude/haiku -->

# Claude Haiku 4.5

![Claude Haiku 4.5](https://www-cdn.anthropic.com/images/4zrzovbb/website/8bb500ca6e681d7f8ef8136cc5b4b52ee62229ae-965x125.svg)

![Claude Haiku 4.5](https://www-cdn.anthropic.com/images/4zrzovbb/website/c788515ce313416153a634242621507511b4c978-174x144.svg)

The cheapest, fastest, and most capable small model we've ever released.

[Try Claude](https://claude.ai/)[Get API access](https://platform.claude.com/)

## Announcements

* New

  Claude Haiku 5.5

  Oct 7, 2026

  Claude Haiku 5.5 is the fastest and most efficient model in the Claude 5.5 family, built for high-volume, cost-sensitive work.

  [Read more](https://www.anthropic.com/claude-haiku-5-5)
* Claude Haiku 4.5

  Oct 15, 2025

  Claude Haiku 4.5 is our fastest, most cost-efficient model, matching Sonnet 4’s performance on coding, computer use, and agent tasks. Claude Haiku 4.5 scores 73.3% on SWE-bench Verified, making it one of the world’s best coding models.

  [Read more](https://www.anthropic.com/news/claude-haiku-4-5)
* Claude 3.5 Haiku

  Oct 22, 2024

  For a similar speed to Haiku 3, Haiku 3.5 improved across every skill set and surpassed Opus 3, the largest model in our previous generation, on many intelligence benchmarks.

  [Read more](https://www.anthropic.com/news/3-5-models-and-computer-use)

## Availability and pricing

Free, Pro, Max, Team, and Enterprise users can select Haiku 5.5 on Claude.ai, available on web, iOS, and Android.

For developers interested in building agents, Haiku 5.5 is available on the Claude Platform natively, and in Amazon Web Services, Google Cloud, and Microsoft Foundry.

Claude Haiku 5.5 is also available in Claude Code.

Pricing for Haiku 5.5 on the Claude Platform depends on prompt length. For prompts up to 100K tokens, it is $0.10 per million input tokens and $0.50 per million output tokens. For prompts over 100K tokens, it is $0.50 per million input tokens and $2.50 per million output tokens. You can save up to 90% with [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) and 50% with [batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing#pricing). To get started, use `claude-haiku-5-5` via the [Claude API](https://platform.claude.com/docs/en/about-claude/models/overview).

## Use cases

Haiku 5.5 is fast enough for real-time experiences and efficient enough to run at volume. It works alongside larger Claude models, making it practical to add things like summarization, classification, routing, and compaction to complex products and agent systems. It is also the first Haiku with effort controls, so teams can tune cost against intelligence for each task.

### High-volume text tasks

Haiku 5.5 powers high-volume product features and natural language processing tasks like classification, summarization, and text generation. Its speed and cost make it practical for processing large volumes of content.

### Real-time experiences

Haiku 5.5 is built for latency-sensitive use cases like chat, voice agents, live support, and in-app assistants, where speed matters most.

### Subagents

Haiku 5.5 is a fast, cost-efficient subagent for coding and well-defined tasks. A more intelligent model like Fable or Opus can plan the work and hand off subtasks to Haiku, making it practical to run many agents in parallel.

### Browser and desktop automation

Haiku 5.5 is a strong computer use agent for repetitive tasks like form filling, data entry, and moving information between apps, and it is cost efficient at scale.

### Simple coding

Haiku 5.5 handles focused coding and multi-step tool use, like direct edits and small, specific changes that need to apply across many files.

## Benchmarks

Haiku 5.5 is our most capable Haiku yet, a significant step up over Haiku 4.5 across coding, tool use, computer use, and agents.

![](https://www-cdn.anthropic.com/images/4zrzovbb/website/1555a3a443d3334052f5406f33c6d405bdbfd138-2000x1607.webp)

## Trust & Safety

We’ve conducted extensive testing and evaluation of Haiku 5.5 against our standards for safety, security, and reliability. In the [system card](https://www.anthropic.com/claude-haiku-5-5-system-card) for this release, we discuss new safety results in several categories.

## Hear from our customers

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/a17e31b7cd5991f3861530df2bc66ea21c3d879e-133x23.svg)

> Ask in Document is one of our big sources of spend, doing about 8M calls a week in production. It answers very specific questions on top of one or a few documents. We ran 400 queries, and Claude Haiku 5.5 was a statistically significant improvement over Haiku 4.5, 0.84 vs. 0.76.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/6449eaa27c807123a8bad597769d230e79b9587b-52x26.svg)

> Our customers use Box AI across large volumes of their enterprise content. With widespread usage comes the need to manage efficiency and cost, and to find the best model to suit the task at hand. In early testing, Claude Haiku 5.5 scored 11 points higher than Haiku 4.5 at about half the latency. We’d put it to use on analytical work that runs at scale, from cost reports to financial summaries and weekly recurring reviews.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/4f83f0b306a971d21d3ab03bd16f8114cff19b35-112x22.svg)

> We’re very impressed with Claude Haiku 5.5, particularly its speed. We ran it through our eval suite for AI Teammates, our AI agent product, covering use cases like triaging bugs, setting up projects, and searching large portfolios to surface high-risk or overdue work. Compared with the model we use today, we saw over a 30% reduction in latency for task completions and up to 2.5x faster inference per agent turn. It’s a noticeably snappier experience.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/beb4f74e935e111be9a63875ae7743aaea2cb0a2-88x64.svg)

> The short and high-volume work is where Haiku 5.5 fits for us, like quick lookups, subagents and summaries. While a bigger model builds the deck, a Haiku 5.5 subagent goes into the 10-K and pulls the segment revenue line the deck needs. It’s accurate enough that we’d trust it there and fast and cheap enough that we can run it a lot.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/9d3cc48409d490a361b2ca9b37f4c32d506165f4-3840x1124.png)

> At HubSpot, we use simulated portals to evaluate new models on CRM tasks like reporting on deals. We mostly test the smaller, more efficient models, and Claude Haiku 5.5 got the best score we’ve seen on this suite yet, at 92.8% averaged over three runs. One CRM audit task asks models to identify stale but ambiguous records. Across all of the models we tested, Haiku 5.5 was fastest to complete the task, and had the highest hit rate and the lowest false positive rate.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/e93eb9aa6aeb9e95f584bf8a401c4bdd1206d225-112x24.svg)

> Claude Haiku 5.5 joins the sidekick lineup in Devin Fusion as an excellent option. With Haiku 5.5 as the sidekick, Fusion holds a top-tier FrontierCode score of 66.2 while cutting cost and latency. You can try it today in the Devin CLI with Opus 5.5 as the lead.

01 / 06

## Frequently asked questions

### When should I use Haiku 5.5?

Use Haiku 5.5 when speed and volume matter most. It works well as a subagent and for high-volume work like summarization, classification, and request routing, and it is fast enough for real-time experiences like chat, voice, and live support. For complex coding and knowledge work, Opus 5.5 is the daily driver, and Sonnet 5.5 is a good fit for well-scoped tasks.

### How much does it cost to use Haiku 5.5?

On the Claude Platform, Haiku 5.5 costs $0.10 per million input tokens and $0.50 per million output tokens for prompts up to 100K tokens, and $0.50 per million input tokens and $2.50 per million output tokens for prompts over 100K tokens. To learn more, check out our [pricing page](https://claude.com/pricing#api).
