<!-- source: https://academy.claude.com/courses/claude-platform-101/what-are-managed-agents -->

Lesson 11 of 13 · Claude Platform 101What are managed agents?

3. /[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

# What are managed agents?

Lesson 117 min

What are managed agents?

**Claude Managed Agents** is a suite of APIs for building and deploying
agents at scale. You define agents with specific tools, personas, and
capabilities. You configure sandbox environments with the right packages and
network controls. Then you fire off sessions from your own application, and
Claude does the work inside an isolated container with full file system
access, bash execution, and web search.

## The agent loop, hosted for you

Under the hood, this is an **agent loop**: Claude reasons, calls a tool, reads the result, and repeats until the job is done. If you've built agents before, you've probably written this kind of loop yourself. Managed agents takes that same loop and hosts it on Anthropic's infrastructure, so you don't have to run it.

You'll find Managed Agents in its own section of the Claude Console.

The best way to understand what this unlocks is to walk through a few examples.

## Example 1: A Kanban board that does the work

Picture a Kanban board sitting on top of managed agents. You drag a ticket into the "in progress" column, and that fires off a **session** automatically. Say the ticket reads "optimize website performance." Here's what happens:

1. Your back end creates a session.
2. The session points to an **environment** you configured with Lighthouse and Puppeteer pre-installed.
3. Your GitHub repo gets mounted into the container.

Now Claude has the codebase, the tools, and a **rubric** that defines what done looks like:

* Lighthouse score above 90
* No render-blocking resources
* All images lazy loaded

Claude runs the audit, then starts compressing images, inlining CSS, and deferring scripts. Every tool call streams back to the board in real time through the **event stream**, so you can watch the work as it happens.

Then the rubric kicks in. A separate **grader**, running in its own context window, evaluates the output against your criteria. Claude reads that feedback, goes back in, fixes what it missed, and resubmits. In the demo, that loop takes the Lighthouse score up to 96.

One more thing: you can drag a second ticket over while the first is still running. Two sessions, two containers, two separate tasks running in parallel.

![A Kanban development board with two tickets in the In Progress column, each running its own agent session and streaming tool call events](https://academy.claude.com/assets/media/f2c489c96e8b17d074b04f4c24dfd19f290ec665bdcb5bfae3b3ea253edbf802.png)

## Example 2: A recurring research agent with memory

Here's a different shape of agent: one whose job is to track prices and plan changes across every SaaS tool your company pays for, with a report ready before stand-up.

![The Pricing Research app with a Run Weekly Report button, an empty agent activity feed, a memory panel, and a deliverables list with an Excel report and executive summary](https://academy.claude.com/assets/media/682c8b1726cb7c24d8b52430bb9e77c013fd6d6fe23ee144be57426fe75c83aa.png)

On each run, the agent:

* Searches the web for current pricing pages, checks for plan tier changes, and flags new features that might affect your contracts
* Runs a cost analysis in Python inside the sandbox
* Uses an Excel spreadsheet skill and writes an executive summary
* Posts a link to Slack and creates a review task in Asana, both through **MCP servers**

The agent also reads from and writes to a **memory store**. Before it starts, it checks what it found last week. After it finishes, it stores what changed. So next Monday's report can say "compute costs are 15% lower since last week" instead of listing the same static pricing data every time.

![The memory panel listing last week's findings, including vendor pricing changes and a total monthly spend estimate the agent stored for its next run](https://academy.claude.com/assets/media/86b9b49f11ba4c0946dd95218cd5c7b5daaad4a0fada12b9a8709b258df6bfb3.png)

## Example 3: Incident response with multiple agents

Now imagine an alert fires from your monitoring stack. A **custom tool** on your back end receives the alert payload and sends it into a new session as a tool result. This session uses **multi-agent coordination**:

* A **coordinator agent** receives the alert and delegates to three specialists.
* Each specialist runs in its own context window on the same shared file system.
* The specialists report back, and the coordinator synthesizes their findings into a single incident summary.

![An incident response dashboard for an API latency spike alert, with Diagnostics, Log Analysis, and Communications specialist panels pending while a Past Incidents panel searches memory for patterns](https://academy.claude.com/assets/media/3b13fbf85dfdb9de7661bacdcf8972dfe939bc9953b06563d22dcf72a4aff403.png)

Before the summary goes to Slack, the **permissions policy** fires. You see the draft on screen, approve it, and the message goes out. Sensitive actions wait for a human.

Memory ties all of this together. The coordinator checks past incidents in the memory store and flags a pattern: "this looks like the DNS resolution issue from two weeks ago that was caused by a misconfigured TTL." The next time a similar alert fires, the agent starts with that context instead of diagnosing from scratch.

## The building blocks

Across these examples, managed agents gives developers the tools to deliver a fully managed, stateful agent experience built on:

* **Agents** — definitions with specific tools, personas, and capabilities
* **Sessions** — individual runs you fire off from your own application
* **Environments** — sandboxes with the right packages and network controls
* **Tools** — including custom tools on your back end
* **MCP** — connections to services like Slack and Asana
* **Memory** — a store the agent reads before starting and writes to when done
* **Outcomes** — rubrics and graders that define and check what done looks like
* **Multi-agent coordination** — coordinators delegating to specialists

## Recap

* **Claude Managed Agents** is a suite of APIs for building and deploying agents at scale, hosted on Anthropic's infrastructure.
* It runs the familiar agent loop — reason, call a tool, read the result, repeat — inside an isolated container with file system access, bash execution, and web search.
* Sessions run in environments you configure, work in parallel, and stream tool calls back to your app in real time.
* Rubrics and separate graders let you define success criteria; Claude iterates until it meets them.
* Memory, MCP servers, custom tools, permissions policies, and multi-agent coordination round out the stateful agent experience.
* You define what done looks like. Claude works until it gets there.

[Previous lessonContext management](https://academy.claude.com/courses/claude-platform-101/context-management)[Next lessonBuilding your first managed agent](https://academy.claude.com/courses/claude-platform-101/building-your-first-managed-agent)

Lesson 11 of 13 · Claude Platform 101What are managed agents?

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

* [The agent loop, hosted for you](#the-agent-loop-hosted-for-you)
* [Example 1: A Kanban board that does the work](#example-1-a-kanban-board-that-does-the-work)
* [Example 2: A recurring research agent with memory](#example-2-a-recurring-research-agent-with-memory)
* [Example 3: Incident response with multiple agents](#example-3-incident-response-with-multiple-agents)
* [The building blocks](#the-building-blocks)
* [Recap](#recap)
