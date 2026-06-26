<!-- source: https://platform.claude.com/docs/en/api/beta/agents/archive -->

# Archive Agent
POST/v1/agents/{agent_id}/archive
Archive Agent
##### Path ParametersExpand Collapse 
agent_id: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#archive.agent_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#archive.betas)
BetaManagedAgentsAgent object { id, archived_at, created_at, 12 more } 
A Managed Agents `agent`.
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.id)
archived_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.archived_at)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.created_at)
description: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.description)
mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url } 
name: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_server_url_definition.name)
type: "url"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_server_url_definition.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_server_url_definition.url)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.mcp_servers)
metadata: map[string]
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.metadata)
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
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B0%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B1%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B2%5D)
"claude-opus-4-6"
Most intelligent model for building agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B3%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B4%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B5%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B6%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B7%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B8%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B9%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B10%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.model%20%2B%20\(resource\)%20beta.agents.id)
speed: optional "standard" or "fast"
Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.
"standard"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.model%20%2B%20\(resource\)%20beta.agents.speed)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.model)
multiagent: [BetaManagedAgentsMultiagent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_multiagent) { agents, type } 
Resolved coordinator topology with a concrete agent roster.
agents: array of [BetaManagedAgentsAgentReference](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_reference) { id, type, version } 
Agents the coordinator may spawn as session threads, each resolved to a specific version.
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.multiagent%20%2B%20\(resource\)%20beta.agents.id)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
version: number
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.multiagent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.multiagent%20%2B%20\(resource\)%20beta.sessions.agents)
type: "coordinator"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.multiagent%20%2B%20\(resource\)%20beta.sessions.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.multiagent)
name: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.name)
skills: array of [BetaManagedAgentsAnthropicSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill_id, type, version }  or [BetaManagedAgentsCustomSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_skill) { skill_id, type, version } 
BetaManagedAgentsAnthropicSkill object { skill_id, type, version } 
A resolved Anthropic-managed skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_anthropic_skill.skill_id)
type: "anthropic"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_anthropic_skill.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_anthropic_skill.version)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_anthropic_skill)
BetaManagedAgentsCustomSkill object { skill_id, type, version } 
A resolved user-created custom skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_skill.skill_id)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_skill.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_skill.version)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_skill)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.skills)
system: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.system)
tools: array of [BetaManagedAgentsAgentToolset20260401](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default_config, type }  or [BetaManagedAgentsMCPToolset](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type }  or [BetaManagedAgentsCustomTool](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input_schema, name, type } 
BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type } 
configs: array of [BetaManagedAgentsAgentToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_tool_config.enabled)
name: "bash" or "edit" or "read" or 5 more
Built-in agent tool identifier.
"bash"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_tool_config.name%5B0%5D)
"edit"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_tool_config.name%5B1%5D)
"read"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_tool_config.name%5B2%5D)
"write"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_tool_config.name%5B3%5D)
"glob"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_tool_config.name%5B4%5D)
"grep"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_tool_config.name%5B5%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_tool_config.name%5B6%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_tool_config.name%5B7%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_tool_config.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_always_allow_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_always_allow_policy)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_always_ask_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_always_ask_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_tool_config.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_toolset20260401.configs)
default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for agent tools.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_toolset20260401.default_config)
type: "agent_toolset_20260401"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_toolset20260401.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent_toolset20260401)
BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type } 
configs: array of [BetaManagedAgentsMCPToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_tool_config.enabled)
name: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_tool_config.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_always_allow_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_always_allow_policy)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_always_ask_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_always_ask_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_tool_config.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_toolset.configs)
default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for all tools from an MCP server.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_toolset.default_config)
mcp_server_name: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_toolset.mcp_server_name)
type: "mcp_toolset"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_toolset.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_mcp_toolset)
BetaManagedAgentsCustomTool object { description, input_schema, name, type } 
A custom tool as returned in API responses.
description: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_tool.description)
input_schema: [BetaManagedAgentsCustomToolInputSchema](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { type, properties, required } 
JSON Schema for custom tool input parameters.
type: "object"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.type)
properties: optional map[unknown]
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.properties)
required: optional array of string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.required)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_tool.input_schema)
name: string
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_tool.name)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_tool.type)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_custom_tool)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.tools)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.updated_at)
version: number
The agent's current version. Starts at 1 and increments when the agent is modified.
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent.version)
[](https://platform.claude.com/docs/en/api/beta/agents/archive#beta_managed_agents_agent)
Archive Agent
cURL

curl https://api.anthropic.com/v1/agents/$AGENT_ID/archive \
    -X POST \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
  ],
  "metadata": {
    "foo": "bar"
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  "multiagent": {
    "agents": [
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
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
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1

  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
  ],
  "metadata": {
    "foo": "bar"
  "model": {
    "id": "claude-sonnet-4-6",
    "speed": "standard"
  "multiagent": {
    "agents": [
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
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
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
