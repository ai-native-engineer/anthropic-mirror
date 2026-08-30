<!-- source: https://academy.claude.com/courses/claude-platform-101/the-agent-loop-explained -->

Lesson 4 of 13 · Claude Platform 101The agent loop explained

3. /[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

# The agent loop explained

Lesson 47 min

The agent loop explained

You've made API calls, but a single call only returns one response. If you
want to automate a workflow, Claude needs to act, look at the result, decide
what's next, and keep going. That pattern is what people mean when they talk
about **agentic workflows**.

## What an agent actually is[](#what-an-agent-actually-is)

An **agent** is an autonomous version of Claude, running both sides of the messaging loop without a human in the middle. An agent receives a task, picks a tool, and executes code in a loop until Claude decides the task is done.

The easiest way to implement an agent loop looks like this:

1. Send a message to Claude with tools available.
2. Claude responds with either a final answer or a request to use a tool you defined.
3. Your code executes that tool.
4. You send the result back to Claude.
5. Repeat until the **stop reason** is `end_turn`.

Think of it as a conversation where the turns alternate: the user kicks things off, the agent calls a tool, the tool returns a result, and the agent keeps going until it has an answer.

## A minimal working example[](#a-minimal-working-example)

To see this loop run end to end without dragging in a database or a UI, we'll wire up a fake tool called `get_weather` and ask Claude what to wear in Austin today. Claude has no way to know the weather on its own, so it has to call the tool, read the result, and then give you an answer.

Here's the whole script:

python

```
import anthropic

client = anthropic.Anthropic()

# The tools array tells Claude what's available:
# a name, a description, and a JSON schema for the inputs.
tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city to get weather for",
                }
            },
            "required": ["city"],
        },
    }
]

# run_tool is just a hardcoded lookup.
# In a real app, this would hit your database, an API, whatever.
def run_tool(name, tool_input):
    if name == "get_weather":
        return f"Weather in {tool_input['city']}: 95F, sunny"
    raise ValueError(f"Unknown tool: {name}")

messages = [
    {"role": "user", "content": "What should I wear in Austin today?"}
]

# The agent loop. Each iteration sends messages to Claude
# and switches on the response's stop reason.
while True:
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

    if response.stop_reason == "end_turn":
        # Claude is done. Print the final text and break.
        for block in response.content:
            if block.type == "text":
                print(block.text)
        break

    if response.stop_reason == "tool_use":
        # Find the tool use blocks in the response and run each one.
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = run_tool(block.name, block.input)
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    }
                )

        # Push the assistant's response and our tool results
        # back into messages, then loop again so Claude can answer.
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})
```

Three pieces to notice:

* The **tools array** tells Claude what's available: a name, a description, and a JSON schema for the inputs.
* **`run_tool`** is just a hardcoded lookup. In a real app, this would hit your database, an API, whatever.
* The **loop** is the agent loop. Each iteration sends the messages to Claude and switches on the response's stop reason. On `end_turn`, Claude is done — print the final text and break. On `tool_use`, find the tool use blocks, run each one, push the assistant's response and your tool results back into `messages`, and loop again so Claude can answer.

## Running it[](#running-it)

When you run the script, you'll see two turns:

1. **Turn one:** the stop reason is `tool_use`. Claude requests `get_weather` for Austin, and your code returns the temperature and conditions.
2. **Turn two:** the stop reason is `end_turn`, and Claude tells you to wear something light and breathable.

![Terminal output of the agent loop: turn 1 stops with tool_use and calls get_weather for Austin, then turn 2 stops with end_turn and Claude prints its final clothing recommendations](https://academy.claude.com/assets/media/1dde6d32a96f660239deb21494ecb642a61aab5b00043c2ca5c306716c310d80.png)

Two API calls, one tool execution, one final answer. That's the entire loop. Everything you build with the Claude API is going to be similar to this.

## The same loop in production[](#the-same-loop-in-production)

In a real environment, this same loop powers something like an auto-review endpoint: a compliance agent that reads a structural report, looks up the relevant building codes via a tool, and writes risk findings back to the database one by one as it works.

![A compliance review dashboard listing uploaded structural reports, each with a Run auto-review button that kicks off the agent](https://academy.claude.com/assets/media/ec53ce30d18abff70f5ce7722eb3071b8a41b147fc1544cc49756b1bcc3d93df.png)

The shape of the loop is identical to what you just ran. The differences are:

* Real tools instead of a mock weather lookup.
* Results stream back to the UI as server-sent events.
* Findings get persisted to a risk-finding table.

![The review trace of a running compliance agent: dozens of tool calls searching the building-code library and looking up specific code sections as the loop iterates](https://academy.claude.com/assets/media/df29fa081f1dd13a5f5c6882a4a04a2446fb2ac075227a350dac5002345805be.png)

## Recap[](#recap)

* An agent is **Claude in a loop**: observe, decide, act, repeat.
* The loop is simple: send messages with tools, run any tool Claude requests, feed the result back, and stop when the stop reason is `end_turn`.
* **You own the loop and the tools. Claude owns the reasoning.**
* The same loop shape scales from a mock weather demo to a production compliance agent — only the tools and plumbing change.
* When you don't want to own the loop, managed agents run this exact loop for you on Anthropic's infrastructure.

[Previous lessonChoosing the right model](https://academy.claude.com/courses/claude-platform-101/choosing-the-right-model)[Next lessonWhat is tool use?](https://academy.claude.com/courses/claude-platform-101/what-is-tool-use)

Lesson 4 of 13 · Claude Platform 101The agent loop explained

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

* [What an agent actually is](#what-an-agent-actually-is)
* [A minimal working example](#a-minimal-working-example)
* [Running it](#running-it)
* [The same loop in production](#the-same-loop-in-production)
* [Recap](#recap)
