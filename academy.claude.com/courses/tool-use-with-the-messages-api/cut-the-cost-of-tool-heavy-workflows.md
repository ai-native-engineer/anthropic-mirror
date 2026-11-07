<!-- source: https://academy.claude.com/courses/tool-use-with-the-messages-api/cut-the-cost-of-tool-heavy-workflows -->

Lesson 8 of 9 · Tool use with the Messages APICut the cost of tool-heavy workflows

3. /[Tool use with the Messages API](https://academy.claude.com/courses/tool-use-with-the-messages-api)

[Tool use with the Messages API](https://academy.claude.com/courses/tool-use-with-the-messages-api)

# Cut the cost of tool-heavy workflows

Lesson 815 min

Cut the cost of tool-heavy workflows

SummaryTranscript

An agent that uses tools sends everything again on every request.
Programmatic tool calling and prompt caching each cut a different part of
its cost.

*The demo in this video was recorded in September 2026. It ran on Claude Sonnet 5 (`claude-sonnet-5`). Results may differ on newer models.*

**An agent that uses tools sends everything again on every request, so its cost grows with each tool call.** Each request carries the tool definitions, the system prompt, the question, and every tool result so far. Those are its input tokens, and each one is billed.

Programmatic tool calling and prompt caching both cut that cost.

Meridian is a fictional engineering consultancy with 40 engineers. Its agent got one question: Which engineers were under 70% utilization in June 2026? The agent had two tools. `list_employees` returns the roster, and `get_employee_hours` returns one engineer's timesheet.

Answering that question took the agent 42 requests and 1,124,799 input tokens. The whole run cost $2.29 in tokens.

## Measure the input tokens in each request[](#measure-the-input-tokens-in-each-request)

**Print `usage.input_tokens` each time a response comes back, because those counts show you where the cost is.**

python

```
resp = client.messages.create(...)
print(resp.usage.input_tokens, "input tokens")
```

Meridian's agent runs a classic loop, where each response asks for one tool call. Here are two of its counts.

| Request | What it carries | Input tokens |
| --- | --- | --- |
| Request 1 | Tool definitions, system prompt, and question | 606 |
| Request 37 | The same, plus 36 earlier tool results | 47,905 |

Request 1 carries only what every request sends. Later requests add tool calls and their results. Compare the two counts to see which part grew.

## Keep tool results out of what Claude reads[](#keep-tool-results-out-of-what-claude-reads)

With [programmatic tool calling(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#how-programmatic-tool-calling-works), Claude writes a script that calls your tools, and the code execution tool runs it in a container. **Only what the script prints reaches Claude.** Meridian's 40 timesheets stay with the script, and Claude gets its short printout.

**Check your tools and your model first.** As of October 2026, programmatic tool calling [doesn't support tools marked `strict: true`(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#feature-incompatibilities). It also doesn't support `disable_parallel_tool_use`, the `tool_choice` setting that limits Claude to one tool call in each response. `tool_choice` can't force Claude to call a tool from the script.

Claude Haiku 4.5 doesn't support the feature. The feature runs on the Claude API, Claude Platform on AWS, and Microsoft Foundry deployments hosted on Anthropic.

Turning on programmatic tool calling takes four changes.

1. **Add the code execution tool to your `tools` list.**
2. **Mark the tools the script may call.** Give each one an `allowed_callers` field that names the code execution tool at [version `code_execution_20260120` or later(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference).
3. **Send the container's ID back.** Read it from each response that stops for a tool call, and send it with the request that returns your tool results.
4. **Describe each tool's result.** Say in the description what shape it takes, because the script has to parse it. Here's Meridian's description for `get_employee_hours`.

`Returns one engineer's hours for the month as JSON: {"name": str, "billable_hours": float, "utilization": float 0-1}`

Here's Meridian's loop after these changes.

python

```
CODE_EXECUTION = "code_execution_20260120"
TOOLS = [
    {"type": CODE_EXECUTION, "name": "code_execution"},
    {**LIST_EMPLOYEES, "allowed_callers": [CODE_EXECUTION]},
    {**GET_EMPLOYEE_HOURS, "allowed_callers": [CODE_EXECUTION]},
]

messages = [{"role": "user", "content": QUESTION}]
container = None
while True:
    resp = client.messages.create(
        model="claude-sonnet-5", max_tokens=4096,
        tools=TOOLS, messages=messages, container=container,
    )
    print(resp.usage.input_tokens, "input tokens")
    if resp.stop_reason not in ("tool_use", "pause_turn"):
        break
    container = resp.container.id
    messages.append({"role": "assistant", "content": resp.content})
    if resp.stop_reason == "tool_use":
        messages.append({"role": "user", "content": run_tools(resp)})
print("".join(b.text for b in resp.content if b.type == "text"))
```

* `LIST_EMPLOYEES` and `GET_EMPLOYEE_HOURS` are Meridian's tool definitions.
* Your own `run_tools` runs each tool call and returns the results.
* On `pause_turn`, the loop sends the response back and continues.

When the script calls a tool, the response's `stop_reason` is `"tool_use"`. Your code runs the tool, and the result goes to the script, not to Claude. The script can run tools in parallel, so one response can hold more than one tool call.

Here's the same question answered both ways.

| Run | Requests | Tool calls | Input tokens | Token cost |
| --- | --- | --- | --- | --- |
| Classic loop | 42 | 41 | 1,124,799 | $2.29 |
| Programmatic tool calling | 3 | 41 | 28,486 | $0.0667 |

*Both runs used the same question, the same tools, and `claude-sonnet-5`. Costs use [prices as of September 2026(opens in new tab)](https://claude.com/pricing), and code execution time is billed separately from tokens.*

Programmatic tool calling fits lookups that don't depend on each other. It helps little when Claude has to reason over each result before it makes the next tool call.

## Cache tool definitions that repeat[](#cache-tool-definitions-that-repeat)

With prompt caching, the API stores the prefix of your request, the part up to a cache point you mark. Reading that prefix again costs far less.

A second Meridian agent has 14 tools, and their definitions come to 3,305 tokens that every request sends again.

**Mark the cache point by putting `cache_control` on the last tool, and the whole list is cached.** That takes one line:

python

```
TOOLS[-1]["cache_control"] = {"type": "ephemeral"}
```

On Claude Sonnet 5, reading the prefix costs [a tenth of the normal input price(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pricing). Writing it costs 1.25 times the normal input price.

The cached prefix lasts five minutes by default, and each use renews it. For requests further apart, add `"ttl": "1h"` to `cache_control` to keep it for an hour. Writing a one-hour cache costs [twice the normal input price(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pricing).

Meridian ran the same eight questions with the cache and without it. Its total input cost fell from $0.0554 to $0.0154.

With [automatic caching(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#automatic-caching), you put one `cache_control` field at the top level of the request, and the API places the cache point for you.

Watch for three things once caching is on:

1. Change any tool definition and you lose the whole cache.
2. On Sonnet 5, a cached prefix has to be at least 1,024 tokens. When it's shorter, nothing is cached and no error says so.
3. With caching on, `input_tokens` leaves out the cached prefix, so a request's true total is `input_tokens`, `cache_read_input_tokens`, and `cache_creation_input_tokens` added together.

## Combine the features where they fit[](#combine-the-features-where-they-fit)

Add them in this order.

1. **Start with caching.** It takes one line.
2. **Test programmatic tool calling.** Run some of your usual traffic with and without `allowed_callers`, then compare each run's billed input tokens.

For each of the two Meridian requests below, find the part that holds most of the input tokens, then pick the feature that cuts it.

## Key takeaways[](#key-takeaways)

* Every request sends everything again, so you pay for old tool results over and over.
* Print `usage.input_tokens` each time a response comes back, so you know which part of the request costs the most.
* Start with caching. Add `cache_control` to the last tool in your list.
* When your tool calls don't depend on each other, set up programmatic tool calling with the code execution tool and `allowed_callers`. Send the container's ID with every later request.

[Previous lessonComputer use: Automate desktop software with no API](https://academy.claude.com/courses/tool-use-with-the-messages-api/computer-use)[Next lessonCourse quiz](https://academy.claude.com/courses/tool-use-with-the-messages-api/course-quiz)

Lesson 8 of 9 · Tool use with the Messages APICut the cost of tool-heavy workflows

Reliable calls

* [Creating tools that Claude picks](https://academy.claude.com/courses/tool-use-with-the-messages-api/creating-tools-that-claude-picks)
* [Strict tool use: Stop rejecting your own calls](https://academy.claude.com/courses/tool-use-with-the-messages-api/strict-tool-use)

Parallel and streamed tool calls

* [Parallel tool calling: Cut the latency](https://academy.claude.com/courses/tool-use-with-the-messages-api/parallel-tool-calling)
* [Streaming tool calls: No more frozen spinners](https://academy.claude.com/courses/tool-use-with-the-messages-api/streaming-tool-calls)

Tools Anthropic provides

* [Code execution: Claude runs the code it writes](https://academy.claude.com/courses/tool-use-with-the-messages-api/code-execution)
* [Web search: Answers from the sites you trust](https://academy.claude.com/courses/tool-use-with-the-messages-api/web-search)
* [Computer use: Automate desktop software with no API](https://academy.claude.com/courses/tool-use-with-the-messages-api/computer-use)

Costs of tool-heavy requests

* [Cut the cost of tool-heavy workflows](https://academy.claude.com/courses/tool-use-with-the-messages-api/cut-the-cost-of-tool-heavy-workflows)

Quiz and next steps

* [Course quizQuiz](https://academy.claude.com/courses/tool-use-with-the-messages-api/course-quiz)
* [Start fixing your own tools](https://academy.claude.com/courses/tool-use-with-the-messages-api/next-steps)

* [Completion badge](https://academy.claude.com/courses/tool-use-with-the-messages-api/badge)

* [Measure the input tokens in each request](#measure-the-input-tokens-in-each-request)
* [Keep tool results out of what Claude reads](#keep-tool-results-out-of-what-claude-reads)
* [Cache tool definitions that repeat](#cache-tool-definitions-that-repeat)
* [Combine the features where they fit](#combine-the-features-where-they-fit)
* [Key takeaways](#key-takeaways)
