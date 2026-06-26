<!-- source: https://platform.claude.com/docs/en/build-with-claude/token-counting -->

# Token counting
Count the tokens in a message before you send it to Claude. Use token counts to manage rate limits and costs, make model routing decisions, and fit prompts to a target length.
Token counting lets you determine the number of tokens in a message before you send it to Claude. This helps you make informed decisions about your prompts and usage. With token counting, you can:
  * Proactively manage rate limits and costs
  * Make smart model routing decisions
  * Optimize prompts to a specific length

This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
* * *
How to count message tokens
The [token counting](https://platform.claude.com/docs/en/api/messages-count-tokens) endpoint accepts the same structured list of inputs for creating a message, including support for system prompts, [tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), [images](https://platform.claude.com/docs/en/build-with-claude/vision), and [PDFs](https://platform.claude.com/docs/en/build-with-claude/pdf-support). The response contains the total number of input tokens.
The token count should be considered an **estimate**. In some cases, the actual number of input tokens used when creating a message may differ by a small amount.
Token counts may include tokens added automatically by Anthropic for system optimizations. **You are not billed for system-added tokens**. Billing reflects only your content.
### 
Supported models
All [active models](https://platform.claude.com/docs/en/about-claude/models/overview) support token counting.
### 
Count tokens in basic messages
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-4-8",
    system="You are a scientist",
    messages=[{"role": "user", "content": "Hello, Claude"}],
)

print(response.json())

Output

{ "input_tokens": 14 }

### 
Count tokens in messages with tools
[Server tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools) token counts only apply to the first sampling call.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-4-8",
    tools=[
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                "required": ["location"],
    ],
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
)

print(response.json())

Output

{ "input_tokens": 403 }

### 
Count tokens in messages with images
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import base64
import httpx

image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image_media_type = "image/jpeg"
image_data = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-4-8",
    messages=[
            "role": "user",
            "content": [
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data,
                {"type": "text", "text": "Describe this image"},
            ],
    ],
)
print(response.json())

Output

{ "input_tokens": 1551 }

### 
Count tokens in messages with extended thinking
See [how the context window is calculated with extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#how-context-window-is-calculated-with-extended-thinking) for more details
  * Thinking blocks from **previous** assistant turns are ignored and **do not** count toward your input tokens
  * **Current** assistant turn thinking **does** count toward your input tokens

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-sonnet-4-6",
    thinking={"type": "enabled", "budget_tokens": 16000},
    messages=[
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
            "role": "assistant",
            "content": [
                    "type": "thinking",
                    "thinking": "This is a nice number theory question. Let's think about it step by step...",
                    "signature": "EuYBCkQYAiJAgCs1le6/Pol5Z4/JMomVOouGrWdhYNsH3ukzUECbB6iWrSQtsQuRHJID6lWV...",
                    "type": "text",
                    "text": "Yes, there are infinitely many prime numbers p such that p mod 4 = 3...",
            ],
        {"role": "user", "content": "Can you write a formal proof?"},
    ],
)

print(response.json())

Output

{ "input_tokens": 88 }

### 
Count tokens in messages with PDFs
Token counting supports PDFs with the same [limitations](https://platform.claude.com/docs/en/build-with-claude/pdf-support#pdf-support-limitations) as the Messages API.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import base64
import anthropic

client = anthropic.Anthropic()

with open("document.pdf", "rb") as pdf_file:
    pdf_base64 = base64.standard_b64encode(pdf_file.read()).decode("utf-8")

response = client.messages.count_tokens(
    model="claude-opus-4-8",
    messages=[
            "role": "user",
            "content": [
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_base64,
                {"type": "text", "text": "Please summarize this document."},
            ],
    ],
)

print(response.json())

Output

{ "input_tokens": 2188 }

* * *
Token counts on Claude Fable 5 and Claude Mythos 5
Claude Fable 5 and Claude Mythos 5 use the tokenizer introduced with Claude Opus 4.7, which produces roughly 30% more tokens than models before Claude Opus 4.7 for the same text. The token counting endpoint returns the count under the tokenizer of the `model` you pass, so to measure the difference for your workload, count the same request twice: once with your current model and once with `model: "claude-fable-5"` (or `"claude-mythos-5"`), and compare the two `input_tokens` values.
**Billing and migration:** Usage and billing on Claude Fable 5 and Claude Mythos 5 reflect this tokenizer's counts. If you're migrating from a model before Claude Opus 4.7, the same content consumes roughly 30% more tokens. When migrating a workload to Claude Fable 5 and Claude Mythos 5, don't reuse token counts measured on a model before Claude Opus 4.7 to estimate costs or context window fit. Count your prompts with `model: "claude-fable-5"` (or `"claude-mythos-5"`).
* * *
Pricing and rate limits
Token counting is **free to use** but subject to requests per minute rate limits based on your [usage tier](https://platform.claude.com/docs/en/api/rate-limits#rate-limits). If you need higher limits, contact sales through the [Claude Console](https://platform.claude.com/settings/limits).  
| Usage tier  | Requests per minute (RPM)  |  
| --- | --- |  
| 1  | 100  |  
| 2  | 2,000  |  
| 3  | 4,000  |  
| 4  | 8,000  |  
Token counting and message creation have separate and independent rate limits. Usage of one does not count against the limits of the other.
* * *
FAQ
### Does token counting use prompt caching?
* * *
Next steps
[  Count message tokens Read the full API reference for the token counting endpoint. ](https://platform.claude.com/docs/en/api/messages-count-tokens)[ Context windows Use token counts to keep prompts within a model's context window. ](https://platform.claude.com/docs/en/build-with-claude/context-windows)[ Rate limits Check token counts before you send a request to stay within your usage tier. ](https://platform.claude.com/docs/en/api/rate-limits)[ Prompt caching Reduce cost and latency on repeated prompts by caching prompt prefixes. ](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
  * [How to count message tokens](https://platform.claude.com/docs/en/build-with-claude/token-counting#how-to-count-message-tokens)
  * [Supported models](https://platform.claude.com/docs/en/build-with-claude/token-counting#supported-models)
  * [Count tokens in basic messages](https://platform.claude.com/docs/en/build-with-claude/token-counting#count-tokens-in-basic-messages)
  * [Count tokens in messages with tools](https://platform.claude.com/docs/en/build-with-claude/token-counting#count-tokens-in-messages-with-tools)
  * [Count tokens in messages with images](https://platform.claude.com/docs/en/build-with-claude/token-counting#count-tokens-in-messages-with-images)
  * [Count tokens in messages with extended thinking](https://platform.claude.com/docs/en/build-with-claude/token-counting#count-tokens-in-messages-with-extended-thinking)
  * [Count tokens in messages with PDFs](https://platform.claude.com/docs/en/build-with-claude/token-counting#count-tokens-in-messages-with-pdfs)
  * [Token counts on Claude Fable 5 and Claude Mythos 5](https://platform.claude.com/docs/en/build-with-claude/token-counting#token-counts-on-claude-fable-5)
  * [Pricing and rate limits](https://platform.claude.com/docs/en/build-with-claude/token-counting#pricing-and-rate-limits)
  * [FAQ](https://platform.claude.com/docs/en/build-with-claude/token-counting#faq)
  * [Next steps](https://platform.claude.com/docs/en/build-with-claude/token-counting#next-steps)

Messages/Context management
# Token counting
Count the tokens in a message before you send it to Claude. Use token counts to manage rate limits and costs, make model routing decisions, and fit prompts to a target length.
Token counting lets you determine the number of tokens in a message before you send it to Claude. This helps you make informed decisions about your prompts and usage. With token counting, you can:
  * Proactively manage rate limits and costs
  * Make smart model routing decisions
  * Optimize prompts to a specific length

This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
* * *
How to count message tokens
The [token counting](https://platform.claude.com/docs/en/api/messages-count-tokens) endpoint accepts the same structured list of inputs for creating a message, including support for system prompts, [tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), [images](https://platform.claude.com/docs/en/build-with-claude/vision), and [PDFs](https://platform.claude.com/docs/en/build-with-claude/pdf-support). The response contains the total number of input tokens.
The token count should be considered an **estimate**. In some cases, the actual number of input tokens used when creating a message may differ by a small amount.
Token counts may include tokens added automatically by Anthropic for system optimizations. **You are not billed for system-added tokens**. Billing reflects only your content.
### 
Supported models
All [active models](https://platform.claude.com/docs/en/about-claude/models/overview) support token counting.
### 
Count tokens in basic messages
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-4-8",
    system="You are a scientist",
    messages=[{"role": "user", "content": "Hello, Claude"}],
)

print(response.json())

Output

{ "input_tokens": 14 }

### 
Count tokens in messages with tools
[Server tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools) token counts only apply to the first sampling call.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-4-8",
    tools=[
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                "required": ["location"],
    ],
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
)

print(response.json())

Output

{ "input_tokens": 403 }

### 
Count tokens in messages with images
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import base64
import httpx

image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image_media_type = "image/jpeg"
image_data = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-opus-4-8",
    messages=[
            "role": "user",
            "content": [
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data,
                {"type": "text", "text": "Describe this image"},
            ],
    ],
)
print(response.json())

Output

{ "input_tokens": 1551 }

### 
Count tokens in messages with extended thinking
See [how the context window is calculated with extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#how-context-window-is-calculated-with-extended-thinking) for more details
  * Thinking blocks from **previous** assistant turns are ignored and **do not** count toward your input tokens
  * **Current** assistant turn thinking **does** count toward your input tokens

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-sonnet-4-6",
    thinking={"type": "enabled", "budget_tokens": 16000},
    messages=[
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
            "role": "assistant",
            "content": [
                    "type": "thinking",
                    "thinking": "This is a nice number theory question. Let's think about it step by step...",
                    "signature": "EuYBCkQYAiJAgCs1le6/Pol5Z4/JMomVOouGrWdhYNsH3ukzUECbB6iWrSQtsQuRHJID6lWV...",
                    "type": "text",
                    "text": "Yes, there are infinitely many prime numbers p such that p mod 4 = 3...",
            ],
        {"role": "user", "content": "Can you write a formal proof?"},
    ],
)

print(response.json())

Output

{ "input_tokens": 88 }

### 
Count tokens in messages with PDFs
Token counting supports PDFs with the same [limitations](https://platform.claude.com/docs/en/build-with-claude/pdf-support#pdf-support-limitations) as the Messages API.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import base64
import anthropic

client = anthropic.Anthropic()

with open("document.pdf", "rb") as pdf_file:
    pdf_base64 = base64.standard_b64encode(pdf_file.read()).decode("utf-8")

response = client.messages.count_tokens(
    model="claude-opus-4-8",
    messages=[
            "role": "user",
            "content": [
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_base64,
                {"type": "text", "text": "Please summarize this document."},
            ],
    ],
)

print(response.json())

Output

{ "input_tokens": 2188 }

* * *
Token counts on Claude Fable 5 and Claude Mythos 5
Claude Fable 5 and Claude Mythos 5 use the tokenizer introduced with Claude Opus 4.7, which produces roughly 30% more tokens than models before Claude Opus 4.7 for the same text. The token counting endpoint returns the count under the tokenizer of the `model` you pass, so to measure the difference for your workload, count the same request twice: once with your current model and once with `model: "claude-fable-5"` (or `"claude-mythos-5"`), and compare the two `input_tokens` values.
**Billing and migration:** Usage and billing on Claude Fable 5 and Claude Mythos 5 reflect this tokenizer's counts. If you're migrating from a model before Claude Opus 4.7, the same content consumes roughly 30% more tokens. When migrating a workload to Claude Fable 5 and Claude Mythos 5, don't reuse token counts measured on a model before Claude Opus 4.7 to estimate costs or context window fit. Count your prompts with `model: "claude-fable-5"` (or `"claude-mythos-5"`).
* * *
Pricing and rate limits
Token counting is **free to use** but subject to requests per minute rate limits based on your [usage tier](https://platform.claude.com/docs/en/api/rate-limits#rate-limits). If you need higher limits, contact sales through the [Claude Console](https://platform.claude.com/settings/limits).  
| Usage tier  | Requests per minute (RPM)  |  
| --- | --- |  
| 1  | 100  |  
| 2  | 2,000  |  
| 3  | 4,000  |  
| 4  | 8,000  |  
Token counting and message creation have separate and independent rate limits. Usage of one does not count against the limits of the other.
* * *
FAQ
### Does token counting use prompt caching?
* * *
Next steps
[  Count message tokens Read the full API reference for the token counting endpoint. ](https://platform.claude.com/docs/en/api/messages-count-tokens)[ Context windows Use token counts to keep prompts within a model's context window. ](https://platform.claude.com/docs/en/build-with-claude/context-windows)[ Rate limits Check token counts before you send a request to stay within your usage tier. ](https://platform.claude.com/docs/en/api/rate-limits)[ Prompt caching Reduce cost and latency on repeated prompts by caching prompt prefixes. ](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
