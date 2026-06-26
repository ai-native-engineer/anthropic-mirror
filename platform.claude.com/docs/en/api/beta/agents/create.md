<!-- source: https://platform.claude.com/docs/en/api/beta/agents/create -->

# Create Agent
POST/v1/agents
Create Agent
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.betas)
#####  Body ParametersJSONExpand Collapse 
model: [BetaManagedAgentsModel](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_model) or [BetaManagedAgentsModelConfigParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_model_config_params) { id, speed } 
Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-4-6`, or a `model_config` object for additional configuration control
BetaManagedAgentsModel = "claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more or string
The model that will power your agent.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more
The model that will power your agent.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D%5B0%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D%5B1%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D%5B2%5D)
"claude-opus-4-6"
Most intelligent model for building agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D%5B3%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D%5B4%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D%5B5%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D%5B6%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D%5B7%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D%5B8%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D%5B9%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D%5B10%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model)
BetaManagedAgentsModelConfigParams object { id, speed } 
An object that defines additional configuration control over model use
id: [BetaManagedAgentsModel](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_model)
The model that will power your agent.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-opus-4-8" or "claude-opus-4-7" or 8 more
The model that will power your agent.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B0%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B1%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B2%5D)
"claude-opus-4-6"
Most intelligent model for building agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B3%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B4%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B5%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B6%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B7%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B8%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B9%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B10%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id%20%2B%20\(resource\)%20beta.agents%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.id)
speed: optional "standard" or "fast"
Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.
"standard"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params.speed)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config_params)
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.model)
name: string
Human-readable name for the agent.
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.name)
description: optional string
Description of what the agent does.
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.description)
mcp_servers: optional array of [BetaManagedAgentsURLMCPServerParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_url_mcp_server_params) { name, type, url } 
MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).
name: string
Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_url_mcp_server_params.name)
type: "url"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_url_mcp_server_params.type)
url: string
Endpoint URL for the MCP server.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_url_mcp_server_params.url)
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.mcp_servers)
metadata: optional map[string]
Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.metadata)
multiagent: optional [BetaManagedAgentsMultiagentParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_multiagent_params) { agents, type } 
A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.
agents: array of [BetaManagedAgentsMultiagentRosterEntryParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_multiagent_roster_entry_params)
Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).
string
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.multiagent%5B0%5D)
BetaManagedAgentsAgentParams object { id, type, version } 
Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version
The `agent` ID.
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.multiagent.id)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.multiagent.type)
version: optional number
The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.multiagent.version)
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.multiagent)
BetaManagedAgentsMultiagentSelfParams object { type } 
Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.
type: "self"
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.multiagent.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.multiagent)
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.multiagent.agents)
type: "coordinator"
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.multiagent.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.multiagent)
skills: optional array of [BetaManagedAgentsSkillParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_skill_params)
Skills available to the agent.
BetaManagedAgentsAnthropicSkillParams object { skill_id, type, version } 
An Anthropic-managed skill.
skill_id: string
Identifier of the Anthropic skill (e.g., "xlsx").
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_anthropic_skill_params.skill_id)
type: "anthropic"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_anthropic_skill_params.type)
version: optional string
Version to pin. Defaults to latest if omitted.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_anthropic_skill_params.version)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_anthropic_skill_params)
BetaManagedAgentsCustomSkillParams object { skill_id, type, version } 
A user-created custom skill.
skill_id: string
Tagged ID of the custom skill (e.g., "skill_01XJ5...").
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_skill_params.skill_id)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_skill_params.type)
version: optional string
Version to pin. Defaults to latest if omitted.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_skill_params.version)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_skill_params)
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.skills)
system: optional string
System prompt for the agent.
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.system)
tools: optional array of [BetaManagedAgentsAgentToolset20260401Params](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset20260401_params) { type, configs, default_config }  or [BetaManagedAgentsMCPToolsetParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset_params) { mcp_server_name, type, configs, default_config }  or [BetaManagedAgentsCustomToolParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool_params) { description, input_schema, name, type } 
Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.
BetaManagedAgentsAgentToolset20260401Params object { type, configs, default_config } 
Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.
type: "agent_toolset_20260401"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401_params.type)
configs: optional array of [BetaManagedAgentsAgentToolConfigParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_tool_config_params) { name, enabled, permission_policy } 
Per-tool configuration overrides.
name: "bash" or "edit" or "read" or 5 more
Built-in agent tool identifier.
"bash"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config_params.name%5B0%5D)
"edit"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config_params.name%5B1%5D)
"read"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config_params.name%5B2%5D)
"write"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config_params.name%5B3%5D)
"glob"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config_params.name%5B4%5D)
"grep"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config_params.name%5B5%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config_params.name%5B6%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config_params.name%5B7%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config_params.name)
enabled: optional boolean
Whether this tool is enabled and available to Claude. Overrides the default_config setting.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config_params.enabled)
permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_allow_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_allow_policy)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_ask_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_ask_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config_params.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401_params.configs)
default_config: optional [BetaManagedAgentsAgentToolsetDefaultConfigParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config_params) { enabled, permission_policy } 
Default configuration for all tools in a toolset.
enabled: optional boolean
Whether tools are enabled and available to Claude by default. Defaults to true if not specified.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401_params.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401_params.default_config)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401_params)
BetaManagedAgentsMCPToolsetParams object { mcp_server_name, type, configs, default_config } 
Configuration for tools from an MCP server defined in `mcp_servers`.
mcp_server_name: string
Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset_params.mcp_server_name)
type: "mcp_toolset"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset_params.type)
configs: optional array of [BetaManagedAgentsMCPToolConfigParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_tool_config_params) { name, enabled, permission_policy } 
Per-tool configuration overrides.
name: string
Name of the MCP tool to configure. 1-128 characters.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_tool_config_params.name)
enabled: optional boolean
Whether this tool is enabled. Overrides the `default_config` setting.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_tool_config_params.enabled)
permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_allow_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_allow_policy)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_ask_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_ask_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_tool_config_params.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset_params.configs)
default_config: optional [BetaManagedAgentsMCPToolsetDefaultConfigParams](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config_params) { enabled, permission_policy } 
Default configuration for all tools from an MCP server.
enabled: optional boolean
Whether tools are enabled by default. Defaults to true if not specified.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset_params.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset_params.default_config)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset_params)
BetaManagedAgentsCustomToolParams object { description, input_schema, name, type } 
A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.
description: string
Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool_params.description)
input_schema: [BetaManagedAgentsCustomToolInputSchema](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { type, properties, required } 
JSON Schema for custom tool input parameters.
type: "object"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool_params.input_schema%20%2B%20\(resource\)%20beta.agents.type)
properties: optional map[unknown]
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool_params.input_schema%20%2B%20\(resource\)%20beta.agents.properties)
required: optional array of string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool_params.input_schema%20%2B%20\(resource\)%20beta.agents.required)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool_params.input_schema)
name: string
Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool_params.name)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool_params.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool_params)
[](https://platform.claude.com/docs/en/api/beta/agents/create#create.tools)
BetaManagedAgentsAgent object { id, archived_at, created_at, 12 more } 
A Managed Agents `agent`.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.id)
archived_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.archived_at)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.created_at)
description: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.description)
mcp_servers: array of [BetaManagedAgentsMCPServerURLDefinition](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_server_url_definition) { name, type, url } 
name: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_server_url_definition.name)
type: "url"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_server_url_definition.type)
url: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_server_url_definition.url)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.mcp_servers)
metadata: map[string]
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.metadata)
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
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B0%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B1%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B2%5D)
"claude-opus-4-6"
Most intelligent model for building agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B3%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B4%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B5%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B6%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B7%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B8%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B9%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D%5B10%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_model_config.id%20%2B%20\(resource\)%20beta.agents%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.model%20%2B%20\(resource\)%20beta.agents.id)
speed: optional "standard" or "fast"
Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.
"standard"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B0%5D)
"fast"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.model%20%2B%20\(resource\)%20beta.agents.speed%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.model%20%2B%20\(resource\)%20beta.agents.speed)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.model)
multiagent: [BetaManagedAgentsMultiagent](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_multiagent) { agents, type } 
Resolved coordinator topology with a concrete agent roster.
agents: array of [BetaManagedAgentsAgentReference](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_reference) { id, type, version } 
Agents the coordinator may spawn as session threads, each resolved to a specific version.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.multiagent%20%2B%20\(resource\)%20beta.agents.id)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.multiagent%20%2B%20\(resource\)%20beta.agents.type)
version: number
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.multiagent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.multiagent%20%2B%20\(resource\)%20beta.sessions.agents)
type: "coordinator"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.multiagent%20%2B%20\(resource\)%20beta.sessions.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.multiagent)
name: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.name)
skills: array of [BetaManagedAgentsAnthropicSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_anthropic_skill) { skill_id, type, version }  or [BetaManagedAgentsCustomSkill](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_skill) { skill_id, type, version } 
BetaManagedAgentsAnthropicSkill object { skill_id, type, version } 
A resolved Anthropic-managed skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_anthropic_skill.skill_id)
type: "anthropic"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_anthropic_skill.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_anthropic_skill.version)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_anthropic_skill)
BetaManagedAgentsCustomSkill object { skill_id, type, version } 
A resolved user-created custom skill.
skill_id: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_skill.skill_id)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_skill.type)
version: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_skill.version)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_skill)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.skills)
system: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.system)
tools: array of [BetaManagedAgentsAgentToolset20260401](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset20260401) { configs, default_config, type }  or [BetaManagedAgentsMCPToolset](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset) { configs, default_config, mcp_server_name, type }  or [BetaManagedAgentsCustomTool](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool) { description, input_schema, name, type } 
BetaManagedAgentsAgentToolset20260401 object { configs, default_config, type } 
configs: array of [BetaManagedAgentsAgentToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config.enabled)
name: "bash" or "edit" or "read" or 5 more
Built-in agent tool identifier.
"bash"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config.name%5B0%5D)
"edit"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config.name%5B1%5D)
"read"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config.name%5B2%5D)
"write"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config.name%5B3%5D)
"glob"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config.name%5B4%5D)
"grep"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config.name%5B5%5D)
"web_fetch"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config.name%5B6%5D)
"web_search"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config.name%5B7%5D)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_allow_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_allow_policy)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_ask_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_ask_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_tool_config.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401.configs)
default_config: [BetaManagedAgentsAgentToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for agent tools.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401.default_config)
type: "agent_toolset_20260401"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent_toolset20260401)
BetaManagedAgentsMCPToolset object { configs, default_config, mcp_server_name, type } 
configs: array of [BetaManagedAgentsMCPToolConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_tool_config) { enabled, name, permission_policy } 
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_tool_config.enabled)
name: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_tool_config.name)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_allow_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_allow_policy)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_ask_policy.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_always_ask_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_tool_config.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset.configs)
default_config: [BetaManagedAgentsMCPToolsetDefaultConfig](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_mcp_toolset_default_config) { enabled, permission_policy } 
Resolved default configuration for all tools from an MCP server.
enabled: boolean
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.enabled)
permission_policy: [BetaManagedAgentsAlwaysAllowPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_allow_policy) { type }  or [BetaManagedAgentsAlwaysAskPolicy](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_always_ask_policy) { type } 
Permission policy for tool execution.
BetaManagedAgentsAlwaysAllowPolicy object { type } 
Tool calls are automatically approved without user confirmation.
type: "always_allow"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
BetaManagedAgentsAlwaysAskPolicy object { type } 
Tool calls require user confirmation before execution.
type: "always_ask"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset.default_config%20%2B%20\(resource\)%20beta.agents.permission_policy)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset.default_config)
mcp_server_name: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset.mcp_server_name)
type: "mcp_toolset"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_mcp_toolset)
BetaManagedAgentsCustomTool object { description, input_schema, name, type } 
A custom tool as returned in API responses.
description: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool.description)
input_schema: [BetaManagedAgentsCustomToolInputSchema](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_custom_tool_input_schema) { type, properties, required } 
JSON Schema for custom tool input parameters.
type: "object"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.type)
properties: optional map[unknown]
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.properties)
required: optional array of string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool.input_schema%20%2B%20\(resource\)%20beta.agents.required)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool.input_schema)
name: string
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool.name)
type: "custom"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool.type)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_custom_tool)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.tools)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.updated_at)
version: number
The agent's current version. Starts at 1 and increments when the agent is modified.
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent.version)
[](https://platform.claude.com/docs/en/api/beta/agents/create#beta_managed_agents_agent)
Create Agent
cURL

curl https://api.anthropic.com/v1/agents \
    -H 'Content-Type: application/json' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d "{
          \"model\": \"claude-sonnet-4-6\",
          \"name\": \"My First Agent\",
          \"description\": \"A general-purpose starter agent.\",
          \"metadata\": {
            \"foo\": \"bar\"
          \"system\": \"You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.\",
          \"tools\": [
              \"type\": \"agent_toolset_20260401\"
          ]
        }"

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
