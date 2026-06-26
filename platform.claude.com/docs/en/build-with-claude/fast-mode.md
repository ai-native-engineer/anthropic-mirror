<!-- source: https://platform.claude.com/docs/en/build-with-claude/fast-mode -->

# Fast mode (research preview)
Get up to 2.5x higher output tokens per second from Claude Opus models.
Fast mode delivers up to 2.5x higher output tokens per second from Claude Opus 4.8, Claude Opus 4.7, and Claude Opus 4.6 at premium pricing. Set `speed: "fast"` with the `fast-mode-2026-02-01` beta header on your request to opt in.
Fast mode is in research preview. Contact your account manager to request access. If you do not have an account manager, [join the waitlist](https://claude.com/fast-mode) for fast mode.
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
Supported models
Fast mode is supported on the following models:
  * Claude Opus 4.8 (claude-opus-4-8)
  * Claude Opus 4.7 (claude-opus-4-7)
  * Claude Opus 4.6 (claude-opus-4-6)

Fast mode for Claude Opus 4.8 launches as a research preview on the Claude API, including [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), only. It is not available on third-party platforms, including Amazon Bedrock, Google Cloud, and Microsoft Foundry.

Fast mode for Claude Opus 4.6 is deprecated as of the Claude Opus 4.8 launch and will be removed approximately 30 days later. After removal, requests to `claude-opus-4-6` with `speed: "fast"` will fall back to standard speed at standard pricing rather than return an error. Migrate to fast mode for Claude Opus 4.8 or Claude Opus 4.7 to keep the speedup.
How fast mode works
Fast mode runs the same model with a faster inference configuration. There is no change to intelligence or capabilities.
  * Up to 2.5x higher output tokens per second compared to standard speed
  * Speed benefits are focused on output tokens per second (OTPS), not time to first token (TTFT)
  * Same model weights and behavior (not a different model)
  * Compatible with [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming), where the OTPS gain is most visible

Basic usage
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[
        {"role": "user", "content": "Refactor this module to use dependency injection"}
    ],
)

print(response.content[0].text)

Pricing
Fast mode is priced at a per-model multiplier on standard rates across the full context window, including requests over 200k input tokens. The following table shows fast mode pricing for each supported model:  
| Model  | Input  | Output  |  
| --- | --- | --- |  
| Claude Opus 4.8  | $10 / MTok  | $50 / MTok  |  
| Claude Opus 4.7 / Claude Opus 4.6  | $30 / MTok  | $150 / MTok  |  
Fast mode pricing stacks with other pricing modifiers:
  * [Prompt caching multipliers](https://platform.claude.com/docs/en/about-claude/pricing#prompt-caching) apply on top of fast mode pricing
  * [Data residency](https://platform.claude.com/docs/en/manage-claude/data-residency) multipliers apply on top of fast mode pricing

For complete pricing details, see the [pricing page](https://platform.claude.com/docs/en/about-claude/pricing#fast-mode-pricing).
Rate limits
Fast mode has a dedicated rate limit that is separate from standard Opus rate limits. When your fast mode rate limit is exceeded, the API returns a `429` error with a `retry-after` header indicating when capacity will be available.
The response includes headers that indicate your fast mode rate limit status:  
| Header  | Description  |  
| --- | --- |  
| `anthropic-fast-input-tokens-limit`  | Maximum fast mode input tokens per minute  |  
| `anthropic-fast-input-tokens-remaining`  | Remaining fast mode input tokens  |  
| `anthropic-fast-input-tokens-reset`  | Time when the fast mode input token limit resets  |  
| `anthropic-fast-output-tokens-limit`  | Maximum fast mode output tokens per minute  |  
| `anthropic-fast-output-tokens-remaining`  | Remaining fast mode output tokens  |  
| `anthropic-fast-output-tokens-reset`  | Time when the fast mode output token limit resets  |  
For tier-specific rate limits, see the [rate limits page](https://platform.claude.com/docs/en/api/rate-limits).
Checking which speed was used
The response `usage` object includes a `speed` field that indicates which speed was used, either `"fast"` or `"standard"`. Fast mode doesn't silently fall back to standard speed on rate limits or capacity (you'll get a `429` or `529` instead), so when you request `speed: "fast"` on a supported model, `usage.speed` is `"fast"`.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.usage.speed)  # "fast" or "standard"

Output

  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
// ...
  "usage": {
    "input_tokens": 8,
    "output_tokens": 12,
    "speed": "fast"

To track fast mode usage and costs across your organization, see the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api).
Retries and fallback
### 
Automatic retries
When fast mode rate limits are exceeded, the API returns a `429` error with a `retry-after` header. The Anthropic SDKs automatically retry these requests up to 2 times by default (configurable with `max_retries`), waiting for the server-specified delay before each retry. Because fast mode uses continuous token replenishment, the `retry-after` delay is typically short and requests succeed once capacity is available.
### 
Falling back to standard speed
If you'd prefer to fall back to standard speed rather than wait for fast mode capacity, catch the rate limit error and retry without `speed: "fast"`. Set `max_retries` to `0` on the initial fast request to skip automatic retries and fail immediately on rate limit errors.
Falling back from fast to standard speed will result in a [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) miss. Requests at different speeds do not share cached prefixes.
Because setting `max_retries` to `0` also disables retries for other transient errors (overloaded, internal server errors), the following examples reissue the original request with default retries for those cases.
CLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

def create_message_with_fast_fallback(max_retries=0, max_attempts=3, **params):
    try:
        return client.with_options(max_retries=max_retries).beta.messages.create(
            **params
        )
    except anthropic.RateLimitError:
        if params.get("speed") == "fast":
            del params["speed"]
            return create_message_with_fast_fallback(max_retries=max_retries, **params)
        raise
    except (
        anthropic.APIStatusError,
        anthropic.APIConnectionError,
    ) as error:
        if isinstance(error, anthropic.APIStatusError) and error.status_code < 500:
            raise
        if max_attempts > 1:
            return create_message_with_fast_fallback(
                max_retries=max_retries, max_attempts=max_attempts - 1, **params
            )
        raise

message = create_message_with_fast_fallback(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    betas=["fast-mode-2026-02-01"],
    speed="fast",
    max_retries=0,
)

Considerations
  * **Prompt caching:** Switching between fast and standard speed invalidates the prompt cache. Requests at different speeds do not share cached prefixes.
  * **Supported models:** Fast mode is supported on Claude Opus 4.8, Claude Opus 4.7, and Claude Opus 4.6. Sending `speed: "fast"` with an unsupported model returns an error.
  * **TTFT:** Fast mode's benefits are focused on output tokens per second (OTPS), not time to first token (TTFT).
  * **Batch API:** Fast mode is not available with the [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing).
  * **Priority Tier:** Fast mode is not available with a [Priority Tier](https://platform.claude.com/docs/en/api/service-tiers) commitment.
  * **Claude Platform on AWS:** Fast mode is not currently available on [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws).

Next steps
[  Structured outputs Get validated JSON results from agent workflows. ](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)[ Pricing Learn about Anthropic's pricing structure for models and features. ](https://platform.claude.com/docs/en/about-claude/pricing#fast-mode-pricing)[ Effort Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency. ](https://platform.claude.com/docs/en/build-with-claude/effort)[  Streaming messages Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas. ](https://platform.claude.com/docs/en/build-with-claude/streaming)
  * [Supported models](https://platform.claude.com/docs/en/build-with-claude/fast-mode#supported-models)
  * [How fast mode works](https://platform.claude.com/docs/en/build-with-claude/fast-mode#how-fast-mode-works)
  * [Basic usage](https://platform.claude.com/docs/en/build-with-claude/fast-mode#basic-usage)
  * [Pricing](https://platform.claude.com/docs/en/build-with-claude/fast-mode#pricing)
  * [Rate limits](https://platform.claude.com/docs/en/build-with-claude/fast-mode#rate-limits)
  * [Checking which speed was used](https://platform.claude.com/docs/en/build-with-claude/fast-mode#checking-which-speed-was-used)
  * [Retries and fallback](https://platform.claude.com/docs/en/build-with-claude/fast-mode#retries-and-fallback)
  * [Automatic retries](https://platform.claude.com/docs/en/build-with-claude/fast-mode#automatic-retries)
  * [Falling back to standard speed](https://platform.claude.com/docs/en/build-with-claude/fast-mode#falling-back-to-standard-speed)
  * [Considerations](https://platform.claude.com/docs/en/build-with-claude/fast-mode#considerations)
  * [Next steps](https://platform.claude.com/docs/en/build-with-claude/fast-mode#next-steps)

Messages/Model capabilities
# Fast mode (research preview)
Get up to 2.5x higher output tokens per second from Claude Opus models.
Fast mode delivers up to 2.5x higher output tokens per second from Claude Opus 4.8, Claude Opus 4.7, and Claude Opus 4.6 at premium pricing. Set `speed: "fast"` with the `fast-mode-2026-02-01` beta header on your request to opt in.
Fast mode is in research preview. Contact your account manager to request access. If you do not have an account manager, [join the waitlist](https://claude.com/fast-mode) for fast mode.
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
Supported models
Fast mode is supported on the following models:
  * Claude Opus 4.8 (claude-opus-4-8)
  * Claude Opus 4.7 (claude-opus-4-7)
  * Claude Opus 4.6 (claude-opus-4-6)

Fast mode for Claude Opus 4.8 launches as a research preview on the Claude API, including [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview), only. It is not available on third-party platforms, including Amazon Bedrock, Google Cloud, and Microsoft Foundry.

Fast mode for Claude Opus 4.6 is deprecated as of the Claude Opus 4.8 launch and will be removed approximately 30 days later. After removal, requests to `claude-opus-4-6` with `speed: "fast"` will fall back to standard speed at standard pricing rather than return an error. Migrate to fast mode for Claude Opus 4.8 or Claude Opus 4.7 to keep the speedup.
How fast mode works
Fast mode runs the same model with a faster inference configuration. There is no change to intelligence or capabilities.
  * Up to 2.5x higher output tokens per second compared to standard speed
  * Speed benefits are focused on output tokens per second (OTPS), not time to first token (TTFT)
  * Same model weights and behavior (not a different model)
  * Compatible with [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming), where the OTPS gain is most visible

Basic usage
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[
        {"role": "user", "content": "Refactor this module to use dependency injection"}
    ],
)

print(response.content[0].text)

Pricing
Fast mode is priced at a per-model multiplier on standard rates across the full context window, including requests over 200k input tokens. The following table shows fast mode pricing for each supported model:  
| Model  | Input  | Output  |  
| --- | --- | --- |  
| Claude Opus 4.8  | $10 / MTok  | $50 / MTok  |  
| Claude Opus 4.7 / Claude Opus 4.6  | $30 / MTok  | $150 / MTok  |  
Fast mode pricing stacks with other pricing modifiers:
  * [Prompt caching multipliers](https://platform.claude.com/docs/en/about-claude/pricing#prompt-caching) apply on top of fast mode pricing
  * [Data residency](https://platform.claude.com/docs/en/manage-claude/data-residency) multipliers apply on top of fast mode pricing

For complete pricing details, see the [pricing page](https://platform.claude.com/docs/en/about-claude/pricing#fast-mode-pricing).
Rate limits
Fast mode has a dedicated rate limit that is separate from standard Opus rate limits. When your fast mode rate limit is exceeded, the API returns a `429` error with a `retry-after` header indicating when capacity will be available.
The response includes headers that indicate your fast mode rate limit status:  
| Header  | Description  |  
| --- | --- |  
| `anthropic-fast-input-tokens-limit`  | Maximum fast mode input tokens per minute  |  
| `anthropic-fast-input-tokens-remaining`  | Remaining fast mode input tokens  |  
| `anthropic-fast-input-tokens-reset`  | Time when the fast mode input token limit resets  |  
| `anthropic-fast-output-tokens-limit`  | Maximum fast mode output tokens per minute  |  
| `anthropic-fast-output-tokens-remaining`  | Remaining fast mode output tokens  |  
| `anthropic-fast-output-tokens-reset`  | Time when the fast mode output token limit resets  |  
For tier-specific rate limits, see the [rate limits page](https://platform.claude.com/docs/en/api/rate-limits).
Checking which speed was used
The response `usage` object includes a `speed` field that indicates which speed was used, either `"fast"` or `"standard"`. Fast mode doesn't silently fall back to standard speed on rate limits or capacity (you'll get a `429` or `529` instead), so when you request `speed: "fast"` on a supported model, `usage.speed` is `"fast"`.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.usage.speed)  # "fast" or "standard"

Output

  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
// ...
  "usage": {
    "input_tokens": 8,
    "output_tokens": 12,
    "speed": "fast"

To track fast mode usage and costs across your organization, see the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api).
Retries and fallback
### 
Automatic retries
When fast mode rate limits are exceeded, the API returns a `429` error with a `retry-after` header. The Anthropic SDKs automatically retry these requests up to 2 times by default (configurable with `max_retries`), waiting for the server-specified delay before each retry. Because fast mode uses continuous token replenishment, the `retry-after` delay is typically short and requests succeed once capacity is available.
### 
Falling back to standard speed
If you'd prefer to fall back to standard speed rather than wait for fast mode capacity, catch the rate limit error and retry without `speed: "fast"`. Set `max_retries` to `0` on the initial fast request to skip automatic retries and fail immediately on rate limit errors.
Falling back from fast to standard speed will result in a [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) miss. Requests at different speeds do not share cached prefixes.
Because setting `max_retries` to `0` also disables retries for other transient errors (overloaded, internal server errors), the following examples reissue the original request with default retries for those cases.
CLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

def create_message_with_fast_fallback(max_retries=0, max_attempts=3, **params):
    try:
        return client.with_options(max_retries=max_retries).beta.messages.create(
            **params
        )
    except anthropic.RateLimitError:
        if params.get("speed") == "fast":
            del params["speed"]
            return create_message_with_fast_fallback(max_retries=max_retries, **params)
        raise
    except (
        anthropic.APIStatusError,
        anthropic.APIConnectionError,
    ) as error:
        if isinstance(error, anthropic.APIStatusError) and error.status_code < 500:
            raise
        if max_attempts > 1:
            return create_message_with_fast_fallback(
                max_retries=max_retries, max_attempts=max_attempts - 1, **params
            )
        raise

message = create_message_with_fast_fallback(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    betas=["fast-mode-2026-02-01"],
    speed="fast",
    max_retries=0,
)

Considerations
  * **Prompt caching:** Switching between fast and standard speed invalidates the prompt cache. Requests at different speeds do not share cached prefixes.
  * **Supported models:** Fast mode is supported on Claude Opus 4.8, Claude Opus 4.7, and Claude Opus 4.6. Sending `speed: "fast"` with an unsupported model returns an error.
  * **TTFT:** Fast mode's benefits are focused on output tokens per second (OTPS), not time to first token (TTFT).
  * **Batch API:** Fast mode is not available with the [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing).
  * **Priority Tier:** Fast mode is not available with a [Priority Tier](https://platform.claude.com/docs/en/api/service-tiers) commitment.
  * **Claude Platform on AWS:** Fast mode is not currently available on [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws).

Next steps
[  Structured outputs Get validated JSON results from agent workflows. ](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)[ Pricing Learn about Anthropic's pricing structure for models and features. ](https://platform.claude.com/docs/en/about-claude/pricing#fast-mode-pricing)[ Effort Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency. ](https://platform.claude.com/docs/en/build-with-claude/effort)[  Streaming messages Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas. ](https://platform.claude.com/docs/en/build-with-claude/streaming)
