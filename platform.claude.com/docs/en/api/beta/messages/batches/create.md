<!-- source: https://platform.claude.com/docs/en/api/beta/messages/batches/create -->

# Create a Message Batch
POST/v1/messages/batches
Send a batch of Message creation requests.
The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.
Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.betas)
#####  Body ParametersJSONExpand Collapse 
requests: array of object { custom_id, params } 
List of requests for prompt completion. Each is an individual request to create a Message.
custom_id: string
Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.
Must be unique for each request within the Message Batch.
maxLength64
minLength1
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.custom_id)
params: object { max_tokens, messages, model, 23 more } 
Messages API creation parameters for the individual request.
See the [Messages API reference](https://docs.claude.com/en/api/messages) for full documentation on available parameters.
max_tokens: number
The maximum number of tokens to generate before stopping.
Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.
Set to `0` to populate the [prompt cache](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.
Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.max_tokens)
messages: array of [BetaMessageParam](https://platform.claude.com/docs/en/api/beta#beta_message_param) { content, role } 
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
content: string or array of [BetaContentBlockParam](https://platform.claude.com/docs/en/api/beta#beta_content_block_param)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_param.content%5B0%5D)
array of [BetaContentBlockParam](https://platform.claude.com/docs/en/api/beta#beta_content_block_param)
BetaTextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control)
citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)
BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param)
BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param)
BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param)
BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param)
BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param)
BetaImageBlockParam object { source, type, cache_control } 
source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media_type, type }  or [BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url }  or [BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file_id, type } 
BetaBase64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source)
BetaURLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source)
BetaFileImageSource object { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param)
BetaRequestDocumentBlock object { source, type, cache_control, 3 more } 
source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type }  or [BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }  or [BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type }  or 2 more
BetaBase64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_pdf_source.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_pdf_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_pdf_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_pdf_source)
BetaPlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_plain_text_source.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_plain_text_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_plain_text_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_plain_text_source)
BetaContentBlockSource object { content, type } 
content: string or array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_content_block_source.content%5B0%5D)
BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)
BetaTextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control)
citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)
BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param)
BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param)
BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param)
BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param)
BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param)
BetaImageBlockParam object { source, type, cache_control } 
source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media_type, type }  or [BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url }  or [BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file_id, type } 
BetaBase64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source)
BetaURLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source)
BetaFileImageSource object { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_content_block_source.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_content_block_source.content)
type: "content"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_content_block_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_content_block_source)
BetaURLPDFSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_pdf_source.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_pdf_source.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_pdf_source)
BetaFileDocumentSource object { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control)
citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.citations%20%2B%20\(resource\)%20beta.messages.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.citations)
context: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.context)
title: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block)
BetaSearchResultBlockParam object { content, source, title, 3 more } 
content: array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control)
citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)
BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param)
BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param)
BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param)
BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param)
BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.content)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.source)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.cache_control)
citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.citations%20%2B%20\(resource\)%20beta.messages.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param)
BetaThinkingBlockParam object { signature, thinking, type } 
signature: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_block_param.signature)
thinking: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_block_param.thinking)
type: "thinking"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_block_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_block_param)
BetaRedactedThinkingBlockParam object { data, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_redacted_thinking_block_param.data)
type: "redacted_thinking"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_redacted_thinking_block_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_redacted_thinking_block_param)
BetaToolUseBlockParam object { id, input, name, 3 more } 
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_use_block_param.id)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_use_block_param.input)
name: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_use_block_param.name)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_use_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_use_block_param.cache_control)
caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }  or [BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
BetaDirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_direct_caller.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_direct_caller)
BetaServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller)
BetaServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_use_block_param.caller)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_use_block_param)
BetaToolResultBlockParam object { tool_use_id, type, cache_control, 2 more } 
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param.tool_use_id)
type: "tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param.cache_control)
content: optional string or array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }  or [BetaImageBlockParam](https://platform.claude.com/docs/en/api/beta#beta_image_block_param) { source, type, cache_control }  or [BetaSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more }  or 2 more
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param.content%5B0%5D)
array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations }  or [BetaImageBlockParam](https://platform.claude.com/docs/en/api/beta#beta_image_block_param) { source, type, cache_control }  or [BetaSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_search_result_block_param) { content, source, title, 3 more }  or 2 more
BetaTextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control)
citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)
BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param)
BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param)
BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param)
BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param)
BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param)
BetaImageBlockParam object { source, type, cache_control } 
source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media_type, type }  or [BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url }  or [BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file_id, type } 
BetaBase64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source)
BetaURLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source)
BetaFileImageSource object { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param)
BetaSearchResultBlockParam object { content, source, title, 3 more } 
content: array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control)
citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)
BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param)
BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param)
BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param)
BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param)
BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.content)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.source)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.cache_control)
citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.citations%20%2B%20\(resource\)%20beta.messages.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_search_result_block_param)
BetaRequestDocumentBlock object { source, type, cache_control, 3 more } 
source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type }  or [BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }  or [BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type }  or 2 more
BetaBase64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_pdf_source.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_pdf_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_pdf_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_pdf_source)
BetaPlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_plain_text_source.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_plain_text_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_plain_text_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_plain_text_source)
BetaContentBlockSource object { content, type } 
content: string or array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_content_block_source.content%5B0%5D)
BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)
BetaTextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control)
citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)
BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param)
BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param)
BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param)
BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param)
BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param)
BetaImageBlockParam object { source, type, cache_control } 
source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media_type, type }  or [BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url }  or [BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file_id, type } 
BetaBase64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_base64_image_source)
BetaURLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_image_source)
BetaFileImageSource object { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_content_block_source.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_content_block_source.content)
type: "content"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_content_block_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_content_block_source)
BetaURLPDFSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_pdf_source.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_pdf_source.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_url_pdf_source)
BetaFileDocumentSource object { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control)
citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.citations%20%2B%20\(resource\)%20beta.messages.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.citations)
context: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.context)
title: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block)
BetaToolReferenceBlockParam object { tool_name, type, cache_control } 
Tool reference block that can be included in tool_result content.
tool_name: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param.content)
is_error: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param.is_error)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_result_block_param)
BetaServerToolUseBlockParam object { id, input, name, 3 more } 
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.id)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.input)
name: "advisor" or "web_search" or "web_fetch" or 5 more
"advisor"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.name%5B0%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.name%5B1%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.name%5B2%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.name%5B3%5D)
"bash_code_execution"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.name%5B4%5D)
"text_editor_code_execution"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.name%5B5%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.name%5B6%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.name%5B7%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.name)
type: "server_tool_use"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.cache_control)
caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }  or [BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
BetaDirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_direct_caller.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_direct_caller)
BetaServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller)
BetaServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param.caller)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_use_block_param)
BetaWebSearchToolResultBlockParam object { content, tool_use_id, type, 2 more } 
content: [BetaWebSearchToolResultBlockParamContent](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_block_param_content)
ResultBlock = array of [BetaWebSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_search_result_block_param) { encrypted_content, title, type, 2 more } 
encrypted_content: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.encrypted_content)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.title)
type: "web_search_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.url)
page_age: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.page_age)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages%5B0%5D)
BetaWebSearchToolRequestError object { error_code, type } 
error_code: [BetaWebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_request_error.error_code%20%2B%20\(resource\)%20beta.messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_request_error.error_code%20%2B%20\(resource\)%20beta.messages%5B1%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_request_error.error_code%20%2B%20\(resource\)%20beta.messages%5B2%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_request_error.error_code%20%2B%20\(resource\)%20beta.messages%5B3%5D)
"query_too_long"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_request_error.error_code%20%2B%20\(resource\)%20beta.messages%5B4%5D)
"request_too_large"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_request_error.error_code%20%2B%20\(resource\)%20beta.messages%5B5%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.error_code)
type: "web_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.tool_use_id)
type: "web_search_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.cache_control)
caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }  or [BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
BetaDirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_direct_caller.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_direct_caller)
BetaServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller)
BetaServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param.caller)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_result_block_param)
BetaWebFetchToolResultBlockParam object { content, tool_use_id, type, 2 more } 
content: [BetaWebFetchToolResultErrorBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_block_param) { error_code, type }  or [BetaWebFetchBlockParam](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_block_param) { content, type, url, retrieved_at } 
BetaWebFetchToolResultErrorBlockParam object { error_code, type } 
error_code: [BetaWebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_web_fetch_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20beta.messages%5B0%5D)
"url_too_long"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20beta.messages%5B1%5D)
"url_not_allowed"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20beta.messages%5B2%5D)
"url_not_in_prior_context"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20beta.messages%5B3%5D)
"url_not_accessible"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20beta.messages%5B4%5D)
"unsupported_content_type"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20beta.messages%5B5%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20beta.messages%5B6%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20beta.messages%5B7%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20beta.messages%5B8%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param.error_code)
type: "web_fetch_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_error_block_param)
BetaWebFetchBlockParam object { content, type, url, retrieved_at } 
content: [BetaRequestDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_request_document_block) { source, type, cache_control, 3 more } 
source: [BetaBase64PDFSource](https://platform.claude.com/docs/en/api/beta#beta_base64_pdf_source) { data, media_type, type }  or [BetaPlainTextSource](https://platform.claude.com/docs/en/api/beta#beta_plain_text_source) { data, media_type, type }  or [BetaContentBlockSource](https://platform.claude.com/docs/en/api/beta#beta_content_block_source) { content, type }  or 2 more
BetaBase64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaPlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaContentBlockSource object { content, type } 
content: string or array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.content%5B0%5D)
BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](https://platform.claude.com/docs/en/api/beta#beta_content_block_source_content)
BetaTextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.cache_control)
citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)
BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaImageBlockParam object { source, type, cache_control } 
source: [BetaBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_base64_image_source) { data, media_type, type }  or [BetaURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_url_image_source) { type, url }  or [BetaFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_file_image_source) { file_id, type } 
BetaBase64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaURLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaFileImageSource object { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_image_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.content)
type: "content"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaURLPDFSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaFileDocumentSource object { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.cache_control)
citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_document_block.citations%20%2B%20\(resource\)%20beta.messages.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.citations)
context: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.context)
title: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content%20%2B%20\(resource\)%20beta.messages.title)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.content)
type: "web_fetch_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.type)
url: string
Fetched content URL
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.url)
retrieved_at: optional string
ISO 8601 timestamp when the content was retrieved
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param.retrieved_at)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_block_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_block_param.tool_use_id)
type: "web_fetch_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_block_param.cache_control)
caller: optional [BetaDirectCaller](https://platform.claude.com/docs/en/api/beta#beta_direct_caller) { type }  or [BetaServerToolCaller](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller) { tool_id, type }  or [BetaServerToolCaller20260120](https://platform.claude.com/docs/en/api/beta#beta_server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
BetaDirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_direct_caller.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_direct_caller)
BetaServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller)
BetaServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_block_param.caller)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_result_block_param)
BetaAdvisorToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [BetaAdvisorToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_advisor_tool_result_error_param) { error_code, type }  or [BetaAdvisorResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_advisor_result_block_param) { text, type, stop_reason }  or [BetaAdvisorRedactedResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_advisor_redacted_result_block_param) { encrypted_content, type, stop_reason } 
BetaAdvisorToolResultErrorParam object { error_code, type } 
error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 4 more
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_error_param.error_code%5B0%5D)
"prompt_too_long"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_error_param.error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_error_param.error_code%5B2%5D)
"overloaded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_error_param.error_code%5B3%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_error_param.error_code%5B4%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_error_param.error_code%5B5%5D)
"model_not_found"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_error_param.error_code%5B6%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_error_param.error_code)
type: "advisor_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_error_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_error_param)
BetaAdvisorResultBlockParam object { text, type, stop_reason } 
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_result_block_param.text)
type: "advisor_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_result_block_param.type)
stop_reason: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_result_block_param.stop_reason)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_result_block_param)
BetaAdvisorRedactedResultBlockParam object { encrypted_content, type, stop_reason } 
encrypted_content: string
Opaque blob produced by a prior response; must be round-tripped verbatim.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_redacted_result_block_param.encrypted_content)
type: "advisor_redacted_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_redacted_result_block_param.type)
stop_reason: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_redacted_result_block_param.stop_reason)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_redacted_result_block_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_block_param.tool_use_id)
type: "advisor_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_result_block_param)
BetaCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [BetaCodeExecutionToolResultBlockParamContent](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)
Code execution result with encrypted stdout for PFC + web_search results.
BetaCodeExecutionToolResultErrorParam object { error_code, type } 
error_code: [BetaCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/beta#beta_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20beta.messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20beta.messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20beta.messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20beta.messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.error_code)
type: "code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaCodeExecutionResultBlockParam object { content, return_code, stderr, 2 more } 
content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.content)
return_code: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.stdout)
type: "code_execution_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages)
BetaEncryptedCodeExecutionResultBlockParam object { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
content: array of [BetaCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_code_execution_output_block_param) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.content)
encrypted_stdout: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.encrypted_stdout)
return_code: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.stderr)
type: "encrypted_code_execution_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.tool_use_id)
type: "code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_result_block_param)
BetaBashCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [BetaBashCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_tool_result_error_param) { error_code, type }  or [BetaBashCodeExecutionResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_result_block_param) { content, return_code, stderr, 2 more } 
BetaBashCodeExecutionToolResultErrorParam object { error_code, type } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_error_param.error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_error_param.error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_error_param.error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_error_param.error_code%5B3%5D)
"output_file_too_large"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_error_param.error_code%5B4%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_error_param.error_code)
type: "bash_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_error_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_error_param)
BetaBashCodeExecutionResultBlockParam object { content, return_code, stderr, 2 more } 
content: array of [BetaBashCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/beta#beta_bash_code_execution_output_block_param) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_output_block_param.file_id)
type: "bash_code_execution_output"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_output_block_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_result_block_param.content)
return_code: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_result_block_param.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_result_block_param.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_result_block_param.stdout)
type: "bash_code_execution_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_result_block_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_result_block_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_block_param.tool_use_id)
type: "bash_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_bash_code_execution_tool_result_block_param)
BetaTextEditorCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [BetaTextEditorCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_tool_result_error_param) { error_code, type, error_message }  or [BetaTextEditorCodeExecutionViewResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_create_result_block_param) { is_file_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more } 
BetaTextEditorCodeExecutionToolResultErrorParam object { error_code, type, error_message } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_error_param.error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_error_param.error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_error_param.error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_error_param.error_code%5B3%5D)
"file_not_found"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_error_param.error_code%5B4%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_error_param.error_code)
type: "text_editor_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_error_param.type)
error_message: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_error_param.error_message)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_error_param)
BetaTextEditorCodeExecutionViewResultBlockParam object { content, file_type, type, 3 more } 
content: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_view_result_block_param.content)
file_type: "text" or "image" or "pdf"
"text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_view_result_block_param.file_type%5B0%5D)
"image"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_view_result_block_param.file_type%5B1%5D)
"pdf"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_view_result_block_param.file_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_view_result_block_param.file_type)
type: "text_editor_code_execution_view_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_view_result_block_param.type)
num_lines: optional number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_view_result_block_param.num_lines)
start_line: optional number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_view_result_block_param.start_line)
total_lines: optional number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_view_result_block_param.total_lines)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_view_result_block_param)
BetaTextEditorCodeExecutionCreateResultBlockParam object { is_file_update, type } 
is_file_update: boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_create_result_block_param.is_file_update)
type: "text_editor_code_execution_create_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_create_result_block_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_create_result_block_param)
BetaTextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new_lines, 3 more } 
type: "text_editor_code_execution_str_replace_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_str_replace_result_block_param.type)
lines: optional array of string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_str_replace_result_block_param.lines)
new_lines: optional number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_str_replace_result_block_param.new_lines)
new_start: optional number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_str_replace_result_block_param.new_start)
old_lines: optional number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_str_replace_result_block_param.old_lines)
old_start: optional number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_str_replace_result_block_param.old_start)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_str_replace_result_block_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_block_param.tool_use_id)
type: "text_editor_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_editor_code_execution_tool_result_block_param)
BetaToolSearchToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [BetaToolSearchToolResultErrorParam](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_result_error_param) { error_code, type, error_message }  or [BetaToolSearchToolSearchResultBlockParam](https://platform.claude.com/docs/en/api/beta#beta_tool_search_tool_search_result_block_param) { tool_references, type } 
BetaToolSearchToolResultErrorParam object { error_code, type, error_message } 
error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_error_param.error_code%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_error_param.error_code%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_error_param.error_code%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_error_param.error_code%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_error_param.error_code)
type: "tool_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_error_param.type)
error_message: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_error_param.error_message)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_error_param)
BetaToolSearchToolSearchResultBlockParam object { tool_references, type } 
tool_references: array of [BetaToolReferenceBlockParam](https://platform.claude.com/docs/en/api/beta#beta_tool_reference_block_param) { tool_name, type, cache_control } 
tool_name: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_reference_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_search_result_block_param.tool_references)
type: "tool_search_tool_search_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_search_result_block_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_search_result_block_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_block_param.tool_use_id)
type: "tool_search_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_result_block_param)
BetaMCPToolUseBlockParam object { id, input, name, 3 more } 
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_use_block_param.id)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_use_block_param.input)
name: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_use_block_param.name)
server_name: string
The name of the MCP server
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_use_block_param.server_name)
type: "mcp_tool_use"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_use_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_use_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_use_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_use_block_param)
BetaRequestMCPToolResultBlockParam object { tool_use_id, type, cache_control, 2 more } 
tool_use_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param.tool_use_id)
type: "mcp_tool_result"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param.cache_control)
content: optional string or array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } 
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param.content%5B0%5D)
BetaMCPToolResultBlockParamContent = array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control)
citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)
BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param)
BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param)
BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param)
BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param)
BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param.content)
is_error: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param.is_error)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_tool_result_block_param)
BetaContainerUploadBlockParam object { file_id, type, cache_control } 
A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.
file_id: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_container_upload_block_param.file_id)
type: "container_upload"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_container_upload_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_container_upload_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_container_upload_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_container_upload_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_container_upload_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_container_upload_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_container_upload_block_param)
BetaCompactionBlockParam object { type, cache_control, content, encrypted_content } 
A compaction block containing summary of previous context.
Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.
When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.
type: "compaction"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_compaction_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_compaction_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_compaction_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_compaction_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_compaction_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_compaction_block_param.cache_control)
content: optional string
Summary of previously compacted content, or null if compaction failed
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_compaction_block_param.content)
encrypted_content: optional string
Opaque metadata from prior compaction, to be round-tripped verbatim
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_compaction_block_param.encrypted_content)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_compaction_block_param)
BetaMidConversationSystemBlockParam object { content, type, cache_control } 
System instructions that appear mid-conversation.
Use this block to provide or update system-level instructions at a specific point in the conversation, rather than only via the top-level `system` parameter.
content: array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } 
System instruction text blocks.
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control)
citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)
BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param)
BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param)
BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param)
BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param)
BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mid_conversation_system_block_param.content)
type: "mid_conv_system"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mid_conversation_system_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mid_conversation_system_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mid_conversation_system_block_param)
BetaFallbackBlockParam object { from, to, type, trigger } 
A `fallback` block echoed back from a prior response.
Accepted in `messages[].content` and not rendered into the prompt; not validated against the request's `fallbacks` chain or top-level `model`.
Echo the assistant turn back verbatim, including this block in its original position. The block marks the boundary between content produced before and after a fallback hop, and the server relies on that boundary to validate the turn: when thinking runs flank the boundary, omitting the block merges them into one span the server cannot validate (the request is rejected), and moving it into the middle of a single run is likewise rejected; between non-thinking blocks the block's placement has no validation effect.
from: [BetaFallbackInfoParam](https://platform.claude.com/docs/en/api/beta#beta_fallback_info_param) { model } 
Identifies one hop of a fallback transition.
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_block_param.from%20%2B%20\(resource\)%20beta.messages.model)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_block_param.from)
to: [BetaFallbackInfoParam](https://platform.claude.com/docs/en/api/beta#beta_fallback_info_param) { model } 
Identifies one hop of a fallback transition.
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_info_param.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_block_param.to%20%2B%20\(resource\)%20beta.messages.model)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_block_param.to)
type: "fallback"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_block_param.type)
trigger: optional unknown
The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_block_param.trigger)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_block_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_param.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_param.content)
role: "user" or "assistant" or "system"
"user"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_param.role%5B0%5D)
"assistant"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_param.role%5B1%5D)
"system"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_param.role%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_param.role)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.messages)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.model)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.cache_control)
container: optional [BetaContainerParams](https://platform.claude.com/docs/en/api/beta#beta_container_params) { id, skills }  or string
Container identifier for reuse across requests.
BetaContainerParams object { id, skills } 
Container parameters with skills to be loaded.
id: optional string
Container id
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_container_params.id)
skills: optional array of [BetaSkillParams](https://platform.claude.com/docs/en/api/beta#beta_skill_params) { skill_id, type, version } 
List of skills to load in the container
skill_id: string
Skill ID
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_skill_params.skill_id)
type: "anthropic" or "custom"
Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)
"anthropic"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_skill_params.type%5B0%5D)
"custom"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_skill_params.type%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_skill_params.type)
version: optional string
Skill version or 'latest' for most recent version
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_skill_params.version)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_container_params.skills)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_container_params)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.container%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.container)
context_management: optional [BetaContextManagementConfig](https://platform.claude.com/docs/en/api/beta#beta_context_management_config) { edits } 
Context management configuration.
This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.
edits: optional array of [BetaClearToolUses20250919Edit](https://platform.claude.com/docs/en/api/beta#beta_clear_tool_uses_20250919_edit) { type, clear_at_least, clear_tool_inputs, 3 more }  or [BetaClearThinking20251015Edit](https://platform.claude.com/docs/en/api/beta#beta_clear_thinking_20251015_edit) { type, keep }  or [BetaCompact20260112Edit](https://platform.claude.com/docs/en/api/beta#beta_compact_20260112_edit) { type, instructions, pause_after_compaction, trigger } 
List of context management edits to apply
BetaClearToolUses20250919Edit object { type, clear_at_least, clear_tool_inputs, 3 more } 
type: "clear_tool_uses_20250919"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.type)
clear_at_least: optional [BetaInputTokensClearAtLeast](https://platform.claude.com/docs/en/api/beta#beta_input_tokens_clear_at_least) { type, value } 
Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.
type: "input_tokens"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_clear_tool_uses_20250919_edit.clear_at_least%20%2B%20\(resource\)%20beta.messages.type)
value: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_clear_tool_uses_20250919_edit.clear_at_least%20%2B%20\(resource\)%20beta.messages.value)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.clear_at_least)
clear_tool_inputs: optional boolean or array of string
Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)
boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.clear_tool_inputs%5B0%5D)
array of string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.clear_tool_inputs%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.clear_tool_inputs)
exclude_tools: optional array of string
Tool names whose uses are preserved from clearing
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.exclude_tools)
keep: optional [BetaToolUsesKeep](https://platform.claude.com/docs/en/api/beta#beta_tool_uses_keep) { type, value } 
Number of tool uses to retain in the conversation
type: "tool_uses"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_clear_tool_uses_20250919_edit.keep%20%2B%20\(resource\)%20beta.messages.type)
value: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_clear_tool_uses_20250919_edit.keep%20%2B%20\(resource\)%20beta.messages.value)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.keep)
trigger: optional [BetaInputTokensTrigger](https://platform.claude.com/docs/en/api/beta#beta_input_tokens_trigger) { type, value }  or [BetaToolUsesTrigger](https://platform.claude.com/docs/en/api/beta#beta_tool_uses_trigger) { type, value } 
Condition that triggers the context management strategy
BetaInputTokensTrigger object { type, value } 
type: "input_tokens"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.type)
value: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.value)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages)
BetaToolUsesTrigger object { type, value } 
type: "tool_uses"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.type)
value: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.value)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.trigger)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages)
BetaClearThinking20251015Edit object { type, keep } 
type: "clear_thinking_20251015"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.type)
keep: optional [BetaThinkingTurns](https://platform.claude.com/docs/en/api/beta#beta_thinking_turns) { type, value }  or [BetaAllThinkingTurns](https://platform.claude.com/docs/en/api/beta#beta_all_thinking_turns) { type }  or "all"
Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.
BetaThinkingTurns object { type, value } 
type: "thinking_turns"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.type)
value: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.value)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages)
BetaAllThinkingTurns object { type } 
type: "all"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages)
"all"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.keep%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.keep)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages)
BetaCompact20260112Edit object { type, instructions, pause_after_compaction, trigger } 
Automatically compact older context when reaching the configured trigger threshold.
type: "compact_20260112"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.type)
instructions: optional string
Additional instructions for summarization.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.instructions)
pause_after_compaction: optional boolean
Whether to pause after compaction and return the compaction block to the user.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.pause_after_compaction)
trigger: optional [BetaInputTokensTrigger](https://platform.claude.com/docs/en/api/beta#beta_input_tokens_trigger) { type, value } 
When to trigger compaction. Defaults to 150000 input tokens.
type: "input_tokens"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_compact_20260112_edit.trigger%20%2B%20\(resource\)%20beta.messages.type)
value: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_compact_20260112_edit.trigger%20%2B%20\(resource\)%20beta.messages.value)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.trigger)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management%20%2B%20\(resource\)%20beta.messages.edits)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.context_management)
diagnostics: optional [BetaDiagnosticsParam](https://platform.claude.com/docs/en/api/beta#beta_diagnostics_param) { previous_message_id } 
Request-level diagnostics. Currently carries the previous response id for prompt-cache divergence reporting.
previous_message_id: optional string
The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.diagnostics%20%2B%20\(resource\)%20beta.messages.previous_message_id)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.diagnostics)
fallback_credit_token: optional string
The `fallback_credit_token` from a prior refusal's `stop_details`.
When a preceding request was refused and returned a `fallback_credit_token`, pass that code here on the retry to have the retry's cache-creation tokens for the prefix that was warm on the refused model billed at the cache-read rate. Must be redeemed by the same organization and workspace, with the same request body (optionally extended by one appended `assistant` message whose content is the partial text — with any trailing whitespace stripped from the final text block — and paired server-tool blocks streamed before the refusal; the appended-assistant form is not available for requests with `output_format` set or forced `tool_choice`), on an eligible fallback model, on the same platform, and within 5 minutes of the refusal; a mismatch is a 400. A token minted mid-server-tool-loop whose partial content was continuable may only be redeemed with the appended-assistant form — if an exact-body retry is rejected with a 400 saying the token must be redeemed by continuing the partial response, retry with the appended-assistant form instead.
When the appended-assistant form is used on a model that otherwise disallows assistant-turn prefill, this token also authorizes that one prefill.
maxLength2048
minLength1
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.fallback_credit_token)
fallbacks: optional array of [BetaFallbackParam](https://platform.claude.com/docs/en/api/beta#beta_fallback_param) { model, max_tokens, output_config, 2 more } 
Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on.
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.model)
max_tokens: optional number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.max_tokens)
output_config: optional [BetaOutputConfig](https://platform.claude.com/docs/en/api/beta#beta_output_config) { effort, format, task_budget } 
effort: optional "low" or "medium" or "high" or 2 more
All possible effort levels.
"low"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.output_config%20%2B%20\(resource\)%20beta.messages.effort%5B0%5D)
"medium"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.output_config%20%2B%20\(resource\)%20beta.messages.effort%5B1%5D)
"high"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.output_config%20%2B%20\(resource\)%20beta.messages.effort%5B2%5D)
"xhigh"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.output_config%20%2B%20\(resource\)%20beta.messages.effort%5B3%5D)
"max"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.output_config%20%2B%20\(resource\)%20beta.messages.effort%5B4%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.output_config%20%2B%20\(resource\)%20beta.messages.effort)
format: optional [BetaJSONOutputFormat](https://platform.claude.com/docs/en/api/beta#beta_json_output_format) { schema, type } 
A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
schema: map[unknown]
The JSON schema of the format
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_output_config.format%20%2B%20\(resource\)%20beta.messages.schema)
type: "json_schema"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_output_config.format%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.output_config%20%2B%20\(resource\)%20beta.messages.format)
task_budget: optional [BetaTokenTaskBudget](https://platform.claude.com/docs/en/api/beta#beta_token_task_budget) { total, type, remaining } 
User-configurable total token budget across contexts.
total: number
Total token budget across all contexts in the session.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_output_config.task_budget%20%2B%20\(resource\)%20beta.messages.total)
type: "tokens"
The budget type. Currently only 'tokens' is supported.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_output_config.task_budget%20%2B%20\(resource\)%20beta.messages.type)
remaining: optional number
Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_output_config.task_budget%20%2B%20\(resource\)%20beta.messages.remaining)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.output_config%20%2B%20\(resource\)%20beta.messages.task_budget)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.output_config)
speed: optional "standard" or "fast"
"standard"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.speed)
thinking: optional [BetaThinkingConfigEnabled](https://platform.claude.com/docs/en/api/beta#beta_thinking_config_enabled) { budget_tokens, type, display }  or [BetaThinkingConfigDisabled](https://platform.claude.com/docs/en/api/beta#beta_thinking_config_disabled) { type }  or [BetaThinkingConfigAdaptive](https://platform.claude.com/docs/en/api/beta#beta_thinking_config_adaptive) { type, display } 
BetaThinkingConfigEnabled object { budget_tokens, type, display } 
budget_tokens: number
Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.
Must be ≥1024 and less than `max_tokens`.
See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.
minimum1024
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_enabled.budget_tokens)
type: "enabled"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_enabled.type)
display: optional "summarized" or "omitted"
Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.
"summarized"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_enabled.display%5B0%5D)
"omitted"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_enabled.display%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_enabled.display)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_enabled)
BetaThinkingConfigDisabled object { type } 
type: "disabled"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_disabled.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_disabled)
BetaThinkingConfigAdaptive object { type, display } 
type: "adaptive"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_adaptive.type)
display: optional "summarized" or "omitted"
Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.
"summarized"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_adaptive.display%5B0%5D)
"omitted"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_adaptive.display%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_adaptive.display)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_thinking_config_adaptive)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_fallback_param.thinking)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.fallbacks)
inference_geo: optional string
Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.inference_geo)
mcp_servers: optional array of [BetaRequestMCPServerURLDefinition](https://platform.claude.com/docs/en/api/beta#beta_request_mcp_server_url_definition) { name, type, url, 2 more } 
MCP servers to be utilized in this request
name: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_server_url_definition.name)
type: "url"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_server_url_definition.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_server_url_definition.url)
authorization_token: optional string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_server_url_definition.authorization_token)
tool_configuration: optional [BetaRequestMCPServerToolConfiguration](https://platform.claude.com/docs/en/api/beta#beta_request_mcp_server_tool_configuration) { allowed_tools, enabled } 
allowed_tools: optional array of string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_server_url_definition.tool_configuration%20%2B%20\(resource\)%20beta.messages.allowed_tools)
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_server_url_definition.tool_configuration%20%2B%20\(resource\)%20beta.messages.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_request_mcp_server_url_definition.tool_configuration)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.mcp_servers)
metadata: optional [BetaMetadata](https://platform.claude.com/docs/en/api/beta#beta_metadata) { user_id } 
An object describing metadata about the request.
user_id: optional string
An external identifier for the user who is associated with the request.
This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.
maxLength512
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.metadata%20%2B%20\(resource\)%20beta.messages.user_id)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.metadata)
output_config: optional [BetaOutputConfig](https://platform.claude.com/docs/en/api/beta#beta_output_config) { effort, format, task_budget } 
Configuration options for the model's output, such as the output format.
effort: optional "low" or "medium" or "high" or 2 more
All possible effort levels.
"low"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_config%20%2B%20\(resource\)%20beta.messages.effort%5B0%5D)
"medium"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_config%20%2B%20\(resource\)%20beta.messages.effort%5B1%5D)
"high"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_config%20%2B%20\(resource\)%20beta.messages.effort%5B2%5D)
"xhigh"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_config%20%2B%20\(resource\)%20beta.messages.effort%5B3%5D)
"max"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_config%20%2B%20\(resource\)%20beta.messages.effort%5B4%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_config%20%2B%20\(resource\)%20beta.messages.effort)
format: optional [BetaJSONOutputFormat](https://platform.claude.com/docs/en/api/beta#beta_json_output_format) { schema, type } 
A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
schema: map[unknown]
The JSON schema of the format
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_output_config.format%20%2B%20\(resource\)%20beta.messages.schema)
type: "json_schema"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_output_config.format%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_config%20%2B%20\(resource\)%20beta.messages.format)
task_budget: optional [BetaTokenTaskBudget](https://platform.claude.com/docs/en/api/beta#beta_token_task_budget) { total, type, remaining } 
User-configurable total token budget across contexts.
total: number
Total token budget across all contexts in the session.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_output_config.task_budget%20%2B%20\(resource\)%20beta.messages.total)
type: "tokens"
The budget type. Currently only 'tokens' is supported.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_output_config.task_budget%20%2B%20\(resource\)%20beta.messages.type)
remaining: optional number
Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_output_config.task_budget%20%2B%20\(resource\)%20beta.messages.remaining)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_config%20%2B%20\(resource\)%20beta.messages.task_budget)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_config)
Deprecatedoutput_format: optional [BetaJSONOutputFormat](https://platform.claude.com/docs/en/api/beta#beta_json_output_format) { schema, type } 
Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
A schema to specify Claude's output format in responses. This parameter will be removed in a future release.
schema: map[unknown]
The JSON schema of the format
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_format%20%2B%20\(resource\)%20beta.messages.schema)
type: "json_schema"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_format%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.output_format)
service_tier: optional "auto" or "standard_only"
Determines whether to use priority capacity (if available) or standard capacity for this request.
Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.
"auto"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.service_tier%5B0%5D)
"standard_only"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.service_tier%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.service_tier)
speed: optional "standard" or "fast"
The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.
"standard"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.speed)
stop_sequences: optional array of string
Custom text sequences that will cause the model to stop generating.
Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.
If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.stop_sequences)
stream: optional boolean
Whether to incrementally stream the response using server-sent events.
See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.stream)
system: optional string or array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } 
System prompt.
A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.system%5B0%5D)
array of [BetaTextBlockParam](https://platform.claude.com/docs/en/api/beta#beta_text_block_param) { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.cache_control)
citations: optional array of [BetaTextCitationParam](https://platform.claude.com/docs/en/api/beta#beta_text_citation_param)
BetaCitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_char_location_param)
BetaCitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_page_location_param)
BetaCitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_content_block_location_param)
BetaCitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_web_search_result_location_param)
BetaCitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_text_block_param.citations)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.system%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.system)
Deprecatedtemperature: optional number
Amount of randomness injected into the response.
Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.
Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.
Note that even with `temperature` of `0.0`, the results will not be fully deterministic.
maximum1
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.temperature)
thinking: optional [BetaThinkingConfigParam](https://platform.claude.com/docs/en/api/beta#beta_thinking_config_param)
Configuration for enabling Claude's extended thinking.
When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.
See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.
BetaThinkingConfigEnabled object { budget_tokens, type, display } 
budget_tokens: number
Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.
Must be ≥1024 and less than `max_tokens`.
See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.
minimum1024
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages.budget_tokens)
type: "enabled"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages.type)
display: optional "summarized" or "omitted"
Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.
"summarized"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages.display%5B0%5D)
"omitted"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages.display%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages.display)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages)
BetaThinkingConfigDisabled object { type } 
type: "disabled"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages)
BetaThinkingConfigAdaptive object { type, display } 
type: "adaptive"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages.type)
display: optional "summarized" or "omitted"
Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.
"summarized"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages.display%5B0%5D)
"omitted"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages.display%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages.display)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.thinking)
tool_choice: optional [BetaToolChoice](https://platform.claude.com/docs/en/api/beta#beta_tool_choice)
How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.
BetaToolChoiceAuto object { type, disable_parallel_tool_use } 
The model will automatically decide whether to use tools.
type: "auto"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages.type)
disable_parallel_tool_use: optional boolean
Whether to disable parallel tool use.
Defaults to `false`. If set to `true`, the model will output at most one tool use.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages.disable_parallel_tool_use)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages)
BetaToolChoiceAny object { type, disable_parallel_tool_use } 
The model will use any available tools.
type: "any"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages.type)
disable_parallel_tool_use: optional boolean
Whether to disable parallel tool use.
Defaults to `false`. If set to `true`, the model will output exactly one tool use.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages.disable_parallel_tool_use)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages)
BetaToolChoiceTool object { name, type, disable_parallel_tool_use } 
The model will use the specified tool with `tool_choice.name`.
name: string
The name of the tool to use.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages.name)
type: "tool"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages.type)
disable_parallel_tool_use: optional boolean
Whether to disable parallel tool use.
Defaults to `false`. If set to `true`, the model will output exactly one tool use.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages.disable_parallel_tool_use)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages)
BetaToolChoiceNone object { type } 
The model will not be allowed to use tools.
type: "none"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice%20%2B%20\(resource\)%20beta.messages)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tool_choice)
tools: optional array of [BetaToolUnion](https://platform.claude.com/docs/en/api/beta#beta_tool_union)
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
BetaTool object { input_schema, name, allowed_callers, 7 more } 
input_schema: object { type, properties, required } 
[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.
This defines the shape of the `input` that your tool accepts and that the model will produce.
type: "object"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.input_schema.type)
properties: optional map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.input_schema.properties)
required: optional array of string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.input_schema.required)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.input_schema)
name: string
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
maxLength128
minLength1
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.name)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.defer_loading)
description: optional string
Description of what this tool does.
Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.description)
eager_input_streaming: optional boolean
Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.eager_input_streaming)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.strict)
type: optional "custom"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool)
BetaToolBash20241022 object { name, type, allowed_callers, 4 more } 
name: "bash"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.name)
type: "bash_20241022"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20241022)
BetaToolBash20250124 object { name, type, allowed_callers, 4 more } 
name: "bash"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.name)
type: "bash_20250124"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_bash_20250124)
BetaCodeExecutionTool20250522 object { name, type, allowed_callers, 3 more } 
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.name)
type: "code_execution_20250522"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250522)
BetaCodeExecutionTool20250825 object { name, type, allowed_callers, 3 more } 
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.name)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20250825)
BetaCodeExecutionTool20260120 object { name, type, allowed_callers, 3 more } 
Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.name)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260120)
BetaCodeExecutionTool20260521 object { name, type, allowed_callers, 3 more } 
Code execution tool with REPL state persistence.
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.name)
type: "code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_code_execution_tool_20260521)
BetaToolComputerUse20241022 object { display_height_px, display_width_px, name, 7 more } 
display_height_px: number
The height of the display in pixels.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.display_height_px)
display_width_px: number
The width of the display in pixels.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.display_width_px)
name: "computer"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.name)
type: "computer_20241022"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.defer_loading)
display_number: optional number
The X11 display number (e.g. 0, 1) for the display.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.display_number)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20241022)
BetaMemoryTool20250818 object { name, type, allowed_callers, 4 more } 
name: "memory"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.name)
type: "memory_20250818"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_memory_tool_20250818)
BetaToolComputerUse20250124 object { display_height_px, display_width_px, name, 7 more } 
display_height_px: number
The height of the display in pixels.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.display_height_px)
display_width_px: number
The width of the display in pixels.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.display_width_px)
name: "computer"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.name)
type: "computer_20250124"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.defer_loading)
display_number: optional number
The X11 display number (e.g. 0, 1) for the display.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.display_number)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20250124)
BetaToolTextEditor20241022 object { name, type, allowed_callers, 4 more } 
name: "str_replace_editor"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.name)
type: "text_editor_20241022"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20241022)
BetaToolComputerUse20251124 object { display_height_px, display_width_px, name, 8 more } 
display_height_px: number
The height of the display in pixels.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.display_height_px)
display_width_px: number
The width of the display in pixels.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.display_width_px)
name: "computer"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.name)
type: "computer_20251124"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.defer_loading)
display_number: optional number
The X11 display number (e.g. 0, 1) for the display.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.display_number)
enable_zoom: optional boolean
Whether to enable an action to take a zoomed-in screenshot of the screen.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.enable_zoom)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_computer_use_20251124)
BetaToolTextEditor20250124 object { name, type, allowed_callers, 4 more } 
name: "str_replace_editor"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.name)
type: "text_editor_20250124"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250124)
BetaToolTextEditor20250429 object { name, type, allowed_callers, 4 more } 
name: "str_replace_based_edit_tool"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.name)
type: "text_editor_20250429"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250429)
BetaToolTextEditor20250728 object { name, type, allowed_callers, 5 more } 
name: "str_replace_based_edit_tool"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.name)
type: "text_editor_20250728"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.input_examples)
max_characters: optional number
Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.max_characters)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_text_editor_20250728)
BetaWebSearchTool20250305 object { name, type, allowed_callers, 7 more } 
name: "web_search"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.name)
type: "web_search_20250305"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.allowed_callers)
allowed_domains: optional array of string
If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.allowed_domains)
blocked_domains: optional array of string
If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.blocked_domains)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.defer_loading)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.strict)
user_location: optional [BetaUserLocation](https://platform.claude.com/docs/en/api/beta#beta_user_location) { type, city, country, 2 more } 
Parameters for the user's location. Used to provide more relevant search results.
type: "approximate"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.user_location%20%2B%20\(resource\)%20beta.messages.type)
city: optional string
The city of the user.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.user_location%20%2B%20\(resource\)%20beta.messages.city)
country: optional string
The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.user_location%20%2B%20\(resource\)%20beta.messages.country)
region: optional string
The region of the user.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.user_location%20%2B%20\(resource\)%20beta.messages.region)
timezone: optional string
The [IANA timezone](https://nodatime.org/TimeZones) of the user.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.user_location%20%2B%20\(resource\)%20beta.messages.timezone)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305.user_location)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20250305)
BetaWebFetchTool20250910 object { name, type, allowed_callers, 8 more } 
name: "web_fetch"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.name)
type: "web_fetch_20250910"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.allowed_callers)
allowed_domains: optional array of string
List of domains to allow fetching from
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.allowed_domains)
blocked_domains: optional array of string
List of domains to block fetching from
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.blocked_domains)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.cache_control)
citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled } 
Citations configuration for fetched documents. Citations are disabled by default.
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.citations%20%2B%20\(resource\)%20beta.messages.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.citations)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.defer_loading)
max_content_tokens: optional number
Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.max_content_tokens)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20250910)
BetaWebSearchTool20260209 object { name, type, allowed_callers, 7 more } 
name: "web_search"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.name)
type: "web_search_20260209"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.allowed_callers)
allowed_domains: optional array of string
If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.allowed_domains)
blocked_domains: optional array of string
If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.blocked_domains)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.defer_loading)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.strict)
user_location: optional [BetaUserLocation](https://platform.claude.com/docs/en/api/beta#beta_user_location) { type, city, country, 2 more } 
Parameters for the user's location. Used to provide more relevant search results.
type: "approximate"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.user_location%20%2B%20\(resource\)%20beta.messages.type)
city: optional string
The city of the user.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.user_location%20%2B%20\(resource\)%20beta.messages.city)
country: optional string
The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.user_location%20%2B%20\(resource\)%20beta.messages.country)
region: optional string
The region of the user.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.user_location%20%2B%20\(resource\)%20beta.messages.region)
timezone: optional string
The [IANA timezone](https://nodatime.org/TimeZones) of the user.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.user_location%20%2B%20\(resource\)%20beta.messages.timezone)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209.user_location)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_search_tool_20260209)
BetaWebFetchTool20260209 object { name, type, allowed_callers, 8 more } 
name: "web_fetch"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.name)
type: "web_fetch_20260209"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.allowed_callers)
allowed_domains: optional array of string
List of domains to allow fetching from
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.allowed_domains)
blocked_domains: optional array of string
List of domains to block fetching from
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.blocked_domains)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.cache_control)
citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled } 
Citations configuration for fetched documents. Citations are disabled by default.
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.citations%20%2B%20\(resource\)%20beta.messages.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.citations)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.defer_loading)
max_content_tokens: optional number
Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.max_content_tokens)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260209)
BetaWebFetchTool20260309 object { name, type, allowed_callers, 9 more } 
Web fetch tool with use_cache parameter for bypassing cached content.
name: "web_fetch"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.name)
type: "web_fetch_20260309"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.allowed_callers)
allowed_domains: optional array of string
List of domains to allow fetching from
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.allowed_domains)
blocked_domains: optional array of string
List of domains to block fetching from
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.blocked_domains)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.cache_control)
citations: optional [BetaCitationsConfigParam](https://platform.claude.com/docs/en/api/beta#beta_citations_config_param) { enabled } 
Citations configuration for fetched documents. Citations are disabled by default.
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.citations%20%2B%20\(resource\)%20beta.messages.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.citations)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.defer_loading)
max_content_tokens: optional number
Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.max_content_tokens)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.strict)
use_cache: optional boolean
Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309.use_cache)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_web_fetch_tool_20260309)
BetaAdvisorTool20260301 object { model, name, type, 7 more } 
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.model)
name: "advisor"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.name)
type: "advisor_20260301"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.cache_control)
caching: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.caching%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.caching%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.caching%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.caching%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.caching)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.defer_loading)
max_tokens: optional number
Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.max_tokens)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_advisor_tool_20260301)
BetaToolSearchToolBm25_20251119 object { name, type, allowed_callers, 3 more } 
name: "tool_search_tool_bm25"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.name)
type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"
"tool_search_tool_bm25_20251119"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.type%5B0%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.type%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_bm25_20251119)
BetaToolSearchToolRegex20251119 object { name, type, allowed_callers, 3 more } 
name: "tool_search_tool_regex"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.name)
type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"
"tool_search_tool_regex_20251119"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.type%5B0%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.type%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.allowed_callers)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119.strict)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_tool_search_tool_regex_20251119)
BetaMCPToolset object { mcp_server_name, type, cache_control, 2 more } 
Configuration for a group of tools from an MCP server.
Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.
mcp_server_name: string
Name of the MCP server to configure tools for
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset.mcp_server_name)
type: "mcp_toolset"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset.type)
cache_control: optional [BetaCacheControlEphemeral](https://platform.claude.com/docs/en/api/beta#beta_cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset.cache_control%20%2B%20\(resource\)%20beta.messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset.cache_control%20%2B%20\(resource\)%20beta.messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset.cache_control%20%2B%20\(resource\)%20beta.messages.ttl)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset.cache_control)
configs: optional map[[BetaMCPToolConfig](https://platform.claude.com/docs/en/api/beta#beta_mcp_tool_config) { defer_loading, enabled } ]
Configuration overrides for specific tools, keyed by tool name
defer_loading: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_config.defer_loading)
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_tool_config.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset.configs)
default_config: optional [BetaMCPToolDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_mcp_tool_default_config) { defer_loading, enabled } 
Default configuration applied to all tools from this server
defer_loading: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.messages.defer_loading)
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.messages.enabled)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset.default_config)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_mcp_toolset)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.tools)
Deprecatedtop_k: optional number
Only sample from the top K options for each subsequent token.
Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.
Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).
Recommended for advanced use cases only.
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.top_k)
Deprecatedtop_p: optional number
Use nucleus sampling.
Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.
In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.
Recommended for advanced use cases only.
maximum1
minimum0
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.top_p)
user_profile_id: optional string
The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params.user_profile_id)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests.items.params)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#create.requests)
BetaMessageBatch object { id, archived_at, cancel_initiated_at, 7 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.id)
archived_at: string
RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.archived_at)
cancel_initiated_at: string
RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.cancel_initiated_at)
created_at: string
RFC 3339 datetime string representing the time at which the Message Batch was created.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.created_at)
ended_at: string
RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.
Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.
formatdate-time
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.ended_at)
expires_at: string
RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.expires_at)
processing_status: "in_progress" or "canceling" or "ended"
Processing status of the Message Batch.
"in_progress"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.processing_status%5B0%5D)
"canceling"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.processing_status%5B1%5D)
"ended"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.processing_status%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.processing_status)
request_counts: [BetaMessageBatchRequestCounts](https://platform.claude.com/docs/en/api/beta#beta_message_batch_request_counts) { canceled, errored, expired, 2 more } 
Tallies requests within the Message Batch, categorized by their status.
Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.
canceled: number
Number of requests in the Message Batch that have been canceled.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.request_counts%20%2B%20\(resource\)%20beta.messages.batches.canceled)
errored: number
Number of requests in the Message Batch that encountered an error.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.request_counts%20%2B%20\(resource\)%20beta.messages.batches.errored)
expired: number
Number of requests in the Message Batch that have expired.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.request_counts%20%2B%20\(resource\)%20beta.messages.batches.expired)
processing: number
Number of requests in the Message Batch that are processing.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.request_counts%20%2B%20\(resource\)%20beta.messages.batches.processing)
succeeded: number
Number of requests in the Message Batch that have completed successfully.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.request_counts%20%2B%20\(resource\)%20beta.messages.batches.succeeded)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.request_counts)
results_url: string
URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.
Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.results_url)
type: "message_batch"
Object type.
For Message Batches, this is always `"message_batch"`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/create#beta_message_batch)
Create a Message Batch
cURL

curl https://api.anthropic.com/v1/messages/batches \
    -H 'Content-Type: application/json' \
    -H 'anthropic-beta: message-batches-2024-09-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "requests": [
              "custom_id": "my-custom-id-1",
              "params": {
                "max_tokens": 1024,
                "messages": [
                    "content": "Hello, world",
                    "role": "user"
                ],
                "model": "claude-opus-4-6"
          ]
        }'

  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"

  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
