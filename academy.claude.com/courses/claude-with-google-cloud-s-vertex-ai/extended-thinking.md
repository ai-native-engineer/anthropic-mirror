<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/extended-thinking -->

Lesson 43 of 66 · Claude with Google Cloud's Vertex AIExtended thinking

Extended thinking is Claude's advanced reasoning feature that gives the model time to think through complex problems before generating a response. When enabled, Claude produces a visible thinking process that users can examine to understand how the model approached their query.

![](https://academy.claude.com/assets/media/bcdce97e3d0ddfdf0d34acce1d47fbb6508b9b207cdfcb0a8fc215b1d301cef1.png)

This feature significantly improves Claude's ability to handle complex tasks with greater accuracy, but it comes with important trade-offs. You'll be charged for all tokens generated during the thinking phase, and the additional processing time increases response latency. The key is knowing when the improved intelligence justifies the extra cost and wait time.

## When to Use Extended Thinking

The decision to enable extended thinking should be driven by your prompt evaluations. Here's the recommended approach:

* Write and test your prompt without extended thinking first
* Run evaluations to measure accuracy
* If results aren't meeting your standards after prompt optimization efforts
* Then consider enabling extended thinking as a solution

## How Extended Thinking Changes Responses

Without extended thinking, Claude's response flow is straightforward - you send a user message with a text block and receive an assistant message with a text block in return.

![](https://academy.claude.com/assets/media/699b356c4c4251173b50811123addb4bd75c50f4b474bcf4fa98e6cad46eb538.png)

With extended thinking enabled, the response structure changes significantly. You'll receive an assistant message containing two distinct blocks:

![](https://academy.claude.com/assets/media/2cee7e788b2e5202fa9336a10501d99309ea1238cce932dfbc1199d17e0cc5ed.png)

* A `thinking` block containing Claude's reasoning process
* A `text` block with the final response

## The Signature System

Each thinking block includes a cryptographic signature that serves an important security purpose. This signature ensures that the thinking text hasn't been modified when you include the message in future conversation turns.

![](https://academy.claude.com/assets/media/87a48c18f07e4e44360d5545e511f0cbb52847e0372491f3448666efd8e19108.png)

Claude relies heavily on the thinking content for response generation, so preventing tampering is crucial for maintaining safe and consistent behavior. If you modify the thinking text, the signature validation will fail.

## Redacted Thinking

Sometimes Claude's thinking process gets flagged by internal safety systems. When this happens, you'll receive a redacted thinking block instead of the raw thinking text.

![](https://academy.claude.com/assets/media/13c20f67d2bd062e106e341bee51a8281674beb8c03beec0da189835345e8105.png)

The redacted content contains the actual thinking text in encrypted form. While you can't read it, you can still include this block in future conversation turns so Claude doesn't lose context from its previous reasoning.

## Implementation

To enable extended thinking in your code, you'll need to modify your chat function with two new parameters:

python

```
def chat(
    messages,
    system=None,
    temperature=1.0,
    stop_sequences=[],
    tools=None,
    thinking=False,
    thinking_budget=1024
):
```

The thinking budget represents the maximum tokens Claude can use for reasoning. The minimum allowed value is 1024 tokens. Importantly, your `max_tokens` parameter must exceed your thinking budget - if you set a thinking budget of 1024, `max_tokens` must be at least 1025.

In practice, you'll want a much larger buffer. For example, with a thinking budget of 1024 and `max_tokens` of 4000, Claude can use up to 1024 tokens for thinking and up to 2976 tokens for the actual response.

Add the thinking configuration to your API parameters when the feature is enabled:

python

```
if thinking:
    params["thinking"] = {
        "type": "enabled",
        "budget_tokens": thinking_budget
    }
```

## Testing Redacted Responses

During development, you may want to test how your application handles redacted thinking blocks. You can force Claude to return a redacted response by including this special trigger string in your message:

```
TRIGGER_REDACTED_THINKING_46C9A13E193C177646C7398A98432ECCCE4C1253D5E2D82641AC0E52CC2876CB
```



This ensures your error handling works correctly when encountering redacted content in production.
