<!-- source: https://platform.claude.com/docs/en/api/beta/sessions/events/list -->

# List Events
GET/v1/sessions/{session_id}/events
List Events
##### Path ParametersExpand Collapse 
session_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.session_id)
##### Query ParametersExpand Collapse 
"created_at[gt]": optional string
Return events created after this time (exclusive).
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.created_at%5Bgt%5D)
"created_at[gte]": optional string
Return events created at or after this time (inclusive).
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.created_at%5Bgte%5D)
"created_at[lt]": optional string
Return events created before this time (exclusive).
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.created_at%5Blt%5D)
"created_at[lte]": optional string
Return events created at or before this time (inclusive).
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.created_at%5Blte%5D)
limit: optional number
Query parameter for limit
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.limit)
order: optional "asc" or "desc"
Sort direction for results, ordered by created_at. Defaults to asc (chronological).
"asc"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.order%5B0%5D)
"desc"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.order%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.order)
page: optional string
Opaque pagination cursor from a previous response's next_page.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.page)
types: optional array of string
Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.types)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list.betas)
data: optional array of [BetaManagedAgentsSessionEvent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_event)
Events for the session, ordered by `created_at`.
BetaManagedAgentsUserMessageEvent object { id, content, type, processed_at } 
A user message event in the session conversation.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_message_event.id)
content: array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title } 
Array of content blocks comprising the user message.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_message_event.content)
type: "user.message"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_message_event.type)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_message_event.processed_at)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_message_event)
BetaManagedAgentsUserInterruptEvent object { id, type, processed_at, session_thread_id } 
An interrupt event that pauses agent execution and returns control to the user.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_interrupt_event.id)
type: "user.interrupt"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_interrupt_event.type)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_interrupt_event.processed_at)
session_thread_id: optional string
If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_interrupt_event.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_interrupt_event)
BetaManagedAgentsUserToolConfirmationEvent object { id, result, tool_use_id, 4 more } 
A tool confirmation event that approves or denies a pending tool execution.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_confirmation_event.id)
result: "allow" or "deny"
UserToolConfirmationResult enum
"allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_confirmation_event.result%5B0%5D)
"deny"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_confirmation_event.result%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_confirmation_event.result)
tool_use_id: string
The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_confirmation_event.tool_use_id)
type: "user.tool_confirmation"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_confirmation_event.type)
deny_message: optional string
Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_confirmation_event.deny_message)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_confirmation_event.processed_at)
session_thread_id: optional string
When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_confirmation_event.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_confirmation_event)
BetaManagedAgentsUserCustomToolResultEvent object { id, custom_tool_use_id, type, 4 more } 
Event sent by the client providing the result of a custom tool execution.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_custom_tool_result_event.id)
custom_tool_use_id: string
The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_custom_tool_result_event.custom_tool_use_id)
type: "user.custom_tool_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_custom_tool_result_event.type)
content: optional array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more } 
The result content returned by the tool.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block)
BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more } 
A block containing a web search result.
citations: [BetaManagedAgentsSearchResultCitations](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled } 
Citation settings for a search result.
enabled: boolean
Whether citations are enabled for this search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.citations%20%2B%20\(resource\)%20beta.sessions.events.enabled)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.citations)
content: array of [BetaManagedAgentsSearchResultContent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type } 
Array of text content blocks from the search result.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_content.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_content.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.content)
source: string
The URL source of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.source)
title: string
The title of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_custom_tool_result_event.content)
is_error: optional boolean
Whether the tool execution resulted in an error.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_custom_tool_result_event.is_error)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_custom_tool_result_event.processed_at)
session_thread_id: optional string
Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_custom_tool_result_event.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_custom_tool_result_event)
BetaManagedAgentsAgentCustomToolUseEvent object { id, input, name, 3 more } 
Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_custom_tool_use_event.id)
input: map[unknown]
Input parameters for the tool call.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_custom_tool_use_event.input)
name: string
Name of the custom tool being called.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_custom_tool_use_event.name)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_custom_tool_use_event.processed_at)
type: "agent.custom_tool_use"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_custom_tool_use_event.type)
session_thread_id: optional string
When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_custom_tool_use_event.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_custom_tool_use_event)
BetaManagedAgentsAgentMessageEvent object { id, content, processed_at, type } 
An agent response event in the session conversation.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_message_event.id)
content: array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type } 
Array of text blocks comprising the agent response.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_message_event.content)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_message_event.processed_at)
type: "agent.message"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_message_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_message_event)
BetaManagedAgentsAgentThinkingEvent object { id, processed_at, type } 
Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thinking_event.id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thinking_event.processed_at)
type: "agent.thinking"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thinking_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thinking_event)
BetaManagedAgentsAgentMCPToolUseEvent object { id, input, mcp_server_name, 5 more } 
Event emitted when the agent invokes a tool provided by an MCP server.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event.id)
input: map[unknown]
Input parameters for the tool call.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event.input)
mcp_server_name: string
Name of the MCP server providing the tool.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event.mcp_server_name)
name: string
Name of the MCP tool being used.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event.name)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event.processed_at)
type: "agent.mcp_tool_use"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event.type)
evaluated_permission: optional "allow" or "ask" or "deny"
AgentEvaluatedPermission enum
"allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event.evaluated_permission%5B0%5D)
"ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event.evaluated_permission%5B1%5D)
"deny"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event.evaluated_permission%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event.evaluated_permission)
session_thread_id: optional string
When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_use_event)
BetaManagedAgentsAgentMCPToolResultEvent object { id, mcp_tool_use_id, processed_at, 3 more } 
Event representing the result of an MCP tool execution.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_result_event.id)
mcp_tool_use_id: string
The id of the `agent.mcp_tool_use` event this result corresponds to.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_result_event.mcp_tool_use_id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_result_event.processed_at)
type: "agent.mcp_tool_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_result_event.type)
content: optional array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more } 
The result content returned by the tool.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block)
BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more } 
A block containing a web search result.
citations: [BetaManagedAgentsSearchResultCitations](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled } 
Citation settings for a search result.
enabled: boolean
Whether citations are enabled for this search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.citations%20%2B%20\(resource\)%20beta.sessions.events.enabled)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.citations)
content: array of [BetaManagedAgentsSearchResultContent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type } 
Array of text content blocks from the search result.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_content.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_content.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.content)
source: string
The URL source of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.source)
title: string
The title of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_result_event.content)
is_error: optional boolean
Whether the tool execution resulted in an error.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_result_event.is_error)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_mcp_tool_result_event)
BetaManagedAgentsAgentToolUseEvent object { id, input, name, 4 more } 
Event emitted when the agent invokes a built-in agent tool.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_use_event.id)
input: map[unknown]
Input parameters for the tool call.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_use_event.input)
name: string
Name of the agent tool being used.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_use_event.name)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_use_event.processed_at)
type: "agent.tool_use"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_use_event.type)
evaluated_permission: optional "allow" or "ask" or "deny"
AgentEvaluatedPermission enum
"allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_use_event.evaluated_permission%5B0%5D)
"ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_use_event.evaluated_permission%5B1%5D)
"deny"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_use_event.evaluated_permission%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_use_event.evaluated_permission)
session_thread_id: optional string
When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_use_event.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_use_event)
BetaManagedAgentsAgentToolResultEvent object { id, processed_at, tool_use_id, 3 more } 
Event representing the result of an agent tool execution.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_result_event.id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_result_event.processed_at)
tool_use_id: string
The id of the `agent.tool_use` event this result corresponds to.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_result_event.tool_use_id)
type: "agent.tool_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_result_event.type)
content: optional array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more } 
The result content returned by the tool.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block)
BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more } 
A block containing a web search result.
citations: [BetaManagedAgentsSearchResultCitations](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled } 
Citation settings for a search result.
enabled: boolean
Whether citations are enabled for this search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.citations%20%2B%20\(resource\)%20beta.sessions.events.enabled)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.citations)
content: array of [BetaManagedAgentsSearchResultContent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type } 
Array of text content blocks from the search result.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_content.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_content.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.content)
source: string
The URL source of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.source)
title: string
The title of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_result_event.content)
is_error: optional boolean
Whether the tool execution resulted in an error.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_result_event.is_error)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_tool_result_event)
BetaManagedAgentsAgentThreadMessageReceivedEvent object { id, content, from_session_thread_id, 3 more } 
Delivery event written to the target thread's input stream when an agent-to-agent message arrives.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_received_event.id)
content: array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title } 
Message content blocks.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_received_event.content)
from_session_thread_id: string
Public `sthr_` ID of the thread that sent the message.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_received_event.from_session_thread_id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_received_event.processed_at)
type: "agent.thread_message_received"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_received_event.type)
from_agent_name: optional string
Name of the callable agent this message came from. Absent when received from the primary agent.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_received_event.from_agent_name)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_received_event)
BetaManagedAgentsAgentThreadMessageSentEvent object { id, content, processed_at, 3 more } 
Observability event emitted to the sender's output stream when an agent-to-agent message is sent.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_sent_event.id)
content: array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title } 
Message content blocks.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_sent_event.content)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_sent_event.processed_at)
to_session_thread_id: string
Public `sthr_` ID of the thread the message was sent to.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_sent_event.to_session_thread_id)
type: "agent.thread_message_sent"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_sent_event.type)
to_agent_name: optional string
Name of the callable agent this message was sent to. Absent when sent to the primary agent.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_sent_event.to_agent_name)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_message_sent_event)
BetaManagedAgentsAgentThreadContextCompactedEvent object { id, processed_at, type } 
Indicates that context compaction (summarization) occurred during the session.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_context_compacted_event.id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_context_compacted_event.processed_at)
type: "agent.thread_context_compacted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_context_compacted_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_thread_context_compacted_event)
BetaManagedAgentsSessionErrorEvent object { id, error, processed_at, type } 
An error event indicating a problem occurred during session execution.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_error_event.id)
error: [BetaManagedAgentsUnknownError](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_unknown_error) { message, retry_status, type }  or [BetaManagedAgentsModelOverloadedError](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_model_overloaded_error) { message, retry_status, type }  or [BetaManagedAgentsModelRateLimitedError](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_model_rate_limited_error) { message, retry_status, type }  or 5 more
An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.
BetaManagedAgentsUnknownError object { message, retry_status, type } 
An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_unknown_error.message)
retry_status: [BetaManagedAgentsRetryStatusRetrying](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type } 
What the client should do next in response to this error.
BetaManagedAgentsRetryStatusRetrying object { type } 
The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.
type: "retrying"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying)
BetaManagedAgentsRetryStatusExhausted object { type } 
This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.
type: "exhausted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted)
BetaManagedAgentsRetryStatusTerminal object { type } 
The session encountered a terminal error and will transition to `terminated` state.
type: "terminal"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_unknown_error.retry_status)
type: "unknown_error"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_unknown_error.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_unknown_error)
BetaManagedAgentsModelOverloadedError object { message, retry_status, type } 
The model is currently overloaded. Emitted after automatic retries are exhausted.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_overloaded_error.message)
retry_status: [BetaManagedAgentsRetryStatusRetrying](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type } 
What the client should do next in response to this error.
BetaManagedAgentsRetryStatusRetrying object { type } 
The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.
type: "retrying"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying)
BetaManagedAgentsRetryStatusExhausted object { type } 
This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.
type: "exhausted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted)
BetaManagedAgentsRetryStatusTerminal object { type } 
The session encountered a terminal error and will transition to `terminated` state.
type: "terminal"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_overloaded_error.retry_status)
type: "model_overloaded_error"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_overloaded_error.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_overloaded_error)
BetaManagedAgentsModelRateLimitedError object { message, retry_status, type } 
The model request was rate-limited.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_rate_limited_error.message)
retry_status: [BetaManagedAgentsRetryStatusRetrying](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type } 
What the client should do next in response to this error.
BetaManagedAgentsRetryStatusRetrying object { type } 
The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.
type: "retrying"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying)
BetaManagedAgentsRetryStatusExhausted object { type } 
This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.
type: "exhausted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted)
BetaManagedAgentsRetryStatusTerminal object { type } 
The session encountered a terminal error and will transition to `terminated` state.
type: "terminal"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_rate_limited_error.retry_status)
type: "model_rate_limited_error"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_rate_limited_error.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_rate_limited_error)
BetaManagedAgentsModelRequestFailedError object { message, retry_status, type } 
A model request failed for a reason other than overload or rate-limiting.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_request_failed_error.message)
retry_status: [BetaManagedAgentsRetryStatusRetrying](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type } 
What the client should do next in response to this error.
BetaManagedAgentsRetryStatusRetrying object { type } 
The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.
type: "retrying"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying)
BetaManagedAgentsRetryStatusExhausted object { type } 
This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.
type: "exhausted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted)
BetaManagedAgentsRetryStatusTerminal object { type } 
The session encountered a terminal error and will transition to `terminated` state.
type: "terminal"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_request_failed_error.retry_status)
type: "model_request_failed_error"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_request_failed_error.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_request_failed_error)
BetaManagedAgentsMCPConnectionFailedError object { mcp_server_name, message, retry_status, type } 
Failed to connect to an MCP server.
mcp_server_name: string
Name of the MCP server that failed to connect.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_connection_failed_error.mcp_server_name)
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_connection_failed_error.message)
retry_status: [BetaManagedAgentsRetryStatusRetrying](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type } 
What the client should do next in response to this error.
BetaManagedAgentsRetryStatusRetrying object { type } 
The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.
type: "retrying"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying)
BetaManagedAgentsRetryStatusExhausted object { type } 
This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.
type: "exhausted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted)
BetaManagedAgentsRetryStatusTerminal object { type } 
The session encountered a terminal error and will transition to `terminated` state.
type: "terminal"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_connection_failed_error.retry_status)
type: "mcp_connection_failed_error"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_connection_failed_error.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_connection_failed_error)
BetaManagedAgentsMCPAuthenticationFailedError object { mcp_server_name, message, retry_status, type } 
Authentication to an MCP server failed.
mcp_server_name: string
Name of the MCP server that failed authentication.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_authentication_failed_error.mcp_server_name)
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_authentication_failed_error.message)
retry_status: [BetaManagedAgentsRetryStatusRetrying](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type } 
What the client should do next in response to this error.
BetaManagedAgentsRetryStatusRetrying object { type } 
The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.
type: "retrying"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying)
BetaManagedAgentsRetryStatusExhausted object { type } 
This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.
type: "exhausted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted)
BetaManagedAgentsRetryStatusTerminal object { type } 
The session encountered a terminal error and will transition to `terminated` state.
type: "terminal"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_authentication_failed_error.retry_status)
type: "mcp_authentication_failed_error"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_authentication_failed_error.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_authentication_failed_error)
BetaManagedAgentsBillingError object { message, retry_status, type } 
The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_billing_error.message)
retry_status: [BetaManagedAgentsRetryStatusRetrying](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type } 
What the client should do next in response to this error.
BetaManagedAgentsRetryStatusRetrying object { type } 
The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.
type: "retrying"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying)
BetaManagedAgentsRetryStatusExhausted object { type } 
This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.
type: "exhausted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted)
BetaManagedAgentsRetryStatusTerminal object { type } 
The session encountered a terminal error and will transition to `terminated` state.
type: "terminal"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_billing_error.retry_status)
type: "billing_error"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_billing_error.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_billing_error)
BetaManagedAgentsCredentialHostUnreachableError object { credential_id, message, retry_status, 2 more } 
An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.
credential_id: string
ID of the affected credential.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_credential_host_unreachable_error.credential_id)
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_credential_host_unreachable_error.message)
retry_status: [BetaManagedAgentsRetryStatusRetrying](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_retrying) { type }  or [BetaManagedAgentsRetryStatusExhausted](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_exhausted) { type }  or [BetaManagedAgentsRetryStatusTerminal](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_retry_status_terminal) { type } 
What the client should do next in response to this error.
BetaManagedAgentsRetryStatusRetrying object { type } 
The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.
type: "retrying"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_retrying)
BetaManagedAgentsRetryStatusExhausted object { type } 
This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.
type: "exhausted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_exhausted)
BetaManagedAgentsRetryStatusTerminal object { type } 
The session encountered a terminal error and will transition to `terminated` state.
type: "terminal"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_retry_status_terminal)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_credential_host_unreachable_error.retry_status)
type: "credential_host_unreachable_error"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_credential_host_unreachable_error.type)
vault_id: string
ID of the vault containing the affected credential.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_credential_host_unreachable_error.vault_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_credential_host_unreachable_error)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_error_event.error)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_error_event.processed_at)
type: "session.error"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_error_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_error_event)
BetaManagedAgentsSessionStatusRescheduledEvent object { id, processed_at, type } 
Indicates the session is recovering from an error state and is rescheduled for execution.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_rescheduled_event.id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_rescheduled_event.processed_at)
type: "session.status_rescheduled"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_rescheduled_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_rescheduled_event)
BetaManagedAgentsSessionStatusRunningEvent object { id, processed_at, type } 
Indicates the session is actively running and the agent is working.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_running_event.id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_running_event.processed_at)
type: "session.status_running"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_running_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_running_event)
BetaManagedAgentsSessionStatusIdleEvent object { id, processed_at, stop_reason, type } 
Indicates the agent has paused and is awaiting user input.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_idle_event.id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_idle_event.processed_at)
stop_reason: [BetaManagedAgentsSessionEndTurn](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_end_turn) { type }  or [BetaManagedAgentsSessionRequiresAction](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_requires_action) { event_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_retries_exhausted) { type } 
The agent completed its turn naturally and is ready for the next user message.
BetaManagedAgentsSessionEndTurn object { type } 
The agent completed its turn naturally and is ready for the next user message.
type: "end_turn"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_end_turn.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_end_turn)
BetaManagedAgentsSessionRequiresAction object { event_ids, type } 
The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.
event_ids: array of string
The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids)
type: "requires_action"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action)
BetaManagedAgentsSessionRetriesExhausted object { type } 
The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).
type: "retries_exhausted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_retries_exhausted.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_retries_exhausted)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_idle_event.stop_reason)
type: "session.status_idle"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_idle_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_idle_event)
BetaManagedAgentsSessionStatusTerminatedEvent object { id, processed_at, type } 
Indicates the session has terminated, either due to an error or completion.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_terminated_event.id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_terminated_event.processed_at)
type: "session.status_terminated"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_terminated_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_status_terminated_event)
BetaManagedAgentsSessionThreadCreatedEvent object { id, agent_name, processed_at, 2 more } 
Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_created_event.id)
agent_name: string
Name of the callable agent the thread runs.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_created_event.agent_name)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_created_event.processed_at)
session_thread_id: string
Public `sthr_` ID of the newly created thread.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_created_event.session_thread_id)
type: "session.thread_created"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_created_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_created_event)
BetaManagedAgentsSpanOutcomeEvaluationStartEvent object { id, iteration, outcome_id, 2 more } 
Emitted when an outcome evaluation cycle begins.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_start_event.id)
iteration: number
0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_start_event.iteration)
outcome_id: string
The `outc_` ID of the outcome being evaluated.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_start_event.outcome_id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_start_event.processed_at)
type: "span.outcome_evaluation_start"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_start_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_start_event)
BetaManagedAgentsSpanOutcomeEvaluationEndEvent object { id, explanation, iteration, 6 more } 
Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.id)
explanation: string
Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.explanation)
iteration: number
0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.iteration)
outcome_evaluation_start_id: string
The id of the corresponding `span.outcome_evaluation_start` event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.outcome_evaluation_start_id)
outcome_id: string
The `outc_` ID of the outcome being evaluated.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.outcome_id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.processed_at)
result: string
Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.result)
type: "span.outcome_evaluation_end"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.type)
usage: [BetaManagedAgentsSpanModelUsage](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_span_model_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more } 
Token usage for a single model request.
cache_creation_input_tokens: number
Tokens used to create prompt cache in this request.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.usage%20%2B%20\(resource\)%20beta.sessions.events.cache_creation_input_tokens)
cache_read_input_tokens: number
Tokens read from prompt cache in this request.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.usage%20%2B%20\(resource\)%20beta.sessions.events.cache_read_input_tokens)
input_tokens: number
Input tokens consumed by this request.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.usage%20%2B%20\(resource\)%20beta.sessions.events.input_tokens)
output_tokens: number
Output tokens generated by this request.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.usage%20%2B%20\(resource\)%20beta.sessions.events.output_tokens)
speed: optional "standard" or "fast"
Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.
"standard"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.usage%20%2B%20\(resource\)%20beta.sessions.events.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.usage%20%2B%20\(resource\)%20beta.sessions.events.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.usage%20%2B%20\(resource\)%20beta.sessions.events.speed)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event.usage)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_end_event)
BetaManagedAgentsSpanModelRequestStartEvent object { id, processed_at, type } 
Emitted when a model request is initiated by the agent.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_start_event.id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_start_event.processed_at)
type: "span.model_request_start"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_start_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_start_event)
BetaManagedAgentsSpanModelRequestEndEvent object { id, is_error, model_request_start_id, 3 more } 
Emitted when a model request completes.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.id)
is_error: boolean
Whether the model request resulted in an error.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.is_error)
model_request_start_id: string
The id of the corresponding `span.model_request_start` event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.model_request_start_id)
model_usage: [BetaManagedAgentsSpanModelUsage](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_span_model_usage) { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more } 
Token usage for a single model request.
cache_creation_input_tokens: number
Tokens used to create prompt cache in this request.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.model_usage%20%2B%20\(resource\)%20beta.sessions.events.cache_creation_input_tokens)
cache_read_input_tokens: number
Tokens read from prompt cache in this request.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.model_usage%20%2B%20\(resource\)%20beta.sessions.events.cache_read_input_tokens)
input_tokens: number
Input tokens consumed by this request.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.model_usage%20%2B%20\(resource\)%20beta.sessions.events.input_tokens)
output_tokens: number
Output tokens generated by this request.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.model_usage%20%2B%20\(resource\)%20beta.sessions.events.output_tokens)
speed: optional "standard" or "fast"
Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.
"standard"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.model_usage%20%2B%20\(resource\)%20beta.sessions.events.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.model_usage%20%2B%20\(resource\)%20beta.sessions.events.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.model_usage%20%2B%20\(resource\)%20beta.sessions.events.speed)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.model_usage)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.processed_at)
type: "span.model_request_end"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_model_request_end_event)
BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object { id, iteration, outcome_id, 2 more } 
Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_ongoing_event.id)
iteration: number
0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_ongoing_event.iteration)
outcome_id: string
The `outc_` ID of the outcome being evaluated.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_ongoing_event.outcome_id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_ongoing_event.processed_at)
type: "span.outcome_evaluation_ongoing"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_ongoing_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_span_outcome_evaluation_ongoing_event)
BetaManagedAgentsUserDefineOutcomeEvent object { id, description, max_iterations, 4 more } 
Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_define_outcome_event.id)
description: string
What the agent should produce. Copied from the input event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_define_outcome_event.description)
max_iterations: number
Evaluate-then-revise cycles before giving up. Default 3, max 20.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_define_outcome_event.max_iterations)
outcome_id: string
Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_define_outcome_event.outcome_id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_define_outcome_event.processed_at)
rubric: [BetaManagedAgentsFileRubric](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_rubric) { file_id, type }  or [BetaManagedAgentsTextRubric](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_rubric) { content, type } 
Rubric for grading the quality of an outcome.
BetaManagedAgentsFileRubric object { file_id, type } 
Rubric referenced by a file uploaded via the Files API.
file_id: string
ID of the rubric file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_rubric.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_rubric.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_rubric)
BetaManagedAgentsTextRubric object { content, type } 
Rubric content provided inline as text.
content: string
Rubric content. Plain text or markdown — the grader treats it as freeform text.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_rubric.content)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_rubric.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_rubric)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_define_outcome_event.rubric)
type: "user.define_outcome"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_define_outcome_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_define_outcome_event)
BetaManagedAgentsSessionDeletedEvent object { id, processed_at, type } 
Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_deleted_event.id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_deleted_event.processed_at)
type: "session.deleted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_deleted_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_deleted_event)
BetaManagedAgentsSessionThreadStatusRunningEvent object { id, agent_name, processed_at, 2 more } 
A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_running_event.id)
agent_name: string
Name of the agent the thread runs.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_running_event.agent_name)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_running_event.processed_at)
session_thread_id: string
Public sthr_ ID of the thread that started running.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_running_event.session_thread_id)
type: "session.thread_status_running"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_running_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_running_event)
BetaManagedAgentsSessionThreadStatusIdleEvent object { id, agent_name, processed_at, 3 more } 
A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_idle_event.id)
agent_name: string
Name of the agent the thread runs.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_idle_event.agent_name)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_idle_event.processed_at)
session_thread_id: string
Public sthr_ ID of the thread that went idle.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_idle_event.session_thread_id)
stop_reason: [BetaManagedAgentsSessionEndTurn](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_end_turn) { type }  or [BetaManagedAgentsSessionRequiresAction](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_requires_action) { event_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_retries_exhausted) { type } 
The agent completed its turn naturally and is ready for the next user message.
BetaManagedAgentsSessionEndTurn object { type } 
The agent completed its turn naturally and is ready for the next user message.
type: "end_turn"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_end_turn.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_end_turn)
BetaManagedAgentsSessionRequiresAction object { event_ids, type } 
The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.
event_ids: array of string
The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids)
type: "requires_action"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action)
BetaManagedAgentsSessionRetriesExhausted object { type } 
The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).
type: "retries_exhausted"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_retries_exhausted.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_retries_exhausted)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_idle_event.stop_reason)
type: "session.thread_status_idle"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_idle_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_idle_event)
BetaManagedAgentsSessionThreadStatusTerminatedEvent object { id, agent_name, processed_at, 2 more } 
A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_terminated_event.id)
agent_name: string
Name of the agent the thread runs.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_terminated_event.agent_name)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_terminated_event.processed_at)
session_thread_id: string
Public sthr_ ID of the thread that terminated.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_terminated_event.session_thread_id)
type: "session.thread_status_terminated"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_terminated_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_terminated_event)
BetaManagedAgentsUserToolResultEvent object { id, tool_use_id, type, 4 more } 
Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_result_event.id)
tool_use_id: string
The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_result_event.tool_use_id)
type: "user.tool_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_result_event.type)
content: optional array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title }  or [BetaManagedAgentsSearchResultBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_block) { citations, content, source, 2 more } 
The result content returned by the tool.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_document_block)
BetaManagedAgentsSearchResultBlock object { citations, content, source, 2 more } 
A block containing a web search result.
citations: [BetaManagedAgentsSearchResultCitations](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_citations) { enabled } 
Citation settings for a search result.
enabled: boolean
Whether citations are enabled for this search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.citations%20%2B%20\(resource\)%20beta.sessions.events.enabled)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.citations)
content: array of [BetaManagedAgentsSearchResultContent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_search_result_content) { text, type } 
Array of text content blocks from the search result.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_content.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_content.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.content)
source: string
The URL source of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.source)
title: string
The title of the search result.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.title)
type: "search_result"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_search_result_block)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_result_event.content)
is_error: optional boolean
Whether the tool execution resulted in an error.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_result_event.is_error)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_result_event.processed_at)
session_thread_id: optional string
Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_result_event.session_thread_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_user_tool_result_event)
BetaManagedAgentsSessionThreadStatusRescheduledEvent object { id, agent_name, processed_at, 2 more } 
A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_rescheduled_event.id)
agent_name: string
Name of the agent the thread runs.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_rescheduled_event.agent_name)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_rescheduled_event.processed_at)
session_thread_id: string
Public sthr_ ID of the thread that is retrying.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_rescheduled_event.session_thread_id)
type: "session.thread_status_rescheduled"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_rescheduled_event.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_status_rescheduled_event)
BetaManagedAgentsSessionUpdatedEvent object { id, processed_at, type, 3 more } 
Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.id)
processed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.processed_at)
type: "session.updated"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.type)
agent: optional [BetaManagedAgentsSessionAgent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_agent) { id, description, mcp_servers, 8 more } 
Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.sessions.id)
description: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.sessions.description)
mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url } 
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name)
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.sessions.mcp_servers)
model: [BetaManagedAgentsModelConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_model_config) { id, speed } 
Model identifier and configuration.
id: [BetaManagedAgentsModel](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_model)
The model that will power your agent.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more
The model that will power your agent.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B0%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B1%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B2%5D)
"claude-opus-4-6"
Most intelligent model for building agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B3%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B4%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B5%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B6%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B7%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B8%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B9%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B10%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.model%20%2B%20\(resource\)%20beta.agents.id)
speed: optional "standard" or "fast"
Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.
"standard"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.model%20%2B%20\(resource\)%20beta.agents.speed)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.sessions.model)
multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_multiagent_coordinator) { agents, type } 
Resolved coordinator topology with full agent definitions for each roster member.
agents: array of [BetaManagedAgentsSessionThreadAgent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_thread_agent) { id, description, mcp_servers, 7 more } 
Full `agent` definitions the coordinator may spawn as session threads.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.id)
description: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.description)
mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url } 
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name)
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.mcp_servers)
model: [BetaManagedAgentsModelConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_model_config) { id, speed } 
Model identifier and configuration.
id: [BetaManagedAgentsModel](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_model)
The model that will power your agent.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more
The model that will power your agent.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B0%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B1%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B2%5D)
"claude-opus-4-6"
Most intelligent model for building agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B3%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B4%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B5%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B6%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B7%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B8%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B9%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B10%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.id)
speed: optional "standard" or "fast"
Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.
"standard"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.speed)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.model)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name)
skills: array of [BetaManagedAgentsAnthropicSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill_id, type, version }  or [BetaManagedAgentsCustomSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_skill) { skill_id, type, version } 
BetaManagedAgentsAnthropicSkill object { skill_id, type, version } 
A resolved Anthropic-managed skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.skill_id)
type: "anthropic"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsCustomSkill object { skill_id, type, version } 
A resolved user-created custom skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.skill_id)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.skills)
system: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.system)
tools: array of [BetaManagedAgentsAgentToolset20260401](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default_config, type }  or [BetaManagedAgentsMCPToolset](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type }  or [BetaManagedAgentsCustomTool](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input_schema, name, type } 
BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type } 
configs: array of [BetaManagedAgentsAgentToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.enabled)
name: "bash" or "edit" or "read" or 5 more
Built-in agent tool identifier.
"bash"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B0%5D)
"edit"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B1%5D)
"read"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B2%5D)
"write"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B3%5D)
"glob"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B4%5D)
"grep"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B5%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B6%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B7%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.configs)
default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for agent tools.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.default_config)
type: "agent_toolset_20260401"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type } 
configs: array of [BetaManagedAgentsMCPToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.enabled)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.configs)
default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for all tools from an MCP server.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.default_config)
mcp_server_name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.mcp_server_name)
type: "mcp_toolset"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsCustomTool object { description, input_schema, name, type } 
A custom tool as returned in API responses.
description: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.description)
input_schema: [BetaManagedAgentsCustomToolInputSchema](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { type, properties, required } 
JSON Schema for custom tool input parameters.
type: "object"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.type)
properties: optional map[unknown]
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.properties)
required: optional array of string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.required)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.input_schema)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.tools)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
version: number
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.sessions.agents)
type: "coordinator"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.sessions.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.sessions.multiagent)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.sessions.name)
skills: array of [BetaManagedAgentsAnthropicSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill_id, type, version }  or [BetaManagedAgentsCustomSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_skill) { skill_id, type, version } 
BetaManagedAgentsAnthropicSkill object { skill_id, type, version } 
A resolved Anthropic-managed skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.skill_id)
type: "anthropic"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsCustomSkill object { skill_id, type, version } 
A resolved user-created custom skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.skill_id)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.sessions.skills)
system: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.sessions.system)
tools: array of [BetaManagedAgentsAgentToolset20260401](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default_config, type }  or [BetaManagedAgentsMCPToolset](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type }  or [BetaManagedAgentsCustomTool](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input_schema, name, type } 
BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type } 
configs: array of [BetaManagedAgentsAgentToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.enabled)
name: "bash" or "edit" or "read" or 5 more
Built-in agent tool identifier.
"bash"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name%5B0%5D)
"edit"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name%5B1%5D)
"read"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name%5B2%5D)
"write"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name%5B3%5D)
"glob"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name%5B4%5D)
"grep"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name%5B5%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name%5B6%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name%5B7%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.configs)
default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for agent tools.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.default_config)
type: "agent_toolset_20260401"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type } 
configs: array of [BetaManagedAgentsMCPToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.enabled)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.configs)
default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for all tools from an MCP server.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.default_config)
mcp_server_name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.mcp_server_name)
type: "mcp_toolset"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsCustomTool object { description, input_schema, name, type } 
A custom tool as returned in API responses.
description: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.description)
input_schema: [BetaManagedAgentsCustomToolInputSchema](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { type, properties, required } 
JSON Schema for custom tool input parameters.
type: "object"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.type)
properties: optional map[unknown]
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.properties)
required: optional array of string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.required)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.input_schema)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.name)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.sessions.tools)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.sessions.type)
version: number
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent%20%2B%20\(resource\)%20beta.sessions.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.agent)
metadata: optional map[string]
The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.metadata)
title: optional string
The session's new title. Present only when the update changed it.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event.title)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_updated_event)
BetaManagedAgentsSystemMessageEvent object { id, content, type, processed_at } 
A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.
Unique identifier for this event.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_system_message_event.id)
content: array of [BetaManagedAgentsSystemContentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_system_content_block) { text, type } 
System content blocks. Text-only.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_system_content_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_system_content_block.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_system_message_event.content)
type: "system.message"
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_system_message_event.type)
processed_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_system_message_event.processed_at)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_system_message_event)
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list)
next_page: optional string
Opaque cursor for the next page. Null when no more results.
[](https://platform.claude.com/docs/en/api/beta/sessions/events/list#list)
List Events
cURL

curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "data": [
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
          "text": "Where is my order #1234?",
          "type": "text"
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
          "text": "Let me look up order #1234 for you.",
          "type": "text"
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="

  "data": [
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
          "text": "Where is my order #1234?",
          "type": "text"
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
          "text": "Let me look up order #1234 for you.",
          "type": "text"
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
