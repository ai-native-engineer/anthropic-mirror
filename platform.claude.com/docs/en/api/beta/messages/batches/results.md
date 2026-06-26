<!-- source: https://platform.claude.com/docs/en/api/beta/messages/batches/results -->

# Retrieve Message Batch results
GET/v1/messages/batches/{message_batch_id}/results
Streams the results of a Message Batch as a `.jsonl` file.
Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.
Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)
##### Path ParametersExpand Collapse 
message_batch_id: string
ID of the Message Batch.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#results.message_batch_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#results.betas)
BetaMessageBatchIndividualResponse object { custom_id, result } 
This is a single line in the response `.jsonl` file and does not represent the response as a whole.
custom_id: string
Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.
Must be unique for each request within the Message Batch.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.custom_id)
result: [BetaMessageBatchResult](https://platform.claude.com/docs/en/api/beta#beta_message_batch_result)
Processing result for this request.
Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.
BetaMessageBatchSucceededResult object { message, type } 
message: [BetaMessage](https://platform.claude.com/docs/en/api/beta#beta_message) { id, container, content, 9 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.id)
container: [BetaContainer](https://platform.claude.com/docs/en/api/beta#beta_container) { id, expires_at, skills } 
Information about the container used in the request (for the code execution tool)
Identifier for the container used in this request
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.container%20%2B%20\(resource\)%20beta.messages.id)
expires_at: string
The time at which the container will expire.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.container%20%2B%20\(resource\)%20beta.messages.expires_at)
skills: array of [BetaSkill](https://platform.claude.com/docs/en/api/beta#beta_skill) { skill_id, type, version } 
Skills loaded in the container
skill_id: string
Skill ID
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.container%20%2B%20\(resource\)%20beta.messages.skill_id)
type: "anthropic" or "custom"
Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)
"anthropic"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.container%20%2B%20\(resource\)%20beta.messages.type%5B0%5D)
"custom"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.container%20%2B%20\(resource\)%20beta.messages.type%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.container%20%2B%20\(resource\)%20beta.messages.type)
version: string
Skill version or 'latest' for most recent version
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.container%20%2B%20\(resource\)%20beta.messages.version)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.container%20%2B%20\(resource\)%20beta.messages.skills)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.container)
content: array of [BetaContentBlock](https://platform.claude.com/docs/en/api/beta#beta_content_block)
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

BetaTextBlock object { citations, text, type } 
citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)
Citations supporting the text block.
The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.
BetaCitationCharLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.end_char_index)
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_id)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaCitationPageLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.end_page_number)
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_id)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaCitationContentBlockLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.end_block_index)
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_id)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaCitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaCitationSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.citations)
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaThinkingBlock object { signature, thinking, type } 
signature: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.signature)
thinking: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.thinking)
type: "thinking"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaRedactedThinkingBlock object { data, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.data)
type: "redacted_thinking"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaToolUseBlock object { id, input, name, 2 more } 
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.id)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.input)
name: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.name)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }  or [BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
BetaDirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.caller)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaServerToolUseBlock object { id, input, name, 2 more } 
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.id)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.input)
name: "advisor" or "web_search" or "web_fetch" or 5 more
"advisor"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.name%5B0%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.name%5B1%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.name%5B2%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.name%5B3%5D)
"bash_code_execution"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.name%5B4%5D)
"text_editor_code_execution"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.name%5B5%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.name%5B6%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.name%5B7%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.name)
type: "server_tool_use"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }  or [BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
BetaDirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.caller)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaWebSearchToolResultBlock object { content, tool_use_id, type, caller } 
content: [BetaWebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_content)
BetaWebSearchToolResultError object { error_code, type } 
error_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_error.error_code%20%2B%20\(resource\)%20beta.messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_error.error_code%20%2B%20\(resource\)%20beta.messages%5B1%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_error.error_code%20%2B%20\(resource\)%20beta.messages%5B2%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_error.error_code%20%2B%20\(resource\)%20beta.messages%5B3%5D)
"query_too_long"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_error.error_code%20%2B%20\(resource\)%20beta.messages%5B4%5D)
"request_too_large"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_error.error_code%20%2B%20\(resource\)%20beta.messages%5B5%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.error_code)
type: "web_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_block.content%20%2B%20\(resource\)%20beta.messages)
array of [BetaWebSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block) { encrypted_content, page_age, title, 2 more } 
encrypted_content: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.encrypted_content)
page_age: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.page_age)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.title)
type: "web_search_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_search_tool_result_block.content%20%2B%20\(resource\)%20beta.messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_use_id)
type: "web_search_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }  or [BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
BetaDirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.caller)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaWebFetchToolResultBlock object { content, tool_use_id, type, caller } 
content: [BetaWebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block) { error_code, type }  or [BetaWebFetchBlock](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block) { content, retrieved_at, type, url } 
BetaWebFetchToolResultErrorBlock object { error_code, type } 
error_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20beta.messages%5B0%5D)
"url_too_long"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20beta.messages%5B1%5D)
"url_not_allowed"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20beta.messages%5B2%5D)
"url_not_in_prior_context"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20beta.messages%5B3%5D)
"url_not_accessible"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20beta.messages%5B4%5D)
"unsupported_content_type"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20beta.messages%5B5%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20beta.messages%5B6%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20beta.messages%5B7%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20beta.messages%5B8%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code)
type: "web_fetch_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaWebFetchBlock object { content, retrieved_at, type, url } 
content: [BetaDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_document_block) { citations, source, title, type } 
citations: [BetaCitationConfig](https://platform.claude.com/docs/en/api/beta#beta_citation_config) { enabled } 
Citation configuration for the document
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_document_block.citations%20%2B%20\(resource\)%20beta.messages.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages.citations)
source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type }  or [BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media_type, type } 
BetaBase64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages)
BetaPlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages.source)
title: string
The title of the document
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages.title)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_web_fetch_block.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
retrieved_at: string
ISO 8601 timestamp when the content was retrieved
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.retrieved_at)
type: "web_fetch_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
url: string
Fetched content URL
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_use_id)
type: "web_fetch_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }  or [BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
BetaDirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.caller)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaAdvisorToolResultBlock object { content, tool_use_id, type } 
content: [BetaAdvisorToolResultError](https://platform.claude.com/docs/en/api/beta#beta_advisor_tool_result_error) { error_code, type }  or [BetaAdvisorResultBlock](https://platform.claude.com/docs/en/api/beta#beta_advisor_result_block) { stop_reason, text, type }  or [BetaAdvisorRedactedResultBlock](https://platform.claude.com/docs/en/api/beta#beta_advisor_redacted_result_block) { encrypted_content, stop_reason, type } 
BetaAdvisorToolResultError object { error_code, type } 
error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 4 more
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B0%5D)
"prompt_too_long"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B2%5D)
"overloaded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B3%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B4%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B5%5D)
"model_not_found"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B6%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code)
type: "advisor_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaAdvisorResultBlock object { stop_reason, text, type } 
stop_reason: string
The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.stop_reason)
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.text)
type: "advisor_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaAdvisorRedactedResultBlock object { encrypted_content, stop_reason, type } 
encrypted_content: string
Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.encrypted_content)
stop_reason: string
The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.stop_reason)
type: "advisor_redacted_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_use_id)
type: "advisor_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaCodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [BetaCodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_content)
Code execution result with encrypted stdout for PFC + web_search results.
BetaCodeExecutionToolResultError object { error_code, type } 
error_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20beta.messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20beta.messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20beta.messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20beta.messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.error_code)
type: "code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages)
BetaCodeExecutionResultBlock object { content, return_code, stderr, 2 more } 
content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.content)
return_code: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.stdout)
type: "code_execution_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages)
BetaEncryptedCodeExecutionResultBlock object { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
content: array of [BetaCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.content)
encrypted_stdout: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.encrypted_stdout)
return_code: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.stderr)
type: "encrypted_code_execution_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_code_execution_tool_result_block.content%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_use_id)
type: "code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaBashCodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [BetaBashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error) { error_code, type }  or [BetaBashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block) { content, return_code, stderr, 2 more } 
BetaBashCodeExecutionToolResultError object { error_code, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B3%5D)
"output_file_too_large"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B4%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code)
type: "bash_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaBashCodeExecutionResultBlock object { content, return_code, stderr, 2 more } 
content: array of [BetaBashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_id)
type: "bash_code_execution_output"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
return_code: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.stdout)
type: "bash_code_execution_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_use_id)
type: "bash_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaTextEditorCodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [BetaTextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error) { error_code, error_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block) { is_file_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more } 
BetaTextEditorCodeExecutionToolResultError object { error_code, error_message, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B3%5D)
"file_not_found"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B4%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_message)
type: "text_editor_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaTextEditorCodeExecutionViewResultBlock object { content, file_type, num_lines, 3 more } 
content: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
file_type: "text" or "image" or "pdf"
"text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_type%5B0%5D)
"image"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_type%5B1%5D)
"pdf"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_type)
num_lines: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.num_lines)
start_line: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.start_line)
total_lines: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.total_lines)
type: "text_editor_code_execution_view_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaTextEditorCodeExecutionCreateResultBlock object { is_file_update, type } 
is_file_update: boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.is_file_update)
type: "text_editor_code_execution_create_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaTextEditorCodeExecutionStrReplaceResultBlock object { lines, new_lines, new_start, 3 more } 
lines: array of string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.lines)
new_lines: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.new_lines)
new_start: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.new_start)
old_lines: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.old_lines)
old_start: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.old_start)
type: "text_editor_code_execution_str_replace_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_use_id)
type: "text_editor_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaToolSearchToolResultBlock object { content, tool_use_id, type } 
content: [BetaToolSearchToolResultError](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error) { error_code, error_message, type }  or [BetaToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block) { tool_references, type } 
BetaToolSearchToolResultError object { error_code, error_message, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.error_message)
type: "tool_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaToolSearchToolSearchResultBlock object { tool_references, type } 
tool_references: array of [BetaToolReferenceBlock](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block) { tool_name, type } 
tool_name: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_references)
type: "tool_search_tool_search_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_use_id)
type: "tool_search_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaMCPToolUseBlock object { id, input, name, 2 more } 
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.id)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.input)
name: string
The name of the MCP tool
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.name)
server_name: string
The name of the MCP server
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.server_name)
type: "mcp_tool_use"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaMCPToolResultBlock object { content, is_error, tool_use_id, type } 
content: string or array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type } 
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content%5B0%5D)
BetaMCPToolResultBlockContent = array of [BetaTextBlock](https://platform.claude.com/docs/en/api/beta#beta_text_block) { citations, text, type } 
citations: array of [BetaTextCitation](https://platform.claude.com/docs/en/api/beta#beta_text_citation)
Citations supporting the text block.
The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.
BetaCitationCharLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.end_char_index)
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_id)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaCitationPageLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.end_page_number)
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_id)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaCitationContentBlockLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.end_block_index)
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_id)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaCitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaCitationSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.citations)
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
is_error: boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.is_error)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.tool_use_id)
type: "mcp_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaContainerUploadBlock object { file_id, type } 
Response model for a file uploaded to the container.
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.file_id)
type: "container_upload"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaCompactionBlock object { content, encrypted_content, type } 
A compaction block returned when autocompact is triggered.
When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.
content: string
Summary of compacted content, or null if compaction failed
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
encrypted_content: string
Opaque metadata from prior compaction, to be round-tripped verbatim
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.encrypted_content)
type: "compaction"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
BetaFallbackBlock object { from, to, trigger, type } 
Marks the point in `content` where one model's output gives way to the next.
One block appears per hop where a preceding model actually ran this turn and declined. A turn where no preceding model ran and declined has no such boundary and carries no block — the signal for whether a fallback model served the response is the presence of a `fallback_message` entry in `usage.iterations`, not this block.
The block is treated like a server-tool content block for streaming: it arrives via the standard `content_block_start` / `content_block_stop` pair and carries no deltas.
from: [BetaFallbackInfo](https://platform.claude.com/docs/en/api/beta#beta_fallback_info) { model } 
The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_block.from%20%2B%20\(resource\)%20beta.messages.model)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.from)
to: [BetaFallbackInfo](https://platform.claude.com/docs/en/api/beta#beta_fallback_info) { model } 
The fallback model producing the content that follows this block. Its `model` is always the canonical id.
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_info.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_block.to%20%2B%20\(resource\)%20beta.messages.model)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.to)
trigger: [BetaFallbackRefusalTrigger](https://platform.claude.com/docs/en/api/beta#beta_fallback_refusal_trigger) { category, type } 
What caused the `from` model to hand over at this hop.
category: "cyber" or "bio" or "frontier_llm" or "reasoning_extraction"
The policy category that triggered a refusal.
"cyber"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_block.trigger%20%2B%20\(resource\)%20beta.messages.category%5B0%5D)
"bio"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_block.trigger%20%2B%20\(resource\)%20beta.messages.category%5B1%5D)
"frontier_llm"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_block.trigger%20%2B%20\(resource\)%20beta.messages.category%5B2%5D)
"reasoning_extraction"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_block.trigger%20%2B%20\(resource\)%20beta.messages.category%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_block.trigger%20%2B%20\(resource\)%20beta.messages.category)
type: "refusal"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_block.trigger%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.trigger)
type: "fallback"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.content)
context_management: [BetaContextManagementResponse](https://platform.claude.com/docs/en/api/beta#beta_context_management_response) { applied_edits } 
Context management response.
Information about context management strategies applied during the request.
applied_edits: array of [BetaClearToolUses20250919EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit_response) { cleared_input_tokens, cleared_tool_uses, type }  or [BetaClearThinking20251015EditResponse](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit_response) { cleared_input_tokens, cleared_thinking_turns, type } 
List of context management edits that were applied.
BetaClearToolUses20250919EditResponse object { cleared_input_tokens, cleared_tool_uses, type } 
cleared_input_tokens: number
Number of input tokens cleared by this edit.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.context_management%20%2B%20\(resource\)%20beta.messages.cleared_input_tokens)
cleared_tool_uses: number
Number of tool uses that were cleared.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.context_management%20%2B%20\(resource\)%20beta.messages.cleared_tool_uses)
type: "clear_tool_uses_20250919"
The type of context management edit applied.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.context_management%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.context_management%20%2B%20\(resource\)%20beta.messages)
BetaClearThinking20251015EditResponse object { cleared_input_tokens, cleared_thinking_turns, type } 
cleared_input_tokens: number
Number of input tokens cleared by this edit.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.context_management%20%2B%20\(resource\)%20beta.messages.cleared_input_tokens)
cleared_thinking_turns: number
Number of thinking turns that were cleared.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.context_management%20%2B%20\(resource\)%20beta.messages.cleared_thinking_turns)
type: "clear_thinking_20251015"
The type of context management edit applied.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.context_management%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.context_management%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.context_management%20%2B%20\(resource\)%20beta.messages.applied_edits)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.context_management)
diagnostics: [BetaDiagnostics](https://platform.claude.com/docs/en/api/beta#beta_diagnostics) { cache_miss_reason } 
Response envelope for request-level diagnostics. Present (possibly null) whenever the caller supplied `diagnostics` on the request.
cache_miss_reason: [BetaCacheMissModelChanged](https://platform.claude.com/docs/en/api/beta#beta_cache_miss_model_changed) { cache_missed_input_tokens, type }  or [BetaCacheMissSystemChanged](https://platform.claude.com/docs/en/api/beta#beta_cache_miss_system_changed) { cache_missed_input_tokens, type }  or [BetaCacheMissToolsChanged](https://platform.claude.com/docs/en/api/beta#beta_cache_miss_tools_changed) { cache_missed_input_tokens, type }  or 3 more
Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.
BetaCacheMissModelChanged object { cache_missed_input_tokens, type } 
cache_missed_input_tokens: number
Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages.cache_missed_input_tokens)
type: "model_changed"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages)
BetaCacheMissSystemChanged object { cache_missed_input_tokens, type } 
cache_missed_input_tokens: number
Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages.cache_missed_input_tokens)
type: "system_changed"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages)
BetaCacheMissToolsChanged object { cache_missed_input_tokens, type } 
cache_missed_input_tokens: number
Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages.cache_missed_input_tokens)
type: "tools_changed"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages)
BetaCacheMissMessagesChanged object { cache_missed_input_tokens, type } 
cache_missed_input_tokens: number
Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages.cache_missed_input_tokens)
type: "messages_changed"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages)
BetaCacheMissPreviousMessageNotFound object { type } 
type: "previous_message_not_found"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages)
BetaCacheMissUnavailable object { type } 
type: "unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.diagnostics%20%2B%20\(resource\)%20beta.messages.cache_miss_reason)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.diagnostics)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.model)
role: "assistant"
Conversational role of the generated message.
This will always be `"assistant"`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.role)
stop_details: [BetaRefusalStopDetails](https://platform.claude.com/docs/en/api/beta#beta_refusal_stop_details) { category, explanation, fallback_credit_token, 3 more } 
Structured information about a refusal.
category: "cyber" or "bio" or "frontier_llm" or "reasoning_extraction"
The policy category that triggered a refusal.
"cyber"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_details%20%2B%20\(resource\)%20beta.messages.category%5B0%5D)
"bio"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_details%20%2B%20\(resource\)%20beta.messages.category%5B1%5D)
"frontier_llm"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_details%20%2B%20\(resource\)%20beta.messages.category%5B2%5D)
"reasoning_extraction"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_details%20%2B%20\(resource\)%20beta.messages.category%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_details%20%2B%20\(resource\)%20beta.messages.category)
explanation: string
Human-readable explanation of the refusal.
This text is not guaranteed to be stable. `null` when no explanation is available for the category.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_details%20%2B%20\(resource\)%20beta.messages.explanation)
fallback_credit_token: string
Opaque code that refunds the cache-miss cost when retrying this refused request on the fallback model. Pass it as `fallback_credit_token` on the retry request. Expires 5 minutes after the refusal.
The retry is sent either with the same request body (`system`, `messages`, `tools`, and other render-shaping fields), or with the same body plus one appended `assistant` message whose content is the partial text (with any trailing whitespace stripped from the final text block) and paired server-tool blocks from this refusal — which also authorizes that appended turn as an assistant-prefill continuation on models that otherwise disallow prefill. A token minted mid-server-tool-loop whose partial content was continuable may only be redeemed the second way — if a same-body retry is rejected with a 400 saying the token must be redeemed by continuing the partial response, retry the second way instead. Either way: same workspace, same platform; a mismatch is a 400. Resending a token for an already-warm prefix is permitted but yields no additional credit.
`null` when the refused model isn't eligible for a fallback credit.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_details%20%2B%20\(resource\)%20beta.messages.fallback_credit_token)
fallback_has_prefill_claim: boolean
Whether the accompanying `fallback_credit_token` may be redeemed with the appended-assistant retry form. Only set when `fallback_credit_token` is present.
`true`: retry by resending the same request body plus one appended `assistant` message whose content is this response's `content` with any trailing whitespace stripped from the final text block and unpaired `tool_use` blocks omitted (the same appended-turn shape described on `fallback_credit_token`), with the token attached. `false`: retry by resending the original request body unchanged, with the token attached — the appended-assistant form is not available for this refusal (no continuable partial content, or the request uses `output_format` or a `tool_choice` that forces tool use). One exception: when the request used `output_format` or a forced `tool_choice` and the refusal arrived after server tools (including MCP connector tools) had already executed, the token may not be redeemable by either retry form; if the exact-body retry is then rejected with a 400 saying the token must be redeemed by continuing the partial response, discard the token and retry without it.
Advisory: if an appended-assistant retry is rejected with a 400 despite `true`, fall back to resending the original request body with the token.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_details%20%2B%20\(resource\)%20beta.messages.fallback_has_prefill_claim)
recommended_model: string
The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_details%20%2B%20\(resource\)%20beta.messages.recommended_model)
type: "refusal"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_details%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.stop_details)
stop_reason: [BetaStopReason](https://platform.claude.com/docs/en/api/beta#beta_stop_reason)
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
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_reason%20%2B%20\(resource\)%20beta.messages%5B0%5D)
"max_tokens"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_reason%20%2B%20\(resource\)%20beta.messages%5B1%5D)
"stop_sequence"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_reason%20%2B%20\(resource\)%20beta.messages%5B2%5D)
"tool_use"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_reason%20%2B%20\(resource\)%20beta.messages%5B3%5D)
"pause_turn"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_reason%20%2B%20\(resource\)%20beta.messages%5B4%5D)
"compaction"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_reason%20%2B%20\(resource\)%20beta.messages%5B5%5D)
"refusal"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_reason%20%2B%20\(resource\)%20beta.messages%5B6%5D)
"model_context_window_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.stop_reason%20%2B%20\(resource\)%20beta.messages%5B7%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.stop_reason)
stop_sequence: string
Which custom stop sequence was generated, if any.
This value will be a non-null string if one of your custom stop sequences was generated.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.stop_sequence)
type: "message"
Object type.
For Messages, this is always `"message"`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.type)
usage: [BetaUsage](https://platform.claude.com/docs/en/api/beta#beta_usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 8 more } 
Billing and rate-limit usage.
Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.
Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.
For example, `output_tokens` will be non-zero, even for an empty string response from Claude.
Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.
cache_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
Breakdown of cached tokens by TTL
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.cache_creation%20%2B%20\(resource\)%20beta.messages.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.cache_creation%20%2B%20\(resource\)%20beta.messages.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.cache_creation)
cache_creation_input_tokens: number
The number of input tokens used to create the cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.cache_creation_input_tokens)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.cache_read_input_tokens)
inference_geo: string
The geographic region where inference was performed for this request.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.inference_geo)
input_tokens: number
The number of input tokens which were used.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.input_tokens)
iterations: [BetaIterationsUsage](https://platform.claude.com/docs/en/api/beta#beta_iterations_usage) { , , ,  } 
Per-iteration token usage breakdown.
Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:
  * Determine which iterations exceeded long context thresholds (>=200k tokens)
  * Calculate the true context window size from the last iteration
  * Understand token accumulation across server-side tool use loops

BetaMessageIterationUsage object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more } 
Token usage for a sampling iteration.
cache_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
Breakdown of cached tokens by TTL
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.cache_creation%20%2B%20\(resource\)%20beta.messages.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.cache_creation%20%2B%20\(resource\)%20beta.messages.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_creation)
cache_creation_input_tokens: number
The number of input tokens used to create the cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_creation_input_tokens)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_read_input_tokens)
input_tokens: number
The number of input tokens which were used.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.input_tokens)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.model)
output_tokens: number
The number of output tokens which were used.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.output_tokens)
type: "message"
Usage for a sampling iteration
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages)
BetaCompactionIterationUsage object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more } 
Token usage for a compaction iteration.
cache_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
Breakdown of cached tokens by TTL
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_compaction_iteration_usage.cache_creation%20%2B%20\(resource\)%20beta.messages.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_compaction_iteration_usage.cache_creation%20%2B%20\(resource\)%20beta.messages.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_creation)
cache_creation_input_tokens: number
The number of input tokens used to create the cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_creation_input_tokens)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_read_input_tokens)
input_tokens: number
The number of input tokens which were used.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.input_tokens)
output_tokens: number
The number of output tokens which were used.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.output_tokens)
type: "compaction"
Usage for a compaction iteration
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages)
BetaAdvisorMessageIterationUsage object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more } 
Token usage for an advisor sub-inference iteration.
cache_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
Breakdown of cached tokens by TTL
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.cache_creation%20%2B%20\(resource\)%20beta.messages.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.cache_creation%20%2B%20\(resource\)%20beta.messages.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_creation)
cache_creation_input_tokens: number
The number of input tokens used to create the cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_creation_input_tokens)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_read_input_tokens)
input_tokens: number
The number of input tokens which were used.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.input_tokens)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_advisor_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.model)
output_tokens: number
The number of output tokens which were used.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.output_tokens)
type: "advisor_message"
Usage for an advisor sub-inference iteration
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages)
BetaFallbackMessageIterationUsage object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more } 
Token usage for the fallback-model attempt of a server-side fallback request.
Produced in place of a `message` entry for whichever hop served the response. A declined hop produces the existing `message` entry. Whether a fallback model served the response is signalled by the presence of this entry in `usage.iterations`.
cache_creation: [BetaCacheCreation](https://platform.claude.com/docs/en/api/beta#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
Breakdown of cached tokens by TTL
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.cache_creation%20%2B%20\(resource\)%20beta.messages.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.cache_creation%20%2B%20\(resource\)%20beta.messages.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_creation)
cache_creation_input_tokens: number
The number of input tokens used to create the cache entry.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_creation_input_tokens)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.cache_read_input_tokens)
input_tokens: number
The number of input tokens which were used.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.input_tokens)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_fallback_message_iteration_usage.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.model)
output_tokens: number
The number of output tokens which were used.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.output_tokens)
type: "fallback_message"
Usage for the fallback-model attempt that served the response
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.iterations%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.iterations)
output_tokens: number
The number of output tokens which were used.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.output_tokens)
output_tokens_details: [BetaOutputTokensDetails](https://platform.claude.com/docs/en/api/beta#beta_output_tokens_details) { thinking_tokens } 
Breakdown of output tokens by category.
`output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you.
thinking_tokens: number
Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.
Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.output_tokens_details%20%2B%20\(resource\)%20beta.messages.thinking_tokens)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.output_tokens_details)
server_tool_use: [BetaServerToolUsage](https://platform.claude.com/docs/en/api/beta#beta_server_tool_usage) { web_fetch_requests, web_search_requests } 
The number of server tool requests.
web_fetch_requests: number
The number of web fetch tool requests.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.server_tool_use%20%2B%20\(resource\)%20beta.messages.web_fetch_requests)
web_search_requests: number
The number of web search tool requests.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_usage.server_tool_use%20%2B%20\(resource\)%20beta.messages.web_search_requests)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.server_tool_use)
service_tier: "standard" or "priority" or "batch"
If the request used the priority, standard, or batch tier.
"standard"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.service_tier%5B0%5D)
"priority"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.service_tier%5B1%5D)
"batch"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.service_tier%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.service_tier)
speed: "standard" or "fast"
The inference speed mode used for this request.
"standard"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message.usage%20%2B%20\(resource\)%20beta.messages.speed)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_succeeded_result.message%20%2B%20\(resource\)%20beta.messages.usage)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.result%20%2B%20\(resource\)%20beta.messages.batches.message)
type: "succeeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.result%20%2B%20\(resource\)%20beta.messages.batches.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.result%20%2B%20\(resource\)%20beta.messages.batches)
BetaMessageBatchErroredResult object { error, type } 
error: [BetaErrorResponse](https://platform.claude.com/docs/en/api/beta#beta_error_response) { error, request_id, type } 
error: [BetaError](https://platform.claude.com/docs/en/api/beta#beta_error)
BetaInvalidRequestError object { message, type } 
message: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.message)
type: "invalid_request_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta)
BetaAuthenticationError object { message, type } 
message: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.message)
type: "authentication_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta)
BetaBillingError object { message, type } 
message: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.message)
type: "billing_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta)
BetaPermissionError object { message, type } 
message: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.message)
type: "permission_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta)
BetaNotFoundError object { message, type } 
message: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.message)
type: "not_found_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta)
BetaRateLimitError object { message, type } 
message: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.message)
type: "rate_limit_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta)
BetaGatewayTimeoutError object { message, type } 
message: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.message)
type: "timeout_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta)
BetaAPIError object { message, type } 
message: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.message)
type: "api_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta)
BetaOverloadedError object { message, type } 
message: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.message)
type: "overloaded_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_error_response.error%20%2B%20\(resource\)%20beta)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_errored_result.error%20%2B%20\(resource\)%20beta.error)
request_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_errored_result.error%20%2B%20\(resource\)%20beta.request_id)
type: "error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_errored_result.error%20%2B%20\(resource\)%20beta.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.result%20%2B%20\(resource\)%20beta.messages.batches.error)
type: "errored"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.result%20%2B%20\(resource\)%20beta.messages.batches.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.result%20%2B%20\(resource\)%20beta.messages.batches)
BetaMessageBatchCanceledResult object { type } 
type: "canceled"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.result%20%2B%20\(resource\)%20beta.messages.batches.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.result%20%2B%20\(resource\)%20beta.messages.batches)
BetaMessageBatchExpiredResult object { type } 
type: "expired"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.result%20%2B%20\(resource\)%20beta.messages.batches.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.result%20%2B%20\(resource\)%20beta.messages.batches)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response.result)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/results#beta_message_batch_individual_response)
Retrieve Message Batch results
cURL

curl https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID/results \
    -H 'anthropic-beta: message-batches-2024-09-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
