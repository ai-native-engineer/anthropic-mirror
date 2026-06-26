<!-- source: https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking -->

# Adaptive thinking
Let Claude dynamically determine when and how much to use extended thinking with adaptive thinking mode.
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
Adaptive thinking is the recommended way to use [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) with Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6. On Claude Fable 5 and [Claude Mythos 5](https://anthropic.com/glasswing), thinking is always enabled and cannot be disabled; adaptive thinking is the only thinking mode. On [Claude Mythos Preview](https://anthropic.com/glasswing), adaptive thinking is the default mode and auto-applies whenever `thinking` is unset. Instead of manually setting a thinking token budget, adaptive thinking lets Claude dynamically determine when and how much to use extended thinking based on the complexity of each request. On Claude Opus 4.8 and Claude Opus 4.7, adaptive thinking is the **only** supported thinking mode; manual `thinking: {type: "enabled", budget_tokens: N}` is no longer accepted.

Adaptive thinking can drive better performance than extended thinking with a fixed `budget_tokens` for many workloads, especially bimodal tasks and long-horizon agentic workflows. No beta header is required.
If your workload requires predictable latency or precise control over thinking costs, extended thinking with `budget_tokens` is still functional on Claude Opus 4.6 and Claude Sonnet 4.6 but is deprecated and no longer recommended. See the warning below.
Supported models
Adaptive thinking is supported on the following models:
  * Claude Fable 5 (`claude-fable-5`) and Claude Mythos 5 (`claude-mythos-5`), adaptive thinking is always on; `thinking: {type: "disabled"}` is not supported
  * Claude Mythos Preview (claude-mythos-preview), adaptive thinking is the default; `thinking: {type: "disabled"}` is not supported
  * Claude Opus 4.8 (claude-opus-4-8), adaptive thinking is the only supported thinking mode. Thinking is off unless you explicitly set `thinking: {type: "adaptive"}` in your request; manual `thinking: {type: "enabled"}` is rejected with a 400 error.
  * Claude Opus 4.7 (claude-opus-4-7), adaptive thinking is the only supported thinking mode. Thinking is off unless you explicitly set `thinking: {type: "adaptive"}` in your request; manual `thinking: {type: "enabled"}` is rejected with a 400 error.
  * Claude Opus 4.6 (claude-opus-4-6)
  * Claude Sonnet 4.6 (claude-sonnet-4-6)


`thinking.type: "enabled"` and `budget_tokens` are [**deprecated**](https://platform.claude.com/docs/en/build-with-claude/overview#feature-availability) on Opus 4.6 and Sonnet 4.6 and will be removed in a future model release. Use `thinking.type: "adaptive"` with the `effort` parameter instead. Existing `budget_tokens` configurations are still functional but no longer recommended; plan to migrate.
Older models (Sonnet 4.5, Opus 4.5, etc.) do not support adaptive thinking and require `thinking.type: "enabled"` with `budget_tokens`.
How adaptive thinking works
In adaptive mode, thinking is optional for the model. Claude evaluates the complexity of each request and determines whether and how much to use extended thinking. At the default effort level (`high`), Claude almost always thinks. At lower effort levels, Claude may skip thinking for simpler problems.
Adaptive thinking also automatically enables [interleaved thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#interleaved-thinking). This means Claude can think between tool calls, making it especially effective for agentic workflows.
How to use adaptive thinking
Set `thinking.type` to `"adaptive"` in your API request:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    messages=[
            "role": "user",
            "content": "Explain why the sum of two even numbers is always even.",
    ],
)

for block in response.content:
    if block.type == "thinking":
        print(f"\nThinking: {block.thinking}")
    elif block.type == "text":
        print(f"\nResponse: {block.text}")

Adaptive thinking with the effort parameter
You can combine adaptive thinking with the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) to guide how much thinking Claude does. The effort level acts as soft guidance for Claude's thinking allocation:  
| Effort level  | Thinking behavior  |  
| --- | --- |  
| `max`  | Claude always thinks with no constraints on thinking depth. Available on Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6.  |  
| `xhigh`  | Claude always thinks deeply with extended exploration. Available on Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, and Claude Opus 4.7.  |  
|  `high` (default)  | Claude almost always thinks. Provides deep reasoning on complex tasks.  |  
| `medium`  | Claude uses moderate thinking. May skip thinking for very simple queries.  |  
| `low`  | Claude minimizes thinking. Skips thinking for simple tasks where speed matters most.  |  
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "medium"},
    messages=[{"role": "user", "content": "What is the capital of France?"}],
)

print(response.content[0].text)

Streaming with adaptive thinking
Adaptive thinking works seamlessly with [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming). Thinking blocks are streamed via `thinking_delta` events just like manual thinking mode:
CLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    messages=[
            "role": "user",
            "content": "What is the greatest common divisor of 1071 and 462?",
    ],
) as stream:
    for event in stream:
        if event.type == "content_block_start":
            print(f"\nStarting {event.content_block.type} block...")
        elif event.type == "content_block_delta":
            if event.delta.type == "thinking_delta":
                print(event.delta.thinking, end="", flush=True)
            elif event.delta.type == "text_delta":
                print(event.delta.text, end="", flush=True)

Adaptive vs manual vs disabled thinking  
| Mode  | Config  | Availability  | When to use  |  
| --- | --- | --- | --- |  
| **Adaptive**  | `thinking: {type: "adaptive"}`  | Claude Fable 5 (always on), Claude Mythos 5 (always on), Claude Mythos Preview (default), Claude Opus 4.8 (only mode), Opus 4.7 (only mode), Opus 4.6, Sonnet 4.6  | Claude determines when and how much to use extended thinking. Use `effort` to guide.  |  
| **Manual**  | `thinking: {type: "enabled", budget_tokens: N}`  | All models except Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, and Claude Opus 4.7 (rejected with a 400 error). Deprecated on Opus 4.6 and Sonnet 4.6 (consider adaptive mode instead).  | When you need precise control over thinking token spend.  |  
| **Disabled**  | Omit `thinking` parameter or pass `{type: "disabled"}`  | All models except Claude Fable 5, Claude Mythos 5, and Claude Mythos Preview  | When you don't need extended thinking and want the lowest latency.  |  
Adaptive thinking is available on Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, Claude Opus 4.8, Claude Opus 4.7, Opus 4.6, and Sonnet 4.6. On Claude Fable 5 and Claude Mythos 5, adaptive thinking is always on: it applies whenever `thinking` is unset and cannot be disabled. On Mythos Preview, adaptive thinking is the default and applies automatically whenever `thinking` is unset. On Claude Opus 4.8, adaptive thinking is the only supported mode; thinking is off unless you explicitly set `thinking: {type: "adaptive"}`, and manual `type: "enabled"` with `budget_tokens` is rejected with a 400 error. On Claude Opus 4.7, adaptive thinking is the only supported mode and `type: "enabled"` with `budget_tokens` is rejected. Older models only support `type: "enabled"` with `budget_tokens`. On Opus 4.6 and Sonnet 4.6, `type: "enabled"` with `budget_tokens` is still functional but deprecated.
**Interleaved thinking availability by mode:**
  * **Adaptive mode:** Interleaved thinking is automatically enabled on Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, Claude Opus 4.8, Claude Opus 4.7, Opus 4.6, and Sonnet 4.6. On Claude Fable 5, Claude Mythos 5, Mythos Preview, Claude Opus 4.8, and Opus 4.7, inter-tool reasoning always lives inside thinking blocks.
  * **Manual mode on Sonnet 4.6:** Interleaved thinking works through the `interleaved-thinking-2025-05-14` beta header.
  * **Manual mode on Opus 4.6:** Interleaved thinking is not available. If your agentic workflow requires thinking between tool calls on Opus 4.6, use adaptive mode.

Important considerations
### 
Validation changes
When using adaptive thinking, previous assistant turns don't need to start with thinking blocks. This is more flexible than manual mode, where the API enforces that thinking-enabled turns begin with a thinking block.
### 
Prompt caching
Consecutive requests using `adaptive` thinking preserve [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) breakpoints. However, switching between `adaptive` and `enabled`/`disabled` thinking modes breaks cache breakpoints for messages. System prompts and tool definitions remain cached regardless of mode changes.
### 
Tuning thinking behavior
Adaptive thinking's triggering behavior is promptable. If Claude is thinking more or less often than you'd like, you can add guidance to your system prompt:

Extended thinking adds latency and should only be used when it
will meaningfully improve answer quality — typically for problems
that require multi-step reasoning. When in doubt, respond directly.

To encourage thinking instead, use a phrase like:

This task involves multi-step reasoning. Think carefully before responding.

Steering effectiveness can be sensitive to exact wording — if one phrasing doesn't produce the behavior you want, try a more direct variant.
You can also steer thinking on a per-message basis from the user turn. Appending `"Please think hard before responding."` to a user message encourages Claude to think on that turn; `"Answer directly without deliberating."` suppresses it. This works independently of the system prompt and is useful when only some requests in a conversation warrant extended reasoning.

Steering Claude to think less often may reduce quality on tasks that benefit from reasoning. Measure the impact on your specific workloads before deploying prompt-based tuning to production. Consider testing with lower [effort levels](https://platform.claude.com/docs/en/build-with-claude/effort) first.
### 
Cost control
Use `max_tokens` as a hard limit on total output (thinking + response text). The `effort` parameter provides additional soft guidance on how much thinking Claude allocates. Together, these give you effective control over cost.
At `high` and `max` effort levels, Claude may think more extensively and can be more likely to exhaust the `max_tokens` budget. If you observe `stop_reason: "max_tokens"` in responses, consider increasing `max_tokens` to give the model more room, or lowering the effort level.
Working with thinking blocks
The following concepts apply to all models that support extended thinking, regardless of whether you use adaptive or manual mode.
### 
Summarized thinking
With extended thinking enabled, the Messages API for Claude 4 models returns a summary of Claude's full thinking process. Summarized thinking provides the full intelligence benefits of extended thinking, while preventing misuse. This is the default behavior on Claude 4 models when the `display` field on the thinking configuration is unset or set to `"summarized"`. On Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, and [Claude Mythos Preview](https://anthropic.com/glasswing), `display` defaults to `"omitted"` instead, so you must set `display: "summarized"` explicitly to receive summarized thinking.
Here are some important considerations for summarized thinking:
  * You're charged for the full thinking tokens generated by the original request, not the summary tokens.
  * The billed output token count will **not match** the count of tokens you see in the response.
  * On Claude 4 models, the first few lines of thinking output are more verbose, providing detailed reasoning that's particularly helpful for prompt engineering purposes. [Claude Mythos Preview](https://anthropic.com/glasswing) summarizes from the first token, so its thinking blocks do not show this verbose preamble.
  * As Anthropic seeks to improve the extended thinking feature, summarization behavior is subject to change.
  * Summarization preserves the key ideas of Claude's thinking process with minimal added latency, enabling a streamable user experience.
  * Summarization is processed by a different model than the one you target in your requests. The thinking model does not see the summarized output.

In rare cases where you need access to full thinking output for Claude 4 models, contact Anthropic sales.
### 
Controlling thinking display
The `display` field on the thinking configuration controls how thinking content is returned in API responses. It accepts two values:
  * `"summarized"`: Thinking blocks contain summarized thinking text. See [Summarized thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#summarized-thinking) for details. This is the default on Claude Opus 4.6, Claude Sonnet 4.6, and earlier Claude 4 models.
  * `"omitted"`: Thinking blocks are returned with an empty `thinking` field. The `signature` field still carries the encrypted full thinking for multi-turn continuity (see [Thinking encryption](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#thinking-encryption)). This is the default on Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, and [Claude Mythos Preview](https://anthropic.com/glasswing).

Setting `display: "omitted"` is useful when your application doesn't surface thinking content to users. The primary benefit is **faster time-to-first-text-token when streaming:** The server skips streaming thinking tokens entirely and delivers only the signature, so the final text response begins streaming sooner.
Here are some important considerations for omitted thinking:
  * You're still charged for the full thinking tokens. Omitting reduces latency, not cost.
  * If you pass thinking blocks back in multi-turn conversations, pass them unchanged. The server decrypts the `signature` to reconstruct the original thinking for prompt construction (see [Preserving thinking blocks](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#preserving-thinking-blocks)). Any text you place in the `thinking` field of a round-tripped omitted block is ignored.
  * `display` is invalid with `thinking.type: "disabled"` (there is nothing to display).
  * When using `thinking.type: "adaptive"` and the model skips thinking for a simple request, no thinking block is produced regardless of `display`.

The `signature` field is identical whether `display` is `"summarized"` or `"omitted"`. Switching `display` values between turns in a conversation is supported.
The `display` setting controls visibility only. Under every setting, thinking happens and is billed the same.
The default for `thinking.display` depends on the model:
  * **Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, and[Claude Mythos Preview](https://anthropic.com/glasswing):** the default is `"omitted"`. Thinking blocks still appear in the response stream, but their `thinking` field is empty unless you explicitly opt in. This is a silent change from Claude Opus 4.6, where the default was `"summarized"`.
  * **Claude Opus 4.6:** the default is `"summarized"`. The readable summary appears without opting in.

To receive summarized thinking text on models where the default is `"omitted"`, set `thinking.display` to `"summarized"` explicitly:

thinking = {
    "type": "adaptive",
    "display": "summarized",

For code examples and streaming behavior with `display: "omitted"`, see [Controlling thinking display](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#controlling-thinking-display) on the extended thinking page. The examples there use `type: "enabled"`; with adaptive thinking, use:

thinking = {"type": "adaptive", "display": "omitted"}

### 
Thinking encryption
Full thinking content is encrypted and returned in the `signature` field. This field is used to verify that thinking blocks were generated by Claude when passed back to the API.
It is only strictly necessary to send back thinking blocks when using [tools with extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-tool-use). Otherwise you can omit thinking blocks from previous turns. If you pass them back, whether the API keeps or strips them depends on the model: Opus 4.5+ and Sonnet 4.6+ keep them in context by default; earlier Opus/Sonnet models and all Haiku models strip them. See [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) to configure this.
If sending back thinking blocks, pass everything back as you received it for consistency and to avoid potential issues.
Here are some important considerations on thinking encryption:
  * When [streaming responses](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#streaming-thinking), the signature is added via a `signature_delta` inside a `content_block_delta` event just before the `content_block_stop` event.
  * `signature` values are significantly longer in Claude 4 models than in previous models.
  * The `signature` field is an opaque field and should not be interpreted or parsed.
  * `signature` values are compatible across platforms (Claude APIs, [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), and [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)). Values generated on one platform will be compatible with another.

### 
Thinking output on Claude Fable 5 and Claude Mythos 5
On Claude Fable 5 and Claude Mythos 5, the raw chain of thought is never returned. The thinking blocks you receive are regular `thinking` blocks, not `redacted_thinking`. The `thinking.display` setting works the same as on other models:
  * `"summarized"` returns a readable summary of the reasoning.
  * `"omitted"` (the default on these models) still includes `thinking` blocks in responses, but their `thinking` field is an empty string.

For the response shape of thinking blocks, see the [Messages API reference](https://platform.claude.com/docs/en/api/messages/create).
When continuing a conversation on the same model, pass each thinking block back to the API exactly as received, including blocks whose `thinking` field is empty. Don't edit or reconstruct them. Reading the summary text for display is fine: the API rejects blocks whose content has been modified, not blocks you have read.
When you switch models, for example after a [classifier refusal fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback), strip `thinking` and `redacted_thinking` blocks from prior assistant turns. Thinking blocks are tied to the model that produced them. Other models silently ignore them rather than rejecting the request, but ignored blocks still add input tokens.
Two exceptions, covered in [Fallback credit](https://platform.claude.com/docs/en/build-with-claude/fallback-credit):
  * Fallback-credit retries must echo the refused request body unchanged.
  * `fallback` blocks from a mid-output fallback stay where they appeared.

To get visibility into the model's reasoning, read the `thinking` blocks described in this section rather than prompting for reasoning in the response text. On Claude Fable 5, a request that attempts to elicit the model's internal reasoning as part of the response text can be refused with `stop_details.category: "reasoning_extraction"`. See [Refusal categories](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response) for the field reference and handling guidance.
### 
Pricing
For complete pricing information including base rates, cache writes, cache hits, and output tokens, see the [pricing page](https://platform.claude.com/docs/en/about-claude/pricing).
The thinking process incurs charges for:
  * Tokens used during thinking (output tokens)
  * Thinking blocks from prior assistant turns kept in context: only the last turn on earlier Opus/Sonnet models and all Haiku models; all turns by default on Opus 4.5+ and Sonnet 4.6+ (input tokens)
  * Standard text output tokens

When extended thinking is enabled, a specialized system prompt is automatically included to support this feature.
When using summarized thinking:
  * **Input tokens:** Tokens in your original request (excludes thinking tokens from previous turns)
  * **Output tokens (billed):** The original thinking tokens that Claude generated internally
  * **Output tokens (visible):** The summarized thinking tokens you see in the response
  * **No charge:** Tokens used to generate the summary

When using `display: "omitted"`:
  * **Input tokens:** Tokens in your original request (same as summarized)
  * **Output tokens (billed):** The original thinking tokens that Claude generated internally (same as summarized)
  * **Output tokens (visible):** Zero thinking tokens (the `thinking` field is empty)


The billed output token count will **not** match the visible token count in the response. You are billed for the full thinking process, not the thinking content visible in the response.
To see how many billed output tokens were spent on internal reasoning, read `usage.output_tokens_details.thinking_tokens` in the response. This value reflects the raw reasoning the model generated (not the summarized text returned in the body) and is always less than or equal to `output_tokens`. Subtract it from `output_tokens` to approximate the non-reasoning portion of the output.

  "usage": {
    "input_tokens": 25,
    "output_tokens": 348,
    "output_tokens_details": {
      "thinking_tokens": 312

`output_tokens` remains the inclusive, authoritative total used for billing. `output_tokens_details` is a read-only breakdown for observability.
### 
Additional topics
The extended thinking page covers several topics in more detail with mode-specific code examples:
  * **[Tool use with thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-tool-use)** : The same rules apply for adaptive thinking: preserve thinking blocks between tool calls and be aware of `tool_choice` limitations when thinking is active.
  * **[Prompt caching](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-prompt-caching)** : With adaptive thinking, consecutive requests using the same thinking mode preserve cache breakpoints. Switching between `adaptive` and `enabled`/`disabled` modes breaks cache breakpoints for messages (system prompts and tool definitions remain cached).
  * **[Context windows](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#max-tokens-and-context-window-size-with-extended-thinking)** : How thinking tokens interact with `max_tokens` and context window limits.

Next steps
[  Extended thinking Learn more about extended thinking, including manual mode, tool use, and prompt caching. ](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)[ Effort parameter Control how thoroughly Claude responds with the effort parameter. ](https://platform.claude.com/docs/en/build-with-claude/effort)
  * [Supported models](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#supported-models)
  * [How adaptive thinking works](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#how-adaptive-thinking-works)
  * [How to use adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#how-to-use-adaptive-thinking)
  * [Adaptive thinking with the effort parameter](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#adaptive-thinking-with-the-effort-parameter)
  * [Streaming with adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#streaming-with-adaptive-thinking)
  * [Adaptive vs manual vs disabled thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#adaptive-vs-manual-vs-disabled-thinking)
  * [Important considerations](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#important-considerations)
  * [Validation changes](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#validation-changes)
  * [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#prompt-caching)
  * [Tuning thinking behavior](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#tuning-thinking-behavior)
  * [Cost control](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#cost-control)
  * [Working with thinking blocks](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#working-with-thinking-blocks)
  * [Summarized thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#summarized-thinking)
  * [Controlling thinking display](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#controlling-thinking-display)
  * [Thinking encryption](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#thinking-encryption)
  * [Thinking output on Claude Fable 5 and Claude Mythos 5](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#thinking-output-on-claude-fable-5-and-claude-mythos-5)
  * [Pricing](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#pricing)
  * [Additional topics](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#additional-topics)
  * [Next steps](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#next-steps)

Messages/Model capabilities
# Adaptive thinking
Let Claude dynamically determine when and how much to use extended thinking with adaptive thinking mode.
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
Adaptive thinking is the recommended way to use [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) with Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6. On Claude Fable 5 and [Claude Mythos 5](https://anthropic.com/glasswing), thinking is always enabled and cannot be disabled; adaptive thinking is the only thinking mode. On [Claude Mythos Preview](https://anthropic.com/glasswing), adaptive thinking is the default mode and auto-applies whenever `thinking` is unset. Instead of manually setting a thinking token budget, adaptive thinking lets Claude dynamically determine when and how much to use extended thinking based on the complexity of each request. On Claude Opus 4.8 and Claude Opus 4.7, adaptive thinking is the **only** supported thinking mode; manual `thinking: {type: "enabled", budget_tokens: N}` is no longer accepted.

Adaptive thinking can drive better performance than extended thinking with a fixed `budget_tokens` for many workloads, especially bimodal tasks and long-horizon agentic workflows. No beta header is required.
If your workload requires predictable latency or precise control over thinking costs, extended thinking with `budget_tokens` is still functional on Claude Opus 4.6 and Claude Sonnet 4.6 but is deprecated and no longer recommended. See the warning below.
Supported models
Adaptive thinking is supported on the following models:
  * Claude Fable 5 (`claude-fable-5`) and Claude Mythos 5 (`claude-mythos-5`), adaptive thinking is always on; `thinking: {type: "disabled"}` is not supported
  * Claude Mythos Preview (claude-mythos-preview), adaptive thinking is the default; `thinking: {type: "disabled"}` is not supported
  * Claude Opus 4.8 (claude-opus-4-8), adaptive thinking is the only supported thinking mode. Thinking is off unless you explicitly set `thinking: {type: "adaptive"}` in your request; manual `thinking: {type: "enabled"}` is rejected with a 400 error.
  * Claude Opus 4.7 (claude-opus-4-7), adaptive thinking is the only supported thinking mode. Thinking is off unless you explicitly set `thinking: {type: "adaptive"}` in your request; manual `thinking: {type: "enabled"}` is rejected with a 400 error.
  * Claude Opus 4.6 (claude-opus-4-6)
  * Claude Sonnet 4.6 (claude-sonnet-4-6)


`thinking.type: "enabled"` and `budget_tokens` are [**deprecated**](https://platform.claude.com/docs/en/build-with-claude/overview#feature-availability) on Opus 4.6 and Sonnet 4.6 and will be removed in a future model release. Use `thinking.type: "adaptive"` with the `effort` parameter instead. Existing `budget_tokens` configurations are still functional but no longer recommended; plan to migrate.
Older models (Sonnet 4.5, Opus 4.5, etc.) do not support adaptive thinking and require `thinking.type: "enabled"` with `budget_tokens`.
How adaptive thinking works
In adaptive mode, thinking is optional for the model. Claude evaluates the complexity of each request and determines whether and how much to use extended thinking. At the default effort level (`high`), Claude almost always thinks. At lower effort levels, Claude may skip thinking for simpler problems.
Adaptive thinking also automatically enables [interleaved thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#interleaved-thinking). This means Claude can think between tool calls, making it especially effective for agentic workflows.
How to use adaptive thinking
Set `thinking.type` to `"adaptive"` in your API request:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    messages=[
            "role": "user",
            "content": "Explain why the sum of two even numbers is always even.",
    ],
)

for block in response.content:
    if block.type == "thinking":
        print(f"\nThinking: {block.thinking}")
    elif block.type == "text":
        print(f"\nResponse: {block.text}")

Adaptive thinking with the effort parameter
You can combine adaptive thinking with the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) to guide how much thinking Claude does. The effort level acts as soft guidance for Claude's thinking allocation:  
| Effort level  | Thinking behavior  |  
| --- | --- |  
| `max`  | Claude always thinks with no constraints on thinking depth. Available on Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6.  |  
| `xhigh`  | Claude always thinks deeply with extended exploration. Available on Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, and Claude Opus 4.7.  |  
|  `high` (default)  | Claude almost always thinks. Provides deep reasoning on complex tasks.  |  
| `medium`  | Claude uses moderate thinking. May skip thinking for very simple queries.  |  
| `low`  | Claude minimizes thinking. Skips thinking for simple tasks where speed matters most.  |  
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "medium"},
    messages=[{"role": "user", "content": "What is the capital of France?"}],
)

print(response.content[0].text)

Streaming with adaptive thinking
Adaptive thinking works seamlessly with [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming). Thinking blocks are streamed via `thinking_delta` events just like manual thinking mode:
CLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    messages=[
            "role": "user",
            "content": "What is the greatest common divisor of 1071 and 462?",
    ],
) as stream:
    for event in stream:
        if event.type == "content_block_start":
            print(f"\nStarting {event.content_block.type} block...")
        elif event.type == "content_block_delta":
            if event.delta.type == "thinking_delta":
                print(event.delta.thinking, end="", flush=True)
            elif event.delta.type == "text_delta":
                print(event.delta.text, end="", flush=True)

Adaptive vs manual vs disabled thinking  
| Mode  | Config  | Availability  | When to use  |  
| --- | --- | --- | --- |  
| **Adaptive**  | `thinking: {type: "adaptive"}`  | Claude Fable 5 (always on), Claude Mythos 5 (always on), Claude Mythos Preview (default), Claude Opus 4.8 (only mode), Opus 4.7 (only mode), Opus 4.6, Sonnet 4.6  | Claude determines when and how much to use extended thinking. Use `effort` to guide.  |  
| **Manual**  | `thinking: {type: "enabled", budget_tokens: N}`  | All models except Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, and Claude Opus 4.7 (rejected with a 400 error). Deprecated on Opus 4.6 and Sonnet 4.6 (consider adaptive mode instead).  | When you need precise control over thinking token spend.  |  
| **Disabled**  | Omit `thinking` parameter or pass `{type: "disabled"}`  | All models except Claude Fable 5, Claude Mythos 5, and Claude Mythos Preview  | When you don't need extended thinking and want the lowest latency.  |  
Adaptive thinking is available on Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, Claude Opus 4.8, Claude Opus 4.7, Opus 4.6, and Sonnet 4.6. On Claude Fable 5 and Claude Mythos 5, adaptive thinking is always on: it applies whenever `thinking` is unset and cannot be disabled. On Mythos Preview, adaptive thinking is the default and applies automatically whenever `thinking` is unset. On Claude Opus 4.8, adaptive thinking is the only supported mode; thinking is off unless you explicitly set `thinking: {type: "adaptive"}`, and manual `type: "enabled"` with `budget_tokens` is rejected with a 400 error. On Claude Opus 4.7, adaptive thinking is the only supported mode and `type: "enabled"` with `budget_tokens` is rejected. Older models only support `type: "enabled"` with `budget_tokens`. On Opus 4.6 and Sonnet 4.6, `type: "enabled"` with `budget_tokens` is still functional but deprecated.
**Interleaved thinking availability by mode:**
  * **Adaptive mode:** Interleaved thinking is automatically enabled on Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, Claude Opus 4.8, Claude Opus 4.7, Opus 4.6, and Sonnet 4.6. On Claude Fable 5, Claude Mythos 5, Mythos Preview, Claude Opus 4.8, and Opus 4.7, inter-tool reasoning always lives inside thinking blocks.
  * **Manual mode on Sonnet 4.6:** Interleaved thinking works through the `interleaved-thinking-2025-05-14` beta header.
  * **Manual mode on Opus 4.6:** Interleaved thinking is not available. If your agentic workflow requires thinking between tool calls on Opus 4.6, use adaptive mode.

Important considerations
### 
Validation changes
When using adaptive thinking, previous assistant turns don't need to start with thinking blocks. This is more flexible than manual mode, where the API enforces that thinking-enabled turns begin with a thinking block.
### 
Prompt caching
Consecutive requests using `adaptive` thinking preserve [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) breakpoints. However, switching between `adaptive` and `enabled`/`disabled` thinking modes breaks cache breakpoints for messages. System prompts and tool definitions remain cached regardless of mode changes.
### 
Tuning thinking behavior
Adaptive thinking's triggering behavior is promptable. If Claude is thinking more or less often than you'd like, you can add guidance to your system prompt:

Extended thinking adds latency and should only be used when it
will meaningfully improve answer quality — typically for problems
that require multi-step reasoning. When in doubt, respond directly.

To encourage thinking instead, use a phrase like:

This task involves multi-step reasoning. Think carefully before responding.

Steering effectiveness can be sensitive to exact wording — if one phrasing doesn't produce the behavior you want, try a more direct variant.
You can also steer thinking on a per-message basis from the user turn. Appending `"Please think hard before responding."` to a user message encourages Claude to think on that turn; `"Answer directly without deliberating."` suppresses it. This works independently of the system prompt and is useful when only some requests in a conversation warrant extended reasoning.

Steering Claude to think less often may reduce quality on tasks that benefit from reasoning. Measure the impact on your specific workloads before deploying prompt-based tuning to production. Consider testing with lower [effort levels](https://platform.claude.com/docs/en/build-with-claude/effort) first.
### 
Cost control
Use `max_tokens` as a hard limit on total output (thinking + response text). The `effort` parameter provides additional soft guidance on how much thinking Claude allocates. Together, these give you effective control over cost.
At `high` and `max` effort levels, Claude may think more extensively and can be more likely to exhaust the `max_tokens` budget. If you observe `stop_reason: "max_tokens"` in responses, consider increasing `max_tokens` to give the model more room, or lowering the effort level.
Working with thinking blocks
The following concepts apply to all models that support extended thinking, regardless of whether you use adaptive or manual mode.
### 
Summarized thinking
With extended thinking enabled, the Messages API for Claude 4 models returns a summary of Claude's full thinking process. Summarized thinking provides the full intelligence benefits of extended thinking, while preventing misuse. This is the default behavior on Claude 4 models when the `display` field on the thinking configuration is unset or set to `"summarized"`. On Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, and [Claude Mythos Preview](https://anthropic.com/glasswing), `display` defaults to `"omitted"` instead, so you must set `display: "summarized"` explicitly to receive summarized thinking.
Here are some important considerations for summarized thinking:
  * You're charged for the full thinking tokens generated by the original request, not the summary tokens.
  * The billed output token count will **not match** the count of tokens you see in the response.
  * On Claude 4 models, the first few lines of thinking output are more verbose, providing detailed reasoning that's particularly helpful for prompt engineering purposes. [Claude Mythos Preview](https://anthropic.com/glasswing) summarizes from the first token, so its thinking blocks do not show this verbose preamble.
  * As Anthropic seeks to improve the extended thinking feature, summarization behavior is subject to change.
  * Summarization preserves the key ideas of Claude's thinking process with minimal added latency, enabling a streamable user experience.
  * Summarization is processed by a different model than the one you target in your requests. The thinking model does not see the summarized output.

In rare cases where you need access to full thinking output for Claude 4 models, contact Anthropic sales.
### 
Controlling thinking display
The `display` field on the thinking configuration controls how thinking content is returned in API responses. It accepts two values:
  * `"summarized"`: Thinking blocks contain summarized thinking text. See [Summarized thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#summarized-thinking) for details. This is the default on Claude Opus 4.6, Claude Sonnet 4.6, and earlier Claude 4 models.
  * `"omitted"`: Thinking blocks are returned with an empty `thinking` field. The `signature` field still carries the encrypted full thinking for multi-turn continuity (see [Thinking encryption](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#thinking-encryption)). This is the default on Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, and [Claude Mythos Preview](https://anthropic.com/glasswing).

Setting `display: "omitted"` is useful when your application doesn't surface thinking content to users. The primary benefit is **faster time-to-first-text-token when streaming:** The server skips streaming thinking tokens entirely and delivers only the signature, so the final text response begins streaming sooner.
Here are some important considerations for omitted thinking:
  * You're still charged for the full thinking tokens. Omitting reduces latency, not cost.
  * If you pass thinking blocks back in multi-turn conversations, pass them unchanged. The server decrypts the `signature` to reconstruct the original thinking for prompt construction (see [Preserving thinking blocks](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#preserving-thinking-blocks)). Any text you place in the `thinking` field of a round-tripped omitted block is ignored.
  * `display` is invalid with `thinking.type: "disabled"` (there is nothing to display).
  * When using `thinking.type: "adaptive"` and the model skips thinking for a simple request, no thinking block is produced regardless of `display`.

The `signature` field is identical whether `display` is `"summarized"` or `"omitted"`. Switching `display` values between turns in a conversation is supported.
The `display` setting controls visibility only. Under every setting, thinking happens and is billed the same.
The default for `thinking.display` depends on the model:
  * **Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, and[Claude Mythos Preview](https://anthropic.com/glasswing):** the default is `"omitted"`. Thinking blocks still appear in the response stream, but their `thinking` field is empty unless you explicitly opt in. This is a silent change from Claude Opus 4.6, where the default was `"summarized"`.
  * **Claude Opus 4.6:** the default is `"summarized"`. The readable summary appears without opting in.

To receive summarized thinking text on models where the default is `"omitted"`, set `thinking.display` to `"summarized"` explicitly:

thinking = {
    "type": "adaptive",
    "display": "summarized",

For code examples and streaming behavior with `display: "omitted"`, see [Controlling thinking display](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#controlling-thinking-display) on the extended thinking page. The examples there use `type: "enabled"`; with adaptive thinking, use:

thinking = {"type": "adaptive", "display": "omitted"}

### 
Thinking encryption
Full thinking content is encrypted and returned in the `signature` field. This field is used to verify that thinking blocks were generated by Claude when passed back to the API.
It is only strictly necessary to send back thinking blocks when using [tools with extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-tool-use). Otherwise you can omit thinking blocks from previous turns. If you pass them back, whether the API keeps or strips them depends on the model: Opus 4.5+ and Sonnet 4.6+ keep them in context by default; earlier Opus/Sonnet models and all Haiku models strip them. See [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) to configure this.
If sending back thinking blocks, pass everything back as you received it for consistency and to avoid potential issues.
Here are some important considerations on thinking encryption:
  * When [streaming responses](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#streaming-thinking), the signature is added via a `signature_delta` inside a `content_block_delta` event just before the `content_block_stop` event.
  * `signature` values are significantly longer in Claude 4 models than in previous models.
  * The `signature` field is an opaque field and should not be interpreted or parsed.
  * `signature` values are compatible across platforms (Claude APIs, [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), and [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)). Values generated on one platform will be compatible with another.

### 
Thinking output on Claude Fable 5 and Claude Mythos 5
On Claude Fable 5 and Claude Mythos 5, the raw chain of thought is never returned. The thinking blocks you receive are regular `thinking` blocks, not `redacted_thinking`. The `thinking.display` setting works the same as on other models:
  * `"summarized"` returns a readable summary of the reasoning.
  * `"omitted"` (the default on these models) still includes `thinking` blocks in responses, but their `thinking` field is an empty string.

For the response shape of thinking blocks, see the [Messages API reference](https://platform.claude.com/docs/en/api/messages/create).
When continuing a conversation on the same model, pass each thinking block back to the API exactly as received, including blocks whose `thinking` field is empty. Don't edit or reconstruct them. Reading the summary text for display is fine: the API rejects blocks whose content has been modified, not blocks you have read.
When you switch models, for example after a [classifier refusal fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback), strip `thinking` and `redacted_thinking` blocks from prior assistant turns. Thinking blocks are tied to the model that produced them. Other models silently ignore them rather than rejecting the request, but ignored blocks still add input tokens.
Two exceptions, covered in [Fallback credit](https://platform.claude.com/docs/en/build-with-claude/fallback-credit):
  * Fallback-credit retries must echo the refused request body unchanged.
  * `fallback` blocks from a mid-output fallback stay where they appeared.

To get visibility into the model's reasoning, read the `thinking` blocks described in this section rather than prompting for reasoning in the response text. On Claude Fable 5, a request that attempts to elicit the model's internal reasoning as part of the response text can be refused with `stop_details.category: "reasoning_extraction"`. See [Refusal categories](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response) for the field reference and handling guidance.
### 
Pricing
For complete pricing information including base rates, cache writes, cache hits, and output tokens, see the [pricing page](https://platform.claude.com/docs/en/about-claude/pricing).
The thinking process incurs charges for:
  * Tokens used during thinking (output tokens)
  * Thinking blocks from prior assistant turns kept in context: only the last turn on earlier Opus/Sonnet models and all Haiku models; all turns by default on Opus 4.5+ and Sonnet 4.6+ (input tokens)
  * Standard text output tokens

When extended thinking is enabled, a specialized system prompt is automatically included to support this feature.
When using summarized thinking:
  * **Input tokens:** Tokens in your original request (excludes thinking tokens from previous turns)
  * **Output tokens (billed):** The original thinking tokens that Claude generated internally
  * **Output tokens (visible):** The summarized thinking tokens you see in the response
  * **No charge:** Tokens used to generate the summary

When using `display: "omitted"`:
  * **Input tokens:** Tokens in your original request (same as summarized)
  * **Output tokens (billed):** The original thinking tokens that Claude generated internally (same as summarized)
  * **Output tokens (visible):** Zero thinking tokens (the `thinking` field is empty)


The billed output token count will **not** match the visible token count in the response. You are billed for the full thinking process, not the thinking content visible in the response.
To see how many billed output tokens were spent on internal reasoning, read `usage.output_tokens_details.thinking_tokens` in the response. This value reflects the raw reasoning the model generated (not the summarized text returned in the body) and is always less than or equal to `output_tokens`. Subtract it from `output_tokens` to approximate the non-reasoning portion of the output.

  "usage": {
    "input_tokens": 25,
    "output_tokens": 348,
    "output_tokens_details": {
      "thinking_tokens": 312

`output_tokens` remains the inclusive, authoritative total used for billing. `output_tokens_details` is a read-only breakdown for observability.
### 
Additional topics
The extended thinking page covers several topics in more detail with mode-specific code examples:
  * **[Tool use with thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-tool-use)** : The same rules apply for adaptive thinking: preserve thinking blocks between tool calls and be aware of `tool_choice` limitations when thinking is active.
  * **[Prompt caching](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-prompt-caching)** : With adaptive thinking, consecutive requests using the same thinking mode preserve cache breakpoints. Switching between `adaptive` and `enabled`/`disabled` modes breaks cache breakpoints for messages (system prompts and tool definitions remain cached).
  * **[Context windows](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#max-tokens-and-context-window-size-with-extended-thinking)** : How thinking tokens interact with `max_tokens` and context window limits.

Next steps
[  Extended thinking Learn more about extended thinking, including manual mode, tool use, and prompt caching. ](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)[ Effort parameter Control how thoroughly Claude responds with the effort parameter. ](https://platform.claude.com/docs/en/build-with-claude/effort)
