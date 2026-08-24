<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/handling-tool-use-responses -->

Lesson 24 of 65 · Claude with Amazon BedrockHandling tool use responses

When Claude decides to use a tool, it returns a special response structure that requires careful handling. Understanding this response format and implementing proper conversation management is crucial for building robust tool-enabled applications.

## Tool Choice Configuration

Before diving into responses, it's worth understanding how to control when Claude uses tools. The `toolChoice` parameter gives you three options:

![](https://academy.claude.com/assets/media/d5cc2db705eb928f4697f1e7fff1fae85dca12bd7f52d4a0c18d58fa9f81dc4a.png)

* **auto** - Claude decides whether to use a tool (default behavior)
* **any** - Claude must use a tool but can choose which one
* **specific tool** - Force Claude to use a particular tool by name

The third option is especially useful for testing when you want to ensure Claude calls a specific function.

## Multi-Part Message Structure

When Claude wants to use a tool, it returns an assistant message with multiple content parts instead of just text:

![](https://academy.claude.com/assets/media/c8f7e87624025a31720dff67b9f4edbb1911958d989c96d53662daec89f4065c.png)

The response contains two parts:

* **Text Part** - Human-readable explanation like "I can help you find out the current time. Let me find that information for you"
* **ToolUse Part** - Structured data telling you which tool to run and with what arguments

## Understanding the ToolUse Part

The ToolUse part contains three key pieces of information:

![](https://academy.claude.com/assets/media/0f51c3d73779b0924a84a1781b65d23f28beea1c52eef15b96e5c15bfb2e9eac.png)

* **toolUseId** - A unique identifier you'll need when sending back the tool result
* **name** - The exact tool name from your JSON schema that Claude wants to call
* **input** - A dictionary of arguments Claude wants to pass to your tool function

## Conversation Flow with Tools

Tool usage follows a specific conversation pattern that requires maintaining complete message history:

![](https://academy.claude.com/assets/media/9eccbcb4136ead3a62a60ff14b1dc7ef966ee74dddba471cffc37ba59ec22560.png)

When you receive a tool use request, you need to:

1. Extract the tool information from the ToolUse part
2. Run your actual tool function
3. Send back a ToolResult message along with the complete conversation history
4. Include the original user message and the assistant's tool use message in your next request

## Updating Helper Functions

To handle multi-part messages properly, you'll need to update your message handling functions. Here's how to make your functions flexible enough to handle both simple text and complex multi-part content:

python

```
def add_user_message(messages, content):
    if isinstance(content, str):
        user_message = {"role": "user", "content": [{"text": content}]}
    else:
        user_message = {"role": "user", "content": content}
    messages.append(user_message)

def add_assistant_message(messages, content):
    if isinstance(content, str):
        assistant_message = {"role": "assistant", "content": [{"text": content}]}
    else:
        assistant_message = {"role": "assistant", "content": content}
    messages.append(assistant_message)
```

You'll also want to update your chat function to return both the text and the full parts list:

python

```
def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
    # ... existing setup code ...

    response = client.converse(**params)

    text = response["output"]["message"]["content"][0]["text"]
    parts = response["output"]["message"]["content"]

    return text, parts
```

## Checking the Stop Reason

Claude's response also includes a top-level `stopReason` field. When it equals `"tool_use"`, Claude wants to call a tool rather than just providing a text response — that's your signal to extract the tool information and execute the requested function. The `chat()` helper above doesn't surface this field yet, so for now you can detect tool use by checking the returned parts list for an entry with a `toolUse` key. You'll extend `chat()` to return `stopReason` directly in a later lesson.

With these patterns in place, you're ready to handle Claude's tool use requests and maintain proper conversation flow throughout multi-turn tool interactions.
