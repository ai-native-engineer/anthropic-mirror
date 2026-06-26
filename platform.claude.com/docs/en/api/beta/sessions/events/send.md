<!-- source: https://platform.claude.com/docs/en/api/beta/sessions/events/send -->

# Send Events
POST/v1/sessions/{session_id}/events
Send Events
##### Path ParametersExpand Collapse 
session_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#send.session_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#send.betas)
#####  Body ParametersJSONExpand Collapse 
events: array of [BetaManagedAgentsEventParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_event_params)
Events to send to the `session`.
BetaManagedAgentsUserMessageEventParams object { content, type } 
Parameters for sending a user message to the session.
content: array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title } 
Array of content blocks for the user message.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_message_event_params.content)
type: "user.message"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_message_event_params.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_message_event_params)
BetaManagedAgentsUserInterruptEventParams object { type, session_thread_id } 
Parameters for sending an interrupt to pause the agent.
type: "user.interrupt"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_interrupt_event_params.type)
session_thread_id: optional string
If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_interrupt_event_params.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_interrupt_event_params)
BetaManagedAgentsUserToolConfirmationEventParams object { result, tool_use_id, type, deny_message } 
Parameters for confirming or denying a tool execution request.
result: "allow" or "deny"
UserToolConfirmationResult enum
"allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event_params.result%5B0%5D)
"deny"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event_params.result%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event_params.result)
tool_use_id: string
The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event_params.tool_use_id)
type: "user.tool_confirmation"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event_params.type)
deny_message: optional string
Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event_params.deny_message)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event_params)
BetaManagedAgentsUserCustomToolResultEventParams object { custom_tool_use_id, type, content, is_error } 
Parameters for providing the result of a custom tool execution.
custom_tool_use_id: string
The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event_params.custom_tool_use_id)
type: "user.custom_tool_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event_params.type)
content: optional array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more } 
The result content returned by the tool.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block)
BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more } 
A block containing a web search result.
citations: [BetaManagedAgentsSearchResultCitations](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled } 
Citation settings for a search result.
enabled: boolean
Whether citations are enabled for this search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.citations%20%2B%20\(resource\)%20beta.sessions.events.enabled)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.citations)
content: array of [BetaManagedAgentsSearchResultContent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type } 
Array of text content blocks from the search result.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_content.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_content.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.content)
source: string
The URL source of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.source)
title: string
The title of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event_params.content)
is_error: optional boolean
Whether the tool execution resulted in an error.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event_params.is_error)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event_params)
BetaManagedAgentsUserDefineOutcomeEventParams object { description, rubric, type, max_iterations } 
Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.
description: string
What the agent should produce. This is the task specification.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event_params.description)
rubric: [BetaManagedAgentsFileRubricParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_rubric_params) { file_id, type }  or [BetaManagedAgentsTextRubricParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_rubric_params) { content, type } 
Rubric for grading the quality of an outcome.
BetaManagedAgentsFileRubricParams object { file_id, type } 
Rubric referenced by a file uploaded via the Files API.
file_id: string
ID of the rubric file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_rubric_params.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_rubric_params.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_rubric_params)
BetaManagedAgentsTextRubricParams object { content, type } 
Rubric content provided inline as text.
content: string
Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_rubric_params.content)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_rubric_params.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_rubric_params)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event_params.rubric)
type: "user.define_outcome"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event_params.type)
max_iterations: optional number
Eval→revision cycles before giving up. Default 3, max 20.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event_params.max_iterations)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event_params)
BetaManagedAgentsUserToolResultEventParams object { tool_use_id, type, content, is_error } 
Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.
tool_use_id: string
The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event_params.tool_use_id)
type: "user.tool_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event_params.type)
content: optional array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more } 
The result content returned by the tool.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block)
BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more } 
A block containing a web search result.
citations: [BetaManagedAgentsSearchResultCitations](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled } 
Citation settings for a search result.
enabled: boolean
Whether citations are enabled for this search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.citations%20%2B%20\(resource\)%20beta.sessions.events.enabled)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.citations)
content: array of [BetaManagedAgentsSearchResultContent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type } 
Array of text content blocks from the search result.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_content.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_content.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.content)
source: string
The URL source of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.source)
title: string
The title of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event_params.content)
is_error: optional boolean
Whether the tool execution resulted in an error.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event_params.is_error)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event_params)
BetaManagedAgentsSystemMessageEventParams object { content, type } 
Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.
content: array of [BetaManagedAgentsSystemContentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_system_content_block) { text, type } 
System content blocks to append. Text-only.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_content_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_content_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_message_event_params.content)
type: "system.message"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_message_event_params.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_message_event_params)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#send.events)
BetaManagedAgentsSendSessionEvents object { data } 
Events that were successfully sent to the session.
data: optional array of [BetaManagedAgentsUserMessageEvent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_user_message_event) { id, content, type, processed_at }  or [BetaManagedAgentsUserInterruptEvent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_user_interrupt_event) { id, type, processed_at, session_thread_id }  or [BetaManagedAgentsUserToolConfirmationEvent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_user_tool_confirmation_event) { id, result, tool_use_id, 4 more }  or 4 more
Sent events
BetaManagedAgentsUserMessageEvent object { id, content, type, processed_at } 
A user message event in the session conversation.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_message_event.id)
content: array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title } 
Array of content blocks comprising the user message.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_message_event.content)
type: "user.message"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_message_event.type)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_message_event.processed_at)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_message_event)
BetaManagedAgentsUserInterruptEvent object { id, type, processed_at, session_thread_id } 
An interrupt event that pauses agent execution and returns control to the user.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_interrupt_event.id)
type: "user.interrupt"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_interrupt_event.type)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_interrupt_event.processed_at)
session_thread_id: optional string
If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_interrupt_event.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_interrupt_event)
BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool_use_id, 4 more } 
A tool confirmation event that approves or denies a pending tool execution.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event.id)
result: "allow" or "deny"
UserToolConfirmationResult enum
"allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event.result%5B0%5D)
"deny"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event.result%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event.result)
tool_use_id: string
The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event.tool_use_id)
type: "user.tool_confirmation"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event.type)
deny_message: optional string
Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event.deny_message)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event.processed_at)
session_thread_id: optional string
When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_confirmation_event)
BetaManagedAgentsUserCustomToolResultEvent object { id, custom_tool_use_id, type, 4 more } 
Event sent by the client providing the result of a custom tool execution.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event.id)
custom_tool_use_id: string
The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event.custom_tool_use_id)
type: "user.custom_tool_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event.type)
content: optional array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more } 
The result content returned by the tool.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block)
BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more } 
A block containing a web search result.
citations: [BetaManagedAgentsSearchResultCitations](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled } 
Citation settings for a search result.
enabled: boolean
Whether citations are enabled for this search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.citations%20%2B%20\(resource\)%20beta.sessions.events.enabled)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.citations)
content: array of [BetaManagedAgentsSearchResultContent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type } 
Array of text content blocks from the search result.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_content.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_content.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.content)
source: string
The URL source of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.source)
title: string
The title of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event.content)
is_error: optional boolean
Whether the tool execution resulted in an error.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event.is_error)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event.processed_at)
session_thread_id: optional string
Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_custom_tool_result_event)
BetaManagedAgentsUserDefineOutcomeEvent object { id, description, max_iterations, 4 more } 
Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event.id)
description: string
What the agent should produce. Copied from the input event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event.description)
max_iterations: number
Evaluate-then-revise cycles before giving up. Default 3, max 20.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event.max_iterations)
outcome_id: string
Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event.outcome_id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event.processed_at)
rubric: [BetaManagedAgentsFileRubric](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_rubric) { file_id, type }  or [BetaManagedAgentsTextRubric](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_rubric) { content, type } 
Rubric for grading the quality of an outcome.
BetaManagedAgentsFileRubric object { file_id, type } 
Rubric referenced by a file uploaded via the Files API.
file_id: string
ID of the rubric file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_rubric.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_rubric.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_rubric)
BetaManagedAgentsTextRubric object { content, type } 
Rubric content provided inline as text.
content: string
Rubric content. Plain text or markdown — the grader treats it as freeform text.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_rubric.content)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_rubric.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_rubric)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event.rubric)
type: "user.define_outcome"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_define_outcome_event)
BetaManagedAgentsUserToolResultEvent object { id, tool_use_id, type, 4 more } 
Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event.id)
tool_use_id: string
The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event.tool_use_id)
type: "user.tool_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event.type)
content: optional array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more } 
The result content returned by the tool.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_document_block)
BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more } 
A block containing a web search result.
citations: [BetaManagedAgentsSearchResultCitations](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled } 
Citation settings for a search result.
enabled: boolean
Whether citations are enabled for this search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.citations%20%2B%20\(resource\)%20beta.sessions.events.enabled)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.citations)
content: array of [BetaManagedAgentsSearchResultContent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type } 
Array of text content blocks from the search result.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_content.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_content.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.content)
source: string
The URL source of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.source)
title: string
The title of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_search_result_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event.content)
is_error: optional boolean
Whether the tool execution resulted in an error.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event.is_error)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event.processed_at)
session_thread_id: optional string
Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_user_tool_result_event)
BetaManagedAgentsSystemMessageEvent object { id, content, type, processed_at } 
A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_message_event.id)
content: array of [BetaManagedAgentsSystemContentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_system_content_block) { text, type } 
System content blocks. Text-only.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_content_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_content_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_message_event.content)
type: "system.message"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_message_event.type)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_message_event.processed_at)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_system_message_event)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_send_session_events.data)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/send#beta_managed_agents_send_session_events)
Send Events
cURL

curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
    -H 'Content-Type: application/json' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "events": [
              "content": [
                  "text": "Where is my order #1234?",
                  "type": "text"
              ],
              "type": "user.message"
          ]
        }'

  "data": [
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
          "text": "Where is my order #1234?",
          "type": "text"
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
  ]

  "data": [
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
          "text": "Where is my order #1234?",
          "type": "text"
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
  ]
