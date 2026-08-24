<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/multi-turn-conversations -->

Lesson 4 of 65 · Claude with Amazon BedrockMulti-Turn conversations

The code we've written so far simulates a very simple exchange with Claude. But what happens when you want to continue a conversation? When you ask a follow-up question like "And 3 more?" after asking "What's 1+1?", you might expect Claude to understand you're asking about adding 3 to the previous result of 2.

![](https://academy.claude.com/assets/media/f29c60433e17d03d10e044a9c2a3fb707fc872e106269c250c8ff185309321e0.png)

However, there's something critical you need to understand about the Bedrock API and Claude itself.

## No Message Storage

Bedrock and Claude do not store any messages. None of the messages you send get stored, and none of the responses you receive are stored either. Each API call is completely independent.

![](https://academy.claude.com/assets/media/e16ef969c212a7411214c239a1a87ff224f3f84aa71924c586f12a2ccaf56142.png)

To have a conversation with multiple messages that maintain context, you need to:

* Manually maintain a list of all messages in your code
* Provide that entire list of messages with each follow-up request

## Why Context Matters

Let's see what happens without proper context. If you send just "And 3 more?" as a standalone message, Claude has no idea what you're referring to. It will do its best to respond, but the answer won't make sense because it lacks the context of your previous conversation.

![](https://academy.claude.com/assets/media/e8cb9ad98933f418225e8f7219abdc2685cde3583eb4bb26bde655351f7cfdbb.png)

When you send only the follow-up question, Claude sees just that isolated message and tries to respond without knowing about the previous "What's 1+1?" exchange.

![](https://academy.claude.com/assets/media/6e2e0f684037ec9034087e687eab7bb834c6932109a56c5e38807b8d7dd74336.png)

## Building Conversation Context

To maintain context, you need to include the full conversation history in each request. Here's how it works:

![](https://academy.claude.com/assets/media/513d4d190ef8558b64469605d419f7722dc06a898c2151ae6818fb7fa85385d0.png)

Your message list should contain all previous exchanges - both user messages and assistant responses. When you send this complete context, Claude can understand that "And 3 more?" refers to adding 3 to the previous result of 2.

## Helper Functions for Message Management

To make conversation management easier, you can create helper functions:

python

```
def add_user_message(messages, text):
    user_message = {
        "role": "user",
        "content": [
            {"text": text}
        ]
    }
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {
        "role": "assistant",
        "content": [
            {"text": text}
        ]
    }
    messages.append(assistant_message)

def chat(messages):
    response = client.converse(
        modelId=model_id,
        messages=messages
    )
    return response["output"]["message"]["content"][0]["text"]
```

## Implementing Multi-Turn Conversations

Here's how to build a conversation step by step:

python

```
# Make a starting list of messages
messages = []

# Add in the initial user question of "What's 1+1?"
add_user_message(messages, "What's 1+1?")

# Pass the list of messages into chat to get an answer
answer = chat(messages)

# Take the answer and add it as an assistant message into our list
add_assistant_message(messages, answer)

# Add in the user's followup question
add_user_message(messages, "And 3 more added to that?")

# Call chat again with the list of messages to get a final answer
answer = chat(messages)
print(answer)
```

This approach ensures Claude has the full context and can respond appropriately: "Starting with the result of 1+1 = 2, if we add 3 more to that, we get: 2 + 3 = 5"

## Message Role Alternation

When building your message list, always ensure that message roles alternate properly:

![](https://academy.claude.com/assets/media/a6c3f43aa044d65f4faa1456f338e1a7f7832b20d328b42f77683071c20d7575.png)

Your conversation should follow the pattern: user → assistant → user → assistant. Never have two user messages in a row or two assistant messages in a row. This alternating pattern is required by the API and reflects natural conversation flow.

While this manual message management might seem tedious at first, you'll quickly get used to it. This pattern is fundamental to building any application that needs to maintain conversational context with Claude.
