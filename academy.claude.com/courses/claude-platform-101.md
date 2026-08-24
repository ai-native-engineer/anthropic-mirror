<!-- source: https://academy.claude.com/courses/claude-platform-101 -->

[Courses](https://academy.claude.com/courses)

# Claude Platform 101

This course teaches developers to build on the Claude Platform from the ground up, whether you've made a few API calls or have only used Claude through a chat window.

13 lessons1.5 hr1 quizCompletion badge

[Start course](https://academy.claude.com/courses/claude-platform-101/what-is-the-claude-platform)[Sign in to save progress](https://academy.claude.com/login?returnTo=https%3A%2F%2Facademy.claude.com%2Fcourses%2Fclaude-platform-101)

![](https://academy.claude.com/assets/v1/thumbnail.light-l85piyo4.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-itkqw1mx.png)

13 lessons · 1 quizClaude Platform 101

What you’ll learnBy the end of this course, you’ll be able to

* Send your first API request with messages.create and read the structured response
* Choose the right model for a job (Fable, Opus, Sonnet, or Haiku) by running a simple evaluation and weighing cost and latency
* Build the agent loop by hand, then collapse it with the SDK's Tool Runner once you understand what it does for you
* Give Claude reach through tool use and let it reason through hard problems with extended thinking
* Extend an agent with Anthropic's built-in tools (web search, code execution, web fetch), Skills, and MCP servers
* Keep a long-running agent inside the context window and affordable with the four context-management patterns
* Build a managed agent end to end, consuming the event stream as Anthropic runs the loop and reports back
* Build with the API using Claude Code itself, and review the code an agent writes for you

There's a wide gap between chatting with Claude in a browser tab and building Claude into something you ship. A chat answers a question and the thread ends there. An application sends Claude structured requests, hands it tools, lets it act on real systems, and runs that loop for one user or a million. The Claude Platform exists to close that gap, and it's a different skill from prompting. Getting value out of it means understanding what's in a request, how an agent decides what to do, and where the costs and limits live.

This course teaches developers to build on the Claude Platform from the ground up, whether you've made a few API calls or have only used Claude through a chat window. We start from first principles: what an API request contains, what an agent loop is, how the context window bounds what Claude can see, and how tools and permissions decide what it can do. The techniques later in the course then land as understanding instead of a list of calls to copy.

You'll send your first request and read the response, then choose the right model for a job (Fable, Opus, Sonnet, or Haiku) and weigh the cost-and-latency trade-off on your own examples instead of guessing. From there you'll build the agent loop by hand to see how Claude acts, observes, and decides, then collapse that hand-written loop with the SDK's Tool Runner once you understand what it does for you. You'll give Claude reach through tool use, let it reason through hard problems with extended thinking, and keep spend predictable with workspaces, limits, and the Console Workbench.

The middle of the course extends an agent beyond your own code: Anthropic's built-in tools (web search, code execution, web fetch) that run on Anthropic's infrastructure, Skills that package a procedure once and reuse it across calls, MCP servers that connect Claude to third-party tools without writing a schema, and the context-management patterns that keep a long-running agent inside the window and affordable past turn ten.

The final section hands work off. You'll learn when to run your own loop and when to let Anthropic run a sandboxed, managed agent for you, then build one end to end, consuming the event stream as Anthropic runs the loop and reports back. A standalone lesson shows you how to build with the API using Claude Code itself, which is also why the rest of the course matters: you need to know what good code looks like to review what an agent writes for you. Every lesson ends with a runnable demo, so you finish each one with working code.

## Recommended prerequisites

Comfort reading and writing code in at least one language, plus basic command-line familiarity. The demos use the TypeScript SDK (`@anthropic-ai/sdk`) with Node and npm. You don't need to be a TypeScript expert, but you should be able to follow along and run a script. (The platform also offers a Python SDK; the course examples are in TypeScript.) You'll need a Claude Console account and an API key from platform.claude.com, plus a small amount of prepaid credit to run the examples. You don't need prior experience building with LLMs.

## Who this is for

Developers who've used Claude in a chat window and want to build it into their own applications, whether you're adding AI features to an existing product or prototyping an agent from scratch. If you've sent a handful of API calls but stalled at "how do I make this act on its own" or "how do I connect it to my real systems," this course is the bridge from a single request to a production agent. You don't need prior agent experience; each lesson builds on the one before it.

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
