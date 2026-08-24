<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/using-multiple-tools -->

Lesson 29 of 66 · Claude with Google Cloud's Vertex AIUsing multiple tools

Adding multiple tools to your Claude implementation becomes straightforward once you have the core tool-handling infrastructure in place. This tutorial shows how to integrate additional tools by following a simple pattern.

![](https://academy.claude.com/assets/media/a717f46eec75a1fd38b52f641b998d3b0877e98425f802cf5a5e8b0926b2e604.png)

## The Tools We're Adding

We need three main capabilities for our reminder system:

* **Get current date time** - Claude needs to know the current date and time
* **Add duration to date time** - Claude isn't perfect with date time addition
* **Set a reminder** - Need a way to set a reminder

The good news is that most of the implementation work is already done. The `add_duration_to_datetime` function handles various time units (seconds, minutes, hours, days, weeks, months) and returns properly formatted datetime strings.

![](https://academy.claude.com/assets/media/f585eb66f25d88933ce57160e314b69102d4d01502cfd38cfa944b674d858970.png)

The `set_reminder` function is a simple placeholder that prints out confirmation details rather than actually setting system reminders.

## Adding Tools to the Conversation

The process follows the same pattern we established earlier. First, update the `run_conversation` function to include the new tool schemas:

python

```
response = chat(messages, tools=[
    get_current_datetime_schema,
    add_duration_to_datetime_schema,
    set_reminder_schema
])
```

![](https://academy.claude.com/assets/media/f321946e99ec905d8bdb68a743b2fa381d0ed4b92f9b72ab51a62d210eebf363.png)

This tells Claude about all available tools it can use during the conversation.

## Handling Tool Execution

Next, update the `run_tool` function to handle the new tool calls:

python

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    elif tool_name == "set_reminder":
        return set_reminder(**tool_input)
```

![](https://academy.claude.com/assets/media/05708aae0b884802d4e2cecf8d1d0cee843a4a3fa77f3621030aeffb87c3930c.png)

The pattern is consistent: check the tool name, call the corresponding function with the provided input, and return the result.

## Testing Multiple Tool Usage

Let's test with a complex request that requires multiple tools: "Set a reminder for my doctors appointment. Its 177 days after Jan 1st, 2050."

This request forces Claude to:

1. Calculate the date 177 days after January 1st, 2050
2. Set a reminder for that calculated date

![](https://academy.claude.com/assets/media/d1666c8c7d26379c7ef52c5df390315ad9f3d22d441faad4789dc191c9cc6305.png)

Claude handles this by first explaining what it needs to do, then using the `add_duration_to_datetime` tool to calculate June 27, 2050, and finally calling `set_reminder` with the correct date.

## Understanding the Message Flow

Looking at the conversation history reveals how Claude manages multiple tools in a single response. The assistant message contains both a text block explaining the process and a tool use block for the first calculation.

![](https://academy.claude.com/assets/media/6df4844f75276d59c6643d37b695c25bf4b90dc18f45c596a4855d726bd01b82.png)

After receiving the tool result, Claude continues with another message containing both text and another tool use block for setting the reminder. This demonstrates how Claude can chain multiple tool calls together to complete complex tasks.

## Key Takeaways

Once you have the basic tool infrastructure set up, adding new tools follows a simple three-step process:

* Add the tool schema to the tools list in `run_conversation`
* Add a case for the new tool in the `run_tool` function
* Implement the actual tool function

The framework handles all the message passing, tool result formatting, and conversation flow automatically. This makes it easy to build sophisticated AI assistants that can perform multiple related tasks in sequence.
