<!-- source: https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve -->

# Get Deployment Run
GET/v1/deployment_runs/{deployment_run_id}
Get Deployment Run
##### Path ParametersExpand Collapse 
deployment_run_id: string
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#retrieve.deployment_run_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#retrieve.betas)
BetaManagedAgentsDeploymentRun object { id, agent, created_at, 5 more } 
A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.
Unique identifier for this run (`drun_...`).
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.id)
agent: [BetaManagedAgentsAgentReference](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_reference) { id, type, version } 
A resolved agent reference with a concrete version.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.agent%20%2B%20\(resource\)%20beta.agents.id)
type: "agent"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.agent%20%2B%20\(resource\)%20beta.agents.type)
version: number
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.agent%20%2B%20\(resource\)%20beta.agents.version)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.agent)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.created_at)
deployment_id: string
ID of the deployment that produced this run.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.deployment_id)
error: [BetaManagedAgentsEnvironmentArchivedRunError](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_environment_archived_run_error) { message, type }  or [BetaManagedAgentsAgentArchivedRunError](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_agent_archived_run_error) { message, type }  or [BetaManagedAgentsEnvironmentNotFoundRunError](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_environment_not_found_run_error) { message, type }  or 13 more
Why the run failed to create a session. The type identifies the failure; message is human-readable detail.
BetaManagedAgentsEnvironmentArchivedRunError object { message, type } 
The deployment's environment was archived.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_environment_archived_run_error.message)
type: "environment_archived_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_environment_archived_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_environment_archived_run_error)
BetaManagedAgentsAgentArchivedRunError object { message, type } 
The deployment's agent was archived.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_agent_archived_run_error.message)
type: "agent_archived_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_agent_archived_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_agent_archived_run_error)
BetaManagedAgentsEnvironmentNotFoundRunError object { message, type } 
The deployment's environment no longer exists.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_environment_not_found_run_error.message)
type: "environment_not_found_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_environment_not_found_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_environment_not_found_run_error)
BetaManagedAgentsVaultNotFoundRunError object { message, type } 
A vault referenced by the deployment no longer exists.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_vault_not_found_run_error.message)
type: "vault_not_found_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_vault_not_found_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_vault_not_found_run_error)
BetaManagedAgentsVaultArchivedRunError object { message, type } 
A vault referenced by the deployment is archived.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_vault_archived_run_error.message)
type: "vault_archived_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_vault_archived_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_vault_archived_run_error)
BetaManagedAgentsFileNotFoundRunError object { message, type } 
A file resource referenced by the deployment no longer exists.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_file_not_found_run_error.message)
type: "file_not_found_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_file_not_found_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_file_not_found_run_error)
BetaManagedAgentsMemoryStoreArchivedRunError object { message, type } 
A memory store referenced by the deployment is archived.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_memory_store_archived_run_error.message)
type: "memory_store_archived_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_memory_store_archived_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_memory_store_archived_run_error)
BetaManagedAgentsSkillNotFoundRunError object { message, type } 
A skill referenced by the deployment's agent no longer exists.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_skill_not_found_run_error.message)
type: "skill_not_found_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_skill_not_found_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_skill_not_found_run_error)
BetaManagedAgentsSessionResourceNotFoundRunError object { message, type } 
A referenced resource no longer exists and its kind was not reported.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_session_resource_not_found_run_error.message)
type: "session_resource_not_found_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_session_resource_not_found_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_session_resource_not_found_run_error)
BetaManagedAgentsWorkspaceArchivedRunError object { message, type } 
The deployment's workspace was archived.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_workspace_archived_run_error.message)
type: "workspace_archived_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_workspace_archived_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_workspace_archived_run_error)
BetaManagedAgentsOrganizationDisabledRunError object { message, type } 
The deployment's organization is disabled.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_organization_disabled_run_error.message)
type: "organization_disabled_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_organization_disabled_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_organization_disabled_run_error)
BetaManagedAgentsSessionRateLimitedRunError object { message, type } 
Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_session_rate_limited_run_error.message)
type: "session_rate_limited_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_session_rate_limited_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_session_rate_limited_run_error)
BetaManagedAgentsSessionCreationRejectedRunError object { message, type } 
The session create request was rejected with a non-retryable validation error.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_session_creation_rejected_run_error.message)
type: "session_creation_rejected_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_session_creation_rejected_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_session_creation_rejected_run_error)
BetaManagedAgentsUnknownRunError object { message, type } 
An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_unknown_run_error.message)
type: "unknown_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_unknown_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_unknown_run_error)
BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object { message, type } 
The deployment configures resources, but its environment is self-hosted and cannot mount them.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_self_hosted_resources_unsupported_run_error.message)
type: "self_hosted_resources_unsupported_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_self_hosted_resources_unsupported_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_self_hosted_resources_unsupported_run_error)
BetaManagedAgentsMCPEgressBlockedRunError object { message, type } 
An MCP server host used by the deployment's agent is blocked by the environment's network policy.
message: string
Human-readable error description.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_mcp_egress_blocked_run_error.message)
type: "mcp_egress_blocked_error"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_mcp_egress_blocked_run_error.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_mcp_egress_blocked_run_error)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.error)
session_id: string
Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.session_id)
trigger_context: [BetaManagedAgentsTriggerContext](https://platform.claude.com/docs/en/api/beta#beta_managed_agents_trigger_context)
Describes what triggered a deployment run, with trigger-specific metadata.
BetaManagedAgentsScheduleTriggerContext object { scheduled_at, type } 
The run was fired by the deployment's cron schedule.
scheduled_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.trigger_context%20%2B%20\(resource\)%20beta.deployment_runs.scheduled_at)
type: "schedule"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.trigger_context%20%2B%20\(resource\)%20beta.deployment_runs.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.trigger_context%20%2B%20\(resource\)%20beta.deployment_runs)
BetaManagedAgentsManualTriggerContext object { type } 
The run was started manually by creating a session directly against the deployment.
type: "manual"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.trigger_context%20%2B%20\(resource\)%20beta.deployment_runs.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.trigger_context%20%2B%20\(resource\)%20beta.deployment_runs)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.trigger_context)
type: "deployment_run"
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run.type)
[](https://platform.claude.com/docs/en/api/beta/deployment_runs/retrieve#beta_managed_agents_deployment_run)
Get Deployment Run
cURL

curl https://api.anthropic.com/v1/deployment_runs/$DEPLOYMENT_RUN_ID \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  "type": "deployment_run"

  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  "type": "deployment_run"
