<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/extended-thinking -->

Lesson 39 of 67 · Building with the Claude APIExtended thinking

**Important Note: Extended Thinking is not compatible with some other features, notably message pre-filling, and it restricts how you can use temperature. See the full list of restrictions here:** [**https://platform.claude.com/docs/en/build-with-claude/thinking#limits-and-feature-compatibility**(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/thinking#limits-and-feature-compatibility)

Extended thinking is Claude's advanced reasoning feature that gives the model time to work through complex problems before generating a final response. Think of it as Claude's "scratch paper" - you can see the reasoning process that leads to the answer, which helps with transparency and often results in better quality responses.

## How Extended Thinking Works

When extended thinking is enabled, Claude's response changes from a simple text block to a structured response containing two parts:

![](https://academy.claude.com/assets/media/60d09f38b5026991011add92839f1a4c9b0d63f9f915469028e6113a6bc9e50c.jpg)

With thinking enabled, you get both the reasoning process and the final answer:

![](https://academy.claude.com/assets/media/a9c2236d86a958a619a6f9a637c7d3a09dad17867bac860f15be695d74286f07.jpg)

The key benefits include:

* Better reasoning capabilities for complex tasks
* Increased accuracy on difficult problems
* Transparency into Claude's thought process

However, there are important trade-offs:

* Higher costs (you pay for thinking tokens)
* Increased latency (thinking takes time)
* More complex response handling in your code

## When to Use Extended Thinking

The decision is straightforward: use your prompt evaluations. Run your prompts without thinking first, and if the accuracy isn't meeting your requirements after you've already optimized your prompt, then consider enabling extended thinking. It's a tool for when standard prompting isn't quite getting you there.

## Response Structure and Security

Extended thinking responses include a special signature system for security:

![](https://academy.claude.com/assets/media/a9c2236d86a958a619a6f9a637c7d3a09dad17867bac860f15be695d74286f07.jpg)

The signature is a cryptographic token that ensures you haven't modified the thinking text. This prevents developers from tampering with Claude's reasoning process, which could potentially lead the model in unsafe directions.

## Redacted Thinking

Sometimes you'll receive a redacted thinking block instead of readable reasoning text:

![](https://academy.claude.com/assets/media/8925b1f16a1ba3df971072e434b23066155a02e661f1c192f2c1515b0479b83a.jpg)

This happens when Claude's thinking process gets flagged by internal safety systems. The redacted content contains the actual thinking in encrypted form, allowing you to pass the complete message back to Claude in future conversations without losing context.

## Implementation

To enable extended thinking in your code, you need to add two parameters to your chat function:

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

The thinking budget — `budget_tokens` in the request — sets the maximum tokens Claude can use for reasoning. The minimum `budget_tokens` value is 1024, and your `max_tokens` parameter must be greater than `budget_tokens`.

Add the `thinking` parameter to your API request — an object with `type` set to `"enabled"` and a `budget_tokens` value — and raise `max_tokens` so it's greater than `budget_tokens`:

python

```
if thinking:
    params["max_tokens"] = thinking_budget + 1000
    params["thinking"] = {
        "type": "enabled",
        "budget_tokens": thinking_budget
    }
```

Then call your chat function with thinking enabled:

python

```
chat(messages, thinking=True)
```

## Testing Redacted Responses

For testing purposes, you can force Claude to return a redacted thinking block by sending a special trigger string. This helps ensure your application handles redacted responses gracefully without crashing.

Extended thinking is a powerful feature when you need Claude to tackle complex reasoning tasks, but use it judiciously given the cost and latency implications. Start with standard prompting, optimize thoroughly, then add thinking when you need that extra reasoning capability.
