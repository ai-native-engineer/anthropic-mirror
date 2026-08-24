<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/system-prompts -->

Lesson 5 of 65 · Claude with Amazon BedrockSystem prompts

When building AI chatbots for specific use cases, you need a way to control how the AI responds. System prompts are the key to transforming a general-purpose AI into a specialized assistant that follows specific guidelines and stays on topic.

![](https://academy.claude.com/assets/media/a8883fbe515bc8ea7e369f29e866caa10ed49af599dd529a3143bed87c9cd346.png)

## The Problem with User-Level Instructions

You might think the solution is to include all your requirements in the user message itself. For example, telling the AI in each conversation to "mention AWS services" and "don't mention competitors." This approach has serious limitations:

* You'd need to anticipate every possible question and edge case
* The instruction list becomes unwieldy and repetitive
* Users see all the internal instructions, making conversations cluttered
* Requirements change based on the specific question being asked

![](https://academy.claude.com/assets/media/0d5cb99bb7a6fcab168500308b061b008367df300bbd299edff265dbebf3805e.png)

## System Prompts: A Better Approach

System prompts solve this problem by giving Claude a role to play. Instead of listing specific do's and don'ts, you tell Claude to act like a particular type of professional. The AI then responds as that person would naturally respond.

![](https://academy.claude.com/assets/media/e8f3cc5bc734943a959be45a79ed9f50cd24eeee7976474ed9b1dbc33fd47b4c.png)

System prompts provide several key benefits:

* Claude gets guidance on how to respond consistently
* The AI adopts the mindset and constraints of the specified role
* Responses stay focused and on-brand automatically
* You don't need to anticipate every possible scenario

## Implementing System Prompts

To add a system prompt to your Claude conversation, you pass it as a parameter to the `converse` function:

python

```
system_prompt = """
You are an AWS cloud support specialist. Your job is to answer user queries related
to cloud hosting services on AWS.
"""

response = client.converse(
    modelId=model_id,
    messages=messages,
    system=[{"text": system_prompt}]
)
```

The system prompt gets passed as a list containing a dictionary with a "text" key. This tells Claude what role to adopt before it sees any user messages.

## Building a Flexible Chat Function

Here's a reusable chat function that handles system prompts elegantly:

python

```
def chat(messages, system=None):
    params = {"modelId": model_id, "messages": messages}

    if system:
        params["system"] = [{"text": system}]

    response = client.converse(**params)

    return response["output"]["message"]["content"][0]["text"]
```

This approach lets you optionally include a system prompt. When no system prompt is provided, Claude responds as its default self. When you include one, Claude adopts that specific role.

## System Prompts in Action

The difference is immediately apparent when you test the same question with and without a system prompt. Ask "How do I host a Postgres database?" without a system prompt, and you'll get a comprehensive answer covering multiple cloud providers and self-hosting options.

![](https://academy.claude.com/assets/media/3068fd0afb53cb298b442ddf08066d861887d2ae5ec6cd1f965e801e9932c039.png)

With an AWS support specialist system prompt, the response focuses exclusively on AWS solutions like RDS, Aurora, and EC2-based deployments. No competitors mentioned, and the answer includes AWS-specific setup steps.

Even more impressive is how system prompts handle off-topic questions. Ask for a bread recipe with the AWS specialist prompt active, and Claude politely declines while staying in character:

![](https://academy.claude.com/assets/media/23098f708f02781a4dd30a7c21b4d0d96413f6a22840b791a63d919a0aa22832.png)

## Important Technical Details

When working with system prompts, keep these requirements in mind:

* System prompts cannot be empty strings - they must contain at least one character
* The system parameter expects a list of dictionaries with "text" keys
* System prompts are processed before any user messages in the conversation
* You can change the top-level `system` value between requests, but not partway through a single `messages` list

If you've worked with Anthropic's Claude API directly, you might know that some Claude models support mid-conversation system messages — adding a message with the `system` role to the `messages` array instead of changing the top-level field. That feature isn't available on Amazon Bedrock. In this course, you'll always set system instructions through the top-level `system` parameter on each `converse` call.

System prompts give you powerful control over AI behavior without complex rule systems. By assigning Claude a specific professional role, you get consistent, appropriate responses that naturally follow the constraints and expertise of that role.
