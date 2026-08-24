<!-- source: https://academy.claude.com/courses/claude-platform-101/building-your-first-managed-agent -->

Lesson 12 of 13 · Claude Platform 101Building your first managed agent

3. /[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

# Building your first managed agent

Lesson 128 min

Building your first managed agent

If you've built an agent loop by hand, you know the drill: while loops, stop
reason switches, tool executions. That works, and for a lot of features it's
actually the right shape. But sometimes that loop is going to run for a very
long time — minutes, maybe even hours — across many tools, with state to
keep, files to write, and work to resume after a network hiccup. At that
point, you don't want to run the loop on your server. You want to delegate
it. That's what **managed agents** are.

## What is a managed agent?

A managed agent is an agent loop that runs on Anthropic's infrastructure instead of yours. You describe the agent once, you give it an environment to work in, and you start a session. Anthropic runs the loop, and you just stream the events back out as it works.

Managed agents are enabled by default for every API account — no special access needed.

## The four primitives

There are four primitives, and they come in order:

1. **Agent** — the persona: model, system prompt, and toolset. This is reusable across many runs.
2. **Environment** — where the agent runs: cloud or self-hosted, networking config, and so on.
3. **Session** — a single run of an agent inside a certain environment. The session is the unit of work.
4. **Events** — the messages flowing in and out: the agent's actions, the tool calls, the results, the replies.

Here's how the pieces fit together: your app talks to a session, the session drives work inside the environment, and everything that happens flows back out through the event stream:

![Architecture diagram showing an agent connected to a Session, which drives an Environment, with results flowing back through an Event Stream to your app](https://academy.claude.com/assets/media/0f28503f2b590760b94b151181e62bda17d55eab4f80a23b512817b07ecf46e3.png)

Notice the shift here: you're not running a while loop. You're sending events and reading events.

## The smallest possible managed agent

Let's build the smallest managed agent that does something useful: create a file in the temp drive, count its lines, and report back.

For tools, we'll use the **agent toolset** — Anthropic's bundled file, bash, and web tools. They work fine for this task, so we don't have to define any tools ourselves.

## Step 1: Create the agent

First, we create the agent. Note the agent toolset defined right in the `tools` array — that's the bundled toolset:

python

```
import anthropic

client = anthropic.Anthropic()

agent = client.beta.agents.create(
    name="Line Counter",
    model="claude-opus-5",
    system="You are a helpful agent that completes small file tasks.",
    tools=[
        {"type": "agent_toolset_20260401", "default_config": {"enabled": True}}
    ],
)
```

Remember: the agent is reusable. Create it once and run it across many sessions.

## Step 2: Create the environment

Next, the environment. This spins up the container template — cloud, with unrestricted networking. This is the sandbox where the file actually gets written:

python

```
environment = client.beta.environments.create(
    name="line-counter-env",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)
```

## Step 3: Create the session

Then we create a session with our agent and environment, plus an optional title. The session is the unit of work:

python

```
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Count lines demo",
)
```

## Step 4: Open the stream, then send the kickoff

Now we open the event stream — and notice that we do this **first**. The stream only delivers events that occur after it opens, so always open it before sending the kickoff message. Then we send the user message into the live stream:

python

```
with client.beta.sessions.events.stream(session_id=session.id) as stream:
    # Stream is open — now send the kickoff
    client.beta.sessions.events.send(
        session_id=session.id,
        events=[
            {
                "type": "user.message",
                "content": [
                    {
                        "type": "text",
                        "text": "Create a file in the temp directory, "
                                "count its lines, and report back.",
                    }
                ],
            }
        ],
    )
```

Notice it's `events` — plural. Events are how everything flows in this API.

## Step 5: Consume the stream

Finally, we consume the stream. There are three event types that matter for this demo:

* `agent.message` — Claude's text
* `agent.tool_use` — what tool Claude picked
* `session.status_idle` — the agent is done

python

```
    for event in stream:
        if event.type == "agent.message":
            for block in event.content:
                if block.type == "text":
                    print(block.text, end="", flush=True)
        elif event.type == "agent.tool_use":
            print(f"\n[tool] {event.name}")
        elif event.type == "session.status_idle":
            print("\n--- Agent done ---")
            break
```

Run it, and the output is the agent reasoning out loud — actual text, the tools it picks, and a final answer. All of it running inside Anthropic's container, not yours:

![Terminal output of the managed agent run: agent, environment, and session IDs are created, then the event stream shows the agent writing the file, running its tools, and reporting that the file contains 3 lines](https://academy.claude.com/assets/media/03c04c48b719f7af90281aa7bbc14d5a79606514b28c3d4febbe5d1366f3e16b.png)

## The trade

Usually with agents, we have our own loop where we have to control everything. With managed agents, you delegate that loop, the sandbox, and the resumability — and just consume the event stream as it comes in.

In a production app, this is the shape for long-running, file-touching, "go organize this for me" tasks. Picture a file share cleanup: a managed agent reads a target directory structure spec, walks the messy incoming folder, moves files into the right project folders, archives duplicates and zero-byte garbage, and flags anything it can't confidently place — all in a session that can run for minutes against thousands of files. Here's what that looks like in a real app — a fileshare cleanup dashboard streaming the agent's activity live as it sorts, archives, and flags files:

![A fileshare cleanup web app powered by a managed agent, showing the folder tree being organized alongside a live activity feed of the agent's events as it moves and archives files](https://academy.claude.com/assets/media/95406d68d7a048f36b750fa6fee3665efe4c6bed6b909eb1d6549b584794e5dd.png)

## Recap

* **Managed agents are the agent loop, run for you** — on Anthropic's infrastructure instead of your server.
* The flow is: **create an agent, create an environment, create a session, send events in, and stream events out**.
* The **agent** (model, system prompt, toolset) is reusable across runs; the **session** is a single run; **events** are how everything flows.
* Open the event stream **before** sending your kickoff message — it only delivers events that occur after it opens.
* Watch for three events: `agent.message` (text), `agent.tool_use` (tool picks), and `session.status_idle` (done).
* Reach for managed agents when the loop would run too long, do too much, or need to survive a hiccup. Reach for a manual loop when you want full control.

[Previous lessonWhat are managed agents?](https://academy.claude.com/courses/claude-platform-101/what-are-managed-agents)[Next lessonBuilding with Claude Code](https://academy.claude.com/courses/claude-platform-101/building-with-claude-code)

Lesson 12 of 13 · Claude Platform 101Building your first managed agent

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

* [What is a managed agent?](#what-is-a-managed-agent)
* [The four primitives](#the-four-primitives)
* [The smallest possible managed agent](#the-smallest-possible-managed-agent)
* [Step 1: Create the agent](#step-1-create-the-agent)
* [Step 2: Create the environment](#step-2-create-the-environment)
* [Step 3: Create the session](#step-3-create-the-session)
* [Step 4: Open the stream, then send the kickoff](#step-4-open-the-stream-then-send-the-kickoff)
* [Step 5: Consume the stream](#step-5-consume-the-stream)
* [The trade](#the-trade)
* [Recap](#recap)
