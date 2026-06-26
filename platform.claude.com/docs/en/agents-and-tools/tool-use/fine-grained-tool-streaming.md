<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming -->

# Fine-grained tool streaming
Stream tool inputs without server-side JSON buffering for latency-sensitive applications.
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
Fine-grained tool streaming is available on all models and all platforms. It enables [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) of tool use parameter values without buffering or JSON validation, reducing the latency to begin receiving large parameters.

When using fine-grained tool streaming, you may potentially receive invalid or partial JSON inputs. Make sure to account for these edge cases in your code.
How to use fine-grained tool streaming
Fine-grained tool streaming is supported on the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai), and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry). To use it, set `eager_input_streaming` to `true` on any user-defined tool where you want fine-grained streaming enabled, and enable streaming on your request.
Here's an example of how to use fine-grained tool streaming with the API:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

with client.messages.stream(
    max_tokens=65536,
    model="claude-opus-4-8",
    tools=[
            "name": "make_file",
            "description": "Write text to a file",
            "eager_input_streaming": True,
            "input_schema": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "The filename to write text to",
                    "lines_of_text": {
                        "type": "array",
                        "description": "An array of lines of text to write to the file",
                "required": ["filename", "lines_of_text"],
    ],
    messages=[
            "role": "user",
            "content": "Can you write a long poem and make a file called poem.txt?",
    ],
) as stream:
    final_message = stream.get_final_message()

print(f"Input tokens: {final_message.usage.input_tokens}")
print(f"Output tokens: {final_message.usage.output_tokens}")

In this example, fine-grained tool streaming enables Claude to stream the lines of a long poem into the tool call `make_file` without buffering to validate if the `lines_of_text` parameter is valid JSON. This means you can see the parameter stream as it arrives, without having to wait for the entire parameter to buffer and validate.
With fine-grained tool streaming, tool input chunks start arriving sooner because the server skips JSON-validation buffering. Chunks are typically longer and contain fewer mid-token breaks as a side effect.

Because fine-grained streaming sends parameters without buffering or JSON validation, there is no guarantee that the resulting stream will complete in a valid JSON string. Particularly, if the [stop reason](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons) `max_tokens` is reached, the stream may end midway through a parameter and may be incomplete. You generally have to write specific support to handle when `max_tokens` is reached.
Accumulating tool input deltas
When a `tool_use` content block streams, the initial `content_block_start` event contains `input: {}` (an empty object). This is a placeholder. The actual input arrives as a series of `input_json_delta` events, each carrying a `partial_json` string fragment. To assemble the full input, concatenate these fragments and parse the result when the block closes.
Where your SDK provides an accumulator helper (as used in the first example on this page), it handles this for you. The manual pattern is for SDKs without a helper, or when you need to react to partial input before the block closes.
The accumulation contract:
  1. On `content_block_start` with `type: "tool_use"`, initialize an empty string: `input_json = ""`
  2. For each `content_block_delta` with `type: "input_json_delta"`, append: `input_json += event.delta.partial_json`
  3. On `content_block_stop`, parse the accumulated string: `json.loads(input_json)`

The type mismatch between the initial `input: {}` (object) and `partial_json` (string) is by design. The empty object marks the slot in the content array; the delta strings build the real value.
PythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

tool_inputs: dict[int, str] = {}  # index -> accumulated JSON string

with client.messages.stream(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[
            "name": "get_weather",
            "description": "Get current weather for a city",
            "eager_input_streaming": True,
            "input_schema": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
    ],
    messages=[{"role": "user", "content": "Weather in Paris?"}],
) as stream:
    for event in stream:
        match event.type:
            case "content_block_start" if event.content_block.type == "tool_use":
                tool_inputs[event.index] = ""
            case "content_block_delta" if event.delta.type == "input_json_delta":
                tool_inputs[event.index] += event.delta.partial_json
            case "content_block_stop" if event.index in tool_inputs:
                parsed = json.loads(tool_inputs[event.index])
                print(f"Tool input: {parsed}")


Reach for the manual pattern when you need to react to partial input before the block closes (for example, rendering a progress indicator). Otherwise, prefer your SDK's accumulator helper where the first example on this page uses one.
Handling invalid JSON in tool responses
When using fine-grained tool streaming, you may receive invalid or incomplete JSON from the model. If you need to pass this invalid JSON back to the model in an error response block, you may wrap it in a JSON object to ensure proper handling (with a reasonable key). For example:

  "INVALID_JSON": "<your invalid json string>"

This approach helps the model understand that the content is invalid JSON while preserving the original malformed data for debugging purposes.
When wrapping invalid JSON, make sure to properly escape any quotes or special characters in the invalid JSON string to maintain valid JSON structure in the wrapper object.
Next steps
[ Streaming messages Full reference for server-sent events and stream event types. ](https://platform.claude.com/docs/en/build-with-claude/streaming)[ Handle tool calls Execute tools and return results in the required message format. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)[ Tool reference Full directory of Anthropic-schema tools and their version strings. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
  * [How to use fine-grained tool streaming](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming#how-to-use-fine-grained-tool-streaming)
  * [Accumulating tool input deltas](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming#accumulating-tool-input-deltas)
  * [Handling invalid JSON in tool responses](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming#handling-invalid-json-in-tool-responses)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming#next-steps)

Messages/Tool infrastructure
# Fine-grained tool streaming
Stream tool inputs without server-side JSON buffering for latency-sensitive applications.
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
Fine-grained tool streaming is available on all models and all platforms. It enables [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) of tool use parameter values without buffering or JSON validation, reducing the latency to begin receiving large parameters.

When using fine-grained tool streaming, you may potentially receive invalid or partial JSON inputs. Make sure to account for these edge cases in your code.
How to use fine-grained tool streaming
Fine-grained tool streaming is supported on the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai), and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry). To use it, set `eager_input_streaming` to `true` on any user-defined tool where you want fine-grained streaming enabled, and enable streaming on your request.
Here's an example of how to use fine-grained tool streaming with the API:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

with client.messages.stream(
    max_tokens=65536,
    model="claude-opus-4-8",
    tools=[
            "name": "make_file",
            "description": "Write text to a file",
            "eager_input_streaming": True,
            "input_schema": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "The filename to write text to",
                    "lines_of_text": {
                        "type": "array",
                        "description": "An array of lines of text to write to the file",
                "required": ["filename", "lines_of_text"],
    ],
    messages=[
            "role": "user",
            "content": "Can you write a long poem and make a file called poem.txt?",
    ],
) as stream:
    final_message = stream.get_final_message()

print(f"Input tokens: {final_message.usage.input_tokens}")
print(f"Output tokens: {final_message.usage.output_tokens}")

In this example, fine-grained tool streaming enables Claude to stream the lines of a long poem into the tool call `make_file` without buffering to validate if the `lines_of_text` parameter is valid JSON. This means you can see the parameter stream as it arrives, without having to wait for the entire parameter to buffer and validate.
With fine-grained tool streaming, tool input chunks start arriving sooner because the server skips JSON-validation buffering. Chunks are typically longer and contain fewer mid-token breaks as a side effect.

Because fine-grained streaming sends parameters without buffering or JSON validation, there is no guarantee that the resulting stream will complete in a valid JSON string. Particularly, if the [stop reason](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons) `max_tokens` is reached, the stream may end midway through a parameter and may be incomplete. You generally have to write specific support to handle when `max_tokens` is reached.
Accumulating tool input deltas
When a `tool_use` content block streams, the initial `content_block_start` event contains `input: {}` (an empty object). This is a placeholder. The actual input arrives as a series of `input_json_delta` events, each carrying a `partial_json` string fragment. To assemble the full input, concatenate these fragments and parse the result when the block closes.
Where your SDK provides an accumulator helper (as used in the first example on this page), it handles this for you. The manual pattern is for SDKs without a helper, or when you need to react to partial input before the block closes.
The accumulation contract:
  1. On `content_block_start` with `type: "tool_use"`, initialize an empty string: `input_json = ""`
  2. For each `content_block_delta` with `type: "input_json_delta"`, append: `input_json += event.delta.partial_json`
  3. On `content_block_stop`, parse the accumulated string: `json.loads(input_json)`

The type mismatch between the initial `input: {}` (object) and `partial_json` (string) is by design. The empty object marks the slot in the content array; the delta strings build the real value.
PythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

tool_inputs: dict[int, str] = {}  # index -> accumulated JSON string

with client.messages.stream(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[
            "name": "get_weather",
            "description": "Get current weather for a city",
            "eager_input_streaming": True,
            "input_schema": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
    ],
    messages=[{"role": "user", "content": "Weather in Paris?"}],
) as stream:
    for event in stream:
        match event.type:
            case "content_block_start" if event.content_block.type == "tool_use":
                tool_inputs[event.index] = ""
            case "content_block_delta" if event.delta.type == "input_json_delta":
                tool_inputs[event.index] += event.delta.partial_json
            case "content_block_stop" if event.index in tool_inputs:
                parsed = json.loads(tool_inputs[event.index])
                print(f"Tool input: {parsed}")


Reach for the manual pattern when you need to react to partial input before the block closes (for example, rendering a progress indicator). Otherwise, prefer your SDK's accumulator helper where the first example on this page uses one.
Handling invalid JSON in tool responses
When using fine-grained tool streaming, you may receive invalid or incomplete JSON from the model. If you need to pass this invalid JSON back to the model in an error response block, you may wrap it in a JSON object to ensure proper handling (with a reasonable key). For example:

  "INVALID_JSON": "<your invalid json string>"

This approach helps the model understand that the content is invalid JSON while preserving the original malformed data for debugging purposes.
When wrapping invalid JSON, make sure to properly escape any quotes or special characters in the invalid JSON string to maintain valid JSON structure in the wrapper object.
Next steps
[ Streaming messages Full reference for server-sent events and stream event types. ](https://platform.claude.com/docs/en/build-with-claude/streaming)[ Handle tool calls Execute tools and return results in the required message format. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)[ Tool reference Full directory of Anthropic-schema tools and their version strings. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
