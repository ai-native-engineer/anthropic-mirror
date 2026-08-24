<!-- source: https://academy.claude.com/courses/claude-platform-101/what-is-thinking -->

Lesson 6 of 13 · Claude Platform 101What is thinking?

3. /[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

# What is thinking?

Lesson 65 min

What is thinking?

Some tasks need more than a quick answer. Claude can work through a problem
before responding — a feature called **extended thinking**. In this lesson,
we'll look at what thinking is, how it works, and when it actually
helps.

Here's the failure mode we're trying to avoid. Ask a model a multi-step question and have it answer immediately, and it can confidently get it wrong:

![Diagram of an app sending a multi-step apples question to a model, which immediately replies with the wrong answer: you'd have 6.5 apples](https://academy.claude.com/assets/media/f5d4c633d434b2972169941e685cd3c1a049b9db48c4126de844bb8490389065.png)

## What is extended thinking?

Extended thinking lets Claude reason step by step before producing a final response. When it's enabled, Claude generates internal reasoning tokens — often called a **chain of thought** — and then delivers the answer. The reasoning isn't hidden: you can see it in the response alongside the final text.

## Adaptive thinking on Claude Opus 5

On Opus 5, thinking is **adaptive** and on by default. There's no token budget to pick: Claude decides dynamically when to think and how much.

To control how much Claude thinks, use the **effort** parameter. One gotcha: it goes inside `output_config`, not next to the `thinking` block. The levels are:

* `low`
* `medium`
* `high` (the default)
* `xhigh` (extra high)
* `max`

## When to use it (and when to skip it)

Extended thinking helps with:

* Math and multi-step logic
* Code debugging
* Regulatory analysis
* Anything that involves trade-offs or comparing options

![Slide showing extended thinking use cases: math, multi-step logic, code debugging, regulatory analysis, and complex comparisons](https://academy.claude.com/assets/media/b6dff79101adfefbcca44c884b9b18a8a19e987a67cf5376756e35160d69ef53.png)

Skip it for simple classification, extraction, or boilerplate. For those tasks it just adds latency and cost without actually improving the results.

## Thinking in action

Let's see it work. Here's an agent loop with one weather tool, and we'll ask Claude to plan a road trip out of San Francisco — two stops, weighing weather and drive time. That's a real trade-off, the kind of question where thinking earns its keep.

python

```
import anthropic

client = anthropic.Anthropic()

weather_tool = {
    "name": "get_weather",
    "description": "Get the current weather for a city.",
    "input_schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "City name"}
        },
        "required": ["city"],
    },
}

response = client.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    thinking={"type": "adaptive", "display": "summarized"},  # summarized = return the reasoning text
    output_config={"effort": "high"},  # low | medium | high | xhigh | max
    tools=[weather_tool],
    messages=[
        {
            "role": "user",
            "content": "Plan a road trip out of San Francisco with two stops, "
                       "weighing weather and drive time.",
        }
    ],
)
```

When you run this, the output is more interesting than usual. You'll see **thinking blocks** where Claude works through the trade-offs, followed by tool calls to check each city, and finally a text block with the actual recommendation.

The reasoning is visible — that's the whole point.

## Why this matters in production

In a production app, this is the difference between an agent that finds problems one at a time and an agent that connects them. Take a compliance review app: toggling adaptive thinking on the auto-review call lets the agent reason *across* report sections — catching things like a wind load spec in section three that conflicts with the material spec elsewhere in the document.

![Compliance review app UI with a Thorough review checkbox enabled, running an auto-review that cross-references findings between report sections](https://academy.claude.com/assets/media/965c3809645179776a2e75d93d26acd5a60a03496c55ce3c69418090f3728b8d.png)

## Recap

* **Extended thinking** gives Claude room to reason before it answers, and the reasoning is visible in the response.
* On Opus 5, adaptive thinking is on by default — no token budget needed. Add `"display": "summarized"` to see the reasoning in the response.
* Dial the depth with the **effort** parameter inside `output_config`: `low`, `medium`, `high` (default), `xhigh`, or `max`.
* Use it for hard, trade-off-heavy problems. Skip it for simple ones — there it just costs latency and tokens.

[Previous lessonWhat is tool use?](https://academy.claude.com/courses/claude-platform-101/what-is-tool-use)[Next lessonBuilt-in tools](https://academy.claude.com/courses/claude-platform-101/built-in-tools)

Lesson 6 of 13 · Claude Platform 101What is thinking?

What is the Claude Platform?

* [What is the Claude Platform?](https://academy.claude.com/courses/claude-platform-101/what-is-the-claude-platform)
* [Your first API call](https://academy.claude.com/courses/claude-platform-101/your-first-api-call)
* [Choosing the right model](https://academy.claude.com/courses/claude-platform-101/choosing-the-right-model)

Teaching your agent

* [The agent loop explained](https://academy.claude.com/courses/claude-platform-101/the-agent-loop-explained)
* [What is tool use?](https://academy.claude.com/courses/claude-platform-101/what-is-tool-use)
* [What is thinking?](https://academy.claude.com/courses/claude-platform-101/what-is-thinking)

Extending your agent

* [Built-in tools](https://academy.claude.com/courses/claude-platform-101/built-in-tools)
* [Skills](https://academy.claude.com/courses/claude-platform-101/skills)
* [MCP](https://academy.claude.com/courses/claude-platform-101/mcp)
* [Context management](https://academy.claude.com/courses/claude-platform-101/context-management)

Managed Agents

* [What are managed agents?](https://academy.claude.com/courses/claude-platform-101/what-are-managed-agents)
* [Building your first managed agent](https://academy.claude.com/courses/claude-platform-101/building-your-first-managed-agent)

Building with Claude Code

* [Building with Claude Code](https://academy.claude.com/courses/claude-platform-101/building-with-claude-code)

Quiz

* [Claude Platform 101 quizQuiz](https://academy.claude.com/courses/claude-platform-101/claude-platform-101-quiz)

* [Completion badge](https://academy.claude.com/courses/claude-platform-101/badge)

* [What is extended thinking?](#what-is-extended-thinking)
* [Adaptive thinking on Claude Opus 5](#adaptive-thinking-on-claude-opus-5)
* [When to use it (and when to skip it)](#when-to-use-it-and-when-to-skip-it)
* [Thinking in action](#thinking-in-action)
* [Why this matters in production](#why-this-matters-in-production)
* [Recap](#recap)
