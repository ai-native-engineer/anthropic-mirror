<!-- source: https://academy.claude.com/courses/claude-platform-101/built-in-tools -->

Lesson 7 of 13 · Claude Platform 101Built-in tools

3. /[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

# Built-in tools

Lesson 76 min

Built-in tools

You can build your own custom tools, but some capabilities are common enough
that Anthropic ships them pre-built. You don't write the code. You don't
host the sandbox. You just declare the tool, and Anthropic runs it.

## Server tools: declared by you, run by Anthropic[](#server-tools-declared-by-you-run-by-anthropic)

Anthropic provides **server tools** that run on their infrastructure. You don't execute these — Anthropic does. That means you don't need an agent loop for these calls. Claude calls the tools on its own, and the result comes back inside the same response.

The main ones are:

* **Web search** — searches the internet and returns results with citations
* **Code execution** — writes and runs Python in a sandbox
* **Web fetch** — retrieves full content from URLs

## Two server tools in one file[](#two-server-tools-in-one-file)

Let's check out some of the big ones in one file: two `messages.create` calls, one with web search and one with code execution.

python

```
import anthropic

client = anthropic.Anthropic()

# Call 1: web search — Anthropic runs the search server-side
search_response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    tools=[{"type": "web_search_20260209", "name": "web_search"}],
    messages=[
        {"role": "user", "content": "What is Anthropic's latest model release? Answer in one sentence."}
    ],
)

for block in search_response.content:
    if block.type == "server_tool_use":
        print(f"Tool call: {block.name} — {block.input}")
    elif block.type == "text":
        print(block.text)

# Call 2: code execution — Claude writes and runs Python in a sandbox
code_response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    tools=[{"type": "code_execution_20260120", "name": "code_execution"}],
    messages=[
        {"role": "user", "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"}
    ],
)

for block in code_response.content:
    if block.type == "server_tool_use":
        print(f"Tool call: {block.name} — {block.input}")
    elif block.type == "bash_code_execution_tool_result":
        print(f"stdout: {block.content.stdout}")
    elif block.type == "text":
        print(block.text)
```

Two things to notice:

1. **There's no agent loop here.** We don't switch on `stop_reason`. We don't push tool results back. Anthropic runs the tool server-side, and the response already contains the result.
2. **The response has new block types.** A `server_tool_use` block for the tool call, a code execution tool result block for the output, plus the regular `text` blocks.

## Running it[](#running-it)

For web search, you'll see Claude's tool call printed, then a one-sentence answer about the latest model release with the search citations folded in.

For code execution, you'll see the actual Python Claude wrote, the stdout from the sandbox running it, and a final text answer.

We didn't have to spin up a search crawler. We didn't run a Python sandbox. We declared two tools and got both for free.

## The other category: client tools[](#the-other-category-client-tools)

Worth knowing the other category exists. **Client tools** run where your code runs. Anthropic publishes their schemas and trains Claude on them, so you don't have to define the schema yourself. Two examples:

* **Memory** — Claude reads and writes memory across sessions
* **Bash** — a persistent bash shell so Claude can execute commands

![The Anthropic docs table of built-in tools, with memory and bash listed as client tools alongside server tools like web fetch and code execution](https://academy.claude.com/assets/media/e1774053aa114f686c3fd446febc366ccd93ba98b80c25625a8164ac18ddd5fd.png)

They have the same shape as a custom tool, but the SDK gives you the schema and a sensible runner.

## Why this matters in production[](#why-this-matters-in-production)

In a production app, this is the shortest path to features that would otherwise take weeks. Web search can power a fact-check endpoint that verifies every numeric and regulatory claim in a draft against the live web.

![A proposal review app using web search to fact-check the regulatory and numeric claims in a draft proposal](https://academy.claude.com/assets/media/b99c7263b4d1f12e776017eca4f4d3557669c2b0e7a89ad56a84f5a560e845c1.png)

One reminder, though: just because something is validated on the internet doesn't mean it's true. Always double-check Claude's work.

## Recap[](#recap)

* **Server tools** — web search, code execution, web fetch — are declared in your `tools` array. Anthropic runs them.
* You get the result in the same response, with **no agent loop required**. Look for `server_tool_use` and tool result blocks alongside the regular text blocks.
* **Client tools** like memory and bash run where your code runs, but the SDK ships the schema and a runner for you.
* The "hosted by Anthropic" idea scales all the way up: **managed agents** apply it to the entire agent, not just one tool.

[Previous lessonWhat is thinking?](https://academy.claude.com/courses/claude-platform-101/what-is-thinking)[Next lessonSkills](https://academy.claude.com/courses/claude-platform-101/skills)

Lesson 7 of 13 · Claude Platform 101Built-in tools

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

* [Server tools: declared by you, run by Anthropic](#server-tools-declared-by-you-run-by-anthropic)
* [Two server tools in one file](#two-server-tools-in-one-file)
* [Running it](#running-it)
* [The other category: client tools](#the-other-category-client-tools)
* [Why this matters in production](#why-this-matters-in-production)
* [Recap](#recap)
