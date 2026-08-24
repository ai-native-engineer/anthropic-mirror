<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/sending-tool-results -->

Lesson 25 of 67 · Building with the Claude APISending tool results

After Claude requests a tool call, you need to execute the function and send the results back. This completes the tool use workflow by providing Claude with the information it requested.

## Running the Tool Function

When Claude responds with a tool use block, you extract the input parameters and call your function. Here's how to access the tool parameters:

python

```
response.content[1].input
```

This gives you a dictionary of the arguments Claude wants to pass to your function. Since your function expects keyword arguments rather than a dictionary, you use Python's unpacking syntax:

python

```
get_current_datetime(**response.content[1].input)
```

![](https://academy.claude.com/assets/media/e2516a817e8c2faed5b8b550b6ee5b9ba916b72f3c56bfd3bdd116879ba030f8.png)

## Tool Result Block

After running the tool function, you need to send the results back to Claude using a tool result block. This block goes inside a user message and tells Claude what happened when you executed the tool.

![](https://academy.claude.com/assets/media/9035ae652bfffca0219c19bc8053048d5e0e805cf4853dc2ee526edf54fe7a28.png)

The tool result block has several important properties:

* **tool\_use\_id** - Must match the id of the ToolUse block that this ToolResult corresponds to
* **content** - Output from running your tool, serialized as a string
* **is\_error** - True if an error occurred

## Handling Multiple Tool Calls

Claude can request multiple tool calls in a single response. For example, if a user asks "What's 10 + 10 and what's 30 + 30?", Claude might respond with two separate ToolUse blocks.

![](https://academy.claude.com/assets/media/eec25fde47ed8fa3a64af5f7f3bdf08cd21bf6aa949e1f2d21a3d0bbd549cddd.png)

Each tool call gets a unique ID, and you must match these IDs when sending back results. This ensures Claude knows which result corresponds to which request, even if the results arrive in a different order.

![](https://academy.claude.com/assets/media/72993e2545b7638dc6d900cd6c75834fabc7535ec4019a99ba40c37ab196b61e.png)

## Building the Follow-up Request

Your follow-up request to Claude must include the complete conversation history plus the new tool result. Here's the structure:

python

```
messages.append({
    "role": "user",
    "content": [{
        "type": "tool_result",
        "tool_use_id": response.content[1].id,
        "content": "15:04:22",
        "is_error": False
    }]
})
```

The complete message history now contains:

* Original user message
* Assistant message with tool use block
* User message with tool result block

## Making the Final Request

When sending the follow-up request, you must still include the tool schema even though you're not expecting Claude to make another tool call. Claude needs the schema to understand the tool references in your conversation history.

python

```
client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    tools=[get_current_datetime_schema]
)
```

![](https://academy.claude.com/assets/media/38aff0f2b767f4e5800935acc9f9bc07ecda5b5b0865247b27554671184ec071.png)

Claude will then respond with a final message that incorporates the tool results into a natural response for the user. The tool use workflow is now complete - you've successfully enabled Claude to access real-time information through your custom function.
