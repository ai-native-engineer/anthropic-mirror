<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/multi-turn-conversations-with-tools -->

Lesson 27 of 66 · Claude with Google Cloud's Vertex AIMulti-turn conversations with tools

When building applications with multiple tools, you need to handle scenarios where Claude might need to call several tools in sequence to answer a single user question. For example, if a user asks "What day is 103 days from today?", Claude needs to first get the current date, then add 103 days to it.

![](https://academy.claude.com/assets/media/b0e37c02f440c757e74cac66bc67b4bfffd1926e5b471b3840753714d7ee7c5c.png)

This creates a multi-turn conversation pattern where Claude makes multiple tool requests before providing a final answer. Your application needs to handle this automatically.

## The Multi-Turn Tool Pattern

Here's what happens behind the scenes when Claude needs multiple tools:

1. User asks: "What day is 103 days from today?"
2. Claude responds with a tool use block requesting `get_current_datetime`
3. Your server calls the function and returns the result
4. Claude realizes it needs more information and requests `add_duration_to_datetime`
5. Your server calls that function and returns the result
6. Claude now has enough information to provide the final answer

![](https://academy.claude.com/assets/media/1af13eec2b4e2fa09cd63b9b1ab3c8efb4728b9c2581a26eb81fc924d9c2badd.png)

## Building a Conversation Loop

To handle this pattern, you need a conversation loop that continues until Claude stops requesting tools:

python

```
def run_conversation(messages):
    while True:
        response = chat(messages)

        add_assistant_message(messages, response)

        # Pseudo code
        if response isn't asking for a tool:
            break

        tool_result_blocks = run_tools(response)
        add_user_message(messages, tool_result_blocks)

    return messages
```

![](https://academy.claude.com/assets/media/f34e1f4fc8abec6af3ca66152b6ac22212d7fbc4c5602ce84c69f75f86c959e4.png)

## Refactoring Helper Functions

Before implementing the conversation loop, you need to update your helper functions to handle multiple message blocks properly.

### Updating Message Handlers

Your `add_user_message` and `add_assistant_message` functions currently assume they're always working with plain text. Update them to handle full message objects:

python

```
from anthropic.types import Message

def add_user_message(messages, message):
    user_message = {
        "role": "user",
        "content": message.content if isinstance(message, Message) else message
    }
    messages.append(user_message)
```

This allows you to pass in either a string, a list of blocks, or a complete message object.

### Updating the Chat Function

Modify your chat function to accept a list of tools and return the full message instead of just text:

python

```
def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
    }

    if tools:
        params["tools"] = tools

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message
```

### Extracting Text from Messages

Since the chat function now returns full messages instead of just text, add a helper to extract text when needed:

python

```
def text_from_message(message):
    return "\n".join(
        [block.text for block in message.content if block.type == "text"]
    )
```

This function finds all text blocks in a message and joins them together, which is useful when you need to display the final response to users.

## Why These Changes Matter

These refactoring steps prepare your code for the reality of tool-enabled conversations:

* **Multiple blocks per message** - Claude's responses can contain both text and tool use blocks
* **Flexible message handling** - Your functions can now work with various message formats
* **Full message preservation** - You maintain all the information Claude provides, not just the text portions
* **Tool list support** - Your chat function can now receive and use multiple tools

With these foundations in place, you're ready to implement the full conversation loop that handles multiple tool calls automatically, creating a seamless experience where Claude can use whatever tools it needs to answer user questions completely.
