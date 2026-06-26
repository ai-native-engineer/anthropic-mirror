<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent -->

# Tutorial: Build a tool-using agent
A guided walkthrough from a single tool call to a production-ready agentic loop.
This tutorial builds a calendar-management agent in five concentric rings. Each ring is a complete, runnable program that adds exactly one concept to the ring before it. By the end you will have written the agentic loop by hand and then replaced it with the Tool Runner SDK abstraction.
The example tool is `create_calendar_event`. Its schema uses nested objects, arrays, and optional fields, so you will see how Claude handles realistic input shapes rather than a single flat string.
Every ring runs standalone. Copy any ring into a fresh file and it will execute without the code from earlier rings.
Ring 1: Single tool, single turn
The smallest possible tool-using program: one tool, one user message, one tool call, one result. The code is heavily commented so you can map each line to the [tool use lifecycle](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works).
The request sends a `tools` array alongside the user message. When Claude decides to call a tool, the response comes back with `stop_reason: "tool_use"` and a `tool_use` content block containing the tool name, a unique `id`, and the structured `input`. Your code executes the tool, then sends the result back in a `tool_result` block whose `tool_use_id` matches the `id` from the call.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Ring 1: Single tool, single turn.

import json

import anthropic

# Create a client. It reads ANTHROPIC_API_KEY from the environment.
client = anthropic.Anthropic()

# Define one tool. The input_schema is a JSON Schema object describing
# the arguments Claude should pass when it calls this tool. This schema
# includes nested objects (recurrence), arrays (attendees), and optional
# fields, which is closer to real-world tools than a flat string argument.
tools = [
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
            "required": ["title", "start", "end"],
]

# Send the user's request along with the tool definition. Claude decides
# whether to call the tool based on the request and the tool description.
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=[
            "role": "user",
            "content": "Schedule a 30-minute sync with [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection) and [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection) next Monday at 10am.",
    ],
)

# When Claude calls a tool, the response has stop_reason "tool_use"
# and the content array contains a tool_use block alongside any text.
print(f"stop_reason: {response.stop_reason}")

# Find the tool_use block. A response may contain text blocks before the
# tool_use block, so scan the content array rather than assuming position.
tool_use = next(block for block in response.content if block.type == "tool_use")
print(f"Tool: {tool_use.name}")
print(f"Input: {tool_use.input}")

# Execute the tool. In a real system this would call your calendar API.
# Here the result is hardcoded to keep the example self-contained.
result = {"event_id": "evt_123", "status": "created"}

# Send the result back. The tool_result block goes in a user message and
# its tool_use_id must match the id from the tool_use block above. The
# assistant's previous response is included so Claude has the full history.
followup = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=[
            "role": "user",
            "content": "Schedule a 30-minute sync with [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection) and [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection) next Monday at 10am.",
        {"role": "assistant", "content": response.content},
            "role": "user",
            "content": [
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": json.dumps(result),
            ],
    ],
)

# With the tool result in hand, Claude produces a final natural-language
# answer and stop_reason becomes "end_turn".
print(f"stop_reason: {followup.stop_reason}")
final_text = next(block for block in followup.content if block.type == "text")
print(final_text.text)

**What to expect**
Output

stop_reason: tool_use
Tool: create_calendar_event
Input: {'title': 'Sync', 'start': '2026-03-30T10:00:00', 'end': '2026-03-30T10:30:00', 'attendees': ['[email protected][](https://platform.claude.com/cdn-cgi/l/email-protection)', '[email protected][](https://platform.claude.com/cdn-cgi/l/email-protection)']}
stop_reason: end_turn
I've scheduled your 30-minute sync with Alice and Bob for next Monday at 10am.

The first `stop_reason` is `tool_use` because Claude is waiting for the calendar result. After you send the result, the second `stop_reason` is `end_turn` and the content is natural language for the user.
Ring 2: The agentic loop
Ring 1 assumed Claude would call the tool exactly once. Real tasks often need several calls: Claude might create an event, read the confirmation, then create another. The fix is a `while` loop that keeps running tools and feeding results back until `stop_reason` is no longer `"tool_use"`.
The other change is conversation history. Instead of rebuilding the `messages` array from scratch on each request, keep a running list and append to it. Every turn sees the complete prior context.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Ring 2: The agentic loop.

import json

import anthropic

client = anthropic.Anthropic()

tools = [
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
            "required": ["title", "start", "end"],
]

def run_tool(name, tool_input):
    if name == "create_calendar_event":
        return {"event_id": "evt_123", "status": "created", "title": tool_input["title"]}
    return {"error": f"Unknown tool: {name}"}

# Keep the full conversation history in a list so each turn sees prior context.
messages = [
        "role": "user",
        "content": "Schedule a weekly team standup every Monday at 9am for the next 4 weeks. Invite the whole team: [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection), [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection), [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection).",
]

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=messages,
)

# Loop until Claude stops asking for tools. Each iteration runs the requested
# tool, appends the result to history, and asks Claude to continue.
while response.stop_reason == "tool_use":
    tool_use = next(block for block in response.content if block.type == "tool_use")
    result = run_tool(tool_use.name, tool_use.input)

    messages.append({"role": "assistant", "content": response.content})
    messages.append(
            "role": "user",
            "content": [
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": json.dumps(result),
            ],
    )

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        tools=tools,
        tool_choice={"type": "auto", "disable_parallel_tool_use": True},
        messages=messages,
    )

final_text = next(block for block in response.content if block.type == "text")
print(final_text.text)

**What to expect**
Output

I've set up your weekly team standup for the next 4 Mondays at 9am with Alice, Bob, and Carol invited.

The loop might run once or several times depending on how Claude breaks down the task. Your code no longer needs to know in advance.
Ring 3: Multiple tools, parallel calls
Agents rarely have just one capability. Add a second tool, `list_calendar_events`, so Claude can check the existing schedule before creating something new.
When Claude has multiple independent tool calls to make, it might return several `tool_use` blocks in a single response. Your loop needs to process all of them and send back all results together in one user message. Iterate over every `tool_use` block in `response.content`, not just the first.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Ring 3: Multiple tools, parallel calls.

import json

import anthropic

client = anthropic.Anthropic()

tools = [
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
            "required": ["title", "start", "end"],
        "name": "list_calendar_events",
        "description": "List all calendar events on a given date.",
        "input_schema": {
            "type": "object",
            "properties": {
                "date": {"type": "string", "format": "date"},
            "required": ["date"],
]

def run_tool(name, tool_input):
    if name == "create_calendar_event":
        return {"event_id": "evt_123", "status": "created", "title": tool_input["title"]}
    if name == "list_calendar_events":
        return {"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]}
    return {"error": f"Unknown tool: {name}"}

messages = [
        "role": "user",
        "content": "Check what I have next Monday, then schedule a planning session that avoids any conflicts.",
]

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    messages=messages,
)

while response.stop_reason == "tool_use":
    # A single response can contain multiple tool_use blocks. Process all of
    # them and return all results together in one user message.
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            result = run_tool(block.name, block.input)
            tool_results.append(
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": json.dumps(result),
            )

    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": tool_results})

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

final_text = next(block for block in response.content if block.type == "text")
print(final_text.text)

**What to expect**
Output

I checked your calendar for next Monday and found an existing meeting from 2pm to 3pm. I've scheduled the planning session for 10am to 11am to avoid the conflict.

For more on concurrent execution and ordering guarantees, see [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).
Ring 4: Error handling
Tools fail. A calendar API might reject an event with too many attendees, or a date might be malformed. When a tool raises an error, send the error message back with `is_error: true` instead of crashing. Claude reads the error and can retry with corrected input, ask the user for clarification, or explain the limitation.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Ring 4: Error handling.

import json

import anthropic

client = anthropic.Anthropic()

tools = [
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
            "required": ["title", "start", "end"],
        "name": "list_calendar_events",
        "description": "List all calendar events on a given date.",
        "input_schema": {
            "type": "object",
            "properties": {
                "date": {"type": "string", "format": "date"},
            "required": ["date"],
]

def run_tool(name, tool_input):
    if name == "create_calendar_event":
        if "attendees" in tool_input and len(tool_input["attendees"]) > 10:
            raise ValueError("Too many attendees (max 10)")
        return {"event_id": "evt_123", "status": "created", "title": tool_input["title"]}
    if name == "list_calendar_events":
        return {"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]}
    raise ValueError(f"Unknown tool: {name}")

messages = [
        "role": "user",
        "content": "Schedule an all-hands with everyone: " + ", ".join(f"user{i}@example.com" for i in range(15)),
]

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    messages=messages,
)

while response.stop_reason == "tool_use":
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            try:
                result = run_tool(block.name, block.input)
                tool_results.append(
                    {"type": "tool_result", "tool_use_id": block.id, "content": json.dumps(result)}
                )
            except Exception as exc:
                # Signal failure so Claude can retry or ask for clarification.
                tool_results.append(
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(exc),
                        "is_error": True,
                )

    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": tool_results})

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

final_text = next(block for block in response.content if block.type == "text")
print(final_text.text)

**What to expect**
Output

I tried to schedule the all-hands but the calendar only allows 10 attendees per event. I can split this into two sessions, or you can let me know which 10 people to prioritize.

The `is_error` flag is the only difference from a successful result. Claude sees the flag and the error text, and responds accordingly. See [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) for the full error-handling reference.
Ring 5: The Tool Runner SDK abstraction
Rings 2 through 4 wrote the same loop by hand: call the API, check `stop_reason`, run tools, append results, repeat. The Tool Runner does this for you. Define each tool as a function, pass the list to `tool_runner`, and retrieve the final message once the loop completes. Error wrapping, result formatting, and conversation management are handled internally.
The Python SDK uses the `@beta_tool` decorator to infer the schema from type hints and the docstring. The TypeScript SDK uses `betaZodTool` with a Zod schema. The other SDKs follow the same pattern with their own helpers: `BetaRunnableTool` in C# and PHP, typed tool classes in Java and Ruby, and `toolrunner.NewBetaToolFromJSONSchema` in Go.
Tool Runner is available in all seven SDKs: Python, TypeScript, C#, Go, Java, PHP, and Ruby. See [Tool Runner](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner) for the full reference. The cURL and CLI tabs show a note instead of code; keep the Ring 4 loop for curl- or CLI-based scripts.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Ring 5: The Tool Runner SDK abstraction.

import json

import anthropic
from anthropic import beta_tool

client = anthropic.Anthropic()

@beta_tool
def create_calendar_event(
    title: str,
    start: str,
    end: str,
    attendees: list[str] | None = None,
    recurrence: dict | None = None,
) -> str:
    """Create a calendar event with attendees and optional recurrence.

    Args:
        title: Event title.
        start: Start time in ISO 8601 format.
        end: End time in ISO 8601 format.
        attendees: Email addresses to invite.
        recurrence: Dict with 'frequency' (daily, weekly, monthly) and 'count'.
    """
    if attendees and len(attendees) > 10:
        raise ValueError("Too many attendees (max 10)")
    return json.dumps({"event_id": "evt_123", "status": "created", "title": title})

@beta_tool
def list_calendar_events(date: str) -> str:
    """List all calendar events on a given date.

    Args:
        date: Date in YYYY-MM-DD format.
    """
    return json.dumps({"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]})

final_message = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[create_calendar_event, list_calendar_events],
    messages=[
            "role": "user",
            "content": "Check what I have next Monday, then schedule a planning session that avoids any conflicts.",
    ],
).until_done()

for block in final_message.content:
    if block.type == "text":
        print(block.text)

**What to expect**
Output

I checked your calendar for next Monday and found an existing meeting from 2pm to 3pm. I've scheduled the planning session for 10am to 11am to avoid the conflict.

The output is identical to Ring 3. The difference is in the code: roughly half the lines, no manual loop, and the schema lives next to the implementation.
What you built
You started with a single hardcoded tool call and ended with a production-shaped agent that handles multiple tools, parallel calls, and errors, then collapsed all of that into the Tool Runner. Along the way you saw every piece of the tool-use protocol: `tool_use` blocks, `tool_result` blocks, `tool_use_id` matching, `stop_reason` checking, and `is_error` signaling.
Next steps
[ Define tools Schema specification and best practices. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)[ Tool Runner deep dive The full SDK abstraction reference. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)[ Troubleshooting Fix common tool-use errors. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)
  * [Ring 1: Single tool, single turn](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent#ring-1-single-tool-single-turn)
  * [Ring 2: The agentic loop](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent#ring-2-the-agentic-loop)
  * [Ring 3: Multiple tools, parallel calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent#ring-3-multiple-tools-parallel-calls)
  * [Ring 4: Error handling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent#ring-4-error-handling)
  * [Ring 5: The Tool Runner SDK abstraction](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent#ring-5-the-tool-runner-sdk-abstraction)
  * [What you built](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent#what-you-built)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent#next-steps)

Messages/Tools
# Tutorial: Build a tool-using agent
A guided walkthrough from a single tool call to a production-ready agentic loop.
This tutorial builds a calendar-management agent in five concentric rings. Each ring is a complete, runnable program that adds exactly one concept to the ring before it. By the end you will have written the agentic loop by hand and then replaced it with the Tool Runner SDK abstraction.
The example tool is `create_calendar_event`. Its schema uses nested objects, arrays, and optional fields, so you will see how Claude handles realistic input shapes rather than a single flat string.
Every ring runs standalone. Copy any ring into a fresh file and it will execute without the code from earlier rings.
Ring 1: Single tool, single turn
The smallest possible tool-using program: one tool, one user message, one tool call, one result. The code is heavily commented so you can map each line to the [tool use lifecycle](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works).
The request sends a `tools` array alongside the user message. When Claude decides to call a tool, the response comes back with `stop_reason: "tool_use"` and a `tool_use` content block containing the tool name, a unique `id`, and the structured `input`. Your code executes the tool, then sends the result back in a `tool_result` block whose `tool_use_id` matches the `id` from the call.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Ring 1: Single tool, single turn.

import json

import anthropic

# Create a client. It reads ANTHROPIC_API_KEY from the environment.
client = anthropic.Anthropic()

# Define one tool. The input_schema is a JSON Schema object describing
# the arguments Claude should pass when it calls this tool. This schema
# includes nested objects (recurrence), arrays (attendees), and optional
# fields, which is closer to real-world tools than a flat string argument.
tools = [
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
            "required": ["title", "start", "end"],
]

# Send the user's request along with the tool definition. Claude decides
# whether to call the tool based on the request and the tool description.
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=[
            "role": "user",
            "content": "Schedule a 30-minute sync with [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection) and [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection) next Monday at 10am.",
    ],
)

# When Claude calls a tool, the response has stop_reason "tool_use"
# and the content array contains a tool_use block alongside any text.
print(f"stop_reason: {response.stop_reason}")

# Find the tool_use block. A response may contain text blocks before the
# tool_use block, so scan the content array rather than assuming position.
tool_use = next(block for block in response.content if block.type == "tool_use")
print(f"Tool: {tool_use.name}")
print(f"Input: {tool_use.input}")

# Execute the tool. In a real system this would call your calendar API.
# Here the result is hardcoded to keep the example self-contained.
result = {"event_id": "evt_123", "status": "created"}

# Send the result back. The tool_result block goes in a user message and
# its tool_use_id must match the id from the tool_use block above. The
# assistant's previous response is included so Claude has the full history.
followup = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=[
            "role": "user",
            "content": "Schedule a 30-minute sync with [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection) and [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection) next Monday at 10am.",
        {"role": "assistant", "content": response.content},
            "role": "user",
            "content": [
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": json.dumps(result),
            ],
    ],
)

# With the tool result in hand, Claude produces a final natural-language
# answer and stop_reason becomes "end_turn".
print(f"stop_reason: {followup.stop_reason}")
final_text = next(block for block in followup.content if block.type == "text")
print(final_text.text)

**What to expect**
Output

stop_reason: tool_use
Tool: create_calendar_event
Input: {'title': 'Sync', 'start': '2026-03-30T10:00:00', 'end': '2026-03-30T10:30:00', 'attendees': ['[email protected][](https://platform.claude.com/cdn-cgi/l/email-protection)', '[email protected][](https://platform.claude.com/cdn-cgi/l/email-protection)']}
stop_reason: end_turn
I've scheduled your 30-minute sync with Alice and Bob for next Monday at 10am.

The first `stop_reason` is `tool_use` because Claude is waiting for the calendar result. After you send the result, the second `stop_reason` is `end_turn` and the content is natural language for the user.
Ring 2: The agentic loop
Ring 1 assumed Claude would call the tool exactly once. Real tasks often need several calls: Claude might create an event, read the confirmation, then create another. The fix is a `while` loop that keeps running tools and feeding results back until `stop_reason` is no longer `"tool_use"`.
The other change is conversation history. Instead of rebuilding the `messages` array from scratch on each request, keep a running list and append to it. Every turn sees the complete prior context.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Ring 2: The agentic loop.

import json

import anthropic

client = anthropic.Anthropic()

tools = [
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
            "required": ["title", "start", "end"],
]

def run_tool(name, tool_input):
    if name == "create_calendar_event":
        return {"event_id": "evt_123", "status": "created", "title": tool_input["title"]}
    return {"error": f"Unknown tool: {name}"}

# Keep the full conversation history in a list so each turn sees prior context.
messages = [
        "role": "user",
        "content": "Schedule a weekly team standup every Monday at 9am for the next 4 weeks. Invite the whole team: [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection), [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection), [email protected][](https://platform.claude.com/cdn-cgi/l/email-protection).",
]

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=messages,
)

# Loop until Claude stops asking for tools. Each iteration runs the requested
# tool, appends the result to history, and asks Claude to continue.
while response.stop_reason == "tool_use":
    tool_use = next(block for block in response.content if block.type == "tool_use")
    result = run_tool(tool_use.name, tool_use.input)

    messages.append({"role": "assistant", "content": response.content})
    messages.append(
            "role": "user",
            "content": [
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": json.dumps(result),
            ],
    )

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        tools=tools,
        tool_choice={"type": "auto", "disable_parallel_tool_use": True},
        messages=messages,
    )

final_text = next(block for block in response.content if block.type == "text")
print(final_text.text)

**What to expect**
Output

I've set up your weekly team standup for the next 4 Mondays at 9am with Alice, Bob, and Carol invited.

The loop might run once or several times depending on how Claude breaks down the task. Your code no longer needs to know in advance.
Ring 3: Multiple tools, parallel calls
Agents rarely have just one capability. Add a second tool, `list_calendar_events`, so Claude can check the existing schedule before creating something new.
When Claude has multiple independent tool calls to make, it might return several `tool_use` blocks in a single response. Your loop needs to process all of them and send back all results together in one user message. Iterate over every `tool_use` block in `response.content`, not just the first.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Ring 3: Multiple tools, parallel calls.

import json

import anthropic

client = anthropic.Anthropic()

tools = [
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
            "required": ["title", "start", "end"],
        "name": "list_calendar_events",
        "description": "List all calendar events on a given date.",
        "input_schema": {
            "type": "object",
            "properties": {
                "date": {"type": "string", "format": "date"},
            "required": ["date"],
]

def run_tool(name, tool_input):
    if name == "create_calendar_event":
        return {"event_id": "evt_123", "status": "created", "title": tool_input["title"]}
    if name == "list_calendar_events":
        return {"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]}
    return {"error": f"Unknown tool: {name}"}

messages = [
        "role": "user",
        "content": "Check what I have next Monday, then schedule a planning session that avoids any conflicts.",
]

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    messages=messages,
)

while response.stop_reason == "tool_use":
    # A single response can contain multiple tool_use blocks. Process all of
    # them and return all results together in one user message.
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            result = run_tool(block.name, block.input)
            tool_results.append(
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": json.dumps(result),
            )

    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": tool_results})

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

final_text = next(block for block in response.content if block.type == "text")
print(final_text.text)

**What to expect**
Output

I checked your calendar for next Monday and found an existing meeting from 2pm to 3pm. I've scheduled the planning session for 10am to 11am to avoid the conflict.

For more on concurrent execution and ordering guarantees, see [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).
Ring 4: Error handling
Tools fail. A calendar API might reject an event with too many attendees, or a date might be malformed. When a tool raises an error, send the error message back with `is_error: true` instead of crashing. Claude reads the error and can retry with corrected input, ask the user for clarification, or explain the limitation.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Ring 4: Error handling.

import json

import anthropic

client = anthropic.Anthropic()

tools = [
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
            "required": ["title", "start", "end"],
        "name": "list_calendar_events",
        "description": "List all calendar events on a given date.",
        "input_schema": {
            "type": "object",
            "properties": {
                "date": {"type": "string", "format": "date"},
            "required": ["date"],
]

def run_tool(name, tool_input):
    if name == "create_calendar_event":
        if "attendees" in tool_input and len(tool_input["attendees"]) > 10:
            raise ValueError("Too many attendees (max 10)")
        return {"event_id": "evt_123", "status": "created", "title": tool_input["title"]}
    if name == "list_calendar_events":
        return {"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]}
    raise ValueError(f"Unknown tool: {name}")

messages = [
        "role": "user",
        "content": "Schedule an all-hands with everyone: " + ", ".join(f"user{i}@example.com" for i in range(15)),
]

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    messages=messages,
)

while response.stop_reason == "tool_use":
    tool_results = []
    for block in response.content:
        if block.type == "tool_use":
            try:
                result = run_tool(block.name, block.input)
                tool_results.append(
                    {"type": "tool_result", "tool_use_id": block.id, "content": json.dumps(result)}
                )
            except Exception as exc:
                # Signal failure so Claude can retry or ask for clarification.
                tool_results.append(
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(exc),
                        "is_error": True,
                )

    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": tool_results})

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

final_text = next(block for block in response.content if block.type == "text")
print(final_text.text)

**What to expect**
Output

I tried to schedule the all-hands but the calendar only allows 10 attendees per event. I can split this into two sessions, or you can let me know which 10 people to prioritize.

The `is_error` flag is the only difference from a successful result. Claude sees the flag and the error text, and responds accordingly. See [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) for the full error-handling reference.
Ring 5: The Tool Runner SDK abstraction
Rings 2 through 4 wrote the same loop by hand: call the API, check `stop_reason`, run tools, append results, repeat. The Tool Runner does this for you. Define each tool as a function, pass the list to `tool_runner`, and retrieve the final message once the loop completes. Error wrapping, result formatting, and conversation management are handled internally.
The Python SDK uses the `@beta_tool` decorator to infer the schema from type hints and the docstring. The TypeScript SDK uses `betaZodTool` with a Zod schema. The other SDKs follow the same pattern with their own helpers: `BetaRunnableTool` in C# and PHP, typed tool classes in Java and Ruby, and `toolrunner.NewBetaToolFromJSONSchema` in Go.
Tool Runner is available in all seven SDKs: Python, TypeScript, C#, Go, Java, PHP, and Ruby. See [Tool Runner](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner) for the full reference. The cURL and CLI tabs show a note instead of code; keep the Ring 4 loop for curl- or CLI-based scripts.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Ring 5: The Tool Runner SDK abstraction.

import json

import anthropic
from anthropic import beta_tool

client = anthropic.Anthropic()

@beta_tool
def create_calendar_event(
    title: str,
    start: str,
    end: str,
    attendees: list[str] | None = None,
    recurrence: dict | None = None,
) -> str:
    """Create a calendar event with attendees and optional recurrence.

    Args:
        title: Event title.
        start: Start time in ISO 8601 format.
        end: End time in ISO 8601 format.
        attendees: Email addresses to invite.
        recurrence: Dict with 'frequency' (daily, weekly, monthly) and 'count'.
    """
    if attendees and len(attendees) > 10:
        raise ValueError("Too many attendees (max 10)")
    return json.dumps({"event_id": "evt_123", "status": "created", "title": title})

@beta_tool
def list_calendar_events(date: str) -> str:
    """List all calendar events on a given date.

    Args:
        date: Date in YYYY-MM-DD format.
    """
    return json.dumps({"events": [{"title": "Existing meeting", "start": "14:00", "end": "15:00"}]})

final_message = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[create_calendar_event, list_calendar_events],
    messages=[
            "role": "user",
            "content": "Check what I have next Monday, then schedule a planning session that avoids any conflicts.",
    ],
).until_done()

for block in final_message.content:
    if block.type == "text":
        print(block.text)

**What to expect**
Output

I checked your calendar for next Monday and found an existing meeting from 2pm to 3pm. I've scheduled the planning session for 10am to 11am to avoid the conflict.

The output is identical to Ring 3. The difference is in the code: roughly half the lines, no manual loop, and the schema lives next to the implementation.
What you built
You started with a single hardcoded tool call and ended with a production-shaped agent that handles multiple tools, parallel calls, and errors, then collapsed all of that into the Tool Runner. Along the way you saw every piece of the tool-use protocol: `tool_use` blocks, `tool_result` blocks, `tool_use_id` matching, `stop_reason` checking, and `is_error` signaling.
Next steps
[ Define tools Schema specification and best practices. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)[ Tool Runner deep dive The full SDK abstraction reference. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)[ Troubleshooting Fix common tool-use errors. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)
