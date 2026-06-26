<!-- source: https://platform.claude.com/docs/en/api/cli/messages/create -->

# Create a Message
$ ant messages create
POST/v1/messages
Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.
The Messages API can be used for either single queries or stateless multi-turn conversations.
Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)
##### ParametersExpand Collapse 
--max-tokens: number
The maximum number of tokens to generate before stopping.
Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.
Set to `0` to populate the [prompt cache](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.
Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.max_tokens)
--message: array of [MessageParam](https://platform.claude.com/docs/en/api/messages#message_param) { content, role } 
Input messages.
Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.
Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.
If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.
Example with a single `user` message:

[{"role": "user", "content": "Hello, Claude"}]

Example with multiple conversational turns:

[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]

Example with a partially-filled response from Claude:

[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("},
]

Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

{"role": "user", "content": "Hello, Claude"}

{"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}

See [input examples](https://docs.claude.com/en/api/messages-examples).
Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.
There is a limit of 100,000 messages in a single request.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.messages)
--model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.model)
--cache-control: optional object { type, ttl } 
Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.cache_control)
--container: optional string
Container identifier for reuse across requests.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.container)
--inference-geo: optional string
Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.inference_geo)
--metadata: optional object { user_id } 
An object describing metadata about the request.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.metadata)
--output-config: optional object { effort, format } 
Configuration options for the model's output, such as the output format.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.output_config)
--service-tier: optional "auto" or "standard_only"
Determines whether to use priority capacity (if available) or standard capacity for this request.
Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.service_tier)
--stop-sequence: optional array of string
Custom text sequences that will cause the model to stop generating.
Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.
If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.stop_sequences)
--system: optional string or array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } 
System prompt.
A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.system)
Deprecated--temperature: optional number
Amount of randomness injected into the response.
Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.
Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.
Note that even with `temperature` of `0.0`, the results will not be fully deterministic.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.temperature)
--thinking: optional [ThinkingConfigEnabled](https://platform.claude.com/docs/en/api/messages#thinking_config_enabled) { budget_tokens, type, display }  or [ThinkingConfigDisabled](https://platform.claude.com/docs/en/api/messages#thinking_config_disabled) { type }  or [ThinkingConfigAdaptive](https://platform.claude.com/docs/en/api/messages#thinking_config_adaptive) { type, display } 
Configuration for enabling Claude's extended thinking.
When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.
See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.thinking)
--tool-choice: optional [ToolChoiceAuto](https://platform.claude.com/docs/en/api/messages#tool_choice_auto) { type, disable_parallel_tool_use }  or [ToolChoiceAny](https://platform.claude.com/docs/en/api/messages#tool_choice_any) { type, disable_parallel_tool_use }  or [ToolChoiceTool](https://platform.claude.com/docs/en/api/messages#tool_choice_tool) { name, type, disable_parallel_tool_use }  or [ToolChoiceNone](https://platform.claude.com/docs/en/api/messages#tool_choice_none) { type } 
How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.tool_choice)
--tool: optional array of [ToolUnion](https://platform.claude.com/docs/en/api/messages#tool_union)
Definitions of tools that the model may use.
If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.
There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).
Each tool definition includes:
  * `name`: Name of the tool.
  * `description`: Optional, but strongly-recommended description of the tool.
  * `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

For example, if you defined `tools` as:

[
    "name": "get_stock_price",
    "description": "Get the current stock price for a given ticker symbol.",
    "input_schema": {
      "type": "object",
      "properties": {
        "ticker": {
          "type": "string",
          "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
      "required": ["ticker"]
]

And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

[
    "type": "tool_use",
    "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "name": "get_stock_price",
    "input": { "ticker": "^GSPC" }
]

You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

[
    "type": "tool_result",
    "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "content": "259.75 USD"
]

Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.
See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.tools)
Deprecated--top-k: optional number
Only sample from the top K options for each subsequent token.
Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.
Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).
Recommended for advanced use cases only.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.top_k)
Deprecated--top-p: optional number
Use nucleus sampling.
Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.
In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.
Recommended for advanced use cases only.
[](https://platform.claude.com/docs/en/api/cli/messages/create#create.top_p)
message: object { id, container, content, 7 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.id)
container: object { id, expires_at } 
Information about the container used in the request (for the code execution tool)
Identifier for the container used in this request
[](https://platform.claude.com/docs/en/api/cli/messages/create#container.id)
expires_at: string
The time at which the container will expire.
[](https://platform.claude.com/docs/en/api/cli/messages/create#container.expires_at)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.container)
content: array of [ContentBlock](https://platform.claude.com/docs/en/api/messages#content_block)
Content generated by the model.
This is an array of content blocks, each of which has a `type` that determines its shape.
Example:

[{"type": "text", "text": "Hi, I'm Claude."}]

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.
For example, if the input `messages` were:

[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]

Then the response `content` might be:

[{"type": "text", "text": "B)"}]

text_block: object { citations, text, type } 
citations: array of [TextCitation](https://platform.claude.com/docs/en/api/messages#text_citation)
Citations supporting the text block.
The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.
citation_char_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.end_char_index)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.file_id)
start_char_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B0%5D)
citation_page_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.end_page_number)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.file_id)
start_page_number: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B1%5D)
citation_content_block_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.end_block_index)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.file_id)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B2%5D)
citations_web_search_result_location: object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.type)
url: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.url)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B3%5D)
citations_search_result_location: object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_block.citations)
text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B0%5D)
thinking_block: object { signature, thinking, type } 
signature: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_block.signature)
thinking: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_block.thinking)
type: "thinking"
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B1%5D)
redacted_thinking_block: object { data, type } 
data: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#redacted_thinking_block.data)
type: "redacted_thinking"
[](https://platform.claude.com/docs/en/api/cli/messages/create#redacted_thinking_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B2%5D)
tool_use_block: object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.input)
name: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.name)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B3%5D)
server_tool_use_block: object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.input)
name: "web_search" or "web_fetch" or "code_execution" or 4 more
"web_search"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B0%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B2%5D)
"bash_code_execution"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B3%5D)
"text_editor_code_execution"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B4%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B5%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B6%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name)
type: "server_tool_use"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B4%5D)
web_search_tool_result_block: object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.caller)
content: [WebSearchToolResultError](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_error) { error_code, type }  or array of [WebSearchResultBlock](https://platform.claude.com/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } 
web_search_tool_result_error: object { error_code, type } 
error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B1%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B2%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B3%5D)
"query_too_long"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B4%5D)
"request_too_large"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B5%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error.error_code)
type: "web_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block_content%5B0%5D)
union_member_1: array of [WebSearchResultBlock](https://platform.claude.com/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } 
encrypted_content: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.encrypted_content)
page_age: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.page_age)
title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.title)
type: "web_search_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.type)
url: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.url)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block_content%5B1%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.tool_use_id)
type: "web_search_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B5%5D)
web_fetch_tool_result_block: object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.caller)
content: [WebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type }  or [WebFetchBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url } 
web_fetch_tool_result_error_block: object { error_code, type } 
error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 6 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B0%5D)
"url_too_long"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B1%5D)
"url_not_allowed"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B2%5D)
"url_not_in_prior_context"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B3%5D)
"url_not_accessible"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B4%5D)
"unsupported_content_type"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B5%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B6%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B7%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B8%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_block.error_code)
type: "web_fetch_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_block)
web_fetch_block: object { content, retrieved_at, type, url } 
content: object { citations, source, title, type } 
citations: object { enabled } 
Citation configuration for the document
enabled: boolean
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_config.enabled)
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.citations)
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type } 
base64_pdf_source: object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source)
plain_text_source: object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source)
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.source)
title: string
The title of the document
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.title)
type: "document"
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.content)
retrieved_at: string
ISO 8601 timestamp when the content was retrieved
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.retrieved_at)
type: "web_fetch_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.type)
url: string
Fetched content URL
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.url)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.tool_use_id)
type: "web_fetch_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B6%5D)
code_execution_tool_result_block: object { content, tool_use_id, type } 
content: [CodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_error) { error_code, type }  or [CodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#code_execution_result_block) { content, return_code, stderr, 2 more }  or [EncryptedCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#encrypted_code_execution_result_block) { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
code_execution_tool_result_error: object { error_code, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B3%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error.error_code)
type: "code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block_content%5B0%5D)
code_execution_result_block: object { content, return_code, stderr, 2 more } 
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.content)
return_code: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.stdout)
type: "code_execution_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block_content%5B1%5D)
encrypted_code_execution_result_block: object { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.content)
encrypted_stdout: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.encrypted_stdout)
return_code: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.stderr)
type: "encrypted_code_execution_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block_content%5B2%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block.tool_use_id)
type: "code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B7%5D)
bash_code_execution_tool_result_block: object { content, tool_use_id, type } 
content: [BashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type }  or [BashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more } 
bash_code_execution_tool_result_error: object { error_code, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B3%5D)
"output_file_too_large"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error.error_code)
type: "bash_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error)
bash_code_execution_result_block: object { content, return_code, stderr, 2 more } 
content: array of [BashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_output_block.file_id)
type: "bash_code_execution_output"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_output_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.content)
return_code: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.stdout)
type: "bash_code_execution_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_block.tool_use_id)
type: "bash_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B8%5D)
text_editor_code_execution_tool_result_block: object { content, tool_use_id, type } 
content: [TextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type }  or [TextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more } 
text_editor_code_execution_tool_result_error: object { error_code, error_message, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B3%5D)
"file_not_found"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error.error_message)
type: "text_editor_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error)
text_editor_code_execution_view_result_block: object { content, file_type, num_lines, 3 more } 
content: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.content)
file_type: "text" or "image" or "pdf"
"text"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type%5B0%5D)
"image"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type%5B1%5D)
"pdf"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type)
num_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.num_lines)
start_line: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.start_line)
total_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.total_lines)
type: "text_editor_code_execution_view_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block)
text_editor_code_execution_create_result_block: object { is_file_update, type } 
is_file_update: boolean
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_create_result_block.is_file_update)
type: "text_editor_code_execution_create_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_create_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_create_result_block)
text_editor_code_execution_str_replace_result_block: object { lines, new_lines, new_start, 3 more } 
lines: array of string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.lines)
new_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.new_lines)
new_start: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.new_start)
old_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.old_lines)
old_start: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.old_start)
type: "text_editor_code_execution_str_replace_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_block.tool_use_id)
type: "text_editor_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B9%5D)
tool_search_tool_result_block: object { content, tool_use_id, type } 
content: [ToolSearchToolResultError](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type }  or [ToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type } 
tool_search_tool_result_error: object { error_code, error_message, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B3%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error.error_message)
type: "tool_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error)
tool_search_tool_search_result_block: object { tool_references, type } 
tool_references: array of [ToolReferenceBlock](https://platform.claude.com/docs/en/api/messages#tool_reference_block) { tool_name, type } 
tool_name: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_reference_block.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_reference_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_search_result_block.tool_references)
type: "tool_search_tool_search_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_search_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_search_result_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_block.tool_use_id)
type: "tool_search_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B10%5D)
container_upload_block: object { file_id, type } 
Response model for a file uploaded to the container.
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#container_upload_block.file_id)
type: "container_upload"
[](https://platform.claude.com/docs/en/api/cli/messages/create#container_upload_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B11%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.content)
model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.model)
role: "assistant"
Conversational role of the generated message.
This will always be `"assistant"`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.role)
stop_details: object { category, explanation, type } 
Structured information about a refusal.
category: "cyber" or "bio" or "frontier_llm" or "reasoning_extraction"
The policy category that triggered a refusal.
"cyber"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B0%5D)
"bio"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B1%5D)
"frontier_llm"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B2%5D)
"reasoning_extraction"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B3%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category)
explanation: string
Human-readable explanation of the refusal.
This text is not guaranteed to be stable. `null` when no explanation is available for the category.
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.explanation)
type: "refusal"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.stop_details)
stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 3 more
The reason that we stopped.
This may be one the following values:
  * `"end_turn"`: the model reached a natural stopping point
  * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
  * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
  * `"tool_use"`: the model invoked one or more tools
  * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
  * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.
"end_turn"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B0%5D)
"max_tokens"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B1%5D)
"stop_sequence"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B2%5D)
"tool_use"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B3%5D)
"pause_turn"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B4%5D)
"refusal"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B5%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.stop_reason)
stop_sequence: string
Which custom stop sequence was generated, if any.
This value will be a non-null string if one of your custom stop sequences was generated.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.stop_sequence)
type: "message"
Object type.
For Messages, this is always `"message"`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.type)
usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more } 
Billing and rate-limit usage.
Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.
Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.
For example, `output_tokens` will be non-zero, even for an empty string response from Claude.
Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.
cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
Breakdown of cached tokens by TTL
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/cli/messages/create#cache_creation.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/cli/messages/create#cache_creation.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.cache_creation)
cache_creation_input_tokens: number
The number of input tokens used to create the cache entry.
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.cache_creation_input_tokens)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.cache_read_input_tokens)
inference_geo: string
The geographic region where inference was performed for this request.
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.inference_geo)
input_tokens: number
The number of input tokens which were used.
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.input_tokens)
output_tokens: number
The number of output tokens which were used.
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.output_tokens)
output_tokens_details: object { thinking_tokens } 
Breakdown of output tokens by category.
`output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you.
thinking_tokens: number
Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.
Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.
[](https://platform.claude.com/docs/en/api/cli/messages/create#output_tokens_details.thinking_tokens)
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.output_tokens_details)
server_tool_use: object { web_fetch_requests, web_search_requests } 
The number of server tool requests.
web_fetch_requests: number
The number of web fetch tool requests.
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_usage.web_fetch_requests)
web_search_requests: number
The number of web search tool requests.
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_usage.web_search_requests)
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.server_tool_use)
service_tier: "standard" or "priority" or "batch"
If the request used the priority, standard, or batch tier.
"standard"
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.service_tier%5B0%5D)
"priority"
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.service_tier%5B1%5D)
"batch"
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.service_tier%5B2%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.service_tier)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.usage)
[](https://platform.claude.com/docs/en/api/cli/messages/create#create)
raw_message_stream_event: [RawMessageStartEvent](https://platform.claude.com/docs/en/api/messages#raw_message_start_event) { message, type }  or [RawMessageDeltaEvent](https://platform.claude.com/docs/en/api/messages#raw_message_delta_event) { delta, type, usage }  or [RawMessageStopEvent](https://platform.claude.com/docs/en/api/messages#raw_message_stop_event) { type }  or 3 more
raw_message_start_event: object { message, type } 
message: object { id, container, content, 7 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.id)
container: object { id, expires_at } 
Information about the container used in the request (for the code execution tool)
Identifier for the container used in this request
[](https://platform.claude.com/docs/en/api/cli/messages/create#container.id)
expires_at: string
The time at which the container will expire.
[](https://platform.claude.com/docs/en/api/cli/messages/create#container.expires_at)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.container)
content: array of [ContentBlock](https://platform.claude.com/docs/en/api/messages#content_block)
Content generated by the model.
This is an array of content blocks, each of which has a `type` that determines its shape.
Example:

[{"type": "text", "text": "Hi, I'm Claude."}]

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.
For example, if the input `messages` were:

[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]

Then the response `content` might be:

[{"type": "text", "text": "B)"}]

text_block: object { citations, text, type } 
citations: array of [TextCitation](https://platform.claude.com/docs/en/api/messages#text_citation)
Citations supporting the text block.
The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.
citation_char_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.end_char_index)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.file_id)
start_char_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B0%5D)
citation_page_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.end_page_number)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.file_id)
start_page_number: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B1%5D)
citation_content_block_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.end_block_index)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.file_id)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B2%5D)
citations_web_search_result_location: object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.type)
url: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.url)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B3%5D)
citations_search_result_location: object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_block.citations)
text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B0%5D)
thinking_block: object { signature, thinking, type } 
signature: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_block.signature)
thinking: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_block.thinking)
type: "thinking"
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B1%5D)
redacted_thinking_block: object { data, type } 
data: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#redacted_thinking_block.data)
type: "redacted_thinking"
[](https://platform.claude.com/docs/en/api/cli/messages/create#redacted_thinking_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B2%5D)
tool_use_block: object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.input)
name: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.name)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B3%5D)
server_tool_use_block: object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.input)
name: "web_search" or "web_fetch" or "code_execution" or 4 more
"web_search"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B0%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B2%5D)
"bash_code_execution"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B3%5D)
"text_editor_code_execution"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B4%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B5%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B6%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name)
type: "server_tool_use"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B4%5D)
web_search_tool_result_block: object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.caller)
content: [WebSearchToolResultError](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_error) { error_code, type }  or array of [WebSearchResultBlock](https://platform.claude.com/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } 
web_search_tool_result_error: object { error_code, type } 
error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B1%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B2%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B3%5D)
"query_too_long"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B4%5D)
"request_too_large"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B5%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error.error_code)
type: "web_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block_content%5B0%5D)
union_member_1: array of [WebSearchResultBlock](https://platform.claude.com/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } 
encrypted_content: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.encrypted_content)
page_age: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.page_age)
title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.title)
type: "web_search_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.type)
url: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.url)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block_content%5B1%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.tool_use_id)
type: "web_search_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B5%5D)
web_fetch_tool_result_block: object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.caller)
content: [WebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type }  or [WebFetchBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url } 
web_fetch_tool_result_error_block: object { error_code, type } 
error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 6 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B0%5D)
"url_too_long"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B1%5D)
"url_not_allowed"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B2%5D)
"url_not_in_prior_context"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B3%5D)
"url_not_accessible"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B4%5D)
"unsupported_content_type"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B5%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B6%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B7%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B8%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_block.error_code)
type: "web_fetch_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_block)
web_fetch_block: object { content, retrieved_at, type, url } 
content: object { citations, source, title, type } 
citations: object { enabled } 
Citation configuration for the document
enabled: boolean
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_config.enabled)
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.citations)
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type } 
base64_pdf_source: object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source)
plain_text_source: object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source)
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.source)
title: string
The title of the document
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.title)
type: "document"
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.content)
retrieved_at: string
ISO 8601 timestamp when the content was retrieved
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.retrieved_at)
type: "web_fetch_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.type)
url: string
Fetched content URL
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.url)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.tool_use_id)
type: "web_fetch_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B6%5D)
code_execution_tool_result_block: object { content, tool_use_id, type } 
content: [CodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_error) { error_code, type }  or [CodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#code_execution_result_block) { content, return_code, stderr, 2 more }  or [EncryptedCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#encrypted_code_execution_result_block) { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
code_execution_tool_result_error: object { error_code, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B3%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error.error_code)
type: "code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block_content%5B0%5D)
code_execution_result_block: object { content, return_code, stderr, 2 more } 
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.content)
return_code: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.stdout)
type: "code_execution_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block_content%5B1%5D)
encrypted_code_execution_result_block: object { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.content)
encrypted_stdout: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.encrypted_stdout)
return_code: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.stderr)
type: "encrypted_code_execution_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block_content%5B2%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block.tool_use_id)
type: "code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B7%5D)
bash_code_execution_tool_result_block: object { content, tool_use_id, type } 
content: [BashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type }  or [BashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more } 
bash_code_execution_tool_result_error: object { error_code, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B3%5D)
"output_file_too_large"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error.error_code)
type: "bash_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error)
bash_code_execution_result_block: object { content, return_code, stderr, 2 more } 
content: array of [BashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_output_block.file_id)
type: "bash_code_execution_output"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_output_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.content)
return_code: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.stdout)
type: "bash_code_execution_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_block.tool_use_id)
type: "bash_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B8%5D)
text_editor_code_execution_tool_result_block: object { content, tool_use_id, type } 
content: [TextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type }  or [TextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more } 
text_editor_code_execution_tool_result_error: object { error_code, error_message, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B3%5D)
"file_not_found"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error.error_message)
type: "text_editor_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error)
text_editor_code_execution_view_result_block: object { content, file_type, num_lines, 3 more } 
content: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.content)
file_type: "text" or "image" or "pdf"
"text"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type%5B0%5D)
"image"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type%5B1%5D)
"pdf"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type)
num_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.num_lines)
start_line: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.start_line)
total_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.total_lines)
type: "text_editor_code_execution_view_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block)
text_editor_code_execution_create_result_block: object { is_file_update, type } 
is_file_update: boolean
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_create_result_block.is_file_update)
type: "text_editor_code_execution_create_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_create_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_create_result_block)
text_editor_code_execution_str_replace_result_block: object { lines, new_lines, new_start, 3 more } 
lines: array of string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.lines)
new_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.new_lines)
new_start: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.new_start)
old_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.old_lines)
old_start: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.old_start)
type: "text_editor_code_execution_str_replace_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_block.tool_use_id)
type: "text_editor_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B9%5D)
tool_search_tool_result_block: object { content, tool_use_id, type } 
content: [ToolSearchToolResultError](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type }  or [ToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type } 
tool_search_tool_result_error: object { error_code, error_message, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B3%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error.error_message)
type: "tool_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error)
tool_search_tool_search_result_block: object { tool_references, type } 
tool_references: array of [ToolReferenceBlock](https://platform.claude.com/docs/en/api/messages#tool_reference_block) { tool_name, type } 
tool_name: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_reference_block.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_reference_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_search_result_block.tool_references)
type: "tool_search_tool_search_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_search_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_search_result_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_block.tool_use_id)
type: "tool_search_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B10%5D)
container_upload_block: object { file_id, type } 
Response model for a file uploaded to the container.
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#container_upload_block.file_id)
type: "container_upload"
[](https://platform.claude.com/docs/en/api/cli/messages/create#container_upload_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#content_block%5B11%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.content)
model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/cli/messages/create#model%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.model)
role: "assistant"
Conversational role of the generated message.
This will always be `"assistant"`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.role)
stop_details: object { category, explanation, type } 
Structured information about a refusal.
category: "cyber" or "bio" or "frontier_llm" or "reasoning_extraction"
The policy category that triggered a refusal.
"cyber"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B0%5D)
"bio"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B1%5D)
"frontier_llm"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B2%5D)
"reasoning_extraction"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B3%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category)
explanation: string
Human-readable explanation of the refusal.
This text is not guaranteed to be stable. `null` when no explanation is available for the category.
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.explanation)
type: "refusal"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.stop_details)
stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 3 more
The reason that we stopped.
This may be one the following values:
  * `"end_turn"`: the model reached a natural stopping point
  * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
  * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
  * `"tool_use"`: the model invoked one or more tools
  * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
  * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.
"end_turn"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B0%5D)
"max_tokens"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B1%5D)
"stop_sequence"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B2%5D)
"tool_use"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B3%5D)
"pause_turn"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B4%5D)
"refusal"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B5%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.stop_reason)
stop_sequence: string
Which custom stop sequence was generated, if any.
This value will be a non-null string if one of your custom stop sequences was generated.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.stop_sequence)
type: "message"
Object type.
For Messages, this is always `"message"`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.type)
usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more } 
Billing and rate-limit usage.
Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.
Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.
For example, `output_tokens` will be non-zero, even for an empty string response from Claude.
Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.
cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
Breakdown of cached tokens by TTL
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/cli/messages/create#cache_creation.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/cli/messages/create#cache_creation.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.cache_creation)
cache_creation_input_tokens: number
The number of input tokens used to create the cache entry.
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.cache_creation_input_tokens)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.cache_read_input_tokens)
inference_geo: string
The geographic region where inference was performed for this request.
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.inference_geo)
input_tokens: number
The number of input tokens which were used.
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.input_tokens)
output_tokens: number
The number of output tokens which were used.
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.output_tokens)
output_tokens_details: object { thinking_tokens } 
Breakdown of output tokens by category.
`output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you.
thinking_tokens: number
Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.
Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.
[](https://platform.claude.com/docs/en/api/cli/messages/create#output_tokens_details.thinking_tokens)
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.output_tokens_details)
server_tool_use: object { web_fetch_requests, web_search_requests } 
The number of server tool requests.
web_fetch_requests: number
The number of web fetch tool requests.
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_usage.web_fetch_requests)
web_search_requests: number
The number of web search tool requests.
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_usage.web_search_requests)
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.server_tool_use)
service_tier: "standard" or "priority" or "batch"
If the request used the priority, standard, or batch tier.
"standard"
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.service_tier%5B0%5D)
"priority"
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.service_tier%5B1%5D)
"batch"
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.service_tier%5B2%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#usage.service_tier)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message.usage)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_start_event.message)
type: "message_start"
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_start_event.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_stream_event%5B0%5D)
raw_message_delta_event: object { delta, type, usage } 
delta: object { container, stop_details, stop_reason, stop_sequence } 
container: object { id, expires_at } 
Information about the container used in the request (for the code execution tool)
Identifier for the container used in this request
[](https://platform.claude.com/docs/en/api/cli/messages/create#container.id)
expires_at: string
The time at which the container will expire.
[](https://platform.claude.com/docs/en/api/cli/messages/create#container.expires_at)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_delta_event.delta.container)
stop_details: object { category, explanation, type } 
Structured information about a refusal.
category: "cyber" or "bio" or "frontier_llm" or "reasoning_extraction"
The policy category that triggered a refusal.
"cyber"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B0%5D)
"bio"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B1%5D)
"frontier_llm"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B2%5D)
"reasoning_extraction"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category%5B3%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.category)
explanation: string
Human-readable explanation of the refusal.
This text is not guaranteed to be stable. `null` when no explanation is available for the category.
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.explanation)
type: "refusal"
[](https://platform.claude.com/docs/en/api/cli/messages/create#refusal_stop_details.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_delta_event.delta.stop_details)
stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 3 more
"end_turn"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B0%5D)
"max_tokens"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B1%5D)
"stop_sequence"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B2%5D)
"tool_use"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B3%5D)
"pause_turn"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B4%5D)
"refusal"
[](https://platform.claude.com/docs/en/api/cli/messages/create#stop_reason%5B5%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_delta_event.delta.stop_reason)
stop_sequence: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_delta_event.delta.stop_sequence)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_delta_event.delta)
type: "message_delta"
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_delta_event.type)
usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more } 
Billing and rate-limit usage.
Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.
Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.
For example, `output_tokens` will be non-zero, even for an empty string response from Claude.
Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.
cache_creation_input_tokens: number
The cumulative number of input tokens used to create the cache entry.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message_delta_usage.cache_creation_input_tokens)
cache_read_input_tokens: number
The cumulative number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message_delta_usage.cache_read_input_tokens)
input_tokens: number
The cumulative number of input tokens which were used.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message_delta_usage.input_tokens)
output_tokens: number
The cumulative number of output tokens which were used.
[](https://platform.claude.com/docs/en/api/cli/messages/create#message_delta_usage.output_tokens)
output_tokens_details: object { thinking_tokens } 
Breakdown of output tokens by category.
`output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you.
thinking_tokens: number
Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.
Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.
[](https://platform.claude.com/docs/en/api/cli/messages/create#output_tokens_details.thinking_tokens)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message_delta_usage.output_tokens_details)
server_tool_use: object { web_fetch_requests, web_search_requests } 
The number of server tool requests.
web_fetch_requests: number
The number of web fetch tool requests.
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_usage.web_fetch_requests)
web_search_requests: number
The number of web search tool requests.
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_usage.web_search_requests)
[](https://platform.claude.com/docs/en/api/cli/messages/create#message_delta_usage.server_tool_use)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_delta_event.usage)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_stream_event%5B1%5D)
raw_message_stop_event: object { type } 
type: "message_stop"
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_stop_event.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_stream_event%5B2%5D)
raw_content_block_start_event: object { content_block, index, type } 
content_block: [TextBlock](https://platform.claude.com/docs/en/api/messages#text_block) { citations, text, type }  or [ThinkingBlock](https://platform.claude.com/docs/en/api/messages#thinking_block) { signature, thinking, type }  or [RedactedThinkingBlock](https://platform.claude.com/docs/en/api/messages#redacted_thinking_block) { data, type }  or 9 more
Response model for a file uploaded to the container.
text_block: object { citations, text, type } 
citations: array of [TextCitation](https://platform.claude.com/docs/en/api/messages#text_citation)
Citations supporting the text block.
The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.
citation_char_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.end_char_index)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.file_id)
start_char_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B0%5D)
citation_page_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.end_page_number)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.file_id)
start_page_number: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B1%5D)
citation_content_block_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.end_block_index)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.file_id)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B2%5D)
citations_web_search_result_location: object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.type)
url: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.url)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B3%5D)
citations_search_result_location: object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_citation%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_block.citations)
text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_block)
thinking_block: object { signature, thinking, type } 
signature: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_block.signature)
thinking: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_block.thinking)
type: "thinking"
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_block)
redacted_thinking_block: object { data, type } 
data: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#redacted_thinking_block.data)
type: "redacted_thinking"
[](https://platform.claude.com/docs/en/api/cli/messages/create#redacted_thinking_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#redacted_thinking_block)
tool_use_block: object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.input)
name: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.name)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_use_block)
server_tool_use_block: object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.input)
name: "web_search" or "web_fetch" or "code_execution" or 4 more
"web_search"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B0%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B2%5D)
"bash_code_execution"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B3%5D)
"text_editor_code_execution"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B4%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B5%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name%5B6%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.name)
type: "server_tool_use"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_use_block)
web_search_tool_result_block: object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.caller)
content: [WebSearchToolResultError](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_error) { error_code, type }  or array of [WebSearchResultBlock](https://platform.claude.com/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } 
web_search_tool_result_error: object { error_code, type } 
error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B1%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B2%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B3%5D)
"query_too_long"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B4%5D)
"request_too_large"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error_code%5B5%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error.error_code)
type: "web_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block_content%5B0%5D)
union_member_1: array of [WebSearchResultBlock](https://platform.claude.com/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } 
encrypted_content: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.encrypted_content)
page_age: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.page_age)
title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.title)
type: "web_search_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.type)
url: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_result_block.url)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block_content%5B1%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.tool_use_id)
type: "web_search_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_search_tool_result_block)
web_fetch_tool_result_block: object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
direct_caller: object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#direct_caller)
server_tool_caller: object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller)
server_tool_caller_20260120: object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.caller)
content: [WebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type }  or [WebFetchBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url } 
web_fetch_tool_result_error_block: object { error_code, type } 
error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 6 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B0%5D)
"url_too_long"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B1%5D)
"url_not_allowed"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B2%5D)
"url_not_in_prior_context"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B3%5D)
"url_not_accessible"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B4%5D)
"unsupported_content_type"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B5%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B6%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B7%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_code%5B8%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_block.error_code)
type: "web_fetch_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_error_block)
web_fetch_block: object { content, retrieved_at, type, url } 
content: object { citations, source, title, type } 
citations: object { enabled } 
Citation configuration for the document
enabled: boolean
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_config.enabled)
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.citations)
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type } 
base64_pdf_source: object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#base64_pdf_source)
plain_text_source: object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#plain_text_source)
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.source)
title: string
The title of the document
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.title)
type: "document"
[](https://platform.claude.com/docs/en/api/cli/messages/create#document_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.content)
retrieved_at: string
ISO 8601 timestamp when the content was retrieved
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.retrieved_at)
type: "web_fetch_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.type)
url: string
Fetched content URL
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block.url)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.tool_use_id)
type: "web_fetch_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#web_fetch_tool_result_block)
code_execution_tool_result_block: object { content, tool_use_id, type } 
content: [CodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_error) { error_code, type }  or [CodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#code_execution_result_block) { content, return_code, stderr, 2 more }  or [EncryptedCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#encrypted_code_execution_result_block) { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
code_execution_tool_result_error: object { error_code, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error_code%5B3%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error.error_code)
type: "code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block_content%5B0%5D)
code_execution_result_block: object { content, return_code, stderr, 2 more } 
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.content)
return_code: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.stdout)
type: "code_execution_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block_content%5B1%5D)
encrypted_code_execution_result_block: object { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_output_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.content)
encrypted_stdout: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.encrypted_stdout)
return_code: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.stderr)
type: "encrypted_code_execution_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#encrypted_code_execution_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block_content%5B2%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block.tool_use_id)
type: "code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#code_execution_tool_result_block)
bash_code_execution_tool_result_block: object { content, tool_use_id, type } 
content: [BashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type }  or [BashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more } 
bash_code_execution_tool_result_error: object { error_code, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B3%5D)
"output_file_too_large"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error_code%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error.error_code)
type: "bash_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_error)
bash_code_execution_result_block: object { content, return_code, stderr, 2 more } 
content: array of [BashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_output_block.file_id)
type: "bash_code_execution_output"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_output_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.content)
return_code: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.stdout)
type: "bash_code_execution_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_result_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_block.tool_use_id)
type: "bash_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#bash_code_execution_tool_result_block)
text_editor_code_execution_tool_result_block: object { content, tool_use_id, type } 
content: [TextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type }  or [TextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more } 
text_editor_code_execution_tool_result_error: object { error_code, error_message, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B3%5D)
"file_not_found"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error_code%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error.error_message)
type: "text_editor_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_error)
text_editor_code_execution_view_result_block: object { content, file_type, num_lines, 3 more } 
content: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.content)
file_type: "text" or "image" or "pdf"
"text"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type%5B0%5D)
"image"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type%5B1%5D)
"pdf"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.file_type)
num_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.num_lines)
start_line: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.start_line)
total_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.total_lines)
type: "text_editor_code_execution_view_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_view_result_block)
text_editor_code_execution_create_result_block: object { is_file_update, type } 
is_file_update: boolean
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_create_result_block.is_file_update)
type: "text_editor_code_execution_create_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_create_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_create_result_block)
text_editor_code_execution_str_replace_result_block: object { lines, new_lines, new_start, 3 more } 
lines: array of string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.lines)
new_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.new_lines)
new_start: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.new_start)
old_lines: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.old_lines)
old_start: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.old_start)
type: "text_editor_code_execution_str_replace_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_str_replace_result_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_block.tool_use_id)
type: "text_editor_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_editor_code_execution_tool_result_block)
tool_search_tool_result_block: object { content, tool_use_id, type } 
content: [ToolSearchToolResultError](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type }  or [ToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type } 
tool_search_tool_result_error: object { error_code, error_message, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error_code%5B3%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error.error_message)
type: "tool_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_error)
tool_search_tool_search_result_block: object { tool_references, type } 
tool_references: array of [ToolReferenceBlock](https://platform.claude.com/docs/en/api/messages#tool_reference_block) { tool_name, type } 
tool_name: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_reference_block.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_reference_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_search_result_block.tool_references)
type: "tool_search_tool_search_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_search_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_search_result_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_block.tool_use_id)
type: "tool_search_tool_result"
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#tool_search_tool_result_block)
container_upload_block: object { file_id, type } 
Response model for a file uploaded to the container.
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#container_upload_block.file_id)
type: "container_upload"
[](https://platform.claude.com/docs/en/api/cli/messages/create#container_upload_block.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#container_upload_block)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_start_event.content_block)
index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_start_event.index)
type: "content_block_start"
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_start_event.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_stream_event%5B3%5D)
raw_content_block_delta_event: object { delta, index, type } 
delta: [TextDelta](https://platform.claude.com/docs/en/api/messages#text_delta) { text, type }  or [InputJSONDelta](https://platform.claude.com/docs/en/api/messages#input_json_delta) { partial_json, type }  or [CitationsDelta](https://platform.claude.com/docs/en/api/messages#citations_delta) { citation, type }  or 2 more
text_delta: object { text, type } 
text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_delta.text)
type: "text_delta"
[](https://platform.claude.com/docs/en/api/cli/messages/create#text_delta.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_delta%5B0%5D)
input_json_delta: object { partial_json, type } 
partial_json: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#input_json_delta.partial_json)
type: "input_json_delta"
[](https://platform.claude.com/docs/en/api/cli/messages/create#input_json_delta.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_delta%5B1%5D)
citations_delta: object { citation, type } 
citation: [CitationCharLocation](https://platform.claude.com/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more }  or [CitationPageLocation](https://platform.claude.com/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more }  or [CitationContentBlockLocation](https://platform.claude.com/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more }  or 2 more
citation_char_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.end_char_index)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.file_id)
start_char_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_char_location)
citation_page_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.end_page_number)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.file_id)
start_page_number: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_page_location)
citation_content_block_location: object { cited_text, document_index, document_title, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.end_block_index)
file_id: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.file_id)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#citation_content_block_location)
citations_web_search_result_location: object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.type)
url: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location.url)
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_web_search_result_location)
citations_search_result_location: object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_search_result_location)
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_delta.citation)
type: "citations_delta"
[](https://platform.claude.com/docs/en/api/cli/messages/create#citations_delta.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_delta%5B2%5D)
thinking_delta: object { thinking, type } 
thinking: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_delta.thinking)
type: "thinking_delta"
[](https://platform.claude.com/docs/en/api/cli/messages/create#thinking_delta.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_delta%5B3%5D)
signature_delta: object { signature, type } 
signature: string
[](https://platform.claude.com/docs/en/api/cli/messages/create#signature_delta.signature)
type: "signature_delta"
[](https://platform.claude.com/docs/en/api/cli/messages/create#signature_delta.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_delta%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_delta_event.delta)
index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_delta_event.index)
type: "content_block_delta"
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_delta_event.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_stream_event%5B4%5D)
raw_content_block_stop_event: object { index, type } 
index: number
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_stop_event.index)
type: "content_block_stop"
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_content_block_stop_event.type)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_stream_event%5B5%5D)
[](https://platform.claude.com/docs/en/api/cli/messages/create#raw_message_stream_event)
Create a Message
CLI

ant messages create \
  --api-key my-anthropic-api-key \
  --max-tokens 1024 \
  --message '{content: [{text: x, type: text}], role: user}' \
  --model claude-opus-4-6

  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z"
  "content": [
      "citations": [
          "cited_text": "cited_text",
          "document_index": 0,
          "document_title": "document_title",
          "end_char_index": 0,
          "file_id": "file_id",
          "start_char_index": 0,
          "type": "char_location"
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
  ],
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "explanation",
    "type": "refusal"
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "inference_geo",
    "input_tokens": 2095,
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    "service_tier": "standard"

  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z"
  "content": [
      "citations": [
          "cited_text": "cited_text",
          "document_index": 0,
          "document_title": "document_title",
          "end_char_index": 0,
          "file_id": "file_id",
          "start_char_index": 0,
          "type": "char_location"
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
  ],
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "explanation",
    "type": "refusal"
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "inference_geo",
    "input_tokens": 2095,
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    "service_tier": "standard"
