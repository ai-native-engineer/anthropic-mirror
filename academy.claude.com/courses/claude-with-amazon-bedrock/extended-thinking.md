<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/extended-thinking -->

Lesson 42 of 65 · Claude with Amazon BedrockExtended thinking

Extended thinking is Claude's advanced feature that gives the model time to reason through complex problems before generating a final response. Think of it as Claude's internal monologue - you can see how it approaches your problem step by step.

![](https://academy.claude.com/assets/media/0bd1c482a9cdf3617fbf43e2386eea9cd78fe67c3ad91b25908844201784558c.png)

## How Extended Thinking Works

When you enable extended thinking, Claude's response includes two parts instead of one:

* **Reasoning Content Part** - Claude's internal thinking process
* **Text Part** - The final response you actually wanted

![](https://academy.claude.com/assets/media/7737b60029d867e83be1ad7abaea1c521cfb6cedbbad66a74b5560b6aed71a0e.png)

The reasoning content shows you exactly how Claude breaks down your problem, what it considers, and how it arrives at its final answer. This transparency can be incredibly valuable for understanding and debugging complex tasks.

## Trade-offs to Consider

Extended thinking comes with clear benefits and costs:

* **Better accuracy** on complex tasks
* **Higher cost** - you pay for all thinking tokens
* **Increased latency** - thinking takes time

The key decision point is simple: use your evaluations. If you've already optimized your prompt but still aren't getting the accuracy you need, that's when extended thinking becomes worth considering.

## The Signature System

One important detail you'll notice immediately is the cryptographic signature attached to reasoning content:

![](https://academy.claude.com/assets/media/fd50c9e46194b656ccf7369d31035d2a5459e0e1adf556a39ed535c1e2b91ced.png)

This signature ensures you can't modify the thinking text. If you want to include Claude's previous reasoning in a follow-up conversation, the signature verifies the content hasn't been tampered with. This prevents potential safety issues from modified reasoning text.

## Redacted Content

Sometimes Claude's thinking gets flagged by safety systems. When this happens, you'll receive a `redactedContent` field instead of readable thinking text:

![](https://academy.claude.com/assets/media/78c6e80cb4759302f2168576aca51757419eaf3970c816d3e0c2775ffed8dfac.png)

The redacted content is encrypted but still functional - you can pass it back to Claude in future conversations without losing context. It's just not readable to you as a developer.

## Implementation

On current Claude models, such as Claude Opus 5 and Claude Sonnet 5, thinking runs as **adaptive thinking** and is on by default: Claude decides how much reasoning each request needs, with no token budget to manage. These models omit the reasoning text unless you ask for it, so set `display` to `summarized` to see it:

python

```
additional_model_fields["thinking"] = {
    "type": "adaptive",
    "display": "summarized"
}
```

With adaptive thinking on, simple questions often come back quickly while harder ones get more reasoning time. To guide how much Claude thinks, you can combine adaptive thinking with the `effort` parameter. The effort level acts as soft guidance for Claude's thinking allocation, and it takes the place of the manual token budget you would otherwise manage.

If you've used extended thinking before, note that the manual configuration is being phased out: `thinking.type: "enabled"` with `budget_tokens` is deprecated on Claude Opus 4.6 and Claude Sonnet 4.6, and Claude Opus 4.7 and later models, including Claude Opus 5 and Claude Sonnet 5, do not support it and reject such requests with a 400 error. Use `thinking.type: "adaptive"` with the `effort` parameter instead.

### Models without adaptive thinking

The Claude 4.5 models (Claude Haiku 4.5, Claude Sonnet 4.5, and Claude Opus 4.5) and earlier models do not support adaptive thinking. On those models you enable extended thinking with a manual token budget:

python

```
additional_model_fields["thinking"] = {
    "type": "enabled",
    "budget_tokens": thinking_budget
}
```

The `thinking_budget` controls how many tokens Claude can spend on reasoning. The minimum is 1024 tokens, but you might need more for complex problems. Like everything else with Claude, use your evaluations to find the right budget for your use case.

Here's how the updated chat function looks:

python

```
def chat(
    messages,
    system=None,
    temperature=1.0,
    stop_sequences=[],
    tools=None,
    tool_choice="auto",
    text_editor=None,
    thinking=False,
    thinking_budget=1024
):
```

## Testing Your Implementation

When building applications that handle extended thinking, you'll want to test both normal reasoning content and redacted content scenarios. There's actually a special test string that forces Claude to return redacted content - useful for making sure your code handles both cases properly.

The most important takeaway about extended thinking is that the decision to use it should always be data-driven. Run your evaluations first, optimize your prompts, and only then consider extended thinking if you need that extra boost in accuracy for complex tasks. That discipline rests on a simple habit: decide what good looks like before you reach for more capability. When you know the accuracy your task needs, you can tell whether extended thinking earns its cost instead of guessing.

## Practice: run adaptive thinking yourself

Adaptive thinking is easiest to understand by watching it make decisions. In the code where you have been building the chat function, turn it on:

python

```
additional_model_fields["thinking"] = {
    "type": "adaptive",
    "display": "summarized"
}
```

Now send two requests through this same configuration. First ask a quick factual question you already know the answer to. Then ask a genuinely hard one, like a multi-step analysis problem from your own work. If you are working on a model that does not support adaptive thinking, enable thinking with the manual `budget_tokens` configuration from the section above and run the same two requests.

### Check what the thinking did

Setting the flag only proves the request was accepted. These checks tell you what the thinking did:

1. **Confirm thinking engaged.** Each response should now contain two parts, the reasoning content and the final text, instead of text alone. The one exception is redacted content, which you saw earlier: a `redactedContent` field means thinking ran but the text is encrypted.
2. **Read the reasoning content.** Check that it genuinely reasons about the question you asked rather than restating it. This is the same transparency you will rely on when debugging complex tasks later.
3. **Compare the two requests.** The simple question will usually come back quickly with little reasoning, while the hard one gets noticeably more. That difference is adaptive thinking making the allocation decision for you.
4. **Weigh the cost.** You pay for every thinking token, so check whether the harder answer is better than what you get without thinking. Your evaluations are the judge of that, and seeing reasoning text appear is no substitute for them.

The behavior worth keeping from this lesson: whenever you enable extended thinking on a new task, read the reasoning content on a few representative requests and re-run your evaluations before deciding the setting stays.
