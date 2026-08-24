<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/handling-message-blocks -->

Lesson 25 of 66 · Claude with Google Cloud's Vertex AIHandling message blocks

When working with Claude's tool functionality, you'll encounter a new type of response structure that's different from the simple text responses you've seen before. Instead of just getting back a single text block, Claude can now return multi-block messages that contain both text and tool usage information.

## Making Tool-Enabled API Calls

To enable Claude to use tools, you need to include a `tools` parameter in your API call. Here's how to structure the request:

python

```
messages = []
messages.append({
    "role": "user",
    "content": "What is the exact time, formatted as HH:MM:SS?"
})

response = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    tools=[get_current_datetime_schema],
)
```

The `tools` parameter takes a list of JSON schemas that describe the available functions Claude can call.

## Understanding Multi-Block Messages

When Claude decides to use a tool, it returns an assistant message with multiple blocks in the content list. This is a significant change from the simple text-only responses you've worked with before.

![](https://academy.claude.com/assets/media/6214bef403068ab7fb0cc1ccf9bb27e7ed7bf1732410990af587fd4c92ac71b1.png)

A multi-block message typically contains:

* **Text Block** - Human-readable text explaining what Claude is doing (like "I can help you find out the current time. Let me find that information for you")
* **ToolUse Block** - Instructions for your code about which tool to call and what parameters to use

The ToolUse block includes:

* An ID for tracking the tool call
* The name of the function to call (like "get\_current\_datetime")
* Input parameters formatted according to your JSON schema
* The type designation "tool\_use"

## Handling Message History with Multi-Block Content

Here's the critical part: Claude doesn't store conversation history, so you must manage it manually. When working with tool responses, you need to preserve the entire content structure, including all blocks.

Instead of just extracting text, you need to append the complete response content:

python

```
messages.append({
    "role": "assistant",
    "content": response.content
})
```

This preserves both the text block and the tool use block, maintaining the full conversation context for future API calls.

## The Complete Flow

The tool usage process follows this pattern:

![](https://academy.claude.com/assets/media/9ec6ca3a38f9ba8b097b53f928990ae28fa557aea044899a6099222eafc1fef9.png)

1. Send user message with tool schema to Claude
2. Receive multi-block assistant message (text + tool use)
3. Extract tool call information and execute the function
4. Send tool result back to Claude with complete message history
5. Receive final response from Claude

Each step requires careful handling of the message structure to maintain conversation continuity. The key insight is that tool-enabled conversations involve more complex message formats, but the fundamental principle of maintaining complete message history remains the same.

## Updating Helper Functions

If you've been using helper functions like `add_user_message` and `add_assistant_message`, you'll need to update them to handle multi-block content. The current versions likely only support single text blocks, but now they need to accommodate the more complex content structures that include tool use blocks.
