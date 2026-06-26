<!-- source: https://platform.claude.com/docs/en/api/beta/environments/work/poll -->

# Poll for Work
GET/v1/environments/{environment_id}/work/poll
Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.
Long poll for work items in the queue.
##### Path ParametersExpand Collapse 
environment_id: string
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#poll.environment_id)
##### Query ParametersExpand Collapse 
block_ms: optional number
How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#poll.block_ms)
reclaim_older_than_ms: optional number
Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#poll.reclaim_older_than_ms)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#poll.betas)
"Anthropic-Worker-ID": optional string
Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#poll.Anthropic-Worker-ID)
BetaSelfHostedWork object { id, acknowledged_at, created_at, 9 more } 
Work resource representing a unit of work in a self-hosted environment.
Work items are queued when sessions are created or when long-dormant sessions receive new messages. The environment worker polls for work to execute in a self-hosted sandbox.
Work identifier (e.g., 'work_...')
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.id)
acknowledged_at: string
RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.acknowledged_at)
created_at: string
RFC 3339 timestamp when work was created
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.created_at)
data: [BetaSessionWorkData](https://platform.claude.com/docs/en/api/beta#beta_session_work_data) { id, type } 
The actual work to be performed
Session identifier (e.g., 'session_...')
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.data%20%2B%20\(resource\)%20beta.environments.work.id)
type: "session"
Type of work data
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.data%20%2B%20\(resource\)%20beta.environments.work.type)
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.data)
environment_id: string
Environment identifier this work belongs to (e.g., `env_...`)
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.environment_id)
latest_heartbeat_at: string
RFC 3339 timestamp of the most recent heartbeat
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.latest_heartbeat_at)
metadata: map[string]
User-provided metadata key-value pairs associated with this work item
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.metadata)
started_at: string
RFC 3339 timestamp when work execution started
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.started_at)
state: "queued" or "starting" or "active" or 2 more
Current state of the work item
"queued"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.state%5B0%5D)
"starting"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.state%5B1%5D)
"active"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.state%5B2%5D)
"stopping"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.state%5B3%5D)
"stopped"
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.state%5B4%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.state)
stop_requested_at: string
RFC 3339 timestamp when stop was requested
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.stop_requested_at)
stopped_at: string
RFC 3339 timestamp when work execution stopped
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.stopped_at)
type: "work"
The type of object (always 'work')
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work.type)
[](https://platform.claude.com/docs/en/api/beta/environments/work/poll#beta_self_hosted_work)
Poll for Work
cURL

curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work/poll \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"

  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
