<!-- source: https://platform.claude.com/docs/en/managed-agents/webhooks -->

# Subscribe to webhooks
Get notified when major events happen without polling.
Sessions are long-running interactions. While most real-time interactions happen through the [SSE event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming), webhooks notify you of major state changes.
Webhook events return the event `type` and `id`, not the full object. When you receive a webhook event, you need to fetch the object directly with a `GET` call. This avoids delivering stale data on retries and keeps every delivery small.
Supported event types
Session events
Session events
Vault events
Vault events  
| Event  | Trigger  |  
| --- | --- |  
| `session.status_run_started`  | Agent execution kicked off. This triggers at every session status transition to `running`.  |  
| `session.status_idled`  | Agent awaiting input, for example a tool permission approval or a new user message.  |  
| `session.status_rescheduled`  | A transient error occurred and the session is retrying automatically.  |  
| `session.status_terminated`  | The session hit a terminal error.  |  
| `session.thread_created`  | New [multiagent thread](https://platform.claude.com/docs/en/managed-agents/multi-agent) opened, meaning an additional agent called by the coordinator is kicking off work.  |  
| `session.thread_idled`  | An agent in a [multiagent interaction](https://platform.claude.com/docs/en/managed-agents/multi-agent) is waiting for input.  |  
| `session.thread_terminated`  | A [multiagent thread](https://platform.claude.com/docs/en/managed-agents/multi-agent) was archived.  |  
| `session.outcome_evaluation_ended`  |  [Outcome evaluation](https://platform.claude.com/docs/en/managed-agents/define-outcomes) for a single iteration completed.  |  
| `session.updated`  | Session properties changed, for example its name or configuration was updated.  |  
| `session.deleted`  | Session permanently deleted. Unlike other events, there is no object left to fetch. Treat the event itself as final.  |  
Register an endpoint
Visit **Manage > Webhooks** in [Console](https://platform.claude.com/settings/workspaces/default/webhooks).
A webhook endpoint consists of:
  * **URL:** Must be HTTPS on port 443 with a publicly resolvable hostname.
  * **Event types:** The list of `data.type` values this endpoint receives. An endpoint only receives events it's subscribed to, plus test events (see [Delivery behavior](https://platform.claude.com/docs/en/managed-agents/webhooks#delivery-behavior)).
  * **Signing secret:** A 32-byte `whsec_`-prefixed secret generated at creation. It's shown only once, so store it securely to verify webhook deliveries.

Verify the signature
Every delivery carries an `X-Webhook-Signature` header. Use the SDK's `unwrap()` helper to verify the signature and parse the event in one step. It throws if the signature is invalid or the payload is more than five minutes old.
Set `ANTHROPIC_WEBHOOK_SIGNING_KEY` to the `whsec_`-prefixed secret shown at endpoint creation.
PythonTypeScriptC#GoJavaPHPRuby

from flask import Flask, request
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_WEBHOOK_SIGNING_KEY from env
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # unwrap() raises if the signature is invalid or the payload is stale
        event = client.beta.webhooks.unwrap(
            request.get_data(as_text=True),
            headers=dict(request.headers),
        )
    except Exception:
        return "invalid signature", 400

    if event.data.type == "session.status_idled":
        print("session idled:", event.data.id)
    # handle other event types

    return "", 200

Handle an event
Parse the body, switch on `data.type`, and fetch the resource by ID. Return any `2xx` to acknowledge. Anything else (including `3xx`) counts as a failure and triggers a retry.
Every event payload has the same structure, including the event type, identifier, and timestamp of when the object was created.

  "type": "event",
  "id": "event_01ABC...",
  "created_at": "2026-03-18T14:05:22Z",
  "data": {
    "type": "session.status_idled",
    "id": "sesn_01XYZ...",
    "organization_id": "8a3d2f1e-...",
    "workspace_id": "c7b0e4d9-..."

PythonTypeScriptC#GoJavaPHPRuby

if event.data.type == "session.status_idled":
    session = client.beta.sessions.retrieve(event.data.id)
    notify_user(session)
return "", 204

The top-level `event.id` is unique per event, not per delivery. If you receive the same `event.id` twice, it's a retry and you can discard it.
Delivery behavior
  * **Ordering is not guaranteed.** `session.status_idled` may arrive before `session.outcome_evaluation_ended` even if the outcome was produced first. Use the `created_at` timestamp to sort if ordering matters.
  * **Retries:** Anthropic retries at least once. The retry delivers the same `event.id`.
  * **Redirects are not followed.** A `3xx` is treated as a failure. If your endpoint moves, update the URL in Console.
  * **Auto-disable:** An endpoint is automatically set to `disabled` with a machine-readable `disabled_reason` after roughly 20 consecutive failed deliveries, or immediately if the hostname resolves to a private IP or the endpoint returns a redirect. Re-enable manually in Console after resolving the issue.

  * [Supported event types](https://platform.claude.com/docs/en/managed-agents/webhooks#supported-event-types)
  * [Register an endpoint](https://platform.claude.com/docs/en/managed-agents/webhooks#register-an-endpoint)
  * [Verify the signature](https://platform.claude.com/docs/en/managed-agents/webhooks#verify-the-signature)
  * [Handle an event](https://platform.claude.com/docs/en/managed-agents/webhooks#handle-an-event)
  * [Delivery behavior](https://platform.claude.com/docs/en/managed-agents/webhooks#delivery-behavior)

Managed Agents/Delegate work to your agent
# Subscribe to webhooks
Get notified when major events happen without polling.
Sessions are long-running interactions. While most real-time interactions happen through the [SSE event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming), webhooks notify you of major state changes.
Webhook events return the event `type` and `id`, not the full object. When you receive a webhook event, you need to fetch the object directly with a `GET` call. This avoids delivering stale data on retries and keeps every delivery small.
Supported event types
Session events
Session events
Vault events
Vault events  
| Event  | Trigger  |  
| --- | --- |  
| `session.status_run_started`  | Agent execution kicked off. This triggers at every session status transition to `running`.  |  
| `session.status_idled`  | Agent awaiting input, for example a tool permission approval or a new user message.  |  
| `session.status_rescheduled`  | A transient error occurred and the session is retrying automatically.  |  
| `session.status_terminated`  | The session hit a terminal error.  |  
| `session.thread_created`  | New [multiagent thread](https://platform.claude.com/docs/en/managed-agents/multi-agent) opened, meaning an additional agent called by the coordinator is kicking off work.  |  
| `session.thread_idled`  | An agent in a [multiagent interaction](https://platform.claude.com/docs/en/managed-agents/multi-agent) is waiting for input.  |  
| `session.thread_terminated`  | A [multiagent thread](https://platform.claude.com/docs/en/managed-agents/multi-agent) was archived.  |  
| `session.outcome_evaluation_ended`  |  [Outcome evaluation](https://platform.claude.com/docs/en/managed-agents/define-outcomes) for a single iteration completed.  |  
| `session.updated`  | Session properties changed, for example its name or configuration was updated.  |  
| `session.deleted`  | Session permanently deleted. Unlike other events, there is no object left to fetch. Treat the event itself as final.  |  
Register an endpoint
Visit **Manage > Webhooks** in [Console](https://platform.claude.com/settings/workspaces/default/webhooks).
A webhook endpoint consists of:
  * **URL:** Must be HTTPS on port 443 with a publicly resolvable hostname.
  * **Event types:** The list of `data.type` values this endpoint receives. An endpoint only receives events it's subscribed to, plus test events (see [Delivery behavior](https://platform.claude.com/docs/en/managed-agents/webhooks#delivery-behavior)).
  * **Signing secret:** A 32-byte `whsec_`-prefixed secret generated at creation. It's shown only once, so store it securely to verify webhook deliveries.

Verify the signature
Every delivery carries an `X-Webhook-Signature` header. Use the SDK's `unwrap()` helper to verify the signature and parse the event in one step. It throws if the signature is invalid or the payload is more than five minutes old.
Set `ANTHROPIC_WEBHOOK_SIGNING_KEY` to the `whsec_`-prefixed secret shown at endpoint creation.
PythonTypeScriptC#GoJavaPHPRuby

from flask import Flask, request
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_WEBHOOK_SIGNING_KEY from env
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # unwrap() raises if the signature is invalid or the payload is stale
        event = client.beta.webhooks.unwrap(
            request.get_data(as_text=True),
            headers=dict(request.headers),
        )
    except Exception:
        return "invalid signature", 400

    if event.data.type == "session.status_idled":
        print("session idled:", event.data.id)
    # handle other event types

    return "", 200

Handle an event
Parse the body, switch on `data.type`, and fetch the resource by ID. Return any `2xx` to acknowledge. Anything else (including `3xx`) counts as a failure and triggers a retry.
Every event payload has the same structure, including the event type, identifier, and timestamp of when the object was created.

  "type": "event",
  "id": "event_01ABC...",
  "created_at": "2026-03-18T14:05:22Z",
  "data": {
    "type": "session.status_idled",
    "id": "sesn_01XYZ...",
    "organization_id": "8a3d2f1e-...",
    "workspace_id": "c7b0e4d9-..."

PythonTypeScriptC#GoJavaPHPRuby

if event.data.type == "session.status_idled":
    session = client.beta.sessions.retrieve(event.data.id)
    notify_user(session)
return "", 204

The top-level `event.id` is unique per event, not per delivery. If you receive the same `event.id` twice, it's a retry and you can discard it.
Delivery behavior
  * **Ordering is not guaranteed.** `session.status_idled` may arrive before `session.outcome_evaluation_ended` even if the outcome was produced first. Use the `created_at` timestamp to sort if ordering matters.
  * **Retries:** Anthropic retries at least once. The retry delivers the same `event.id`.
  * **Redirects are not followed.** A `3xx` is treated as a failure. If your endpoint moves, update the URL in Console.
  * **Auto-disable:** An endpoint is automatically set to `disabled` with a machine-readable `disabled_reason` after roughly 20 consecutive failed deliveries, or immediately if the hostname resolves to a private IP or the endpoint returns a redirect. Re-enable manually in Console after resolving the issue.
