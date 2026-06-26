<!-- source: https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk -->

# OpenAI SDK compatibility
Anthropic provides a compatibility layer that enables you to use the OpenAI SDK to test the Claude API. With a few code changes, you can quickly evaluate Anthropic model capabilities.
This compatibility layer is primarily intended to test and compare model capabilities, and is not considered a long-term or production-ready solution for most use cases. While it is intended to remain fully functional and not have breaking changes, the priority is the reliability and effectiveness of the [Claude API](https://platform.claude.com/docs/en/api/overview).
For more information on known compatibility limitations, see [Important OpenAI compatibility limitations](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#important-openai-compatibility-limitations).
If you encounter any issues with the OpenAI SDK compatibility feature, please share your feedback via this [compatibility feedback form](https://forms.gle/oQV4McQNiuuNbz9n8).

For the best experience and access to Claude API full feature set ([PDF processing](https://platform.claude.com/docs/en/build-with-claude/pdf-support), [citations](https://platform.claude.com/docs/en/build-with-claude/citations), [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking), and [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)), use the native [Claude API](https://platform.claude.com/docs/en/api/overview).
Getting started with the OpenAI SDK
To use the OpenAI SDK compatibility feature, you'll need to:
  1. Use an official OpenAI SDK
  2. Change the following
     * Update your base URL to point to the Claude API
     * Replace your API key with a [Claude API key](https://platform.claude.com/settings/keys)
     * Update your model name to use a [Claude model](https://platform.claude.com/docs/en/about-claude/models/overview)
  3. Review the documentation below for what features are supported

### 
Quick start example
PythonTypeScript

import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Your Claude API key
    base_url="https://api.anthropic.com/v1/",  # the Claude API endpoint
)

response = client.chat.completions.create(
    model="claude-opus-4-8",  # Claude model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who are you?"},
    ],
)

print(response.choices[0].message.content)

Important OpenAI compatibility limitations
### 
API behavior
Here are the most substantial differences from using OpenAI:
  * The `strict` parameter for function calling is ignored, which means the tool use JSON is not guaranteed to follow the supplied schema. For guaranteed schema conformance, use the native [Claude API with Structured Outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs).
  * Audio input is not supported; it will simply be ignored and stripped from input
  * Prompt caching is not supported, but it is supported in the [Anthropic SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)
  * System/developer messages are hoisted and concatenated to the beginning of the conversation, as Anthropic only supports a single initial system message.

Most unsupported fields are silently ignored rather than producing errors. These are all documented below.
### 
Output quality considerations
If you’ve done lots of tweaking to your prompt, it’s likely to be well-tuned to OpenAI specifically. Consider using the [prompt improver in the Claude Console](https://platform.claude.com/dashboard) as a good starting point.
### 
System / developer message hoisting
Most of the inputs to the OpenAI SDK clearly map directly to Anthropic’s API parameters, but one distinct difference is the handling of system / developer prompts. These two prompts can be put throughout a chat conversation via OpenAI. Since Anthropic only supports an initial system message, the API takes all system/developer messages and concatenates them together with a single newline (`\n`) in between them. This full string is then supplied as a single system message at the start of the messages.
### 
Extended thinking support
You can enable [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) capabilities by adding the `thinking` parameter. While this improves Claude's reasoning for complex tasks, the OpenAI SDK doesn't return Claude's detailed thought process. For full extended thinking features, including access to Claude's step-by-step reasoning output, use the native Claude API.
PythonTypeScript

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Who are you?"}],
    extra_body={"thinking": {"type": "enabled", "budget_tokens": 2000}},
)

Rate limits
Rate limits follow Anthropic's [standard limits](https://platform.claude.com/docs/en/api/rate-limits) for the `/v1/messages` endpoint.
Detailed OpenAI compatible API support
### 
Request fields
#### 
Simple fields  
| Field  | Support status  |  
| --- | --- |  
| `model`  | Use Claude model names  |  
| `max_tokens`  | Fully supported  |  
| `max_completion_tokens`  | Fully supported  |  
| `stream`  | Fully supported  |  
| `stream_options`  | Fully supported  |  
| `top_p`  | Fully supported  |  
| `parallel_tool_calls`  | Fully supported  |  
| `stop`  | All non-whitespace stop sequences work  |  
| `temperature`  | Between 0 and 1 (inclusive). Values greater than 1 are capped at 1.  |  
| `n`  | Must be exactly 1  |  
| `logprobs`  | Ignored  |  
| `metadata`  | Ignored  |  
| `response_format`  | Ignored. For JSON output, use [Structured Outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) with the native Claude API  |  
| `prediction`  | Ignored  |  
| `presence_penalty`  | Ignored  |  
| `frequency_penalty`  | Ignored  |  
| `seed`  | Ignored  |  
| `service_tier`  | Ignored  |  
| `audio`  | Ignored  |  
| `logit_bias`  | Ignored  |  
| `store`  | Ignored  |  
| `user`  | Ignored  |  
| `modalities`  | Ignored  |  
| `top_logprobs`  | Ignored  |  
| `reasoning_effort`  | Ignored  |  
#### 
`tools` / `functions` fields
### Show fields
#### 
`messages` array fields
### Show fields
### 
Response fields  
| Field  | Support status  |  
| --- | --- |  
| `id`  | Fully supported  |  
| `choices[]`  | Will always have a length of 1  |  
| `choices[].finish_reason`  | Fully supported  |  
| `choices[].index`  | Fully supported  |  
| `choices[].message.role`  | Fully supported  |  
| `choices[].message.content`  | Fully supported  |  
| `choices[].message.tool_calls`  | Fully supported  |  
| `object`  | Fully supported  |  
| `created`  | Fully supported  |  
| `model`  | Fully supported  |  
| `finish_reason`  | Fully supported  |  
| `content`  | Fully supported  |  
| `usage.completion_tokens`  | Fully supported  |  
| `usage.prompt_tokens`  | Fully supported  |  
| `usage.total_tokens`  | Fully supported  |  
| `usage.completion_tokens_details`  | Always empty  |  
| `usage.prompt_tokens_details`  | Always empty  |  
| `choices[].message.refusal`  | Always empty  |  
| `choices[].message.audio`  | Always empty  |  
| `logprobs`  | Always empty  |  
| `service_tier`  | Always empty  |  
| `system_fingerprint`  | Always empty  |  
### 
Error message compatibility
The compatibility layer maintains consistent error formats with the OpenAI API. However, the detailed error messages will not be equivalent. Only use the error messages for logging and debugging.
### 
Header compatibility
While the OpenAI SDK automatically manages headers, here is the complete list of headers supported by the Claude API for developers who need to work with them directly.  
| Header  | Support Status  |  
| --- | --- |  
| `x-ratelimit-limit-requests`  | Fully supported  |  
| `x-ratelimit-limit-tokens`  | Fully supported  |  
| `x-ratelimit-remaining-requests`  | Fully supported  |  
| `x-ratelimit-remaining-tokens`  | Fully supported  |  
| `x-ratelimit-reset-requests`  | Fully supported  |  
| `x-ratelimit-reset-tokens`  | Fully supported  |  
| `retry-after`  | Fully supported  |  
| `request-id`  | Fully supported  |  
| `openai-version`  | Always `2020-10-01`  |  
| `authorization`  | Fully supported  |  
| `openai-processing-ms`  | Always empty  |  
  * [Getting started with the OpenAI SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#getting-started-with-the-open-ai-sdk)
  * [Quick start example](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#quick-start-example)
  * [Important OpenAI compatibility limitations](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#important-open-ai-compatibility-limitations)
  * [API behavior](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#api-behavior)
  * [Output quality considerations](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#output-quality-considerations)
  * [System / developer message hoisting](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#system-developer-message-hoisting)
  * [Extended thinking support](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#extended-thinking-support)
  * [Rate limits](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#rate-limits)
  * [Detailed OpenAI compatible API support](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#detailed-open-ai-compatible-api-support)
  * [Request fields](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#request-fields)
  * [Response fields](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#response-fields)
  * [Error message compatibility](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#error-message-compatibility)
  * [Header compatibility](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#header-compatibility)

CLI, SDKs, and libraries/Libraries and integrations
# OpenAI SDK compatibility
Anthropic provides a compatibility layer that enables you to use the OpenAI SDK to test the Claude API. With a few code changes, you can quickly evaluate Anthropic model capabilities.
This compatibility layer is primarily intended to test and compare model capabilities, and is not considered a long-term or production-ready solution for most use cases. While it is intended to remain fully functional and not have breaking changes, the priority is the reliability and effectiveness of the [Claude API](https://platform.claude.com/docs/en/api/overview).
For more information on known compatibility limitations, see [Important OpenAI compatibility limitations](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk#important-openai-compatibility-limitations).
If you encounter any issues with the OpenAI SDK compatibility feature, please share your feedback via this [compatibility feedback form](https://forms.gle/oQV4McQNiuuNbz9n8).

For the best experience and access to Claude API full feature set ([PDF processing](https://platform.claude.com/docs/en/build-with-claude/pdf-support), [citations](https://platform.claude.com/docs/en/build-with-claude/citations), [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking), and [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)), use the native [Claude API](https://platform.claude.com/docs/en/api/overview).
Getting started with the OpenAI SDK
To use the OpenAI SDK compatibility feature, you'll need to:
  1. Use an official OpenAI SDK
  2. Change the following
     * Update your base URL to point to the Claude API
     * Replace your API key with a [Claude API key](https://platform.claude.com/settings/keys)
     * Update your model name to use a [Claude model](https://platform.claude.com/docs/en/about-claude/models/overview)
  3. Review the documentation below for what features are supported

### 
Quick start example
PythonTypeScript

import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Your Claude API key
    base_url="https://api.anthropic.com/v1/",  # the Claude API endpoint
)

response = client.chat.completions.create(
    model="claude-opus-4-8",  # Claude model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who are you?"},
    ],
)

print(response.choices[0].message.content)

Important OpenAI compatibility limitations
### 
API behavior
Here are the most substantial differences from using OpenAI:
  * The `strict` parameter for function calling is ignored, which means the tool use JSON is not guaranteed to follow the supplied schema. For guaranteed schema conformance, use the native [Claude API with Structured Outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs).
  * Audio input is not supported; it will simply be ignored and stripped from input
  * Prompt caching is not supported, but it is supported in the [Anthropic SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)
  * System/developer messages are hoisted and concatenated to the beginning of the conversation, as Anthropic only supports a single initial system message.

Most unsupported fields are silently ignored rather than producing errors. These are all documented below.
### 
Output quality considerations
If you’ve done lots of tweaking to your prompt, it’s likely to be well-tuned to OpenAI specifically. Consider using the [prompt improver in the Claude Console](https://platform.claude.com/dashboard) as a good starting point.
### 
System / developer message hoisting
Most of the inputs to the OpenAI SDK clearly map directly to Anthropic’s API parameters, but one distinct difference is the handling of system / developer prompts. These two prompts can be put throughout a chat conversation via OpenAI. Since Anthropic only supports an initial system message, the API takes all system/developer messages and concatenates them together with a single newline (`\n`) in between them. This full string is then supplied as a single system message at the start of the messages.
### 
Extended thinking support
You can enable [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) capabilities by adding the `thinking` parameter. While this improves Claude's reasoning for complex tasks, the OpenAI SDK doesn't return Claude's detailed thought process. For full extended thinking features, including access to Claude's step-by-step reasoning output, use the native Claude API.
PythonTypeScript

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Who are you?"}],
    extra_body={"thinking": {"type": "enabled", "budget_tokens": 2000}},
)

Rate limits
Rate limits follow Anthropic's [standard limits](https://platform.claude.com/docs/en/api/rate-limits) for the `/v1/messages` endpoint.
Detailed OpenAI compatible API support
### 
Request fields
#### 
Simple fields  
| Field  | Support status  |  
| --- | --- |  
| `model`  | Use Claude model names  |  
| `max_tokens`  | Fully supported  |  
| `max_completion_tokens`  | Fully supported  |  
| `stream`  | Fully supported  |  
| `stream_options`  | Fully supported  |  
| `top_p`  | Fully supported  |  
| `parallel_tool_calls`  | Fully supported  |  
| `stop`  | All non-whitespace stop sequences work  |  
| `temperature`  | Between 0 and 1 (inclusive). Values greater than 1 are capped at 1.  |  
| `n`  | Must be exactly 1  |  
| `logprobs`  | Ignored  |  
| `metadata`  | Ignored  |  
| `response_format`  | Ignored. For JSON output, use [Structured Outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) with the native Claude API  |  
| `prediction`  | Ignored  |  
| `presence_penalty`  | Ignored  |  
| `frequency_penalty`  | Ignored  |  
| `seed`  | Ignored  |  
| `service_tier`  | Ignored  |  
| `audio`  | Ignored  |  
| `logit_bias`  | Ignored  |  
| `store`  | Ignored  |  
| `user`  | Ignored  |  
| `modalities`  | Ignored  |  
| `top_logprobs`  | Ignored  |  
| `reasoning_effort`  | Ignored  |  
#### 
`tools` / `functions` fields
### Show fields
#### 
`messages` array fields
### Show fields
### 
Response fields  
| Field  | Support status  |  
| --- | --- |  
| `id`  | Fully supported  |  
| `choices[]`  | Will always have a length of 1  |  
| `choices[].finish_reason`  | Fully supported  |  
| `choices[].index`  | Fully supported  |  
| `choices[].message.role`  | Fully supported  |  
| `choices[].message.content`  | Fully supported  |  
| `choices[].message.tool_calls`  | Fully supported  |  
| `object`  | Fully supported  |  
| `created`  | Fully supported  |  
| `model`  | Fully supported  |  
| `finish_reason`  | Fully supported  |  
| `content`  | Fully supported  |  
| `usage.completion_tokens`  | Fully supported  |  
| `usage.prompt_tokens`  | Fully supported  |  
| `usage.total_tokens`  | Fully supported  |  
| `usage.completion_tokens_details`  | Always empty  |  
| `usage.prompt_tokens_details`  | Always empty  |  
| `choices[].message.refusal`  | Always empty  |  
| `choices[].message.audio`  | Always empty  |  
| `logprobs`  | Always empty  |  
| `service_tier`  | Always empty  |  
| `system_fingerprint`  | Always empty  |  
### 
Error message compatibility
The compatibility layer maintains consistent error formats with the OpenAI API. However, the detailed error messages will not be equivalent. Only use the error messages for logging and debugging.
### 
Header compatibility
While the OpenAI SDK automatically manages headers, here is the complete list of headers supported by the Claude API for developers who need to work with them directly.  
| Header  | Support Status  |  
| --- | --- |  
| `x-ratelimit-limit-requests`  | Fully supported  |  
| `x-ratelimit-limit-tokens`  | Fully supported  |  
| `x-ratelimit-remaining-requests`  | Fully supported  |  
| `x-ratelimit-remaining-tokens`  | Fully supported  |  
| `x-ratelimit-reset-requests`  | Fully supported  |  
| `x-ratelimit-reset-tokens`  | Fully supported  |  
| `retry-after`  | Fully supported  |  
| `request-id`  | Fully supported  |  
| `openai-version`  | Always `2020-10-01`  |  
| `authorization`  | Fully supported  |  
| `openai-processing-ms`  | Always empty  |
