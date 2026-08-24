<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/making-a-request -->

Lesson 3 of 66 · Claude with Google Cloud's Vertex AIMaking a request

Now it's time to get hands-on with the Anthropic Python SDK and make your first request to Claude through Vertex AI. We'll walk through three essential steps: installing the SDK, creating a client, and making your first API call.

## Installing the Anthropic Python SDK

First, you'll need to install the Anthropic SDK with Vertex AI support. In your Jupyter notebook, run this magic command:

bash

```
%pip install "anthropic[vertex]"
```

The `[vertex]` part ensures you get the specific components needed to connect to Google Cloud's Vertex AI platform.

## Creating an API Client

Next, import and create a client instance specifically designed for Vertex AI:

python

```
from anthropic import AnthropicVertex

client = AnthropicVertex(region="global", project_id="your-project-id")
model = "claude-sonnet-4@20250514"
```

You'll need to replace `"your-project-id"` with your actual Google Cloud project ID, which you can find in the Google Cloud Console's project selector. Setting the model as a variable saves you from typing it repeatedly throughout your notebooks.

## Understanding the Create Function

The core of making requests to Claude is the `create` function, which requires three key parameters:

![](https://academy.claude.com/assets/media/2bb00b866f804886bcdfb39e996abc128d1b51647f4de2d8a03fce3e6fce88de.png)

* **model** - The name of the Claude model you want to use
* **max\_tokens** - A safety limit on response length (Claude won't try to hit this target, it just won't exceed it)
* **messages** - The conversation history you're sending to Claude

Think of `max_tokens` as a budget rather than a goal. If you set it to 1000, Claude will write whatever response it thinks is appropriate, but stop if it would exceed 1000 tokens.

## Understanding Messages

Messages represent the back-and-forth conversation between you and Claude, just like in a chat application:

![](https://academy.claude.com/assets/media/7eb6f8c396ec3fcdd8568722972dbabed6cfa0c66ba0f19258f4138a1658a2a1.png)

There are two types of messages:

* **User messages** - Content written by humans that you want to feed into Claude
* **Assistant messages** - Content that Claude has generated and sent back to you

## Making Your First Request

Here's how to structure a basic request:

python

```
message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)
```

Each message is a dictionary with a `role` (either "user" or "assistant") and `content` (the actual text).

## Extracting the Response

When you run the request, you'll get back a complex response object with lots of metadata. To get just the text that Claude generated, use:

python

```
message.content[0].text
```

This gives you clean, readable output instead of the full response object with all its technical details. You'll use this pattern frequently when working with Claude's responses.
