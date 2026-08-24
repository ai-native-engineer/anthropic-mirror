<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/sending-tool-results -->

Lesson 26 of 66 · Claude with Google Cloud's Vertex AISending tool results

After Claude requests a tool call, you need to execute the function and send the results back. This completes the tool use workflow by providing Claude with the information it requested.

## Running the Tool Function

When Claude responds with a tool use block, you extract the input parameters and call your function. Here's how to access the tool parameters:

python

```
# Access the tool use block
tool_use_block = response.content[1]

# Get the input parameters
input_params = tool_use_block.input

# Call your function with the parameters
result = get_current_datetime(**input_params)
```

The double asterisk (`**`) unpacks the dictionary into keyword arguments that your function expects.

## Tool Result Block

After running the tool, you send the results back to Claude using a tool result block. This block has several important properties:

![](https://academy.claude.com/assets/media/9035ae652bfffca0219c19bc8053048d5e0e805cf4853dc2ee526edf54fe7a28.png)

* **tool\_use\_id** - Must match the ID from the original tool use block
* **content** - The output from your tool function, converted to a string
* **is\_error** - Set to true if an error occurred during execution

## Handling Multiple Tool Calls

Claude can request multiple tool calls in a single response. For example, if a user asks "What's 10 + 10 and what's 30 + 30?", Claude might send two separate tool use blocks:

![](https://academy.claude.com/assets/media/eec25fde47ed8fa3a64af5f7f3bdf08cd21bf6aa949e1f2d21a3d0bbd549cddd.png)

Each tool use block gets a unique ID, and you must match these IDs when sending back results:

![](https://academy.claude.com/assets/media/72993e2545b7638dc6d900cd6c75834fabc7535ec4019a99ba40c37ab196b61e.png)

This ID system ensures Claude can correctly match each result with its corresponding request, even if the results arrive in a different order.

## Sending the Follow-up Request

Your follow-up request to Claude must include the complete conversation history plus the new tool result:

python

```
messages.append({
    "role": "user",
    "content": [{
        "type": "tool_result",
        "tool_use_id": response.content[1].id,
        "content": result,
        "is_error": False
    }]
})
```

The conversation flow looks like this:

![](https://academy.claude.com/assets/media/38aff0f2b767f4e5800935acc9f9bc07ecda5b5b0865247b27554671184ec071.png)

Remember to include the tool schema in your follow-up request, even though Claude probably won't need to call tools again. Claude needs the schema to understand the tool references in the conversation history.

## Complete Workflow

Here's the full process:

1. User asks a question requiring tool use
2. Claude responds with a tool use block
3. You execute the requested tool function
4. You send a follow-up request with the tool result
5. Claude provides a final answer using the tool output

The final request includes your complete message history, the tool result block, and the tool schema. Claude then responds with a regular text message that incorporates the information from your tool execution.
