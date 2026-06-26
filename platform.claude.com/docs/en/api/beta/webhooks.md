<!-- source: https://platform.claude.com/docs/en/api/beta/webhooks -->

# Webhooks
Helpers for receiving and verifying webhook events. Use `unwrap` in your SDK to verify signatures and parse payloads; see the [webhooks guide](https://platform.claude.com/docs/en/managed-agents/webhooks) for handler examples.
Possible `data.type` values:
  * `session.archived`
  * `session.created`
  * `session.deleted`
  * `session.idled`
  * `session.outcome_evaluation_ended`
  * `session.pending`
  * `session.requires_action`
  * `session.running`
  * `session.status_idled`
  * `session.status_rescheduled`
  * `session.status_run_started`
  * `session.status_terminated`
  * `session.thread_created`
  * `session.thread_idled`
  * `session.thread_terminated`
  * `session.updated`
  * `vault.archived`
  * `vault.created`
  * `vault.deleted`
  * `vault_credential.archived`
  * `vault_credential.created`
  * `vault_credential.deleted`
  * `vault_credential.refresh_failed`

##### ModelsExpand Collapse 
BetaWebhookEvent object { id, created_at, data, type } 
Unique event identifier for idempotency.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.id)
created_at: string
RFC 3339 timestamp when the event occurred.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.created_at)
data: [BetaWebhookEventData](https://platform.claude.com/docs/en/api/beta#beta_webhook_event_data)
BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.pending"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.running"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.requires_action"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.status_rescheduled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.status_run_started"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.status_idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.status_terminated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.session_thread_id)
type: "session.thread_created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.session_thread_id)
type: "session.thread_idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.session_thread_id)
type: "session.thread_terminated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.outcome_evaluation_ended"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault_credential.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault_credential.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault_credential.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault_credential.refresh_failed"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.updated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.data)
type: "event"
Object type. Always `event` for webhook payloads.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event.type)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event)
BetaWebhookEventData = [BetaWebhookSessionCreatedEventData](https://platform.claude.com/docs/en/api/beta#beta_webhook_session_created_event_data) { id, organization_id, type, workspace_id }  or [BetaWebhookSessionPendingEventData](https://platform.claude.com/docs/en/api/beta#beta_webhook_session_pending_event_data) { id, organization_id, type, workspace_id }  or [BetaWebhookSessionRunningEventData](https://platform.claude.com/docs/en/api/beta#beta_webhook_session_running_event_data) { id, organization_id, type, workspace_id }  or 20 more
BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_created_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_created_event_data.organization_id)
type: "session.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_created_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_created_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_created_event_data)
BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_pending_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_pending_event_data.organization_id)
type: "session.pending"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_pending_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_pending_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_pending_event_data)
BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_running_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_running_event_data.organization_id)
type: "session.running"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_running_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_running_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_running_event_data)
BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_idled_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_idled_event_data.organization_id)
type: "session.idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_idled_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_idled_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_idled_event_data)
BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_requires_action_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_requires_action_event_data.organization_id)
type: "session.requires_action"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_requires_action_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_requires_action_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_requires_action_event_data)
BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_archived_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_archived_event_data.organization_id)
type: "session.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_archived_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_archived_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_archived_event_data)
BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_deleted_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_deleted_event_data.organization_id)
type: "session.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_deleted_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_deleted_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_deleted_event_data)
BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_rescheduled_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_rescheduled_event_data.organization_id)
type: "session.status_rescheduled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_rescheduled_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_rescheduled_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_rescheduled_event_data)
BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_run_started_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_run_started_event_data.organization_id)
type: "session.status_run_started"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_run_started_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_run_started_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_run_started_event_data)
BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_idled_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_idled_event_data.organization_id)
type: "session.status_idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_idled_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_idled_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_idled_event_data)
BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_terminated_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_terminated_event_data.organization_id)
type: "session.status_terminated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_terminated_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_terminated_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_terminated_event_data)
BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data.session_thread_id)
type: "session.thread_created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data)
BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data.session_thread_id)
type: "session.thread_idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data)
BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data.session_thread_id)
type: "session.thread_terminated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data)
BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_outcome_evaluation_ended_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_outcome_evaluation_ended_event_data.organization_id)
type: "session.outcome_evaluation_ended"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_outcome_evaluation_ended_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_outcome_evaluation_ended_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_outcome_evaluation_ended_event_data)
BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_created_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_created_event_data.organization_id)
type: "vault.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_created_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_created_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_created_event_data)
BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_archived_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_archived_event_data.organization_id)
type: "vault.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_archived_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_archived_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_archived_event_data)
BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_deleted_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_deleted_event_data.organization_id)
type: "vault.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_deleted_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_deleted_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_deleted_event_data)
BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data.organization_id)
type: "vault_credential.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data)
BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data.organization_id)
type: "vault_credential.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data)
BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data.organization_id)
type: "vault_credential.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data)
BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data.organization_id)
type: "vault_credential.refresh_failed"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data)
BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_updated_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_updated_event_data.organization_id)
type: "session.updated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_updated_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_updated_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_updated_event_data)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_event_data)
BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_archived_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_archived_event_data.organization_id)
type: "session.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_archived_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_archived_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_archived_event_data)
BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_created_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_created_event_data.organization_id)
type: "session.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_created_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_created_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_created_event_data)
BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_deleted_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_deleted_event_data.organization_id)
type: "session.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_deleted_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_deleted_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_deleted_event_data)
BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_idled_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_idled_event_data.organization_id)
type: "session.idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_idled_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_idled_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_idled_event_data)
BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_outcome_evaluation_ended_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_outcome_evaluation_ended_event_data.organization_id)
type: "session.outcome_evaluation_ended"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_outcome_evaluation_ended_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_outcome_evaluation_ended_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_outcome_evaluation_ended_event_data)
BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_pending_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_pending_event_data.organization_id)
type: "session.pending"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_pending_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_pending_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_pending_event_data)
BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_requires_action_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_requires_action_event_data.organization_id)
type: "session.requires_action"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_requires_action_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_requires_action_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_requires_action_event_data)
BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_running_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_running_event_data.organization_id)
type: "session.running"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_running_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_running_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_running_event_data)
BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_idled_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_idled_event_data.organization_id)
type: "session.status_idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_idled_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_idled_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_idled_event_data)
BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_rescheduled_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_rescheduled_event_data.organization_id)
type: "session.status_rescheduled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_rescheduled_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_rescheduled_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_rescheduled_event_data)
BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_run_started_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_run_started_event_data.organization_id)
type: "session.status_run_started"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_run_started_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_run_started_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_run_started_event_data)
BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_terminated_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_terminated_event_data.organization_id)
type: "session.status_terminated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_terminated_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_terminated_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_status_terminated_event_data)
BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data.session_thread_id)
type: "session.thread_created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_created_event_data)
BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data.session_thread_id)
type: "session.thread_idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_idled_event_data)
BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data.session_thread_id)
type: "session.thread_terminated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_thread_terminated_event_data)
BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_updated_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_updated_event_data.organization_id)
type: "session.updated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_updated_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_updated_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_session_updated_event_data)
BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_archived_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_archived_event_data.organization_id)
type: "vault.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_archived_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_archived_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_archived_event_data)
BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_created_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_created_event_data.organization_id)
type: "vault.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_created_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_created_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_created_event_data)
BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data.organization_id)
type: "vault_credential.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_archived_event_data)
BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data.organization_id)
type: "vault_credential.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_created_event_data)
BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data.organization_id)
type: "vault_credential.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_deleted_event_data)
BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data.organization_id)
type: "vault_credential.refresh_failed"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_credential_refresh_failed_event_data)
BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_deleted_event_data.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_deleted_event_data.organization_id)
type: "vault.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_deleted_event_data.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_deleted_event_data.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#beta_webhook_vault_deleted_event_data)
UnwrapWebhookEvent object { id, created_at, data, type } 
Unique event identifier for idempotency.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.id)
created_at: string
RFC 3339 timestamp when the event occurred.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.created_at)
data: [BetaWebhookEventData](https://platform.claude.com/docs/en/api/beta#beta_webhook_event_data)
BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.pending"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.running"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.requires_action"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.status_rescheduled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.status_run_started"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.status_idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.status_terminated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.session_thread_id)
type: "session.thread_created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.session_thread_id)
type: "session.thread_idled"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
session_thread_id: string
ID of the session thread this event refers to.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.session_thread_id)
type: "session.thread_terminated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.outcome_evaluation_ended"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id } 
ID of the vault that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault_credential.created"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault_credential.archived"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault_credential.deleted"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more } 
ID of the vault credential that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "vault_credential.refresh_failed"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
vault_id: string
ID of the vault that owns this credential.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.vault_id)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id } 
ID of the session that triggered the event.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.id)
organization_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.organization_id)
type: "session.updated"
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.type)
workspace_id: string
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks.workspace_id)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data%20%2B%20\(resource\)%20beta.webhooks)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.data)
type: "event"
Object type. Always `event` for webhook payloads.
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event.type)
[](https://platform.claude.com/docs/en/api/beta/webhooks#unwrap_webhook_event)
