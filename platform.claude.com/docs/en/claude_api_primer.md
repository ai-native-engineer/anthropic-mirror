<!-- source: https://platform.claude.com/docs/en/claude_api_primer -->

# API usage primer for Claude
This guide is designed to give Claude the basics of using the Claude API. It gives explanation and examples of model IDs/the basic messages API, tool use, streaming, extended thinking, and nothing else.
# 
API usage primer for Claude
> This guide is designed to give Claude the basics of using the Claude API. It gives explanation and examples of model IDs/the basic messages API, tool use, streaming, extended thinking, and nothing else.
Models

Smartest model: Claude Opus 4.8: claude-opus-4-8
Smart model: Claude Sonnet 4.6: claude-sonnet-4-6
For fast, cost-effective tasks: Claude Haiku 4.5: claude-haiku-4-5-20251001

Calling the API
### 
Basic request and response
CLIPython

import anthropic
import os

message = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
).messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message)

Output

  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "content": [
      "type": "text",
      "text": "Hello!"
  ],
  "model": "claude-opus-4-8",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 12,
    "output_tokens": 6

### 
Multiple conversational turns
The Messages API is stateless, which means that you always send the full conversational history to the API. You can use this pattern to build up a conversation over time. Earlier conversational turns don't necessarily need to actually originate from Claude. You can use synthetic `assistant` messages.
CLIPython

import anthropic

message = anthropic.Anthropic().messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"},
        {"role": "assistant", "content": "Hello!"},
        {"role": "user", "content": "Can you describe LLMs to me?"},
    ],
)
print(message)

### 
Putting words in Claude's mouth
You can pre-fill part of Claude's response in the last position of the input messages list. This can be used to shape Claude's response. The example below uses `"max_tokens": 1` to get a single multiple choice answer from Claude.
CLIPython

message = anthropic.Anthropic().messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1,
    messages=[
            "role": "user",
            "content": "What is latin for Ant? (A) Apoidea, (B) Rhopalocera, (C) Formicidae",
        {"role": "assistant", "content": "The answer is ("},
    ],
)
print(message.content[0].text)

### 
Vision
Claude can read both text and images in requests. Both `base64` and `url` source types are supported for images, along with the `image/jpeg`, `image/png`, `image/gif`, and `image/webp` media types.
CLIPython

import anthropic
import base64
import httpx

# Option 1: Base64-encoded image
image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image_media_type = "image/jpeg"
image_data = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

message = anthropic.Anthropic().messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": [
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data,
                {"type": "text", "text": "What is in the above image?"},
            ],
    ],
)
print(message.content[0].text)

# Option 2: URL-referenced image
message_from_url = anthropic.Anthropic().messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": [
                    "type": "image",
                    "source": {
                        "type": "url",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                {"type": "text", "text": "What is in the above image?"},
            ],
    ],
)
print(message_from_url.content[0].text)

Extended thinking
Extended thinking can sometimes help Claude with very hard tasks. On models before Claude Opus 4.7, temperature must be set to 1 when extended thinking is enabled.
Extended thinking is supported in the following models:
  * Claude Opus 4.8 (claude-opus-4-8, adaptive thinking only)
  * Claude Opus 4.7 (`claude-opus-4-7`)
  * Claude Opus 4.6 (`claude-opus-4-6`)
  * Claude Opus 4.5 (`claude-opus-4-5-20251101`)
  * Claude Sonnet 4.6 (`claude-sonnet-4-6`)
  * Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
  * Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)

On Claude Opus 4.8 and Claude Opus 4.7, manual extended thinking (`type: enabled` with a `budget_tokens` value) is not supported and returns a 400 error. Use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (`type: adaptive`) instead.
### 
How extended thinking works
When extended thinking is turned on, Claude creates `thinking` content blocks where it outputs its internal reasoning. The API response will include `thinking` content blocks, followed by `text` content blocks.
CLIPython

import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive", "display": "summarized"},
    messages=[
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
    ],
)

# The response will contain summarized thinking blocks and text blocks
for block in response.content:
    if block.type == "thinking":
        print(f"\nThinking summary: {block.thinking}")
    elif block.type == "text":
        print(f"\nResponse: {block.text}")

When using manual extended thinking (`type: enabled`), the `budget_tokens` parameter determines the maximum number of tokens Claude is allowed to use for its internal reasoning process. In Claude 4 and later models, this limit applies to full thinking tokens, and not to the summarized output. Larger budgets can improve response quality by enabling more thorough analysis for complex problems. Unless you are using [interleaved thinking](https://platform.claude.com/docs/en/claude_api_primer#interleaved-thinking), `budget_tokens` must be less than `max_tokens` so that Claude has space to write its response after thinking is complete.
Extended thinking with tool use
Extended thinking can be used alongside tool use, allowing Claude to reason through tool selection and results processing.
Important limitations:
  1. **Tool choice limitation:** Only supports `tool_choice: {"type": "auto"}` (default) or `tool_choice: {"type": "none"}`.
  2. **Preserving thinking blocks:** During tool use, you must pass `thinking` blocks back to the API for the last assistant message.

### 
Preserving thinking blocks
CLIPython

import anthropic

client = anthropic.Anthropic()

weather_tool = {
    "name": "get_weather",
    "description": "Get the current weather for a location.",
    "input_schema": {
        "type": "object",
        "properties": {"location": {"type": "string", "description": "The city name."}},
        "required": ["location"],

weather_data = {"temperature": 72}

# First request - Claude responds with thinking and tool request
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive", "display": "summarized"},
    tools=[weather_tool],
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
)

# Extract thinking block and tool use block
thinking_block = next(
    (block for block in response.content if block.type == "thinking"), None
)
tool_use_block = next(
    (block for block in response.content if block.type == "tool_use"), None
)

# Second request - Include thinking block and tool result
continuation = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive", "display": "summarized"},
    tools=[weather_tool],
    messages=[
        {"role": "user", "content": "What's the weather in Paris?"},
        # Notice that the thinking_block is passed in as well as the tool_use_block
        {"role": "assistant", "content": [thinking_block, tool_use_block]},
            "role": "user",
            "content": [
                    "type": "tool_result",
                    "tool_use_id": tool_use_block.id,
                    "content": f"Current temperature: {weather_data['temperature']}°F",
            ],
    ],
)

for block in continuation.content:
    if block.type == "text":
        print(block.text)

### 
Interleaved thinking
Extended thinking with tool use in Claude 4 models supports interleaved thinking, which enables Claude to think between tool calls. To enable on Claude 4, 4.5, and Sonnet 4.6 models, add the beta header `interleaved-thinking-2025-05-14` to your API request.
CLIPython

import anthropic

client = anthropic.Anthropic()

calculator_tool = {
    "name": "calculator",
    "description": "Perform arithmetic calculations.",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "The math expression to evaluate.",
        "required": ["expression"],

database_tool = {
    "name": "database_query",
    "description": "Query the product database.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "The database query."}
        "required": ["query"],

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    tools=[calculator_tool, database_tool],
    messages=[
            "role": "user",
            "content": "What's the total revenue if we sold 150 units of product A at $50 each?",
    ],
    betas=["interleaved-thinking-2025-05-14"],
)

for block in response.content:
    if block.type == "thinking":
        print(f"Thinking: {block.thinking}")
    elif block.type == "tool_use":
        print(f"Tool call: {block.name}({block.input})")
    elif block.type == "text":
        print(f"Response: {block.text}")

With interleaved thinking and ONLY with interleaved thinking (not regular extended thinking), the `budget_tokens` can exceed the `max_tokens` parameter, as `budget_tokens` in this case represents the total budget across all thinking blocks within one assistant turn.
For Claude Opus 4.8, Claude Opus 4.7, and Claude Opus 4.6, interleaved thinking is automatically enabled when using [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (`thinking: {type: "adaptive"}`). No beta header is needed. Sonnet 4.6 supports both the `interleaved-thinking-2025-05-14` beta header with manual extended thinking and adaptive thinking.
Tool use
### 
Specifying client tools
Client tools are specified in the `tools` top-level parameter of the API request. Each tool definition includes:  
| Parameter  | Description  |  
| --- | --- |  
| `name`  | The name of the tool. Must match the regex `^[a-zA-Z0-9_-]{1,64}$`.  |  
| `description`  | A detailed plaintext description of what the tool does, when it should be used, and how it behaves.  |  
| `input_schema`  | A [JSON Schema](https://json-schema.org/) object defining the expected parameters for the tool.  |  

  "name": "get_weather",
  "description": "Get the current weather in a given location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The city and state, e.g. San Francisco, CA"
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
    "required": ["location"]

### 
Best practices for tool definitions
**Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain every detail about the tool, including:
  * What the tool does
  * When it should be used (and when it shouldn't)
  * What each parameter means and how it affects the tool's behavior
  * Any important caveats or limitations

**Consider using`input_examples` for complex tools.** For tools with nested objects, optional parameters, or format-sensitive inputs, you can provide concrete examples using the `input_examples` field (beta). This helps Claude understand expected input patterns. See [Providing tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#providing-tool-use-examples) for details.
Example of a good tool description:

  "name": "get_stock_price",
  "description": "Retrieves the current stock price for a given ticker symbol. The ticker symbol must be a valid symbol for a publicly traded company on a major US stock exchange like NYSE or NASDAQ. The tool will return the latest trade price in USD. It should be used when the user asks about the current or most recent price of a specific stock. It will not provide any other information about the stock or company.",
  "input_schema": {
    "type": "object",
    "properties": {
      "ticker": {
        "type": "string",
        "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
    "required": ["ticker"]

Controlling Claude's output
### 
Forcing tool use
You can force Claude to use a specific tool by specifying the tool in the `tool_choice` field:

tool_choice = {"type": "tool", "name": "get_weather"}

When working with the tool_choice parameter, there are four possible options:
  * `auto` allows Claude to decide whether to call any provided tools or not (default).
  * `any` tells Claude that it must use one of the provided tools.
  * `tool` forces Claude to always use a particular tool.
  * `none` prevents Claude from using any tools.

### 
JSON output
Tools do not necessarily need to be client functions. You can use tools anytime you want the model to return JSON output that follows a provided schema.
### 
Chain of thought
When using tools, Claude will often show its "chain of thought," that is, the step-by-step reasoning it uses to break down the problem and decide which tools to use.

  "role": "assistant",
  "content": [
      "type": "text",
      "text": "<thinking>To answer this question, I will: 1. Use the get_weather tool to get the current weather in San Francisco. 2. Use the get_time tool to get the current time in the America/Los_Angeles timezone, which covers San Francisco, CA.</thinking>"
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": { "location": "San Francisco, CA" }
  ]

### 
Parallel tool use
By default, Claude may use multiple tools to answer a user query. You can disable this behavior by setting `disable_parallel_tool_use=true`.
Handling tool use and tool result content blocks
### 
Handling results from client tools
The response will have a `stop_reason` of `tool_use` and one or more `tool_use` content blocks that include:
  * `id`: A unique identifier for this particular tool use block.
  * `name`: The name of the tool being used.
  * `input`: An object containing the input being passed to the tool.

When you receive a tool use response, you should:
  1. Extract the `name`, `id`, and `input` from the `tool_use` block.
  2. Run the actual tool in your codebase corresponding to that tool name.
  3. Continue the conversation by sending a new message with a `tool_result`:

  "role": "user",
  "content": [
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "15 degrees"
  ]

### 
Handling the `max_tokens` stop reason
If Claude's response is cut off due to hitting the `max_tokens` limit during tool use, retry the request with a higher `max_tokens` value.
### 
Handling the `pause_turn` stop reason
When using server tools like web search, the API may return a `pause_turn` stop reason. Continue the conversation by passing the paused response back as-is in a subsequent request.
Troubleshooting errors
### 
Tool execution error
If the tool itself throws an error during execution, return the error message with `"is_error": true`:

  "role": "user",
  "content": [
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "ConnectionError: the weather service API is not available (HTTP 500)",
      "is_error": true
  ]

### 
Invalid tool name
If Claude's attempted use of a tool is invalid (e.g. missing required parameters), try the request again with more-detailed `description` values in your tool definitions.
Streaming messages
When creating a Message, you can set `"stream": true` to incrementally stream the response using server-sent events (SSE).
### 
Streaming with SDKs
CLIPython

import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    model="claude-opus-4-8",
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

### 
Event types
Each server-sent event includes a named event type and associated JSON data. Each stream uses the following event flow:
  1. `message_start`: contains a `Message` object with empty `content`.
  2. A series of content blocks, each with `content_block_start`, one or more `content_block_delta` events, and `content_block_stop`.
  3. One or more `message_delta` events, indicating top-level changes to the final `Message` object.
  4. A final `message_stop` event.

**Warning:** The token counts shown in the `usage` field of the `message_delta` event are _cumulative_.
### 
Content block delta types
#### 
Text delta

  "type": "content_block_delta",
  "index": 0,
  "delta": { "type": "text_delta", "text": "Hello frien" }

#### 
Input JSON delta
For `tool_use` content blocks, deltas are _partial JSON strings_ :

{"type": "content_block_delta","index": 1,"delta": {"type": "input_json_delta","partial_json": "{\"location\": \"San Fra"}}}

#### 
Thinking delta
When using extended thinking with streaming:

  "type": "content_block_delta",
  "index": 0,
  "delta": {
    "type": "thinking_delta",
    "thinking": "Let me solve this step by step..."

### 
Basic streaming request example

event: message_start
data: {"type": "message_start", "message": {"id": "msg_1nZdL29xx5MUA1yADyHTEsnR8uuvGzszyY", "type": "message", "role": "assistant", "content": [], "model": "claude-opus-4-8", "stop_reason": null, "stop_sequence": null, "usage": {"input_tokens": 25, "output_tokens": 1}}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "Hello"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "!"}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 0}

event: message_delta
data: {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence":null}, "usage": {"output_tokens": 15}}

event: message_stop
data: {"type": "message_stop"}

  * [Models](https://platform.claude.com/docs/en/claude_api_primer#models)
  * [Calling the API](https://platform.claude.com/docs/en/claude_api_primer#calling-the-api)
  * [Basic request and response](https://platform.claude.com/docs/en/claude_api_primer#basic-request-and-response)
  * [Multiple conversational turns](https://platform.claude.com/docs/en/claude_api_primer#multiple-conversational-turns)
  * [Putting words in Claude's mouth](https://platform.claude.com/docs/en/claude_api_primer#putting-words-in-claudes-mouth)
  * [Vision](https://platform.claude.com/docs/en/claude_api_primer#vision)
  * [Extended thinking](https://platform.claude.com/docs/en/claude_api_primer#extended-thinking)
  * [How extended thinking works](https://platform.claude.com/docs/en/claude_api_primer#how-extended-thinking-works)
  * [Extended thinking with tool use](https://platform.claude.com/docs/en/claude_api_primer#extended-thinking-with-tool-use)
  * [Preserving thinking blocks](https://platform.claude.com/docs/en/claude_api_primer#preserving-thinking-blocks)
  * [Interleaved thinking](https://platform.claude.com/docs/en/claude_api_primer#interleaved-thinking)
  * [Tool use](https://platform.claude.com/docs/en/claude_api_primer#tool-use)
  * [Specifying client tools](https://platform.claude.com/docs/en/claude_api_primer#specifying-client-tools)
  * [Best practices for tool definitions](https://platform.claude.com/docs/en/claude_api_primer#best-practices-for-tool-definitions)
  * [Controlling Claude's output](https://platform.claude.com/docs/en/claude_api_primer#controlling-claudes-output)
  * [Forcing tool use](https://platform.claude.com/docs/en/claude_api_primer#forcing-tool-use)
  * [JSON output](https://platform.claude.com/docs/en/claude_api_primer#json-output)
  * [Chain of thought](https://platform.claude.com/docs/en/claude_api_primer#chain-of-thought)
  * [Parallel tool use](https://platform.claude.com/docs/en/claude_api_primer#parallel-tool-use)
  * [Handling tool use and tool result content blocks](https://platform.claude.com/docs/en/claude_api_primer#handling-tool-use-and-tool-result-content-blocks)
  * [Handling results from client tools](https://platform.claude.com/docs/en/claude_api_primer#handling-results-from-client-tools)
  * [Handling the max_tokens stop reason](https://platform.claude.com/docs/en/claude_api_primer#handling-the-max-tokens-stop-reason)
  * [Handling the pause_turn stop reason](https://platform.claude.com/docs/en/claude_api_primer#handling-the-pause-turn-stop-reason)
  * [Troubleshooting errors](https://platform.claude.com/docs/en/claude_api_primer#troubleshooting-errors)
  * [Tool execution error](https://platform.claude.com/docs/en/claude_api_primer#tool-execution-error)
  * [Invalid tool name](https://platform.claude.com/docs/en/claude_api_primer#invalid-tool-name)
  * [Streaming messages](https://platform.claude.com/docs/en/claude_api_primer#streaming-messages)
  * [Streaming with SDKs](https://platform.claude.com/docs/en/claude_api_primer#streaming-with-sdks)
  * [Event types](https://platform.claude.com/docs/en/claude_api_primer#event-types)
  * [Content block delta types](https://platform.claude.com/docs/en/claude_api_primer#content-block-delta-types)
  * [Basic streaming request example](https://platform.claude.com/docs/en/claude_api_primer#basic-streaming-request-example)

Documentation
# API usage primer for Claude
This guide is designed to give Claude the basics of using the Claude API. It gives explanation and examples of model IDs/the basic messages API, tool use, streaming, extended thinking, and nothing else.
# 
API usage primer for Claude
> This guide is designed to give Claude the basics of using the Claude API. It gives explanation and examples of model IDs/the basic messages API, tool use, streaming, extended thinking, and nothing else.
Models

Smartest model: Claude Opus 4.8: claude-opus-4-8
Smart model: Claude Sonnet 4.6: claude-sonnet-4-6
For fast, cost-effective tasks: Claude Haiku 4.5: claude-haiku-4-5-20251001

Calling the API
### 
Basic request and response
CLIPython

import anthropic
import os

message = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
).messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message)

Output

  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "content": [
      "type": "text",
      "text": "Hello!"
  ],
  "model": "claude-opus-4-8",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 12,
    "output_tokens": 6

### 
Multiple conversational turns
The Messages API is stateless, which means that you always send the full conversational history to the API. You can use this pattern to build up a conversation over time. Earlier conversational turns don't necessarily need to actually originate from Claude. You can use synthetic `assistant` messages.
CLIPython

import anthropic

message = anthropic.Anthropic().messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"},
        {"role": "assistant", "content": "Hello!"},
        {"role": "user", "content": "Can you describe LLMs to me?"},
    ],
)
print(message)

### 
Putting words in Claude's mouth
You can pre-fill part of Claude's response in the last position of the input messages list. This can be used to shape Claude's response. The example below uses `"max_tokens": 1` to get a single multiple choice answer from Claude.
CLIPython

message = anthropic.Anthropic().messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1,
    messages=[
            "role": "user",
            "content": "What is latin for Ant? (A) Apoidea, (B) Rhopalocera, (C) Formicidae",
        {"role": "assistant", "content": "The answer is ("},
    ],
)
print(message.content[0].text)

### 
Vision
Claude can read both text and images in requests. Both `base64` and `url` source types are supported for images, along with the `image/jpeg`, `image/png`, `image/gif`, and `image/webp` media types.
CLIPython

import anthropic
import base64
import httpx

# Option 1: Base64-encoded image
image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image_media_type = "image/jpeg"
image_data = base64.standard_b64encode(httpx.get(image_url).content).decode("utf-8")

message = anthropic.Anthropic().messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": [
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data,
                {"type": "text", "text": "What is in the above image?"},
            ],
    ],
)
print(message.content[0].text)

# Option 2: URL-referenced image
message_from_url = anthropic.Anthropic().messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": [
                    "type": "image",
                    "source": {
                        "type": "url",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                {"type": "text", "text": "What is in the above image?"},
            ],
    ],
)
print(message_from_url.content[0].text)

Extended thinking
Extended thinking can sometimes help Claude with very hard tasks. On models before Claude Opus 4.7, temperature must be set to 1 when extended thinking is enabled.
Extended thinking is supported in the following models:
  * Claude Opus 4.8 (claude-opus-4-8, adaptive thinking only)
  * Claude Opus 4.7 (`claude-opus-4-7`)
  * Claude Opus 4.6 (`claude-opus-4-6`)
  * Claude Opus 4.5 (`claude-opus-4-5-20251101`)
  * Claude Sonnet 4.6 (`claude-sonnet-4-6`)
  * Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
  * Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)

On Claude Opus 4.8 and Claude Opus 4.7, manual extended thinking (`type: enabled` with a `budget_tokens` value) is not supported and returns a 400 error. Use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (`type: adaptive`) instead.
### 
How extended thinking works
When extended thinking is turned on, Claude creates `thinking` content blocks where it outputs its internal reasoning. The API response will include `thinking` content blocks, followed by `text` content blocks.
CLIPython

import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive", "display": "summarized"},
    messages=[
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
    ],
)

# The response will contain summarized thinking blocks and text blocks
for block in response.content:
    if block.type == "thinking":
        print(f"\nThinking summary: {block.thinking}")
    elif block.type == "text":
        print(f"\nResponse: {block.text}")

When using manual extended thinking (`type: enabled`), the `budget_tokens` parameter determines the maximum number of tokens Claude is allowed to use for its internal reasoning process. In Claude 4 and later models, this limit applies to full thinking tokens, and not to the summarized output. Larger budgets can improve response quality by enabling more thorough analysis for complex problems. Unless you are using [interleaved thinking](https://platform.claude.com/docs/en/claude_api_primer#interleaved-thinking), `budget_tokens` must be less than `max_tokens` so that Claude has space to write its response after thinking is complete.
Extended thinking with tool use
Extended thinking can be used alongside tool use, allowing Claude to reason through tool selection and results processing.
Important limitations:
  1. **Tool choice limitation:** Only supports `tool_choice: {"type": "auto"}` (default) or `tool_choice: {"type": "none"}`.
  2. **Preserving thinking blocks:** During tool use, you must pass `thinking` blocks back to the API for the last assistant message.

### 
Preserving thinking blocks
CLIPython

import anthropic

client = anthropic.Anthropic()

weather_tool = {
    "name": "get_weather",
    "description": "Get the current weather for a location.",
    "input_schema": {
        "type": "object",
        "properties": {"location": {"type": "string", "description": "The city name."}},
        "required": ["location"],

weather_data = {"temperature": 72}

# First request - Claude responds with thinking and tool request
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive", "display": "summarized"},
    tools=[weather_tool],
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
)

# Extract thinking block and tool use block
thinking_block = next(
    (block for block in response.content if block.type == "thinking"), None
)
tool_use_block = next(
    (block for block in response.content if block.type == "tool_use"), None
)

# Second request - Include thinking block and tool result
continuation = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    thinking={"type": "adaptive", "display": "summarized"},
    tools=[weather_tool],
    messages=[
        {"role": "user", "content": "What's the weather in Paris?"},
        # Notice that the thinking_block is passed in as well as the tool_use_block
        {"role": "assistant", "content": [thinking_block, tool_use_block]},
            "role": "user",
            "content": [
                    "type": "tool_result",
                    "tool_use_id": tool_use_block.id,
                    "content": f"Current temperature: {weather_data['temperature']}°F",
            ],
    ],
)

for block in continuation.content:
    if block.type == "text":
        print(block.text)

### 
Interleaved thinking
Extended thinking with tool use in Claude 4 models supports interleaved thinking, which enables Claude to think between tool calls. To enable on Claude 4, 4.5, and Sonnet 4.6 models, add the beta header `interleaved-thinking-2025-05-14` to your API request.
CLIPython

import anthropic

client = anthropic.Anthropic()

calculator_tool = {
    "name": "calculator",
    "description": "Perform arithmetic calculations.",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "The math expression to evaluate.",
        "required": ["expression"],

database_tool = {
    "name": "database_query",
    "description": "Query the product database.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "The database query."}
        "required": ["query"],

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    tools=[calculator_tool, database_tool],
    messages=[
            "role": "user",
            "content": "What's the total revenue if we sold 150 units of product A at $50 each?",
    ],
    betas=["interleaved-thinking-2025-05-14"],
)

for block in response.content:
    if block.type == "thinking":
        print(f"Thinking: {block.thinking}")
    elif block.type == "tool_use":
        print(f"Tool call: {block.name}({block.input})")
    elif block.type == "text":
        print(f"Response: {block.text}")

With interleaved thinking and ONLY with interleaved thinking (not regular extended thinking), the `budget_tokens` can exceed the `max_tokens` parameter, as `budget_tokens` in this case represents the total budget across all thinking blocks within one assistant turn.
For Claude Opus 4.8, Claude Opus 4.7, and Claude Opus 4.6, interleaved thinking is automatically enabled when using [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (`thinking: {type: "adaptive"}`). No beta header is needed. Sonnet 4.6 supports both the `interleaved-thinking-2025-05-14` beta header with manual extended thinking and adaptive thinking.
Tool use
### 
Specifying client tools
Client tools are specified in the `tools` top-level parameter of the API request. Each tool definition includes:  
| Parameter  | Description  |  
| --- | --- |  
| `name`  | The name of the tool. Must match the regex `^[a-zA-Z0-9_-]{1,64}$`.  |  
| `description`  | A detailed plaintext description of what the tool does, when it should be used, and how it behaves.  |  
| `input_schema`  | A [JSON Schema](https://json-schema.org/) object defining the expected parameters for the tool.  |  

  "name": "get_weather",
  "description": "Get the current weather in a given location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The city and state, e.g. San Francisco, CA"
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
    "required": ["location"]

### 
Best practices for tool definitions
**Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain every detail about the tool, including:
  * What the tool does
  * When it should be used (and when it shouldn't)
  * What each parameter means and how it affects the tool's behavior
  * Any important caveats or limitations

**Consider using`input_examples` for complex tools.** For tools with nested objects, optional parameters, or format-sensitive inputs, you can provide concrete examples using the `input_examples` field (beta). This helps Claude understand expected input patterns. See [Providing tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#providing-tool-use-examples) for details.
Example of a good tool description:

  "name": "get_stock_price",
  "description": "Retrieves the current stock price for a given ticker symbol. The ticker symbol must be a valid symbol for a publicly traded company on a major US stock exchange like NYSE or NASDAQ. The tool will return the latest trade price in USD. It should be used when the user asks about the current or most recent price of a specific stock. It will not provide any other information about the stock or company.",
  "input_schema": {
    "type": "object",
    "properties": {
      "ticker": {
        "type": "string",
        "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
    "required": ["ticker"]

Controlling Claude's output
### 
Forcing tool use
You can force Claude to use a specific tool by specifying the tool in the `tool_choice` field:

tool_choice = {"type": "tool", "name": "get_weather"}

When working with the tool_choice parameter, there are four possible options:
  * `auto` allows Claude to decide whether to call any provided tools or not (default).
  * `any` tells Claude that it must use one of the provided tools.
  * `tool` forces Claude to always use a particular tool.
  * `none` prevents Claude from using any tools.

### 
JSON output
Tools do not necessarily need to be client functions. You can use tools anytime you want the model to return JSON output that follows a provided schema.
### 
Chain of thought
When using tools, Claude will often show its "chain of thought," that is, the step-by-step reasoning it uses to break down the problem and decide which tools to use.

  "role": "assistant",
  "content": [
      "type": "text",
      "text": "<thinking>To answer this question, I will: 1. Use the get_weather tool to get the current weather in San Francisco. 2. Use the get_time tool to get the current time in the America/Los_Angeles timezone, which covers San Francisco, CA.</thinking>"
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": { "location": "San Francisco, CA" }
  ]

### 
Parallel tool use
By default, Claude may use multiple tools to answer a user query. You can disable this behavior by setting `disable_parallel_tool_use=true`.
Handling tool use and tool result content blocks
### 
Handling results from client tools
The response will have a `stop_reason` of `tool_use` and one or more `tool_use` content blocks that include:
  * `id`: A unique identifier for this particular tool use block.
  * `name`: The name of the tool being used.
  * `input`: An object containing the input being passed to the tool.

When you receive a tool use response, you should:
  1. Extract the `name`, `id`, and `input` from the `tool_use` block.
  2. Run the actual tool in your codebase corresponding to that tool name.
  3. Continue the conversation by sending a new message with a `tool_result`:

  "role": "user",
  "content": [
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "15 degrees"
  ]

### 
Handling the `max_tokens` stop reason
If Claude's response is cut off due to hitting the `max_tokens` limit during tool use, retry the request with a higher `max_tokens` value.
### 
Handling the `pause_turn` stop reason
When using server tools like web search, the API may return a `pause_turn` stop reason. Continue the conversation by passing the paused response back as-is in a subsequent request.
Troubleshooting errors
### 
Tool execution error
If the tool itself throws an error during execution, return the error message with `"is_error": true`:

  "role": "user",
  "content": [
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "ConnectionError: the weather service API is not available (HTTP 500)",
      "is_error": true
  ]

### 
Invalid tool name
If Claude's attempted use of a tool is invalid (e.g. missing required parameters), try the request again with more-detailed `description` values in your tool definitions.
Streaming messages
When creating a Message, you can set `"stream": true` to incrementally stream the response using server-sent events (SSE).
### 
Streaming with SDKs
CLIPython

import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    model="claude-opus-4-8",
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

### 
Event types
Each server-sent event includes a named event type and associated JSON data. Each stream uses the following event flow:
  1. `message_start`: contains a `Message` object with empty `content`.
  2. A series of content blocks, each with `content_block_start`, one or more `content_block_delta` events, and `content_block_stop`.
  3. One or more `message_delta` events, indicating top-level changes to the final `Message` object.
  4. A final `message_stop` event.

**Warning:** The token counts shown in the `usage` field of the `message_delta` event are _cumulative_.
### 
Content block delta types
#### 
Text delta

  "type": "content_block_delta",
  "index": 0,
  "delta": { "type": "text_delta", "text": "Hello frien" }

#### 
Input JSON delta
For `tool_use` content blocks, deltas are _partial JSON strings_ :

{"type": "content_block_delta","index": 1,"delta": {"type": "input_json_delta","partial_json": "{\"location\": \"San Fra"}}}

#### 
Thinking delta
When using extended thinking with streaming:

  "type": "content_block_delta",
  "index": 0,
  "delta": {
    "type": "thinking_delta",
    "thinking": "Let me solve this step by step..."

### 
Basic streaming request example

event: message_start
data: {"type": "message_start", "message": {"id": "msg_1nZdL29xx5MUA1yADyHTEsnR8uuvGzszyY", "type": "message", "role": "assistant", "content": [], "model": "claude-opus-4-8", "stop_reason": null, "stop_sequence": null, "usage": {"input_tokens": 25, "output_tokens": 1}}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "Hello"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": "!"}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 0}

event: message_delta
data: {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence":null}, "usage": {"output_tokens": 15}}

event: message_stop
data: {"type": "message_stop"}
