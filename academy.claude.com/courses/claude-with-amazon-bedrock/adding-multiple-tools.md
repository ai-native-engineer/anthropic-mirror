<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/adding-multiple-tools -->

Lesson 28 of 65 · Claude with Amazon BedrockAdding multiple tools

Now that we have one tool working, it's time to add the remaining two tools to complete our project: `add_duration_to_datetime` and `set_reminder`. The good news is that once you have the foundation in place, adding new tools is straightforward.

![](https://academy.claude.com/assets/media/91f4fc5203e3c1c26229c13016088eaf51bee660857c84c5fef4d90148b5b199.jpg)

## Pre-built Functions and Schemas

To save time, the implementations for both additional functions are already provided, along with their JSON schema specifications. You can find these in the earlier code cells:

* **add\_duration\_to\_datetime** - Handles date arithmetic for various time units
* **set\_reminder** - Creates reminders (currently just prints output, but could be extended to integrate with actual reminder systems)

![](https://academy.claude.com/assets/media/ce5f610d33fa1b308e460383ebcd24b7ce46a410e71cf68fc72f3576d68f0c63.jpg)

Each function comes with a corresponding JSON schema that defines the expected parameters and their types.

## Adding Tools to the Conversation

The first step is to include the new tool schemas in your conversation function. In the `run_conversation` function, add the additional schemas to the tools array:

python

```
tools=[
    get_current_datetime_schema,
    add_duration_to_datetime_schema,
    set_reminder_schema
]
```

![](https://academy.claude.com/assets/media/57194c1c8700e889e86f892decc1168bf13fadb36e6cb0ce1bdf89d2aae6d34d.jpg)

## Wiring Up the Tool Functions

Next, you need to update the `run_tool` function to handle the new tool names. Add two additional conditional branches:

python

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "set_reminder":
        return set_reminder(**tool_input)
    elif tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    else:
        raise Exception(f"Unknown tool name: {tool_name}")
```

![](https://academy.claude.com/assets/media/2ff12ab3be5565da2e0f1a73749609e5af1b4881d76a747fc3ff0c57a2dfcd05.jpg)

## Testing the Complete System

With all tools connected, you can now test complex workflows that require multiple tool calls. For example, asking Claude to "Set a reminder to go to the doctor. The appointment is in 100 days" will trigger a sequence of operations:

1. Get today's date using `get_current_datetime`
2. Add 100 days to that date using `add_duration_to_datetime`
3. Create the reminder using `set_reminder`

![](https://academy.claude.com/assets/media/dcbabb51d3ac3d5a4f52172f10ffab8efd52e4d679360640b1f8ce94d861fbb5.jpg)

Claude automatically breaks down the request into logical steps and explains its plan before executing each tool call. The output shows the complete workflow, including the calculated future date and confirmation of the reminder being set.

## Key Takeaway

Once you have the foundational tool use infrastructure in place, adding new tools requires just two simple steps: including the schema in your tools array and adding a case to handle the tool name in your routing function. The initial setup might feel complex, but scaling to multiple tools becomes very manageable.
