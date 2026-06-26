<!-- source: https://platform.claude.com/docs/en/managed-agents/scheduled-deployments -->

# Scheduled deployments
Run an agent on a recurring cron schedule and inspect its run history.
A **scheduled deployment** allows an [agent](https://platform.claude.com/docs/en/managed-agents/agent-setup) to kick off [sessions](https://platform.claude.com/docs/en/managed-agents/sessions) autonomously, enabling task completion over a predictable cadence.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Create a scheduled deployment
When creating a deployment, you pass the [session configurations](https://platform.claude.com/docs/en/managed-agents/sessions) required for execution, in addition to a `schedule`.
  * Deployments require [agent configuration](https://platform.claude.com/docs/en/managed-agents/agent-setup) and [environment configuration](https://platform.claude.com/docs/en/managed-agents/environments), and optionally accept [files](https://platform.claude.com/docs/en/managed-agents/files), [GitHub](https://platform.claude.com/docs/en/managed-agents/github), [memory stores](https://platform.claude.com/docs/en/managed-agents/memory), and [vaults](https://platform.claude.com/docs/en/managed-agents/vaults).
  * Deployments also require an initial `user.message` event that starts the session's work.
  * In the `schedule`, you define a cron `expression` and a `timezone`. Maximum granularity supported is at the minute level.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

DEPLOYMENT_ID=$(ant beta:deployments create <<YAML | jq -er '.id'
name: Weekly compliance scan
agent: $AGENT_ID
environment_id: $ENVIRONMENT_ID
initial_events:
  - type: user.message
    content:
      - type: text
        text: Run the weekly compliance scan.
schedule:
  type: cron
  expression: "0 20 * * 5"
  timezone: America/New_York
YAML
)

The response includes a deployment object with a populated `schedule.upcoming_runs_at` with the next upcoming fire times, to confirm your schedule was set correctly.

  "id": "depl_01xyz",
  "status": "active",
  "paused_reason": null,
  "schedule": {
    "type": "cron",
    "expression": "0 20 * * 5",
    "timezone": "America/New_York",
    "last_run_at": null,
    "upcoming_runs_at": [
      "2026-05-09T00:00:00Z",
      "2026-05-16T00:00:00Z",
      "2026-05-23T00:00:00Z"
    ]

The upcoming run timestamps are based on the exact schedule configured. However, to distribute load, deployments may apply jitter of up to 10 seconds.
A maximum of **1,000 scheduled deployments** is supported per organization. Contact Anthropic support if you need more.
### 
Cron and timezone semantics
  * **Expression:** Standard POSIX cron (`minute hour day-of-month month day-of-week`). You can generate and validate these cron expressions in the [Claude Console](https://platform.claude.com/workspaces/default/deployments).
  * **Timezone:** IANA timezone identifier (for example, `"America/Los_Angeles"`).
  * **DST:** Cron schedules use literal wall-clock matching, so `"0 20 * * *"` in `America/New_York` fires at 8
PM local time regardless of whether EST or EDT is in effect.

Wall-clock times that do not exist on a spring-forward day (such as 2 AM) are not triggered. Wall-clock times that occur twice on a fall-back day fire twice. Schedule outside the 1–3 AM local window, or use UTC, when missed or duplicate executions are unacceptable.
Deployment runs
Deployments can fail to trigger for a variety of reasons: for example, if the `environment` resource has been archived, or if session creation is rate-limited. Each attempt at executing a deployment generates a **deployment run** record, allowing you to track successes and failures independent of the session lifecycle.
Successful deployments generate active sessions, and a successful deployment run contains the associated `session_id`. To follow a session's lifecycle, track the session events through the [event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) or [webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks).
List all deployment runs for a deployment as follows:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployment-runs list --deployment-id "$DEPLOYMENT_ID"

You can additionally filter on deployment runs with errors:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployment-runs list --deployment-id "$DEPLOYMENT_ID" --has-error

A failed run includes an `error` with a `type` describing why session creation was rejected (for example, `environment_archived_error`, `agent_archived_error`, or `session_rate_limited_error`).

  "type": "deployment_run",
  "id": "drun_01abc124",
  "deployment_id": "depl_01xyz",
  "trigger_context": { "type": "schedule", "scheduled_at": "2026-05-09T00:00:00Z" },
  "session_id": null,
  "error": {
    "type": "environment_archived_error",
    "message": "environment `env_01abc` is archived"
  "agent": { "type": "agent", "id": "agent_01ghi789", "version": 3 },
  "created_at": "2026-05-09T00:00:01Z"

Managing deployment lifecycle
**Pause** suppresses scheduled triggers on a go-forward basis; running sessions from a prior deployment run continue to execute. Manual runs through the `run` endpoint are still allowed while paused. Pausing sets `paused_reason` to `{"type": "manual"}`; unpausing clears it.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployments pause --deployment-id "$DEPLOYMENT_ID"

**Unpause** resumes the schedule from the next scheduled occurrence. Missed triggers are not backfilled.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployments unpause --deployment-id "$DEPLOYMENT_ID"

**Archive** , unlike **pause** , is terminal: the schedule terminates and the deployment cannot be modified.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployments archive --deployment-id "$DEPLOYMENT_ID"

### 
Failure behavior
Session creation rate-limit responses are recorded immediately as a `session_rate_limited_error` run without retry; the schedule attempts again at the next scheduled occurrence. Rate limits on underlying API calls within a session are handled by the session itself.
If a deployment's agent has been archived or deleted, the deployment is automatically archived in the same operation; no deployment run is recorded. If a subagent referenced by the agent has been archived, the next trigger records a failed run with `error.type: "agent_archived_error"` and the deployment is automatically paused so you can update the agent and resume.
Trigger a manual run
To run a deployment outside its schedule, call the `run` endpoint. This creates a session immediately and writes a deployment run with `trigger_context.type: "manual"`. This allows you to test a deployment before committing to the schedule.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployments run --deployment-id "$DEPLOYMENT_ID"

  * [Create a scheduled deployment](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments#create-a-scheduled-deployment)
  * [Cron and timezone semantics](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments#cron-and-timezone-semantics)
  * [Deployment runs](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments#deployment-runs)
  * [Managing deployment lifecycle](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments#managing-deployment-lifecycle)
  * [Failure behavior](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments#failure-behavior)
  * [Trigger a manual run](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments#trigger-a-manual-run)

Managed Agents/Advanced orchestration
# Scheduled deployments
Run an agent on a recurring cron schedule and inspect its run history.
A **scheduled deployment** allows an [agent](https://platform.claude.com/docs/en/managed-agents/agent-setup) to kick off [sessions](https://platform.claude.com/docs/en/managed-agents/sessions) autonomously, enabling task completion over a predictable cadence.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Create a scheduled deployment
When creating a deployment, you pass the [session configurations](https://platform.claude.com/docs/en/managed-agents/sessions) required for execution, in addition to a `schedule`.
  * Deployments require [agent configuration](https://platform.claude.com/docs/en/managed-agents/agent-setup) and [environment configuration](https://platform.claude.com/docs/en/managed-agents/environments), and optionally accept [files](https://platform.claude.com/docs/en/managed-agents/files), [GitHub](https://platform.claude.com/docs/en/managed-agents/github), [memory stores](https://platform.claude.com/docs/en/managed-agents/memory), and [vaults](https://platform.claude.com/docs/en/managed-agents/vaults).
  * Deployments also require an initial `user.message` event that starts the session's work.
  * In the `schedule`, you define a cron `expression` and a `timezone`. Maximum granularity supported is at the minute level.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

DEPLOYMENT_ID=$(ant beta:deployments create <<YAML | jq -er '.id'
name: Weekly compliance scan
agent: $AGENT_ID
environment_id: $ENVIRONMENT_ID
initial_events:
  - type: user.message
    content:
      - type: text
        text: Run the weekly compliance scan.
schedule:
  type: cron
  expression: "0 20 * * 5"
  timezone: America/New_York
YAML
)

The response includes a deployment object with a populated `schedule.upcoming_runs_at` with the next upcoming fire times, to confirm your schedule was set correctly.

  "id": "depl_01xyz",
  "status": "active",
  "paused_reason": null,
  "schedule": {
    "type": "cron",
    "expression": "0 20 * * 5",
    "timezone": "America/New_York",
    "last_run_at": null,
    "upcoming_runs_at": [
      "2026-05-09T00:00:00Z",
      "2026-05-16T00:00:00Z",
      "2026-05-23T00:00:00Z"
    ]

The upcoming run timestamps are based on the exact schedule configured. However, to distribute load, deployments may apply jitter of up to 10 seconds.
A maximum of **1,000 scheduled deployments** is supported per organization. Contact Anthropic support if you need more.
### 
Cron and timezone semantics
  * **Expression:** Standard POSIX cron (`minute hour day-of-month month day-of-week`). You can generate and validate these cron expressions in the [Claude Console](https://platform.claude.com/workspaces/default/deployments).
  * **Timezone:** IANA timezone identifier (for example, `"America/Los_Angeles"`).
  * **DST:** Cron schedules use literal wall-clock matching, so `"0 20 * * *"` in `America/New_York` fires at 8
PM local time regardless of whether EST or EDT is in effect.

Wall-clock times that do not exist on a spring-forward day (such as 2 AM) are not triggered. Wall-clock times that occur twice on a fall-back day fire twice. Schedule outside the 1–3 AM local window, or use UTC, when missed or duplicate executions are unacceptable.
Deployment runs
Deployments can fail to trigger for a variety of reasons: for example, if the `environment` resource has been archived, or if session creation is rate-limited. Each attempt at executing a deployment generates a **deployment run** record, allowing you to track successes and failures independent of the session lifecycle.
Successful deployments generate active sessions, and a successful deployment run contains the associated `session_id`. To follow a session's lifecycle, track the session events through the [event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) or [webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks).
List all deployment runs for a deployment as follows:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployment-runs list --deployment-id "$DEPLOYMENT_ID"

You can additionally filter on deployment runs with errors:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployment-runs list --deployment-id "$DEPLOYMENT_ID" --has-error

A failed run includes an `error` with a `type` describing why session creation was rejected (for example, `environment_archived_error`, `agent_archived_error`, or `session_rate_limited_error`).

  "type": "deployment_run",
  "id": "drun_01abc124",
  "deployment_id": "depl_01xyz",
  "trigger_context": { "type": "schedule", "scheduled_at": "2026-05-09T00:00:00Z" },
  "session_id": null,
  "error": {
    "type": "environment_archived_error",
    "message": "environment `env_01abc` is archived"
  "agent": { "type": "agent", "id": "agent_01ghi789", "version": 3 },
  "created_at": "2026-05-09T00:00:01Z"

Managing deployment lifecycle
**Pause** suppresses scheduled triggers on a go-forward basis; running sessions from a prior deployment run continue to execute. Manual runs through the `run` endpoint are still allowed while paused. Pausing sets `paused_reason` to `{"type": "manual"}`; unpausing clears it.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployments pause --deployment-id "$DEPLOYMENT_ID"

**Unpause** resumes the schedule from the next scheduled occurrence. Missed triggers are not backfilled.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployments unpause --deployment-id "$DEPLOYMENT_ID"

**Archive** , unlike **pause** , is terminal: the schedule terminates and the deployment cannot be modified.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployments archive --deployment-id "$DEPLOYMENT_ID"

### 
Failure behavior
Session creation rate-limit responses are recorded immediately as a `session_rate_limited_error` run without retry; the schedule attempts again at the next scheduled occurrence. Rate limits on underlying API calls within a session are handled by the session itself.
If a deployment's agent has been archived or deleted, the deployment is automatically archived in the same operation; no deployment run is recorded. If a subagent referenced by the agent has been archived, the next trigger records a failed run with `error.type: "agent_archived_error"` and the deployment is automatically paused so you can update the agent and resume.
Trigger a manual run
To run a deployment outside its schedule, call the `run` endpoint. This creates a session immediately and writes a deployment run with `trigger_context.type: "manual"`. This allows you to test a deployment before committing to the schedule.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:deployments run --deployment-id "$DEPLOYMENT_ID"
