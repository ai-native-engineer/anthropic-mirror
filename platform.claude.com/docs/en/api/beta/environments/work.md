<!-- source: https://platform.claude.com/docs/en/api/beta/environments/work -->

# Work
##### [Get Work Item](https://platform.claude.com/docs/en/api/beta/environments/work/retrieve)
GET/v1/environments/{environment_id}/work/{work_id}
##### [Poll for Work](https://platform.claude.com/docs/en/api/beta/environments/work/poll)
GET/v1/environments/{environment_id}/work/poll
##### [Acknowledge Work](https://platform.claude.com/docs/en/api/beta/environments/work/ack)
POST/v1/environments/{environment_id}/work/{work_id}/ack
##### [Record Heartbeat](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat)
POST/v1/environments/{environment_id}/work/{work_id}/heartbeat
##### [Stop Work](https://platform.claude.com/docs/en/api/beta/environments/work/stop)
POST/v1/environments/{environment_id}/work/{work_id}/stop
##### [List Work Items](https://platform.claude.com/docs/en/api/beta/environments/work/list)
GET/v1/environments/{environment_id}/work
##### [Update Work Item](https://platform.claude.com/docs/en/api/beta/environments/work/update)
POST/v1/environments/{environment_id}/work/{work_id}
##### [Get Queue Statistics](https://platform.claude.com/docs/en/api/beta/environments/work/stats)
GET/v1/environments/{environment_id}/work/stats
##### ModelsExpand Collapse 
BetaSelfHostedWork object { id, acknowledged_at, created_at, 9 more } 
Work resource representing a unit of work in a self-hosted environment.
Work items are queued when sessions are created or when long-dormant sessions receive new messages. The environment worker polls for work to execute in a self-hosted sandbox.
Work identifier (e.g., 'work_...')
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.id)
acknowledged_at: string
RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.acknowledged_at)
created_at: string
RFC 3339 timestamp when work was created
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.created_at)
data: [BetaSessionWorkData](https://platform.claude.com/docs/en/api/beta#beta_session_work_data) { id, type } 
The actual work to be performed
Session identifier (e.g., 'session_...')
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.data%20%2B%20\(resource\)%20beta.environments.work.id)
type: "session"
Type of work data
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.data%20%2B%20\(resource\)%20beta.environments.work.type)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.data)
environment_id: string
Environment identifier this work belongs to (e.g., `env_...`)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.environment_id)
latest_heartbeat_at: string
RFC 3339 timestamp of the most recent heartbeat
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.latest_heartbeat_at)
metadata: map[string]
User-provided metadata key-value pairs associated with this work item
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.metadata)
started_at: string
RFC 3339 timestamp when work execution started
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.started_at)
state: "queued" or "starting" or "active" or 2 more
Current state of the work item
"queued"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state%5B0%5D)
"starting"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state%5B1%5D)
"active"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state%5B2%5D)
"stopping"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state%5B3%5D)
"stopped"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state%5B4%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state)
stop_requested_at: string
RFC 3339 timestamp when stop was requested
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.stop_requested_at)
stopped_at: string
RFC 3339 timestamp when work execution stopped
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.stopped_at)
type: "work"
The type of object (always 'work')
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.type)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work)
BetaSelfHostedWorkHeartbeatResponse object { last_heartbeat, lease_extended, state, 2 more } 
Response after recording a heartbeat for a work item.
last_heartbeat: string
RFC 3339 timestamp of the actual heartbeat from DB
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_heartbeat_response.last_heartbeat)
lease_extended: boolean
Whether the heartbeat succeeded in extending the lease
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_heartbeat_response.lease_extended)
state: "queued" or "starting" or "active" or 2 more
Current state of the work item (active/stopping/stopped)
"queued"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_heartbeat_response.state%5B0%5D)
"starting"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_heartbeat_response.state%5B1%5D)
"active"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_heartbeat_response.state%5B2%5D)
"stopping"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_heartbeat_response.state%5B3%5D)
"stopped"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_heartbeat_response.state%5B4%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_heartbeat_response.state)
ttl_seconds: number
Effective TTL applied to the lease
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_heartbeat_response.ttl_seconds)
type: "work_heartbeat"
The type of response
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_heartbeat_response.type)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_heartbeat_response)
BetaSelfHostedWorkListResponse object { data, next_page } 
Response when listing work items with cursor-based pagination.
data: array of [BetaSelfHostedWork](https://platform.claude.com/docs/en/api/beta#beta_self_hosted_work) { id, acknowledged_at, created_at, 9 more } 
List of work items
Work identifier (e.g., 'work_...')
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.id)
acknowledged_at: string
RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.acknowledged_at)
created_at: string
RFC 3339 timestamp when work was created
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.created_at)
data: [BetaSessionWorkData](https://platform.claude.com/docs/en/api/beta#beta_session_work_data) { id, type } 
The actual work to be performed
Session identifier (e.g., 'session_...')
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.data%20%2B%20\(resource\)%20beta.environments.work.id)
type: "session"
Type of work data
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.data%20%2B%20\(resource\)%20beta.environments.work.type)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.data)
environment_id: string
Environment identifier this work belongs to (e.g., `env_...`)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.environment_id)
latest_heartbeat_at: string
RFC 3339 timestamp of the most recent heartbeat
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.latest_heartbeat_at)
metadata: map[string]
User-provided metadata key-value pairs associated with this work item
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.metadata)
started_at: string
RFC 3339 timestamp when work execution started
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.started_at)
state: "queued" or "starting" or "active" or 2 more
Current state of the work item
"queued"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state%5B0%5D)
"starting"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state%5B1%5D)
"active"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state%5B2%5D)
"stopping"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state%5B3%5D)
"stopped"
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state%5B4%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.state)
stop_requested_at: string
RFC 3339 timestamp when stop was requested
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.stop_requested_at)
stopped_at: string
RFC 3339 timestamp when work execution stopped
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.stopped_at)
type: "work"
The type of object (always 'work')
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work.type)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_list_response.data)
next_page: string
Opaque cursor for fetching the next page of results
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_list_response.next_page)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_list_response)
BetaSelfHostedWorkQueueStats object { depth, oldest_queued_at, pending, 2 more } 
Statistics about the work queue for an environment.
Uses Redis Stream consumer group metrics for O(1) queries.
depth: number
Number of work items waiting to be picked up (lag from consumer group)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_queue_stats.depth)
oldest_queued_at: string
RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_queue_stats.oldest_queued_at)
pending: number
Number of work items being processed (polled but not acknowledged)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_queue_stats.pending)
type: "work_queue_stats"
The type of object
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_queue_stats.type)
workers_polling: number
Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_queue_stats.workers_polling)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_queue_stats)
BetaSelfHostedWorkStopRequest object { force } 
Request to stop a work item.
force: optional boolean
If true, immediately stop work without graceful shutdown
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_stop_request.force)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_stop_request)
BetaSelfHostedWorkUpdateRequest object { metadata } 
Request to update work item metadata.
metadata: map[string]
Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_update_request.metadata)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_self_hosted_work_update_request)
BetaSessionWorkData object { id, type } 
Work data for session work items.
This resource type is used when work represents a session that needs to be executed in a self-hosted environment.
Session identifier (e.g., 'session_...')
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_session_work_data.id)
type: "session"
Type of work data
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_session_work_data.type)
[](https://platform.claude.com/docs/en/api/beta/environments/work#beta_session_work_data)
