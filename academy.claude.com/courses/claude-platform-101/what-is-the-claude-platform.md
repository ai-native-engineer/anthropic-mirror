<!-- source: https://academy.claude.com/courses/claude-platform-101/what-is-the-claude-platform -->

Lesson 1 of 13 · Claude Platform 101What is the Claude Platform?

3. /[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

# What is the Claude Platform?

Lesson 16 min

What is the Claude Platform?

The **Claude Platform** is Anthropic's infrastructure for building with
Claude programmatically. Instead of chatting with Claude in a browser, you
send structured requests from your code and get structured responses back,
with control over every detail: which model to use, how many tokens to
spend, what tools Claude can use, and what system instructions it follows.

Concretely, the platform is made up of a few pieces:

* A **REST API** you can call from any language
* **SDKs** for different programming languages
* **Command line interfaces**
* A **console** where you manage API keys, monitor usage, deploy managed agents, and test prompts

## The three layers of the platform

A useful way to picture the platform is as three layers stacked on top of each other.

1. **Primitives** — the API building blocks tuned to Claude. This is the Messages API, tool use, files, web search, code execution, MCP servers, and skills. These are the pieces you actually call from your code.
2. **Infrastructure** — what you need to build and scale agentic systems past a prototype. Managed agents, retries, queues, observability — the plumbing that keeps things running when one Claude call becomes a thousand.
3. **Controls** — the tools for running those systems in production, like dashboards and evals. These are the dials your team uses once it's live.

![Diagram of the Claude Platform's three layers: Primitives (Messages API, tool use, files, web search, code execution, MCP), Infrastructure (managed agents, retries, queues, observability, prompt caching, memory), and Controls (dashboards, evaluations, workspaces, usage and spend limits, request logs)](https://academy.claude.com/assets/media/c0b387c11cfeb9623b40a5f857693c4bf88212403b7307cba592b040a3d351a6.png)

The shorthand: **build with primitives, scale on infrastructure, run with control.**

You can see this structure reflected in the Claude Console itself — it's where the infrastructure and control layers live, with sections for building, managing agents, and analytics.

## A real example: drafting help desk replies

Say you manage a basic help desk app, and you've been asked to add a feature: draft a reply based on the contents of a ticket, following your team's tone and guidelines. You want to wire this up to a button in the UI.

![A help desk app showing an open support ticket about a duplicate charge, with a Draft reply with Claude button above an empty reply box](https://academy.claude.com/assets/media/95d639f351882b6778e264a898638447582768595d77be27fa478e7f80e8a611.png)

This is a perfect use case for the **Messages API**. The flow looks like this:

1. Define a client
2. Retrieve the ticket the chat refers to
3. Call `messages.create`
4. Return the response to the button to render

python

```
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-haiku-4-5",   # Haiku: a good fit for a simple drafting task
    max_tokens=1024,
    system=TONE_AND_GUIDELINES,
    messages=[
        {"role": "user", "content": ticket_content}
    ],
)

draft = response.content
```

Each parameter does a specific job:

* **model** — which model handles the request. Here that's **Haiku**, since drafting a reply is a simple task.
* **max\_tokens** — caps how long Claude's response can be.
* **system** — the system prompt, where you define the role Claude plays. The relevant tone and guidelines go here.
* **messages** — an array of objects. The `user` role tells Claude this is user input; the ticket content goes there.

Then you retrieve the response and return it to the button to render. Done.

![The help desk app's reply box populated with a Claude-drafted refund response, with Discard and Send reply buttons and a note to review and edit before sending](https://academy.claude.com/assets/media/0d0ae20981f7f5d29a69c70fc35854a5063c0c58eb8f454ac2571eb77ef6e308.png)

## From "ask Claude a question" to "Claude is part of my product"

Notice what happened in that example: you're not building a chatbot from scratch. You're adding Claude into a product that already exists, and the API is how you wire it in.

That's the core idea. The Claude Platform is your API-level access to Claude's models, tools, and infrastructure. It's how you go from *ask Claude a question* to *Claude is part of my product*.

And when your product needs agents, the platform doesn't just hand you the model. With **managed agents**, it runs them for you.

## Recap

* The Claude Platform is Anthropic's infrastructure for building with Claude programmatically: a REST API, SDKs, CLIs, and a console for keys, usage, managed agents, and prompt testing.
* Think of it as three layers: **primitives** (Messages API, tool use, files, web search, code execution, MCP servers, skills), **infrastructure** (managed agents, retries, queues, observability), and **controls** (dashboards, evals).
* The shorthand: build with primitives, scale on infrastructure, run with control.
* A single `messages.create` call gives you full control over the model, response length, system prompt, and user input — enough to wire Claude into an existing feature like drafting help desk replies.
* The platform takes you from asking Claude questions to making Claude part of your product — and with managed agents, it can run your agents for you.

[Next lessonYour first API call](https://academy.claude.com/courses/claude-platform-101/your-first-api-call)

Lesson 1 of 13 · Claude Platform 101What is the Claude Platform?

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

* [The three layers of the platform](#the-three-layers-of-the-platform)
* [A real example: drafting help desk replies](#a-real-example-drafting-help-desk-replies)
* [From "ask Claude a question" to "Claude is part of my product"](#from-ask-claude-a-question-to-claude-is-part-of-my-product)
* [Recap](#recap)
