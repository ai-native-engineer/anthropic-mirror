<!-- source: https://platform.claude.com/docs/en/api/messages/count_tokens -->

# Count tokens in a Message
POST/v1/messages/count_tokens
Count the number of tokens in a Message.
The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.
Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)
#####  Body ParametersJSONExpand Collapse 
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
[](https://platform.claude.com/docs/en/api/messages/count_tokens#message_param.content%5B0%5D)
array of [ContentBlockParam](https://platform.claude.com/docs/en/api/messages#content_block_param)
TextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param)
ImageBlockParam object { source, type, cache_control } 
source: [Base64ImageSource](https://platform.claude.com/docs/en/api/messages#base64_image_source) { data, media_type, type }  or [URLImageSource](https://platform.claude.com/docs/en/api/messages#url_image_source) { type, url } 
Base64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source)
URLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param)
DocumentBlockParam object { source, type, cache_control, 3 more } 
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type }  or [ContentBlockSource](https://platform.claude.com/docs/en/api/messages#content_block_source) { content, type }  or [URLPDFSource](https://platform.claude.com/docs/en/api/messages#url_pdf_source) { type, url } 
Base64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_pdf_source.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_pdf_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_pdf_source.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_pdf_source)
PlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#plain_text_source.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#plain_text_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#plain_text_source.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#plain_text_source)
ContentBlockSource object { content, type } 
content: string or array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#content_block_source.content%5B0%5D)
ContentBlockSourceContent = array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
TextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param)
ImageBlockParam object { source, type, cache_control } 
source: [Base64ImageSource](https://platform.claude.com/docs/en/api/messages#base64_image_source) { data, media_type, type }  or [URLImageSource](https://platform.claude.com/docs/en/api/messages#url_image_source) { type, url } 
Base64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source)
URLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#content_block_source.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#content_block_source.content)
type: "content"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#content_block_source.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#content_block_source)
URLPDFSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_pdf_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_pdf_source.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_pdf_source)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.source)
type: "document"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.citations)
context: optional string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.context)
title: optional string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.title)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param)
SearchResultBlockParam object { content, source, title, 3 more } 
content: array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.content)
source: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.source)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param)
ThinkingBlockParam object { signature, thinking, type } 
signature: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#thinking_block_param.signature)
thinking: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#thinking_block_param.thinking)
type: "thinking"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#thinking_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#thinking_block_param)
RedactedThinkingBlockParam object { data, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#redacted_thinking_block_param.data)
type: "redacted_thinking"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#redacted_thinking_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#redacted_thinking_block_param)
ToolUseBlockParam object { id, input, name, 3 more } 
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_use_block_param.id)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_use_block_param.input)
name: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_use_block_param.name)
type: "tool_use"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_use_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_use_block_param.cache_control)
caller: optional [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_use_block_param.caller)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_use_block_param)
ToolResultBlockParam object { tool_use_id, type, cache_control, 2 more } 
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param.tool_use_id)
type: "tool_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param.cache_control)
content: optional string or array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }  or [ImageBlockParam](https://platform.claude.com/docs/en/api/messages#image_block_param) { source, type, cache_control }  or [SearchResultBlockParam](https://platform.claude.com/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more }  or 2 more
string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param.content%5B0%5D)
array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations }  or [ImageBlockParam](https://platform.claude.com/docs/en/api/messages#image_block_param) { source, type, cache_control }  or [SearchResultBlockParam](https://platform.claude.com/docs/en/api/messages#search_result_block_param) { content, source, title, 3 more }  or 2 more
TextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param)
ImageBlockParam object { source, type, cache_control } 
source: [Base64ImageSource](https://platform.claude.com/docs/en/api/messages#base64_image_source) { data, media_type, type }  or [URLImageSource](https://platform.claude.com/docs/en/api/messages#url_image_source) { type, url } 
Base64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source)
URLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param)
SearchResultBlockParam object { content, source, title, 3 more } 
content: array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.content)
source: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.source)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#search_result_block_param)
DocumentBlockParam object { source, type, cache_control, 3 more } 
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type }  or [ContentBlockSource](https://platform.claude.com/docs/en/api/messages#content_block_source) { content, type }  or [URLPDFSource](https://platform.claude.com/docs/en/api/messages#url_pdf_source) { type, url } 
Base64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_pdf_source.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_pdf_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_pdf_source.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_pdf_source)
PlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#plain_text_source.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#plain_text_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#plain_text_source.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#plain_text_source)
ContentBlockSource object { content, type } 
content: string or array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#content_block_source.content%5B0%5D)
ContentBlockSourceContent = array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
TextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param)
ImageBlockParam object { source, type, cache_control } 
source: [Base64ImageSource](https://platform.claude.com/docs/en/api/messages#base64_image_source) { data, media_type, type }  or [URLImageSource](https://platform.claude.com/docs/en/api/messages#url_image_source) { type, url } 
Base64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#base64_image_source)
URLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_image_source)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.source)
type: "image"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#content_block_source.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#content_block_source.content)
type: "content"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#content_block_source.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#content_block_source)
URLPDFSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_pdf_source.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_pdf_source.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#url_pdf_source)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.source)
type: "document"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.citations)
context: optional string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.context)
title: optional string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.title)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param)
ToolReferenceBlockParam object { tool_name, type, cache_control } 
Tool reference block that can be included in tool_result content.
tool_name: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param.content)
is_error: optional boolean
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param.is_error)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_result_block_param)
ServerToolUseBlockParam object { id, input, name, 3 more } 
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.id)
input: map[unknown]
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.input)
name: "web_search" or "web_fetch" or "code_execution" or 4 more
"web_search"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.name%5B0%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.name%5B1%5D)
"code_execution"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.name%5B2%5D)
"bash_code_execution"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.name%5B3%5D)
"text_editor_code_execution"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.name%5B4%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.name%5B5%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.name%5B6%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.name)
type: "server_tool_use"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.cache_control)
caller: optional [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param.caller)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_use_block_param)
WebSearchToolResultBlockParam object { content, tool_use_id, type, 2 more } 
content: [WebSearchToolResultBlockParamContent](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_block_param_content)
WebSearchToolResultBlockItem = array of [WebSearchResultBlockParam](https://platform.claude.com/docs/en/api/messages#web_search_result_block_param) { encrypted_content, title, type, 2 more } 
encrypted_content: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.encrypted_content)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.title)
type: "web_search_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.url)
page_age: optional string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.page_age)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages%5B0%5D)
WebSearchToolRequestError object { error_code, type } 
error_code: [WebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#web_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"query_too_long"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
"request_too_large"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_request_error.error_code%20%2B%20\(resource\)%20messages%5B5%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.error_code)
type: "web_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.tool_use_id)
type: "web_search_tool_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.cache_control)
caller: optional [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param.caller)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_result_block_param)
WebFetchToolResultBlockParam object { content, tool_use_id, type, 2 more } 
content: [WebFetchToolResultErrorBlockParam](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_block_param) { error_code, type }  or [WebFetchBlockParam](https://platform.claude.com/docs/en/api/messages#web_fetch_block_param) { content, type, url, retrieved_at } 
WebFetchToolResultErrorBlockParam object { error_code, type } 
error_code: [WebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#web_fetch_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"url_too_long"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"url_not_allowed"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"url_not_in_prior_context"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"url_not_accessible"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
"unsupported_content_type"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B5%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B6%5D)
"max_uses_exceeded"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B7%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param.error_code%20%2B%20\(resource\)%20messages%5B8%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param.error_code)
type: "web_fetch_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_error_block_param)
WebFetchBlockParam object { content, type, url, retrieved_at } 
content: [DocumentBlockParam](https://platform.claude.com/docs/en/api/messages#document_block_param) { source, type, cache_control, 3 more } 
source: [Base64PDFSource](https://platform.claude.com/docs/en/api/messages#base64_pdf_source) { data, media_type, type }  or [PlainTextSource](https://platform.claude.com/docs/en/api/messages#plain_text_source) { data, media_type, type }  or [ContentBlockSource](https://platform.claude.com/docs/en/api/messages#content_block_source) { content, type }  or [URLPDFSource](https://platform.claude.com/docs/en/api/messages#url_pdf_source) { type, url } 
Base64PDFSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.data)
media_type: "application/pdf"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
PlainTextSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.data)
media_type: "text/plain"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
ContentBlockSource object { content, type } 
content: string or array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.content%5B0%5D)
ContentBlockSourceContent = array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/messages#content_block_source_content)
TextBlockParam object { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.citations)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
ImageBlockParam object { source, type, cache_control } 
source: [Base64ImageSource](https://platform.claude.com/docs/en/api/messages#base64_image_source) { data, media_type, type }  or [URLImageSource](https://platform.claude.com/docs/en/api/messages#url_image_source) { type, url } 
Base64ImageSource object { data, media_type, type } 
data: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.data)
media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"
"image/jpeg"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type%5B0%5D)
"image/png"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type%5B1%5D)
"image/gif"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type%5B2%5D)
"image/webp"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
URLImageSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.source)
type: "image"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#image_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.content)
type: "content"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
URLPDFSource object { type, url } 
type: "url"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.source)
type: "document"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/count_tokens#document_block_param.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.citations)
context: optional string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.context)
title: optional string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content%20%2B%20\(resource\)%20messages.title)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.content)
type: "web_fetch_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.type)
url: string
Fetched content URL
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.url)
retrieved_at: optional string
ISO 8601 timestamp when the content was retrieved
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param.retrieved_at)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_block_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_block_param.tool_use_id)
type: "web_fetch_tool_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_block_param.cache_control)
caller: optional [DirectCaller](https://platform.claude.com/docs/en/api/messages#direct_caller) { type }  or [ServerToolCaller](https://platform.claude.com/docs/en/api/messages#server_tool_caller) { tool_id, type }  or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/messages#server_tool_caller_20260120) { tool_id, type } 
Tool invocation directly from the model.
DirectCaller object { type } 
Tool invocation directly from the model.
type: "direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#direct_caller.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#direct_caller)
ServerToolCaller object { tool_id, type } 
Tool invocation generated by a server-side tool.
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller.tool_id)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller)
ServerToolCaller20260120 object { tool_id, type } 
tool_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120.tool_id)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#server_tool_caller_20260120)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_block_param.caller)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_result_block_param)
CodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [CodeExecutionToolResultBlockParamContent](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_block_param_content)
Code execution result with encrypted stdout for PFC + web_search results.
CodeExecutionToolResultErrorParam object { error_code, type } 
error_code: [CodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.error_code)
type: "code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages)
CodeExecutionResultBlockParam object { content, return_code, stderr, 2 more } 
content: array of [CodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/messages#code_execution_output_block_param) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.content)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.stdout)
type: "code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages)
EncryptedCodeExecutionResultBlockParam object { content, encrypted_stdout, return_code, 2 more } 
Code execution result with encrypted stdout for PFC + web_search results.
content: array of [CodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/messages#code_execution_output_block_param) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.file_id)
type: "code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.content)
encrypted_stdout: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.encrypted_stdout)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.stderr)
type: "encrypted_code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content%20%2B%20\(resource\)%20messages)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.tool_use_id)
type: "code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_result_block_param)
BashCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [BashCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error_param) { error_code, type }  or [BashCodeExecutionResultBlockParam](https://platform.claude.com/docs/en/api/messages#bash_code_execution_result_block_param) { content, return_code, stderr, 2 more } 
BashCodeExecutionToolResultErrorParam object { error_code, type } 
error_code: [BashCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#bash_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"output_file_too_large"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_error_param.error_code)
type: "bash_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_error_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_error_param)
BashCodeExecutionResultBlockParam object { content, return_code, stderr, 2 more } 
content: array of [BashCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/messages#bash_code_execution_output_block_param) { file_id, type } 
file_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_output_block_param.file_id)
type: "bash_code_execution_output"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_output_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_result_block_param.content)
return_code: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_result_block_param.return_code)
stderr: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_result_block_param.stderr)
stdout: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_result_block_param.stdout)
type: "bash_code_execution_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_result_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_result_block_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_block_param.tool_use_id)
type: "bash_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#bash_code_execution_tool_result_block_param)
TextEditorCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [TextEditorCodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error_param) { error_code, type, error_message }  or [TextEditorCodeExecutionViewResultBlockParam](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_view_result_block_param) { content, file_type, type, 3 more }  or [TextEditorCodeExecutionCreateResultBlockParam](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_create_result_block_param) { is_file_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlockParam](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_str_replace_result_block_param) { type, lines, new_lines, 3 more } 
TextEditorCodeExecutionToolResultErrorParam object { error_code, type, error_message } 
error_code: [TextEditorCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#text_editor_code_execution_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
"file_not_found"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_error_param.error_code)
type: "text_editor_code_execution_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_error_param.type)
error_message: optional string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_error_param.error_message)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_error_param)
TextEditorCodeExecutionViewResultBlockParam object { content, file_type, type, 3 more } 
content: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_view_result_block_param.content)
file_type: "text" or "image" or "pdf"
"text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_view_result_block_param.file_type%5B0%5D)
"image"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_view_result_block_param.file_type%5B1%5D)
"pdf"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_view_result_block_param.file_type%5B2%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_view_result_block_param.file_type)
type: "text_editor_code_execution_view_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_view_result_block_param.type)
num_lines: optional number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_view_result_block_param.num_lines)
start_line: optional number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_view_result_block_param.start_line)
total_lines: optional number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_view_result_block_param.total_lines)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_view_result_block_param)
TextEditorCodeExecutionCreateResultBlockParam object { is_file_update, type } 
is_file_update: boolean
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_create_result_block_param.is_file_update)
type: "text_editor_code_execution_create_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_create_result_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_create_result_block_param)
TextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new_lines, 3 more } 
type: "text_editor_code_execution_str_replace_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_str_replace_result_block_param.type)
lines: optional array of string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_str_replace_result_block_param.lines)
new_lines: optional number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_str_replace_result_block_param.new_lines)
new_start: optional number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_str_replace_result_block_param.new_start)
old_lines: optional number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_str_replace_result_block_param.old_lines)
old_start: optional number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_str_replace_result_block_param.old_start)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_str_replace_result_block_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_block_param.tool_use_id)
type: "text_editor_code_execution_tool_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_editor_code_execution_tool_result_block_param)
ToolSearchToolResultBlockParam object { content, tool_use_id, type, cache_control } 
content: [ToolSearchToolResultErrorParam](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error_param) { error_code, type, error_message }  or [ToolSearchToolSearchResultBlockParam](https://platform.claude.com/docs/en/api/messages#tool_search_tool_search_result_block_param) { tool_references, type } 
ToolSearchToolResultErrorParam object { error_code, type, error_message } 
error_code: [ToolSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/messages#tool_search_tool_result_error_code)
"invalid_tool_input"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B0%5D)
"unavailable"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B1%5D)
"too_many_requests"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B2%5D)
"execution_time_exceeded"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_error_param.error_code%20%2B%20\(resource\)%20messages%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_error_param.error_code)
type: "tool_search_tool_result_error"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_error_param.type)
error_message: optional string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_error_param.error_message)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_error_param)
ToolSearchToolSearchResultBlockParam object { tool_references, type } 
tool_references: array of [ToolReferenceBlockParam](https://platform.claude.com/docs/en/api/messages#tool_reference_block_param) { tool_name, type, cache_control } 
tool_name: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.tool_name)
type: "tool_reference"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_reference_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_search_result_block_param.tool_references)
type: "tool_search_tool_search_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_search_result_block_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_search_result_block_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_block_param.content)
tool_use_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_block_param.tool_use_id)
type: "tool_search_tool_result"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_result_block_param)
ContainerUploadBlockParam object { file_id, type, cache_control } 
A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.
file_id: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#container_upload_block_param.file_id)
type: "container_upload"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#container_upload_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#container_upload_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#container_upload_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#container_upload_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#container_upload_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#container_upload_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#container_upload_block_param)
MidConversationSystemBlockParam object { content, type, cache_control } 
System instructions that appear mid-conversation.
Use this block to provide or update system-level instructions at a specific point in the conversation, rather than only via the top-level `system` parameter.
content: array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } 
System instruction text blocks.
text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#mid_conversation_system_block_param.content)
type: "mid_conv_system"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#mid_conversation_system_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#mid_conversation_system_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#mid_conversation_system_block_param.cache_control)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#mid_conversation_system_block_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#message_param.content%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#message_param.content)
role: "user" or "assistant" or "system"
"user"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#message_param.role%5B0%5D)
"assistant"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#message_param.role%5B1%5D)
"system"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#message_param.role%5B2%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#message_param.role)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.messages)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.model)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.cache_control.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.cache_control.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.cache_control.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.cache_control.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.cache_control)
output_config: optional [OutputConfig](https://platform.claude.com/docs/en/api/messages#output_config) { effort, format } 
Configuration options for the model's output, such as the output format.
effort: optional "low" or "medium" or "high" or 2 more
All possible effort levels.
"low"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.output_config.effort%5B0%5D)
"medium"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.output_config.effort%5B1%5D)
"high"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.output_config.effort%5B2%5D)
"xhigh"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.output_config.effort%5B3%5D)
"max"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.output_config.effort%5B4%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.output_config.effort)
format: optional [JSONOutputFormat](https://platform.claude.com/docs/en/api/messages#json_output_format) { schema, type } 
A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
schema: map[unknown]
The JSON schema of the format
[](https://platform.claude.com/docs/en/api/messages/count_tokens#output_config.format%20%2B%20\(resource\)%20messages.schema)
type: "json_schema"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#output_config.format%20%2B%20\(resource\)%20messages.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.output_config.format)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.output_config)
system: optional string or array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } 
System prompt.
A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).
string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.system%5B0%5D)
array of [TextBlockParam](https://platform.claude.com/docs/en/api/messages#text_block_param) { text, type, cache_control, citations } 
text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.text)
type: "text"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.type)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.cache_control)
citations: optional array of [TextCitationParam](https://platform.claude.com/docs/en/api/messages#text_citation_param)
CitationCharLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.document_title)
end_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.end_char_index)
start_char_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.start_char_index)
type: "char_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_char_location_param)
CitationPageLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.document_title)
end_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.end_page_number)
start_page_number: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.start_page_number)
type: "page_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_page_location_param)
CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.cited_text)
document_index: number
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_index)
document_title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.document_title)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.end_block_index)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.start_block_index)
type: "content_block_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_content_block_location_param)
CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more } 
cited_text: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.cited_text)
encrypted_index: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.encrypted_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.title)
type: "web_search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.type)
url: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param.url)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_web_search_result_location_param)
CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more } 
cited_text: string
The full text of the cited block range, concatenated.
Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.cited_text)
end_block_index: number
Exclusive 0-based end index of the cited block range in the source's `content` array.
Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.end_block_index)
search_result_index: number
0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.
Counted separately from `document_index`; server-side web search results are not included in this count.
minimum0
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.search_result_index)
source: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.source)
start_block_index: number
0-based index of the first cited block in the source's `content` array.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.start_block_index)
title: string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.title)
type: "search_result_location"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#citation_search_result_location_param)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#text_block_param.citations)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.system%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.system)
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
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking.budget_tokens)
type: "enabled"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking.type)
display: optional "summarized" or "omitted"
Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.
"summarized"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking.display%5B0%5D)
"omitted"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking.display%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking.display)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking)
ThinkingConfigDisabled object { type } 
type: "disabled"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking)
ThinkingConfigAdaptive object { type, display } 
type: "adaptive"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking.type)
display: optional "summarized" or "omitted"
Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.
"summarized"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking.display%5B0%5D)
"omitted"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking.display%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking.display)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.thinking)
tool_choice: optional [ToolChoice](https://platform.claude.com/docs/en/api/messages#tool_choice)
How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.
ToolChoiceAuto object { type, disable_parallel_tool_use } 
The model will automatically decide whether to use tools.
type: "auto"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice.type)
disable_parallel_tool_use: optional boolean
Whether to disable parallel tool use.
Defaults to `false`. If set to `true`, the model will output at most one tool use.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice.disable_parallel_tool_use)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice)
ToolChoiceAny object { type, disable_parallel_tool_use } 
The model will use any available tools.
type: "any"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice.type)
disable_parallel_tool_use: optional boolean
Whether to disable parallel tool use.
Defaults to `false`. If set to `true`, the model will output exactly one tool use.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice.disable_parallel_tool_use)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice)
ToolChoiceTool object { name, type, disable_parallel_tool_use } 
The model will use the specified tool with `tool_choice.name`.
name: string
The name of the tool to use.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice.name)
type: "tool"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice.type)
disable_parallel_tool_use: optional boolean
Whether to disable parallel tool use.
Defaults to `false`. If set to `true`, the model will output exactly one tool use.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice.disable_parallel_tool_use)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice)
ToolChoiceNone object { type } 
The model will not be allowed to use tools.
type: "none"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tool_choice)
tools: optional array of [MessageCountTokensTool](https://platform.claude.com/docs/en/api/messages#message_count_tokens_tool)
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
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.input_schema.type)
properties: optional map[unknown]
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.input_schema.properties)
required: optional array of string
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.input_schema.required)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.input_schema)
name: string
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
maxLength128
minLength1
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.name)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.defer_loading)
description: optional string
Description of what this tool does.
Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.description)
eager_input_streaming: optional boolean
Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.eager_input_streaming)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.strict)
type: optional "custom"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool.type)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool)
ToolBash20250124 object { name, type, allowed_callers, 4 more } 
name: "bash"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.name)
type: "bash_20250124"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_bash_20250124)
CodeExecutionTool20250522 object { name, type, allowed_callers, 3 more } 
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.name)
type: "code_execution_20250522"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250522)
CodeExecutionTool20250825 object { name, type, allowed_callers, 3 more } 
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.name)
type: "code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20250825)
CodeExecutionTool20260120 object { name, type, allowed_callers, 3 more } 
Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.name)
type: "code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260120)
CodeExecutionTool20260521 object { name, type, allowed_callers, 3 more } 
Code execution tool with REPL state persistence.
name: "code_execution"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.name)
type: "code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#code_execution_tool_20260521)
MemoryTool20250818 object { name, type, allowed_callers, 4 more } 
name: "memory"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.name)
type: "memory_20250818"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#memory_tool_20250818)
ToolTextEditor20250124 object { name, type, allowed_callers, 4 more } 
name: "str_replace_editor"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.name)
type: "text_editor_20250124"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250124)
ToolTextEditor20250429 object { name, type, allowed_callers, 4 more } 
name: "str_replace_based_edit_tool"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.name)
type: "text_editor_20250429"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.input_examples)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250429)
ToolTextEditor20250728 object { name, type, allowed_callers, 5 more } 
name: "str_replace_based_edit_tool"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.name)
type: "text_editor_20250728"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.defer_loading)
input_examples: optional array of map[unknown]
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.input_examples)
max_characters: optional number
Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.max_characters)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_text_editor_20250728)
WebSearchTool20250305 object { name, type, allowed_callers, 7 more } 
name: "web_search"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.name)
type: "web_search_20250305"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.allowed_callers)
allowed_domains: optional array of string
If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.allowed_domains)
blocked_domains: optional array of string
If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.blocked_domains)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.defer_loading)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.strict)
user_location: optional [UserLocation](https://platform.claude.com/docs/en/api/messages#user_location) { type, city, country, 2 more } 
Parameters for the user's location. Used to provide more relevant search results.
type: "approximate"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.user_location%20%2B%20\(resource\)%20messages.type)
city: optional string
The city of the user.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.user_location%20%2B%20\(resource\)%20messages.city)
country: optional string
The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.user_location%20%2B%20\(resource\)%20messages.country)
region: optional string
The region of the user.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.user_location%20%2B%20\(resource\)%20messages.region)
timezone: optional string
The [IANA timezone](https://nodatime.org/TimeZones) of the user.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.user_location%20%2B%20\(resource\)%20messages.timezone)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305.user_location)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20250305)
WebFetchTool20250910 object { name, type, allowed_callers, 8 more } 
name: "web_fetch"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.name)
type: "web_fetch_20250910"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.allowed_callers)
allowed_domains: optional array of string
List of domains to allow fetching from
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.allowed_domains)
blocked_domains: optional array of string
List of domains to block fetching from
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.blocked_domains)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
Citations configuration for fetched documents. Citations are disabled by default.
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.citations)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.defer_loading)
max_content_tokens: optional number
Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.max_content_tokens)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20250910)
WebSearchTool20260209 object { name, type, allowed_callers, 7 more } 
name: "web_search"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.name)
type: "web_search_20260209"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.allowed_callers)
allowed_domains: optional array of string
If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.allowed_domains)
blocked_domains: optional array of string
If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.blocked_domains)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.defer_loading)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.strict)
user_location: optional [UserLocation](https://platform.claude.com/docs/en/api/messages#user_location) { type, city, country, 2 more } 
Parameters for the user's location. Used to provide more relevant search results.
type: "approximate"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.user_location%20%2B%20\(resource\)%20messages.type)
city: optional string
The city of the user.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.user_location%20%2B%20\(resource\)%20messages.city)
country: optional string
The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.user_location%20%2B%20\(resource\)%20messages.country)
region: optional string
The region of the user.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.user_location%20%2B%20\(resource\)%20messages.region)
timezone: optional string
The [IANA timezone](https://nodatime.org/TimeZones) of the user.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.user_location%20%2B%20\(resource\)%20messages.timezone)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209.user_location)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_search_tool_20260209)
WebFetchTool20260209 object { name, type, allowed_callers, 8 more } 
name: "web_fetch"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.name)
type: "web_fetch_20260209"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.allowed_callers)
allowed_domains: optional array of string
List of domains to allow fetching from
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.allowed_domains)
blocked_domains: optional array of string
List of domains to block fetching from
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.blocked_domains)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
Citations configuration for fetched documents. Citations are disabled by default.
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.citations)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.defer_loading)
max_content_tokens: optional number
Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.max_content_tokens)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260209)
WebFetchTool20260309 object { name, type, allowed_callers, 9 more } 
Web fetch tool with use_cache parameter for bypassing cached content.
name: "web_fetch"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.name)
type: "web_fetch_20260309"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.allowed_callers)
allowed_domains: optional array of string
List of domains to allow fetching from
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.allowed_domains)
blocked_domains: optional array of string
List of domains to block fetching from
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.blocked_domains)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.cache_control)
citations: optional [CitationsConfigParam](https://platform.claude.com/docs/en/api/messages#citations_config_param) { enabled } 
Citations configuration for fetched documents. Citations are disabled by default.
enabled: optional boolean
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.citations%20%2B%20\(resource\)%20messages.enabled)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.citations)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.defer_loading)
max_content_tokens: optional number
Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.max_content_tokens)
max_uses: optional number
Maximum number of times the tool can be used in the API request.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.max_uses)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.strict)
use_cache: optional boolean
Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309.use_cache)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#web_fetch_tool_20260309)
ToolSearchToolBm25_20251119 object { name, type, allowed_callers, 3 more } 
name: "tool_search_tool_bm25"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.name)
type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"
"tool_search_tool_bm25_20251119"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.type%5B0%5D)
"tool_search_tool_bm25"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.type%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_bm25_20251119)
ToolSearchToolRegex20251119 object { name, type, allowed_callers, 3 more } 
name: "tool_search_tool_regex"
Name of the tool.
This is how the tool will be called by the model and in `tool_use` blocks.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.name)
type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"
"tool_search_tool_regex_20251119"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.type%5B0%5D)
"tool_search_tool_regex"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.type%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.type)
allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"
"direct"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.allowed_callers.items%5B0%5D)
"code_execution_20250825"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.allowed_callers.items%5B1%5D)
"code_execution_20260120"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.allowed_callers.items%5B2%5D)
"code_execution_20260521"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.allowed_callers.items%5B3%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.allowed_callers)
cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/messages#cache_control_ephemeral) { type, ttl } 
Create a cache control breakpoint at this content block.
type: "ephemeral"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20messages.type)
ttl: optional "5m" or "1h"
The time-to-live for the cache control breakpoint.
This may be one the following values:
  * `5m`: 5 minutes
  * `1h`: 1 hour

Defaults to `5m`.
"5m"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl%5B0%5D)
"1h"
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl%5B1%5D)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.cache_control%20%2B%20\(resource\)%20messages.ttl)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.cache_control)
defer_loading: optional boolean
If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.defer_loading)
strict: optional boolean
When true, guarantees schema validation on tool names and inputs
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119.strict)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#tool_search_tool_regex_20251119)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#count_tokens.tools)
MessageTokensCount object { input_tokens } 
input_tokens: number
The total number of tokens across the provided list of messages, system prompt, and tools.
[](https://platform.claude.com/docs/en/api/messages/count_tokens#message_tokens_count.input_tokens)
[](https://platform.claude.com/docs/en/api/messages/count_tokens#message_tokens_count)
Count tokens in a Message
cURL

curl https://api.anthropic.com/v1/messages/count_tokens \
    -H 'Content-Type: application/json' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d "{
          \"messages\": [
              \"content\": \"Hello, world\",
              \"role\": \"user\"
          ],
          \"model\": \"claude-opus-4-6\",
          \"system\": [
              \"text\": \"Today's date is 2024-06-01.\",
              \"type\": \"text\"
          ],
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
          ]
        }"

  "input_tokens": 2095

  "input_tokens": 2095
