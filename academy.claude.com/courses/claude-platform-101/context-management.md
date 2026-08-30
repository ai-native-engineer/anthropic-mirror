<!-- source: https://academy.claude.com/courses/claude-platform-101/context-management -->

Lesson 10 of 13 · Claude Platform 101Context management

3. /[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

# Context management

Lesson 106 min

Context management

Every request you send Claude has a **context window**. A million tokens
sounds like a lot, but it runs out faster than you think once you're
shipping a real agent. That's where **context management** comes in: it's
how you stay inside the window without losing what matters.

## What counts as context[](#what-counts-as-context)

Context is **everything Claude sees on a given turn**:

* The system prompt
* The message history
* Tool definitions and tool results
* Attached files and skills
* Thinking blocks

![Diagram of the five components of context: system prompt, message history, tools, files and skills, and thinking blocks](https://academy.claude.com/assets/media/0223d85fc703611c0aa3e8bfc1a1d8b6c33b87ba4708d716c89a26487c94f836.png)

It's the input to every single API call. You pay for it on the way in, and you pay for it on the way out. And once the window is full, the request fails.

So the goal isn't to fit everything in. The goal is to **fit the right things in**.

Anthropic publishes **four patterns** for managing context in long-running agents. Three are first-class API features, and one is a design pattern.

![Diagram of the four patterns for managing context: just-in-time context, compaction, caching, and memory](https://academy.claude.com/assets/media/aa9eae1644eab04cb5954503b69a4622a7a21bb6af326f3c4ca0d9aaea86d849.png)

## Pattern 1: Just-in-time context[](#pattern-1-just-in-time-context)

Don't load everything upfront. Load what the agent needs *now*, and let it pull more in via tools when it asks.

Think of a compliance review agent. It doesn't get the entire building code book stuffed into its system prompt — it calls a `lookup_building_code` tool when it needs a specific section. This is the design pattern of the four: nothing special in the API, just a deliberate choice about what you load and when.

## Pattern 2: Server-side compaction[](#pattern-2-server-side-compaction)

When a conversation runs long, Anthropic's **server-side compaction** summarizes old turns into a single block. You opt in by adding a `context_management` key to your request, holding an edit with a type:

python

```
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-5",
    max_tokens=1024,
    context_management={
        "edits": [
            {"type": "compact_20260112"}
        ]
    },
    messages=messages,
)
```

The API auto-summarizes when the input crosses the trigger threshold. You don't have to track conversation length yourself.

## Pattern 3: Prompt caching[](#pattern-3-prompt-caching)

**Prompt caching** lets you mark the stable parts of a request — the system prompt, the tool definitions, a long document — and reuse them across calls at a fraction of the cost.

The math matters more than it looks. If your system prompt is 4,000 tokens and you call it 100 times an hour, caching is the difference between a usable bill and a phone call from finance.

## Pattern 4: The memory tool[](#pattern-4-the-memory-tool)

Some context needs to survive *across sessions*: user preferences, the agent's running notes, what was decided last week. The recommended primitive for this is the **memory tool**.

Here's how it works:

* Claude reads and writes to a memory directory via tool calls.
* You implement the storage backend client-side — a file system, a database, an encrypted store, whatever you want.
* Anthropic auto-injects a system instruction telling Claude to check the memory directory before starting work.

![A memory directory viewed in the browser, with folders for incidents and saas-pricing and a saved incident note from a previous session](https://academy.claude.com/assets/media/151cfe356d66b03d1e13d1f02081c2bcf76d0ab15bb144209018db18b3bc71b8.png)

## Layering the patterns[](#layering-the-patterns)

In a production app, you'll usually layer all four at once. The compliance review agent caches its system prompt and tool definitions, and pulls building code sections in just in time via `lookup_building_code`.

Each pattern handles a different failure mode: **cost**, **window size**, **statelessness**. Pick the ones that match what's breaking for you.

## Recap[](#recap)

* Context is everything Claude sees on a turn — and it isn't free or infinite. Once the window fills, the request fails.
* **Just-in-time context**: load what's needed now, let tools pull in the rest. This is the design pattern of the four.
* **Server-side compaction**: add a `context_management` key, and the API summarizes old turns automatically when input crosses the trigger threshold.
* **Prompt caching**: mark stable parts of the request and reuse them across calls at a fraction of the cost.
* **The memory tool**: Claude reads and writes a memory directory via tool calls; you own the storage backend, so context survives across sessions.
* Four patterns, one goal. Wire them up by hand, or use Claude managed agents, which ship with caching and compaction on by default.

[Previous lessonMCP](https://academy.claude.com/courses/claude-platform-101/mcp)[Next lessonWhat are managed agents?](https://academy.claude.com/courses/claude-platform-101/what-are-managed-agents)

Lesson 10 of 13 · Claude Platform 101Context management

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

* [What counts as context](#what-counts-as-context)
* [Pattern 1: Just-in-time context](#pattern-1-just-in-time-context)
* [Pattern 2: Server-side compaction](#pattern-2-server-side-compaction)
* [Pattern 3: Prompt caching](#pattern-3-prompt-caching)
* [Pattern 4: The memory tool](#pattern-4-the-memory-tool)
* [Layering the patterns](#layering-the-patterns)
* [Recap](#recap)
