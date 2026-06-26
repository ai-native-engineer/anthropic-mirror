<!-- source: https://platform.claude.com/docs/en/api/beta/deployments/update -->

# Update Deployment
POST/v1/deployments/{deployment_id}
Update Deployment
##### Path ParametersExpand Collapse 
deployment_id: string
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.deployment_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.betas)
#####  Body ParametersJSONExpand Collapse 
agent: optional string or [BetaManagedAgentsAgentParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_params) { id, type, version } 
Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.
string
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.agent%5B0%5D)
BetaManagedAgentsAgentParams object { id, type, version } 
Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version
The `agent` ID.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_agent_params.id)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_agent_params.type)
version: optional number
The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_agent_params.version)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_agent_params)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.agent)
description: optional string
Description. Omit to preserve; send empty string or null to clear.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.description)
environment_id: optional string
ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.environment_id)
initial_events: optional array of [BetaManagedAgentsDeploymentInitialEventParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_deployment_initial_event_params)
Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.
BetaManagedAgentsUserMessageEventParams object { content, type } 
Parameters for sending a user message to the session.
content: array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title } 
Array of content blocks for the user message.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_document_block)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_user_message_event_params.content)
type: "user.message"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_user_message_event_params.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_user_message_event_params)
BetaManagedAgentsUserDefineOutcomeEventParams object { description, rubric, type, max_iterations } 
Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.
description: string
What the agent should produce. This is the task specification.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_user_define_outcome_event_params.description)
rubric: [BetaManagedAgentsFileRubricParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_rubric_params) { file_id, type }  or [BetaManagedAgentsTextRubricParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_rubric_params) { content, type } 
Rubric for grading the quality of an outcome.
BetaManagedAgentsFileRubricParams object { file_id, type } 
Rubric referenced by a file uploaded via the Files API.
file_id: string
ID of the rubric file.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_rubric_params.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_rubric_params.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_rubric_params)
BetaManagedAgentsTextRubricParams object { content, type } 
Rubric content provided inline as text.
content: string
Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_rubric_params.content)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_rubric_params.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_rubric_params)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_user_define_outcome_event_params.rubric)
type: "user.define_outcome"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_user_define_outcome_event_params.type)
max_iterations: optional number
Eval→revision cycles before giving up. Default 3, max 20.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_user_define_outcome_event_params.max_iterations)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_user_define_outcome_event_params)
BetaManagedAgentsSystemMessageEventParams object { content, type } 
Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.
content: array of [BetaManagedAgentsSystemContentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_system_content_block) { text, type } 
System content blocks to append. Text-only.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_system_content_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_system_content_block.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_system_message_event_params.content)
type: "system.message"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_system_message_event_params.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_system_message_event_params)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.initial_events)
metadata: optional map[string]
Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.metadata)
name: optional string
Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.name)
resources: optional array of [BetaManagedAgentsGitHubRepositoryResourceParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_github_repository_resource_params) { authorization_token, type, url, 2 more }  or [BetaManagedAgentsFileResourceParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_resource_params) { file_id, type, mount_path }  or [BetaManagedAgentsMemoryStoreResourceParam](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_memory_store_resource_param) { memory_store_id, type, access, instructions } 
Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.
BetaManagedAgentsGitHubRepositoryResourceParams object { authorization_token, type, url, 2 more } 
Mount a GitHub repository into the session's container.
authorization_token: string
GitHub authorization token used to clone the repository.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_github_repository_resource_params.authorization_token)
type: "github_repository"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_github_repository_resource_params.type)
url: string
Github URL of the repository
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_github_repository_resource_params.url)
checkout: optional [BetaManagedAgentsBranchCheckout](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_branch_checkout) { name, type }  or [BetaManagedAgentsCommitCheckout](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_commit_checkout) { sha, type } 
Branch or commit to check out. Defaults to the repository's default branch.
BetaManagedAgentsBranchCheckout object { name, type } 
name: string
Branch name to check out.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_branch_checkout.name)
type: "branch"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_branch_checkout.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_branch_checkout)
BetaManagedAgentsCommitCheckout object { sha, type } 
sha: string
Full commit SHA to check out.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_commit_checkout.sha)
type: "commit"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_commit_checkout.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_commit_checkout)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_github_repository_resource_params.checkout)
mount_path: optional string
Mount path in the container. Defaults to `/workspace/<repo-name>`.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_github_repository_resource_params.mount_path)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_github_repository_resource_params)
BetaManagedAgentsFileResourceParams object { file_id, type, mount_path } 
Mount a file uploaded via the Files API into the session.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_resource_params.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_resource_params.type)
mount_path: optional string
Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_resource_params.mount_path)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_resource_params)
BetaManagedAgentsMemoryStoreResourceParam object { memory_store_id, type, access, instructions } 
Parameters for attaching a memory store to an agent session.
memory_store_id: string
The memory store ID (memstore_...). Must belong to the caller's organization and workspace.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_param.memory_store_id)
type: "memory_store"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_param.type)
access: optional "read_write" or "read_only"
Access mode for an attached memory store.
"read_write"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_param.access%5B0%5D)
"read_only"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_param.access%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_param.access)
instructions: optional string
Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_param.instructions)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_param)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.resources)
schedule: optional [BetaManagedAgentsScheduleParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_schedule_params) { expression, timezone, type } 
5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.
expression: string
5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.schedule.expression)
timezone: string
Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.schedule.timezone)
type: "cron"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.schedule.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.schedule)
vault_ids: optional array of string
Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#update.vault_ids)
BetaManagedAgentsDeployment object { id, agent, archived_at, 13 more } 
A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.
Unique identifier for this deployment.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.id)
agent: [BetaManagedAgentsAgentReference](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_reference) { id, type, version } 
A resolved agent reference with a concrete version.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.agent%20%2B%20\(resource\)%20beta.agents.id)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.agent%20%2B%20\(resource\)%20beta.agents.type)
version: number
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.agent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.agent)
archived_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.archived_at)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.created_at)
description: string
Description of what the deployment does.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.description)
environment_id: string
ID of the `environment` where sessions run.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.environment_id)
initial_events: array of [BetaManagedAgentsDeploymentInitialEvent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_deployment_initial_event)
Events sent to each session immediately after creation.
BetaManagedAgentsDeploymentUserMessageEvent object { content, type } 
A user message sent to the session.
content: array of [BetaManagedAgentsTextBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_block) { text, type }  or [BetaManagedAgentsImageBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_image_block) { source, type }  or [BetaManagedAgentsDocumentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_document_block) { source, type, context, title } 
Array of content blocks for the user message.
BetaManagedAgentsTextBlock object { text, type } 
Regular text content.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_block.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_block)
BetaManagedAgentsImageBlock object { source, type } 
Image content specified directly as base64 data or as a reference via a URL.
source: [BetaManagedAgentsBase64ImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_image_source) { data, media_type, type }  or [BetaManagedAgentsURLImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_image_source) { type, url }  or [BetaManagedAgentsFileImageSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_image_source) { file_id, type } 
Union type for image source variants.
BetaManagedAgentsBase64ImageSource object { data, media_type, type } 
Base64-encoded image data.
data: string
Base64-encoded image data.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_image_source.data)
media_type: string
MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_image_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_image_source)
BetaManagedAgentsURLImageSource object { type, url } 
Image referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_image_source.type)
url: string
URL of the image to fetch.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_image_source.url)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_image_source)
BetaManagedAgentsFileImageSource object { file_id, type } 
Image referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_image_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_image_source.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_image_source)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_image_block.source)
type: "image"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_image_block.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_image_block)
BetaManagedAgentsDocumentBlock object { source, type, context, title } 
Document content, either specified directly as base64 data, as text, or as a reference via a URL.
source: [BetaManagedAgentsBase64DocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_base64_document_source) { data, media_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_plain_text_document_source) { data, media_type, type }  or [BetaManagedAgentsURLDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_document_source) { type, url }  or [BetaManagedAgentsFileDocumentSource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_document_source) { file_id, type } 
Union type for document source variants.
BetaManagedAgentsBase64DocumentSource object { data, media_type, type } 
Base64-encoded document data.
data: string
Base64-encoded document data.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_document_source.data)
media_type: string
MIME type of the document (e.g., "application/pdf").
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_document_source.media_type)
type: "base64"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_base64_document_source)
BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type } 
Plain text document content.
data: string
The plain text content.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_plain_text_document_source.data)
media_type: "text/plain"
MIME type of the text content. Must be "text/plain".
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_plain_text_document_source.media_type)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_plain_text_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_plain_text_document_source)
BetaManagedAgentsURLDocumentSource object { type, url } 
Document referenced by URL.
type: "url"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_document_source.type)
url: string
URL of the document to fetch.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_document_source.url)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_url_document_source)
BetaManagedAgentsFileDocumentSource object { file_id, type } 
Document referenced by file ID.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_document_source.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_document_source.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_document_source)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_document_block.source)
type: "document"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_document_block.type)
context: optional string
Additional context about the document for the model.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_document_block.context)
title: optional string
The title of the document.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_document_block.title)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_document_block)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment_user_message_event.content)
type: "user.message"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment_user_message_event.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment_user_message_event)
BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations } 
An outcome the agent should work toward. The agent begins work on receipt.
description: string
What the agent should produce. This is the task specification.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment_user_define_outcome_event.description)
rubric: [BetaManagedAgentsFileRubric](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_rubric) { file_id, type }  or [BetaManagedAgentsTextRubric](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_text_rubric) { content, type } 
Rubric for grading the quality of an outcome.
BetaManagedAgentsFileRubric object { file_id, type } 
Rubric referenced by a file uploaded via the Files API.
file_id: string
ID of the rubric file.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_rubric.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_rubric.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_rubric)
BetaManagedAgentsTextRubric object { content, type } 
Rubric content provided inline as text.
content: string
Rubric content. Plain text or markdown — the grader treats it as freeform text.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_rubric.content)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_rubric.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_text_rubric)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment_user_define_outcome_event.rubric)
type: "user.define_outcome"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment_user_define_outcome_event.type)
max_iterations: optional number
Eval→revision cycles before giving up. Default 3, max 20.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment_user_define_outcome_event.max_iterations)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment_user_define_outcome_event)
BetaManagedAgentsDeploymentSystemMessageEvent object { content, type } 
Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.
content: array of [BetaManagedAgentsSystemContentBlock](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_system_content_block) { text, type } 
System content blocks to append. Text-only.
text: string
The text content.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_system_content_block.text)
type: "text"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_system_content_block.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment_system_message_event.content)
type: "system.message"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment_system_message_event.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment_system_message_event)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.initial_events)
metadata: map[string]
Arbitrary key-value metadata. Maximum 16 pairs.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.metadata)
name: string
Human-readable name.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.name)
paused_reason: [BetaManagedAgentsDeploymentPausedReason](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_deployment_paused_reason)
Why a deployment is paused. Non-null exactly when `status` is `paused`.
BetaManagedAgentsManualDeploymentPausedReason object { type } 
The caller invoked the pause endpoint on the deployment.
type: "manual"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.paused_reason%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.paused_reason%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsErrorDeploymentPausedReason object { error, type } 
A scheduled fire recorded a failed run whose error auto-pauses the deployment.
error: [BetaManagedAgentsDeploymentPausedReasonError](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_deployment_paused_reason_error)
The error that triggered an auto-pause. Matches the failed run's `error.type`.
BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type } 
The deployment's environment was archived.
type: "environment_archived_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type } 
The deployment's agent was archived.
type: "agent_archived_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type } 
The deployment's environment no longer exists.
type: "environment_not_found_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type } 
A vault referenced by the deployment no longer exists.
type: "vault_not_found_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type } 
A file resource referenced by the deployment no longer exists.
type: "file_not_found_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type } 
A referenced resource no longer exists and its kind was not reported.
type: "session_resource_not_found_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type } 
The deployment's workspace was archived.
type: "workspace_archived_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type } 
The deployment's organization is disabled.
type: "organization_disabled_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type } 
A memory store referenced by the deployment is archived.
type: "memory_store_archived_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type } 
A skill referenced by the deployment's agent no longer exists.
type: "skill_not_found_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type } 
A vault referenced by the deployment is archived.
type: "vault_archived_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsUnknownDeploymentPausedReasonError object { type } 
An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.
type: "unknown_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type } 
The deployment configures resources, but its environment is self-hosted and cannot mount them.
type: "self_hosted_resources_unsupported_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type } 
An MCP server host used by the deployment's agent is blocked by the environment's network policy.
type: "mcp_egress_blocked_error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20\(resource\)%20beta.deployments)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.paused_reason%20%2B%20\(resource\)%20beta.deployments.error)
type: "error"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.paused_reason%20%2B%20\(resource\)%20beta.deployments.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.paused_reason%20%2B%20\(resource\)%20beta.deployments)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.paused_reason)
resources: array of [BetaManagedAgentsSessionResourceConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_resource_config)
Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.
BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path } 
A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.
type: "github_repository"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_github_repository_resource_config.type)
url: string
Github URL of the repository
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_github_repository_resource_config.url)
checkout: optional [BetaManagedAgentsBranchCheckout](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_branch_checkout) { name, type }  or [BetaManagedAgentsCommitCheckout](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_commit_checkout) { sha, type } 
Branch or commit to check out. Defaults to the repository's default branch.
BetaManagedAgentsBranchCheckout object { name, type } 
name: string
Branch name to check out.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_branch_checkout.name)
type: "branch"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_branch_checkout.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_branch_checkout)
BetaManagedAgentsCommitCheckout object { sha, type } 
sha: string
Full commit SHA to check out.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_commit_checkout.sha)
type: "commit"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_commit_checkout.type)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_commit_checkout)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_github_repository_resource_config.checkout)
mount_path: optional string
Mount path in the container. Defaults to `/workspace/<repo-name>`.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_github_repository_resource_config.mount_path)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_github_repository_resource_config)
BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path } 
A file mounted into each session's container.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_resource_config.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_resource_config.type)
mount_path: optional string
Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_resource_config.mount_path)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_file_resource_config)
BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions } 
A memory store attached to each session created from this deployment.
memory_store_id: string
The memory store ID (memstore_...). Must belong to the caller's organization and workspace.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_config.memory_store_id)
type: "memory_store"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_config.type)
access: optional "read_write" or "read_only"
Access mode for an attached memory store.
"read_write"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_config.access%5B0%5D)
"read_only"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_config.access%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_config.access)
instructions: optional string
Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_config.instructions)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_memory_store_resource_config)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.resources)
schedule: [BetaManagedAgentsSchedule](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_schedule) { expression, timezone, type, 2 more } 
5-field POSIX cron schedule with computed runtime timestamps.
expression: string
5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.schedule%20%2B%20\(resource\)%20beta.deployments.expression)
timezone: string
IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.schedule%20%2B%20\(resource\)%20beta.deployments.timezone)
type: "cron"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.schedule%20%2B%20\(resource\)%20beta.deployments.type)
last_run_at: optional string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.schedule%20%2B%20\(resource\)%20beta.deployments.last_run_at)
upcoming_runs_at: optional array of string
Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.schedule%20%2B%20\(resource\)%20beta.deployments.upcoming_runs_at)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.schedule)
status: [BetaManagedAgentsDeploymentStatus](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_deployment_status)
Lifecycle status of a deployment.
"active"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.status%20%2B%20\(resource\)%20beta.deployments%5B0%5D)
"paused"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.status%20%2B%20\(resource\)%20beta.deployments%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.status)
type: "deployment"
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.updated_at)
vault_ids: array of string
Vault IDs supplying stored credentials for sessions created from this deployment.
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment.vault_ids)
[](https://platform.claude.com/docs/en/api/beta/deployments/update#beta_managed_agents_deployment)
Update Deployment
cURL

curl https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'

  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
      "content": [
          "text": "Where is my order #1234?",
          "type": "text"
      ],
      "type": "user.message"
  ],
  "metadata": {
    "foo": "string"
  "name": "name",
  "paused_reason": {
    "type": "manual"
  "resources": [
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      "mount_path": "mount_path"
  ],
  "schedule": {
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]

  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "environment_id": "environment_id",
  "initial_events": [
      "content": [
          "text": "Where is my order #1234?",
          "type": "text"
      ],
      "type": "user.message"
  ],
  "metadata": {
    "foo": "string"
  "name": "name",
  "paused_reason": {
    "type": "manual"
  "resources": [
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      "mount_path": "mount_path"
  ],
  "schedule": {
    "expression": "x",
    "timezone": "x",
    "type": "cron",
    "last_run_at": "2019-12-27T18:11:19.117Z",
    "upcoming_runs_at": [
      "2019-12-27T18:11:19.117Z"
    ]
  "status": "active",
  "type": "deployment",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "vault_ids": [
    "string"
  ]
