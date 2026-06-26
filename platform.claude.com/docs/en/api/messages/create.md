<!-- source: https://platform.claude.com/docs/en/api/messages/create -->

# Create a Message
POST/v1/messages
Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.
The Messages API can be used for either single queries or stateless multi-turn conversations.
Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)
#####  Body ParametersJSONExpand Collapse 
max_tokens: number
The maximum number of tokens to generate before stopping.
Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.
Set to `0` to populate the [prompt cache](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.
Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#create.max_tokens)
messages: array of [MessageParam](https://platform.claude.com/docs/en/api/messages#message_param) { content, role } 
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
content: string or array of [ContentBlockParam](https://platform.claude.com/docs/en/api/messages#content_block_param)
string
[](https://platform.claude.com/docs/en/api/messages/create#message_param.content%5B0%5D)
array of [ContentBlockParam](https://platform.claude.com/docs/en/api/messages#content_block_param)
TextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param)
ImageBlockParam object { source, type, cache_control } 
source: [Base64ImageSource](https://platform.claude.com/docs/en/api/messages#base64_image_source) { data, media_type, type }  or [URLImageSource](https://platform.claude.com/docs/en/api/messages#url_image_source) { type, url } 
Base64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.type)
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source)
URLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source.url)
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param)
DocumentBlockParam object { source, type, cache_control, 3 more } 
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type }  or [ContentBlockSource](https://platform.claude.com/docs/en/api/messages#content_block_source) { content, type }  or [URLPDFSource](https://platform.claude.com/docs/en/api/messages#url_pdf_source) { type, url } 
Base64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#base64_pdf_source.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/messages/create#base64_pdf_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/create#base64_pdf_source.type)
[](https://platform.claude.com/docs/en/api/messages/create#base64_pdf_source)
PlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#plain_text_source.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/messages/create#plain_text_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#plain_text_source.type)
[](https://platform.claude.com/docs/en/api/messages/create#plain_text_source)
ContentBlockSource object { content, type } 
content: string or array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
string
[](https://platform.claude.com/docs/en/api/messages/create#content_block_source.content%5B0%5D)
ContentBlockSourceContent = array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
TextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param)
ImageBlockParam object { source, type, cache_control } 
source: [Base64ImageSource](https://platform.claude.com/docs/en/api/messages#base64_image_source) { data, media_type, type }  or [URLImageSource](https://platform.claude.com/docs/en/api/messages#url_image_source) { type, url } 
Base64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.type)
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source)
URLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source.url)
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param)
[](https://platform.claude.com/docs/en/api/messages/create#content_block_source.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#content_block_source.content)
type: "content"
[](https://platform.claude.com/docs/en/api/messages/create#content_block_source.type)
[](https://platform.claude.com/docs/en/api/messages/create#content_block_source)
URLPDFSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/create#url_pdf_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#url_pdf_source.url)
[](https://platform.claude.com/docs/en/api/messages/create#url_pdf_source)
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.source)
type: "document"
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.citations)
context: optional string
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.context)
title: optional string
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.title)
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param)
SearchResultBlockParam object { content, source, title, 3 more } 
content: array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.content)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.source)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param)
ThinkingBlockParam object { signature, thinking, type } 
signature: string
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block_param.signature)
thinking: string
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block_param.thinking)
type: "thinking"
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block_param)
RedactedThinkingBlockParam object { data, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#redacted_thinking_block_param.data)
type: "redacted_thinking"
[](https://platform.claude.com/docs/en/api/messages/create#redacted_thinking_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#redacted_thinking_block_param)
ToolUseBlockParam object { id, input, name, 3 more } 
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block_param.id)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block_param.input)
name: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block_param.name)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block_param.cache_control)
caller: optional [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block_param.caller)
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block_param)
ToolResultBlockParam object { tool_use_id, type, cache_control, 2 more } 
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param.tool_use_id)
type: "tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param.cache_control)
content: optional string or array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }  or [ImageBlockParam](https://platform.claude.com/docs/en/api/messages#image_block_param) { source, type, cache_control }  or [SearchResultBlockParam](https://platform.claude.com/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more }  or 2 more
string
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param.content%5B0%5D)
array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }  or [ImageBlockParam](https://platform.claude.com/docs/en/api/messages#image_block_param) { source, type, cache_control }  or [SearchResultBlockParam](https://platform.claude.com/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more }  or 2 more
TextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param)
ImageBlockParam object { source, type, cache_control } 
source: [Base64ImageSource](https://platform.claude.com/docs/en/api/messages#base64_image_source) { data, media_type, type }  or [URLImageSource](https://platform.claude.com/docs/en/api/messages#url_image_source) { type, url } 
Base64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.type)
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source)
URLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source.url)
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param)
SearchResultBlockParam object { content, source, title, 3 more } 
content: array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.content)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.source)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/create#search_result_block_param)
DocumentBlockParam object { source, type, cache_control, 3 more } 
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type }  or [ContentBlockSource](https://platform.claude.com/docs/en/api/messages#content_block_source) { content, type }  or [URLPDFSource](https://platform.claude.com/docs/en/api/messages#url_pdf_source) { type, url } 
Base64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#base64_pdf_source.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/messages/create#base64_pdf_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/create#base64_pdf_source.type)
[](https://platform.claude.com/docs/en/api/messages/create#base64_pdf_source)
PlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#plain_text_source.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/messages/create#plain_text_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#plain_text_source.type)
[](https://platform.claude.com/docs/en/api/messages/create#plain_text_source)
ContentBlockSource object { content, type } 
content: string or array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
string
[](https://platform.claude.com/docs/en/api/messages/create#content_block_source.content%5B0%5D)
ContentBlockSourceContent = array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
TextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param)
ImageBlockParam object { source, type, cache_control } 
source: [Base64ImageSource](https://platform.claude.com/docs/en/api/messages#base64_image_source) { data, media_type, type }  or [URLImageSource](https://platform.claude.com/docs/en/api/messages#url_image_source) { type, url } 
Base64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source.type)
[](https://platform.claude.com/docs/en/api/messages/create#base64_image_source)
URLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source.url)
[](https://platform.claude.com/docs/en/api/messages/create#url_image_source)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param)
[](https://platform.claude.com/docs/en/api/messages/create#content_block_source.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#content_block_source.content)
type: "content"
[](https://platform.claude.com/docs/en/api/messages/create#content_block_source.type)
[](https://platform.claude.com/docs/en/api/messages/create#content_block_source)
URLPDFSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/create#url_pdf_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#url_pdf_source.url)
[](https://platform.claude.com/docs/en/api/messages/create#url_pdf_source)
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.source)
type: "document"
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.citations)
context: optional string
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.context)
title: optional string
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.title)
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param)
ToolReferenceBlockParam object { tool_name, type, cache_control } 
Tool reference block that can be included in tool_result content.
tool_name: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param)
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param.content)
is_error: optional boolean
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param.is_error)
[](https://platform.claude.com/docs/en/api/messages/create#tool_result_block_param)
ServerToolUseBlockParam object { id, input, name, 3 more } 
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.id)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.input)
name: "web_search" or "web_fetch" or "code_execution" or 4 more
"web_search"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.name%5B0%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.name%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.name%5B2%5D)
"bash_code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.name%5B3%5D)
"text_editor_code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.name%5B4%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.name%5B5%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.name%5B6%5D)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.name)
type: "server_tool_use"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.cache_control)
caller: optional [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param.caller)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block_param)
WebSearchToolResultBlockParam object { content, tool_use_id, type, 2 more } 
content: [WebSearchToolResultBlockParamContent](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_block_param_content)
WebSearchToolResultBlockItem = array of [WebSearchResultBlockParam](https://platform.claude.com/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } 
encrypted_content: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.encrypted_content)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.title)
type: "web_search_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.url)
page_age: optional string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.page_age)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages%5B0%5D)
WebSearchToolRequestError object { error_code, type } 
error_code: [WebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"query_too_long"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
"request_too_large"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B5%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.error_code)
type: "web_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.tool_use_id)
type: "web_search_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.cache_control)
caller: optional [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param.caller)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block_param)
WebFetchToolResultBlockParam object { content, tool_use_id, type, 2 more } 
content: [WebFetchToolResultErrorBlockParam](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_block_param) { error_code, type }  or [WebFetchBlockParam](https://platform.claude.com/docs/en/api/messages#web_fetch_block_param) { content, type, url, retrieved_at } 
WebFetchToolResultErrorBlockParam object { error_code, type } 
error_code: [WebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"url_too_long"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"url_not_allowed"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"url_not_in_prior_context"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"url_not_accessible"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
"unsupported_content_type"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B5%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B6%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B7%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B8%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param.error_code)
type: "web_fetch_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block_param)
WebFetchBlockParam object { content, type, url, retrieved_at } 
content: [DocumentBlockParam](https://platform.claude.com/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } 
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type }  or [ContentBlockSource](https://platform.claude.com/docs/en/api/messages#content_block_source) { content, type }  or [URLPDFSource](https://platform.claude.com/docs/en/api/messages#url_pdf_source) { type, url } 
Base64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
PlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
ContentBlockSource object { content, type } 
content: string or array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.content%5B0%5D)
ContentBlockSourceContent = array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
TextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.citations)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
ImageBlockParam object { source, type, cache_control } 
source: [Base64ImageSource](https://platform.claude.com/docs/en/api/messages#base64_image_source) { data, media_type, type }  or [URLImageSource](https://platform.claude.com/docs/en/api/messages#url_image_source) { type, url } 
Base64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
URLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.source)
type: "image"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.content)
type: "content"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
URLPDFSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.source)
type: "document"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/create#document_block_param.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.citations)
context: optional string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.context)
title: optional string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.title)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.content)
type: "web_fetch_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.type)
url: string
Fetched content URL
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.url)
retrieved_at: optional string
ISO 8601 timestamp when the content was retrieved
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param.retrieved_at)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block_param)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block_param.tool_use_id)
type: "web_fetch_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block_param.cache_control)
caller: optional [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block_param.caller)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block_param)
CodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [CodeExecutionToolResultBlockParamContent](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_block_param_content)
Code execution result with encrypted stdout for PFC + web_search results.
CodeExecutionToolResultErrorParam object { error_code, type } 
error_code: [CodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.error_code)
type: "code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages)
CodeExecutionResultBlockParam object { content, return_code, stderr, 2 more } 
content: array of [CodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/messages#code_execution_output_block_param) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.content)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.stdout)
type: "code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages)
EncryptedCodeExecutionResultBlockParam object { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
content: array of [CodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/messages#code_execution_output_block_param) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.content)
encrypted_stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.encrypted_stdout)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.stderr)
type: "encrypted_code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.tool_use_id)
type: "code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block_param)
BashCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [BashCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error_param) { error_code, type }  or [BashCodeExecutionResultBlockParam](https://platform.claude.com/docs/en/api/messages#bash_code_execution_result_block_param) { content, return_code, stderr, 2 more } 
BashCodeExecutionToolResultErrorParam object { error_code, type } 
error_code: [BashCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"output_file_too_large"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error_param.error_code)
type: "bash_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error_param)
BashCodeExecutionResultBlockParam object { content, return_code, stderr, 2 more } 
content: array of [BashCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/messages#bash_code_execution_output_block_param) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_output_block_param.file_id)
type: "bash_code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_output_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block_param.content)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block_param.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block_param.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block_param.stdout)
type: "bash_code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block_param)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block_param.tool_use_id)
type: "bash_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block_param)
TextEditorCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [TextEditorCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error_param) { error_code, type, error_message }  or [TextEditorCodeExecutionViewResultBlockParam](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more }  or [TextEditorCodeExecutionCreateResultBlockParam](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_create_result_block_param) { is_file_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlockParam](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more } 
TextEditorCodeExecutionToolResultErrorParam object { error_code, type, error_message } 
error_code: [TextEditorCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"file_not_found"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error_param.error_code)
type: "text_editor_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error_param.type)
error_message: optional string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error_param.error_message)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error_param)
TextEditorCodeExecutionViewResultBlockParam object { content, file_type, type, 3 more } 
content: string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block_param.content)
file_type: "text" or "image" or "pdf"
"text"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block_param.file_type%5B0%5D)
"image"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block_param.file_type%5B1%5D)
"pdf"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block_param.file_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block_param.file_type)
type: "text_editor_code_execution_view_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block_param.type)
num_lines: optional number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block_param.num_lines)
start_line: optional number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block_param.start_line)
total_lines: optional number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block_param.total_lines)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block_param)
TextEditorCodeExecutionCreateResultBlockParam object { is_file_update, type } 
is_file_update: boolean
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_create_result_block_param.is_file_update)
type: "text_editor_code_execution_create_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_create_result_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_create_result_block_param)
TextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new_lines, 3 more } 
type: "text_editor_code_execution_str_replace_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block_param.type)
lines: optional array of string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block_param.lines)
new_lines: optional number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block_param.new_lines)
new_start: optional number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block_param.new_start)
old_lines: optional number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block_param.old_lines)
old_start: optional number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block_param.old_start)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block_param)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block_param.tool_use_id)
type: "text_editor_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block_param)
ToolSearchToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [ToolSearchToolResultErrorParam](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error_param) { error_code, type, error_message }  or [ToolSearchToolSearchResultBlockParam](https://platform.claude.com/docs/en/api/messages#tool_search_tool_search_result_block_param) { tool_references, type } 
ToolSearchToolResultErrorParam object { error_code, type, error_message } 
error_code: [ToolSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error_param.error_code)
type: "tool_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error_param.type)
error_message: optional string
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error_param.error_message)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error_param)
ToolSearchToolSearchResultBlockParam object { tool_references, type } 
tool_references: array of [ToolReferenceBlockParam](https://platform.claude.com/docs/en/api/messages#tool_reference_block_param) { tool_name, type, cache_control } 
tool_name: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_search_result_block_param.tool_references)
type: "tool_search_tool_search_result"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_search_result_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_search_result_block_param)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block_param.tool_use_id)
type: "tool_search_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block_param)
ContainerUploadBlockParam object { file_id, type, cache_control } 
A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block_param.file_id)
type: "container_upload"
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block_param)
MidConversationSystemBlockParam object { content, type, cache_control } 
System instructions that appear mid-conversation.
Use this block to provide or update system-level instructions at a specific point in the conversation, rather than only via the top-level `system` parameter.
content: array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } 
System instruction text blocks.
text: string
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/create#mid_conversation_system_block_param.content)
type: "mid_conv_system"
[](https://platform.claude.com/docs/en/api/messages/create#mid_conversation_system_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#mid_conversation_system_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/create#mid_conversation_system_block_param)
[](https://platform.claude.com/docs/en/api/messages/create#message_param.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#message_param.content)
role: "user" or "assistant" or "system"
"user"
[](https://platform.claude.com/docs/en/api/messages/create#message_param.role%5B0%5D)
"assistant"
[](https://platform.claude.com/docs/en/api/messages/create#message_param.role%5B1%5D)
"system"
[](https://platform.claude.com/docs/en/api/messages/create#message_param.role%5B2%5D)
[](https://platform.claude.com/docs/en/api/messages/create#message_param.role)
[](https://platform.claude.com/docs/en/api/messages/create#create.messages)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/messages/create#create.model%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#create.model)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#create.cache_control.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#create.cache_control.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#create.cache_control.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#create.cache_control.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#create.cache_control)
container: optional string
Container identifier for reuse across requests.
[](https://platform.claude.com/docs/en/api/messages/create#create.container)
inference_geo: optional string
Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.
[](https://platform.claude.com/docs/en/api/messages/create#create.inference_geo)
metadata: optional [Metadata](https://platform.claude.com/docs/en/api/messages#metadata) { user_id } 
An object describing metadata about the request.
user_id: optional string
An external identifier for the user who is associated with the request.
This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.
maxLength512
[](https://platform.claude.com/docs/en/api/messages/create#create.metadata.user_id)
[](https://platform.claude.com/docs/en/api/messages/create#create.metadata)
output_config: optional [OutputConfig](https://platform.claude.com/docs/en/api/messages#output_config) { effort, format } 
Configuration options for the model's output, such as the output format.
effort: optional "low" or "medium" or "high" or 2 more
All possible effort levels.
"low"
[](https://platform.claude.com/docs/en/api/messages/create#create.output_config.effort%5B0%5D)
"medium"
[](https://platform.claude.com/docs/en/api/messages/create#create.output_config.effort%5B1%5D)
"high"
[](https://platform.claude.com/docs/en/api/messages/create#create.output_config.effort%5B2%5D)
"xhigh"
[](https://platform.claude.com/docs/en/api/messages/create#create.output_config.effort%5B3%5D)
"max"
[](https://platform.claude.com/docs/en/api/messages/create#create.output_config.effort%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/create#create.output_config.effort)
format: optional [JSONOutputFormat](https://platform.claude.com/docs/en/api/messages#json_output_format) { schema, type } 
A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
schema: map[unknown]
The JSON schema of the format
[](https://platform.claude.com/docs/en/api/messages/create#output_config.format%20%2B%20\(resource\)%20messages.schema)
type: "json_schema"
[](https://platform.claude.com/docs/en/api/messages/create#output_config.format%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#create.output_config.format)
[](https://platform.claude.com/docs/en/api/messages/create#create.output_config)
service_tier: optional "auto" or "standard_only"
Determines whether to use priority capacity (if available) or standard capacity for this request.
Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.
"auto"
[](https://platform.claude.com/docs/en/api/messages/create#create.service_tier%5B0%5D)
"standard_only"
[](https://platform.claude.com/docs/en/api/messages/create#create.service_tier%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#create.service_tier)
stop_sequences: optional array of string
Custom text sequences that will cause the model to stop generating.
Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.
If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.
[](https://platform.claude.com/docs/en/api/messages/create#create.stop_sequences)
stream: optional boolean
Whether to incrementally stream the response using server-sent events.
See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.
[](https://platform.claude.com/docs/en/api/messages/create#create.stream)
system: optional string or array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } 
System prompt.
A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).
string
[](https://platform.claude.com/docs/en/api/messages/create#create.system%5B0%5D)
array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/create#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/create#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/create#create.system%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#create.system)
Deprecatedtemperature: optional number
Amount of randomness injected into the response.
Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.
Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.
Note that even with `temperature` of `0.0`, the results will not be fully deterministic.
maximum1
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#create.temperature)
thinking: optional [ThinkingConfigParam](https://platform.claude.com/docs/en/api/messages#thinking_config_param)
Configuration for enabling Claude's extended thinking.
When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.
See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.
ThinkingConfigEnabled object { budget_tokens, type, display } 
budget_tokens: number
Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.
Must be ≥1024 and less than `max_tokens`.
See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.
minimum1024
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking.budget_tokens)
type: "enabled"
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking.type)
display: optional "summarized" or "omitted"
Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.
"summarized"
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking.display%5B0%5D)
"omitted"
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking.display%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking.display)
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking)
ThinkingConfigDisabled object { type } 
type: "disabled"
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking.type)
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking)
ThinkingConfigAdaptive object { type, display } 
type: "adaptive"
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking.type)
display: optional "summarized" or "omitted"
Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.
"summarized"
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking.display%5B0%5D)
"omitted"
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking.display%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking.display)
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking)
[](https://platform.claude.com/docs/en/api/messages/create#create.thinking)
tool_choice: optional [ToolChoice](https://platform.claude.com/docs/en/api/messages#tool_choice)
How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.
ToolChoiceAuto object { type, disable_parallel_tool_use } 
The model will automatically decide whether to use tools.
type: "auto"
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice.type)
disable_parallel_tool_use: optional boolean
Whether to disable parallel tool use.
Defaults to `false`. If set to `true`, the model will output at most one tool use.
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice.disable_parallel_tool_use)
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice)
ToolChoiceAny object { type, disable_parallel_tool_use } 
The model will use any available tools.
type: "any"
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice.type)
disable_parallel_tool_use: optional boolean
Whether to disable parallel tool use.
Defaults to `false`. If set to `true`, the model will output exactly one tool use.
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice.disable_parallel_tool_use)
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice)
ToolChoiceTool object { name, type, disable_parallel_tool_use } 
The model will use the specified tool with `tool_choice.name`.
name: string
The name of the tool to use.
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice.name)
type: "tool"
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice.type)
disable_parallel_tool_use: optional boolean
Whether to disable parallel tool use.
Defaults to `false`. If set to `true`, the model will output exactly one tool use.
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice.disable_parallel_tool_use)
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice)
ToolChoiceNone object { type } 
The model will not be allowed to use tools.
type: "none"
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice.type)
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice)
[](https://platform.claude.com/docs/en/api/messages/create#create.tool_choice)
tools: optional array of [ToolUnion](https://platform.claude.com/docs/en/api/messages#tool_union)
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
Tool object { input_schema, name, allowed_callers, 7 more } 
input_schema: object { type, properties, required } 
[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.
This defines the shape of the `input` that your tool accepts and that the model will produce.
type: "object"
[](https://platform.claude.com/docs/en/api/messages/create#tool.input_schema.type)
properties: optional map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#tool.input_schema.properties)
required: optional array of string
[](https://platform.claude.com/docs/en/api/messages/create#tool.input_schema.required)
[](https://platform.claude.com/docs/en/api/messages/create#tool.input_schema)
name: string
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
maxLength128
minLength1
[](https://platform.claude.com/docs/en/api/messages/create#tool.name)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#tool.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#tool.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#tool.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#tool.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#tool.defer_loading)
description: optional string
Description of what this tool does.
Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.
[](https://platform.claude.com/docs/en/api/messages/create#tool.description)
eager_input_streaming: optional boolean
Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.
[](https://platform.claude.com/docs/en/api/messages/create#tool.eager_input_streaming)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#tool.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#tool.strict)
type: optional "custom"
[](https://platform.claude.com/docs/en/api/messages/create#tool.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool)
ToolBash20250124 object { name, type, allowed_callers, 4 more } 
name: "bash"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.name)
type: "bash_20250124"
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124.strict)
[](https://platform.claude.com/docs/en/api/messages/create#tool_bash_20250124)
CodeExecutionTool20250522 object { name, type, allowed_callers, 3 more } 
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.name)
type: "code_execution_20250522"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522.strict)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250522)
CodeExecutionTool20250825 object { name, type, allowed_callers, 3 more } 
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.name)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825.strict)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20250825)
CodeExecutionTool20260120 object { name, type, allowed_callers, 3 more } 
Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.name)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120.strict)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260120)
CodeExecutionTool20260521 object { name, type, allowed_callers, 3 more } 
Code execution tool with REPL state persistence.
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.name)
type: "code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521.strict)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_20260521)
MemoryTool20250818 object { name, type, allowed_callers, 4 more } 
name: "memory"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.name)
type: "memory_20250818"
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818.strict)
[](https://platform.claude.com/docs/en/api/messages/create#memory_tool_20250818)
ToolTextEditor20250124 object { name, type, allowed_callers, 4 more } 
name: "str_replace_editor"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.name)
type: "text_editor_20250124"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124.strict)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250124)
ToolTextEditor20250429 object { name, type, allowed_callers, 4 more } 
name: "str_replace_based_edit_tool"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.name)
type: "text_editor_20250429"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429.strict)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250429)
ToolTextEditor20250728 object { name, type, allowed_callers, 5 more } 
name: "str_replace_based_edit_tool"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.name)
type: "text_editor_20250728"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.input_examples)
max_characters: optional number
Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.max_characters)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728.strict)
[](https://platform.claude.com/docs/en/api/messages/create#tool_text_editor_20250728)
WebSearchTool20250305 object { name, type, allowed_callers, 7 more } 
name: "web_search"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.name)
type: "web_search_20250305"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.allowed_callers)
allowed_domains: optional array of string
If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.allowed_domains)
blocked_domains: optional array of string
If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.blocked_domains)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.defer_loading)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.strict)
user_location: optional [UserLocation](https://platform.claude.com/docs/en/api/messages#user_location) { type, city, country, 2 more } 
Parameters for the user's location. Used to provide more relevant search results.
type: "approximate"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.user_location%20%2B%20\(resource\)%20messages.type)
city: optional string
The city of the user.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.user_location%20%2B%20\(resource\)%20messages.city)
country: optional string
The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.user_location%20%2B%20\(resource\)%20messages.country)
region: optional string
The region of the user.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.user_location%20%2B%20\(resource\)%20messages.region)
timezone: optional string
The [IANA timezone](https://nodatime.org/TimeZones) of the user.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.user_location%20%2B%20\(resource\)%20messages.timezone)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305.user_location)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20250305)
WebFetchTool20250910 object { name, type, allowed_callers, 8 more } 
name: "web_fetch"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.name)
type: "web_fetch_20250910"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.allowed_callers)
allowed_domains: optional array of string
List of domains to allow fetching from
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.allowed_domains)
blocked_domains: optional array of string
List of domains to block fetching from
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.blocked_domains)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
Citations configuration for fetched documents. Citations are disabled by default.
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.citations)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.defer_loading)
max_content_tokens: optional number
Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.max_content_tokens)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910.strict)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20250910)
WebSearchTool20260209 object { name, type, allowed_callers, 7 more } 
name: "web_search"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.name)
type: "web_search_20260209"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.allowed_callers)
allowed_domains: optional array of string
If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.allowed_domains)
blocked_domains: optional array of string
If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.blocked_domains)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.defer_loading)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.strict)
user_location: optional [UserLocation](https://platform.claude.com/docs/en/api/messages#user_location) { type, city, country, 2 more } 
Parameters for the user's location. Used to provide more relevant search results.
type: "approximate"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.user_location%20%2B%20\(resource\)%20messages.type)
city: optional string
The city of the user.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.user_location%20%2B%20\(resource\)%20messages.city)
country: optional string
The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.user_location%20%2B%20\(resource\)%20messages.country)
region: optional string
The region of the user.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.user_location%20%2B%20\(resource\)%20messages.region)
timezone: optional string
The [IANA timezone](https://nodatime.org/TimeZones) of the user.
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.user_location%20%2B%20\(resource\)%20messages.timezone)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209.user_location)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_20260209)
WebFetchTool20260209 object { name, type, allowed_callers, 8 more } 
name: "web_fetch"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.name)
type: "web_fetch_20260209"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.allowed_callers)
allowed_domains: optional array of string
List of domains to allow fetching from
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.allowed_domains)
blocked_domains: optional array of string
List of domains to block fetching from
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.blocked_domains)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
Citations configuration for fetched documents. Citations are disabled by default.
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.citations)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.defer_loading)
max_content_tokens: optional number
Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.max_content_tokens)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209.strict)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260209)
WebFetchTool20260309 object { name, type, allowed_callers, 9 more } 
Web fetch tool with use_cache parameter for bypassing cached content.
name: "web_fetch"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.name)
type: "web_fetch_20260309"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.allowed_callers)
allowed_domains: optional array of string
List of domains to allow fetching from
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.allowed_domains)
blocked_domains: optional array of string
List of domains to block fetching from
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.blocked_domains)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
Citations configuration for fetched documents. Citations are disabled by default.
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.citations)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.defer_loading)
max_content_tokens: optional number
Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.max_content_tokens)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.strict)
use_cache: optional boolean
Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309.use_cache)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_20260309)
ToolSearchToolBm25_20251119 object { name, type, allowed_callers, 3 more } 
name: "tool_search_tool_bm25"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.name)
type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"
"tool_search_tool_bm25_20251119"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.type%5B0%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.type%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119.strict)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_bm25_20251119)
ToolSearchToolRegex20251119 object { name, type, allowed_callers, 3 more } 
name: "tool_search_tool_regex"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.name)
type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"
"tool_search_tool_regex_20251119"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.type%5B0%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.type%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119.strict)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_regex_20251119)
[](https://platform.claude.com/docs/en/api/messages/create#create.tools)
Deprecatedtop_k: optional number
Only sample from the top K options for each subsequent token.
Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.
Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).
Recommended for advanced use cases only.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#create.top_k)
Deprecatedtop_p: optional number
Use nucleus sampling.
Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.
In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.
Recommended for advanced use cases only.
maximum1
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#create.top_p)
Message object { id, container, content, 7 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/messages/create#message.id)
container: [Container](https://platform.claude.com/docs/en/api/messages#container) { id, expires_at } 
Information about the container used in the request (for the code execution tool)
Identifier for the container used in this request
[](https://platform.claude.com/docs/en/api/messages/create#message.container%20%2B%20\(resource\)%20messages.id)
expires_at: string
The time at which the container will expire.
[](https://platform.claude.com/docs/en/api/messages/create#message.container%20%2B%20\(resource\)%20messages.expires_at)
[](https://platform.claude.com/docs/en/api/messages/create#message.container)
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

TextBlock object { citations, text, type } 
citations: array of [TextCitation](https://platform.claude.com/docs/en/api/messages#text_citation)
Citations supporting the text block.
The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.
CitationCharLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.end_char_index)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.file_id)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location)
CitationPageLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.end_page_number)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.file_id)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location)
CitationContentBlockLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.end_block_index)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.file_id)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location)
CitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location.url)
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location)
CitationsSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.type)
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location)
[](https://platform.claude.com/docs/en/api/messages/create#text_block.citations)
text: string
[](https://platform.claude.com/docs/en/api/messages/create#text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#text_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_block)
ThinkingBlock object { signature, thinking, type } 
signature: string
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block.signature)
thinking: string
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block.thinking)
type: "thinking"
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block)
RedactedThinkingBlock object { data, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#redacted_thinking_block.data)
type: "redacted_thinking"
[](https://platform.claude.com/docs/en/api/messages/create#redacted_thinking_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#redacted_thinking_block)
ToolUseBlock object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block.input)
name: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block.name)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block)
ServerToolUseBlock object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.input)
name: "web_search" or "web_fetch" or "code_execution" or 4 more
"web_search"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B0%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B2%5D)
"bash_code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B3%5D)
"text_editor_code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B4%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B5%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B6%5D)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name)
type: "server_tool_use"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block)
WebSearchToolResultBlock object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.caller)
content: [WebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_block_content)
WebSearchToolResultError object { error_code, type } 
error_code: [WebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"query_too_long"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
"request_too_large"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B5%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.error_code)
type: "web_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages)
array of [WebSearchResultBlock](https://platform.claude.com/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } 
encrypted_content: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.encrypted_content)
page_age: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.page_age)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.title)
type: "web_search_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.tool_use_id)
type: "web_search_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block)
WebFetchToolResultBlock object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block.caller)
content: [WebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type }  or [WebFetchBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url } 
WebFetchToolResultErrorBlock object { error_code, type } 
error_code: [WebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"url_too_long"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"url_not_allowed"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"url_not_in_prior_context"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"url_not_accessible"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
"unsupported_content_type"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B5%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B6%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B7%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B8%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code)
type: "web_fetch_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block)
WebFetchBlock object { content, retrieved_at, type, url } 
content: [DocumentBlock](https://platform.claude.com/docs/en/api/messages#document_block) { citations, source, title, type } 
citations: [CitationsConfig](https://platform.claude.com/docs/en/api/messages#citations_config) { enabled } 
Citation configuration for the document
enabled: boolean
[](https://platform.claude.com/docs/en/api/messages/create#document_block.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.citations)
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type } 
Base64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages)
PlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.source)
title: string
The title of the document
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.title)
type: "document"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content)
retrieved_at: string
ISO 8601 timestamp when the content was retrieved
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.retrieved_at)
type: "web_fetch_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.type)
url: string
Fetched content URL
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.url)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block.tool_use_id)
type: "web_fetch_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block)
CodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [CodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_block_content)
Code execution result with encrypted stdout for PFC + web_search results.
CodeExecutionToolResultError object { error_code, type } 
error_code: [CodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.error_code)
type: "code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages)
CodeExecutionResultBlock object { content, return_code, stderr, 2 more } 
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.content)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.stdout)
type: "code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages)
EncryptedCodeExecutionResultBlock object { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.content)
encrypted_stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.encrypted_stdout)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.stderr)
type: "encrypted_code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.tool_use_id)
type: "code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block)
BashCodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [BashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type }  or [BashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more } 
BashCodeExecutionToolResultError object { error_code, type } 
error_code: [BashCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"output_file_too_large"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code)
type: "bash_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error)
BashCodeExecutionResultBlock object { content, return_code, stderr, 2 more } 
content: array of [BashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_output_block.file_id)
type: "bash_code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_output_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block.content)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block.stdout)
type: "bash_code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block.tool_use_id)
type: "bash_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block)
TextEditorCodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [TextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type }  or [TextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more } 
TextEditorCodeExecutionToolResultError object { error_code, error_message, type } 
error_code: [TextEditorCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"file_not_found"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_message)
type: "text_editor_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error)
TextEditorCodeExecutionViewResultBlock object { content, file_type, num_lines, 3 more } 
content: string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.content)
file_type: "text" or "image" or "pdf"
"text"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.file_type%5B0%5D)
"image"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.file_type%5B1%5D)
"pdf"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.file_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.file_type)
num_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.num_lines)
start_line: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.start_line)
total_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.total_lines)
type: "text_editor_code_execution_view_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block)
TextEditorCodeExecutionCreateResultBlock object { is_file_update, type } 
is_file_update: boolean
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_create_result_block.is_file_update)
type: "text_editor_code_execution_create_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_create_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_create_result_block)
TextEditorCodeExecutionStrReplaceResultBlock object { lines, new_lines, new_start, 3 more } 
lines: array of string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.lines)
new_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.new_lines)
new_start: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.new_start)
old_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.old_lines)
old_start: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.old_start)
type: "text_editor_code_execution_str_replace_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block.tool_use_id)
type: "text_editor_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block)
ToolSearchToolResultBlock object { content, tool_use_id, type } 
content: [ToolSearchToolResultError](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type }  or [ToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type } 
ToolSearchToolResultError object { error_code, error_message, type } 
error_code: [ToolSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_message)
type: "tool_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error)
ToolSearchToolSearchResultBlock object { tool_references, type } 
tool_references: array of [ToolReferenceBlock](https://platform.claude.com/docs/en/api/messages#tool_reference_block) { tool_name, type } 
tool_name: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_search_result_block.tool_references)
type: "tool_search_tool_search_result"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_search_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_search_result_block)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block.tool_use_id)
type: "tool_search_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block)
ContainerUploadBlock object { file_id, type } 
Response model for a file uploaded to the container.
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block.file_id)
type: "container_upload"
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block)
[](https://platform.claude.com/docs/en/api/messages/create#message.content)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#message.model)
role: "assistant"
Conversational role of the generated message.
This will always be `"assistant"`.
[](https://platform.claude.com/docs/en/api/messages/create#message.role)
stop_details: [RefusalStopDetails](https://platform.claude.com/docs/en/api/messages#refusal_stop_details) { category, explanation, type } 
Structured information about a refusal.
category: "cyber" or "bio" or "frontier_llm" or "reasoning_extraction"
The policy category that triggered a refusal.
"cyber"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.category%5B0%5D)
"bio"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.category%5B1%5D)
"frontier_llm"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.category%5B2%5D)
"reasoning_extraction"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.category%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.category)
explanation: string
Human-readable explanation of the refusal.
This text is not guaranteed to be stable. `null` when no explanation is available for the category.
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.explanation)
type: "refusal"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details)
stop_reason: [StopReason](https://platform.claude.com/docs/en/api/messages#stop_reason)
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
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B0%5D)
"max_tokens"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B1%5D)
"stop_sequence"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B2%5D)
"tool_use"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B3%5D)
"pause_turn"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B4%5D)
"refusal"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B5%5D)
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason)
stop_sequence: string
Which custom stop sequence was generated, if any.
This value will be a non-null string if one of your custom stop sequences was generated.
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_sequence)
type: "message"
Object type.
For Messages, this is always `"message"`.
[](https://platform.claude.com/docs/en/api/messages/create#message.type)
usage: [Usage](https://platform.claude.com/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more } 
Billing and rate-limit usage.
Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.
Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.
For example, `output_tokens` will be non-zero, even for an empty string response from Claude.
Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.
cache_creation: [CacheCreation](https://platform.claude.com/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
Breakdown of cached tokens by TTL
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/messages/create#usage.cache_creation%20%2B%20\(resource\)%20messages.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/messages/create#usage.cache_creation%20%2B%20\(resource\)%20messages.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.cache_creation)
cache_creation_input_tokens: number
The number of input tokens used to create the cache entry.
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.cache_creation_input_tokens)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.cache_read_input_tokens)
inference_geo: string
The geographic region where inference was performed for this request.
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.inference_geo)
input_tokens: number
The number of input tokens which were used.
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.input_tokens)
output_tokens: number
The number of output tokens which were used.
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.output_tokens)
output_tokens_details: [OutputTokensDetails](https://platform.claude.com/docs/en/api/messages#output_tokens_details) { thinking_tokens } 
Breakdown of output tokens by category.
`output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you.
thinking_tokens: number
Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.
Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#usage.output_tokens_details%20%2B%20\(resource\)%20messages.thinking_tokens)
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.output_tokens_details)
server_tool_use: [ServerToolUsage](https://platform.claude.com/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } 
The number of server tool requests.
web_fetch_requests: number
The number of web fetch tool requests.
[](https://platform.claude.com/docs/en/api/messages/create#usage.server_tool_use%20%2B%20\(resource\)%20messages.web_fetch_requests)
web_search_requests: number
The number of web search tool requests.
[](https://platform.claude.com/docs/en/api/messages/create#usage.server_tool_use%20%2B%20\(resource\)%20messages.web_search_requests)
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.server_tool_use)
service_tier: "standard" or "priority" or "batch"
If the request used the priority, standard, or batch tier.
"standard"
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.service_tier%5B0%5D)
"priority"
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.service_tier%5B1%5D)
"batch"
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.service_tier%5B2%5D)
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.service_tier)
[](https://platform.claude.com/docs/en/api/messages/create#message.usage)
[](https://platform.claude.com/docs/en/api/messages/create#message)
RawMessageStreamEvent = [RawMessageStartEvent](https://platform.claude.com/docs/en/api/messages#raw_message_start_event) { message, type }  or [RawMessageDeltaEvent](https://platform.claude.com/docs/en/api/messages#raw_message_delta_event) { delta, type, usage }  or [RawMessageStopEvent](https://platform.claude.com/docs/en/api/messages#raw_message_stop_event) { type }  or 3 more
RawMessageStartEvent object { message, type } 
message: [Message](https://platform.claude.com/docs/en/api/messages#message) { id, container, content, 7 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.id)
container: [Container](https://platform.claude.com/docs/en/api/messages#container) { id, expires_at } 
Information about the container used in the request (for the code execution tool)
Identifier for the container used in this request
[](https://platform.claude.com/docs/en/api/messages/create#message.container%20%2B%20\(resource\)%20messages.id)
expires_at: string
The time at which the container will expire.
[](https://platform.claude.com/docs/en/api/messages/create#message.container%20%2B%20\(resource\)%20messages.expires_at)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.container)
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

TextBlock object { citations, text, type } 
citations: array of [TextCitation](https://platform.claude.com/docs/en/api/messages#text_citation)
Citations supporting the text block.
The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.
CitationCharLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.end_char_index)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.file_id)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
CitationPageLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.end_page_number)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.file_id)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
CitationContentBlockLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.end_block_index)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.file_id)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
CitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
CitationsSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.citations)
text: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ThinkingBlock object { signature, thinking, type } 
signature: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.signature)
thinking: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.thinking)
type: "thinking"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
RedactedThinkingBlock object { data, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.data)
type: "redacted_thinking"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ToolUseBlock object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.input)
name: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.name)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ServerToolUseBlock object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.input)
name: "web_search" or "web_fetch" or "code_execution" or 4 more
"web_search"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.name%5B0%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.name%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.name%5B2%5D)
"bash_code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.name%5B3%5D)
"text_editor_code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.name%5B4%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.name%5B5%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.name%5B6%5D)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.name)
type: "server_tool_use"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
WebSearchToolResultBlock object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.caller)
content: [WebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_block_content)
WebSearchToolResultError object { error_code, type } 
error_code: [WebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"query_too_long"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
"request_too_large"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B5%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.error_code)
type: "web_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages)
array of [WebSearchResultBlock](https://platform.claude.com/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } 
encrypted_content: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.encrypted_content)
page_age: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.page_age)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.title)
type: "web_search_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_use_id)
type: "web_search_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
WebFetchToolResultBlock object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.caller)
content: [WebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type }  or [WebFetchBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url } 
WebFetchToolResultErrorBlock object { error_code, type } 
error_code: [WebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"url_too_long"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"url_not_allowed"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"url_not_in_prior_context"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"url_not_accessible"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
"unsupported_content_type"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B5%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B6%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B7%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B8%5D)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.error_code)
type: "web_fetch_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
WebFetchBlock object { content, retrieved_at, type, url } 
content: [DocumentBlock](https://platform.claude.com/docs/en/api/messages#document_block) { citations, source, title, type } 
citations: [CitationsConfig](https://platform.claude.com/docs/en/api/messages#citations_config) { enabled } 
Citation configuration for the document
enabled: boolean
[](https://platform.claude.com/docs/en/api/messages/create#document_block.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.citations)
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type } 
Base64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages)
PlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.source)
title: string
The title of the document
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.title)
type: "document"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.content)
retrieved_at: string
ISO 8601 timestamp when the content was retrieved
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.retrieved_at)
type: "web_fetch_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
url: string
Fetched content URL
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_use_id)
type: "web_fetch_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
CodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [CodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_block_content)
Code execution result with encrypted stdout for PFC + web_search results.
CodeExecutionToolResultError object { error_code, type } 
error_code: [CodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.error_code)
type: "code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages)
CodeExecutionResultBlock object { content, return_code, stderr, 2 more } 
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.content)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.stdout)
type: "code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages)
EncryptedCodeExecutionResultBlock object { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.content)
encrypted_stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.encrypted_stdout)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.stderr)
type: "encrypted_code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_use_id)
type: "code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
BashCodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [BashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type }  or [BashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more } 
BashCodeExecutionToolResultError object { error_code, type } 
error_code: [BashCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"output_file_too_large"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.error_code)
type: "bash_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
BashCodeExecutionResultBlock object { content, return_code, stderr, 2 more } 
content: array of [BashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.file_id)
type: "bash_code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.content)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.stdout)
type: "bash_code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_use_id)
type: "bash_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
TextEditorCodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [TextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type }  or [TextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more } 
TextEditorCodeExecutionToolResultError object { error_code, error_message, type } 
error_code: [TextEditorCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"file_not_found"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.error_message)
type: "text_editor_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
TextEditorCodeExecutionViewResultBlock object { content, file_type, num_lines, 3 more } 
content: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.content)
file_type: "text" or "image" or "pdf"
"text"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.file_type%5B0%5D)
"image"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.file_type%5B1%5D)
"pdf"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.file_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.file_type)
num_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.num_lines)
start_line: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.start_line)
total_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.total_lines)
type: "text_editor_code_execution_view_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
TextEditorCodeExecutionCreateResultBlock object { is_file_update, type } 
is_file_update: boolean
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.is_file_update)
type: "text_editor_code_execution_create_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
TextEditorCodeExecutionStrReplaceResultBlock object { lines, new_lines, new_start, 3 more } 
lines: array of string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.lines)
new_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.new_lines)
new_start: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.new_start)
old_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.old_lines)
old_start: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.old_start)
type: "text_editor_code_execution_str_replace_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_use_id)
type: "text_editor_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ToolSearchToolResultBlock object { content, tool_use_id, type } 
content: [ToolSearchToolResultError](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type }  or [ToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type } 
ToolSearchToolResultError object { error_code, error_message, type } 
error_code: [ToolSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.error_message)
type: "tool_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ToolSearchToolSearchResultBlock object { tool_references, type } 
tool_references: array of [ToolReferenceBlock](https://platform.claude.com/docs/en/api/messages#tool_reference_block) { tool_name, type } 
tool_name: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_references)
type: "tool_search_tool_search_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.tool_use_id)
type: "tool_search_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
ContainerUploadBlock object { file_id, type } 
Response model for a file uploaded to the container.
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.file_id)
type: "container_upload"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.content)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/messages/create#message.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.model)
role: "assistant"
Conversational role of the generated message.
This will always be `"assistant"`.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.role)
stop_details: [RefusalStopDetails](https://platform.claude.com/docs/en/api/messages#refusal_stop_details) { category, explanation, type } 
Structured information about a refusal.
category: "cyber" or "bio" or "frontier_llm" or "reasoning_extraction"
The policy category that triggered a refusal.
"cyber"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.category%5B0%5D)
"bio"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.category%5B1%5D)
"frontier_llm"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.category%5B2%5D)
"reasoning_extraction"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.category%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.category)
explanation: string
Human-readable explanation of the refusal.
This text is not guaranteed to be stable. `null` when no explanation is available for the category.
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.explanation)
type: "refusal"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_details%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.stop_details)
stop_reason: [StopReason](https://platform.claude.com/docs/en/api/messages#stop_reason)
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
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B0%5D)
"max_tokens"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B1%5D)
"stop_sequence"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B2%5D)
"tool_use"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B3%5D)
"pause_turn"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B4%5D)
"refusal"
[](https://platform.claude.com/docs/en/api/messages/create#message.stop_reason%20%2B%20\(resource\)%20messages%5B5%5D)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.stop_reason)
stop_sequence: string
Which custom stop sequence was generated, if any.
This value will be a non-null string if one of your custom stop sequences was generated.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.stop_sequence)
type: "message"
Object type.
For Messages, this is always `"message"`.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.type)
usage: [Usage](https://platform.claude.com/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more } 
Billing and rate-limit usage.
Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.
Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.
For example, `output_tokens` will be non-zero, even for an empty string response from Claude.
Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.
cache_creation: [CacheCreation](https://platform.claude.com/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
Breakdown of cached tokens by TTL
ephemeral_1h_input_tokens: number
The number of input tokens used to create the 1 hour cache entry.
[](https://platform.claude.com/docs/en/api/messages/create#usage.cache_creation%20%2B%20\(resource\)%20messages.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: number
The number of input tokens used to create the 5 minute cache entry.
[](https://platform.claude.com/docs/en/api/messages/create#usage.cache_creation%20%2B%20\(resource\)%20messages.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.cache_creation)
cache_creation_input_tokens: number
The number of input tokens used to create the cache entry.
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.cache_creation_input_tokens)
cache_read_input_tokens: number
The number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.cache_read_input_tokens)
inference_geo: string
The geographic region where inference was performed for this request.
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.inference_geo)
input_tokens: number
The number of input tokens which were used.
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.input_tokens)
output_tokens: number
The number of output tokens which were used.
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.output_tokens)
output_tokens_details: [OutputTokensDetails](https://platform.claude.com/docs/en/api/messages#output_tokens_details) { thinking_tokens } 
Breakdown of output tokens by category.
`output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you.
thinking_tokens: number
Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.
Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#usage.output_tokens_details%20%2B%20\(resource\)%20messages.thinking_tokens)
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.output_tokens_details)
server_tool_use: [ServerToolUsage](https://platform.claude.com/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } 
The number of server tool requests.
web_fetch_requests: number
The number of web fetch tool requests.
[](https://platform.claude.com/docs/en/api/messages/create#usage.server_tool_use%20%2B%20\(resource\)%20messages.web_fetch_requests)
web_search_requests: number
The number of web search tool requests.
[](https://platform.claude.com/docs/en/api/messages/create#usage.server_tool_use%20%2B%20\(resource\)%20messages.web_search_requests)
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.server_tool_use)
service_tier: "standard" or "priority" or "batch"
If the request used the priority, standard, or batch tier.
"standard"
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.service_tier%5B0%5D)
"priority"
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.service_tier%5B1%5D)
"batch"
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.service_tier%5B2%5D)
[](https://platform.claude.com/docs/en/api/messages/create#message.usage%20%2B%20\(resource\)%20messages.service_tier)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message%20%2B%20\(resource\)%20messages.usage)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.message)
type: "message_start"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_start_event)
RawMessageDeltaEvent object { delta, type, usage } 
delta: object { container, stop_details, stop_reason, stop_sequence } 
container: [Container](https://platform.claude.com/docs/en/api/messages#container) { id, expires_at } 
Information about the container used in the request (for the code execution tool)
Identifier for the container used in this request
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.container%20%2B%20\(resource\)%20messages.id)
expires_at: string
The time at which the container will expire.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.container%20%2B%20\(resource\)%20messages.expires_at)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.container)
stop_details: [RefusalStopDetails](https://platform.claude.com/docs/en/api/messages#refusal_stop_details) { category, explanation, type } 
Structured information about a refusal.
category: "cyber" or "bio" or "frontier_llm" or "reasoning_extraction"
The policy category that triggered a refusal.
"cyber"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_details%20%2B%20\(resource\)%20messages.category%5B0%5D)
"bio"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_details%20%2B%20\(resource\)%20messages.category%5B1%5D)
"frontier_llm"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_details%20%2B%20\(resource\)%20messages.category%5B2%5D)
"reasoning_extraction"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_details%20%2B%20\(resource\)%20messages.category%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_details%20%2B%20\(resource\)%20messages.category)
explanation: string
Human-readable explanation of the refusal.
This text is not guaranteed to be stable. `null` when no explanation is available for the category.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_details%20%2B%20\(resource\)%20messages.explanation)
type: "refusal"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_details%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_details)
stop_reason: [StopReason](https://platform.claude.com/docs/en/api/messages#stop_reason)
"end_turn"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_reason%20%2B%20\(resource\)%20messages%5B0%5D)
"max_tokens"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_reason%20%2B%20\(resource\)%20messages%5B1%5D)
"stop_sequence"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_reason%20%2B%20\(resource\)%20messages%5B2%5D)
"tool_use"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_reason%20%2B%20\(resource\)%20messages%5B3%5D)
"pause_turn"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_reason%20%2B%20\(resource\)%20messages%5B4%5D)
"refusal"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_reason%20%2B%20\(resource\)%20messages%5B5%5D)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_reason)
stop_sequence: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta.stop_sequence)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.delta)
type: "message_delta"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.type)
usage: [MessageDeltaUsage](https://platform.claude.com/docs/en/api/messages#message_delta_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more } 
Billing and rate-limit usage.
Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.
Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.
For example, `output_tokens` will be non-zero, even for an empty string response from Claude.
Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.
cache_creation_input_tokens: number
The cumulative number of input tokens used to create the cache entry.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.usage%20%2B%20\(resource\)%20messages.cache_creation_input_tokens)
cache_read_input_tokens: number
The cumulative number of input tokens read from the cache.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.usage%20%2B%20\(resource\)%20messages.cache_read_input_tokens)
input_tokens: number
The cumulative number of input tokens which were used.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.usage%20%2B%20\(resource\)%20messages.input_tokens)
output_tokens: number
The cumulative number of output tokens which were used.
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.usage%20%2B%20\(resource\)%20messages.output_tokens)
output_tokens_details: [OutputTokensDetails](https://platform.claude.com/docs/en/api/messages#output_tokens_details) { thinking_tokens } 
Breakdown of output tokens by category.
`output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you.
thinking_tokens: number
Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.
Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#message_delta_usage.output_tokens_details%20%2B%20\(resource\)%20messages.thinking_tokens)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.usage%20%2B%20\(resource\)%20messages.output_tokens_details)
server_tool_use: [ServerToolUsage](https://platform.claude.com/docs/en/api/messages#server_tool_usage) { web_fetch_requests, web_search_requests } 
The number of server tool requests.
web_fetch_requests: number
The number of web fetch tool requests.
[](https://platform.claude.com/docs/en/api/messages/create#message_delta_usage.server_tool_use%20%2B%20\(resource\)%20messages.web_fetch_requests)
web_search_requests: number
The number of web search tool requests.
[](https://platform.claude.com/docs/en/api/messages/create#message_delta_usage.server_tool_use%20%2B%20\(resource\)%20messages.web_search_requests)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.usage%20%2B%20\(resource\)%20messages.server_tool_use)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event.usage)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_delta_event)
RawMessageStopEvent object { type } 
type: "message_stop"
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_stop_event.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_stop_event)
RawContentBlockStartEvent object { content_block, index, type } 
content_block: [TextBlock](https://platform.claude.com/docs/en/api/messages#text_block) { citations, text, type }  or [ThinkingBlock](https://platform.claude.com/docs/en/api/messages#thinking_block) { signature, thinking, type }  or [RedactedThinkingBlock](https://platform.claude.com/docs/en/api/messages#redacted_thinking_block) { data, type }  or 9 more
Response model for a file uploaded to the container.
TextBlock object { citations, text, type } 
citations: array of [TextCitation](https://platform.claude.com/docs/en/api/messages#text_citation)
Citations supporting the text block.
The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.
CitationCharLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.end_char_index)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.file_id)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_char_location)
CitationPageLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.end_page_number)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.file_id)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_page_location)
CitationContentBlockLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.end_block_index)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.file_id)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location.type)
[](https://platform.claude.com/docs/en/api/messages/create#citation_content_block_location)
CitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location.url)
[](https://platform.claude.com/docs/en/api/messages/create#citations_web_search_result_location)
CitationsSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location.type)
[](https://platform.claude.com/docs/en/api/messages/create#citations_search_result_location)
[](https://platform.claude.com/docs/en/api/messages/create#text_block.citations)
text: string
[](https://platform.claude.com/docs/en/api/messages/create#text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#text_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_block)
ThinkingBlock object { signature, thinking, type } 
signature: string
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block.signature)
thinking: string
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block.thinking)
type: "thinking"
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#thinking_block)
RedactedThinkingBlock object { data, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#redacted_thinking_block.data)
type: "redacted_thinking"
[](https://platform.claude.com/docs/en/api/messages/create#redacted_thinking_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#redacted_thinking_block)
ToolUseBlock object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block.input)
name: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block.name)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool_use_block)
ServerToolUseBlock object { id, caller, input, 2 more } 
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.id)
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.caller)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.input)
name: "web_search" or "web_fetch" or "code_execution" or 4 more
"web_search"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B0%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B2%5D)
"bash_code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B3%5D)
"text_editor_code_execution"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B4%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B5%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name%5B6%5D)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.name)
type: "server_tool_use"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_use_block)
WebSearchToolResultBlock object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.caller)
content: [WebSearchToolResultBlockContent](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_block_content)
WebSearchToolResultError object { error_code, type } 
error_code: [WebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"query_too_long"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
"request_too_large"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B5%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.error_code)
type: "web_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages)
array of [WebSearchResultBlock](https://platform.claude.com/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } 
encrypted_content: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.encrypted_content)
page_age: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.page_age)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.title)
type: "web_search_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.tool_use_id)
type: "web_search_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_search_tool_result_block)
WebFetchToolResultBlock object { caller, content, tool_use_id, type } 
caller: [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/create#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block.caller)
content: [WebFetchToolResultErrorBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_block) { error_code, type }  or [WebFetchBlock](https://platform.claude.com/docs/en/api/messages#web_fetch_block) { content, retrieved_at, type, url } 
WebFetchToolResultErrorBlock object { error_code, type } 
error_code: [WebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"url_too_long"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"url_not_allowed"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"url_not_in_prior_context"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"url_not_accessible"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
"unsupported_content_type"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B5%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B6%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B7%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code%20%2B%20\(resource\)%20messages%5B8%5D)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.error_code)
type: "web_fetch_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_error_block)
WebFetchBlock object { content, retrieved_at, type, url } 
content: [DocumentBlock](https://platform.claude.com/docs/en/api/messages#document_block) { citations, source, title, type } 
citations: [CitationsConfig](https://platform.claude.com/docs/en/api/messages#citations_config) { enabled } 
Citation configuration for the document
enabled: boolean
[](https://platform.claude.com/docs/en/api/messages/create#document_block.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.citations)
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type } 
Base64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages)
PlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.source)
title: string
The title of the document
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.title)
type: "document"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.content)
retrieved_at: string
ISO 8601 timestamp when the content was retrieved
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.retrieved_at)
type: "web_fetch_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.type)
url: string
Fetched content URL
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block.url)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_block)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block.tool_use_id)
type: "web_fetch_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#web_fetch_tool_result_block)
CodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [CodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_block_content)
Code execution result with encrypted stdout for PFC + web_search results.
CodeExecutionToolResultError object { error_code, type } 
error_code: [CodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.error_code)
type: "code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages)
CodeExecutionResultBlock object { content, return_code, stderr, 2 more } 
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.content)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.stdout)
type: "code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages)
EncryptedCodeExecutionResultBlock object { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.content)
encrypted_stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.encrypted_stdout)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.stderr)
type: "encrypted_code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.tool_use_id)
type: "code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#code_execution_tool_result_block)
BashCodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [BashCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error) { error_code, type }  or [BashCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_result_block) { content, return_code, stderr, 2 more } 
BashCodeExecutionToolResultError object { error_code, type } 
error_code: [BashCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"output_file_too_large"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.error_code)
type: "bash_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_error)
BashCodeExecutionResultBlock object { content, return_code, stderr, 2 more } 
content: array of [BashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/messages#bash_code_execution_output_block) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_output_block.file_id)
type: "bash_code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_output_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block.content)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block.stdout)
type: "bash_code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_result_block)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block.tool_use_id)
type: "bash_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#bash_code_execution_tool_result_block)
TextEditorCodeExecutionToolResultBlock object { content, tool_use_id, type } 
content: [TextEditorCodeExecutionToolResultError](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error) { error_code, error_message, type }  or [TextEditorCodeExecutionViewResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_view_result_block) { content, file_type, num_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_create_result_block) { is_file_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_str_replace_result_block) { lines, new_lines, new_start, 3 more } 
TextEditorCodeExecutionToolResultError object { error_code, error_message, type } 
error_code: [TextEditorCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"file_not_found"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.error_message)
type: "text_editor_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_error)
TextEditorCodeExecutionViewResultBlock object { content, file_type, num_lines, 3 more } 
content: string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.content)
file_type: "text" or "image" or "pdf"
"text"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.file_type%5B0%5D)
"image"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.file_type%5B1%5D)
"pdf"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.file_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.file_type)
num_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.num_lines)
start_line: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.start_line)
total_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.total_lines)
type: "text_editor_code_execution_view_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_view_result_block)
TextEditorCodeExecutionCreateResultBlock object { is_file_update, type } 
is_file_update: boolean
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_create_result_block.is_file_update)
type: "text_editor_code_execution_create_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_create_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_create_result_block)
TextEditorCodeExecutionStrReplaceResultBlock object { lines, new_lines, new_start, 3 more } 
lines: array of string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.lines)
new_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.new_lines)
new_start: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.new_start)
old_lines: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.old_lines)
old_start: number
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.old_start)
type: "text_editor_code_execution_str_replace_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_str_replace_result_block)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block.tool_use_id)
type: "text_editor_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#text_editor_code_execution_tool_result_block)
ToolSearchToolResultBlock object { content, tool_use_id, type } 
content: [ToolSearchToolResultError](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error) { error_code, error_message, type }  or [ToolSearchToolSearchResultBlock](https://platform.claude.com/docs/en/api/messages#tool_search_tool_search_result_block) { tool_references, type } 
ToolSearchToolResultError object { error_code, error_message, type } 
error_code: [ToolSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_code)
error_message: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.error_message)
type: "tool_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_error)
ToolSearchToolSearchResultBlock object { tool_references, type } 
tool_references: array of [ToolReferenceBlock](https://platform.claude.com/docs/en/api/messages#tool_reference_block) { tool_name, type } 
tool_name: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/messages/create#tool_reference_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_search_result_block.tool_references)
type: "tool_search_tool_search_result"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_search_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_search_result_block)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block.tool_use_id)
type: "tool_search_tool_result"
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#tool_search_tool_result_block)
ContainerUploadBlock object { file_id, type } 
Response model for a file uploaded to the container.
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block.file_id)
type: "container_upload"
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block.type)
[](https://platform.claude.com/docs/en/api/messages/create#container_upload_block)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_start_event.content_block)
index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_start_event.index)
type: "content_block_start"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_start_event.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_start_event)
RawContentBlockDeltaEvent object { delta, index, type } 
delta: [RawContentBlockDelta](https://platform.claude.com/docs/en/api/messages#raw_content_block_delta)
TextDelta object { text, type } 
text: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.text)
type: "text_delta"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages)
InputJSONDelta object { partial_json, type } 
partial_json: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.partial_json)
type: "input_json_delta"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages)
CitationsDelta object { citation, type } 
citation: [CitationCharLocation](https://platform.claude.com/docs/en/api/messages#citation_char_location) { cited_text, document_index, document_title, 4 more }  or [CitationPageLocation](https://platform.claude.com/docs/en/api/messages#citation_page_location) { cited_text, document_index, document_title, 4 more }  or [CitationContentBlockLocation](https://platform.claude.com/docs/en/api/messages#citation_content_block_location) { cited_text, document_index, document_title, 4 more }  or 2 more
CitationCharLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.end_char_index)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.file_id)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages)
CitationPageLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.end_page_number)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.file_id)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages)
CitationContentBlockLocation object { cited_text, document_index, document_title, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.end_block_index)
file_id: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.file_id)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages)
CitationsWebSearchResultLocation object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages)
CitationsSearchResultLocation object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.citation)
type: "citations_delta"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages)
ThinkingDelta object { thinking, type } 
thinking: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.thinking)
type: "thinking_delta"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages)
SignatureDelta object { signature, type } 
signature: string
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.signature)
type: "signature_delta"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.delta)
index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.index)
type: "content_block_delta"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_delta_event)
RawContentBlockStopEvent object { index, type } 
index: number
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_stop_event.index)
type: "content_block_stop"
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_stop_event.type)
[](https://platform.claude.com/docs/en/api/messages/create#raw_content_block_stop_event)
[](https://platform.claude.com/docs/en/api/messages/create#raw_message_stream_event)
Create a Message
cURL

curl https://api.anthropic.com/v1/messages \
    -H 'Content-Type: application/json' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    --max-time 600 \
    -d "{
          \"max_tokens\": 1024,
          \"messages\": [
              \"content\": \"Hello, world\",
              \"role\": \"user\"
          ],
          \"model\": \"claude-opus-4-6\",
          \"system\": [
              \"text\": \"Today's date is 2024-06-01.\",
              \"type\": \"text\"
          ],
          \"temperature\": 1,
          \"thinking\": {
            \"type\": \"adaptive\"
          \"tools\": [
              \"input_schema\": {
                \"type\": \"object\",
                \"properties\": {
                  \"location\": \"bar\",
                  \"unit\": \"bar\"
                \"required\": [
                  \"location\"
                ]
              \"name\": \"name\"
          ],
          \"top_k\": 5,
          \"top_p\": 0.7
        }"

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
