<!-- source: https://platform.claude.com/docs/en/api/beta/sessions/create -->

# Create Session
POST/v1/sessions
Create Session
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#create.betas)
#####  Body ParametersJSONExpand Collapse 
agent: string or [BetaManagedAgentsAgentParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_params) { id, type, version } 
Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.
string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#create.agent%5B0%5D)
BetaManagedAgentsAgentParams object { id, type, version } 
Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version
The `agent` ID.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_params.id)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_params.type)
version: optional number
The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_params.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_params)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#create.agent)
environment_id: string
ID of the `environment` defining the container configuration for this session.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#create.environment_id)
metadata: optional map[string]
Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#create.metadata)
resources: optional array of [BetaManagedAgentsGitHubRepositoryResourceParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_github_repository_resource_params) { authorization_token, type, url, 2 more }  or [BetaManagedAgentsFileResourceParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_file_resource_params) { file_id, type, mount_path }  or [BetaManagedAgentsMemoryStoreResourceParam](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_memory_store_resource_param) { memory_store_id, type, access, instructions } 
Resources (e.g. repositories, files) to mount into the session's container.
BetaManagedAgentsGitHubRepositoryResourceParams object { authorization_token, type, url, 2 more } 
Mount a GitHub repository into the session's container.
authorization_token: string
GitHub authorization token used to clone the repository.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource_params.authorization_token)
type: "github_repository"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource_params.type)
url: string
Github URL of the repository
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource_params.url)
checkout: optional [BetaManagedAgentsBranchCheckout](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_branch_checkout) { name, type }  or [BetaManagedAgentsCommitCheckout](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_commit_checkout) { sha, type } 
Branch or commit to check out. Defaults to the repository's default branch.
BetaManagedAgentsBranchCheckout object { name, type } 
name: string
Branch name to check out.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_branch_checkout.name)
type: "branch"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_branch_checkout.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_branch_checkout)
BetaManagedAgentsCommitCheckout object { sha, type } 
sha: string
Full commit SHA to check out.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_commit_checkout.sha)
type: "commit"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_commit_checkout.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_commit_checkout)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource_params.checkout)
mount_path: optional string
Mount path in the container. Defaults to `/workspace/<repo-name>`.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource_params.mount_path)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource_params)
BetaManagedAgentsFileResourceParams object { file_id, type, mount_path } 
Mount a file uploaded via the Files API into the session.
file_id: string
ID of a previously uploaded file.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_file_resource_params.file_id)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_file_resource_params.type)
mount_path: optional string
Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_file_resource_params.mount_path)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_file_resource_params)
BetaManagedAgentsMemoryStoreResourceParam object { memory_store_id, type, access, instructions } 
Parameters for attaching a memory store to an agent session.
memory_store_id: string
The memory store ID (memstore_...). Must belong to the caller's organization and workspace.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource_param.memory_store_id)
type: "memory_store"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource_param.type)
access: optional "read_write" or "read_only"
Access mode for an attached memory store.
"read_write"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource_param.access%5B0%5D)
"read_only"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource_param.access%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource_param.access)
instructions: optional string
Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource_param.instructions)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource_param)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#create.resources)
title: optional string
Human-readable session title.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#create.title)
vault_ids: optional array of string
Vault IDs for stored credentials the agent can use during the session.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#create.vault_ids)
BetaManagedAgentsSession object { id, agent, archived_at, 13 more } 
A Managed Agents `session`.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.id)
agent: [BetaManagedAgentsSessionAgent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_agent) { id, description, mcp_servers, 8 more } 
Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.sessions.id)
description: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.sessions.description)
mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url } 
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name)
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.sessions.mcp_servers)
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
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B0%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B1%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B2%5D)
"claude-opus-4-6"
Most intelligent model for building agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B3%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B4%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B5%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B6%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B7%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B8%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B9%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B10%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.model%20%2B%20\(resource\)%20beta.agents.id)
speed: optional "standard" or "fast"
Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.
"standard"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.model%20%2B%20\(resource\)%20beta.agents.speed)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.sessions.model)
multiagent: [BetaManagedAgentsSessionMultiagentCoordinator](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_multiagent_coordinator) { agents, type } 
Resolved coordinator topology with full agent definitions for each roster member.
agents: array of [BetaManagedAgentsSessionThreadAgent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_thread_agent) { id, description, mcp_servers, 7 more } 
Full `agent` definitions the coordinator may spawn as session threads.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.id)
description: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.description)
mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url } 
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name)
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.mcp_servers)
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
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B0%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B1%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B2%5D)
"claude-opus-4-6"
Most intelligent model for building agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B3%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B4%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B5%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B6%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B7%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B8%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B9%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B10%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.id)
speed: optional "standard" or "fast"
Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.
"standard"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.speed)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.model)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name)
skills: array of [BetaManagedAgentsAnthropicSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill_id, type, version }  or [BetaManagedAgentsCustomSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_skill) { skill_id, type, version } 
BetaManagedAgentsAnthropicSkill object { skill_id, type, version } 
A resolved Anthropic-managed skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.skill_id)
type: "anthropic"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsCustomSkill object { skill_id, type, version } 
A resolved user-created custom skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.skill_id)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.skills)
system: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.system)
tools: array of [BetaManagedAgentsAgentToolset20260401](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default_config, type }  or [BetaManagedAgentsMCPToolset](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type }  or [BetaManagedAgentsCustomTool](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input_schema, name, type } 
BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type } 
configs: array of [BetaManagedAgentsAgentToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.enabled)
name: "bash" or "edit" or "read" or 5 more
Built-in agent tool identifier.
"bash"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B0%5D)
"edit"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B1%5D)
"read"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B2%5D)
"write"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B3%5D)
"glob"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B4%5D)
"grep"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B5%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B6%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name%5B7%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.configs)
default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for agent tools.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.default_config)
type: "agent_toolset_20260401"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type } 
configs: array of [BetaManagedAgentsMCPToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.enabled)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.configs)
default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for all tools from an MCP server.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.default_config)
mcp_server_name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.mcp_server_name)
type: "mcp_toolset"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsCustomTool object { description, input_schema, name, type } 
A custom tool as returned in API responses.
description: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.description)
input_schema: [BetaManagedAgentsCustomToolInputSchema](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { type, properties, required } 
JSON Schema for custom tool input parameters.
type: "object"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.type)
properties: optional map[unknown]
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.properties)
required: optional array of string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.required)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.input_schema)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.name)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.tools)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
version: number
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.sessions.agents)
type: "coordinator"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_agent.multiagent%20%2B%20\(resource\)%20beta.sessions.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.sessions.multiagent)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.sessions.name)
skills: array of [BetaManagedAgentsAnthropicSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill_id, type, version }  or [BetaManagedAgentsCustomSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_skill) { skill_id, type, version } 
BetaManagedAgentsAnthropicSkill object { skill_id, type, version } 
A resolved Anthropic-managed skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.skill_id)
type: "anthropic"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsCustomSkill object { skill_id, type, version } 
A resolved user-created custom skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.skill_id)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.sessions.skills)
system: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.sessions.system)
tools: array of [BetaManagedAgentsAgentToolset20260401](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default_config, type }  or [BetaManagedAgentsMCPToolset](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type }  or [BetaManagedAgentsCustomTool](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input_schema, name, type } 
BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type } 
configs: array of [BetaManagedAgentsAgentToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.enabled)
name: "bash" or "edit" or "read" or 5 more
Built-in agent tool identifier.
"bash"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name%5B0%5D)
"edit"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name%5B1%5D)
"read"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name%5B2%5D)
"write"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name%5B3%5D)
"glob"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name%5B4%5D)
"grep"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name%5B5%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name%5B6%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name%5B7%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.configs)
default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for agent tools.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.default_config)
type: "agent_toolset_20260401"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type } 
configs: array of [BetaManagedAgentsMCPToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.enabled)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.configs)
default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for all tools from an MCP server.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.default_config)
mcp_server_name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.mcp_server_name)
type: "mcp_toolset"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsCustomTool object { description, input_schema, name, type } 
A custom tool as returned in API responses.
description: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.description)
input_schema: [BetaManagedAgentsCustomToolInputSchema](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { type, properties, required } 
JSON Schema for custom tool input parameters.
type: "object"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.type)
properties: optional map[unknown]
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.properties)
required: optional array of string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.required)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.input_schema)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.name)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.sessions.tools)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.sessions.type)
version: number
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent%20%2B%20\(resource\)%20beta.sessions.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.agent)
archived_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.archived_at)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.created_at)
environment_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.environment_id)
metadata: map[string]
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.metadata)
outcome_evaluations: array of [BetaManagedAgentsOutcomeEvaluationResource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_outcome_evaluation_resource) { completed_at, description, explanation, 4 more } 
Per-outcome evaluation state. One entry per define_outcome event sent to the session.
completed_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_outcome_evaluation_resource.completed_at)
description: string
What the agent should produce.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_outcome_evaluation_resource.description)
explanation: string
Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_outcome_evaluation_resource.explanation)
iteration: number
0-indexed revision cycle the outcome is currently on.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_outcome_evaluation_resource.iteration)
outcome_id: string
Server-generated outc_ ID for this outcome.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_outcome_evaluation_resource.outcome_id)
result: string
Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_outcome_evaluation_resource.result)
type: "outcome_evaluation"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_outcome_evaluation_resource.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.outcome_evaluations)
resources: array of [BetaManagedAgentsSessionResource](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_resource)
BetaManagedAgentsGitHubRepositoryResource object { id, created_at, mount_path, 4 more } 
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource.id)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource.created_at)
mount_path: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource.mount_path)
type: "github_repository"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource.updated_at)
url: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource.url)
checkout: optional [BetaManagedAgentsBranchCheckout](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_branch_checkout) { name, type }  or [BetaManagedAgentsCommitCheckout](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_commit_checkout) { sha, type } 
BetaManagedAgentsBranchCheckout object { name, type } 
name: string
Branch name to check out.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_branch_checkout.name)
type: "branch"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_branch_checkout.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_branch_checkout)
BetaManagedAgentsCommitCheckout object { sha, type } 
sha: string
Full commit SHA to check out.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_commit_checkout.sha)
type: "commit"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_commit_checkout.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_commit_checkout)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource.checkout)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_github_repository_resource)
BetaManagedAgentsFileResource object { id, created_at, file_id, 3 more } 
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_file_resource.id)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_file_resource.created_at)
file_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_file_resource.file_id)
mount_path: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_file_resource.mount_path)
type: "file"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_file_resource.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_file_resource.updated_at)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_file_resource)
BetaManagedAgentsMemoryStoreResource object { memory_store_id, type, access, 4 more } 
A memory store attached to an agent session.
memory_store_id: string
The memory store ID (memstore_...). Must belong to the caller's organization and workspace.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource.memory_store_id)
type: "memory_store"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource.type)
access: optional "read_write" or "read_only"
Access mode for an attached memory store.
"read_write"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource.access%5B0%5D)
"read_only"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource.access%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource.access)
description: optional string
Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource.description)
instructions: optional string
Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource.instructions)
mount_path: optional string
Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource.mount_path)
name: optional string
Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource.name)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_memory_store_resource)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.resources)
stats: [BetaManagedAgentsSessionStats](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_stats) { active_seconds, duration_seconds } 
Timing statistics for a session.
active_seconds: optional number
Cumulative time in seconds the session spent in running status. Excludes idle time.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.stats%20%2B%20\(resource\)%20beta.sessions.active_seconds)
duration_seconds: optional number
Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.stats%20%2B%20\(resource\)%20beta.sessions.duration_seconds)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.stats)
status: "rescheduling" or "running" or "idle" or "terminated"
SessionStatus enum
"rescheduling"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.status%5B0%5D)
"running"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.status%5B1%5D)
"idle"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.status%5B2%5D)
"terminated"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.status%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.status)
title: string
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.title)
type: "session"
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.updated_at)
usage: [BetaManagedAgentsSessionUsage](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_usage) { cache_creation, cache_read_input_tokens, input_tokens, output_tokens } 
Cumulative token usage for a session across all turns.
cache_creation: optional [BetaManagedAgentsCacheCreationUsage](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_cache_creation_usage) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
Prompt-cache creation token usage broken down by cache lifetime.
ephemeral_1h_input_tokens: optional number
Tokens used to create 1-hour ephemeral cache entries.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_usage.cache_creation%20%2B%20\(resource\)%20beta.sessions.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: optional number
Tokens used to create 5-minute ephemeral cache entries.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session_usage.cache_creation%20%2B%20\(resource\)%20beta.sessions.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.usage%20%2B%20\(resource\)%20beta.sessions.cache_creation)
cache_read_input_tokens: optional number
Total tokens read from prompt cache.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.usage%20%2B%20\(resource\)%20beta.sessions.cache_read_input_tokens)
input_tokens: optional number
Total input tokens consumed across all turns.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.usage%20%2B%20\(resource\)%20beta.sessions.input_tokens)
output_tokens: optional number
Total output tokens generated across all turns.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.usage%20%2B%20\(resource\)%20beta.sessions.output_tokens)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.usage)
vault_ids: array of string
Vault IDs attached to the session at creation. Empty when no vaults were supplied.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.vault_ids)
deployment_id: optional string
Deployment ID when the session was created from a deployment reference. Null otherwise.
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session.deployment_id)
[](https://platform.claude.com/docs/en/api/beta/sessions/create#beta_managed_agents_session)
Create Session
cURL

curl https://api.anthropic.com/v1/sessions \
    -H 'Content-Type: application/json' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "agent": "agent_011CZkYpogX7uDKUyvBTophP",
          "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
          "title": "Order #1234 inquiry"
        }'

  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    "multiagent": {
      "agents": [
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
          ],
          "model": {
            "id": "claude-sonnet-4-6",
            "speed": "standard"
          "name": "Researcher",
          "skills": [
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
              "configs": [
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
              "type": "agent_toolset_20260401"
          ],
          "type": "agent",
          "version": 1
      ],
      "type": "coordinator"
    "name": "My First Agent",
    "skills": [
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
        "configs": [
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
        "type": "agent_toolset_20260401"
    ],
    "type": "agent",
    "version": 1
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
  ],
  "resources": [
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"

  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
    ],
    "model": {
      "id": "claude-sonnet-4-6",
      "speed": "standard"
    "multiagent": {
      "agents": [
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
          ],
          "model": {
            "id": "claude-sonnet-4-6",
            "speed": "standard"
          "name": "Researcher",
          "skills": [
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
              "configs": [
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
              "type": "agent_toolset_20260401"
          ],
          "type": "agent",
          "version": 1
      ],
      "type": "coordinator"
    "name": "My First Agent",
    "skills": [
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
        "configs": [
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
        "type": "agent_toolset_20260401"
    ],
    "type": "agent",
    "version": 1
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
  ],
  "resources": [
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
