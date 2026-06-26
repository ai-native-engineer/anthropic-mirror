<!-- source: https://claude.com/blog/the-advisor-strategy -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22c7f111435762ad994_1b398dbdfa4995ce5ce943aa87d8b78b2c2ba065-1000x1000.svg)

# The advisor strategy: Give agents an intelligence boost

Pair Opus as an advisor with Sonnet or Haiku as an executor, and get near Opus-level intelligence in your agents at a fraction of the cost.

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

* Date

  April 9, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/the-advisor-strategy

Developers who want to better balance intelligence and cost have converged on what we call the advisor strategy: pair Opus as an advisor with Sonnet or Haiku as an executor. This brings near Opus-level intelligence to your agents while keeping costs near Sonnet levels.

Today we're introducing the advisor tool on the Claude Platform to make the advisor strategy a one-line change in your API call.

## Build cost-effective agents with the advisor strategy

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d7a8216b96ea826922fcf4_e9f8286d.png)

With the advisor strategy, Sonnet or Haiku runs the task end-to-end as the executor, calling tools, reading results, and iterating toward a solution. When the executor hits a decision it can't reasonably solve, it consults Opus for guidance as the advisor. Opus accesses the shared context and returns a plan, a correction, or a stop signal, and the executor resumes. The advisor never calls tools or produces user-facing output, and only provides guidance to the executor.

This inverts a common sub-agent pattern, where a larger orchestrator model decomposes work and delegates to smaller worker models. In the advisor strategy, a smaller, more cost-effective model drives and escalates without decomposition, a worker pool, or orchestration logic. Frontier-level reasoning applies only when the executor needs it, and the rest of the run stays at executor-level cost.

In our evaluations, Sonnet with Opus as an advisor showed a 2.7 percentage point increase on [SWE-bench Multilingual](https://www.swebench.com/multilingual.html)1 over Sonnet alone, while reducing cost per agentic task by 11.9%.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d908f43209164823554d52_Claude-Blog-Advisor-tool-SWE-bench-Multilingual.png)

## **The advisor tool**

We’re bringing the advisor strategy to our API with the [**advisor tool**](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool), a server-side tool which Sonnet and Haiku know to invoke when they need guidance or help with a specific task.

In our evaluations, Sonnet with an Opus advisor improved scores across BrowseComp2 and Terminal-Bench 2.03 benchmarks while costing less per task than Sonnet alone.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d7a8216b96ea826922fcfa_880b9e59.png)

The advisor strategy also works with Haiku as the executor. On BrowseComp, Haiku with an Opus advisor scored 41.2%, more than double its solo score of 19.7%. Haiku with an Opus advisor trails Sonnet solo by 29% in score but costs 85% less per task. The advisor adds cost relative to Haiku alone, but the combined price is still a fraction of what Sonnet costs, making it a strong option for high-volume tasks that require a balance of intelligence and cost.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d7a8216b96ea826922fcfd_ca657f5f.png)

Declareadvisor\_20260301 in your Messages API request, and the model handoff happens inside a single /v1/messages request—no extra round-trips or context management. The executor model decides when to invoke it. When it does, we route the curated context to the advisor model, return the plan, and the executor continues all within the same request.

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

**Pricing**. Advisor tokens are billed at the advisor model's rates; executor tokens are billed at the executor model's rates. Since the advisor only generates a short plan (typically 400-700 text tokens) while the executor handles the full output at its lower rate, the overall cost stays well below running the advisor model end-to-end.  **Built-in cost controls.** Set max\_uses to cap advisor calls per request. Advisor tokens are reported separately in the usage block so you can track spend per tier.

**Works alongside your existing tools.** The advisor tool is just another entry in your Messages API request. Your agent can [search the web](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool), [execute code](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool), and consult Opus in the same loop.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f26e70e1444e31742ca027_logo_boltupdatedlogo-light-mode.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f26e76cdf0245458a77c3f_logo_boltupdatedlogo-dark-mode.svg)

“It makes better architectural decisions on complex tasks while adding no overhead on simple ones. The plans and trajectories are night and day different.”

Eric Simmons, CEO and Founder, Bolt

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c33d3cb4813a779adb7133_cs-logo-genspark-light-theme.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c33d3e748405bce1e71684_cs-logo-genspark-dark-theme.svg)

“We saw clear improvements in agent turns, tool calls, and overall score — better than a planning tool we built ourselves.”

Kay Zhu, Cofounder & CTO, Genspark

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ebbdde1a3d17f2d9e91607_eve-light-mode.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ebbde617bb08ba0d0157b8_eve-dark-mode.svg)

“On structured document extraction tasks, the advisor tool enables Haiku 4.5 to dynamically scale intelligence by consulting Opus 4.6 as complexity demands, matching frontier-model quality at 5× lower cost.”

Anuraj Pandey, Machine Learning Engineer, Eve Legal

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Get started

Theadvisor toolis available now in beta natively on the Claude Platform. To get started:

1. Add the beta feature header: anthropic-beta: advisor-tool-2026-03-01
2. Add the advisor\_20260301 to your Messages API request
3. Modify your [system prompt](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#suggested-system-prompt-for-coding-tasks) based on your use case

We recommend running your existing eval suite against Sonnet solo, Sonnet executor with Opus advisor, and Opus solo. Explore the [docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool) to learn more.

## Footnotes

1. **SWE-bench Multilingual:** Sonnet 4.6 solo used adaptive thinking. Sonnet 4.6 + Advisor used our suggested system prompt for coding with thinking turned off. Both runs used high effort with bash and file editing tools. Scores are averaged over five trials of 300 problems across nine languages. Opus 4.6 was used as the advisor model in all runs.
2. **BrowseComp:** All runs used thinking turned off with web search and web fetch tools. Sonnet 4.6 runs used medium effort. Sonnet 4.6 + Advisor used our suggested system prompt for coding; Haiku 4.5 + Advisor did not. No programmatic tool calling or context compaction. Scores are based on 1,266 problems with one attempt per problem. Opus 4.6 was used as the advisor model in all runs.**‍**
3. **Terminal-Bench 2.0:** All runs used thinking turned off with bash and file editing tools. Sonnet 4.6 runs used medium effort. Neither advisor run used our suggested system prompt for coding. Each task ran in an isolated pod with 3x resource allocation and a 1x timeout. Scores are averaged over five attempts per task across 89 tasks. Opus 4.6 was used as the advisor model in all runs.

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Jun 17, 2026

### Secure access to the Claude Platform with Workload Identity Federation

Product announcements

[Secure access to the Claude Platform with Workload Identity Federation](#)Secure access to the Claude Platform with Workload Identity Federation

[Secure access to the Claude Platform with Workload Identity Federation](/blog/workload-identity-federation)Secure access to the Claude Platform with Workload Identity Federation

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

May 7, 2026

### Collaborate with Claude across Excel, PowerPoint, Word and Outlook

Product announcements

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](#) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224ef32980bc807847d_a683fdcfe3e2c7c6532342a0fa4ff789c3fd4852-1000x1000.svg)

May 19, 2026

### New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

Product announcements

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](#)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](/blog/new-in-claude-managed-agents)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Apr 30, 2026

### Claude Security is now in public beta

Product announcements

[Claude Security is now in public beta](#)Claude Security is now in public beta

[Claude Security is now in public beta](/blog/claude-security-public-beta)Claude Security is now in public beta

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Agents

Coding

Productivity
