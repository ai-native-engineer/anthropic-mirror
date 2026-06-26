<!-- source: https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve -->

# Get Session Thread
GET/v1/sessions/{session_id}/threads/{thread_id}
Get Session Thread
##### Path ParametersExpand Collapse 
session_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#retrieve.session_id)
thread_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#retrieve.thread_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#retrieve.betas)
BetaManagedAgentsSessionThread object { id, agent, archived_at, 8 more } 
An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.
Unique identifier for this thread.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.id)
agent: [BetaManagedAgentsSessionThreadAgent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_thread_agent) { id, description, mcp_servers, 7 more } 
Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.id)
description: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.description)
mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url } 
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name)
type: "url"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.url)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.mcp_servers)
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
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B0%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B1%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B2%5D)
"claude-opus-4-6"
Most intelligent model for building agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B3%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B4%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B5%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B6%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B7%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B8%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B9%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B10%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.id)
speed: optional "standard" or "fast"
Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.
"standard"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread_agent.model%20%2B%20\(resource\)%20beta.agents.speed)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.model)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name)
skills: array of [BetaManagedAgentsAnthropicSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill_id, type, version }  or [BetaManagedAgentsCustomSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_skill) { skill_id, type, version } 
BetaManagedAgentsAnthropicSkill object { skill_id, type, version } 
A resolved Anthropic-managed skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.skill_id)
type: "anthropic"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsCustomSkill object { skill_id, type, version } 
A resolved user-created custom skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.skill_id)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.skills)
system: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.system)
tools: array of [BetaManagedAgentsAgentToolset20260401](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default_config, type }  or [BetaManagedAgentsMCPToolset](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type }  or [BetaManagedAgentsCustomTool](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input_schema, name, type } 
BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type } 
configs: array of [BetaManagedAgentsAgentToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.enabled)
name: "bash" or "edit" or "read" or 5 more
Built-in agent tool identifier.
"bash"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name%5B0%5D)
"edit"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name%5B1%5D)
"read"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name%5B2%5D)
"write"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name%5B3%5D)
"glob"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name%5B4%5D)
"grep"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name%5B5%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name%5B6%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name%5B7%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.configs)
default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for agent tools.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.default_config)
type: "agent_toolset_20260401"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type } 
configs: array of [BetaManagedAgentsMCPToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.enabled)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.configs)
default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for all tools from an MCP server.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.default_config)
mcp_server_name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.mcp_server_name)
type: "mcp_toolset"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsCustomTool object { description, input_schema, name, type } 
A custom tool as returned in API responses.
description: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.description)
input_schema: [BetaManagedAgentsCustomToolInputSchema](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { type, properties, required } 
JSON Schema for custom tool input parameters.
type: "object"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.type)
properties: optional map[unknown]
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.properties)
required: optional array of string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.required)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.input_schema)
name: string
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.name)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.tools)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.type)
version: number
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.agent)
archived_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.archived_at)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.created_at)
parent_thread_id: string
Parent thread that spawned this thread. Null for the primary thread.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.parent_thread_id)
session_id: string
The session this thread belongs to.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.session_id)
stats: [BetaManagedAgentsSessionThreadStats](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_thread_stats) { active_seconds, duration_seconds, startup_seconds } 
Timing statistics for a session thread.
active_seconds: optional number
Cumulative time in seconds the thread spent actively running. Excludes idle time.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.stats%20%2B%20\(resource\)%20beta.sessions.threads.active_seconds)
duration_seconds: optional number
Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.stats%20%2B%20\(resource\)%20beta.sessions.threads.duration_seconds)
startup_seconds: optional number
Time in seconds for the thread to begin running. Zero for child threads, which start immediately.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.stats%20%2B%20\(resource\)%20beta.sessions.threads.startup_seconds)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.stats)
status: [BetaManagedAgentsSessionThreadStatus](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_thread_status)
SessionThreadStatus enum
"running"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.status%20%2B%20\(resource\)%20beta.sessions.threads%5B0%5D)
"idle"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.status%20%2B%20\(resource\)%20beta.sessions.threads%5B1%5D)
"rescheduling"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.status%20%2B%20\(resource\)%20beta.sessions.threads%5B2%5D)
"terminated"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.status%20%2B%20\(resource\)%20beta.sessions.threads%5B3%5D)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.status)
type: "session_thread"
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.updated_at)
usage: [BetaManagedAgentsSessionThreadUsage](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_session_thread_usage) { cache_creation, cache_read_input_tokens, input_tokens, output_tokens } 
Cumulative token usage for a session thread across all turns.
cache_creation: optional [BetaManagedAgentsCacheCreationUsage](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_cache_creation_usage) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } 
Prompt-cache creation token usage broken down by cache lifetime.
ephemeral_1h_input_tokens: optional number
Tokens used to create 1-hour ephemeral cache entries.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread_usage.cache_creation%20%2B%20\(resource\)%20beta.sessions.ephemeral_1h_input_tokens)
ephemeral_5m_input_tokens: optional number
Tokens used to create 5-minute ephemeral cache entries.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread_usage.cache_creation%20%2B%20\(resource\)%20beta.sessions.ephemeral_5m_input_tokens)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.usage%20%2B%20\(resource\)%20beta.sessions.threads.cache_creation)
cache_read_input_tokens: optional number
Total tokens read from prompt cache.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.usage%20%2B%20\(resource\)%20beta.sessions.threads.cache_read_input_tokens)
input_tokens: optional number
Total input tokens consumed across all turns.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.usage%20%2B%20\(resource\)%20beta.sessions.threads.input_tokens)
output_tokens: optional number
Total output tokens generated across all turns.
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.usage%20%2B%20\(resource\)%20beta.sessions.threads.output_tokens)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread.usage)
[](https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve#beta_managed_agents_session_thread)
Get Session Thread
cURL

curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
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
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0

  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
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
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
