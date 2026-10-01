<!-- source: https://www.anthropic.com/claude/opus -->

# Claude Opus 4.8

![Claude Opus 4.8](https://www-cdn.anthropic.com/images/4zrzovbb/website/8b7aeb2c294b8da6ffdd641e472704a115675e3e-916x140.svg)

![Claude Opus 4.8](https://www-cdn.anthropic.com/images/4zrzovbb/website/072b5ad0a2fc97b5beff71c076cdc92516cd51ff-174x155.svg)

Hybrid reasoning model built for serious coding and AI agents, featuring a 1M context window

[Try Claude](https://claude.ai/)[Get API access](https://platform.claude.com/)

## Announcements

* NEW

  Claude Opus 5.5

  Sep 22, 2026

  We’re introducing Claude Opus 5.5. It performs at the level of Claude Fable 5.1 on most work and costs 40% less to run than Opus 5.

  [Read more](https://www.anthropic.com/claude-opus-5-5)
* Claude Opus 5

  Jul 24, 2026

  A step-change improvement for the Opus tier: stronger coding, more capable agents, and sharper professional work.

  [Read more](https://www.anthropic.com/news/claude-opus-5)
* Claude Opus 4.8

  May 28, 2026

  Stronger across coding, agentic tasks, and professional work, Opus 4.8 has the consistency and autonomy to keep working on long-running tasks.

  [Read more](https://www.anthropic.com/news/claude-opus-4-8)
* Claude Opus 4.7

  Apr 16, 2026

  Claude Opus 4.7 brings stronger performance across coding, vision, and complex multi-step tasks. It’s more thorough and consistent on difficult work, with better results across professional knowledge work.

  [Read more](https://www.anthropic.com/news/claude-opus-4-7)
* Claude Opus 4.6

  Feb 5, 2026

  Claude Opus 4.6 is our most capable model to date. Building on the intelligence of Opus 4.5, it brings new levels of reliability and precision to coding, agents, and enterprise workflows.

  [Read more](https://www.anthropic.com/news/claude-opus-4-6)

## Availability and pricing

Claude Opus 5.5 is our strongest Opus model yet, powering long-running, highly capable agents while delivering improvements in coding and professional work.

For business users and consumers who want to collaborate with a powerful model on complex tasks, Opus 5.5 is available on Claude for Pro, Max, Team, and Enterprise users.

For developers interested in building AI solutions that demand strong intelligence, Opus 5.5 is available on the Claude Platform natively, and in Amazon Web Services, Google Cloud, and Microsoft Foundry. Pricing for Opus 5.5 will cost an estimated 40% less to run than Opus 5 for typical workloads billed by token. Opus 5.5 costs$4 per million input tokens and $20 per million output tokens, 20% below Opus 5. [Cache reads](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), which are a large share of the cost of long-running agentic work, also now cost 60% less than Opus 5, at $0.20 per million tokens. To learn more, check out our [pricing page](https://claude.com/pricing#api). To get started, use `claude-opus-5-5` via the [Claude API](https://platform.claude.com/docs/en/about-claude/models/overview).

Fast mode for Opus 5.5 is also available now in Claude Code and on the Claude Platform with up to 2.5x faster speed. It costs $8 per million input tokens and $40 per million output tokens.

For workloads that need to run in the US, US-only inference is available at 1.1x pricing for input and output tokens. [Learn more](https://platform.claude.com/docs/en/build-with-claude/data-residency).

## Use cases

Claude Opus 5.5 is our most capable Opus model yet for coding, agents, and knowledge work. It costs less per token than Opus 5 and uses fewer tokens per task, so work on the Claude Platform, in Claude Code, and in the Claude apps costs about 40% less for work billed by token than on Opus 5.

Opus 5.5 also communicates more clearly. It leads with what matters, avoids jargon, and follows your writing rules, which makes it a better partner over long sessions. Key use cases include:

### Advanced coding

Opus 5.5 is our strongest Opus model for agentic coding. It handles long-running work in large codebases, including building features, debugging, refactoring, and code review. It finds the root cause before changing anything, checks its work as it goes, and explains its changes in plain language, so engineers can review and trust them quickly.

### Agents

Opus 5.5 is the Opus tier’s strongest agentic model, reliably orchestrating complex multi-tool tasks. It plans deliberately, coordinates subagents, uses memory to learn across sessions, and drives long-running work forward with minimal oversight. Along the way, it reports back clearly on what it did, what it found, and what it needs next.

### Enterprise workflows

Opus 5.5 is built to be the enterprise daily driver, powering agents that run projects end-to-end. It follows instructions precisely, stays in scope, and produces professional-grade spreadsheets, slides, and docs that are ready to use.

### Financial analysis

Opus 5.5 brings deeper reasoning and precision to financial workflows. It reads dense filings, models, and charts accurately, carries context across an entire deal or reporting cycle, and handles the nuance of compliance-sensitive work, with clear summaries of what it found and how it got there.

### Vision & computer use

Opus 5.5 is our best Opus model for vision and computer use. It reads dense documents, charts, screenshots, and diagrams at high fidelity, making it reliable for document extraction, visual analysis, and interpreting complex real-world imagery. Opus 5.5 brings deep reasoning to computer use, handling multi-step tasks that span multiple applications and require planning and judgment.

## Benchmarks

Claude Opus 5.5 delivers the intelligence and reliability to be your daily driver for serious coding and knowledge work.

![](https://www-cdn.anthropic.com/images/4zrzovbb/website/dc0c3b4c8b63872b717f3c7a28c7f3b3fc4a3fba-2160x1932.png)

Unless otherwise noted, all Claude Opus 5.5 results use adaptive thinking at max effort. Terminal-Bench 4.0 results are reported for Claude Opus 5.5 at xhigh effort and GPT-6 Astra at high effort, as reported by OpenAI; these represent each model’s highest score. Claude Opus 5.5 was evaluated with its production safeguards enabled. When they intervened, cybersecurity tasks were completed by Claude Opus 4.8, and biology and frontier LLM development tasks were completed by Claude Opus 5. This likely reduces Claude Opus 5.5’s performance on these benchmarks.1**Terminal-Bench 4.0:** The standard error is ±2.6 pts for Claude Opus 5.5 and ±1.6–2 pts for the other Claude models. The public leaderboard (5 trials/task, Claude Code harness) reports Claude Opus 5 at 51.8%; our setup reproduces it at 52.3%, within noise. GPT-6 Astra and GPT-5.6 Sol figures are as reported by OpenAI.2**AutomationBench:** AutomationBench results were run and reported by Zapier. These runs were performed without fallback models, so safeguard interventions were considered failures—this resulted in a lower score than Claude Opus 5.5 would achieve in practice. Claude Opus 5.5 results come from Zapier’s own evaluation during early access. Results for Opus 5, GPT-5.6 Sol, and GPT-6 Astra come from Zapier’s public leaderboard.3**Terminal-Bench-Science 0.1:** The standard error is ±3.5–5 pts per model. The public leaderboard (3 trials/task, Claude Code harness) reports Claude Opus 5 at 30.0%; our setup reproduces it at 29.0%, within noise. The GPT-6 Astra figure is as reported by OpenAI.

## Trust and safety

Extensive testing and evaluation ensures the release of Opus 5.5 meets Anthropic’s standards for safety, security, and reliability. The accompanying [system card](https://www.anthropic.com/claude-opus-5-5-system-card) covers safety results in depth.

## Safeguards

Opus 5.5 is the first Opus model to launch with a similar class of safeguards to Fable 5.1 in cybersecurity, biology, and anti-distillation. As our models grow more powerful, stricter safeguards are one way we prevent new capabilities from becoming tools for misuse.

## Hear from our customers

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/fc55f4db8afa5db479127fde5be3e492940f513d-94x64.svg)

> Developers want agents that can take on real software work and finish it. In our testing across GitHub Copilot CLI and VS Code, Claude Opus 5.5 used among the fewest tokens and steps we measured. In VS Code, it solved more terminal tasks than Opus 5 in less than half the steps. More than making individual tasks more efficient, it’s making developers’ bigger projects more achievable.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/72d90f8ad7d9766efae833c5d1d8d70bb7c46435-131x64.svg)

> I handed Claude Opus 5.5 a large engineering task across six of our repositories and let it run overnight, unattended. It stayed on task for over 18 hours defining how our services talk to each other and working out how each one should apply that. Compared with Opus 5, it hit milestones faster and required minimal reworking. Its code comments were short and useful instead of long and prose-heavy. I’m struggling to find anything negative to say.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/40a2a6a28afd8ac8fbf0e764b6bbf4ebf06a1977-133x64.svg)

> For Lovable builders, Opus 5.5 means faster builds with the same quality, whether you’re starting from scratch or working on a live app. It gathers context once, makes fewer and more complete edits, and doesn’t get stuck retrying, finishing in a third to half fewer steps and using significantly fewer tokens along the way.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/0ac44b8505d1e5d6ef413b164a81942a62e06f12-148x64.svg)

> On our genomics analysis work, Claude Opus 5 behaves more like a careful scientist than any model we’ve run. It reaches for the right statistical tests to rule out confounders, cross-checks its own results by independent methods, and stays on track through long multi-step analyses.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/559d5a46493e4a7546583509f86fe38167267409-161x64.svg)

> With Claude Opus 5.5, we’ve seen a clear improvement in token efficiency across our internal evaluations, as we’ve been able to complete the same tasks both cheaper and faster.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/fbd45dbecde0ed6e7c3bf8551df0525d87efd4de-127x64.svg)

> We test models on real engineering and trading-desk work. On our agentic coding tasks, Claude Opus 5.5 matched Opus 5’s quality in about half the turns, time and output tokens, cutting the cost of that workload by 40 to 50%. It posted the highest score we’ve recorded on one desk’s trading-support suite, passing tasks earlier Claude models had failed, and topped all eight models on our analysis task.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/4cd6a4282b7245aa0f3d86ba6b00c5b23fdbb272-114x64.svg)

> Claude Opus 5.5 delegates to subagents far more effectively and checks its own work in creative ways. Self-verification loops feel easier to set up. It found savings opportunities in our cloud bill that previous models had missed, and in code review it caught a bug by checking external docs for a third-party integration we’d modeled wrong several commits earlier.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/198c9eb920db5dc4581daefd3dc19d9fb51f6637-125x32.svg)

> Every call an agent makes is time and cost a developer feels. On a public benchmark of real command-line tasks, Claude Opus 5.5 solved more than Opus 5 while making about 40% fewer calls and using half the tokens. For developers building with Kiro, that means faster, more affordable agent sessions for routine tasks and complex challenges alike. Opus 5.5 will soon be available in Kiro.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/fc0cf984de735ef64c17f033f10efb9e273d69d8-125x64.svg)

> Even at its lowest effort setting, Claude Opus 5.5 caught 72% of known bugs in our code reviews to Opus 5’s 56% at high effort, with fewer false alarms and a fraction of the output. On US consulting analysis, low thinking effort matched its higher thinking settings on half the output and passed our quality checks. When more lower thinking efforts are deployed in production, that’s client-ready work delivered efficiently.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/beb4f74e935e111be9a63875ae7743aaea2cb0a2-88x64.svg)

> Financial firms need outputs that are consistently correct. At its lowest effort setting, Claude Opus 5.5 beat Opus 5 at high effort on our BigFinance Bench with about 60% fewer output tokens. Its answers are shorter and better structured, and its slides come out denser, more in line with industry standards.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/bf3f6430e27cae249b7696911571ab17b0715d9d-172x64.svg)

> Evaluating new models is central to the multi-model approach behind the LexisNexis Legal Intelligence Engine. In our initial evaluations, Claude Opus 5.5 identified highly relevant citations consistently, demonstrated strength with statutes, and structured its answers around the central legal frameworks and key issues. These are the kinds of capabilities we look for to help our customers accomplish more with Lexis+ with Protégé.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/74f9dcd65076def29413e42e822da248590b68d3-145x64.svg)

> In quant research, one wrong assumption can undermine a result. At its lowest effort setting, Claude Opus 5.5 largely solved our evaluation task. At higher settings, it went even further: it detected that the minute indexing in our own instructions was off by one and corrected for it, noting that this would cost it points with the grader. It was right, and no model we’ve tested had caught and acted on that before.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/7fbed01e869d6a4faf97317a1fc4b74f7997c66e-78x64.svg)

> As models get better at data work, we’re seeing more convincing-sounding conclusions the data doesn’t support. Claude Opus 5.5 keeps digging past the first plausible answer. One task in our DataBench benchmark asks whether packages were late or tracking was just slow. Opus 5 checked delivery confirmations and called tracking healthy. Opus 5.5 found the packages were late and tracking was broken too. We’re bringing it into the Hex agent for this work.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/efe6b287384573de696a70288b0418b9b4c3eebe-222x64.svg)

> CoCounsel combines multiple models with our content and expertise for complex legal work. With Claude Opus 5.5, we’re seeing better results in our expert evaluations and on our internal benchmarks, alongside gains in speed and token efficiency. We’re excited for customers to experience that difference in the back-and-forth with CoCounsel as a sounding board, weighing evidence and refining their thinking in ways benchmarks don’t fully capture.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/ac77c59a0734811a829fab67d7ee8e801e45c50c-136x64.svg)

> On end-to-end finance workflows graded against expert rubrics, Claude Opus 5.5 covered 86.6% of what we look for versus 60.3% for Opus 5. On retrieval evals, it achieved our best-ever citation recall with better token efficiency than Opus 5, which keeps our cost per research task in check.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/799ce98295cd71c7a43c13ddca27e9b893842b5f-100x64.svg)

> Viktor is an AI employee that lives in Slack and Microsoft Teams, so every step he takes shows up in our costs. At the same effort, Claude Opus 5.5 needs fewer steps and tool calls per task than Opus 5 and costs nearly half as much, while getting twice as many of our hardest tasks right.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/04280ffcf9a88b0f6fa85f2437b46102c8cb35e6-118x64.svg)

> Verbose, hard-to-follow output has been my biggest frustration with frontier models, and Claude Opus 5.5 fixes it. It writes like a good colleague, and follows our writing rules. A design spec came out usable with very minimal edits, and when it rewrote one of our prompts I preferred its version to my own. When it optimized our test suite, I could follow its reasoning easily and shipped the change with confidence.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/d514853a44cf69f069306c98b558f214112c4ef3-91x64.svg)

> I run long Claude Code sessions every day. On a multi-day rebase of 40 stacked pull requests, one Claude Opus 5.5 session directed a dozen more sessions and laid out every conflict plainly. On the calls that it held, it framed them clearly that after hours away I could answer in minutes. All 40 passed CI the next afternoon. It’s a substantial upgrade over Opus 5.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/bf162513ba017e72d4e07b0cd7683b86c4c5bc88-60x64.svg)

> Our customers use Box AI on enormous amounts of content, so speed and cost are a top priority. In our evaluations, Claude Opus 5.5 used a third of the tokens Opus 5 did, and its answers were 40% less verbose without losing accuracy. We expect that to matter a lot for teams running agents across their content in areas like financial services and the public sector.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/e778eeea7ac1ccd90b9842d9d3da3c17a8029c5e-216x64.svg)

> Overnight, Claude Opus 5.5 autonomously handled a bug in our Lakehouse services layer that I hadn’t had time to diagnose. It investigated, designed the fix, and implemented it on its own. By morning the change was done and passed our test suite. Its writing is easy to follow and more coherent than Opus 5’s. Our pull requests and user-facing docs have needed almost no editing.

![ logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/18f900625532e1baaa3302bdf9539f73592bdf60-164x64.svg)

> Claude Opus 5.5 is the first model we’d default to at medium effort. In our testing it matched Opus 5 on high effort, while using 20 to 25% fewer output tokens. On long, messy investigations it always came back with a clear, actionable answer. This means our customers get more done for less.

01 / 21

## Frequently asked questions

### When should I use Claude Opus 5.5?

We offer Claude models across the spectrum of speed, price, and performance. We recommend Opus 5.5 as your daily driver for coding and knowledge work—particularly production-ready code, complex document creation, and computer use.

### How much does it cost to use Claude Opus 5.5?

Pricing depends on how you want to use Opus 5.5. To learn more, check out our [pricing page](https://claude.com/pricing#api).
