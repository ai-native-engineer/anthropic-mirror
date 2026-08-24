<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/streaming -->

Lesson 7 of 65 · Claude with Amazon BedrockStreaming

When building chat interfaces with AI models, users expect to see responses appear immediately rather than waiting 10-30 seconds for a complete response. The `converse_stream` function solves this by streaming text as it's generated, creating a much better user experience.

## How Streaming Works

Instead of waiting for the entire response to be generated, streaming sends back pieces of text as soon as they're available. Here's how the flow changes:

![](https://academy.claude.com/assets/media/77791ffb43d5b4b169cafc72d9d05c0db3cd65b01f57dc394ac9defe463e0846.png)

When you call `converse_stream`, you immediately get back an initial response that contains a `stream` object. This stream is a generator that yields events as the model generates text. Each event contains a small chunk of the overall response.

## Basic Implementation

Here's how to use `converse_stream` in your code:

python

```
messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")
response = client.converse_stream(messages=messages, modelId=model_id)

for event in response["stream"]:
    print(event)
```

This will print out all the different events as they arrive. You'll see the response come in chunks rather than all at once.

## Understanding Stream Events

The stream yields several types of events, each serving a different purpose:

![](https://academy.claude.com/assets/media/e652a5f85512e95413552937a4205b09a51f3e2515ddf234e4911fbdac5c7ec2.png)

For basic text generation, you only need to care about `contentBlockDelta` events. These contain the actual generated text chunks that you want to display to users.

![](https://academy.claude.com/assets/media/97a9dc1ff5a0c677b9b0d0cb85a69c47e7b4a2a43776ca19b1aa715c845f9f83.png)

The events always arrive in a predictable order: `messageStart`, multiple `contentBlockDelta` events containing your text, then `contentBlockStop`, `messageStop`, and finally `metadata`.

## Extracting the Text

To get just the generated text from each chunk, filter for `contentBlockDelta` events and extract the text:

python

```
text = ""
for event in response["stream"]:
    if "contentBlockDelta" in event:
        chunk = event["contentBlockDelta"]["delta"]["text"]
        print(chunk, end="")
        text += chunk

print("\n\nTotal Message:\n" + text)
```

The `end=""` parameter removes the automatic newline that Python's print function adds, making the streaming text appear more naturally.

## Practical Applications

In a real application, instead of printing each chunk, you'd typically:

* Send each chunk to your frontend via WebSockets or Server-Sent Events
* Update the UI to display the growing response in real-time
* Store the complete message once streaming finishes
* Handle any errors that might occur during streaming

This streaming approach transforms the user experience from "submit and wait" to "submit and watch the response appear," making your AI-powered applications feel much more responsive and engaging.
