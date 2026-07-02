<!-- https://anthropic-partners.skilljar.com/partner-basecamp/464539 -->
<!-- scorm-content: https://anthropic-partners.skilljar.com/content/wp/4hdejjwplbrm/24n24awq8yvf4/module-06-agent-sdk.html -->

# Agent SDK

Module 6 of 6

# The Claude *Agent SDK*

You know how to prompt Claude and chain calls. This module shows you how to build autonomous systems that gather context, act with tools, and verify their own work.

Partner Basecamp
~20 min
SET B - DAY 2 PREP
2 practice scenarios

What you'll be able to do

## Three things that change how you build with Claude

01

Know when a task needs an agent, when it doesn't, and why that decision is the most consequential one you'll make.

02

Navigate the SDK's two interfaces, nine built-in tools, and 1M context window without burning resources or hitting walls.

03

Design agents that are safe to run in production, with sessions, permission modes, hooks, and structured output that feeds your pipeline directly.

Agent or not?

## The first decision: make it before you write a line of code

The most expensive mistake in agent development is building one for a task that didn't need it. Agents add latency, token cost, and debugging complexity. They earn their place only when the task genuinely demands autonomy.

Use an agent when

* The task is multi-step and can't be fully specified up front
* It requires tools that adapt to what they find in the environment
* Real-time decision-making depends on intermediate results
* The simple approach keeps failing in interesting ways

Skip the agent when

* You're doing template-based generation with known inputs
* The sequence of steps is fully deterministic and fixed
* A well-crafted prompt handles it in 200 milliseconds
* You can fully specify the output format in advance

"Start with the simplest approach that works. You'll know when it's not enough."

The agent loop

## Gather, Act, Verify: the cycle behind every agent

Every agent in the Claude SDK runs the same cycle. It gathers context from its environment using tools. It acts on what it finds. It verifies the result against the goal. Then it decides whether it's done, or starts the loop again.

Phase 1

Gather

Read
Glob
Grep
WebFetch

Phase 2

Act

Write
Edit
Bash
Task

Phase 3

Verify

Read
Bash
Grep

Tools are the agent's hands. Each of the nine built-in tools returns structured results with a predictable token cost. The agent doesn't guess what's in the environment. It asks a targeted question and updates its model of the world based on what comes back. That's what separates an agent from a script.

Two interfaces

## query() or session: this is a decision, not a default

One-shot

query()

Stateless
Fresh context each call

Each call starts from scratch. No memory of prior tool calls, prior context, or prior results. The next invocation knows nothing about this one.

Best for

* CI pipelines and automated batch jobs
* Cron scripts where each run is independent
* Single-shot, stateless automation

Conversational

ClaudeSDKClient

Stateful
Context builds across turns

Context accumulates. The agent carries what it learned in one turn into the next. Follow-up requests don't repeat work that's already been done.

Best for

* Multi-turn debugging and iterative refinement
* Complex tasks where follow-ups build on earlier results
* Interactive workflows with human feedback loops

# query(): starts fresh every time
query("Fix the auth bug in login")
→ Bash("ls -la src/") # again, never saw this before
→ Read("src/index.ts") # again
→ 5 tool calls total
# ClaudeSDKClient: carries context forward
session.send("Fix the auth bug in login")
→ # Already know the structure from last turn
→ Read("src/routes/auth.ts")
→ 2 tool calls total

If the next step depends on what the current step learned, use a session. If each invocation is independent, query() is cheaper and simpler.

Now that you understand when to use agents and how the two main interfaces work, here's the full landscape of what the SDK gives you.

SDK capability map

## Six groups. The full surface area.

Before going deep on any single feature, here's the complete map. Each group gets its own treatment in the screens ahead.

Tools

9 built-in: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch, Task. Structured results with predictable token cost.

Context

1M window with auto-compaction at 80%. Managed via selective tool registration (you choose which tools are available at runtime) and the CLAUDE.md project config file.

Integration

MCP servers via stdio or HTTP/SSE. Custom tool registration for any external service without an MCP server.

State

Sessions persist context across requests. Resumption from crash checkpoints. Session forking for parallel strategy exploration.

Safety

Permission modes and pre/post execution hooks on every tool call. Sandboxing isolates destructive operations from the host.

Output

Structured output schemas enforce typed, consistent response formats. Agent responses come back as parseable objects, not prose.

Context window

## 1M tokens. Use them with intention.

Before your agent runs a single tool, roughly 25K tokens are already used: system prompt, CLAUDE.md, tool definitions, conversation history. What remains is yours to spend wisely or burn through quickly.

Naive agent
Optimized agent

Sys

MD

Tool results

Free (~117K)

58K

tokens used on tool results

71%

of window consumed, near compaction threshold

**What happened**
The agent ran Bash to dump full test output (12K tokens), Read an entire compiled bundle instead of the source file (18K tokens), and used cat to inspect package.json when Glob would have found the relevant field in 200 tokens. Auto-compaction triggers at 80%. This agent is almost there after four calls.

Sys

MD

Results

Free (~87%)

11.5K

tokens used on tool results

87%

of window still free after same task

**What changed**
The optimized agent used Glob to find the file list (240 tokens), Grep to search for the relevant pattern (800 tokens), and Read with a line range to pull only what it needed (1,100 tokens). Same task. Five times the remaining headroom. The rule: never use Bash when a structured tool will do.

MCP connections

## Connecting external services: three ways in

Nine built-in tools handle local file and system operations. For everything else, MCP servers connect your agent to external services without custom API code. Pick the connection pattern that fits where your service lives.

stdio
HTTP / SSE
SDK built-in

{ "mcpServers": { "local-db": {
"command": "python",
"args": ["mcp\_server.py"],
"env": { "DB\_PATH": "./data.db" }
} } }

Use for

Local processes running on the same machine: database CLIs, local code analysis tools, any service you spin up with a command. The SDK launches the process and communicates over stdin/stdout.

{ "mcpServers": { "github": {
"type": "sse",
"url": "https://mcp.github.com/sse"
} } }

Use for

Hosted remote services: GitHub, Postgres, internal APIs, any service with an MCP server endpoint. Tool calls go over HTTP. Results stream back via Server-Sent Events. Fully transparent to the agent.

agent.enable\_mcp("github", api\_key="...")

Use for

The simplest path to well-supported services. One line. The SDK handles all connection plumbing, authentication, and tool registration. Start here if the service is supported.

Tool naming convention

MCP tools appear as mcp\_\_server\_\_tool\_name, for example mcp\_\_github\_\_list\_repos. The double-underscore prefix tells you immediately which tools are built-in and which come from an MCP server. Crucial when reading a long tool call trace and trying to figure out what went wrong.

Subagent patterns

## Parallel power, three things to get right

Subagents let your parent agent spawn specialized workers that run in parallel. Code review, test runner, and documentation checker running simultaneously, with results merged at the parent. The power is real. So are the failure modes.

01

Context Isolation

Each subagent gets a fresh 1M window. It does not see the parent's history. Write self-contained prompts.

02

Token Budgets

Three subagents = three times the token cost. Use parallelism for tasks that genuinely benefit from it, not just decomposition.

03

Failure Handling

Design for one subagent failing. The others should complete. The parent decides to retry, skip, or escalate.

Scenario

Your parent agent has spent 20 minutes building deep context about a client's codebase. You now want to spawn a subagent to write technical documentation for the authentication module. What does the subagent have access to when it starts?

A

The parent's full accumulated context. The subagent picks up where the parent left off and already knows the codebase.



B

Only the prompt you write for it. It starts with a fresh 1M window and nothing else.



C

A compressed summary the SDK automatically generates from the parent's session history.

Not quite

The parent's context does not carry over to subagents. Each subagent gets a fresh 1M window with nothing in it except the prompt you provide. This is the detail that catches teams off guard most often.

Correct

Context isolation is the most important thing to understand about subagents. Every subagent starts from scratch. The practical implication: every subagent prompt must be fully self-contained, including all relevant context the subagent needs to do its job.

Not quite

The SDK doesn't auto-generate context summaries for subagents. You're fully responsible for what goes into the subagent's prompt. There is no automatic handoff from parent to child.

Sessions and state

## In production, state is infrastructure

Agents run for minutes or hours in production. Sessions, resumption, and forking are how you keep long-running agents reliable, recoverable, and worth experimenting with.

Sessions

Context accumulates across turns. The agent builds a model of what it's working on and carries it forward. This is the ClaudeSDKClient interface in a production context: each turn builds on the last rather than starting from scratch.

Resumption

A 45-minute codebase analysis crashes at minute 43 due to a network blip. Without checkpoints, you start over. With resumption, you reload from the last checkpoint and pick up where you left off. Build this in from the start for any task that runs longer than five minutes. It is not optional for serious production work.

Forking

You are 15 minutes into an agent run with rich accumulated context. You want to try two approaches to the next phase. Fork the session. Both forks start with identical context and explore independently. Compare results, pick the winner.

fork\_a = client.fork(session\_id="sess\_abc123")
fork\_b = client.fork(session\_id="sess\_abc123")
result\_a = fork\_a.send("Approach A: refactor in place")
result\_b = fork\_b.send("Approach B: rewrite from scratch")
# Both start with identical context, diverge independently

Safety as architecture

## Permissions and hooks are load-bearing walls

Safety controls are not features you add before going to production. They are structural decisions you make at the start. Retroactively adding them is the hardest way to do it.

Default

Prompts the user when a tool call looks destructive: file overwrites, rm commands, sudo calls. Human stays in the loop on anything risky.

Recommended for dev

Accept Edits

Requires explicit confirmation for anything destructive. The agent stops and waits. Nothing irreversible happens without a human decision.

High-stakes environments

Bypass

No prompting. The agent runs fully autonomously. Use only in automated pipelines where no human can intervene. Document why you chose it.

Automated pipelines only

PreToolUse

Inspect args. Block patterns. Add logging.

→

Execute

Runs in sandbox. Isolated from host.

→

PostToolUse

Log result. Redact sensitive data. Transform output.

→

Agent

Sees the filtered result and continues reasoning.

Permission modes and hooks compose. You can run Accept Edits mode and have a PreToolUse hook that blocks `rm -rf` patterns simultaneously. They are not a choice between two approaches. They are layers of defense designed to be used together.

Configure and consume

## CLAUDE.md and structured output: set it once, apply it everywhere

Two features that change the quality of what your agent does and what you can do with its output.

Project config

CLAUDE.md

A plain text file in your project root. Every rule you put in it fires on every agent turn, automatically, without being re-stated in the prompt. Think of it as a behavioral contract.

# Project: payments-api
# Stack: Python 3.11, FastAPI, SQLAlchemy
Never use raw SQL. Use SQLAlchemy ORM.
All endpoints require auth middleware.
Run pytest before every commit.

Token cost: ~1,850 tokens for a 3-rule file. Worth it for the behavioral consistency every agent turn receives.

Typed responses

Structured Output

Define a JSON schema and the agent's response conforms to it. Risk level becomes an enum field, not a sentence buried in a paragraph. Agents become first-class data pipeline citizens.

{
"summary": "string",
"risk\_level": "low | medium | high",
"actions": ["array of strings"],
"confidence": 0.0 – 1.0
}

You don't want to parse a paragraph to find the risk level. You want `risk_level: "high"` in a typed field your application can act on directly.

Three principles

## What will serve you in every agent system you build

1

Simplicity Wins

Tap to reveal

The most impressive thing you can build is a system that solves the problem reliably. A well-prompted model with targeted tool use will outperform an over-engineered orchestration system in speed, cost, and debuggability. Start with the simplest approach that works. You will know when it is not enough because the simple approach will start failing in interesting ways that only an agent can handle.

2

Compose, Don't Stack

Tap to reveal

The SDK gives you orchestration, subagents, parallelization, sessions, hooks, and MCP. These are composable primitives. The best agents combine two or three of these patterns well, not all of them at once. More patterns mean more surface area for things to go wrong. Pick the patterns that fit the problem. Resist the instinct to use everything available.

3

Safety Is Architecture

Tap to reveal

Permissions, sandboxing, and hooks are not things you bolt on before going to production. They are load-bearing walls. Design for control from the start. Every destructive tool call should flow through a hook. Every subagent should have a defined scope. Every agent should have a permission mode appropriate to its autonomy level. If you are doing this work after the agent is built, you are doing it in the hardest possible order.

Reveal all three to continue

Module 6 of 6 Complete

## Build agents that think. *Design ones that last.*

You have covered the full Claude Agent SDK, from the decision to use an agent at all, through two interfaces, nine tools, context management, MCP connections, subagent patterns, sessions, safety controls, and structured output. The **technical knowledge** is here. The **design discipline** is what separates agents that work in a demo from ones that run reliably in production.

You're ready for Day 2

Bring this to the Basecamp sessions

The facilitated sessions build directly on what you have covered across all six modules. Come with questions about the tools and constraints that matter most to your clients' environments.

Mark all pre-work for Day 2 Complete



Begin
