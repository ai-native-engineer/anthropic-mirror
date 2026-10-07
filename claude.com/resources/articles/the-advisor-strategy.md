<!-- source: https://claude.com/resources/articles/the-advisor-strategy -->

Developers who want to better balance intelligence and cost have converged on what we call the advisor strategy: pair Opus as an advisor with Sonnet or Haiku as an executor. This brings near Opus-level intelligence to your agents while keeping costs near Sonnet levels.

Today we're introducing the advisor tool on the Claude Platform to make the advisor strategy a one-line change in your API call.

## Build cost-effective agents with the advisor strategy

![](https://assets.claude.com/8f630cd9ff3ec9f706e977e7b91143743c04221d.png)

With the advisor strategy, Sonnet or Haiku runs the task end-to-end as the executor, calling tools, reading results, and iterating toward a solution. When the executor hits a decision it can't reasonably solve, it consults Opus for guidance as the advisor. Opus accesses the shared context and returns a plan, a correction, or a stop signal, and the executor resumes. The advisor never calls tools or produces user-facing output, and only provides guidance to the executor.

This inverts a common sub-agent pattern, where a larger orchestrator model decomposes work and delegates to smaller worker models. In the advisor strategy, a smaller, more cost-effective model drives and escalates without decomposition, a worker pool, or orchestration logic. Frontier-level reasoning applies only when the executor needs it, and the rest of the run stays at executor-level cost.

In our evaluations, Sonnet with Opus as an advisor showed a 2.7 percentage point increase on [SWE-bench Multilingual](https://www.swebench.com/multilingual.html)1 over Sonnet alone, while reducing cost per agentic task by 11.9%.

![](https://assets.claude.com/fe28fc77f04a26f04870c65c3f36204f69a23e49.png)

## **The advisor tool**

We’re bringing the advisor strategy to our API with the [**advisor tool**](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool), a server-side tool which Sonnet and Haiku know to invoke when they need guidance or help with a specific task.

In our evaluations, Sonnet with an Opus advisor improved scores across BrowseComp2 and Terminal-Bench 2.03 benchmarks while costing less per task than Sonnet alone.

![](https://assets.claude.com/c01f1490dc3cfe7d5995541fc3fbd64d55d0dffe.png)

The advisor strategy also works with Haiku as the executor. On BrowseComp, Haiku with an Opus advisor scored 41.2%, more than double its solo score of 19.7%. Haiku with an Opus advisor trails Sonnet solo by 29% in score but costs 85% less per task. The advisor adds cost relative to Haiku alone, but the combined price is still a fraction of what Sonnet costs, making it a strong option for high-volume tasks that require a balance of intelligence and cost.

![](https://assets.claude.com/ea472c56f2d583b9d09c85e5c6539864e4dd9ab4.png)

Declare advisor\_20260301 in your Messages API request, and the model handoff happens inside a single /v1/messages request—no extra round-trips or context management. The executor model decides when to invoke it. When it does, we route the curated context to the advisor model, return the plan, and the executor continues all within the same request.

Copy

```
response = client.messages.create(
    model="claude-sonnet-4-6",  # executor
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-6",
            "max_uses": 3,
        },
        # ... your other tools
    ],
    messages=[...]
)

# Advisor tokens reported separately
# in the usage block.
```

**Pricing**. Advisor tokens are billed at the advisor model's rates; executor tokens are billed at the executor model's rates. Since the advisor only generates a short plan (typically 400-700 text tokens) while the executor handles the full output at its lower rate, the overall cost stays well below running the advisor model end-to-end.

**Built-in cost controls.** Set max\_uses to cap advisor calls per request. Advisor tokens are reported separately in the usage block so you can track spend per tier.

**Works alongside your existing tools.** The advisor tool is just another entry in your Messages API request. Your agent can [search the web](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool), [execute code](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool), and consult Opus in the same loop.

![Bolt](https://assets.claude.com/c47ae719ec15794844da97bc7651c0081ce5a4e2.svg)

> “It makes better architectural decisions on complex tasks while adding no overhead on simple ones. The plans and trajectories are night and day different.””

Eric Simmons, CEO and Founder, Bolt

![Genspark (square)](https://assets.claude.com/b1e42f1b17a4c1b366adb56b71934a19f5b0c621.svg)

> “We saw clear improvements in agent turns, tool calls, and overall score — better than a planning tool we built ourselves.”

Kay Zhu, Cofounder & CTO, Genspark

![Eve Legal](https://assets.claude.com/f1efc487a08ab700dd2f0a0d09e717745da3e2d0.svg)

> “On structured document extraction tasks, the advisor tool enables Haiku 4.5 to dynamically scale intelligence by consulting Opus 4.6 as complexity demands, matching frontier-model quality at 5× lower cost.”

Anuraj Pandey, Machine Learning Engineer, Eve Legal

## Get started

The advisor tool is available now in beta natively on the Claude Platform. To get started:

1. Add the beta feature header: anthropic-beta: advisor-tool-2026-03-01
2. Add the advisor\_20260301 to your Messages API request
3. Modify your [system prompt](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#suggested-system-prompt-for-coding-tasks) based on your use case

We recommend running your existing eval suite against Sonnet solo, Sonnet executor with Opus advisor, and Opus solo. Explore the [docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool) to learn more.

## Footnotes

1. **SWE-bench Multilingual:** Sonnet 4.6 solo used adaptive thinking. Sonnet 4.6 + Advisor used our suggested system prompt for coding with thinking turned off. Both runs used high effort with bash and file editing tools. Scores are averaged over five trials of 300 problems across nine languages. Opus 4.6 was used as the advisor model in all runs.
2. **BrowseComp:** All runs used thinking turned off with web search and web fetch tools. Sonnet 4.6 runs used medium effort. Sonnet 4.6 + Advisor used our suggested system prompt for coding; Haiku 4.5 + Advisor did not. No programmatic tool calling or context compaction. Scores are based on 1,266 problems with one attempt per problem. Opus 4.6 was used as the advisor model in all runs.**‍**
3. **Terminal-Bench 2.0:** All runs used thinking turned off with bash and file editing tools. Sonnet 4.6 runs used medium effort. Neither advisor run used our suggested system prompt for coding. Each task ran in an isolated pod with 3x resource allocation and a 1x timeout. Scores are averaged over five attempts per task across 89 tasks. Opus 4.6 was used as the advisor model in all runs.

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
