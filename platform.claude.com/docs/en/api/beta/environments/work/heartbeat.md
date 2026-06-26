<!-- source: https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat -->

# Record Heartbeat
POST/v1/environments/{environment_id}/work/{work_id}/heartbeat
Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.
Record a heartbeat for a work item to maintain the lease.
##### Path ParametersExpand Collapse 
environment_id: string
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#heartbeat.environment_id)
work_id: string
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#heartbeat.work_id)
##### Query ParametersExpand Collapse 
desired_ttl_seconds: optional number
Desired TTL in seconds
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#heartbeat.desired_ttl_seconds)
expected_last_heartbeat: optional string
Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#heartbeat.expected_last_heartbeat)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#heartbeat.betas)
BetaSelfHostedWorkHeartbeatResponse object { last_heartbeat, lease_extended, state, 2 more } 
Response after recording a heartbeat for a work item.
last_heartbeat: string
RFC 3339 timestamp of the actual heartbeat from DB
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#beta_self_hosted_work_heartbeat_response.last_heartbeat)
lease_extended: boolean
Whether the heartbeat succeeded in extending the lease
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#beta_self_hosted_work_heartbeat_response.lease_extended)
state: "queued" or "starting" or "active" or 2 more
Current state of the work item (active/stopping/stopped)
"queued"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#beta_self_hosted_work_heartbeat_response.state%5B0%5D)
"starting"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#beta_self_hosted_work_heartbeat_response.state%5B1%5D)
"active"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#beta_self_hosted_work_heartbeat_response.state%5B2%5D)
"stopping"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#beta_self_hosted_work_heartbeat_response.state%5B3%5D)
"stopped"
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#beta_self_hosted_work_heartbeat_response.state%5B4%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#beta_self_hosted_work_heartbeat_response.state)
ttl_seconds: number
Effective TTL applied to the lease
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#beta_self_hosted_work_heartbeat_response.ttl_seconds)
type: "work_heartbeat"
The type of response
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#beta_self_hosted_work_heartbeat_response.type)
[](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat#beta_self_hosted_work_heartbeat_response)
Record Heartbeat
cURL

curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID/work/$WORK_ID/heartbeat \
    -X POST \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"

  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
